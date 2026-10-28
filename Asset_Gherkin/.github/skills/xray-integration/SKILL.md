---
name: xray-integration
description: 'Sincroniza archivos .feature (Gherkin/Cucumber) con Xray Cloud y Jira Cloud ejecutando la herramienta Python utilities/XRAY, descargada bajo demanda desde un repositorio de herramientas configurable (sin URL fija): etiqueta escenarios con la clave del Test Issue (@PROYECTO-n), crea o reutiliza Test Issues, propaga nombre/etiquetas/pasos, vincula Historias de Usuario mediante @related:ID y publica resultados de ejecucion (Test Execution) desde un reporte JSON de Cucumber. Usar cuando se pida sincronizar, etiquetar, vincular o enviar escenarios/resultados a Xray o Jira, configurar .env.xray, generar una Test Execution, o conectar los .feature generados por este copiloto con Jira.'
argument-hint: 'validate [dir_features] | send [reporte.json] | run -- <comando_de_pruebas>'
---

# Integración con Xray Cloud / Jira Cloud

## Obtener las herramientas — paso obligatorio, siempre el primero

Antes de ejecutar cualquier otra sección de este documento:

1. **Pregunta siempre** por la URL (o ruta local) del repositorio de skills/utilities, salvo que ya la tengas
   de un paso anterior de esta misma conversación. Ejemplo: *"¿Cuál es la URL (o ruta local) del repositorio
   del que debo descargar `utilities/XRAY`?"*. Es un dato obligatorio: no continúes sin una respuesta, y no
   la des por sabida ni la sustituyas por una URL propia de este proyecto.
2. Resuelve esa respuesta como `${tools_repo_url}` y obtén una copia local siguiendo
   [references/obtener-herramientas.md](./references/obtener-herramientas.md) (admite tanto una URL git como
   una ruta local ya existente, con caché para no descargar de nuevo en cada ejecución).
3. A partir de ahí, en todo este documento `XRAY/` significa `<copia_local>/utilities/XRAY` — sustitúyelo por
   esa ruta real al ejecutar los comandos.

## Cuándo usar esta skill

- Piden sincronizar, etiquetar, vincular o "subir" escenarios `.feature` a Xray o Jira.
- Piden publicar el resultado de una ejecución de pruebas como Test Execution en Jira.
- Preguntan cómo configurar `.env.xray`, credenciales de Xray/Jira, o el link `@related:ID`.
- Quieren probar la integración sin tocar un Jira real (modo demo / mock).
- Justo después de generar `.feature` (con este copiloto o cualquier otro), si se pide conectarlos con Jira.

## Qué resuelve (resumen)

- Asocia cada escenario a un Test Issue de Xray mediante la etiqueta `@<CLAVE>-<n>` (ej. `@QA-123`): busca
  primero por nombre exacto; si no existe, importa el `.feature` completo y añade la etiqueta.
- Los `.feature` son la fuente de verdad: en cada ejecución propaga a Jira el nombre (summary), las etiquetas
  funcionales (como labels) y los pasos Gherkin (como descripción en formato ADF).
- Vínculo opcional con una Historia de Usuario mediante la etiqueta `@related:ID` — la misma convención que
  ya usan muchos generadores de Gherkin (en este copiloto, ver `generate_gherkin_standards.instructions.md`).
  Es idempotente y elimina vínculos obsoletos si se quita la etiqueta.
- Ignora por completo los escenarios `@pendiente` / `@pending`.
- Crea una Test Execution (`Ejecucion Playwright - AAAA-MM-DD HH:MM:SS`, UTC) importando un reporte JSON de
  Cucumber; si falla el envío, guarda un registro local en `reports/json/xray-pending.json` para reintentar.

Detalle completo del algoritmo: [references/etiquetado-sincronizacion.md](./references/etiquetado-sincronizacion.md).

## Requisitos previos

- Python 3.9 o superior.
- Dependencias instaladas: `pip install -r XRAY/requirements.txt` (instala `requests` y `python-dotenv`).
- Un proyecto Xray Cloud + Jira Cloud con el tipo de issue **Test** (subtipo Cucumber) habilitado.
- Credenciales: API Key de Xray Cloud (Client ID/Secret) y API Token de Jira Cloud.

## Configuración inicial

1. Decide **dónde viven los `.feature` que quieres sincronizar**: normalmente es el `e2e_repo` (repositorio
   de salida) que ya usa el flujo principal de este copiloto, no la carpeta de esta skill ni la copia local
   de las herramientas obtenida en el paso anterior.
