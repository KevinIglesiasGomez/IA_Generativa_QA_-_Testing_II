# Reverse Engineering Functional Analyst — Agente de GitHub Copilot

> Agente de IA especializado en ingeniería inversa funcional: extrae documentación funcional completa (historias de usuario, casos funcionales, endpoints, reglas de negocio y arquitectura) a partir del código fuente de aplicaciones web y móviles.

---

## 🎯 Objetivo General

Este proyecto contiene un **agente personalizado para GitHub Copilot**, diseñado para actuar como un **analista funcional experto en ingeniería inversa de software**. Se integra directamente en VS Code y proporciona las siguientes capacidades:

### Capacidades Principales

- **Exploración exhaustiva** del código fuente para descubrir toda la funcionalidad implementada
- **Comprensión arquitectónica** del framework utilizado (Angular, React, Vue, Ionic, Next.js, Flutter, etc.)
- **Extracción funcional por capas**: routing, componentes, servicios, modelos, guards, stores
- **Generación de documentación funcional** en formato Markdown, lista para conversión a PDF
- **Propuesta incremental** de historias de usuario con aprobación individual
- **Documentación dual**: documento general (visión completa) + documentos detallados por épica/historia
- **Gestión avanzada de contexto**: persistencia de estado en memoria de sesión y recuperación post-compactado
- **Solo casos verificables**: NO documenta comportamientos inferidos, solo lo que está completamente verificable en el código

### Frameworks Soportados

Angular • Angular + Ionic • React • React Native • Vue.js • Next.js • Nuxt • Flutter

---

## 📁 Arquitectura del Proyecto

```
Demo_IngenieriaInversa/
├── .github/                                   Configuración del agente
│   ├── agents/
│   │   └── reverse_engineering_analyst.agent.md              Definición del agente
│   ├── instructions/                          Conjunto de instrucciones modulares
│   │   ├── reverse_engineering_main.instructions.md          Criterios y estándares principales
│   │   ├── reverse_engineering_code_analysis.instructions.md Técnicas de análisis por capas
│   │   ├── reverse_engineering_interactive_flow.instructions.md Protocolo interactivo
│   │   ├── reverse_engineering_document_generation.instructions.md Formato y calidad
│   │   ├── reverse_engineering_context_management.instructions.md Gestión de estado
│   │   └── reverse_engineering_quality_verification.instructions.md Checklist de calidad
│   ├── prompts/                               Prompts del flujo de trabajo
│   │   ├── reverse_engineering_step0_discovery.prompt.md    Descubrimiento del proyecto
│   │   ├── reverse_engineering_step1_general.prompt.md      Documento general (overview)
│   │   └── reverse_engineering_step2_detail.prompt.md       Documento detallado por historia
│   └── README.md                              Esta guía
├── .gitignore                                 Control de versiones
└── Demo_IngenieriaInversa.code-workspace      Configuración del workspace VS Code
```

### Componentes del Sistema

| Componente | Propósito | Ubicación |
|------------|-----------|-----------|
| **Agente** | Definición del agente con rol, herramientas y modelo | `agents/reverse_engineering_analyst.agent.md` |
| **Instrucciones** | Conjunto modular de criterios y estándares de análisis | `instructions/*.instructions.md` |
| **Prompts** | Flujo de trabajo en 3 pasos (descubrimiento → general → detalle) | `prompts/*.prompt.md` |
| **Workspace** | Configuración de VS Code con agente habilitado | `Demo_IngenieriaInversa.code-workspace` |

---

## 📚 Descripción de Componentes

### 🤖 Agente: `reverse_engineering_analyst.agent.md`

Define la identidad, rol y comportamiento del agente de GitHub Copilot.

#### Configuración

| Parámetro | Valor |
|-----------|-------|
| **Nombre** | Reverse Engineering Functional Analyst |
| **Modelo** | Claude Sonnet 4.6 |
| **Skills** | `/explain`, `/search`, `/review` |
| **Idioma** | Español (ortografía completa) |

#### Herramientas Habilitadas

- `edit/createDirectory` — Crear estructura de carpetas para documentación
- `edit/editFiles` — Generar y modificar documentos Markdown
- `search` — Exploración exhaustiva del código fuente
- `read/readFile` — Lectura de archivos de código
- `vscode/getProjectSetupInfo` — Detección de configuración del proyecto
- `execute/runInTerminal` — Ejecución de comandos cuando sea necesario
- `usages` — Análisis de referencias cruzadas

#### Enfoque Metodológico

