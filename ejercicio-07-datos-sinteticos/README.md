# Ejercicio 07 - Generación de datos sintéticos

Asset: `Asset_SyntheticData` (agente `Generador de Datos Sinteticos`).

## Objetivo

Generar, validar y documentar un dataset sintético de la cartera de seguros de Pruebas Seguros (clientes, pólizas y siniestros) con integridad referencial y reglas de negocio verificables.

## Datos

El Step 1 admite tres flujos; cada uno tiene su carpeta de entrada.

| Flujo | Carpeta | Contenido |
|---|---|---|
| A. Documentación funcional | `flujo-a-documentacion/documentation/` | `requisitos_negocio.md` con el dominio descrito en lenguaje natural |
| B. Instrucciones existentes | `flujo-b-instrucciones-existentes/` | `client_specific_data.instructions.md` completo, con dataset de ejemplo |
| C. Creación interactiva | Ninguna | Se responde a las preguntas del agente con los valores de `requisitos_negocio.md` |

Recomendación: ejecutar el flujo B primero (más rápido) y repetir con el flujo A para comparar el esquema que deduce el agente.

## Parámetros del Step 0

| Variable | Valor |
|---|---|
| `project_name` | `pruebas-seguros-cartera` |
| `data_purpose` | Funcional |
| `business_domain` | Seguros |
| `num_records` | `670` (200 clientes, 350 pólizas, 120 siniestros) |
| `locale` | `es_ES` |
| `output_formats` | CSV y JSON |
| `output_directory` | `ejercicio-07-datos-sinteticos/salida` |
| `client_instructions_file` | Flujo B: `ejercicio-07-datos-sinteticos/flujo-b-instrucciones-existentes/client_specific_data.instructions.md`; flujos A y C: vacío |
| `seed` | `42` |
| `scenario_distribution` | `70/20/10` |
| `date_range` | Últimos 5 años |
| `realism_level` | Alto |

Para el flujo A, copiar `flujo-a-documentacion/documentation/` al workspace `Asset_SyntheticData` o indicar su ruta cuando el agente la solicite.

## Cómo ejecutarlo

1. Abrir el workspace `Asset_SyntheticData`.
2. Lanzar por orden `generate_synthetic_data_step0` a `step4` con el agente `Generador de Datos Sinteticos`.
3. Revisar el informe de validación y el README generados en `salida/`.

## Criterios de evaluación

- Se generan 3 ficheros (`clientes`, `polizas`, `siniestros`) en CSV y JSON.
- La generación es reproducible: dos ejecuciones con `seed=42` producen los mismos datos.
- Todas las claves foráneas son válidas y los DNI únicos con letra de control correcta.
- Se cumplen las reglas cruzadas: vigencia de un año, plazos de declaración, siniestros dentro de vigencia y primas por rango de tipo.
- La distribución real se acerca a 70/20/10.
- No se incluyen datos personales reales.
