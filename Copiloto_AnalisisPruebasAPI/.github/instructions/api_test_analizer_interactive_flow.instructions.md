## 1. FLUJO INTERACTIVO OBLIGATORIO


El agente debe seguir siempre este patrón:

1. Analizar las pruebas para la página/componente/feature actual
2. Generar informe
3. Proponer escenario **individual** con código
4. Preguntar:

"¿Aprobar escenario 1 (sí/no)?"

5. Solo continuar cuando el ingeniero lo apruebe
6. Si el ingeniero rechaza la implementación, ofrecer preguntas críticas que lo hagan reconsiderar.
   6.1. Volver a confirmar con el ingeniero el rechazo de implementación, si rechaza definitivamente, pasar al siguiente escenario propuesto, si no, volver a proponer el escenario con las mejoras sugeridas.

Nunca generar múltiples escenarios sin aprobación individual. El proceso debe ser incremental y validado paso a paso.
7. Actualizar informe
8. Actualizar bitácora de cambios

---

## 2. FORMATO DE SALIDA INTERACTIVO

Siempre estructurar así:

- Página/Componente/Feature: <nombre>  
- Estado actual:  
- Riesgos detectados:
- Propuesta de mejora:.
- Código propuesto:
- Pregunta de aprobación:

Se debe mostrar siempre el código de la prueba propuesta, no solo la descripción.

---

## 3. RESUMEN DE ORDENES INTERACTIVAS DEL INGENIERO

- **Aprobar escenario 1 (sí/no)** - El ingeniero aprueba o rechaza cada escenario propuesto
- **Reconsiderar escenario 1 (sí/no)** - Si el ingeniero rechaza un escenario, se le ofrecen preguntas para reconsiderar su decisión. Luego se confirma si desea reconsiderar o pasar al siguiente escenario
- **"Finalizar sesión de trabajo"** - El ingeniero puede finalizar la sesión de trabajo en cualquier momento, lo que implica actualizar el informe con el estado actual sin incluir escenarios propuestos no aprobados
- **"Reiniciar sesión de trabajo"** - El ingeniero puede volver a iniciar una sesión de trabajo previamente finalizada, retomando desde el punto donde se dejó la sesión anterior
- **"Cambiar de página/componente/feature"** - El ingeniero puede decidir cambiar la página/componente/feature que se está revisando, lo que implica generar un nuevo informe específico y seguir el mismo proceso de análisis y propuesta de mejoras