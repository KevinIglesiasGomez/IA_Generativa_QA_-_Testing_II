"""
Validador de escenarios para integracion con XRay.
Verifica que todos los escenarios tienen etiqueta Jira (@PROYECTO-X) y
crea Test Issues Cucumber en XRay para los que no la tienen.

Algoritmo de dos pasos por feature:
  1. Buscar por nombre -> reutilizar Test Issues ya existentes
  2. Si faltan -> importar el feature completo (crea Cucumber tests)
     y luego buscar por nombre para obtener la clave

Ejecutar antes de las pruebas: python scenario_validator.py [directorio_features]
"""

import os
import re
import sys

import xray_config as config
import xray_test_manager as test_manager
from xray_http import advertir, mensaje_error
from xray_test_manager import es_cabecera_escenario, js_trim, nombre_escenario

PREFIJOS_CABECERA = ("Característica:", "Feature:", "Antecedentes:", "Background:")
TAGS_PENDIENTE = ("@pendiente", "@pending")


def encontrar_features(directorio):
    """Busca recursivamente archivos .feature en un directorio."""
    resultado = []
    if not os.path.exists(directorio):
        return resultado

    for entrada in os.scandir(directorio):
        if entrada.is_dir():
            resultado.extend(encontrar_features(entrada.path))
        elif entrada.name.endswith(".feature"):
            resultado.append(entrada.path)
    return resultado


def _escenario(nombre, tags, lineas, ruta):
    return {"nombre": nombre, "tags": list(tags), "gherkin": "\n".join(lineas), "ruta": ruta}


def parsear_escenarios(ruta_feature):
    """
    Parsea los escenarios de un archivo feature.
    Devuelve nombre, tags y contenido Gherkin de cada escenario.
    """
    with open(ruta_feature, "r", encoding="utf-8", newline="") as flujo:
        contenido = flujo.read()
    lineas = contenido.split("\n")
    escenarios = []

    tags_bloque = []
    en_escenario = False
    nombre_actual = None
    lineas_escenario = []

    for linea in lineas:
        trim = js_trim(linea)

        if not en_escenario and (trim == "" or trim.startswith("#")):
            tags_bloque = []
            continue

        if trim.startswith("@"):
            if en_escenario:
                escenarios.append(_escenario(nombre_actual, tags_bloque, lineas_escenario, ruta_feature))
                lineas_escenario = []
                en_escenario = False
                tags_bloque = []
            nuevas_tags = [t for t in re.split(r"\s+", trim) if t.startswith("@")]
            tags_bloque = [*tags_bloque, *nuevas_tags]
            continue

        if es_cabecera_escenario(trim):
            if en_escenario:
                escenarios.append(_escenario(nombre_actual, tags_bloque, lineas_escenario, ruta_feature))
                lineas_escenario = []
            en_escenario = True
            nombre_actual = nombre_escenario(trim)
            lineas_escenario = [linea]
            tags_bloque = [*tags_bloque]
            continue

        if trim.startswith(PREFIJOS_CABECERA):
            if en_escenario:
                escenarios.append(_escenario(nombre_actual, tags_bloque, lineas_escenario, ruta_feature))
                lineas_escenario = []
                en_escenario = False
            tags_bloque = []
            continue

        if en_escenario:
            lineas_escenario.append(linea)

    if en_escenario and nombre_actual:
        escenarios.append(_escenario(nombre_actual, tags_bloque, lineas_escenario, ruta_feature))

    return escenarios


def _es_pendiente(escenario):
    return any(t in TAGS_PENDIENTE for t in escenario["tags"])


def sincronizar_historia_escenario(clave_test, tags):
    """
    Sincroniza de forma unidireccional el vinculo de un Test con su Historia de Usuario segun la
    etiqueta opcional @related:ID del escenario. El .feature es la fuente de verdad: si la etiqueta
    no esta presente (o se elimino), se retira cualquier vinculo existente del tipo configurado.
    """
    clave_historia = test_manager.extraer_clave_historia(tags)
    try:
        creado, eliminados = test_manager.sincronizar_historia(clave_test, clave_historia)
        if creado:
            print(f"  [Historia] {clave_test} vinculado con {clave_historia} ({config.jira.storyLinkType})")
        if eliminados > 0:
            print(f"  [Historia] {clave_test}: {eliminados} vinculo(s) eliminado(s) ({config.jira.storyLinkType})")
    except Exception as error:
        advertir(f"  No se pudo sincronizar la Historia de {clave_test}: {mensaje_error(error)}")