2. Copia la plantilla de credenciales a ese proyecto y complétala:
   ```bash
   cp XRAY/.env.xray.example <ruta_del_proyecto_destino>/.env.xray
   ```
3. Antes de ejecutar cualquier comando, define `XRAY_PROJECT_ROOT` apuntando a ese proyecto (de ahí se
   resuelven `.env.xray`, `reports/json/cucumber-report.json` y el directorio de features por defecto):
   ```powershell
   $env:XRAY_PROJECT_ROOT = "<ruta_del_proyecto_destino>"
   ```
   Si no se define, la raíz por defecto es la propia carpeta `utilities/XRAY`.
4. Rellena las variables de `.env.xray` (credenciales, clave de proyecto Jira, tipo de link). Referencia
   completa de cada variable: [references/configuracion.md](./references/configuracion.md).

## Comandos principales

| Comando | Equivale a | Uso |
|---|---|---|
| `python XRAY/xray_cli.py validate [dir_features]` | `npm run xray:validate` (versión Node) | Etiqueta y sincroniza `.feature` sin ejecutar pruebas |
| `python XRAY/xray_cli.py send [reporte.json]` | `npm run xray:send` | Envía un reporte Cucumber ya generado |
| `python XRAY/xray_cli.py run [--headed] [--features DIR] -- <comando>` | `npm run test:xray:headless/headed` | Valida, ejecuta `<comando>` y envía resultados solo si termina en código 0 |

También se pueden invocar directamente `python XRAY/scenario_validator.py [dir]` y
`python XRAY/xray_sync.py [reporte]`. Referencia completa con ejemplos (incluye uso con `behave`,
`cucumber-js` y el hook `after_all`): [references/comandos-cli.md](./references/comandos-cli.md).

## Flujo recomendado junto al generador de Gherkin

1. Generar los `.feature` con el flujo principal del agente (Steps 0-5) en `${e2e_repo}/features/`.
2. Configurar `.env.xray` en `${e2e_repo}` (una sola vez) y definir `XRAY_PROJECT_ROOT` apuntando ahí.
3. Ejecutar `validate` sobre `${e2e_repo}/features/` para etiquetar y sincronizar con Jira.
4. Ejecutar la batería de pruebas del proyecto destino generando `reports/json/cucumber-report.json` (o usar
   `run` para encadenar automáticamente validate + pruebas + send).
5. Confirmar en el repositorio los `.feature` modificados (ahora llevan la etiqueta `@PROYECTO-n`).

## Probar sin tocar un Jira real

`XRAY/tests/demo_local.py` levanta un Jira/Xray simulado en memoria y ejecuta `validate` + `send` contra un
proyecto temporal, sin credenciales reales. Útil para comprobar que todo funciona antes de usar un Jira de
verdad. Detalle: [references/pruebas-locales-y-problemas.md](./references/pruebas-locales-y-problemas.md).

## Seguridad

- Nunca commitear `.env.xray` (solo se versiona `.env.xray.example`, sin valores reales).
- Credenciales (Client Secret de Xray, API Token de Jira) solo en variables de entorno o secretos de CI/CD.
- Rotar periódicamente las API keys y tokens.
- Si el repositorio de herramientas requiere autenticación, resúelvela desde el entorno de quien ejecuta el
  comando (credential manager, SSH, token ya configurado); no guardes esa credencial en ningún archivo.

## Límites conocidos

Resumen rápido (detalle en la referencia de pruebas/problemas):
- Escenarios `@pendiente`/`@pending` no se etiquetan, pero si el `.feature` se importa completo Xray puede
  crear igualmente un Test para ellos.
- Un reporte Cucumber con escenarios sin etiqueta `@PROYECTO-n` puede crear Tests nuevos al enviarlo; excluye
  esos escenarios al ejecutar las pruebas (`--tags "not @pendiente"` o equivalente del runner).
- Xray reporta el estado de un paso omitido (`skipped`) como `TO DO`.

## Estructura de esta skill

```
xray-integration/
├── SKILL.md                              # Este archivo
└── references/
    ├── obtener-herramientas.md           # Cómo resolver ${tools_repo_url} en una copia local (paso 1)
    ├── configuracion.md                  # Todas las variables de .env.xray explicadas
    ├── comandos-cli.md                   # Referencia completa de validate / send / run
    ├── etiquetado-sincronizacion.md      # Algoritmo de etiquetado, @related:ID, labels
    └── pruebas-locales-y-problemas.md    # Mock de Jira, utilidades de demo, limitaciones
```

El código se obtiene en tiempo de ejecución siguiendo
[references/obtener-herramientas.md](./references/obtener-herramientas.md).
