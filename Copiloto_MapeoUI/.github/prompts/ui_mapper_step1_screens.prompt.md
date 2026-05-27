---
agent: "ui_mapper"
tools: ["search", "read/readFile"]
description: "Step 1: Construccion del arbol completo de pantallas, extraccion de rutas desde sistema de navegacion (React Router/Angular Router/Vue Router/GoRouter), jerarquia de navegacion y clasificacion inicial de pantallas por complejidad"
model: "Claude Sonnet 4.6"
---

# Step 1: Deteccion de Pantallas y Arbol de Navegacion

## 0. ARQUITECTURA COGNITIVA INTERNA

### ROL A: Cartografo de Rutas
**Objetivo:** Extraer el mapa completo de rutas de la aplicacion.
- Leer ficheros de rutas del proyecto | Construir arbol con rutas padre/hijo | Identificar parametros dinamicos, rutas protegidas y lazy loading

### ROL B: Identificador de Vistas
**Objetivo:** Asociar cada ruta con su componente de vista principal.
- Por cada ruta, encontrar el componente asignado | Verificar que existe | Determinar tipo de vista: pantalla, modal, tab, drawer

### ROL C: Clasificador de Complejidad
**Objetivo:** Estimar la complejidad de cada pantalla antes del analisis detallado.
- Contar elementos interactivos en template | Detectar sub-vistas | Clasificar segun criterios de `ui_mapper_reference_tables.instructions.md` seccion 6

### ROL D: Validador de Alcance
**Objetivo:** Confirmar con el usuario el subconjunto de pantallas a procesar.
- Presentar arbol completo con clasificaciones | Identificar pantallas en alcance definido Step 0 | Detectar duplicados | Proponer orden logico

---

## 1. PREREQUISITOS

El Step 0 debe estar completado con:
- `<PROJECT_ROOT>` o `<APP_URL>` confirmado
- Framework del proyecto identificado
- Modo de operacion definido (estatico o dinamico)
- Alcance del analisis definido

---

## 2. INSTRUCCIONES DEL STEP

### Fase 1 - Lectura del sistema de rutas

**Si es modo Estatico (React / Next.js)**:
- Buscar ficheros con patrones: `<Route path=`, `createBrowserRouter`, `<Routes>`, `/pages/` (Next.js)
- Para Next.js: el sistema de ficheros en `/pages/` o `/app/` ya define las rutas directamente
- Construir el arbol de rutas con el path completo

**Si es modo Estatico (Angular)**:
- Buscar `app-routing.module.ts` y todos los ficheros `*-routing.module.ts`
- Leer el array `Routes[]` de cada fichero
- Construir el arbol de rutas con lazy loading resuelto

**Si es modo Estatico (Vue / Nuxt)**:
- Buscar `router/index.js` o `router/index.ts`
- Para Nuxt: analizar el directorio `/pages/`
- Extraer el array de rutas con sus componentes asignados

**Si es modo Estatico (React Native)**:
- Buscar los ficheros de navegacion en `/navigation/` o `/screens/`
- Identificar los Stack, Tab y Drawer navigators
- Cada Screen dentro de los navigators es una pantalla

**Si es modo Estatico (Flutter)**:
- Buscar la configuracion de `GoRouter`, `MaterialApp routes` o el `Navigator`
- Extraer la lista de rutas y sus widgets asociados

**Si es modo Dinamico**:
- Analizar el DOM de la pagina actual para identificar enlaces de navegacion internos
- Registrar las rutas accesibles desde la pagina actual
- Documentar que el arbol solo incluye las rutas descubiertas

**Si es modo Dinamico Movil (Appium / Android / iOS - Jetpack Compose, React Native, Flutter):**
- Las pantallas no tienen rutas URL; se identifican por el estado de navegacion del framework
- Para cada pantalla accesible, capturar el UI tree (XML/JSON) y extraer los `resource-id` unicos
- Construir la **tabla de landmarks de deteccion de pantalla activa** (referencia: `ui_mapper_reference_tables.instructions.md` seccion 9):
  - Por cada pantalla: identificar 1-2 resource-ids que la identifiquen univocamente
  - Identificar resource-ids que DEBEN estar ausentes para distinguirla de pantallas similares
  - Registrar la tabla en el contexto de sesion para uso en Steps 2 y 3
- Documentar si la app usa navegacion basada en Compose NavHost, Stack Navigator u otro mecanismo (afecta a como navegar entre pantallas en el script de captura)

### Fase 2 - Construccion del arbol de pantallas

Para cada ruta identificada:
1. Registrar el path completo (ej: `/usuarios/:id/editar`)
2. Identificar el componente principal asignado
3. Detectar el tipo de pantalla:
   - **Pagina completa**: ocupa toda la pantalla, tiene ruta propia
   - **Modal**: se superpone a otra pantalla, puede o no tener ruta propia
   - **Tab**: contenido dentro de un tab bar o tabs
   - **Step de wizard**: paso dentro de un formulario multi-paso
4. Determinar la pantalla padre (si aplica)
5. Estimar la complejidad (Simple/Compleja/Modulo)

### Fase 3 - Deteccion de sub-pantallas en modulos complejos

Para pantallas clasificadas como Modulo:
- Leer el template del componente principal
- Identificar sub-pantallas segun condiciones automaticas de subdivision (**`ui_mapper_reference_tables.instructions.md` seccion 6**)
- Proponer la subdivision al usuario y esperar aprobacion

### Fase 4 - Confirmacion del alcance final

Presentar al usuario el arbol completo y solicitar:
1. Confirmacion de que el arbol es correcto
2. Marcado de cuales pantallas estan dentro del alcance de este analisis
3. Orden de procesamiento preferido

---

## 3. SALIDA ESPERADA

```
## Arbol de Pantallas - Step 1 Completado

### Pantallas identificadas

| # | ID Pantalla | Nombre | Ruta | Tipo | Complejidad | Padre | En alcance |
|---|-------------|--------|------|------|-------------|-------|-----------|
| 1 | login | Login | /login | Pagina | Simple | - | Si |
| 2 | home | Home | /home | Pagina | Compleja | - | Si |
| 3 | home-tab-tasks | Home - Tab Tareas | /home (tab 1) | Tab | Simple | home | Si |
| 4 | home-tab-calendar | Home - Tab Calendario | /home (tab 2) | Tab | Simple | home | Si |
| 5 | users-list | Listado de Usuarios | /usuarios | Pagina | Simple | - | Si |
| 6 | users-detail | Detalle de Usuario | /usuarios/:id | Pagina | Compleja | users-list | Si |
| 7 | users-edit | Edicion de Usuario | /usuarios/:id/editar | Pagina | Compleja | users-detail | Si |
| 8 | settings | Configuracion | /ajustes | Pagina | Simple | - | No (fuera de alcance) |

### Resumen

**Total de pantallas identificadas**: 8
**Pantallas en alcance**: 7
**Pantallas fuera de alcance**: 1
**Procesamiento estimado**: 7 ciclos Steps 2-3-4

### Orden de procesamiento propuesto

1. login (autenticacion - prerequisito para las demas pantallas)
2. home / home-tab-tasks / home-tab-calendar
3. users-list
4. users-detail
5. users-edit

---

Confirma si este arbol y el orden de procesamiento son correctos para avanzar al ciclo Step 2-3-4.
```

---

## 4. PREREQUISITOS PARA AVANZAR AL STEP 2

- El arbol de pantallas esta aprobado por el usuario
- Las pantallas en alcance estan claramente identificadas
- El orden de procesamiento esta confirmado
- La primera pantalla a procesar ha sido seleccionada

