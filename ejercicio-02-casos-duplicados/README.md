# Ejercicio 02 - Detección de casos duplicados

Asset: `Asset_CasosDuplicadosDetector` (agente `csv_duplicate_detector`).

## Objetivo

Detectar qué casos Gherkin pendientes de importar ya existen en Jira, aunque estén redactados de forma distinta, y generar un CSV limpio.

## Datos

| Fichero | Contenido |
|---|---|
| `datos/jira_casos_existentes.csv` | 15 casos exportados de Jira (texto libre) |
| `datos/gherkin_casos_importar.csv` | 15 casos Gherkin a importar |
| `solucion_esperada.md` | Resultado de referencia (no abrir antes de ejecutar) |

Ambos CSV usan coma como separador y codificación UTF-8. Los casos proceden de las historias de Splash, Login y Home del ejercicio 01.

## Cómo ejecutarlo

1. Abrir el workspace `Asset_CasosDuplicadosDetector` en VS Code.
2. Lanzar el prompt `csv_duplicate_detection` con el agente `csv_duplicate_detector` e indicar estas variables:

| Variable | Valor |
|---|---|
| `csv_jira_path` | `ejercicio-02-casos-duplicados/datos/jira_casos_existentes.csv` |
| `csv_gherkin_path` | `ejercicio-02-casos-duplicados/datos/gherkin_casos_importar.csv` |
| `output_report_path` | `ejercicio-02-casos-duplicados/salida/informe_duplicados.md` |
| `output_clean_csv_path` | `ejercicio-02-casos-duplicados/salida/gherkin_casos_limpio.csv` |

3. Revisar el informe y confirmar de forma interactiva qué duplicados se eliminan.

## Criterios de evaluación

- Se detectan los 10 duplicados reales con su caso Jira correcto.
- Los 5 casos con redacción parecida pero objetivo distinto no se marcan como duplicados.
- El CSV limpio conserva el formato original (separador, comillas y saltos de línea del campo Gherkin).
