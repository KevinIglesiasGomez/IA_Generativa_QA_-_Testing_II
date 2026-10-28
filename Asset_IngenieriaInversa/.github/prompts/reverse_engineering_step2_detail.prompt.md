---
agent: "reverse_engineering_analyst"
tools: ["search", "edit/editFiles", "edit/createDirectory"]
description: "Paso 2: Generación del documento detallado de una historia de usuario específica"
model: "Claude Sonnet 4.6"
---

# Prompt Step 2: Generación del Documento Detallado por Épica o Historia

## 0. ARQUITECTURA COGNITIVA INTERNA

Antes de generar el documento detallado, el agente ejecuta internamente las siguientes fases cognitivas:

### ROL A: Lector Profundo de Código
Objetivo: Extraer toda la información funcional del módulo.

- Leer TODOS los ficheros del módulo en orden: routing → enums → modelos → guards → servicios → stores → páginas → modales
- Identificar cada elemento interactivo, condicional de estado y llamada API
- Documentar relaciones entre componentes

### ROL B: Redactor Funcional
Objetivo: Transformar la información técnica en documentación funcional.

Por cada vista:
- Construir casos funcionales exhaustivos en formato Dado/Cuando/Entonces
- Incluir TODOS los elementos de interfaz con sus propiedades exactas
- Garantizar que los 3 estados de interfaz (CARGANDO/SIN DATOS/CON DATOS) están documentados

### ROL C: Verificador de Trazabilidad
Objetivo: Garantizar que todo lo documentado es verificable.

- ¿Cada caso funcional tiene origen verificable en el código?
- ¿Las reglas de negocio están expresadas en el código fuente?
- Registrar en tabla de dudas cualquier ambigüedad

### ROL D: Inspector de Calidad Final
Objetivo: Validar completitud antes de entregar.

- Verificar métricas de cobertura: rutas, endpoints, vistas, casos funcionales
- Confirmar coherencia con documento general (si existe)
- Preparar reporte de calidad para el usuario

## Objetivo

Este prompt genera el documento detallado correspondiente al módulo analizado:
- Si el módulo es una **Épica** → genera `Recovered_Backlog_<App>_Epic_H<numero>_<EpicName>.md` y planifica las sub-historias
- Si el módulo es una **Historia independiente** → genera `Recovered_Backlog_<App>_Story_H<numero>_<StoryName>.md`
- Si el módulo es una **sub-historia de Épica** → genera `Recovered_Backlog_<App>_Story_H<numero>.<subnumero>_<StoryName>.md`

> `<App>` = nombre corto en PascalCase. `<numero>` = 2 dígitos. `<subnumero>` = 2 dígitos. Ejemplos: `Recovered_Backlog_StarOnline_Epic_H02_TasacionVehiculos.md`, `Recovered_Backlog_StarOnline_Story_H01_GestionTalleres.md`, `Recovered_Backlog_StarOnline_Story_H02.01_TasacionListado.md`

## Instrucciones

### Fase 0 — Clasificación del módulo (OBLIGATORIA)

Antes de iniciar el análisis, determinar si el módulo es una **Épica** o una **Historia** contando cuántos de estos indicadores superan su umbral:

| Indicador | Umbral para ser Épica |
|-----------|-----------------------|
| Vistas / páginas independientes | > 5 |
| Endpoints en los servicios del módulo | > 10 |
| Perfiles con flujos completamente distintos | > 2 |
| Sub-módulos con routing propio (lazy load) | Sí |
| Estimación de casos funcionales totales | > 25 |
| Flujos completamente desconectados entre sí | Sí |

**Si 2 o más indicadores superan el umbral → ÉPICA.**
**Si 0 o 1 indicadores superan el umbral → HISTORIA.**