Análisis por capas en orden de prioridad:
1. Routing modules → descubrimiento de navegación
2. Guards → control de acceso y perfiles
3. Enums → estados y catálogos
4. Services/Adapters → contratos API
5. Stores → gestión de estado
6. Components → vistas e interacciones
7. Models → estructuras de datos

---

### 📋 Instrucciones

#### `reverse_engineering_main.instructions.md`

**Instrucciones centrales** que definen los criterios y estándares del análisis.

**Contenido:**
- Análisis estructural del proyecto (arquitectura, módulos, routing)
- Extracción funcional por capas (routing → guards → services → components)
- Modelo de Historias de Usuario (formato Dado/Cuando/Entonces)
- Clasificación Épica vs Historia (con umbrales cuantitativos)
- Estrategia de exploración y priorización
- Nomenclatura de ficheros: `Recovered_Backlog_<App>_[Overview|Epic|Story]_...`

#### `reverse_engineering_code_analysis.instructions.md`

**Técnicas de análisis** para extraer información funcional de cada artefacto de código.

**Contenido:**
- Routing modules: rutas, guards, parámetros, lazy loading
- Componentes: estados de interfaz, elementos interactivos, ciclo de vida
- Servicios: endpoints HTTP, payloads, respuestas
- Modelos: campos, tipos, relaciones
- Enumeraciones: estados, códigos, valores
- Guards: condiciones, redirects, efectos secundarios
- Stores: estado, acciones, selectores, efectos
- Patrones por framework: Angular, Ionic, React, Vue

#### `reverse_engineering_interactive_flow.instructions.md`

**Protocolo de interacción** entre el agente y el usuario.

**Contenido:**
- Fases del flujo: Confirmación → Descubrimiento → General → Detalle
- Modos de generación: Resumen (automático) vs Completo (aprobación)
- Protocolo de aprobación individual de historias
- Gestión de ambigüedades con tabla de dudas
- Comandos interactivos: "Siguiente historia", "Detalla esta", "Muestra dudas"
- Gestión de `/compact`: cuándo sugerir, recuperación post-compactado

#### `reverse_engineering_document_generation.instructions.md`

**Reglas de formato** y estructura de los documentos generados.

**Contenido:**
- Estructura del **documento general** (overview): cabecera, índice, arquitectura, perfiles, historias resumidas, endpoints globales, tabla de dudas
- Estructura de **documentos de épica**: cabecera, mapa de sub-historias, flujo de navegación, endpoints compartidos
- Estructura de **documentos por historia**: cabecera, índice detallado, descripción, rutas, casos funcionales, servicios/API, vistas con estados, modales, reglas de negocio
- Formato Markdown: encabezados, tablas, código inline, HTML en celdas
- Ortografía española: completa en contenido, sin tildes en nombres de archivo
- Nomenclatura estandarizada de ficheros

#### `reverse_engineering_context_management.instructions.md`

**Gestión del contexto** y persistencia de estado durante el análisis.

**Contenido:**
- Persistencia en memoria de sesión: momentos obligatorios de guardado
- Formato del fichero de estado con información crítica
- Protocolo de recuperación post-`/compact`: lectura y confirmación
- Puntos críticos donde sugerir compactado (cada 3-4 historias)
- Información a preservar: PROJECT_ROOT, mapa de módulos, fase, progreso

#### `reverse_engineering_quality_verification.instructions.md`

**Checklist de calidad** pre-entrega de documentos.

**Contenido:**
- Verificación estructural: índice, formato Markdown, orden de secciones
- Verificación de contenido: trazabilidad con código, ortografía
- Verificación de completitud: umbrales mínimos de cobertura
- Casos funcionales obligatorios por vista: happy path, carga, error, sin datos
- Coherencia entre documentos: general vs detallados, épica vs sub-historias
- Anti-patrones: casos inferidos, asunciones, código comentado
- Reporte de calidad: formato de resumen con métricas

---

### 🎬 Prompts (Flujo de Trabajo)

El análisis se estructura en **3 pasos secuenciales**:

#### Step 0: `reverse_engineering_step0_discovery.prompt.md`

**Fase de descubrimiento** del proyecto a analizar.

**Acciones:**
1. Solicitar la ruta del directorio raíz del proyecto (`PROJECT_ROOT`)
2. Identificar tecnología y framework (Angular, React, Vue, etc.)
3. Explorar estructura de carpetas y módulos
4. Mapear rutas y guards de seguridad
5. Clasificar módulos en Épicas vs Historias (según umbrales cuantitativos)
6. Presentar mapa del proyecto para confirmación del usuario

