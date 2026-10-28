---
description: Verificación y criterios de aseguramiento de calidad.
applyTo: "**/*.feature,**/features/**/*.feature"
---

## Objetivo

Instrucciones para verificar la calidad de los escenarios BDD generados y asegurar que cumplan con los estándares de Cucumber. Una vez generados los .features se deben realizar comprobaciones de calidad, validaciones y revisiones antes de considerar los escenarios como listos para su uso.
Es obligatorio que cada característica de Cucumber generada cumpla con los siguientes criterios de calidad y verificación para asegurar su efectividad y mantenibilidad:

### Criterios de Aseguramiento de Calidad

**COMPROBACIONES OBLIGATORIAS:**
- [ ] Todos los escenarios son **ejecutables** y **comprobables**
- [ ] Cada característica tiene al menos 1 escenario `@smoke` (ruta crítica)
- [ ] Las pruebas de valores límite están incluidas para entradas numéricas
- [ ] Los pasos usan **lenguaje declarativo** (evitar detalles de implementación)
- [ ] Los datos de prueba son **independientes** entre escenarios
- [ ] Las características son **cohesivas** y **bien organizadas**
- [ ] La estrategia de etiquetado es **consistente** en todas las características
- [ ] La documentación es **completa** y **accionable**
- [ ] Si se generan características a partir de **Historias de Usuario** con ID de Jira, cada escenario tiene la etiqueta de relación correspondiente en formato `@related:ID-1234`
- [ ] Cada paso nuevo ha sido **contrastado contra el inventario de steps ya existentes** (de esta ejecución y de `e2e_repo/features/`) antes de darse por válido, reutilizando o parametrizando pasos equivalentes en lugar de duplicar redacciones

---

### Validación y Revisión

**Lista de Verificación de Revisión:**
- [ ] Todos los escenarios siguen el patrón Given-When-Then (Dado-Cuando-Entonces)
- [ ] **Obligatorio** En cada feature. No hay saltos de línea innecesarios entre pasos
- [ ] **Obligatorio** En cada feature. No permitir iniciar pasos con palabras clave no estándar, solo pueden iniciarse con "Dado", "Cuando", "Entonces" o "Y"
  - **PROHIBIDO**: Pasos que comienzan con "O", "Pero", "E", "*", o cualquier otra palabra
  - **CORRECTO**: Usar "Y" para concatenar múltiples aserciones o condiciones alternativas
  - **VALIDACIÓN**: Ejecutar búsqueda regex `^    O ` en todos los .feature antes de finalizar
- [ ] Las etiquetas están correctamente asignadas
- [ ] El lenguaje es declarativo y libre de detalles de implementación
- [ ] Los escenarios son independientes entre sí
- [ ] Se incluyen tanto casos de éxito como de error
- [ ] La documentación está completa y actualizada
- [ ] Los nombres de archivos siguen las convenciones
- [ ] Se aplican los principios de reutilización de pasos