# XRAY — Integración con Xray Cloud / Jira Cloud (Python)

Migración a Python de `src/utils/xray/` del proyecto `qa-playwright-fwk`. Sincroniza escenarios Gherkin (`.feature`) con Xray Cloud/Jira Cloud y publica el resultado de cada ejecución (reporte JSON de Cucumber).

## Equivalencias con la versión Node.js

| Node.js (`src/utils/xray/`) | Python (esta carpeta) |
| --- | --- |
| `xray.config.js` | `xray_config.py` |
| `xrayAuthService.js` | `xray_auth_service.py` |
| `xrayTestManager.js` | `xray_test_manager.py` |
| `scenarioValidator.js` | `scenario_validator.py` |
| `xraySender.js` | `xray_sender.py` |
| `xraySync.js` | `xray_sync.py` |
| `xrayHooks.js` (`AfterAll`) | `xray_hooks.py` (`after_all`, p. ej. behave) |
| scripts npm (`xray:validate`, `xray:send`, `test:xray:*`) | `xray_cli.py` (`validate`, `send`, `run`) |
| (axios) | `xray_http.py` (helpers HTTP con la semántica de axios) |

## Funcionalidad

- Asocia cada escenario a un Test Issue de Xray mediante la etiqueta `@<CLAVE>-<n>` (ej. `@QA-123`): busca por nombre exacto; si no existe, importa el feature y añade la etiqueta al `.feature` (respeta CRLF/LF).
- Los `.feature` son la fuente de verdad: propaga a Jira nombre (summary), labels funcionales y descripción (Gherkin en ADF).
- Vínculo opcional con la Historia de Usuario mediante `@related:ID` (idempotente; elimina vínculos obsoletos). Tipo de link configurable con `XRAY_STORY_LINK_TYPE` (por defecto `Test`).
- Ignora escenarios `@pendiente` / `@pending`.
- Crea una Test Execution (`Ejecucion Playwright - AAAA-MM-DD HH:MM:SS`, UTC) importando `cucumber-report.json`; si falla guarda `reports/json/xray-pending.json`.

## Instalación

```bash
pip install -r requirements.txt
cp .env.xray.example .env.xray   # y rellenar credenciales
```

`.env.xray` se busca en la raíz del proyecto, que por defecto es esta carpeta. Para usarla sobre otro proyecto, defina `XRAY_PROJECT_ROOT` (de ahí se resuelven `.env.xray`, `reports/json/cucumber-report.json` y `src/features/`). `XRAY_FEATURES_DIR` cambia el directorio de features por defecto.

La integración se desactiva si no existe `.env.xray`, si `XRAY_ENABLED=false` o si falta `XRAY_CLIENT_ID`.

## Uso

```bash
python xray_cli.py validate [dir_features]     # = npm run xray:validate
python xray_cli.py send [cucumber-report.json] # = npm run xray:send
python xray_cli.py run [--headed] [--features DIR] -- <comando de pruebas>
```

`run` valida, ejecuta el comando (debe generar `reports/json/cucumber-report.json`) y solo envía resultados si termina con código 0 (igual que el encadenado `&&` de `test:xray:headless`). `--headed` define `HEADED=true`.

También se pueden invocar directamente `python scenario_validator.py [dir]` y `python xray_sync.py [reporte]`.

Ejemplo con behave: `python xray_cli.py run -- behave features --format json -o reports/json/cucumber-report.json`.

## Prueba local sin entorno real

```bash
python tests/demo_local.py
```

Levanta un Jira/Xray simulado (`tests/mock_jira_xray.py`), crea un proyecto temporal con un `.feature` y ejecuta `validate` y `send`. Imprime el feature antes y después, y un resumen final (código de salida 0 si todo es correcto). No toca tu Jira ni tus archivos.

## Diferencias deliberadas respecto a la versión Node.js

- Se parte de `develop` incluyendo la integración `@related` / `storyLinkType` de `feature/xray-link-hu-id` (en `develop` la función existía pero no estaba conectada y faltaba `storyLinkType`).
- Se corrige el patrón de labels internas en el paso 4 del validador (en JS `\d` sin escapar dentro de un template literal impedía excluir `PROY-n` al comparar labels).
- Al etiquetar un `.feature` con saltos de línea CRLF, la línea `@PROY-n` insertada también termina en CRLF (la versión Node la dejaba en LF y el archivo quedaba con saltos mezclados).
- El mensaje de `xray-pending.json` indica comandos Python.
- `statusMap` se conserva en la configuración, pero (igual que en Node) no se usa.

## Limitaciones conocidas (heredadas de la versión Node.js)

- **`@pendiente` / `@pending`:** estos escenarios no se etiquetan ni se sincronizan, pero cuando el validador importa un `.feature` completo en Xray, Xray crea igualmente un Test para ellos (sin etiqueta `@PROY-n` en el archivo).
- **Reportes Cucumber:** si el reporte contiene escenarios sin etiqueta `@PROY-n` (por ejemplo `@pendiente`), Xray creará Tests nuevos al importar los resultados. Excluya esos escenarios al ejecutar (`--tags "not @pendiente"`).
- Xray devuelve el estado de un paso omitido como `TO DO`.
