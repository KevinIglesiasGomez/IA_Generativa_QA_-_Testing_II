# Instrucciones de Generación de Documentos para el Agente: Reverse Engineering Functional Analyst

## Objetivo

Estas instrucciones definen las reglas de formato, estructura y calidad que deben cumplir los documentos generados por el agente, tanto el documento general como los documentos detallados por historia.

---

## 1. DOCUMENTO GENERAL — ESTRUCTURA OBLIGATORIA

### 1.1 Cabecera

```markdown
# Casos Funcionales — [Nombre de la Aplicación]

**Aplicación**: [Nombre legible] (`nombre-técnico-del-proyecto`)
**Empresa**: [Nombre de la empresa]
**Versión**: [Versión identificada en package.json o equivalente]
**Tecnología**: [Framework principal + versión] (ej: Angular 18.2.14 + Ionic)
**Fecha de análisis**: [Fecha actual]

---
```

### 1.2 Índice

Índice generado con enlaces Markdown a cada sección:
```markdown
## Índice

- [Diseños y Arquitectura](#diseños-y-arquitectura)
- [Perfiles de Usuario](#perfiles-de-usuario)
- [Historia 01 — Nombre](#historia-01--nombre)
- ...
- [Servicios y Endpoints](#servicios-y-endpoints)
- [Tabla de Dudas](#tabla-de-dudas)
```

### 1.3 Diseños y Arquitectura

- URL Base del API (extraída de los servicios/configuración)
- Arquitectura de navegación (tabs, drawer, etc.)
- Tabla de tabs/funcionalidades por perfil
- Lista de guards de seguridad con descripción breve

### 1.4 Perfiles de Usuario

```markdown
| Perfil | Descripción | Permisos principales |
|--------|-------------|----------------------|
| **Nombre** | Descripción | Lista de permisos |
```

### 1.5 Historias de Usuario (resumen)

Para cada historia:
```markdown
## Historia XX — Nombre Descriptivo

Como [perfil]
Quiero [acción]
Para [beneficio]

**Descripción general**: [Párrafo descriptivo]

### Requisitos generales
- [Requisito 1]
- [Requisito 2]

### Rutas disponibles
| Pantalla | Ruta |
|----------|------|
| Nombre | `/ruta/{param}` |

### Casos funcionales

| # | Dado | Cuando | Entonces |
|---|------|--------|----------|
| 1 | [Contexto del usuario y estado previo] | [Acción concreta que realiza el usuario, indicando botón/elemento, vista y funcionalidad] | [Descripción del resultado observable con los elementos de interfaz principales, estados y llamadas API] |
| 2 | ... | ... | ... |
```

> **IMPORTANTE**: Los casos funcionales se posicionan ANTES de la sección de Servicios y Endpoints.

### 1.6 Servicios y Endpoints

```markdown
## Servicios y Endpoints

**URL Base**: `https://...`

### Resumen global de endpoints identificados
| Dominio | GET | POST | PUT | DELETE | Total |
|---------|-----|------|-----|--------|-------|

### Endpoints principales — [Dominio]
| Operación | Método | Endpoint |
|-----------|--------|----------|
```

### 1.7 Tabla de Dudas

```markdown
## Tabla de Dudas

| # | Área | Pregunta / Duda |
|---|------|-----------------|
| 1 | ... | ... |
```

---

### 1.8 DOCUMENTO DE ÉPICA — ESTRUCTURA OBLIGATORIA

> Aplicar cuando el módulo ha sido clasificado como ÉPICA según los criterios de la sección 3.3 de las instrucciones principales.

#### 1.8.1 Cabecera

```markdown
# Épica M<numero> — <NombreDescriptivo>

**Aplicación**: [Nombre] (`nombre-técnico`)
**Tipo**: ÉPICA
**Módulo**: `ruta/del/módulo`
**Guards**: `Guard1`, `Guard2`
**Sub-historias**: `M<n>.HU-COD-01 — Nombre`, `M<n>.HU-COD-02 — Nombre`, ...
**Fecha**: [Fecha actual]

