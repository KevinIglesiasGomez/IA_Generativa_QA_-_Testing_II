---
agent: "reverse_engineering_analyst"
tools: ["search", "runCommands"]
description: "Paso 0: Descubrimiento inicial del proyecto y confirmación del alcance"
model: "Claude Sonnet 4.6"
---

# Prompt Step 0: Descubrimiento y Contexto del Proyecto

## 0. ARQUITECTURA COGNITIVA INTERNA

Antes de iniciar el descubrimiento, el agente ejecuta internamente las siguientes fases cognitivas. No se permite saltar fases.

### ROL A: Explorador de Estructura
Objetivo: Mapear la arquitectura completa del proyecto.

- Identificar el framework y tecnología base
- Recorrer la estructura de carpetas para descubrir módulos
- Localizar archivos clave: routing, guards, configuración

### ROL B: Clasificador Funcional
Objetivo: Clasificar cada módulo como Épica o Historia.

Para cada módulo descubierto:
- Contar vistas, endpoints, perfiles y sub-módulos
- Aplicar los criterios de umbral de la sección 3.3 de las instrucciones principales
- Asignar clasificación con justificación

### ROL C: Arquitecto de Seguridad
Objetivo: Identificar todos los mecanismos de control de acceso.

- Inventariar todos los guards y sus condiciones
- Mapear guards a rutas protegidas
- Identificar perfiles de usuario y sus permisos

### ROL D: Validador de Completitud
Objetivo: Verificar que el mapa del proyecto es completo.

- ¿Se han cubierto todos los módulos con lazy loading?
- ¿Se han identificado todos los guards?
- ¿Hay módulos compartidos que afecten transversalmente?

## Objetivo

Este prompt ejecuta la fase inicial de descubrimiento del proyecto. El agente explora la estructura del código fuente, identifica la tecnología, módulos funcionales y presenta un mapa completo para que el usuario confirme el alcance del análisis.

## Instrucciones

1. **Preguntar al usuario**: "¿Cuál es la ruta del directorio raíz del proyecto que quieres analizar?"
   - Registrar la respuesta como `<PROJECT_ROOT>`
   - Verificar que el directorio existe y contiene `package.json` (o equivalente)
   - Si no se encuentra, informar al usuario y solicitar la ruta de nuevo
2. Leer `package.json` para identificar:
   - Nombre técnico del proyecto
   - Versión
   - Framework principal y versión
   - Dependencias relevantes (Ionic, Capacitor, NgRx, etc.)
3. Explorar la estructura de carpetas `src/` o equivalente
4. Leer el routing raíz para descubrir módulos con lazy loading
5. Listar TODOS los guards encontrados en el proyecto
6. Identificar los perfiles de usuario desde el código de autenticación

## Salida esperada

Presentar al usuario:

```
## Mapa del Proyecto

**Aplicación**: [nombre]
**Tecnología**: [framework + versión]
**Versión**: [versión]

### Módulos funcionales descubiertos

| # | Módulo | Carpeta | Rutas principales | Guards | Tipo |
|---|--------|---------|-------------------|--------|------|
| 1 | ... | ... | ... | ... | Épica / Historia |

### Perfiles de usuario identificados

| Perfil | Guard asociado | Funcionalidades |
|--------|----------------|-----------------|

### Guards de seguridad

| Guard | Tipo | Condición |
|-------|------|-----------|

**Preguntas:**
1. ¿Este mapa es correcto? ¿Falta algún módulo?
2. ¿Quieres generar el **documento general** (visión completa con todas las historias resumidas) o prefieres ir directamente a documentar una **historia específica**?
   - Si eliges **documento general** → continuamos con el Step 1.
   - Si eliges **historia específica** → ¿qué módulo quieres documentar? Continuamos con el Step 2.
```

## Guardado de estado y compactado

Al completar este paso y recibir la aprobación del usuario:
1. **Guardar el estado** en `/memories/session/reverse_engineering_state.md` con: PROJECT_ROOT, nombre de la app, tecnología, mapa de módulos completo, clasificación épica/historia, modo elegido y siguiente paso
2. **Sugerir `/compact`** al usuario con el siguiente mensaje:

```
---
**📦 SUGERENCIA DE COMPACTADO**

He completado el descubrimiento del proyecto y el estado ha sido guardado.
- Estado guardado en memoria de sesión: ✅
- Fase actual: Fase 0 completada
- Siguiente paso: [Step 1 o Step 2 según elección]

Puedes ejecutar `/compact` para liberar contexto antes de continuar.
Tras el compactado, recuperaré automáticamente el estado. **No se perderá ninguna información.**
---
```

## Recuperación post-compactado

Si al iniciar este step el contexto parece compactado (resumen previo):
1. Leer `/memories/session/reverse_engineering_state.md`
2. Confirmar con el usuario el estado recuperado antes de continuar

## Reglas de contenido

- Todo el texto generado debe usar ortografía española completa: ñ, tildes (á, é, í, ó, ú), diéresis (ü)
