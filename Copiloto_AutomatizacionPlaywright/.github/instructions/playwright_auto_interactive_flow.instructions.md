---
description: Flujo interactivo obligatorio para el agente Playwright Automation
applyTo: "**"
---

## 1. FLUJO INTERACTIVO OBLIGATORIO

El agente debe seguir siempre este patrón:

0. Analizar el framework completo y en profundidad para entender su estructura, patrones de diseño, convenciones de código y cobertura actual de pruebas
1. Analizar las pruebas existentes para la página/componente/feature actual
2. Analizar el escenario Gherkin que se necesita automatizar identificando los pasos que aún no están cubiertos por pruebas automatizadas, los datos necesarios y los endpoints a consumir. Identificar también cualquier riesgo o desafío técnico asociado a la automatización de ese escenario específico. Proponer mejoras concretas para abordar esos riesgos o desafíos técnicos, como cambios en el framework, nuevas utilidades o patrones de diseño que faciliten la implementación del escenario propuesto.
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

10. **ANÁLISIS AUTOMÁTICO DEL RESULTADO** (OBLIGATORIO):
    
    Tras la ejecución, el agente **DEBE ANALIZAR AUTOMÁTICAMENTE** el resultado basándose en:
    - **Exit Code del comando**: 0 = éxito, != 0 = fallo
    - **Salida del terminal**: Buscar patrones "scenario (X passed)", "scenario (X failed)", mensajes de error
    
    **CASO A: EJECUCIÓN EXITOSA** (Exit Code = 0 y "scenario (X passed)" visible)
    - Confirmar éxito al usuario: "Escenario ejecutado exitosamente ([X/Y] steps passed)"
    - Actualizar bitácora automáticamente
    - Preguntar: "¿Continuar con el siguiente escenario? (sí/no)"
    
    **CASO B: EJECUCIÓN FALLIDA** (Exit Code != 0 o "scenario (X failed)" visible)
    - Analizar automáticamente el error de la salida del terminal
    - Identificar la causa raíz del error
    - Presentar diagnóstico y opciones SIN PREGUNTAR primero si falló (ya es evidente)
    - Seguir protocolo de fallos (sección 4) directamente
    
    **REGLA CRÍTICA**: 
    - **NUNCA preguntar** "¿La prueba funcionó correctamente?" - El Exit Code y la salida ya lo indican
    - **ANALIZAR primero**, **INFORMAR después**, **PREGUNTAR solo para aprobar correcciones**

11. Si el análisis automático detecta fallo, seguir el protocolo de fallos automático (sección 4)

12. La bitácora se actualiza automáticamente tras éxito confirmado

---

## 2. FORMATO DE SALIDA INTERACTIVO

Siempre estructurar así:

- Feature: <nombre>
- Escenario: <nombre>
- Estado actual:
- Riesgos detectados:
- Código propuesto:
- Pregunta de aprobación:

Se debe mostrar siempre el código de la prueba propuesta, no solo la descripción.

---

## 3. RESUMEN DE ORDENES INTERACTIVAS DEL INGENIERO

**Comandos de aprobación**:
- **"sí" / "aprobar"** - Aprueba la acción propuesta
- **"no" / "rechazar"** - Rechaza la acción propuesta

**Comandos de flujo**:
- **"Aprobar escenario N (sí/no)"** - Aprueba o rechaza cada escenario propuesto
- **"Reconsiderar escenario N"** - Solicita mejoras a la implementación propuesta
- **"Ejecutar"** - Confirma que se puede ejecutar la prueba
- **"Continuar"** - Avanza al siguiente escenario tras éxito
- **"para"** - Detiene el flujo actual

**Nota:** Ya NO es necesario responder "error" tras una ejecución fallida - el agente lo detecta automáticamente analizando el Exit Code y la salida del terminal

**Comandos de sesión**:
- **"Finalizar sesión de trabajo"** - Cierra la sesión y actualiza bitácora
- **"Reiniciar sesión de trabajo"** - Retoma desde el último punto registrado
- **"Cambiar de página/componente/feature"** - Cambia el foco de trabajo

**IMPORTANTE**: 
- El copiloto **DEBE ESPERAR** confirmaciones antes de aplicar correcciones
- El copiloto **DEBE ANALIZAR AUTOMÁTICAMENTE** los resultados de ejecuciones (no preguntar si pasó/falló)
- **Exit Code y salida del terminal** son la fuente de verdad para determinar éxito/fallo

---