---
```

#### 1.8.2 Descripción de la Épica

Párrafo descriptivo del dominio funcional completo que abarca la épica. Debe responder: qué problema resuelve, qué perfiles la usan y qué flujos principales contiene.

#### 1.8.3 Perfiles involucrados

```markdown
| Perfil | Sub-historias que le aplican |
|--------|------------------------------|
| **Nombre** | H<n>.01, H<n>.02 |
```

#### 1.8.4 Mapa de sub-historias

```markdown
| Sub-historia | Nombre descriptivo | Descripción breve | Rutas principales |
|:------------:|--------------------|-------------------|-------------------|
| M<n>.HU-COD-01 | Nombre | Descripción | `/ruta/...` |
| M<n>.HU-COD-02 | Nombre | Descripción | `/ruta/...` |
```

#### 1.8.5 Flujo de navegación entre sub-historias

Descripción textual o tabla de cómo el usuario transita entre sub-historias dentro de la épica (puntos de entrada y salida, rutas compartidas).

#### 1.8.6 Endpoints compartidos entre sub-historias

```markdown
| Operación | Método | Endpoint |
|-----------|--------|----------|
```

#### 1.8.7 Tabla de dudas de la Épica

```markdown
| # | Área | Pregunta / Duda |
|---|------|-----------------|
```

---

## 2. DOCUMENTO POR HISTORIA — ESTRUCTURA OBLIGATORIA

### 2.1 Cabecera

```markdown
# Historia XX — Nombre Descriptivo

**Aplicación**: [Nombre] (`nombre-técnico`)
**Perfil**: [Perfil principal] ([roles])
**Módulo**: `ruta/del/módulo`
**Guards**: `Guard1`, `Guard2`
**Fecha**: [Fecha actual]

---
```

### 2.2 Índice detallado

Incluir TODAS las secciones con anclas:
```markdown
## Índice

