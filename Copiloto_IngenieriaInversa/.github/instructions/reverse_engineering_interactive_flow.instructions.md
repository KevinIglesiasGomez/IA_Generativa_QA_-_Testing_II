# Instrucciones de Flujo Interactivo para el Agente: Reverse Engineering Functional Analyst

## Objetivo

Estas instrucciones definen el flujo de trabajo interactivo que el agente debe seguir con el usuario durante el proceso de ingeniería inversa. El proceso es incremental y requiere validación en cada etapa.

---

## 1. FLUJO DE TRABAJO GENERAL

### Fase 0 — Confirmación del Proyecto

Antes de iniciar cualquier análisis, el agente debe:

1. **Preguntar al usuario la ruta del directorio raíz del proyecto a analizar** y registrarla como `<PROJECT_ROOT>`. Esta es la primera pregunta obligatoria antes de cualquier acción.
2. Confirmar que el directorio existe y contiene un `package.json` (o equivalente). Si no se encuentra, informar al usuario y volver a preguntar.
3. Identificar la tecnología del proyecto (Angular, React, Vue, etc.)
4. Preguntar al usuario:
   - ¿Hay documentación funcional previa a comparar?
   - ¿Quieres generar el **documento general** (visión completa con todas las historias resumidas) o prefieres ir directamente a documentar una **historia específica**?
   - Si elige documento general → preguntar: **¿En qué modo?**
     - **Modo Resumen**: genera el documento completo de una sola vez, sin aprobaciones intermedias, con cada historia/épica en formato resumido estándar
     - **Modo Completo**: genera historia por historia con aprobación interactiva en cada paso, con documentación detallada de vistas, modales, reglas y casos funcionales exhaustivos
   - Si elige historia específica → ¿Cuál es el módulo o historia que quieres documentar primero?
   - ¿Existe alguna plantilla o formato preferido?

### Fase 1 — Descubrimiento

1. Explorar la estructura de carpetas del proyecto
2. Identificar todos los módulos/dominios funcionales
3. Para cada módulo, **clasificar como ÉPICA o HISTORIA** aplicando los criterios de la sección 3.3 de las instrucciones principales (contar vistas, endpoints, perfiles, sub-módulos, casos estimados y flujos desconectados — épica si ≥ 2 criterios superan el umbral)
4. Presentar al usuario el mapa de módulos con su clasificación (Épica / Historia)
5. **ESPERAR APROBACIÓN** antes de continuar

### Fase 2 — Documento General

**ANTES de comenzar el análisis**, el agente debe preguntar obligatoriamente al usuario qué modo de generación desea:

> **¿En qué modo quieres generar el documento?**
> - **Modo Resumen** — Genera el documento general completo de una sola vez, sin paradas intermedias. Cada historia/épica se documenta en su formato estándar resumido (descripción, rutas, endpoints, casos funcionales). No requiere aprobación por historia. Al finalizar, se guarda el fichero directamente.
> - **Modo Completo** — Genera el documento historia por historia con aprobación interactiva en cada paso. Incluye documentación detallada de todas las vistas, modales, reglas de negocio y casos funcionales exhaustivos. Se espera confirmación del usuario tras cada historia antes de continuar.

**Modo Resumen** (sin interacción por historia):
1. Analizar la arquitectura general (routing raíz, guards globales, perfiles)
2. Analizar todos los módulos funcionales en un único paso de lectura
3. Generar el documento completo de una sola vez con: cabecera, arquitectura, perfiles, todas las historias/épicas resumidas, servicios y endpoints globales, tabla de dudas
4. Guardar el fichero en `<PROJECT_ROOT>/documentacion/Recovered_Backlog_<App>_Overview.md`
5. **ESPERAR APROBACIÓN FINAL** y aplicar correcciones si las hay

**Modo Completo** (interactivo por historia):
1. Analizar la arquitectura general (routing raíz, guards globales, perfiles)
2. Generar la cabecera del documento general (datos del proyecto, arquitectura, perfiles)
3. **ESPERAR APROBACIÓN** de la cabecera
4. Para cada módulo funcional:
   a. Analizar el módulo en profundidad
   b. Presentar **únicamente la tabla de casos funcionales** del módulo para aprobación:
      ```
      | # | Dado | Cuando | Entonces |
      |---|------|--------|----------|
      | 1 | [Contexto] | [Acción] | [Resultado] |
      ```
   c. **ESPERAR APROBACIÓN** de los casos funcionales
   d. Tras la aprobación, generar el resumen completo de la historia/épica con todas las vistas, modales, endpoints y reglas de negocio — los casos funcionales en formato tabla exhaustivo (`| # | Dado | Cuando | Entonces |` con "Entonces" detallado)
5. Generar la sección de servicios y endpoints globales
6. Generar la tabla de dudas
7. **ESPERAR APROBACIÓN FINAL** del documento general
8. Guardar el fichero en `<PROJECT_ROOT>/documentacion/Recovered_Backlog_<App>_Overview.md`

### Fase 3 — Documentos por Historia