def procesar_feature(archivo, patron_tag):
    """
    Procesa un archivo feature:
      Paso 1: Busca Test Issues existentes por nombre (reutiliza sin crear duplicados).
      Paso 2: Para los no encontrados, importa el feature completo a XRay y vuelve a buscar.
      Paso 3: Añade las etiquetas @PROYECTO-X a los escenarios sin etiquetar.
      Paso 4: Sincroniza nombre, labels, descripcion y vinculo con Historia de los ya etiquetados.
    Devuelve contadores de creadas, reutilizadas y errores.
    """
    escenarios = parsear_escenarios(archivo)
    sin_tag = [
        e for e in escenarios
        if not any(patron_tag.match(t) for t in e["tags"]) and not _es_pendiente(e)
    ]

    # Paso 4 se ejecuta siempre: actualiza descripciones de escenarios ya etiquetados
    con_tag = [
        e for e in escenarios
        if any(patron_tag.match(t) for t in e["tags"]) and not _es_pendiente(e)
    ]

    # Early return solo si no hay nada que procesar en ninguno de los dos grupos
    if len(sin_tag) == 0 and len(con_tag) == 0:
        return {"creadas": 0, "reutilizadas": 0, "errores": 0}

    creadas = 0
    reutilizadas = 0
    errores = 0

    if len(sin_tag) > 0:
        print(f"\n{os.path.basename(archivo)}: {len(sin_tag)} escenario(s) sin etiqueta")

        # Paso 1: buscar issues existentes por nombre
        mapeo_claves = {}
        sin_issue = []

        for esc in sin_tag:
            try:
                issue = test_manager.buscar_test_por_nombre(esc["nombre"])
                if issue:
                    mapeo_claves[esc["nombre"]] = issue["key"]
                    print(f'  Existente: {issue["key"]} -> "{esc["nombre"]}"')
                else:
                    sin_issue.append(esc)
            except Exception as error:
                advertir(f'  Error buscando "{esc["nombre"]}": {mensaje_error(error)}')
                sin_issue.append(esc)

        # Paso 2: importar el feature completo para los escenarios sin issue
        if len(sin_issue) > 0:
            print(f"  Importando feature ({len(sin_issue)} escenario(s) nuevos)...")
            try:
                test_manager.importar_feature(archivo)
                for esc in sin_issue:
                    try:
                        issue = test_manager.buscar_test_por_nombre(esc["nombre"])
                        if issue:
                            mapeo_claves[esc["nombre"]] = issue["key"]
                            print(f'  Creado: {issue["key"]} -> "{esc["nombre"]}"')
                        else:
                            advertir(f'  No encontrado tras import: "{esc["nombre"]}"')
                    except Exception as error:
                        advertir(f'  Error buscando tras import "{esc["nombre"]}": {mensaje_error(error)}')
            except Exception as error:
                advertir(f"  Error importando feature {os.path.basename(archivo)}: {mensaje_error(error)}")

        # Paso 3: añadir etiquetas y actualizar descripcion de escenarios sin tag
        for esc in sin_tag:
            clave = mapeo_claves.get(esc["nombre"])
            if clave:
                test_manager.etiquetar_escenario(archivo, esc["nombre"], clave)
                try:
                    test_manager.actualizar_descripcion(clave, esc["tags"], esc["gherkin"])
                except Exception as error:
                    advertir(f"  No se pudo actualizar descripcion de {clave}: {mensaje_error(error)}")
                # Etiqueta opcional @related:ID: si no esta presente, el test no se vincula a ninguna Historia
                sincronizar_historia_escenario(clave, esc["tags"])
                if any(s["nombre"] == esc["nombre"] for s in sin_issue):
                    creadas += 1
                else:
                    reutilizadas += 1
            else:
                errores += 1

    # Paso 4: sincronizacion bidireccional — los .features son la fuente de verdad.
    # Para escenarios ya etiquetados, detecta cambios de nombre, tags y steps
    # y los propaga a las Test Issues correspondientes en Jira.
    if len(con_tag) > 0:
        patron_xray = test_manager.patron_tag_xray()

        # Obtener el estado actual de todas las issues en un solo batch (eficiente)
        claves = [c for c in (
            test_manager.extraer_clave_jira(e["tags"], config.jira.projectKey) for e in con_tag
        ) if c]
        estados_jira = test_manager.obtener_estado_jira(claves)

        for esc in con_tag:
            clave = test_manager.extraer_clave_jira(esc["tags"], config.jira.projectKey)
            if not clave:
                continue

            # La etiqueta @related:ID no es una label funcional, es la relacion con la Historia de Usuario
            tags_funcionales = [
                t for t in esc["tags"]
                if not patron_xray.match(t) and not re.match(r"^@related:", t, re.IGNORECASE)
            ]
            estado_actual = estados_jira.get(clave)

            if not estado_actual:
                # Issue no encontrada en el batch (puede que se haya borrado): solo descripcion
                try:
                    test_manager.actualizar_descripcion(clave, esc["tags"], esc["gherkin"])
                except Exception:
                    pass
                continue

            # Detectar y propagar cambio de nombre
            if estado_actual["summary"] != esc["nombre"]:
                print(f'  [Nombre] {clave}: "{estado_actual["summary"]}" -> "{esc["nombre"]}"')
                try:
                    test_manager.actualizar_summary(clave, esc["nombre"])
                except Exception as error:
                    advertir(f"  No se pudo actualizar nombre de {clave}: {mensaje_error(error)}")

            # Detectar y propagar cambio de tags funcionales (labels en Jira)
            excluidas = {"pendiente", "pending"}
            patron_clave = re.compile(rf"^{re.escape(config.jira.projectKey or '')}-[0-9]+$")
            # Excluir labels internas de XRay (PROY-XXX) de la comparacion — XRay las gestiona internamente
            labels_actuales = sorted(
                l for l in (estado_actual.get("labels") or [])
                if l not in excluidas and not patron_clave.match(l)
            )
            labels_nuevas = sorted(
                l for l in (re.sub(r"^@", "", t, count=1) for t in tags_funcionales)
                if l not in excluidas and not patron_clave.match(l)
            )
            if labels_actuales != labels_nuevas:
                anadidas = [l for l in labels_nuevas if l not in labels_actuales]
                eliminadas = [l for l in labels_actuales if l not in labels_nuevas]
                if anadidas:
                    print(f"  [Tags+] {clave}: {', '.join(anadidas)}")
                if eliminadas:
                    print(f"  [Tags-] {clave}: {', '.join(eliminadas)}")
                try:
                    test_manager.actualizar_labels(clave, tags_funcionales, estado_actual["labels"])
                except Exception as error:
                    advertir(f"  No se pudo actualizar labels de {clave}: {mensaje_error(error)}")

            # Actualizar descripcion siempre (refleja el estado actual del feature: steps + tags)
            try:
                test_manager.actualizar_descripcion(clave, esc["tags"], esc["gherkin"])
            except Exception as error:
                advertir(f"  No se pudo actualizar descripcion de {clave}: {mensaje_error(error)}")

            # Cubre el vinculo inicial, el cambio de Historia y la eliminacion de la etiqueta del escenario
            sincronizar_historia_escenario(clave, esc["tags"])

    return {"creadas": creadas, "reutilizadas": reutilizadas, "errores": errores}


