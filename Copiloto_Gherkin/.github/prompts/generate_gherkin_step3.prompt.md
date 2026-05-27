---
agent: "Generador de escenarios Gherkin"
description: "Analizar documentación y generar casos de uso BDD"
---

### Paso 3: Identificación de Tipo de Documento

Después de completar la revisión completa de documentación e integración opcional de herramientas externas, analiza el contenido de los documentos ubicados en **${input:document_location}**.

Basado en su estructura, contenido e idioma, determina el tipo de documento más apropiado entre los siguientes:

- `user_manual`
- `business_requirements`
- `functional_specification`
- `technical_specification`
- `test_plan`
- `process_documentation`
- `system_manual`
- `tutorial`
- `user_stories`
- _(o sugiere una nueva etiqueta más apropiada si es necesario)_

Establece este valor como `${input:document_type}` y explica brevemente tu razonamiento.

**IMPORTANTE** Si la documentación es un **CSV con Historias de Usuario**, genera todos los escenarios BDD necesarios para probar cada una de las historias, usando el ID de Jira como etiqueta y siguiendo los criterios de aseguramiento de calidad definidos en `generate_gherkin_quality_verification.instructions.md`.

---