- [Descripción general](#descripción-general)
- [Rutas disponibles](#rutas-disponibles)
- [Casos funcionales](#casos-funcionales)
- [Servicios API implicados](#servicios-api-implicados)
- [Estados](#estados)
- [Vista: NOMBRE DE LA VISTA](#vista-nombre)
  - [Modal: NOMBRE DEL MODAL](#modal-nombre)
- ...
- [Tabla de condiciones y reglas de negocio](#tabla-de-condiciones-y-reglas-de-negocio)
```

> **IMPORTANTE**: La sección de Casos funcionales aparece ANTES de Servicios API implicados.

### 2.3 Descripción general

Párrafo que describe el módulo funcional completo. Incluir:
- Qué permite hacer al usuario
- Qué protecciones de seguridad tiene
- Qué flujo general sigue

### 2.4 Rutas disponibles

Tabla COMPLETA con todas las rutas del módulo, incluyendo las de componentes hijos.

### 2.5 Casos funcionales

Los casos funcionales se documentan en formato tabla ANTES de la sección de servicios API:

```markdown
## Casos funcionales

| # | Dado | Cuando | Entonces |
|---|------|--------|----------|
| 1 | [Contexto: quién es el usuario, en qué estado se encuentra, qué ha hecho previamente. Al final, ruta en cursiva: *Accede a `/ruta`*] | [Acción concreta que realiza el usuario, indicando el botón, enlace o elemento, la vista donde se encuentra y la funcionalidad] | [Descripción del resultado observable: vista mostrada, elementos de interfaz principales con texto/placeholder/estado, llamadas API (`MÉTODO /endpoint`), navegación resultante, notas importantes] |
| 2 | ... | ... | ... |
```

### 2.6 Servicios API implicados

Tabla con TODOS los endpoints utilizados en el módulo.

### 2.7 Estados (si aplica)

```markdown
| Estado | Clase CSS | Color visual | Descripción |
|--------|-----------|-------------|-------------|
```

### 2.8 Vistas — Casos funcionales detallados

Para cada vista/componente principal, los casos funcionales siguen el formato tabla:
```markdown
## Vista: NOMBRE — `/ruta/completa`

### Casos funcionales

| # | Dado | Cuando | Entonces |
|---|------|--------|----------|
| N | [Contexto del usuario y pasos previos para llegar a esta pantalla. El primer caso de cada vista describe el camino completo desde el inicio de sesión. *Accede a `/ruta/completa`*] | [Acción concreta o evento en la pantalla, indicando el botón/elemento específico y la vista donde se encuentra] | [Resultado detallado: nombre de la vista mostrada; elementos de interfaz con sus propiedades exactas (texto, placeholder, valor por defecto, estado); estados de la interfaz (CARGANDO / SIN DATOS / CON DATOS); llamadas API (`MÉTODO /ruta/endpoint`); navegación resultante; notas importantes] |
```

#### Reglas de redacción de las columnas Dado / Cuando / Entonces

- **Dado**: Contexto y pasos del usuario para llegar a la pantalla en lenguaje natural. El primer caso de cada vista siempre describe el camino completo desde el inicio de sesión. **Al final**, separado con salto de línea, se añade la ruta técnica en cursiva: `*Accede a \`/ruta\`*`.
- **Cuando**: Describe la acción concreta o el evento. Debe indicar el botón, enlace o elemento específico, la vista donde se encuentra y la funcionalidad. Ejemplo: "Pulse en el botón INICIAR SESIÓN de la vista LANDING SPLASH".
- **Entonces**: Describe el resultado observable con detalle exhaustivo. Debe incluir:
  - Nombre de la vista resultante
  - TODOS los elementos de interfaz visibles con: texto exacto, valor por defecto, placeholder, estado (habilitado/deshabilitado), estilo
  - Secciones de la vista, agrupaciones, espacios
  - Llamadas API identificadas
  - Notas importantes sobre implicaciones funcionales

El campo "Entonces" en los documentos detallados DEBE ser exhaustivo. Incluir:
- Nombre de la vista o sección que se muestra
- Todos los elementos de interfaz con sus propiedades exactas (texto, placeholder, valor por defecto, estado, estilo)
- Estados de la interfaz (CARGANDO / SIN DATOS / CON DATOS) con descripción de cada uno
- Llamadas API identificadas en formato `MÉTODO /ruta/endpoint`
- Navegación resultante
- Notas importantes sobre implicaciones funcionales o técnicas

### 2.9 Modales

Misma estructura que las vistas, pero indicando cómo se abre el modal.

### 2.10 Tabla de condiciones y reglas de negocio

```markdown
## Tabla de condiciones y reglas de negocio

| Regla | Condición | Comportamiento |
|-------|-----------|---------------|
```

---

## 3. REGLAS DE FORMATO

### 3.1 Markdown

- Usar encabezados `##` para secciones principales, `###` para subsecciones
- Usar tablas Markdown para datos tabulares
- Usar listas (`-`) para enumeraciones
- Usar código inline (`` ` ``) para nombres técnicos (rutas, componentes, endpoints)
- Usar bloques de código (`` ``` ``) solo cuando sea estrictamente necesario
- Usar separadores `---` entre secciones principales

### 3.2 Tablas

- Las tablas deben tener cabecera y separador
- Mantener consistencia de columnas entre tablas del mismo tipo
- Las tablas se usan para: rutas, endpoints, estados, reglas de negocio y **la tabla de aprobación de casos funcionales**
- **Los casos funcionales usan SIEMPRE formato tabla** `| # | Dado | Cuando | Entonces |`, tanto en la propuesta de aprobación como en el documento final generado
- La diferencia entre ambos contextos es el nivel de detalle del campo "Entonces":
  - **En la propuesta de aprobación**: "Entonces" es un resumen conciso (una frase) del resultado observable
  - **En el documento generado**: "Entonces" es exhaustivo: vista, todos los elementos de interfaz con propiedades exactas, estados (CARGANDO/SIN DATOS/CON DATOS), llamadas API, navegación y notas

### 3.3 Ortografía española en el contenido

- Todo el contenido de los ficheros .md generados DEBE usar ortografía española completa: ñ, tildes (á, é, í, ó, ú), diéresis (ü) y todos los caracteres propios del español
- Los textos deben llevar acentos correctos: "descripción", "información", "sesión", "contraseña", "búsqueda", etc.
- La restricción de "sin tildes ni caracteres especiales" aplica ÚNICAMENTE a los nombres de fichero (para compatibilidad de sistema de archivos), NUNCA al contenido del documento
- Si el código fuente contiene textos en español sin acentos, el agente debe corregirlos al documentarlos

### 3.4 Nomenclatura de ficheros y directorios

#### Directorio por módulo (OBLIGATORIO)

Antes de generar cualquier fichero de un módulo, el agente DEBE crear el directorio correspondiente dentro de `<PROJECT_ROOT>/documentacion/`:

- Patrón: `M<numero>-epica-<nombre>/`
  - `<numero>` = 2 dígitos con padding (01, 02, 03, ...)
  - `<nombre>` = nombre del módulo en minúsculas con guiones, sin tildes ni caracteres especiales
  - Ejemplo: `M03-epica-tasaciones/`, `M04-epica-inspeccion/`, `M05-epica-talleres/`
- Tanto el fichero de épica como todos sus ficheros de sub-historia se colocan DENTRO de este directorio

#### Nomenclatura de ficheros

- Documento general: `Recovered_Backlog_<App>_Overview.md`
  - `<App>` = nombre técnico de la aplicación en PascalCase o el nombre corto identificado en `package.json`
  - Ejemplo: `Recovered_Backlog_StarOnlineMobile_Overview.md`
- Documento de épica: `Recovered_Backlog_<App>_M<numero>_Epica_<Nombre>.md` (dentro de `M<numero>-epica-<nombre>/`)
  - `<numero>` = 2 dígitos con padding
  - `<Nombre>` = nombre descriptivo en PascalCase, sin tildes ni caracteres especiales
  - Ejemplo: `Recovered_Backlog_StarOnlineMobile_M03_Epica_Tasaciones.md`
- Documentos de sub-historia: `Recovered_Backlog_<App>_M<numero>_HU-<COD>-<NN>_<Nombre>.md` (dentro de `M<numero>-epica-<nombre>/`)
  - `<COD>` = código de 3 letras identificativo del módulo en mayúsculas (ej: TAS, INS, TAL, REP)
  - `<NN>` = número de sub-historia con 2 dígitos con padding (01, 02, ...)
  - `<Nombre>` = nombre descriptivo en PascalCase con guiones bajos, sin tildes
  - Ejemplo: `Recovered_Backlog_StarOnlineMobile_M03_HU-TAS-01_Listado_Tasaciones.md`

### 3.5 Numeración de casos funcionales

- En el documento general: numerar del 1 a N por cada historia (reinicio por historia)
- En el documento detallado: numerar del 1 a N de forma continua en todo el documento
- Los casos funcionales usan formato narrativo (no tabla): `### Caso Funcional [N]` con **Dado**, **Cuando**, **Entonces**

---

## 4. REGLAS DE CALIDAD

### 4.1 Verificaciones antes de entregar un documento

1. Todos los enlaces del índice apuntan a secciones existentes
2. Todas las rutas documentadas existen en el código fuente
3. Todos los endpoints documentados existen en algún servicio
4. Los casos funcionales cubren al menos:
   - Flujo principal (happy path)
   - Estado de carga
   - Estado sin datos
   - Al menos un caso de error o excepción
5. La tabla de reglas de negocio contiene todas las condiciones identificadas en guards y lógica de componentes

### 4.2 Coherencia entre documentos

- Los datos del documento general deben ser consistentes con los documentos detallados
- Si se actualiza un documento detallado, verificar si el general necesita actualización
- Las rutas y endpoints deben coincidir entre el general y los detallados

### 4.3 Métricas de completitud sugeridas

| Métrica | Umbral mínimo |
|---------|--------------|
| Rutas documentadas vs rutas en código | 100% |
| Endpoints documentados vs endpoints en servicios | 100% |
| Vistas con estados de interfaz | 100% de las vistas principales |
| Historias con tabla de reglas de negocio | 100% |
| Casos funcionales por vista principal | Mínimo 3 (happy path + carga + error/vacío) |
