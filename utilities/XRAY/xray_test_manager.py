"""
Gestor de Test Issues en XRay / Jira Cloud.
Busca, crea y actualiza Test Issues, y etiqueta los archivos feature.
"""

import os
import re

import requests

import xray_auth_service as auth
import xray_config as config
from xray_http import TIMEOUT_SEGUNDOS, advertir, datos, mensaje_error, verificar

PREFIJOS_ESCENARIO = ("Escenario:", "Scenario:", "Esquema del escenario:", "Scenario Outline:")
PATRON_PREFIJO_ESCENARIO = re.compile(r"^(Esquema del escenario|Scenario Outline|Escenario|Scenario):\s*")

# Etiqueta opcional que vincula el escenario con su Historia de Usuario: @related:QA-45
PATRON_TAG_HISTORIA = re.compile(r"^@related:(.+)$", re.IGNORECASE)


def js_trim(texto):
    """Equivalente a String.prototype.trim de JavaScript (incluye BOM)."""
    return texto.strip().strip("\ufeff").strip()


def es_cabecera_escenario(linea_trim):
    return linea_trim.startswith(PREFIJOS_ESCENARIO)


def nombre_escenario(linea_trim):
    return js_trim(PATRON_PREFIJO_ESCENARIO.sub("", linea_trim, count=1))


def _patron_clave(project_key, con_arroba):
    prefijo = "@" if con_arroba else ""
    return re.compile(rf"^{prefijo}{re.escape(project_key or '')}-[0-9]+$")


def patron_tag_xray():
    """Patron de etiqueta XRay de un escenario (ej: @QA-12)."""
    return _patron_clave(config.jira.projectKey, True)


def _get_jira(url, **kwargs):
    return verificar(requests.get(url, headers=auth.obtener_headers_jira(), timeout=TIMEOUT_SEGUNDOS, **kwargs))


def _put_jira(url, cuerpo):
    return verificar(requests.put(url, json=cuerpo, headers=auth.obtener_headers_jira(), timeout=TIMEOUT_SEGUNDOS))


def buscar_test_por_nombre(nombre_escenario_buscado):
    """Busca una Test Issue en Jira por nombre de escenario (coincidencia exacta)."""
    nombre_escapado = nombre_escenario_buscado.replace('"', '\\"')
    jql = (
        f'project = "{config.jira.projectKey}" AND issuetype = Test '
        f'AND summary ~ "{nombre_escapado}" ORDER BY created DESC'
    )

    respuesta = _get_jira(
        f"{config.jira.baseUrl}/rest/api/3/search/jql",
        params={"jql": jql, "maxResults": 10, "fields": "summary"},
    )

    issues = datos(respuesta).get("issues") or []
    for issue in issues:
        if issue["fields"]["summary"] == nombre_escenario_buscado:
            return issue
    return None


def importar_feature(ruta_feature):
    """
    Importa un archivo feature completo a XRay creando un Test Cucumber por cada escenario.
    Devuelve la respuesta completa de XRay con updatedOrCreatedTests.
    """
    nombre_archivo = os.path.basename(ruta_feature)
    print(f"Importando feature a XRay: {nombre_archivo}...")

    token = auth.obtener_token()
    with open(ruta_feature, "rb") as flujo:
        respuesta = verificar(requests.post(
            f"{config.xray.baseUrl}/api/v2/import/feature",
            params={"projectKey": config.jira.projectKey},
            files={"file": (nombre_archivo, flujo, "text/plain")},
            headers={"Authorization": f"Bearer {token}"},
            timeout=TIMEOUT_SEGUNDOS,
        ))

    cuerpo = datos(respuesta)
    tests = cuerpo.get("updatedOrCreatedTests") or []
    errores = cuerpo.get("errors") or []

    if len(errores) > 0:
        advertir(f"Advertencias al importar feature: {', '.join(str(e) for e in errores)}")
    print(f"Feature importado: {len(tests)} tests creados/actualizados.")
    return cuerpo


def actualizar_gherkin(issue_id, contenido_gherkin):
    """Actualiza el contenido Gherkin de un Test Issue en XRay (ID numerico de la issue)."""
    headers = auth.obtener_headers_xray()
    headers["Content-Type"] = "text/plain"
    verificar(requests.put(
        f"{config.xray.baseUrl}{config.xray.testEndpoint}/{issue_id}/gherkin",
        data=contenido_gherkin.encode("utf-8"),
        headers=headers,
        timeout=TIMEOUT_SEGUNDOS,
    ))


def obtener_gherkin(issue_id):
    """Obtiene el Gherkin actual de un Test Issue en XRay."""
    try:
        headers = auth.obtener_headers_xray()
        respuesta = verificar(requests.get(
            f"{config.xray.baseUrl}{config.xray.testEndpoint}/{issue_id}/gherkin",
            headers=headers,
            timeout=TIMEOUT_SEGUNDOS,
        ))
        return datos(respuesta) or ""
    except Exception:
        return ""


