---
agent: "reverse_engineering_analyst"
tools: ["search", "edit/editFiles", "edit/createDirectory"]
description: "Paso 1: Generación del documento general con todas las historias resumidas"
model: "Claude Sonnet 4.6"
---

# Prompt Step 1: Generación del Documento General

## 0. ARQUITECTURA COGNITIVA INTERNA

Antes de generar el documento general, el agente ejecuta internamente las siguientes fases cognitivas:

### ROL A: Analista de Arquitectura
Objetivo: Comprender la arquitectura global de la aplicación.

- Analizar routing raíz, guards globales, perfiles
- Identificar patrones de navegación (tabs, drawer, etc.)
- Extraer URL base del API y configuraciones globales

### ROL B: Sintetizador Funcional
Objetivo: Resumir cada módulo en una historia de usuario coherente.

Por cada módulo:
- Leer routing → guards → servicios → componentes
- Generar user story (Como/Quiero/Para) verificable en el código
- Documentar casos funcionales mínimos (≥5 por historia)

### ROL C: Inspector de Calidad
Objetivo: Verificar coherencia y completitud del documento.

- ¿Todas las rutas del código están documentadas?
- ¿Todos los endpoints han sido inventariados?
- ¿Los casos funcionales cubren happy path, carga, error y vacío?

### ROL D: Evaluador de Impacto
Objetivo: Clasificar la complejidad de cada historia.

- Número de vistas y modales
- Cantidad de endpoints implicados
- Complejidad de reglas de negocio
- Sistema de clasificación para priorización

## Objetivo

Este prompt genera el documento `Recovered_Backlog_<App>_Overview.md` con la visión completa de la aplicación. Asume que el Step 0 ya se ejecutó y el mapa de módulos fue aprobado.

> `<App>` se extrae del nombre técnico del proyecto identificado en el Step 0 (campo `name` de `package.json` o nombre corto de la aplicación en PascalCase). Ejemplo: `Recovered_Backlog_StarOnline_Overview.md`

## Instrucciones

### Fase 0 — Selección de modo

**ANTES de comenzar el análisis**, preguntar al usuario qué modo de generación desea:

> **¿En qué modo quieres generar el documento?**
> - **Modo Resumen** — Genera el documento general completo de una sola vez, sin paradas intermedias. Cada historia/épica se documenta en su formato estándar resumido. No requiere aprobación por historia. Al finalizar, se guarda el fichero directamente.
> - **Modo Completo** — Genera el documento historia por historia con aprobación interactiva en cada paso. Incluye documentación detallada de todas las vistas, modales, reglas de negocio y casos funcionales exhaustivos. Se espera confirmación del usuario tras cada historia antes de continuar.

---

### Modo Resumen

1. Analizar la arquitectura general (routing raíz, guards globales, perfiles)
2. Analizar todos los módulos funcionales en un único paso de lectura
3. Generar el documento completo de una sola vez con: cabecera, arquitectura, perfiles, todas las historias/épicas resumidas, servicios y endpoints globales, tabla de dudas
4. Guardar el fichero en `<PROJECT_ROOT>/documentacion/Recovered_Backlog_<App>_Overview.md`
5. **ESPERAR APROBACIÓN FINAL** y aplicar correcciones si las hay

---

### Modo Completo

#### Fase 1 — Cabecera y arquitectura

1. Generar la cabecera del documento (nombre, empresa, versión, tecnología, fecha)
2. Documentar la arquitectura de navegación (tabs/menú por perfil)
3. Documentar los guards de seguridad
4. Documentar los perfiles de usuario
5. **ESPERAR APROBACIÓN** de la cabecera

#### Fase 2 — Historias de usuario (resumen)

Para cada módulo funcional (en orden de prioridad):
1. Analizar el módulo siguiendo el orden:
   - Routing → Guards → Enums/Modelos → Servicios → Componentes principales
2. Presentar **únicamente la tabla de casos funcionales** para revisión y aprobación, con este formato:
   ```
   ---
   **VALIDACIÓN REQUERIDA — [Historia XX — Nombre]**

   Casos funcionales identificados:

   | # | Dado | Cuando | Entonces |
   |---|------|--------|----------|
   | 1 | [Contexto del usuario y estado previo] | [Acción concreta del usuario] | [Resultado observable] |
   | 2 | ... | ... | ... |

   Una vez aprobados los casos funcionales, se generará el contenido completo de la historia.
   ¿Apruebas estos casos funcionales? ¿Necesitas añadir, eliminar o corregir alguno?
   ---
   ```