**Si es ÉPICA:**
1. Identificar los flujos funcionales independientes del módulo
2. Proponer la descomposición en sub-historias con nombres descriptivos
3. **ESPERAR APROBACIÓN** de la descomposición
4. Generar el fichero de Épica (ver sección 1.8 de las instrucciones de generación de documentos)
5. Documentar cada sub-historia de forma independiente con este mismo proceso

**Si es HISTORIA (o sub-historia):**
Continuar directamente con la Fase 1.

### Fase 1 — Análisis profundo del módulo

Leer en este orden TODOS los ficheros del módulo:

1. **Routing**: `*-routing.module.ts` → rutas completas con guards y parámetros
2. **Enums**: `*.enum.ts` → todos los estados, tipos y catálogos
3. **Modelos**: `*.model.ts` / `*.interface.ts` → estructuras de datos completas
4. **Guards**: `*.guard.ts` → condiciones, redirects, side effects
5. **Servicios**: `*.service.ts` / `*.adapter.ts` → TODOS los endpoints con payloads
6. **Stores**: `*.store.ts` → estado, acciones, selectores
7. **Páginas**: `*.page.ts` + `*.page.html` → lógica + UI completa
8. **Modales**: modal components → formularios, acciones, cierre
9. **Pipes/Directivas**: formatos de datos relevantes

### Fase 2 — Generación del documento detallado

El documento debe incluir:

1. **Cabecera** con: aplicación, perfil, módulo, guards, fecha
2. **Índice detallado** con anclas a TODAS las secciones
3. **Descripción general** del módulo
4. **Rutas disponibles** — tabla COMPLETA
5. **Casos funcionales** — en formato tabla ANTES de los servicios:
   ```
   | # | Dado | Cuando | Entonces |
   |---|------|--------|----------|
   | 1 | [Contexto del usuario, estado previo, pasos para llegar. *Accede a `/ruta`*] | [Acción concreta indicando botón/elemento, vista y funcionalidad] | [Resultado detallado: vista mostrada, todos los elementos de interfaz con texto/placeholder/valor por defecto/estado/estilo, estados CARGANDO/SIN DATOS/CON DATOS, llamadas API `MÉTODO /ruta/endpoint`, navegación resultante, notas importantes] |
   ```
6. **Servicios API implicados** — tabla COMPLETA
7. **Estados** (si aplica) — tabla con código, clase CSS, descripción
8. **Por cada vista/componente principal**:
   - Sección con la ruta de la vista
   - Casos funcionales DETALLADOS en formato tabla:
     ```
     | # | Dado | Cuando | Entonces |
     |---|------|--------|----------|
     | N | [Contexto del usuario y pasos desde inicio de sesión para el primer caso de cada vista. *Accede a `/ruta`*] | [Acción concreta indicando botón/elemento, vista y funcionalidad] | [Descripción de la cabecera (botones, título, iconos); ESTADOS DE LA INTERFAZ: CARGANDO / SIN DATOS / CON DATOS con descripción; todos los elementos con propiedades exactas; llamadas API: `MÉTODO /endpoint`; navegación resultante; gestos disponibles (swipe, pull-to-refresh)] |
     ```
9. **Por cada modal**:
   - Cómo se abre
   - Cabecera del modal
   - Campos del formulario (tipo, validación, longitud máxima)
   - Botones de acción (texto, color, comportamiento)
   - API calls al confirmar
10. **Tabla de condiciones y reglas de negocio**

### Fase 3 — Validación

Presentar **únicamente la tabla de casos funcionales** identificados para revisión y aprobación. No se muestra el documento completo en este paso:

```
---
**VALIDACIÓN REQUERIDA — [Historia XX — Nombre]**

Casos funcionales identificados:

| # | Dado | Cuando | Entonces |
|---|------|--------|----------|
| 1 | [Contexto del usuario y estado previo] | [Acción concreta del usuario] | [Resultado observable] |
| 2 | ... | ... | ... |
| N | ... | ... | ... |

Una vez aprobados los casos funcionales, se generará el documento completo con:
- Documento: [nombre del fichero según tipo: Épica / Historia / Sub-historia]
- Todas las secciones: descripción, rutas, casos funcionales detallados, endpoints, estados, vistas, modales, reglas de negocio, tabla de dudas

¿Apruebas estos casos funcionales? ¿Necesitas añadir, eliminar o corregir alguno?
---
```