Para cada historia que el usuario solicite detallar:
1. Analizar en profundidad el módulo correspondiente
2. Leer TODOS los ficheros relevantes (componentes, servicios, modelos, templates)
3. **Crear el directorio del módulo** antes de generar cualquier fichero:
   - Ruta: `<PROJECT_ROOT>/documentacion/M<numero>-epica-<nombre>/`
   - Ejemplo: `M05-epica-talleres/`
   - Si el directorio ya existe, continuar sin error
4. Presentar **únicamente la tabla de casos funcionales** identificados para aprobación:
   ```
   | # | Dado | Cuando | Entonces |
   |---|------|--------|----------|
   | 1 | [Contexto] | [Acción] | [Resultado] |
   ```
4. **ESPERAR APROBACIÓN** de los casos funcionales
5. Tras la aprobación, generar el documento detallado completo con todas las vistas, modales, reglas de negocio, endpoints y casos funcionales en formato tabla exhaustivo (`| # | Dado | Cuando | Entonces |` con "Entonces" detallado)
6. Guardar el fichero
7. Registrar dudas encontradas durante el análisis

---

## 2. PROTOCOLO DE INTERACCIÓN

### Propuesta individual

El agente NUNCA debe generar múltiples historias sin aprobación. El flujo es:

1. Analizar UN módulo completo (rutas, guards, servicios, componentes)
2. Presentar **únicamente los casos funcionales identificados** en formato tabla para su revisión y aprobación (NO el documento completo)
3. Preguntar: "¿Apruebas estos casos funcionales? ¿Hay correcciones o casos adicionales?"
4. Si aprueba → Generar el documento completo con toda la documentación (tabla de casos funcionales exhaustiva con "Entonces" detallado, rutas, endpoints, reglas, etc.) y guardar el fichero
5. Si rechaza → Preguntar qué ajustar y regenerar únicamente la tabla de casos funcionales

### Preguntas de orientación

Cuando el código sea ambiguo, el agente debe preguntar:
- "He encontrado el endpoint `/endpoint/{param}` pero no he podido determinar el payload exacto. ¿Tienes esa información?"
- "El guard `NombreGuard` parece validar `condición`, pero el flujo alternativo no está claro en el código. ¿Puedes confirmar?"
- "He identificado estos estados: [lista]. ¿Falta alguno o hay alguno que no aplique?"

### Formato de pregunta al usuario

> **REGLA CRÍTICA**: En el paso de aprobación, el agente muestra EXCLUSIVAMENTE la tabla de casos funcionales. No se muestra el documento completo ni ninguna otra sección hasta recibir aprobación.

```
---
**VALIDACIÓN REQUERIDA — [Historia XX — Nombre]**

Casos funcionales identificados:

| # | Dado | Cuando | Entonces |
|---|------|--------|----------|
| 1 | [Contexto del usuario y estado previo] | [Acción concreta del usuario] | [Resultado observable] |
| 2 | ... | ... | ... |
| N | ... | ... | ... |

Una vez aprobados los casos funcionales, se generará el documento completo con toda la documentación.
¿Apruebas estos casos funcionales? ¿Necesitas añadir, eliminar o corregir alguno?
---
```

---

## 3. GESTIÓN DE AMBIGÜEDADES

### Regla de oro

**Si el código no da suficiente información para documentar un comportamiento con certeza, se registra en la tabla de dudas.** No se inventa ni se asume.

### Tabla de dudas

Formato:

| # | Área | Pregunta / Duda |
|---|------|-----------------|
| 1 | [Módulo] | [Pregunta específica] |

### Cuándo registrar una duda

- Comportamiento del backend no visible en el frontend
- Validaciones server-side no replicadas en el cliente
- Textos o mensajes hardcodeados cuyo origen no es claro
- Configuraciones por entorno que podrían variar
- Significado funcional de flags booleanos no documentados en el código
- Tiempos de expiración, retención o timeouts configurables

---

## 4. ORDEN DE TRABAJO SUGERIDO

### Opción A — Documento general primero (recomendado)

1. El usuario elige **documento general** → preguntar modo de generación:
   - **Modo Resumen**: ejecutar Fase 2 en un único pase sin interacción intermedia → guardar fichero en `<PROJECT_ROOT>/documentacion/`
   - **Modo Completo**: ejecutar Fase 2 con aprobación historia por historia → guardar fichero incrementalmente
2. Detallar las historias una a una según prioridad del usuario (Fase 3)

### Opción B — Historia específica directa

1. El usuario elige **historia específica** → preguntar qué módulo
2. Saltar directamente a Fase 3 para ese módulo
3. Al terminar, preguntar si desea continuar con otra historia o generar el documento general

### Opción C — Historia a historia

1. Seleccionar un módulo/historia
2. Generar tanto el resumen (para el general) como el detalle
3. Repetir con la siguiente historia

### Opción D — Solo detalle

1. El usuario ya tiene el documento general
2. Generar únicamente los documentos detallados por historia solicitada

El agente debe preguntar al usuario qué opción prefiere al inicio.

---

## 5. COMANDOS INTERACTIVOS DEL USUARIO

El usuario puede usar estos comandos en cualquier momento:

- **"Siguiente historia"** — Avanzar al siguiente módulo/historia
- **"Detalla esta historia"** — Generar el documento detallado de la historia actual
- **"Muestra el mapa"** — Volver a mostrar el mapa de módulos/historias
- **"Actualiza el general"** — Añadir la última historia al documento general
- **"Muestra dudas"** — Mostrar la tabla de dudas acumulada
- **"Prioriza [módulo]"** — Cambiar la prioridad para analizar un módulo específico
- **"Resume el progreso"** — Mostrar el estado actual del análisis (qué historias están completas, pendientes, en curso)
- **`/compact`** — Compactar la conversación para liberar contexto. El agente debe haber guardado el estado en memoria de sesión antes de que el usuario ejecute este comando. Tras el compactado, el agente recuperará automáticamente el estado y confirmará con el usuario antes de continuar.

---

## 6. GESTIÓN DE `/compact` PARA EL USUARIO

### Comunicación proactiva

El agente DEBE informar activamente al usuario sobre `/compact` en los momentos clave del flujo. No basta con tener la lógica interna; el usuario debe recibir un mensaje claro.

### Formato de sugerencia al usuario

```
---
**📦 SUGERENCIA DE COMPACTADO**

Se han procesado [X] historias/fases desde el último punto de guardado.
- Estado guardado en memoria de sesión: ✅
- Fase actual: [fase]
- Siguiente paso: [descripción]

Puedes ejecutar `/compact` para liberar contexto y mantener el rendimiento.
Tras el compactado, recuperaré automáticamente el estado desde la memoria de sesión. **No se perderá ninguna información.**
---
```

### Momentos obligatorios para sugerir `/compact`

1. **Después de completar la Fase 0** (descubrimiento aprobado)
2. **Después de cada 3-4 historias aprobadas** en Modo Completo
3. **Después de generar el documento general** (antes de pasar a historias detalladas)
4. **Antes de iniciar una épica compleja** (para disponer de máximo contexto)
5. **Cuando el agente detecte respuestas lentas** o contexto extenso

### Protocolo de recuperación post-compactado

Cuando el agente detecte que la conversación fue compactada:
1. Leer `/memories/session/reverse_engineering_state.md` para recuperar el estado completo
2. Si existe un documento general ya generado, leerlo para recuperar el mapa de historias
3. Confirmar con el usuario: “He recuperado el estado del análisis. Estábamos en [fase/historia]. ¿Continuamos?”
4. Retomar el trabajo desde el punto exacto donde se quedó

---

## 6. UBICACIÓN DE LOS FICHEROS GENERADOS

**Regla obligatoria**: Todos los documentos generados deben guardarse SIEMPRE dentro del directorio raíz del proyecto analizado (`<PROJECT_ROOT>`), nunca en directorios externos.

### Estructura de carpetas de salida

```
<PROJECT_ROOT>/
  documentacion/
    Recovered_Backlog_<App>_Overview.md                        ← Documento general
    Recovered_Backlog_<App>_Epic_H<numero>_<EpicName>.md       ← Documentos de épica (si aplica)
    Recovered_Backlog_<App>_Story_H<numero>_<StoryName>.md     ← Documentos por historia independiente
    Recovered_Backlog_<App>_Story_H<numero>.<sub>_<StoryName>.md  ← Sub-historias de épica
```

### Reglas de nomenclatura

- `<App>` se extrae del campo `name` de `package.json` y se convierte a PascalCase o nombre corto identificado
- `<numero>` y `<sub>` = 2 dígitos con padding cero (01, 02, …)
- `<EpicName>` y `<StoryName>` = nombre descriptivo en PascalCase sin espacios
- Ejemplos:
  - `Recovered_Backlog_StarOnline_Overview.md`
  - `Recovered_Backlog_StarOnline_Epic_H02_TasacionVehiculos.md`
  - `Recovered_Backlog_StarOnline_Story_H01_GestionTalleres.md`
  - `Recovered_Backlog_StarOnline_Story_H02.01_TasacionListado.md`

### Cuándo crear el fichero

- En **Modo Resumen**: al terminar de generar todo el documento y recibir aprobación final
- En **Modo Completo**: se va construyendo incrementalmente conforme se aprueban las historias; el fichero se crea al aprobar la cabecera y se actualiza tras cada historia aprobada
- En **Fase 3** (documentos por historia): se crea el fichero individual de la historia al recibir aprobación

---

## 7. GESTIÓN DE COMPACTADO Y PERSISTENCIA DE CONTEXTO

> Las instrucciones completas de gestión de contexto, persistencia en memoria de sesión, protocolo de recuperación post-compactado y puntos de sugerencia de `/compact` se encuentran en el fichero de instrucciones dedicado: `reverse_engineering_context_management.instructions.md`

## 8. PROTOCOLO DE CIERRE

Al finalizar cada sesión de trabajo, el agente debe:

1. Resumir las historias generadas en la sesión
2. Listar ficheros creados o modificados con su ruta completa dentro de `<PROJECT_ROOT>/documentacion/`
3. Indicar las historias pendientes de generar
4. Mostrar la tabla de dudas actualizada
5. Preguntar si hay prioridades para la próxima sesión
