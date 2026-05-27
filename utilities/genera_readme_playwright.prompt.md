---
agent: "agent"
tools:
  ["read/readFile", "edit/editFiles", "search", "execute/runInTerminal", "execute/getTerminalOutput"]
description: "Genera un README.md completo para proyectos de automatización e2e con Playwright (con o sin Cucumber/BDD), cubriendo estructura del proyecto, requisitos previos, instalación, configuración de entornos y ejecución de pruebas."
model: "Claude Sonnet 4.5"
---

# Prompt: Genera README.md para proyecto de automatización Playwright

## 1. CONTEXTO Y PRERREQUISITOS

### 1.1 Rol de la IA
Actúa como un arquitecto QA experto en Playwright. Tu responsabilidad es explorar el proyecto, comprender su arquitectura y generar documentación técnica de calidad que sirva como referencia definitiva para cualquier desarrollador o QA que trabaje con el proyecto.

### 1.2 Criterios de análisis del proyecto
Antes de generar ningún contenido, debes analizar el proyecto real para descubrir su estructura y patrones. No asumas que existe ninguna carpeta, fichero o convención concreta. Durante el análisis, identifica si el proyecto implementa alguno de los siguientes patrones; documenta únicamente los que estén presentes:

- **Patrón Page Object Model (POM)**: detectado si existe una carpeta con clases que encapsulan selectores y acciones sobre páginas o componentes
- **Patrón BDD / Gherkin**: detectado si existen ficheros `.feature` con escenarios escritos en lenguaje natural
- **Definiciones de pasos**: detectado si existen ficheros de steps que mapean los escenarios Gherkin a código ejecutable
- **Browser Factory o gestión centralizada del navegador**: detectado si existe un módulo que centraliza la creación y destrucción de instancias del navegador
- **Generación de datos de prueba**: detectado si existe alguna utilidad que genere datos dinámicos para los escenarios
- **Configuración por ambiente**: detectado si existen ficheros de configuración separados por entorno (`local`, `test`, `staging`, etc.)
- **Sistema de etiquetas/tags**: detectado si los escenarios usan anotaciones (`@smoke`, `@regression`, u otras) para clasificar las pruebas
- **Generación de reportes**: detectado si la configuración produce salidas HTML, JSON u otros formatos de reporte

Usa estos patrones como guía de exploración, no como supuestos. Si un patrón no existe en el proyecto, no lo menciones en el README.

---

## 2. ENTRADAS ESPERADAS

Este prompt acepta los siguientes parámetros configurables. Sustitúyelos antes de ejecutar:

| Parámetro | Descripción | Ejemplo |
|---|---|---|
| `${input:playwright_folder}` | Carpeta base del proyecto Playwright (ruta relativa o absoluta dentro del Área de trabajo) | `taxis-e2e` |
| `${input:project_bdd}` | Directorio que contiene los ficheros BDD (`.feature`). Dejar vacío si el proyecto no usa Cucumber | `src/features` |

**Uso:**
```
playwright_folder: ${input:playwright_folder}
project_bdd: ${input:project_bdd}
```

Si no se proporcionan valores, el prompt preguntará al usuario en el paso obligatorio de la sección 3.

---

## 3. REQUISITOS PREVIOS Y CONTEXTO

### 3.1 Propósito
Este prompt genera un fichero `README.md` profesional y completo para cualquier proyecto de automatización de pruebas E2E basado en Playwright. Es compatible con proyectos que usen Playwright puro, Playwright + Cucumber/BDD u otras combinaciones.

### 3.2 Área de trabajo requerida
Para ejecutar este prompt necesitas tener acceso al proyecto de automatización en el Área de trabajo. El prompt explorará de forma autónoma los siguientes ficheros si existen:

- `package.json` — dependencias, scripts npm y metadatos del proyecto
- `playwright.config.js` / `playwright.config.ts` — configuración base de Playwright
- `cucumber.config.js` / `cucumber.config.ts` — configuración de Cucumber (si aplica)
- `env.*.js` / `.env` / `.env.example` — variables de entorno y configuración por ambiente
- `src/features/` — ficheros `.feature` (escenarios BDD, si aplica)
- `src/steps/` — definiciones de pasos
- `src/pages/` — Page Object Model
- `src/support/` — utilidades, hooks y generadores de reportes
- `src/utils/` — utilidades generales
- `clean.js` / `README.md` existente — contexto adicional