### Fase 4 — Generar fichero

1. Determinar `<App>`, `<numero>` y el nombre descriptivo a partir del módulo analizado
2. Crear la carpeta `documentacion/` en la raíz del proyecto analizado si no existe
3. Crear el fichero dentro de esa carpeta con el nombre que corresponda según el tipo:
   - Épica: `Recovered_Backlog_<App>_Epic_H<numero>_<EpicName>.md`
   - Historia independiente: `Recovered_Backlog_<App>_Story_H<numero>_<StoryName>.md`
   - Sub-historia de épica: `Recovered_Backlog_<App>_Story_H<numero>.<subnumero>_<StoryName>.md`
4. Confirmar la creación con la ruta completa y el nombre de fichero exacto utilizado

## Reglas

- **FLUJO DE APROBACIÓN**: En la Fase 3 mostrar ÚNICAMENTE la tabla de casos funcionales. Solo tras la aprobación del usuario se genera el documento completo. Nunca mostrar el documento completo antes de la aprobación.
- **FORMATO TABLA en todos los contextos**: Los casos funcionales usan SIEMPRE tabla `| # | Dado | Cuando | Entonces |`, tanto en la propuesta de aprobación como en el documento final.
- La diferencia entre ambos contextos es el nivel de detalle del campo "Entonces":
  - **En la propuesta de aprobación**: "Entonces" es un resumen conciso (una frase) del resultado observable
  - **En el documento generado**: "Entonces" es exhaustivo: vista, todos los elementos de interfaz con propiedades exactas (texto, placeholder, valor por defecto, estado, estilo), estados (CARGANDO/SIN DATOS/CON DATOS), llamadas API, navegación y notas
- Los casos funcionales en formato tabla aparecen ANTES de los servicios/endpoints en el documento final
- Documentar los 3 estados de interfaz para CADA vista principal
- Incluir las llamadas API en formato `MÉTODO /ruta/endpoint` dentro del campo Entonces
- Numerar los casos funcionales de forma continua en todo el documento
- Registrar en la tabla de reglas TODAS las condiciones encontradas en el código
- Todo el contenido debe usar ortografía española completa: ñ, tildes (á, é, í, ó, ú), diéresis (ü). La restricción de "sin tildes" aplica SOLO a nombres de fichero

## Guardado de estado y compactado

### Tras cada historia/épica aprobada
1. Actualizar `/memories/session/reverse_engineering_state.md` con: historia completada, fichero generado, dudas nuevas, siguiente historia pendiente
2. Si se han completado 3+ historias detalladas desde el último compactado → sugerir `/compact` con el siguiente mensaje:

```
---
**📦 SUGERENCIA DE COMPACTADO**

Se han completado [X] historias desde el último punto de guardado.
- Estado guardado en memoria de sesión: ✅
- Historias completadas: [lista]
- Siguiente historia pendiente: [nombre]

Puedes ejecutar `/compact` para liberar contexto y mantener el rendimiento.
Tras el compactado, recuperaré automáticamente el estado. **No se perderá ninguna información.**
---
```

### Antes de iniciar una épica compleja
- Guardar estado completo en memoria de sesión
- Sugerir `/compact` al usuario con un mensaje claro indicando que es seguro y no se pierde información

### Recuperación post-compactado
Si al iniciar este step el contexto parece compactado:
1. Leer `/memories/session/reverse_engineering_state.md`
2. Leer el documento general ya generado para recuperar el mapa de historias
3. Confirmar con el usuario: "He recuperado el estado. La siguiente historia pendiente es [X]. ¿Continuamos?"
