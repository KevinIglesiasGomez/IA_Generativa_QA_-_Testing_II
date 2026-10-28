# Configuración — variables de `.env.xray`

Todas las variables se leen exclusivamente de `.env.xray` (vía `xray_config.py`, con `python-dotenv`). Nunca
se mezclan con el `.env` de la aplicación bajo prueba ni con `env.local.js`/`playwright.config.js`.

## Activación / desactivación

La integración queda **habilitada** solo si se cumplen las tres condiciones:

1. Existe el archivo `.env.xray` en la raíz del proyecto (`XRAY_PROJECT_ROOT`).
2. `XRAY_ENABLED` no vale `"false"`.
3. `XRAY_CLIENT_ID` tiene algún valor.

Si falta cualquiera de las tres, los comandos `validate`/`send`/`run` terminan sin error y sin contactar a
Xray ni a Jira (mensaje: "Integración con XRay desactivada").

## Variables obligatorias

| Variable | Descripción | Dónde obtenerla |
|---|---|---|
| `XRAY_ENABLED` | `true`/`false`. Interruptor maestro de la integración. | — |
| `XRAY_CLIENT_ID` | Client ID de la API de Xray Cloud. | Xray Cloud → Settings → API Keys |
| `XRAY_CLIENT_SECRET` | Client Secret asociado al Client ID. | Xray Cloud → Settings → API Keys |
| `XRAY_BASE_URL` | URL base de Xray Cloud. | Por defecto `https://xray.cloud.getxray.app` si se omite |
| `JIRA_BASE_URL` | URL de la instancia de Jira Cloud. | `https://tu-organizacion.atlassian.net` |
| `JIRA_USER_EMAIL` | Email del usuario de Jira usado para autenticación Basic. | Tu cuenta de Atlassian |
| `JIRA_API_TOKEN` | Token de API de Jira (no es la contraseña). | https://id.atlassian.com/manage-profile/security/api-tokens |
| `JIRA_PROJECT_KEY` | Clave del proyecto Jira donde se crean los Test / Test Execution (ej. `QA`). | Jira → configuración del proyecto |

## Variables opcionales

| Variable | Por defecto | Efecto |
|---|---|---|
| `XRAY_STORY_LINK_TYPE` | `Test` | Tipo de issue link usado por la etiqueta `@related:ID` para vincular el Test con su Historia de Usuario. Verifica el nombre exacto disponible en tu instancia con `GET /rest/api/3/issueLinkType`. |
| `XRAY_PROJECT_ROOT` | Carpeta de `utilities/XRAY` | Raíz desde la que se resuelven `.env.xray`, `reports/json/cucumber-report.json` y, si no se define `XRAY_FEATURES_DIR`, `src/features/`. Apúntala al proyecto con los `.feature` reales (por ejemplo, el `e2e_repo` generado por el flujo principal de este agente). |
| `XRAY_FEATURES_DIR` | `<XRAY_PROJECT_ROOT>/src/features` | Carpeta donde `validate` busca archivos `.feature` si no se pasa un directorio explícito por línea de comandos. |

## Cómo apuntar la skill a otro proyecto

Por defecto, si no defines `XRAY_PROJECT_ROOT`, todo se resuelve relativo a la propia carpeta
`utilities/XRAY` de la copia local obtenida en [obtener-herramientas.md](./obtener-herramientas.md). Para
apuntar al proyecto donde están tus `.feature` (por ejemplo, el `e2e_repo` que generó el agente de Gherkin):

```powershell
$env:XRAY_PROJECT_ROOT = "C:\ruta\al\proyecto\destino"
python XRAY/xray_cli.py validate
```

Con `XRAY_PROJECT_ROOT` definido, `validate` buscará `.feature` en `<XRAY_PROJECT_ROOT>/src/features` salvo
que pases un directorio explícito o definas `XRAY_FEATURES_DIR`, y `send`/`run` leerán y escribirán los
reportes en `<XRAY_PROJECT_ROOT>/reports/json/`.

## Seguridad

- `.env.xray` nunca debe commitearse; solo se versiona `.env.xray.example` (sin valores reales).
- El token de Jira y el Client Secret de Xray son secretos: deben vivir en variables de entorno o en el
  gestor de secretos del CI/CD, nunca en texto plano en el repositorio.
- Rota las credenciales periódicamente y revócalas de inmediato si se filtran.
