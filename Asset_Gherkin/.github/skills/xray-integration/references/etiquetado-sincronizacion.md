# Algoritmo de etiquetado y sincronización

Aplica a lo que ejecuta `validate` (`scenario_validator.py`) sobre cada archivo `.feature` encontrado.

## Paso 1 — Escenarios sin etiqueta `@PROYECTO-n`

Para cada escenario que no tiene ya una etiqueta `@<JIRA_PROJECT_KEY>-<número>` ni es `@pendiente`/`@pending`:

1. Busca en Jira un Test Issue con el **nombre exacto** del escenario (JQL `summary ~ "..."`, filtrando
   después por igualdad exacta).
2. Si lo encuentra, reutiliza esa clave (no crea un duplicado).
3. Si no lo encuentra, importa el `.feature` **completo** a Xray (`POST /api/v2/import/feature`), lo que crea
   un Test Cucumber por cada escenario del archivo que aún no exista en Jira. Vuelve a buscar por nombre para
   obtener la clave recién creada.
4. Inserta la etiqueta `@<CLAVE>` justo antes de la línea `Escenario:`/`Scenario:` correspondiente, respetando
   la indentación y el tipo de salto de línea (CRLF o LF) del archivo original.
5. Actualiza la descripción del Test Issue en Jira con las etiquetas funcionales + el Gherkin completo del
   escenario (como ADF, un párrafo por línea).
6. Sincroniza el vínculo con la Historia de Usuario (ver más abajo).

## Paso 2 — Escenarios ya etiquetados (sincronización bidireccional)

El `.feature` es siempre la fuente de verdad. Para cada escenario que ya tiene `@<CLAVE>`, en cada ejecución
de `validate` se compara el estado actual en Jira contra el archivo y se propaga cualquier diferencia:

- **Nombre**: si el texto tras `Escenario:`/`Scenario:` cambió, actualiza el `summary` del Test Issue.
- **Etiquetas funcionales → labels de Jira**: cualquier tag que no sea la clave Xray (`@QA-n`), ni
  `@related:ID`, ni `@pendiente`/`@pending`, se sincroniza como label de Jira sin el prefijo `@`. Se añaden
  las nuevas y se eliminan las que ya no están en el `.feature`. Las labels internas de Xray (con forma
  `PROYECTO-n`) se preservan siempre.
- **Descripción**: se reescribe siempre con las etiquetas + pasos Gherkin actuales.
- **Vínculo con la Historia de Usuario**: ver siguiente sección.

Esta consulta se hace en lote (JQL `key in (...)`, de 50 en 50) para minimizar llamadas a la API cuando hay
muchos escenarios.

## Etiqueta `@related:ID` — vínculo con la Historia de Usuario

Mismo formato que usa el flujo principal de este agente (`generate_gherkin_standards.instructions.md`):
`@related:HU-2451`, `@related:QA-45`, etc. No es una label funcional: es una relación de tipo "issue link" en
Jira, configurable con `XRAY_STORY_LINK_TYPE` (por defecto `Test`).

Reglas (idempotentes, se evalúan en cada `validate`):

| Estado del `.feature` | Acción |
|---|---|
| `@related:ID` presente y aún no hay vínculo | Crea el issue link (Test → Historia) |
| `@related:ID` presente y ya está vinculado a esa misma Historia | No hace nada |
| `@related:ID` ausente, o apunta a otra Historia distinta a la vinculada | Elimina el/los vínculo(s) existentes del tipo `XRAY_STORY_LINK_TYPE` que ya no correspondan |

Esto cubre también el caso de quitar la etiqueta del escenario: en la siguiente ejecución de `validate` se
retira el vínculo en Jira.

## Escenarios `@pendiente` / `@pending`

Se excluyen de todo el proceso anterior: no se buscan, no se etiquetan y no se sincronizan. Ver limitación
relacionada en [pruebas-locales-y-problemas.md](./pruebas-locales-y-problemas.md).

## Resumen de la Test Execution (`send`)

- Nombre: `Ejecucion Playwright - AAAA-MM-DD HH:MM:SS` (UTC).
- Antes de enviar, avisa (sin bloquear) si ya existe una Test Execution con ese nombre exacto.
- Importa el JSON de Cucumber tal cual vía `POST /api/v2/import/execution/cucumber/multipart`, usando el
  campo `info` para fijar proyecto, summary y tipo de issue.
- Mapeo de estados Cucumber → Xray (constante `statusMap`, informativo: Xray interpreta el JSON
  directamente): `passed→PASSED`, `failed→FAILED`, `pending/skipped/undefined/ambiguous→TODO`.
