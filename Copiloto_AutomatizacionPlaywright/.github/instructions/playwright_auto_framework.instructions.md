---
description: Instrucciones de estructura del framework Playwright existente
applyTo: "**/*.js,**/package.json,**/*.feature,**/cucumber.config.js"
---

# Instrucciones de Estructura del Framework Playwright

## 0. Caracteristicas Clave del Framework Playwright Existente

- Playwright para automatización funcional e2e multi-navegador (chromium, firefox, webkit)
- Cucumber JS como ejecutor principal de pruebas con archivos .feature
- JavaScript / Node.js como lenguaje de programación
- Patron de diseño Page Object Model (POM) para mantenibilidad y reutilización
- Browser Factory Pattern para gestión centralizada del navegador
- Gestión de datasets SQL para datos de prueba mediante `AtDBConnector.js` y `QueryDeposit.js`
- Integración con herramientas de CI/CD para ejecución automatizada
- Soporte multi-entorno mediante archivos `env.local.js` y `env.test.js`

**IMPORTANTE** Si el framework Playwright del area de trabajo difiere en algo de lo que se describe en estas instrucciones, se debe parar el flujo y revisar con el ingeniero de software para validar si se debe adaptar el framework existente o si se debe seguir la estructura descrita en estas instrucciones.

## 1. ARQUITECTURA Y ESTRUCTURA DEL FRAMEWORK

### 1.1 Estructura del Proyecto Playwright

```
framework-playwright/
│
├── cucumber.config.js               # Configuración principal de Cucumber
├── playwright.config.js             # Configuración mínima de Playwright (NO se ejecuta)
├── package.json                     # Dependencias y scripts npm
├── env.local.js                     # Configuración de entorno local
├── env.test.js                      # Configuración de entorno de pruebas
├── clean.js                         # Script de limpieza de reportes
│
├── /src/
│   ├── /features/                   # Archivos BDD Cucumber/Gherkin
│   │   ├── Login.feature            # Escenarios de autenticacion
│   │   ├── authentication.feature   # Escenarios de autenticacion extendidos
│   │   └── [features por modulo...] # Features por cada modulo funcional
│   │
│   ├── /pages/                      # Page Object Model classes
│   │   ├── LoginPage.js             # POM para funcionalidad de login
│   │   ├── MenuPage.js              # POM para navegacion del menu principal
│   │   └── /pagesLocators/          # Localizadores de elementos separados
│   │       ├── LoginPageLocators.js # Localizadores de la pagina de login
│   │       └── MenuPageLocators.js  # Localizadores del menu principal
│   │
│   ├── /steps/                      # Definiciones de pasos Cucumber
│   │   ├── common.steps.js          # Pasos comunes y gestión del ciclo de vida del navegador
│   │   ├── login.steps.js           # Pasos para autenticacion
│   │   └── [funcionalidad].steps.js # Pasos especificos por funcionalidad
│   │
│   ├── /support/                    # Archivos de soporte del framework
│   │   ├── browserFactory.js        # Patron Browser Factory (OBLIGATORIO)
│   │   ├── environmentLoader.js     # Cargador de configuracion de entorno
│   │   ├── commands.js              # Comandos personalizados reutilizables
│   │   └── reportGenerator.js       # Generador de reportes HTML
│   │
│   ├── /utils/                      # Funciones de utilidad
│   │   ├── AtDBConnector.js         # Conector MySQL para pruebas
│   │   ├── CommonUtilities.js       # Utilidades comunes reutilizables
│   │   └── QueryDeposit.js          # Repositorio de queries SQL
│   │
│   ├── /datas/                      # Clases de datos para compartir contexto
│   │   ├── LoginData.js             # Datos de autenticacion
│   │   └── UsuarioData.js           # Datos del usuario
│   │
│   ├── /models/                     # Modelos de datos
│   │   └── Usuario.js               # Modelo de usuario del sistema
│   │
│   └── /constantes/                 # Constantes del framework
│       └── RolesConstantes.js       # Constantes de roles de usuario
│
└── /reports/                        # Reportes generados automaticamente
    ├── /json/                       # Reportes JSON de Cucumber
    ├── /html/                       # Reportes HTML navegables
    ├── /screenshots/                # Capturas de pantalla en fallos
    └── /videos/                     # Videos de ejecucion
```