### 3.3 Primer paso obligatorio
Antes de generar el README, debes preguntarme:
1. ¿Cuál es la ruta raíz del proyecto de automatización dentro del Área de trabajo?
2. ¿Hay alguna sección adicional que quieras incluir o alguna que quieras omitir?
3. ¿En qué idioma debe estar escrito el README? (por defecto: español)

No generes ningún fichero hasta tener confirmadas las respuestas anteriores.

---

## 4. FLUJO DE TRABAJO

Ejecuta los siguientes pasos en orden. No avances al siguiente hasta completar el actual.

**Step 1 — Analizar el proyecto**
Explora la estructura real del proyecto y extrae toda la información necesaria para documentarlo.

**Step 2 — Generar el README**
Redacta el fichero `README.md` con las secciones definidas, basándote exclusivamente en lo encontrado en el Step 1.

**Step 3 — Validar criterios de calidad**
Revisa el README generado contra el checklist de la sección 6 antes de guardarlo. Si algún criterio no se cumple, corrígelo antes de finalizar.

---

### 4.1 Detalle del Step 1 — Exploración del proyecto
Una vez confirmada la ruta del proyecto (o los valores de `${input:playwright_folder}` y `${input:project_bdd}`), explora y lee los ficheros indicados en la sección 3.2. Extrae la siguiente información:

- **Nombre y descripción** del proyecto desde `package.json`
- **Tecnologías y versiones** desde `dependencies` y `devDependencies`
- **Scripts disponibles** desde la sección `scripts` de `package.json`
- **Configuración de Playwright**: timeouts, navegadores, viewport, screenshot, video, traza
- **Configuración de Cucumber** (si aplica): paralelismo, reintentos, formatos de reporte
- **Variables de entorno**: lista completa de variables con su descripción y valores por defecto
- **Estructura de carpetas**: árbol de directorios con descripción de cada elemento
- **Features disponibles**: lista de ficheros `.feature` con su propósito

### 4.2 Detalle del Step 2 — Estructura del README a generar
Genera el README con exactamente las siguientes secciones, en este orden:

#### Sección 1 — Título y descripción
- Nombre del proyecto como título principal `# `
- Descripción breve (máximo 3 líneas) obtenida del `package.json`
- Badges de tecnologías principales (Node.js, Playwright, Cucumber si aplica)

#### Sección 2 — Requisitos previos
Lista de software necesario con versiones mínimas recomendadas:
- Node.js (versión según `engines` en `package.json` o recomendación estándar)
- npm / yarn
- Playwright y sus navegadores
- Cualquier otro requisito detectado

#### Sección 3 — Estructura del proyecto
Árbol de directorios con descripción de cada carpeta y fichero relevante. Usa bloques de código con el formato:
```
proyecto-raiz/
├── src/
│   ├── features/     # Escenarios BDD en Gherkin
│   ├── steps/        # Definiciones de pasos
│   ├── pages/        # Page Object Model
│   ├── support/      # Hooks, browser factory, reportes
│   └── utils/        # Utilidades y generadores de datos
├── package.json
└── ...
```
Adapta el árbol a la estructura real encontrada.

#### Sección 4 — Instalación
Pasos numerados y claros:
1. Clonar el repositorio (incluye ejemplo de comando `git clone`)
2. Instalar dependencias con `npm install`
3. Instalar navegadores de Playwright (`npx playwright install`)
4. Configurar variables de entorno (remite a la sección de configuración)

#### Sección 5 — Configuración
Subsecciones:
- **Variables de entorno**: tabla con columnas `Variable | Descripción | Valor por defecto | Obligatoria`; extrae los datos de `env.local.js`, `env.test.js` y `.env.example`
- **Ambientes disponibles**: explica cada fichero `env.*.js` encontrado y cómo activarlo
- **Configuración del navegador**: navegadores soportados, modo headless, viewport

#### Sección 6 — Ejecución de pruebas
Subsecciones con todos los scripts detectados en `package.json`, agrupados por categoría:
- **Ejecución básica** (script `test` principal)
- **Por ambiente** (local, test, staging si existen)
- **Por navegador** (chrome, firefox, webkit si existen)
- **Por etiquetas/tags** (smoke, regression si existen)
- **Modo especial** (headless, dry-run, parallel si existen)
- **Ejecución de features específicas** (si existen scripts para ello)

Para cada script incluye el comando npm y una descripción de qué hace.