#### Step 1: `reverse_engineering_step1_general.prompt.md`

**Generación del documento general** con visión completa de la aplicación.

**Modos de ejecución:**
- **Modo Resumen**: Genera documento completo automáticamente (historias resumidas)
- **Modo Completo**: Propone cada historia individualmente para aprobación

**Artefacto generado:**  
`Recovered_Backlog_<App>_Overview.md`

**Contenido:**
- Cabecera con metadatos del proyecto
- Índice completo de historias/épicas
- Arquitectura de navegación (routing tree)
- Perfiles de usuario y guards
- Historias resumidas con casos funcionales principales
- Inventario global de endpoints por dominio
- Tabla de dudas técnicas

#### Step 2: `reverse_engineering_step2_detail.prompt.md`

**Generación de documentos detallados** por épica o historia individual.

**Artefactos generados:**  
- Épicas: `Recovered_Backlog_<App>_Epic_E<XX>_<Name>.md`
- Historias: `Recovered_Backlog_<App>_Story_H<XX>_<Name>.md`

**Contenido de documento de historia:**
1. Cabecera con metadatos
2. Índice detallado con anclajes
3. Descripción funcional de la historia
4. Rutas asociadas (con parámetros)
5. **Casos funcionales** (Dado/Cuando/Entonces) — posicionados ANTES de servicios
6. Servicios/API consumidos (endpoints completos)
7. Vistas con **3 estados de interfaz**:
   - 🔄 CARGANDO (skeleton/spinner)
   - ⚠️ SIN DATOS (vacío/error)
   - ✅ CON DATOS (datos cargados)
8. Modales (formularios, validaciones, acciones)
9. Reglas de negocio y condiciones

---

## 🚀 Cómo Usar

### Paso 1: Preparar el Workspace

1. Abre VS Code
2. Abre el archivo `Demo_IngenieriaInversa.code-workspace`
3. Asegúrate de tener instalada la extensión **GitHub Copilot** con acceso al modelo Claude Sonnet 4.6

### Paso 2: Configurar el Proyecto a Analizar

El proyecto de ingeniería inversa debe estar disponible en el workspace. Puedes:
- Agregar la carpeta del proyecto al workspace actual
- O tener el código ya abierto en VS Code

### Paso 3: Invocar el Agente

En el chat de GitHub Copilot, escribe:

```
@reverse_engineering_analyst
```

### Paso 4: Iniciar el Descubrimiento

Usa el prompt de la **Fase 0** para iniciar el análisis:

```
Usa el prompt reverse_engineering_step0_discovery para descubrir el proyecto
```

El agente te pedirá:
1. La **ruta raíz** del proyecto a analizar
2. Confirmación del mapa de módulos descubierto

### Paso 5: Generar Documentación

Según tus necesidades, el agente te ofrecerá:

#### Opción A: Documento General Primero

```
Genera el documento general en modo Resumen
```
o
```
Genera el documento general en modo Completo (con aprobación por historia)
```

#### Opción B: Documentos Detallados por Historia

```
Detalla la historia H01: Gestión de Inspecciones
```

### Paso 6: Gestionar el Contexto

Cuando el agente sugiera usar `/compact`, escribe en el chat:

```
/compact
```

Tras el compactado, el agente recuperará automáticamente el estado desde la memoria de sesión.

---

## 📊 Artefactos Generados

### 1. Documento General (Overview)

**Nombre del archivo:**  
`Recovered_Backlog_<NombreApp>_Overview.md`

**Ejemplo:**  
`Recovered_Backlog_SOLHibrida_Overview.md`

**Contenido:**
- **Cabecera**: Nombre de la aplicación, versión, tecnología, fecha de análisis
- **Índice**: Lista completa de épicas e historias
- **Arquitectura**: Árbol de navegación (routing tree)
- **Perfiles y Guards**: Roles de usuario y condiciones de acceso
- **Historias Resumidas**: Tabla con # | Historia | Casos Funcionales (formato Dado/Cuando/Entonces)
- **Endpoints Globales**: Inventario de API por dominio
- **Tabla de Dudas**: Comportamientos no verificables en el código

### 2. Documentos de Épica

**Nombre del archivo:**  
`Recovered_Backlog_<NombreApp>_Epic_E<XX>_<NombreEpica>.md`

**Ejemplo:**  
`Recovered_Backlog_SOLHibrida_Epic_E01_Inspeccion_Tecnica_Talleres.md`