### 1.2 Scripts de Inspección Temporal (Opcional)

Para aplicaciones sin acceso al código fuente o con arquitecturas complejas (framesets, SPA dinámicas), se pueden crear scripts temporales de inspección en la raíz del proyecto. Estos scripts utilizan Playwright para lanzar el navegador, analizar el DOM renderizado y detectar frames, elementos dinámicos y generar selectores precisos.

**Cuándo usar scripts de inspección:**
- Aplicaciones legacy con framesets o iframes
- Arquitecturas JSP/Servlets con renderizado servidor
- Elementos generados dinámicamente por JavaScript/AJAX
- Sin acceso al código fuente HTML/JSX de la aplicación
- Necesidad de verificar selectores del DOM final

Ver snippet: `[snippet:inspeccion-dinamica]` para el patrón completo.

### 1.3 Dependencias y Tecnologias del Framework Playwright

**Dependencias principales (package.json):**

- **Playwright 1.41.2**: Motor de automatizacion web multi-navegador
- **@cucumber/cucumber 10.3.1**: Framework BDD para JavaScript
- **mysql2 3.20.0**: Conectividad con base de datos MySQL
- **dotenv 16.0.0**: Carga de variables de entorno
- **cross-env 7.0.3**: Variables de entorno cross-platform
- **cucumber-html-reporter 7.1.1**: Generación de reportes HTML
- **http-server 14.1.1**: Servidor para visualizar reportes

### 1.4 Configuracion Multi-entorno

**Archivos de configuración:**

- **`env.local.js`**: Entorno de desarrollo local
- **`env.test.js`**: Entorno de testing

**Configuración por entorno incluye:**

- `baseUrl`: URL base de la aplicacion
- `username` / `password`: Credenciales de prueba (desde `process.env`)
- `browser`: Tipo de navegador (chromium, firefox, webkit)
- `headless`: Modo sin interfaz gráfica
- `timeout` / `slowMo`: Tiempos de espera
- `screenshotOnFailure` / `videoOnFailure`: Captura de evidencias
- `workers` / `retries`: Paralelismo y reintentos

### 1.5 Patron de Arquitectura

**Browser Factory como gestor central:**

- `browserFactory.js` gestiona la creación y cierre de instancias de navegador
- Metodos: `createBrowser(browserType, options)` y `closeBrowser(browser, context)`
- Retorna `{ browser, context, page }` para uso en `common.steps.js`
- Soporte multi-navegador: chromium, firefox, webkit

**Page Objects:**

- Reciben `this.page` del contexto compartido por constructor
- Definen localizadores en archivos `*PageLocators.js` separados
- Inicializan localizadores en el método `initializeLocators()`
- Metodos especificos por funcionalidad en cada Page Object
- Los screenshots de fallo se capturan directamente desde el Page Object mediante `this.page.screenshot()`

**Contexto compartido (this):**

- `this.page`: Instancia de pagina Playwright compartida entre todos los Steps
- `this.browser`: Instancia del navegador (solo para cierre en After)
- `this.context`: Contexto del navegador (solo para cierre en After)
- `this.baseUrl`: URL base de la aplicacion
- `this.config`: Configuración completa del entorno activo
- `this.scenarioName`: Nombre del escenario en ejecucion

**Clases Data para datos del escenario:**

- Clases JavaScript simples (NO tienen acceso a `this.page`)
- Almacenan datos de dominio generados o usados durante el escenario
- Se instancian en los Steps y se pasan entre métodos cuando necesario
- Ejemplo: `LoginData`, `UsuarioData`

**Queries SQL centralizadas:**

- `src/utils/QueryDeposit.js`: Repositorio de consultas SQL reutilizables
- `src/utils/AtDBConnector.js`: Conector a base de datos MySQL
- NUNCA escribir queries SQL inline en Steps ni Page Objects
