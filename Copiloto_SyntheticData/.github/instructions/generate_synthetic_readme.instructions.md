# Genera un README.md completo que incluya:

## Descripción del dataset

**AVISO**: Este dataset contiene datos sintéticos generados artificialmente para propósitos de testing y desarrollo. Ningún dato corresponde a personas, organizaciones o eventos reales. Cualquier similitud es puramente coincidental.


## Información General

- **Proyecto**: {config['dataset_info']['project']}
- **Dominio**: {config['dataset_info']['domain']}
- **Propósito**: {config['dataset_info']['purpose']}
- **Versión**: {config['dataset_info']['version']}
- **Fecha de Generación**: {config['dataset_info']['created_date']}
- **Generado por**: {config['dataset_info']['created_by']}

## Métricas de Calidad

| Dimensión | Score | Estado |
|-----------|-------|--------|
| **Completitud** | {quality_report['dimensions']['completeness']['score']}% | {quality_report['dimensions']['completeness']['status']} |
| **Validez** | {quality_report['dimensions']['validity']['score']}% | {quality_report['dimensions']['validity']['status']} |
| **Unicidad** | {quality_report['dimensions']['uniqueness']['score']}% | {quality_report['dimensions']['uniqueness']['status']} |
| **Consistencia** | {quality_report['dimensions']['consistency']['score']}% | {quality_report['dimensions']['consistency']['status']} |
| **Integridad Referencial** | {quality_report['dimensions']['referential_integrity']['score']}% | {quality_report['dimensions']['referential_integrity']['status']} |
| **SCORE GLOBAL** | **{quality_report['quality_score']}%** | **{quality_report['overall_status']}** |

## Estructura de Datos

## Formatos Disponibles

Este dataset está disponible en múltiples formatos:

- **CSV** (`datasets/csv/`) - Para uso general, importación a Excel, procesamiento con pandas
- **JSON** (`datasets/json/`) - Para APIs, aplicaciones web, estructura jerárquica
- **JSON Lines** (`datasets/jsonl/`) - Para procesamiento por lotes, streaming
- **SQL** (`datasets/sql/`) - Scripts de INSERT para cargar en base de datos
- **Excel** (`datasets/excel/`) - Para revisión manual y análisis (si <100K registros)

### Muestras

Archivos de muestra con los primeros 10 registros disponibles en `samples/` para revisión rápida.

## Cómo Usar los Datos

## Configuración de Generación

- **Semilla (seed)**: {config['generation_params']['seed']}
- **Locale**: {config['generation_params']['locale']}
- **Distribución de escenarios**:
  - Casos normales: {config['generation_params']['scenario_distribution']['normal']}%
  - Casos límite: {config['generation_params']['scenario_distribution']['boundary']}%
  - Casos excepcionales: {config['generation_params']['scenario_distribution']['exceptional']}%
- **Rango de fechas**: {config['generation_params']['date_range']['start']} a {config['generation_params']['date_range']['end']}

## Privacidad y Cumplimiento

✓ **Todos los datos son completamente ficticios**
✓ No se utilizaron datos personales reales
✓ Los DNI/NIE/NIF no son reales ni válidos
✓ Los emails utilizan dominios ficticios (example.com)
✓ Los teléfonos están en rangos ficticios
✓ Cumple con GDPR y normativas de protección de datos
 
## Archivos Incluidos

## Problemas Conocidos y Limitaciones

## Changelog

### v1.0.0 - Generación Inicial
- Generación inicial del dataset
- Todas las entidades incluidas
- Validaciones de calidad ejecutadas


## Soporte y Contacto

Para preguntas, problemas o mejoras, por favor contacta al equipo de QA.

## Licencia y disclaimer


---