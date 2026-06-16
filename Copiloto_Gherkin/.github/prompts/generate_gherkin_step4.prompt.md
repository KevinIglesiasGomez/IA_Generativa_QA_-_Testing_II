---
agent: "Generador de escenarios Gherkin"
description: "Analizar documentación y generar casos de uso BDD"
model: "Claude Sonnet 4.6"
---

### Paso 4: Extracción de Casos de Uso y Generación de Características BDD

Ahora, usando el tipo de documento identificado **${input:document_type}** y el análisis completo de documentación (incluyendo datos de herramientas externas cuando estén disponibles), completa lo siguiente:

1. Revisar todos los documentos e identificar flujos de trabajo principales, reglas o casos de uso.
2. **Integrar datos de herramientas externas** (OPCIONAL solo si están disponibles) para enriquecer la comprensión y validación de casos de uso.
3. Hacer referencias cruzadas con el código del sistema disponible en el workspace.
4. Escribir un archivo `.feature` (en **Cucumber BDD**, en **español**) para cada caso funcional principal, usando la misma terminología que en los documentos.
5. **OBLIGATORIO** Para cada archivo .feature generado asegurate de **repasar las instrucciones de calidad y verificación** definidas en el archivo de instrucciones correspondiente y aplicar todos los criterios de aseguramiento de calidad definidos ANTES de pasar a la siguiente feature. No avances al siguiente archivo .feature hasta que el actual cumpla con TODOS los criterios de calidad y verificación. Esto es crucial para asegurar la efectividad y mantenibilidad de las características generadas.
6. Es **OBLIGATORIO** que en cada archivo .feature se generen **más de 15 escenarios** distintos que cubran:
   - Flujos positivos y negativos
   - Casos de limites
   - Validaciones de reglas de negocio
   - Interacciones de usuario clave
   - Validaciones de formulario
   6.1. **Si en la documentación hay Historias de Usuario**, asegúrate de generar escenarios que cubran TODOS los criterios de aceptación definidos en cada historia. Como minimo deben generarse 3 escenarios por historia. Prima calidad y cobertura sobre cantidad, pero no te limites a generar solo unos pocos escenarios por historia si los criterios de aceptación lo requieren.
   6.2. **Si en la documentación hay Historias de Usuario**, los escenarios deben estar ordenados en cada feature por el ID de la historia de usuario a la que correspondan.
7. **IMPORTANTE** No te limítes a 15 escenarios; si el caso de uso lo requiere, **genera tantos escenarios como sean necesarios para una cobertura completa**. No te limites a escenarios simples; incluye escenarios complejos que reflejen interacciones del mundo real.
8. **IMPORTANTE - Datos Sensibles**: Los escenarios BDD NO deben contener datos sensibles hardcodeados (credenciales, NIFs, matrículas, números de teléfono, códigos de reglas específicos, etc.). Usar referencias genéricas como "credenciales válidas", "un NIF válido", "una matrícula de prueba". Los datos reales deben configurarse en archivos `.env`.
9. **Guardar archivos .feature en **: **${input:e2e_repo}** (solo archivos .feature en este directorio)
10. **Crear un archivo INFORME.md comprensivo** en la raíz de **${input:e2e_repo}/** siguiendo TODOS los requisitos de documentación definidos en las instrucciones.
   - Incluir referencias a fuentes de herramientas externas cuando se usen
   - Documentar cualquier validación externa o referencias cruzadas aplicadas
   - Aclarar que la documentación técnica se usó solo como contexto
11. Aplicar TODAS las convenciones de nomenclatura, organización de archivos y estrategias de etiquetado definidas en las instrucciones.

---


