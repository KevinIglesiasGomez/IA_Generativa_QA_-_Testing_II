---
description: Flujo interactivo obligatorio para el agente Playwright Automation
applyTo: "**"
---

## 1. FLUJO INTERACTIVO OBLIGATORIO

El agente debe seguir siempre este patrón:

0. Analizar el framework completo y en profundidad para entender su estructura, patrones de diseño, convenciones de código y cobertura actual de pruebas
1. Analizar las pruebas existentes para la página/componente/feature actual
2. Analizar únicamente el escenario Gherkin que se necesita automatizar identificando los pasos que aún no están cubiertos por pruebas automatizadas, los datos necesarios y los endpoints a consumir. Identificar también cualquier riesgo o desafío técnico asociado a la automatización de ese escenario específico. Proponer mejoras concretas para abordar esos riesgos o desafíos técnicos, como cambios en el framework, nuevas utilidades o patrones de diseño que faciliten la implementación del escenario propuesto.
3. Proponer escenario **individual** con código
4. Preguntar:

"¿Aprobar escenario 1 (sí/no)?"

5. Solo continuar cuando el ingeniero lo apruebe
6. Si el ingeniero rechaza la implementación, ofrecer preguntas críticas para que indique el motivo del rechazo y que sugiera mejoras concretas a la automatización propuesta.

Nunca generar múltiples escenarios sin aprobación individual. El proceso debe ser incremental y validado paso a paso.

7. Una vez aprobado e implementado, **PREGUNTAR ANTES DE EJECUTAR**:
   "La implementación está lista. ¿Ejecutar la prueba ahora? (sí/no)"
   
8. Solo tras confirmación, ejecutar la prueba en modo visible (no-headless):
   ```bash
   npx cucumber-js --config cucumber.config.js src/features/Login.feature --tags "@<tag_del_escenario>"
   ```
   O el equivalente en scripts npm del proyecto.
   
9. **ESPERAR A QUE LA EJECUCIÓN TERMINE COMPLETAMENTE** antes de continuar.

10. Tras la ejecución, **PREGUNTAR OBLIGATORIAMENTE**:
    "¿La prueba funcionó correctamente? (sí/no/error)"
    
    - Si el usuario responde **"sí"**: Actualizar bitácora y continuar con siguiente escenario
    - Si el usuario responde **"no" o "error"**: Solicitar detalles del error o screenshot
    - **NUNCA asumir** el resultado de la ejecución, siempre esperar respuesta del usuario

11. Si hay error reportado por el usuario, seguir el protocolo de fallos (sección 4)

12. Actualizar bitácora de cambios solo tras confirmación de éxito

---

## 2. FORMATO DE SALIDA INTERACTIVO

Siempre estructurar así:

- Feature: <nombre>
- Escenario: <nombre>
- Estado actual:
- Código propuesto:
- Pregunta de aprobación:

Se debe mostrar siempre el código de la prueba propuesta, no solo la descripción.

---

## 3. RESUMEN DE ORDENES INTERACTIVAS DEL INGENIERO

**Comandos de aprobación**:
- **"sí" / "aprobar"** - Aprueba la acción propuesta
- **"no" / "rechazar"** - Rechaza la acción propuesta
- **"error"** - Indica que hubo un error en la ejecución

**Comandos de flujo**:
- **"Aprobar escenario N (sí/no)"** - Aprueba o rechaza cada escenario propuesto
- **"Reconsiderar escenario N"** - Solicita mejoras a la implementación propuesta
- **"Ejecutar"** - Confirma que se puede ejecutar la prueba
- **"Reintentar"** - Confirma que se puede volver a ejecutar tras corrección
- **"Continuar"** - Avanza al siguiente escenario tras éxito
- **"para"** - Detiene el flujo actual

**Comandos de sesión**:
- **"Finalizar sesión de trabajo"** - Cierra la sesión y actualiza bitácora
- **"Reiniciar sesión de trabajo"** - Retoma desde el último punto registrado
- **"Cambiar de página/componente/feature"** - Cambia el foco de trabajo

**IMPORTANTE**: El copiloto **DEBE ESPERAR** estas confirmaciones antes de proceder. **NUNCA asumir** la respuesta del usuario.

---

## 4. PROTOCOLO ANTE FALLOS Y BLOQUEOS

### 4.1 Protocolo estricto de reintentos (OBLIGATORIO)

Cuando un escenario falla al ejecutar:

**PRIMER FALLO (Intento 1)**:
1. Mostrar el error exacto al usuario
2. Analizar la causa raíz
3. **PREGUNTAR OBLIGATORIAMENTE**:
   "He detectado el siguiente error: [descripción]
   Causa identificada: [causa]
   Propuesta de corrección: [solución]
   
   ¿Aplicar esta corrección? (sí/no)"
4. **ESPERAR respuesta del usuario**
5. Solo si el usuario aprueba, aplicar la corrección
6. **PREGUNTAR antes de reejecutar**: "¿Ejecutar nuevamente la prueba? (sí/no)"

**SEGUNDO FALLO (Intento 2)**:
1. **DETENER inmediatamente** cualquier intento automático
2. Presentar diagnóstico estructurado al usuario:
   - Error exacto observado
   - Historial de correcciones intentadas
   - Causa raíz probable
   - Opciones de solución con sus implicaciones
3. **PREGUNTAR**: "¿Cómo deseas proceder?"
   - Opción A: Intentar otra corrección específica
   - Opción B: Marcar como @pendiente y continuar
   - Opción C: Investigación manual necesaria
4. **NO aplicar ningún cambio sin aprobación explícita**

**REGLAS CRÍTICAS**:
- **NUNCA ejecutar más de una vez sin preguntar**
- **NUNCA asumir que una corrección funcionará**
- **NUNCA aplicar múltiples correcciones en secuencia sin confirmación**
- **SIEMPRE esperar respuesta del usuario antes de cada acción**
- **SIEMPRE preguntar antes de reejecutar**

### 4.2 Protocolo de escalado ante bloqueos

Escalar al ingeniero de forma inmediata (sin consumir intentos y tokens) cuando:
- El error de sintaxis apunta a un módulo o clase que no existe en el framework real
- El localizador no puede obtenerse del código fuente disponible en `${input:code_folder}`
- El escenario requiere acceso a un endpoint o dato que no está documentado ni accesible

En estos casos, presentar:
1. Descripción del bloqueo
2. Información mínima necesaria para desbloquearlo
3. Pregunta: "¿Puedes proporcionar esta información o cómo deseas continuar?"

No marcar el escenario como `@pendiente` sin informar primero al ingeniero del motivo.
