"""
Procesador y enviador de resultados de pruebas a XRay.
Lee el JSON de Cucumber y crea una Test Execution en XRay con los resultados.
"""

import json
import os
from datetime import datetime, timezone

import requests

import xray_auth_service as auth
import xray_config as config
from xray_http import TIMEOUT_SEGUNDOS, advertir, datos, mensaje_error, verificar


def generar_nombre_ejecucion():
    """
    Genera el nombre de la ejecucion con fecha y hora actuales (UTC).
    Formato: "Ejecucion Playwright - YYYY-MM-DD HH:MM:SS"
    """
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return f"{config.execution.namePrefix} - {fecha}"


def buscar_ejecucion_existente(nombre):
    """Comprueba si ya existe una Test Execution con el mismo nombre en Jira."""
    nombre_escapado = nombre.replace('"', '\\"')
    jql = (
        f'project = "{config.jira.projectKey}" AND issuetype = "Test Execution" '
        f'AND summary = "{nombre_escapado}"'
    )

    try:
        respuesta = verificar(requests.get(
            f"{config.jira.baseUrl}/rest/api/3/search/jql",
            headers=auth.obtener_headers_jira(),
            params={"jql": jql, "maxResults": 1, "fields": "summary"},
            timeout=TIMEOUT_SEGUNDOS,
        ))
        issues = datos(respuesta).get("issues") or []
        return issues[0] if len(issues) > 0 else None
    except Exception as error:
        advertir(f"No se pudo comprobar ejecuciones existentes: {mensaje_error(error)}")
        return None


def importar_resultados(ruta_reporte, nombre_ejecucion):
    """
    Importa el reporte Cucumber a XRay usando el endpoint multipart.
    Permite especificar el nombre de la Test Execution via el campo info.
    """
    with open(ruta_reporte, "r", encoding="utf-8") as flujo:
        contenido_reporte = flujo.read()

    info_ejecucion = json.dumps(
        {
            "fields": {
                "project": {"key": config.jira.projectKey},
                "summary": nombre_ejecucion,
                "issuetype": {"name": "Test Execution"},
            }
        },
        separators=(",", ":"),
        ensure_ascii=False,
    )

    token = auth.obtener_token()
    respuesta = verificar(requests.post(
        f"{config.xray.baseUrl}{config.xray.importEndpoint}",
        files={
            "results": ("cucumber-report.json", contenido_reporte.encode("utf-8"), "application/json"),
            "info": ("info.json", info_ejecucion.encode("utf-8"), "application/json"),
        },
        headers={"Authorization": f"Bearer {token}"},
        timeout=TIMEOUT_SEGUNDOS,
    ))

    return datos(respuesta)


def guardar_resultado_pendiente(ruta_reporte, error):
    """Guarda un registro pendiente localmente si falla la conexion con XRay."""
    try:
        ruta_pendiente = config.reports.xrayPending
        os.makedirs(os.path.dirname(ruta_pendiente), exist_ok=True)
        pendiente = {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "error": mensaje_error(error),
            "reportePath": str(ruta_reporte),
            "instrucciones": 'Ejecuta "python xray_sync.py" (o "python xray_cli.py send") para reintentar el envio.',
        }
        with open(ruta_pendiente, "w", encoding="utf-8") as flujo:
            flujo.write(json.dumps(pendiente, indent=2, ensure_ascii=False))
        advertir(f"Resultado pendiente guardado en: {ruta_pendiente}")
    except Exception as err_guardado:
        advertir(f"No se pudo guardar el resultado pendiente: {mensaje_error(err_guardado)}")


def enviar_resultados(ruta_reporte=None):
    """
    Punto de entrada principal.
    Lee el reporte JSON de Cucumber y envia los resultados a XRay.
    """
    ruta_reporte = ruta_reporte or config.reports.cucumberJson

    if not config.enabled:
        print("Integracion con XRay desactivada. No se envian resultados.")
        return None

    if not os.path.exists(ruta_reporte):
        advertir(f"Reporte no encontrado: {ruta_reporte}")
        advertir("Ejecuta las pruebas antes de enviar resultados a XRay.")
        return None

    nombre_ejecucion = generar_nombre_ejecucion()
    print("\nIniciando envio de resultados a XRay...")
    print(f"Nombre de ejecucion: {nombre_ejecucion}")

    existente = buscar_ejecucion_existente(nombre_ejecucion)
    if existente:
        advertir(f'Atencion: ya existe la ejecucion "{existente["key"]}" con el mismo nombre.')

    try:
        print("Importando resultados a XRay...")
        resultado = importar_resultados(ruta_reporte, nombre_ejecucion)

        clave_ejecucion = (
            resultado.get("key")
            or (resultado.get("testExecIssue") or {}).get("key")
            or "desconocida"
        )

        print("\nResultados enviados correctamente a XRay.")
        print(f"Test Execution: {clave_ejecucion}")
        print(f"URL: {config.jira.baseUrl}/browse/{clave_ejecucion}")

        return resultado
    except Exception as error:
        respuesta = getattr(error, "response", None)
        detalle = (
            json.dumps(datos(respuesta), indent=2, ensure_ascii=False)
            if respuesta is not None
            else mensaje_error(error)
        )
        advertir(f"Error al enviar resultados a XRay: {detalle}")
        guardar_resultado_pendiente(ruta_reporte, error)
        return None