**Contenido:**
- Descripción de la épica
- Mapa de sub-historias contenidas
- Flujo de navegación entre sub-historias
- Endpoints compartidos
- Componentes reutilizables

### 3. Documentos de Historia

**Nombre del archivo:**  
`Recovered_Backlog_<NombreApp>_Story_H<XX>_<NombreHistoria>.md`

**Ejemplo:**  
`Recovered_Backlog_SOLHibrida_Story_H13_Lista_Inspecciones_Pendientes.md`

**Contenido:**
- Análisis exhaustivo de UN módulo funcional
- Todos los endpoints consumidos
- Todas las vistas con sus 3 estados de interfaz
- Casos funcionales detallados (Dado/Cuando/Entonces)
- Modales con formularios y validaciones
- Reglas de negocio aplicadas

---

## ✅ Características Principales

| Característica | Descripción |
|----------------|-------------|
| **Flujo Interactivo** | Propone historias individualmente y espera aprobación antes de continuar |
| **Análisis por Capas** | Routing → Guards → Enums → Services → Stores → Components → Modals |
| **Documentación Dual** | Documento general (overview) + documentos detallados (épica/historia) |
| **Multi-Framework** | Angular, Ionic, React, React Native, Vue, Next.js, Nuxt, Flutter |
| **Trazabilidad** | Referencias a código fuente y tabla de dudas para comportamientos no verificables |
| **Solo Casos Verificables** | NO documenta casos inferidos — solo comportamientos verificables en el código |
| **Formato QA-Ready** | Casos funcionales en formato Dado/Cuando/Entonces, listos para diseño de pruebas |
| **Gestión de Contexto** | Persistencia en memoria de sesión y recuperación post-`/compact` |

---

## 📋 Requisitos

- **Editor**: VS Code (versión reciente)
- **Extensión**: GitHub Copilot activo
- **Modelo**: Claude Sonnet 4.6 configurado
- **Proyecto**: Código fuente de la aplicación a analizar (accesible en el workspace)

---

## 🎯 Público Objetivo

Este agente está diseñado para:

- **QA Engineers** — Comprender aplicaciones sin documentación para diseñar casos de prueba
- **Analistas Funcionales** — Validar o completar documentación existente
- **Equipos de Testing** — Identificar escenarios de prueba desde el código fuente
- **Product Owners** — Obtener visión funcional actualizada de lo implementado
- **Desarrolladores** — Documentar proyectos legacy o sin documentación

---

## 📝 Notas Importantes

### Regla de Oro: Solo Casos Verificables

El agente **NO** documenta:
- Casos inferidos o asumidos
- Comportamientos que no se pueden confirmar en el código
- Estados o transiciones que no están implementados

Si hay ambigüedad, el agente:
- Registra la duda en la **Tabla de Dudas**
- Marca el comportamiento como **PENDIENTE DE VERIFICAR**

### Ortografía Española Completa

- Todo el contenido usa ortografía española: ñ, tildes, diéresis
- Los nombres de archivo NO usan tildes (para compatibilidad de sistemas)

### Formato de Casos Funcionales

Todos los casos funcionales siguen el formato:

```
DADO que [precondición/estado inicial]
CUANDO [acción del usuario]
ENTONCES [resultado esperado]
```

---

## 📚 Referencias

Para más información sobre cada componente, consulta los archivos en:

- **Definición del agente**: [agents/reverse_engineering_analyst.agent.md](agents/reverse_engineering_analyst.agent.md)
- **Instrucciones principales**: [instructions/reverse_engineering_main.instructions.md](instructions/reverse_engineering_main.instructions.md)
- **Análisis de código**: [instructions/reverse_engineering_code_analysis.instructions.md](instructions/reverse_engineering_code_analysis.instructions.md)
- **Flujo interactivo**: [instructions/reverse_engineering_interactive_flow.instructions.md](instructions/reverse_engineering_interactive_flow.instructions.md)
- **Generación de documentos**: [instructions/reverse_engineering_document_generation.instructions.md](instructions/reverse_engineering_document_generation.instructions.md)
- **Gestión de contexto**: [instructions/reverse_engineering_context_management.instructions.md](instructions/reverse_engineering_context_management.instructions.md)
- **Verificación de calidad**: [instructions/reverse_engineering_quality_verification.instructions.md](instructions/reverse_engineering_quality_verification.instructions.md)

---

## 📄 Licencia

Este proyecto es parte de las demostraciones de la **Comunidad QA CE** para ilustrar capacidades de ingeniería inversa con agentes de IA.