def validar_y_sincronizar(features_dir=None):
    """Valida todos los escenarios y crea Test Issues Cucumber en XRay para los que no tienen etiqueta."""
    if not config.enabled:
        print("Integracion con XRay desactivada. Saltando validacion de escenarios.")
        return

    features_dir = features_dir or str(config.featuresDir)
    print(f"Validando escenarios en: {features_dir}")

    archivos_feature = encontrar_features(features_dir)
    if len(archivos_feature) == 0:
        advertir("No se encontraron archivos .feature en el directorio especificado.")
        return

    patron_tag = test_manager.patron_tag_xray()
    total_escenarios = 0
    total_ya_etiquetados = 0
    total_creadas = 0
    total_reutilizadas = 0
    total_errores = 0

    for archivo in archivos_feature:
        escenarios = parsear_escenarios(archivo)
        total_escenarios += len(escenarios)
        total_ya_etiquetados += len([
            e for e in escenarios
            if any(patron_tag.match(t) for t in e["tags"]) or _es_pendiente(e)
        ])

        resultado = procesar_feature(archivo, patron_tag)
        total_creadas += resultado["creadas"]
        total_reutilizadas += resultado["reutilizadas"]
        total_errores += resultado["errores"]

    print("\nResumen de validacion:")
    print(f"  Features procesados:          {len(archivos_feature)}")
    print(f"  Total escenarios:             {total_escenarios}")
    print(f"  Ya etiquetados con XRay:      {total_ya_etiquetados}")
    print(f"  Test Issues reutilizadas:     {total_reutilizadas}")
    print(f"  Test Issues nuevas (Cucumber): {total_creadas}")
    print(f"  Errores:                      {total_errores}")

    if total_errores > 0:
        advertir(f"Atencion: {total_errores} escenarios no pudieron sincronizarse.")
    print("Validacion completada.\n")


# Ejecucion directa como script
if __name__ == "__main__":
    try:
        validar_y_sincronizar(sys.argv[1] if len(sys.argv) > 1 else None)
    except Exception as err:
        advertir(f"Error en la validacion: {mensaje_error(err)}")
        sys.exit(1)
