"""
Configuracion centralizada para la integracion con XRay / Jira Cloud.
Carga exclusivamente .env.xray, sin afectar la configuracion de la aplicacion.

Para desactivar la integracion: establecer XRAY_ENABLED=false en .env.xray
o eliminar el archivo .env.xray.

Raiz del proyecto: por defecto es la carpeta de este modulo. Se puede cambiar con la
variable de entorno XRAY_PROJECT_ROOT (de ahi se resuelven .env.xray, reports/ y src/features/).
"""

import os
import sys
from pathlib import Path
from types import SimpleNamespace

from dotenv import load_dotenv

# Evita errores de codificacion al imprimir en consolas Windows (cp1252)
for _flujo in (sys.stdout, sys.stderr):
    try:
        _flujo.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

RAIZ_PROYECTO = Path(os.environ.get("XRAY_PROJECT_ROOT") or Path(__file__).resolve().parent).resolve()
ENV_XRAY_PATH = RAIZ_PROYECTO / ".env.xray"

# Carga .env.xray solo si existe, para no contaminar os.environ con variables de XRay
if ENV_XRAY_PATH.exists():
    load_dotenv(ENV_XRAY_PATH)

habilitado = (
    ENV_XRAY_PATH.exists()
    and os.environ.get("XRAY_ENABLED") != "false"
    and bool(os.environ.get("XRAY_CLIENT_ID"))
)

enabled = habilitado

xray = SimpleNamespace(
    clientId=os.environ.get("XRAY_CLIENT_ID"),
    clientSecret=os.environ.get("XRAY_CLIENT_SECRET"),
    baseUrl=os.environ.get("XRAY_BASE_URL") or "https://xray.cloud.getxray.app",
    authEndpoint="/api/v2/authenticate",
    importEndpoint="/api/v2/import/execution/cucumber/multipart",
    testEndpoint="/api/v2/test",
)

jira = SimpleNamespace(
    baseUrl=os.environ.get("JIRA_BASE_URL"),
    userEmail=os.environ.get("JIRA_USER_EMAIL"),
    apiToken=os.environ.get("JIRA_API_TOKEN"),
    projectKey=os.environ.get("JIRA_PROJECT_KEY"),
    # Tipo de link usado para vincular el Test con su Historia de Usuario (etiqueta @related:ID).
    # El link estandar de Xray Cloud se llama "Test"; verificar con GET /rest/api/3/issueLinkType.
    storyLinkType=os.environ.get("XRAY_STORY_LINK_TYPE") or "Test",
)

reports = SimpleNamespace(
    cucumberJson=RAIZ_PROYECTO / "reports" / "json" / "cucumber-report.json",
    xrayPending=RAIZ_PROYECTO / "reports" / "json" / "xray-pending.json",
)

# Mapeo de estados de Cucumber a estados de XRay
statusMap = {
    "passed": "PASSED",
    "failed": "FAILED",
    "pending": "TODO",
    "skipped": "TODO",
    "undefined": "TODO",
    "ambiguous": "TODO",
}

execution = SimpleNamespace(namePrefix="Ejecucion Playwright")

featuresDir = Path(os.environ.get("XRAY_FEATURES_DIR") or RAIZ_PROYECTO / "src" / "features")
