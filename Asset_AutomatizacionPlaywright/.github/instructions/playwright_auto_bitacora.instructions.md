---
description: Instrucciones para generar la bitacora de automatización de pruebas en Playwright
applyTo: "**/automation_bitacora.md"
---

# Instrucciones para generar la bitacora para el agente: Playwright Automation

## 1. Instrucciones generales para la Bitácora de Automatización de Pruebas en Playwright
- La bitácora de automatización debe ser un documento vivo que se actualice con cada escenario automatizado.
- Para cada escenario automatizado, registra cualquier desafío o problema encontrado durante la automatización, así como las soluciones implementadas para resolver esos desafíos.
- **Mantén un registro de cada escenario automatizado**, incluyendo los pasos automatizados, los archivos modificados y cualquier cambio realizado en la lógica de negocio o en los localizadores de elementos web durante la automatización.
- Asegúrate de que la **bitácora de automatización esté actualizada** y documentada de manera clara. Esto es crucial para la trazabilidad y para futuras referencias en caso de que se necesiten ajustes o correcciones en los escenarios automatizados.
- **Los registros en la bitácora de automatización deben ser BREVES** pero lo suficientemente detallados para que cualquier ingeniero pueda entender el proceso de automatización, los cambios realizados y las decisiones tomadas durante la automatización de los escenarios del archivo .feature al framework Playwright.
TODO: Salta escenarios que no se hayan automatizado, pero registra el motivo de la omisión en la bitácora de automatización.

## 2. Formato de la Bitácora de Automatización
- Formato Markdown.
- Directorio nuevo: `automation_logs/`
- Un único archivo para todas las sesiones de trabajo: `automation_logs/automation_bitacora.md`. Si el archivo no existe, se crea. Si existe, el archivo se actualiza con cada escenario automatizado.
- La bitácora de automatización debe seguir un formato estructurado, con secciones claras para cada escenario automatizado, incluyendo:
  - **Nombre del escenario automatizado**: El nombre del escenario tal como aparece en el archivo .feature.
  - **Fecha de automatización**: La fecha en la que se realizó la automatización de ese escenario específico.
  - **Desafíos encontrados**: Breve. Cualquier desafío o problema encontrado durante la automatización de ese escenario específico.
  - **Soluciones implementadas**: Breve. Las soluciones o ajustes realizados para resolver los desafíos encontrados durante la automatización.
  - **Archivos modificados**: Breve. Una lista de los archivos que fueron modificados durante la automatización de ese escenario, incluyendo los archivos de definiciones de pasos, los Page Objects y los localizadores relacionados.