#### Sección 7 — Reportes
- Dónde se generan los reportes (carpeta `reports/` o equivalente)
- Formatos disponibles (HTML, JSON, etc.) según la configuración de Cucumber/Playwright
- Cómo abrir el reporte HTML si hay script para ello (`report:open` u equivalente)
- Cómo limpiar los reportes si hay script `clean`

#### Sección 8 — Features disponibles (solo si el proyecto usa Cucumber/BDD)
Tabla con columnas `Fichero | Descripción funcional`. Infiere la descripción funcional del nombre del fichero `.feature` y de su contenido si puedes leerlo.

#### Sección 9 — Convenciones y estructura de código
Breve descripción de los patrones usados:
- Page Object Model (si hay carpeta `pages/`)
- Patrón BDD / Gherkin (si hay carpeta `features/`)
- Generación de datos de prueba (si hay `dataGenerator.js` u equivalente)
- Browser Factory (si existe `browserFactory.js`)

---

## 5. REGLAS Y RESTRICCIONES

### 5.1 Restricciones críticas
- **CRÍTICO: No generes tests reales, casos de prueba ni scripts de instalación ejecutables.** El único artefacto de salida es el fichero `README.md`.
- **CRÍTICO: No crees ficheros adicionales.** Si necesitas mostrar ejemplos de código, inclúyelos como bloques de código dentro del README, nunca como ficheros independientes.
- **CRÍTICO: Toda la documentación, comentarios y texto del README debe estar en español, con lenguaje natural, claro y comprensible para cualquier perfil técnico.**

### 5.2 Reglas de contenido
- Toda la información del README debe estar basada en el código y ficheros reales del proyecto. No inventes ni asumas información que no puedas verificar.
- Si un dato no está disponible en los ficheros (por ejemplo, no hay `.env.example`), indícalo con `_No disponible en el proyecto actual_` en lugar de omitir la sección.
- Usa bloques de código para todos los comandos de terminal.
- No uses emoticonos ni lenguaje informal.
- Las tablas deben estar correctamente formateadas en Markdown.
- El README debe ser comprensible para cualquier desarrollador o QA que no conozca el proyecto.
- Si detectas que el proyecto no usa Cucumber sino Playwright puro, omite las secciones exclusivas de Cucumber (features, tags BDD) y adapta la sección de ejecución a los comandos de Playwright (`npx playwright test`).
- Genera el fichero `README.md` en la raíz del proyecto de automatización, no en un subdirectorio.

---

## 6. CRITERIOS DE CALIDAD Y VERIFICACIÓN FINAL (Step 3 — OBLIGATORIO)

Antes de guardar el fichero `README.md`, verifica cada criterio del siguiente checklist. Todos deben cumplirse:

### 6.1 Estructura y completitud
- [ ] El README cubre todas las secciones aplicables al tipo de proyecto detectado
- [ ] No aparece ninguna sección vacía ni con texto de marcador de posición
- [ ] El árbol de estructura del proyecto refleja la estructura real del directorio, no una estructura supuesta
- [ ] Las secciones exclusivas de Cucumber/BDD solo están presentes si el proyecto realmente usa ese patrón

### 6.2 Exactitud técnica
- [ ] Todos los comandos de la sección de ejecución existen literalmente en la sección `scripts` del `package.json`
- [ ] La tabla de variables de entorno coincide con los valores reales encontrados en los ficheros de configuración del proyecto
- [ ] Las versiones de dependencias mencionadas corresponden a las declaradas en `package.json`
- [ ] Los patrones de arquitectura documentados (POM, BDD, Browser Factory, etc.) han sido verificados en el código fuente

### 6.3 Calidad de la documentación
- [ ] Todo el texto está en español, con lenguaje natural y claro
- [ ] No hay emoticonos, lenguaje informal ni anglicismos innecesarios
- [ ] Los bloques de código tienen el lenguaje especificado (` ```bash `, ` ```js `, etc.)
- [ ] Las tablas Markdown están correctamente formateadas y alineadas
- [ ] El README es comprensible para un desarrollador o QA que no conozca el proyecto

### 6.4 Restricciones cumplidas
- [ ] No se ha creado ningún fichero adicional aparte del `README.md`
- [ ] No se han generado tests, scripts ejecutables ni ficheros de configuración
- [ ] El fichero `README.md` se ha creado en la raíz del proyecto (`${input:playwright_folder}`)

Informa al usuario del resultado final indicando la ruta donde se ha generado el fichero, el número de criterios verificados y cualquier limitación encontrada durante el análisis.