def etiquetar_escenario(ruta_feature, nombre_escenario_buscado, clave_issue):
    """
    Añade la etiqueta @PROYECTO-X al escenario en el archivo feature.
    Respeta las etiquetas funcionales ya existentes.
    """
    # newline="" conserva los saltos de linea originales (CRLF/LF) del archivo
    with open(ruta_feature, "r", encoding="utf-8", newline="") as flujo:
        contenido = flujo.read()
    lineas = contenido.split("\n")
    etiqueta = f"@{clave_issue}"

    for i in range(len(lineas)):
        trim = js_trim(lineas[i])
        if es_cabecera_escenario(trim):
            # Comparacion exacta para evitar que "Login" matchee "Login con error"
            if nombre_escenario(trim) != nombre_escenario_buscado:
                continue
            ya_etiquetado = any(etiqueta in l for l in lineas[max(0, i - 5):i])
            if not ya_etiquetado:
                indentacion = re.match(r"^(\s*)", lineas[i]).group(1)
                # Si el archivo usa CRLF, la linea insertada debe terminar tambien en \r
                fin_linea = "\r" if lineas[i].endswith("\r") else ""
                lineas.insert(i, f"{indentacion.rstrip(chr(13))}{etiqueta}{fin_linea}")
                with open(ruta_feature, "w", encoding="utf-8", newline="") as flujo:
                    flujo.write("\n".join(lineas))
                print(f'Etiqueta {etiqueta} añadida a "{nombre_escenario_buscado}"')
            break


def actualizar_descripcion(clave_issue, tags_escenario, gherkin):
    """
    Actualiza la descripcion de una Test Issue en Jira con el contenido completo del escenario.
    El contenido incluye las etiquetas funcionales, la clave XRay y todos los pasos Gherkin.
    """
    # Separar tags funcionales de la etiqueta XRay para no duplicarla en la descripcion
    patron_xray = patron_tag_xray()
    tags_funcionales = [t for t in tags_escenario if not patron_xray.match(t)]
    tags_linea = " ".join([*tags_funcionales, f"@{clave_issue}"])

    # Incluir linea de tags + lineas del escenario, descartando lineas vacias (ADF no acepta texto vacio)
    lineas = [l.rstrip() for l in [tags_linea, *gherkin.split("\n")]]
    lineas = [l for l in lineas if len(js_trim(l)) > 0]

    contenido_adf = [
        {"type": "paragraph", "content": [{"type": "text", "text": linea}]}
        for linea in lineas
    ]

    _put_jira(
        f"{config.jira.baseUrl}/rest/api/3/issue/{clave_issue}",
        {"fields": {"description": {"type": "doc", "version": 1, "content": contenido_adf}}},
    )


def obtener_estado_jira(claves):
    """
    Obtiene el estado actual de un lote de Test Issues desde Jira.
    Usa JQL "key in (...)" en batches de 50 para minimizar llamadas a la API.
    Devuelve un mapa { 'QA-330': { summary, labels, gherkin } }.
    """
    if not claves:
        return {}

    resultado = {}
    BATCH_SIZE = 50

    for i in range(0, len(claves), BATCH_SIZE):
        lote = claves[i:i + BATCH_SIZE]
        jql = f"key in ({','.join(lote)})"
        try:
            respuesta = _get_jira(
                f"{config.jira.baseUrl}/rest/api/3/search/jql",
                params={"jql": jql, "maxResults": BATCH_SIZE, "fields": "summary,labels,description"},
            )
            for issue in datos(respuesta).get("issues") or []:
                # Extraer el Gherkin de la descripcion ADF descartando la primera linea (linea de tags)
                desc = issue["fields"].get("description")
                bloques = desc["content"] if desc and desc.get("content") else []
                parrafos = [
                    "".join((n.get("text") or "") for n in b["content"]) if b.get("content") else ""
                    for b in bloques
                ]
                parrafos = [t for t in parrafos if len(js_trim(t)) > 0]
                resultado[issue["key"]] = {
                    "summary": issue["fields"].get("summary") or "",
                    "labels": issue["fields"].get("labels") or [],
                    "gherkin": "\n".join(parrafos[1:]),
                }
        except Exception as error:
            advertir(f"Error consultando estado de Jira: {mensaje_error(error)}")
    return resultado


def actualizar_summary(clave_issue, nuevo_nombre):
    """Actualiza el nombre (summary) de una Test Issue en Jira."""
    _put_jira(
        f"{config.jira.baseUrl}/rest/api/3/issue/{clave_issue}",
        {"fields": {"summary": nuevo_nombre}},
    )


