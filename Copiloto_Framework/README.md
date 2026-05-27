# Demo_Framework - Copiloto de Creacion de Framework de Automatizacion

## Objetivo General

Este copiloto permite generar de forma automatizada un **framework completo de pruebas end-to-end** basado en **Playwright + Cucumber (BDD)** siguiendo el patron **Page Object Model (POM)**. Opera en dos fases secuenciales: primero crea la estructura base del proyecto (carpetas, configuraciones, dependencias) y despues genera las pruebas automatizadas a partir de escenarios Gherkin (.feature).

El framework resultante utiliza **Cucumber como unico ejecutor de pruebas** (nunca Playwright directamente), implementa el **patron Browser Factory obligatorio** para la gestion centralizada del navegador y soporta ejecucion **multi-navegador** (Chromium, Firefox, WebKit).

---

## Estructura del Copiloto

```
Demo_Framework/
├── .github/
│   ├── agents/
│   │   ├── framework_setup.agent.md
│   │   └── framework_test_generation.agent.md
│   ├── instructions/
│   │   ├── framework_playwright_structure.instructions.md
│   │   └── framework_playwright_tests.instructions.md
│   └── prompts/
│       ├── framework_step1_playwright_structure.prompt.md
│       └── framework_step2_playwright_tests.prompt.md
├── features/
│   ├── Login.feature
│   ├── LoginCaptcha.feature
│   └── LoginDemo.feature
├── html/
│   ├── DigitalDesktop.html
│   ├── DigitalDesktop_files/
│   ├── login.html
│   ├── login_files/
│   ├── menu.html
│   └── README.md
├── playwright-demo/
├── Demo_Framework.code-workspace
├── lanza_structure.txt
└── README.md
```

---

## Descripcion de Cada Fichero

### Agentes (.github/agents/)

| Fichero | Descripcion |
|---------|-------------|
| `framework_setup.agent.md` | **Automation Architect** (Claude Sonnet 4). Crea la estructura base del proyecto de automatizacion: carpetas, ficheros de configuracion, dependencias npm, Browser Factory, environment loader y archivos de ejemplo. No genera pruebas reales. |
| `framework_test_generation.agent.md` | **QA Automation Engineer** (Claude Sonnet 4.5). Genera pruebas automatizadas a partir de escenarios BDD existentes y el framework ya creado. Utiliza herramientas MCP de Playwright para interactuar con la aplicacion bajo prueba. |

### Instrucciones (.github/instructions/)

| Fichero | Descripcion |
|---------|-------------|
| `framework_playwright_structure.instructions.md` | Fuente tecnica de verdad para la fase de estructura. Define la arquitectura completa del framework: arbol de carpetas (`src/pages`, `src/steps`, `src/support`, `src/features`, `src/utils`), configuracion de Cucumber con reportes basados en timestamp, patron Browser Factory obligatorio, environment loader, soporte multi-navegador, requisitos de seguridad (sin secretos en codigo) y plantillas de codigo. |
| `framework_playwright_tests.instructions.md` | Fuente tecnica de verdad para la fase de generacion de pruebas. Define las reglas de implementacion: Cucumber como unico test runner, patron POM sin herencia, uso obligatorio del Browser Factory, analisis de ficheros .feature y paginas JSP/HTML para localizadores, etiqueta `@pendiente` para escenarios sin implementar, scripts npm multi-navegador, modo HEADLESS desactivado por defecto, reportes JSON+HTML y documentacion en espanol. |

### Prompts (.github/prompts/)

| Fichero | Descripcion |
|---------|-------------|
| `framework_step1_playwright_structure.prompt.md` | **Fase 1 - Generacion de estructura**. Prompt asociado al agente `framework_setup`. Recibe como variables de entrada: nombre de carpeta del proyecto, carpeta con ficheros .feature, URL base del entorno, credenciales y roles. Genera exclusivamente la estructura base del framework sin implementaciones reales. Exige licencia GPLv3 y author "Knowmadmood" en package.json. |
| `framework_step2_playwright_tests.prompt.md` | **Fase 2 - Generacion de pruebas**. Prompt asociado al agente `framework_test_generation`. Recibe como variables: nombre del fichero .feature a implementar, carpeta BDD, carpeta del framework y carpeta con paginas JSP/HTML de referencia. Implementa escenario por escenario de forma incremental, validando cada uno antes de avanzar al siguiente. |

### Recursos del Proyecto

| Fichero / Carpeta | Descripcion |
|--------------------|-------------|
| `features/` | Carpeta con los escenarios BDD de entrada en formato Gherkin (.feature): `Login.feature`, `LoginCaptcha.feature` y `LoginDemo.feature`. Sirven como especificacion funcional para la generacion de pruebas. |
| `html/` | Paginas HTML estaticas de la aplicacion bajo prueba (pantallas de login, escritorio digital y menu). Se utilizan como referencia para identificar localizadores de elementos y comprender la estructura de la interfaz. Incluye un README con detalles de navegacion. |
| `playwright-demo/` | Carpeta destino donde el copiloto genera el framework completo de Playwright. Inicialmente vacia; se puebla tras ejecutar la Fase 1. |
| `lanza_structure.txt` | Fichero de referencia rapida con los comandos de ejecucion de ambos prompts y sus parametros de entrada. |
| `Demo_Framework.code-workspace` | Configuracion de workspace de VS Code para el proyecto. |

