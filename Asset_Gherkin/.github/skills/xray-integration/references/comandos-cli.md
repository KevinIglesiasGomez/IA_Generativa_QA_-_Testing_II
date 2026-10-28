# Referencia de comandos

Todos los comandos se ejecutan con Python, apuntando al script dentro de la copia local de `utilities/XRAY`
obtenida siguiendo [obtener-herramientas.md](./obtener-herramientas.md) (abreviado `XRAY/` en esta guía;
sustitúyelo por esa ruta real, por ejemplo `.copilot-tools-cache/demos-ia/utilities/XRAY`).

## `xray_cli.py validate [dir_features]`

Sincroniza los `.feature` con Xray **sin ejecutar pruebas**. Equivale a `npm run xray:validate` en la versión
Node.js del framework.

```bash
python XRAY/xray_cli.py validate
python XRAY/xray_cli.py validate ruta/a/mis/features
```

Si se omite `dir_features`, usa `XRAY_FEATURES_DIR` o `<XRAY_PROJECT_ROOT>/src/features`. Código de salida
`0` si no hubo errores de sincronización, `1` en caso contrario.

## `xray_cli.py send [reporte.json]`

Envía un reporte JSON de Cucumber ya generado, creando una Test Execution en Jira. Equivale a
`npm run xray:send`.

```bash
python XRAY/xray_cli.py send
python XRAY/xray_cli.py send reports/json/cucumber-report.json
```

Si se omite, usa `<XRAY_PROJECT_ROOT>/reports/json/cucumber-report.json`. Si el envío falla (red, Jira caído,
etc.), se guarda un registro en `reports/json/xray-pending.json` con instrucciones para reintentar; basta con
repetir el mismo comando más tarde.

## `xray_cli.py run [--headed] [--features DIR] -- <comando_de_pruebas>`

Encadena las tres fases: `validate` → `<comando_de_pruebas>` → `send` (solo si el comando de pruebas termina
con código `0`). Equivale a `npm run test:xray:headless` / `test:xray:headed`.

```bash
# Con behave
python XRAY/xray_cli.py run -- behave features --format json -o reports/json/cucumber-report.json

# Con cucumber-js (el comando de pruebas puede ser de cualquier lenguaje/runner)
python XRAY/xray_cli.py run -- npx cucumber-js "src/features/**/*.feature" --format json:reports/json/cucumber-report.json

# Con navegador visible (define HEADED=true en el entorno del comando)
python XRAY/xray_cli.py run --headed -- behave features --format json -o reports/json/cucumber-report.json

# Indicando un directorio de features distinto al de por defecto para la fase de validate
python XRAY/xray_cli.py run --features ruta/a/features -- behave ruta/a/features --format json -o reports/json/cucumber-report.json
```

Importante: el comando de pruebas **debe** generar el JSON de Cucumber exactamente en la ruta que espera
`send` (`<XRAY_PROJECT_ROOT>/reports/json/cucumber-report.json`, salvo que configures otra cosa). El
subcomando `run` es agnóstico del runner: solo necesita que el comando indicado tras `--` produzca ese JSON y
devuelva código de salida `0`.

Si `<comando_de_pruebas>` termina con código distinto de `0` (por ejemplo, un escenario falló), `send` **no**
se ejecuta en esa misma cadena; el reporte ya generado puede enviarse después a mano con
`xray_cli.py send`.

## Invocación directa de los scripts internos

Equivalentes de bajo nivel, útiles si no quieres pasar por `xray_cli.py`:

```bash
python XRAY/scenario_validator.py [dir_features]   # = xray_cli.py validate
python XRAY/xray_sync.py [reporte.json]            # = xray_cli.py send
```

## Hook para `behave` (alternativa a `send`/`run`)

`XRAY/xray_hooks.py` expone `after_all(context)`, pensado para `features/environment.py` de `behave`:

```python
from xray_hooks import after_all


def after_all(context):
    after_all(context)
```

No se recomienda si se necesita fiabilidad estricta: `after_all` puede dispararse antes de que el formatter
JSON de Cucumber/behave termine de escribir el archivo. Es más seguro encadenar `xray_cli.py run` o llamar a
`xray_sync.py` / `xray_cli.py send` como paso explícito después de que termine la ejecución de pruebas.