def actualizar_labels(clave_issue, tags_funcionales, labels_existentes=None):
    """
    Actualiza las labels (etiquetas funcionales) de una Test Issue en Jira.
    Convierte los tags del feature (ej: ['@smoke']) en labels de Jira (ej: ['smoke']).
    Excluye automaticamente @QA-X, @pendiente y @pending.
    """
    excluidas = {"pendiente", "pending"}
    patron_xray = _patron_clave(config.jira.projectKey, False)
    # Preservar labels internas de XRay (QA-XXX) que gestiona XRay internamente
    labels_internas = [l for l in (labels_existentes or []) if patron_xray.match(l)]
    labels_funcionales = []
    for t in tags_funcionales:
        if PATRON_TAG_HISTORIA.match(t):
            continue
        t = re.sub(r"^@", "", t, count=1)
        if t in excluidas or patron_xray.match(t):
            continue
        labels_funcionales.append(t)
    labels = list(dict.fromkeys([*labels_internas, *labels_funcionales]))
    _put_jira(
        f"{config.jira.baseUrl}/rest/api/3/issue/{clave_issue}",
        {"fields": {"labels": labels}},
    )


def _nombre_tag(tag):
    return tag if isinstance(tag, str) else tag["name"]


def extraer_clave_jira(tags, project_key):
    """
    Extrae la clave Jira de un array de tags del escenario.
    Acepta strings o diccionarios con la clave "name". Devuelve (ej: QA-1) o None.
    """
    patron = _patron_clave(project_key, True)
    for t in tags:
        nombre = _nombre_tag(t)
        if patron.match(nombre):
            return nombre.replace("@", "", 1)
    return None


def extraer_clave_historia(tags):
    """
    Extrae la clave de la Historia de Usuario del tag opcional @related:ID.
    Devuelve None si el escenario no lleva esa etiqueta (caso normal, sin vinculo).
    """
    for t in tags:
        coincidencia = PATRON_TAG_HISTORIA.match(_nombre_tag(t))
        if coincidencia:
            return js_trim(coincidencia.group(1))
    return None


def obtener_enlaces(clave_issue):
    """Obtiene los issue links existentes de una issue de Jira."""
    respuesta = _get_jira(
        f"{config.jira.baseUrl}/rest/api/3/issue/{clave_issue}",
        params={"fields": "issuelinks"},
    )
    return datos(respuesta)["fields"].get("issuelinks") or []


def desvincular_historia(id_enlace):
    """Elimina un issue link de Jira por su id."""
    verificar(requests.delete(
        f"{config.jira.baseUrl}/rest/api/3/issueLink/{id_enlace}",
        headers=auth.obtener_headers_jira(),
        timeout=TIMEOUT_SEGUNDOS,
    ))


def sincronizar_historia(clave_test, clave_historia):
    """
    Sincroniza el vinculo de un Test con su Historia de Usuario segun el estado actual del tag @related:ID.
    Unidireccional: el .feature es la fuente de verdad. Es idempotente y cubre los tres casos:
      - clave_historia presente y sin vinculo previo -> crea el link.
      - clave_historia presente y ya vinculado -> no hace nada.
      - clave_historia ausente o distinta de la vinculada -> elimina el/los link(s) del tipo configurado
        que ya no correspondan (incluye el caso de eliminar la etiqueta del escenario).
    Devuelve (creado, eliminados).
    """
    enlaces = [e for e in obtener_enlaces(clave_test) if e["type"]["name"] == config.jira.storyLinkType]

    eliminados = 0
    ya_vinculado = False
    for enlace in enlaces:
        # Jira solo devuelve el issue "del otro lado" del enlace: al consultar el propio Test,
        # el campo poblado es siempre outwardIssue (nunca inwardIssue), apuntando a la Historia.
        es_vinculo_vigente = (
            bool(clave_historia)
            and enlace.get("outwardIssue") is not None
            and enlace["outwardIssue"].get("key") == clave_historia
        )
        if es_vinculo_vigente:
            ya_vinculado = True
            continue
        # El .feature ya no referencia esta Historia, o la referencia con la direccion incorrecta
        desvincular_historia(enlace["id"])
        eliminados += 1

    if not clave_historia or ya_vinculado:
        return False, eliminados

    # inwardIssue = Test para que su pagina muestre "tests" hacia la Historia (outwardIssue)
    verificar(requests.post(
        f"{config.jira.baseUrl}/rest/api/3/issueLink",
        json={
            "type": {"name": config.jira.storyLinkType},
            "inwardIssue": {"key": clave_test},
            "outwardIssue": {"key": clave_historia},
        },
        headers=auth.obtener_headers_jira(),
        timeout=TIMEOUT_SEGUNDOS,
    ))
    return True, eliminados