3. **ESPERAR APROBACIÓN** de los casos funcionales
4. Tras la aprobación, generar el resumen completo de la historia con:
   - User story (Como/Quiero/Para)
   - Descripción general
   - Requisitos generales
   - Rutas disponibles (tabla)
   - **Casos funcionales en formato tabla**, posicionados ANTES de los endpoints:
     ```
     | # | Dado | Cuando | Entonces |
     |---|------|--------|----------|
     | 1 | [Contexto del usuario. *Accede a `/ruta`*] | [Acción concreta indicando botón/elemento, vista y funcionalidad] | [Resultado detallado: vista mostrada, elementos de interfaz con propiedades (texto, placeholder, estado), llamadas API, navegación, notas] |
     ```
   - Endpoints de la historia (tabla)

#### Fase 3 — Servicios y endpoints

1. Consolidar TODOS los endpoints descubiertos por dominio
2. Generar tabla resumen: Dominio | GET | POST | PUT | DELETE | Total
3. Generar tablas detalladas por dominio
4. **ESPERAR APROBACIÓN**

#### Fase 4 — Tabla de dudas

1. Consolidar todas las dudas encontradas durante el análisis
2. Presentar la tabla con: # | Área | Pregunta

#### Fase 5 — Generar fichero

1. Determinar `<App>` a partir del nombre identificado en el Step 0
2. Crear la carpeta `documentacion/` en la raíz del proyecto analizado si no existe
3. Crear el fichero `Recovered_Backlog_<App>_Overview.md` dentro de esa carpeta
4. Confirmar la creación con la ruta completa y el nombre de fichero exacto utilizado

## Reglas

- **FLUJO DE APROBACIÓN (Modo Completo)**: En la Fase 2 mostrar ÚNICAMENTE la tabla de casos funcionales para cada historia. Solo tras la aprobación se genera el contenido completo de la historia. Nunca mostrar el resumen completo antes de la aprobación.
- **FORMATO TABLA en todos los contextos**: Los casos funcionales usan SIEMPRE tabla `| # | Dado | Cuando | Entonces |`, tanto en la propuesta de aprobación como en el documento final.
- La diferencia entre ambos contextos es el nivel de detalle del campo "Entonces":
  - **En la propuesta de aprobación**: "Entonces" es un resumen conciso (una frase) del resultado observable
  - **En el documento generado**: "Entonces" es exhaustivo: vista, elementos de interfaz con propiedades exactas, estados (CARGANDO/SIN DATOS/CON DATOS), llamadas API, navegación y notas
- Los casos funcionales en formato tabla aparecen ANTES de los endpoints en el documento final
- El campo "Entonces" en el documento debe incluir todos los elementos de interfaz con sus propiedades (texto, placeholder, valor por defecto, estado, estilo)
- Cada historia debe tener mínimo 5 casos funcionales
- Las rutas deben ser COMPLETAS (con todos los segmentos)
- Los endpoints deben especificar método HTTP y ruta completa
- Todo el contenido debe usar ortografía española completa: ñ, tildes (á, é, í, ó, ú), diéresis (ü). La restricción de "sin tildes" aplica SOLO a nombres de fichero

## Guardado de estado y compactado

### Durante la generación (Modo Completo)
- Actualizar `/memories/session/reverse_engineering_state.md` tras cada historia aprobada
- **Cada 3-4 historias aprobadas**: sugerir al usuario ejecutar `/compact` para liberar contexto
- Antes de sugerir `/compact`: verificar que el estado en memoria de sesión está actualizado

### Al completar el documento general
1. Guardar estado final en memoria de sesión: fichero generado, todas las historias documentadas, dudas acumuladas
2. **Sugerir `/compact`** antes de pasar al Step 2 (historias detalladas) con el siguiente mensaje:

```
---
**📦 SUGERENCIA DE COMPACTADO**

El documento general ha sido completado y guardado.
- Estado guardado en memoria de sesión: ✅
- Fichero generado: [nombre del fichero]
- Historias documentadas: [X]
- Siguiente paso: Step 2 — Historias detalladas

Puedes ejecutar `/compact` para liberar contexto antes de continuar con las historias detalladas.
Tras el compactado, recuperaré automáticamente el estado. **No se perderá ninguna información.**
---
```

### Recuperación post-compactado
Si al iniciar este step el contexto parece compactado, leer `/memories/session/reverse_engineering_state.md` y confirmar con el usuario antes de continuar
