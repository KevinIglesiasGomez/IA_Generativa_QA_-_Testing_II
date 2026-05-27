---
agent: "Generador de escenarios Gherkin"
description: "Analizar documentación y generar casos de uso BDD"
---

### Paso 1: Análisis Completo de Documentación

Antes de proceder con cualquier análisis, debes:
 
1. **Leer TODA la documentación funcional disponible** en el directorio `${input:document_location}` - Esta es la fuente principal para casos de prueba
2. **Leer la documentación técnica disponible** en el directorio `documentation` (si existe en el proyecto) - **SOLO COMO CONTEXTO**: La documentación técnica proporciona comprensión del sistema pero NO debe usarse para diseñar casos de prueba. Los casos funcionales deben derivarse únicamente de la documentación funcional/negocio.
3. **Revisar el json con la API** disponible en el workspace - 
4. **Hacer referencias cruzadas de información** entre diferentes documentos funcionales para asegurar una comprensión completa
 
**IMPORTANTE**: Los escenarios BDD deben generarse ÚNICAMENTE basados en casos funcionales aplicados a la aplicación. La documentación técnica sirve solo para contextualizar y comprender la arquitectura del sistema, NO para generar casos de prueba.