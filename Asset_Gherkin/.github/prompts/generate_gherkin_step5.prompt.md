---
agent: "Generador de escenarios Gherkin"
description: "Revisión semántica final de reutilización de steps entre todas las features generadas"
model: "Claude Sonnet 5"
---

### Paso 5: Revisión Semántica de Reutilización de Steps (**obligatorio**)

Una vez generados y validados individualmente TODOS los archivos `.feature` de la ejecución actual en `e2e_repo/features/`, realiza una pasada de consolidación:

1. **Leer todos los archivos `.feature`** generados en esta ejecución (y los preexistentes en `e2e_repo/features/` si los hubiera).
2. **Extraer el listado completo de pasos** (Dado/Cuando/Entonces/Y) de todas las features.
3. **Detectar semánticamente pasos equivalentes** redactados de forma distinta entre features (mismo comportamiento, distinta literalidad: sinónimos, orden de palabras, valores concretos en vez de placeholders).
4. Para cada grupo de pasos equivalentes detectado:
   - Definir una **única redacción parametrizada** siguiendo la sección "Reutilización Sistemática de Steps" de `generate_gherkin_standards.instructions.md`.
   - **Reescribir** todas las ocurrencias en todas las features afectadas para usar esa redacción unificada, sustituyendo los valores concretos por los placeholders correspondientes.
5. Tras la unificación, **repasar de nuevo cada feature modificada** contra `generate_gherkin_quality_verification.instructions.md` para confirmar que sigue cumpliendo todos los criterios de calidad.
6. **Documentar en el `INFORME_<fecha_hora>.md`** un resumen de los pasos unificados/parametrizados como resultado de esta revisión (step original por feature y step final reutilizado).

**IMPORTANTE**: No des por finalizada la generación hasta completar esta revisión. Este paso es el que garantiza que la reutilización de steps se aplique de forma consistente entre todas las features de la entrega, no solo dentro de cada una.
