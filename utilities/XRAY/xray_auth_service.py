"""
Servicio de autenticacion para XRay Cloud y Jira Cloud.
Gestiona tokens de acceso y credenciales de forma segura.
"""

import base64
import re
import time

import requests

import xray_config as config
from xray_http import TIMEOUT_SEGUNDOS, datos, verificar

# Cache del token de XRay para evitar peticiones innecesarias
_token_cache = None
_token_expiry = None


def obtener_token():
    """Obtiene (o reutiliza del cache) el token de acceso a la API de XRay Cloud."""
    global _token_cache, _token_expiry

    if _token_cache and _token_expiry and time.time() * 1000 < _token_expiry:
        return _token_cache

    print("Autenticando con XRay Cloud...")

    respuesta = verificar(requests.post(
        f"{config.xray.baseUrl}{config.xray.authEndpoint}",
        json={"client_id": config.xray.clientId, "client_secret": config.xray.clientSecret},
        headers={"Content-Type": "application/json"},
        timeout=TIMEOUT_SEGUNDOS,
    ))

    # XRay devuelve el token como string JSON con comillas externas
    token_raw = datos(respuesta)
    if isinstance(token_raw, str):
        token_raw = re.sub(r'^"|"$', "", token_raw)
    _token_cache = token_raw
    # El token de XRay Cloud dura 1 hora; se renueva 5 minutos antes
    _token_expiry = time.time() * 1000 + 55 * 60 * 1000

    print("Autenticacion con XRay correcta.")
    return _token_cache


def obtener_headers_jira():
    """Devuelve las cabeceras de autenticacion Basic para la API de Jira."""
    credenciales = base64.b64encode(
        f"{config.jira.userEmail}:{config.jira.apiToken}".encode("utf-8")
    ).decode("ascii")
    return {
        "Authorization": f"Basic {credenciales}",
        "Content-Type": "application/json",
    }


def obtener_headers_xray():
    """Devuelve las cabeceras de autenticacion Bearer para la API de XRay."""
    token = obtener_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
