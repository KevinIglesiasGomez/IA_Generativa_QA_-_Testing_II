# Instrucciones para generar el informe para el Agente: Frontend Test Quality Analizer


## 1. Informe

Antes de interactuar con el ingeniero, debes generar un informe por cada página/componente/features

- Formato Markdown
- Directorio nuevo "informes/" en **la raiz del area de trabajo**.
- Nombre del fichero: "informe_[nombre_pagina_componente].md" (ej: informe_login.md)
- Descripción funcional de la página/componente
- Elementos identificados (formularios, botones, listas, etc.)
- TODAS las Pruebas existentes
- TODOS los Riesgos o gaps detectados según modelo UNIFIED
- Cobertura alcanzada por categoría
- NO incluir en el informe los escenarios propuestos.
- El informe debe ser extenso y sin limitaciones.

### 1.1 Actualización del informe

1. **OBLIGATORIO**: Al finalizar cada sesión de trabajo con el ingeniero, debes actualizar el **informe inicial** con las pruebas nuevas añadidas. Este proceso debe realizarse ANTES de cerrar la sesión e incluir:
   - Añadir los nuevos escenarios implementados en "PRUEBAS EXISTENTES" con subsecciones apropiadas según su categoría.
   - Actualizar los porcentajes de cobertura mostrando comparativa "Cobertura Anterior" vs "Cobertura Actual"
   - Actualizar la cobertura global mostrando progresión (ej: **47%** → **52%**)
   - Marcar como "GAP MITIGADO" o "COBERTURA PARCIAL" los riesgos detectados que fueron resueltos o mejorados.
   - Actualizar la priorización.waitForTimeout
   - El **informe inicial** NO debe tener una sección de siguientes pasos NI fechas de actualización, esta información se debe mantener en la **bitácora** de cambios para no sobrecargar el informe con información temporal que puede dificultar su lectura y comprensión a largo plazo. 

2. Adicionalmente por cada página/componente/feature nueva que se trabaje, debes generar otro fichero Markdown a modo de **bitácora** donde se vayan registrando los cambios realizados, las pruebas añadidas, los riesgos detectados o mitigados y los porcentajes de cobertura alcanzados. El objetivo es mantener un historial detallado de la evolución de la suite de pruebas a lo largo del tiempo sin que el **informe inicial** crezca de forma descontrolada. Esta bitácora debe ser clara, organizada y sin demasiado verbose. Actualiza esta bitácora en cada decisión importante tomada durante la sesión, como por ejemplo:
   - Implementación de un nuevo escenario de prueba
   - Identificación de un nuevo riesgo o gap
   - Mitigación de un riesgo existente
   - Actualización significativa en los porcentajes de cobertura

3. **Verificación**: Antes de finalizar la sesión, confirma que:
   - El **informe inicial** refleja TODAS las pruebas implementadas en la sesión
   - Los porcentajes de cobertura están actualizados
   - Los gaps mitigados están marcados correctamente
   - La priorización refleja el estado actual
   - La **bitácora** está sincronizada con el **informe inicial**

## 1.2 Reglas para la generación y actualización del informe y bitácora

- Antes de generar nada comprueba si ya existe un informe para esa página/componente, si es así, actualízalo en lugar de crear uno nuevo.
- El **informe inicial** no debe mantener un historial de cambios, este historial se debe mantener en los ficheros de **bitácora**, indicando claramente qué pruebas fueron añadidas en cada sesión de trabajo con el ingeniero.
- El **informe inicial** debe ser claro y organizado, facilitando la comprensión de la evolución de la suite de pruebas a lo largo del tiempo.
- **CRÍTICO**: Se debe actualizar la sección de "Riesgos detectados" en cada sesión, reflejando cualquier nuevo riesgo identificado o mitigado con las pruebas añadidas así como los porcentajes de cobertura alcanzados con las nuevas pruebas implementadas. 
- **IMPORTANTE**: La tabla de cobertura POISED debe mostrar:
  - Columna "Cobertura Anterior" con porcentaje inicial
  - Columna "Cobertura Actual" con porcentaje tras las implementaciones
  - Indicadores de mejora (+X%) en las descripciones
  - Cobertura global con formato: **X%** → **Y%** (+Z puntos porcentuales)
- La sección "Priorización de gaps" debe:
  - Tachar con ~~texto~~ los items completamente implementados
  - Marcar con ✅ antes del item tachado
  - Marcar con ⚠️ los items parcialmente implementados
  - Incluir referencia al número de escenario entre paréntesis (Escenario X)
- No debe existir sección "Siguientes pasos" en el **informe inicial**, esta información se debe mantener en la **bitácora** de cambios para no sobrecargar el informe con información temporal que puede dificultar su lectura y comprensión a largo plazo.
- Si la **bitácora** se vuelve demasiado extensa, considera organizarla en secciones o subsecciones para mantener la claridad.
- Si se cambia de página/componente/feature se debe generar un nuevo **informe inicial** específico, pero manteniendo el mismo formato y estructura que el informe anterior y una nueva **bitácora** de cambios para esa página/componente/feature.
- Nombre del fichero de bitácora: "bitacora_[nombre_pagina_componente].md" (ej: bitacora_login.md)

## 1.3 Comprobación de finalización de sesión

Antes de dar por finalizada una sesión de trabajo, verifica que has completado la actualización del **informe inicial** y de la **bitácora**.