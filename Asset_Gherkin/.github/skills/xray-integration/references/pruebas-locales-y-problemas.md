# Pruebas locales y problemas conocidos

## Probar de extremo a extremo sin un Jira real

`utilities/XRAY/tests/demo_local.py`:

```bash
python XRAY/tests/demo_local.py
```

Qué hace:

1. Levanta un servidor HTTP local que simula las APIs de Xray Cloud y Jira Cloud
   (`XRAY/tests/mock_jira_xray.py`), sin credenciales reales.
2. Crea un proyecto temporal con un `.feature` de ejemplo y un `.env.xray` apuntando a ese servidor simulado.
3. Ejecuta `validate` y `send` reales contra ese entorno simulado.
4. Imprime el `.feature` antes y después (para ver las etiquetas añadidas) y un resumen final con código de
   salida `0` si todo fue correcto.

No modifica tu Jira real ni ningún archivo fuera del directorio temporal. Ejecútalo antes de usar
credenciales reales.

## Generar un reporte Cucumber falso (sin ejecutar pruebas)

Para probar `send` de forma aislada, sin un test runner real:

```bash
python XRAY/tests/crear_reporte.py QA-12=passed QA-13=failed
```

Genera `reports/json/cucumber-report.json` con un escenario por cada `CLAVE=estado` indicado (estados
válidos: `passed`, `failed`, `skipped`).

## Limpiar lo creado durante pruebas manuales contra un Jira real

```bash
python XRAY/tests/borrar_prueba.py [QA-20 QA-21 ...]
```

Solo borra, de forma segura:

- Issues cuyo `summary` empieza por `[DEMO-XRAY-PY]`.
- Las Test Executions cuya clave se pase como argumento, y solo si su nombre empieza por
  `"Ejecucion Playwright - "`.

También deja `tests/demo.feature` como plantilla, quitando las etiquetas `@PROYECTO-n` que haya añadido
`validate`. Requiere credenciales reales válidas en `.env.xray` (no usa el mock).

## Limitaciones conocidas

- **`@pendiente` / `@pending`**: estos escenarios nunca se etiquetan ni se sincronizan, pero si el validador
  necesita importar el `.feature` completo (porque hay otros escenarios nuevos en el mismo archivo), Xray
  crea igualmente un Test para ellos — simplemente queda sin la etiqueta `@PROYECTO-n` en el archivo.
- **Reportes Cucumber con escenarios sin etiquetar**: si el reporte enviado con `send` contiene escenarios sin
  `@PROYECTO-n` (por ejemplo los `@pendiente`), Xray crea Tests nuevos al importar los resultados. Excluye
  esos escenarios al ejecutar las pruebas (por ejemplo `--tags "not @pendiente"` en Cucumber/behave).
- **Pasos omitidos (`skipped`)**: Xray los reporta con estado `TO DO`, no como "skipped".
- **Nombres de escenario duplicados**: la búsqueda por nombre exacto puede confundir dos escenarios con
  exactamente el mismo texto en features distintos; usa nombres descriptivos y únicos.
- **Rendimiento**: `validate` hace al menos una llamada a Jira por escenario sin etiquetar (búsqueda por
  nombre) más una consulta en lote para los ya etiquetados; en features muy grandes puede tardar.