## 4. PROTOCOLO ANTE FALLOS Y BLOQUEOS (ANÁLISIS AUTOMÁTICO)

### 4.1 Protocolo automático de reintentos (OBLIGATORIO)

Cuando el análisis automático detecta un fallo (Exit Code != 0):

**PRIMER FALLO (Intento 1)**:
1. **ANÁLISIS AUTOMÁTICO del error** desde la salida del terminal
2. Extraer el mensaje de error exacto y la línea/paso que falló
3. Identificar la causa raíz probable (frame detached, selector no encontrado, timeout, etc.)
4. **PRESENTAR DIAGNÓSTICO AUTOMÁTICAMENTE**:
   ```
    Ejecución fallida - Análisis automático:
   
   Error detectado: [mensaje exacto del error]
   Paso que falló: [nombre del paso y línea]
   Causa identificada: [análisis de causa raíz]
   
   Propuesta de corrección:
   [descripción de la solución propuesta]
   [código modificado si aplica]
   
   ¿Aplicar esta corrección? (sí/no)
   ```
5. **ESPERAR respuesta del usuario**
6. Solo si el usuario aprueba, aplicar la corrección
7. **PREGUNTAR antes de reejecutar**: "¿Ejecutar nuevamente la prueba? (sí/no)"

**SEGUNDO FALLO (Intento 2)**:
1. **ANÁLISIS AUTOMÁTICO del nuevo error**
2. Comparar con el error anterior para determinar si es el mismo o diferente
3. **PRESENTAR DIAGNÓSTICO ACTUALIZADO AUTOMÁTICAMENTE**:
   ```
   Segundo fallo - Análisis automático:
   
   La corrección anterior no resolvió el problema.
   
   Nuevo error: [mensaje exacto]
   Comparación: [mismo error / error diferente]
   Nueva causa identificada: [análisis actualizado]
   
   Propuesta alternativa:
   [descripción de solución alternativa]
   [código modificado si aplica]
   
   ¿Aplicar esta corrección alternativa? (sí/no)
   ```
4. **ESPERAR respuesta del usuario**
5. Solo si el usuario aprueba, aplicar la corrección
6. **PREGUNTAR antes de reejecutar**: "¿Ejecutar nuevamente la prueba? (sí/no)"

**TERCER FALLO (Intento 3)**:
1. **DETENER inmediatamente** cualquier intento automático
2. **PRESENTAR DIAGNÓSTICO COMPLETO ESTRUCTURADO**:
   ```
   Tercer fallo consecutivo - Análisis completo:
   
   Historial de errores:
   - Intento 1: [error y corrección aplicada]
   - Intento 2: [error y corrección aplicada]  
   - Intento 3: [error actual]
   
   Causa raíz probable: [análisis profundo]
   
   Opciones de solución:
   A. [Corrección específica con implicaciones]
   B. Marcar escenario como @pendiente y continuar
   C. Requiere investigación manual / información adicional
   
   ¿Cómo deseas proceder? (A/B/C)
   ```
3. **ESPERAR respuesta del usuario**
4. **NO aplicar ningún cambio sin aprobación explícita**

**REGLAS CRÍTICAS ACTUALIZADAS**:
- **ANALIZAR AUTOMÁTICAMENTE** cada fallo usando Exit Code y salida del terminal
- **PRESENTAR DIAGNÓSTICO** antes de preguntar qué hacer
- **NUNCA ejecutar más de una vez sin preguntar**
- **NUNCA asumir que una corrección funcionará**
- **NUNCA aplicar múltiples correcciones en secuencia sin confirmación**
- **SIEMPRE esperar respuesta del usuario antes de cada acción**
- **SIEMPRE preguntar antes de reejecutar**
- **NUNCA preguntar** "¿Funcionó la prueba?" - Ya está en el Exit Code

### 4.2 Protocolo de escalado ante bloqueos

Escalar al ingeniero de forma inmediata (sin consumir intentos) cuando:
- El error de sintaxis apunta a un módulo o clase que no existe en el framework real
- El localizador no puede obtenerse del código fuente disponible en `${input:code_folder}`
- El escenario requiere acceso a un endpoint o dato que no está documentado ni accesible

En estos casos, presentar:
1. Descripción del bloqueo
2. Información mínima necesaria para desbloquearlo
3. Pregunta: "¿Puedes proporcionar esta información o cómo deseas continuar?"

No marcar el escenario como `@pendiente` sin informar primero al ingeniero del motivo.