---

## Caracteristicas Principales

| Caracteristica | Detalle |
|----------------|---------|
| Flujo de trabajo | Dos fases secuenciales: estructura del framework (Fase 1) y generacion de pruebas (Fase 2) |
| Test runner | Cucumber.js como unico ejecutor de pruebas; Playwright se utiliza internamente por los Page Objects |
| Patron arquitectonico | Page Object Model (POM) sin herencia, con contexto compartido `this.page` |
| Gestion de navegador | Patron Browser Factory obligatorio con instancia unica centralizada en `browserFactory.js` |
| Multi-navegador | Soporte para Chromium, Firefox y WebKit mediante variables de entorno |
| Configuracion de entorno | Variables de entorno obligatorias; prohibicion de credenciales en codigo fuente |
| Reportes | JSON + HTML con nomenclatura basada en timestamp para evitar sobreescrituras |
| Carga de pasos | Patron escalable `src/steps/**/*.js` con descubrimiento automatico |
| Escenarios pendientes | Etiqueta `@pendiente` a nivel de escenario individual para funcionalidad no implementada |
| Idioma | Documentacion, comentarios y logs en espanol; nombres de ficheros y variables en ingles |
| Licencia | GPLv3 con author "Knowmadmood" |

---

## Roles y Publico Objetivo

| Rol | Uso esperado |
|-----|-------------|
| Automation Architect | Generar la estructura base del framework de pruebas mediante la Fase 1, definiendo la arquitectura, patrones y configuraciones del proyecto |
| QA Automation Engineer | Implementar pruebas automatizadas a partir de escenarios BDD mediante la Fase 2, creando Page Objects y definiciones de pasos |
| Technical Lead | Supervisar la arquitectura del framework generado y validar el cumplimiento de patrones (Browser Factory, POM, seguridad) |
| Equipo DevOps | Integrar los scripts npm generados en pipelines de CI/CD aprovechando el soporte multi-navegador y multi-entorno |

---

## Modo de Uso

### Fase 1 - Generar Estructura del Framework

1. Abrir el workspace `Demo_Framework.code-workspace` en VS Code.
2. Invocar el prompt `framework_step1_playwright_structure` proporcionando las variables requeridas:
   - `playwright_folder`: nombre de la carpeta destino (ej. `playwright-demo/`).
   - `project_bdd`: carpeta con los ficheros .feature (ej. `features/`).
   - `environment_url`: URL base del entorno de pruebas.
   - `username`, `password`, `role`: credenciales y roles para la configuracion de ejemplo.
3. El agente `framework_setup` genera la estructura completa: carpetas, configuracion de Cucumber, Browser Factory, environment loader, scripts npm y ficheros de ejemplo.

### Fase 2 - Generar Pruebas Automatizadas

1. Una vez completada la Fase 1, invocar el prompt `framework_step2_playwright_tests` proporcionando:
   - `feature_name`: nombre del fichero .feature a implementar (ej. `Login.feature`).
   - `project_bdd`: carpeta con los .feature dentro del framework (ej. `playwright-demo/src/features`).
   - `playwright_folder`: carpeta del framework generado (ej. `playwright-demo/`).
   - `JSP_folder`: carpeta con paginas HTML/JSP de referencia (ej. `html/`).
2. El agente `framework_test_generation` implementa los escenarios del .feature indicado uno por uno, validando cada escenario antes de pasar al siguiente.
3. Repetir la Fase 2 para cada fichero .feature adicional que se desee automatizar.

---

## Requisitos

- Visual Studio Code con GitHub Copilot habilitado y soporte para agentes personalizados.
- Node.js instalado en el entorno local para la ejecucion de scripts npm y Cucumber.
- Acceso a la URL del entorno de pruebas configurada como variable de entorno.
- Ficheros .feature con los escenarios BDD definidos previamente en la carpeta `features/`.
- Paginas HTML/JSP de referencia de la aplicacion bajo prueba en la carpeta `html/` (opcional pero recomendado para localizadores).

---

## Nota

Este copiloto esta disenado para generar frameworks de pruebas completos y funcionales de forma reproducible. La separacion en dos fases permite reutilizar la estructura base con distintos conjuntos de escenarios BDD. El patron Browser Factory garantiza una unica instancia de navegador durante la ejecucion, evitando problemas de recursos y asegurando compatibilidad multi-navegador. Toda la configuracion sensible se gestiona mediante variables de entorno, cumpliendo con los requisitos de seguridad establecidos.
