# Instrucciones de Estructura del Framework Playwright

## 1. VISIÓN GENERAL Y OBJETIVOS DEL FRAMEWORK

### 1.1 Objetivo Principal
Crear SOLO la estructura base del framework de pruebas automatizadas usando:

- Cucumber como el ejecutor principal de pruebas con archivos .feature plantilla
- Playwright para automatización funcional e2e (usado por las definiciones de pasos de Cucumber)
- JavaScript como lenguaje de programación y usar CommonJS
- Patrón de diseño Page Object Model (POM) para mantenibilidad y reutilización
- Configurar Cucumber para relacionar pasos Gherkin con acciones de Playwright pero no páginas o pasos específicos
- **Toda ejecución de pruebas se realiza a través de comandos de Cucumber, no Playwright directamente**
- No debes generar scripts de instalación. Todo lo requerido debe hacerse usando comandos nativos y debe documentarse en el Readme

**CRÍTICO**: Generar SOLO archivos de ejemplo ÚNICOS. NO crear pruebas reales, escenarios o implementaciones específicas de aplicación basadas en características gherkin.

## 2. RESTRICCIONES CRÍTICAS Y PROHIBICIONES

### 2.1 Restricciones de Archivos y Contenido
- **SOLO archivos de ejemplo únicos**: NO crear pruebas reales, escenarios o implementaciones específicas de aplicación
- **Páginas específicas PROHIBIDAS**: NO crear LoginPage.js, HomePage.js, o cualquier clase de página específica
- **Pasos específicos PROHIBIDOS**: NO crear LoginSteps.js, HomeSteps.js, o archivos de definición de pasos específicos
- **SOLO plantillas genéricas**: Crear UN solo ExamplePage.js y UN solo example.steps.js como plantillas
- **NO análisis de características**: Copiar archivos .feature sin leer, analizar o crear implementaciones basadas en ellos

### 2.2 Restricciones de Seguridad
- **NUNCA codificar información sensible**: URLs, credenciales, datos específicos del entorno en archivos de configuración
- **Variables de entorno OBLIGATORIAS**: Toda configuración sensible debe usar `process.env` con valores predeterminados sensatos
- **Agregar .env a .gitignore**: Prevenir commits accidentales de información sensible

### 2.3 Restricciones de Ejecución
- **Cucumber es el ÚNICO ejecutor de pruebas**: Toda ejecución fluye a través de comandos de Cucumber, NO Playwright directamente
- **Scripts npm con cucumber-js**: NO usar comandos playwright en package.json
- **Patrón Browser Factory OBLIGATORIO**: Gestión centralizada de navegador a través de un solo archivo browserFactory.js, NO múltiples instancias

### 2.4 Restricciones de Implementación
- **NO scripts de instalación**: Todo debe hacerse usando comandos nativos documentados en README
- **Documentación en español OBLIGATORIA**: README, comentarios, texto orientado al usuario
- **Convenciones de nomenclatura**: CamelCase para archivos de páginas y pasos

## 3. ARQUITECTURA Y ESTRUCTURA DEL FRAMEWORK

### 3.1 Estructura del Proyecto
Este proyecto sigue esta estructura:

/project-root
│
├── /src
│ ├── /pages # Page Object Model classes
│ │ └── ExamplePage.js
│ │
│ ├── /steps # Step Definitions for Cucumber
│ │ ├── common.steps.js # Browser lifecycle management (REQUIRED)
│ │ └── example.steps.js
│ │
│ ├── /support # Support files for tests
│ │ ├── commands.js # Custom commands for Playwright
│ │ ├── browserFactory.js # Browser Factory Pattern (REQUIRED)
│ │ ├── environmentLoader.js # Environment configuration loader (REQUIRED)
│ │ └── reportGenerator.js # HTML report generator
│ │  
│ │── /utils # Utility functions
│ │ ├── dataGenerator.js # Example utility function
│ │
│ └── /features # BDD Cucumber/Gherkin feature files
│
├── /reports # Reports folder (json and html subfolders created automatically)
├── env.local.js
├── env.test.js
├── cucumber.config.js
├── playwright.config.js
├── package.json
├── .gitignore # Must include .env to prevent committing secrets
└── README.md

### 3.2 Configuración Mejorada de Cucumber
El archivo cucumber.config.js debe implementar la siguiente estructura MEJORADA:

**Requisitos Clave:**
- **Formato de Configuración Moderno**: Usar estructura `module.exports = { default: { ... } }`
- **Carga Escalable de Pasos**: Usar patrón `'src/steps/**/*.js'` para cargar automáticamente TODOS los archivos de definición de pasos
- **Integración de Archivos de Soporte**: Incluir `'src/support/**/*.js'` para carga automática de archivos de soporte  
- **Generación Única de Reportes**: Implementar nomenclatura de reportes basada en timestamp para prevenir sobrescrituras
- **Estructura de Directorios Mejorada**: Auto-crear directorios para screenshots, videos, reportes JSON y HTML
- **Retroalimentación Completa**: Proporcionar información detallada de configuración durante la inicialización
- **Reportes Post-ejecución**: Incluir manejador process.on('exit') con información de ubicación de reportes
- **worldParameters Extendidos**: Incluir compartición comprensiva de configuración con definiciones de pasos
- **Manejo de Errores**: Incluir bloques try-catch para carga de configuración con mensajes de error apropiados
- **Retroalimentación Visual de Configuración**: Proporcionar salida de consola clara y amigable con estado de configuración

**Estructura de Plantilla:**
```javascript
// Configuración de Cucumber - Test Runner Principal del Framework
const fs = require('fs');
const path = require('path');
const EnvironmentLoader = require('./src/support/environmentLoader');

// Cargar configuración con manejo de errores
let config;
try {
  config = EnvironmentLoader.getCurrentEnvironmentConfig();
  console.log(`Configuración cargada para entorno: ${config.environment || 'local'}`);
} catch (error) {
  console.error('Error al cargar configuración:', error.message);
  process.exit(1);
}

// Generar nombre único para reportes
const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
const reportName = `cucumber-report-${timestamp}`;

module.exports = {
  default: {
    features: ['src/features/**/*.feature'],
    
    // ESCALABLE: Carga AUTOMÁTICA de todos los steps y support files
    require: [
      'src/steps/**/*.js',     // Carga TODOS los archivos de steps
      'src/support/**/*.js'    // Incluye archivos de soporte
    ],
    
    // Reportes únicos con timestamp
    format: [
      'progress-bar',
      `json:reports/json/${reportName}.json`,
      `html:reports/html/${reportName}.html`
    ],
    
    // WorldParameters MEJORADOS
    worldParameters: {
      environment: config.environment || 'local',
      config: config,
      browser: process.env.BROWSER || config.browser,
      headless: process.env.HEADLESS === 'true' || config.headless,
      baseUrl: config.baseUrl,
      screenshotOnFailure: config.screenshotOnFailure || true,
      videoOnFailure: config.videoOnFailure || false
    },
    
    // Configuración estándar
    formatOptions: { snippetInterface: 'async-await' },
    parallel: config.workers || 1,
    retry: config.retries || 0,
    timeout: config.timeout || 60000,
    tags: process.env.TAGS || 'not @skip'
  }
};

// Crear TODOS los directorios automáticamente
const dirs = ['reports', 'reports/json', 'reports/html', 'reports/screenshots', 'reports/videos'];
dirs.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
    console.log(`Directorio creado: ${dir}`);
  }
});

// Post-procesamiento con información de reportes
process.on('exit', () => {
  console.log('Ejecución completada');
  console.log(`Reportes disponibles en: reports/`);
});
```

**CRÍTICO**: Todos los scripts npm deben referenciar `cucumber.config.js` usando el parámetro `--config cucumber.config.js` para asegurar la carga de configuración mejorada.


## 4. PATRÓN BROWSER FACTORY (OBLIGATORIO)

### 4.1 Visión General del Patrón
El Patrón Browser Factory es **OBLIGATORIO** para la gestión centralizada del navegador. Esto previene múltiples instancias de navegador y asegura una gestión consistente del ciclo de vida del navegador en todas las pruebas.

### 4.2 Componentes Clave
- **`src/support/browserFactory.js`**: Factory central de navegador para crear y gestionar instancias de navegador
- **`src/steps/common.steps.js`**: Archivo único responsable de la gestión del ciclo de vida del navegador (hooks Before/After)
- **Contexto compartido (`this.page`)**: Todos los archivos de pasos usan instancia de página compartida, nunca crean sus propios navegadores

### 4.3 Reglas de Implementación
- **Solo UN archivo gestiona el ciclo de vida del navegador**: Típicamente `common.steps.js` con hooks Before/After
- **OBLIGATORIO**: Debes incluir en `common.steps.js` el "setDefaultTimeout":
´´´
const { Before, After, BeforeAll, AfterAll, Status, setDefaultTimeout } = require('@cucumber/cucumber');
setDefaultTimeout(120000);
´´´
- El "setDefaultTimeout" **debe establecerse en 120000 (120 segundos)**

- **Los archivos de pasos específicos de características NO DEBEN inicializar navegadores**: Usan `this.page` del contexto compartido
- **NO duplicar hooks Before/After**: Solo un conjunto de hooks de gestión de navegador en todos los archivos de pasos
- **Los Page Objects reciben el parámetro `this.page`**: Del contexto compartido, nunca crean sus propias instancias de navegador
- **Instancias de página globales con alcance por archivo de pasos**: Inicializadas con `this.page` cuando sea necesario

### 4.4 Requisitos de Soporte Multi-navegador
- **Soporte para chromium, firefox, webkit**: Selección de navegador vía variable de entorno
- **Compatibilidad cross-browser**: Todos los Page Objects deben funcionar en diferentes tipos de navegador
- **Scripts npm para cada navegador**: Comandos separados para probar diferentes navegadores

### 4.5 Estructura de Browser Factory
```javascript
// Example browserFactory.js structure
class BrowserFactory {
  static async createBrowser(browserType = 'chromium') {
    // Browser creation logic with multi-browser support
  }
  
  static async closeBrowser(browser) {
    // Clean browser closure logic
  }
}
```

### 4.6 Flujo de Ejecución de Browser Factory
1. **Inicia la prueba**: Cucumber ejecuta el hook Before en `common.steps.js`
2. **Creación del navegador**: `common.steps.js` llama a `BrowserFactory.createBrowser()`
3. **Compartición del navegador**: La instancia del navegador se almacena en el contexto compartido (`this.page`)
4. **Ejecución de pasos**: Todos los archivos de pasos usan `this.page` compartido, nunca crean navegadores
5. **Uso de Page Object**: Los Page Objects reciben el parámetro `this.page` de los archivos de pasos
6. **Finalización de la prueba**: Cucumber ejecuta el hook After en `common.steps.js`
7. **Limpieza del navegador**: `common.steps.js` llama a `BrowserFactory.closeBrowser()`

**CRÍTICO**: Solo `common.steps.js` gestiona el ciclo de vida del navegador. Los archivos de pasos específicos de características usan SOLO el contexto compartido.

### 4.7 Integración de Configuración de Browser Factory
**IMPORTANTE**: Dado que la gestión del navegador está centralizada a través del Patrón Browser Factory:
- **playwright.config.js NO se usa funcionalmente** - Existe solo para prevenir errores de dependencias
- **browserFactory.js gestiona TODO** - Configuración completa del navegador, opciones de lanzamiento
- **playwright.config.js es MÍNIMO** - Solo configuración básica para satisfacer dependencias
- **Soporte multi-navegador vía variables de entorno** - BROWSER=chromium|firefox|webkit pasado a browserFactory.js
- **NO opciones complejas de lanzamiento de navegador en playwright.config.js** - Toda configuración específica del navegador debe estar en browserFactory.js
- **Mantener playwright.config.js MÍNIMO** - Solo configuraciones básicas del framework, no gestión de navegador

**CRÍTICO**: playwright.config.js NO se ejecuta durante las pruebas - toda la configuración es vía Cucumber + Browser Factory.

## 5. ARQUITECTURA DE EJECUCIÓN DE PRUEBAS

### 5.1 Jerarquía de Flujo de Ejecución
1. **Cucumber (Ejecutor de Pruebas)** - Punto de entrada principal para toda ejecución de pruebas
2. **Definiciones de Pasos** - Traducen pasos Gherkin en acciones JavaScript
3. **Page Objects** - Encapsulan interacciones del navegador usando Playwright
4. **Playwright** - Realiza la automatización real del navegador (uso interno solamente)

### 5.2 Separación Clara de Responsabilidades
- **Cucumber es el ÚNICO ejecutor de pruebas** - TODA ejecución fluye a través de comandos de Cucumber, NUNCA Playwright directamente
- **Playwright se usa internamente** por las definiciones de pasos a través de Page Objects para automatización del navegador
- **Los scripts npm DEBEN usar comandos cucumber-js**, NUNCA comandos playwright
- **Las definiciones de pasos actúan como puente** conectando pasos Gherkin con acciones de Playwright dentro de Page Objects

### 5.3 Ejemplos de Comandos de Ejecución de Pruebas
```bash
# Basic execution
npm run test - cucumber-js (runs all features)
npm run test:smoke - cucumber-js --tags @smoke
npm run test:feature - cucumber-js src/features/specific.feature

# Multi-browser execution (MANDATORY support)
npm run test:chrome - BROWSER=chromium cucumber-js
npm run test:firefox - BROWSER=firefox cucumber-js
npm run test:webkit - BROWSER=webkit cucumber-js

# Environment-specific execution
npm run test:local - NODE_ENV=local cucumber-js
npm run test:staging - NODE_ENV=test cucumber-js
```

### 5.4 Secuencia de Flujo de Ejecución
1. **El usuario ejecuta comando npm**: Llama a cucumber-js (NO playwright)
2. **Cucumber lee archivos .feature**: Analiza escenarios Gherkin
3. **Cucumber ejecuta definiciones de pasos**: Coincide pasos Gherkin con funciones JavaScript
4. **Las definiciones de pasos llaman a Page Objects**: Pasan el contexto compartido `this.page`
5. **Los Page Objects usan Playwright**: Realizan acciones del navegador (click, type, navigate, etc.)
6. **Browser Factory gestiona el ciclo de vida del navegador**: Crea/cierra navegadores centralmente
7. **Cucumber genera reportes**: Reportes JSON y HTML (NO reportes de Playwright)

### 5.5 Responsabilidades de Carpetas
- `src/features` contiene archivos plantilla de características cucumber BDD para desarrollo futuro de pruebas
- `src/pages` contiene clases plantilla base de page object con estructura de ejemplo para localizadores y métodos de acción
- `src/steps` contiene definiciones de pasos plantilla conectando pasos Gherkin con Page Objects
- `src/support` contiene archivos de soporte para pruebas (plantilla commands.js, **browserFactory.js REQUERIDO**, **environmentLoader.js REQUERIDO**, reportGenerator.js)
- `src/utils` contiene plantillas de funciones de utilidad para pruebas (plantilla dataGenerator.js)

**IMPORTANTE**: Todos los archivos en estas carpetas deben ser ejemplos únicos, NO pruebas específicas de aplicación reales.

## 6. GESTIÓN DE CONFIGURACIÓN

### 6.1 Configuración de Entorno
Cada archivo de entorno (env.local.js, env.test.js) debe exportar configuración usando variables de entorno.

**CRÍTICO**: El archivo `environmentLoader.js` es **OBLIGATORIO** para la gestión centralizada de configuración de entorno:
- **Ubicación**: `src/support/environmentLoader.js`
- **Propósito**: Proporciona carga y validación centralizada de configuraciones de entorno
- **Integración**: Debe ser usado tanto por cucumber.config.js como por otros archivos de configuración
- **Manejo de Errores**: Debe incluir manejo adecuado de errores para configuraciones faltantes o inválidas
- **Soporte Multi-entorno**: Debe soportar la carga de diferentes archivos de entorno (env.local.js, env.test.js)

```javascript
// Ejemplo de configuración estándar (env.local.js, env.test.js)
module.exports = {
  BASE_URL: process.env.BASE_URL || "https://...",
  USERNAME: process.env.USERNAME || "...",
  PASSWORD: process.env.PASSWORD || "...",
  HEADLESS: process.env.HEADLESS === "true" || false,
  BROWSER: process.env.BROWSER || "chromium",
  TIMEOUT: parseInt(process.env.TIMEOUT) || 30000,

  // Configuración de navegador
  SUPPORTED_BROWSERS: ["chromium", "firefox", "webkit"],
  
  // Configuración de viewport
  VIEWPORT_WIDTH: 1280,
  VIEWPORT_HEIGHT: 720,
  
  // Configuración de reportes
  SCREENSHOT_ON_FAILURE: true,
  VIDEO_ON_FAILURE: false,
  
  // Configuración de paralelismo
  WORKERS: 1,
  RETRIES: 0,
  SLOW_MO: parseInt(process.env.SLOW_MO) || 100
};
```

### 6.2 Archivo de Configuración de Playwright
**ACLARACIÓN CRÍTICA**: `playwright.config.js` existe ÚNICAMENTE para prevenir errores de dependencias de Playwright, pero **NO es usado por el framework para ninguna configuración funcional**.

#### 6.2.1 Propósito del Archivo
**¿Por qué existe este archivo?**
- Playwright como paquete npm espera encontrar un archivo de configuración
- Sin este archivo, pueden aparecer advertencias o errores al instalar dependencias
- **NO se ejecuta durante las pruebas** - toda la configuración real está en Cucumber + Browser Factory

**¿Qué contiene?**
- Configuración básica mínima para satisfacer dependencias
- Comentarios claros explicando que NO se usa
- Estructura simple que NO interfiere con Cucumber

#### 6.2.2 Plantilla Obligatoria
```javascript
/**
 * ARCHIVO NO USADO POR EL FRAMEWORK
 * 
 * Este archivo existe SOLO para prevenir errores de dependencias de Playwright.
 * NO se ejecuta durante la ejecución de pruebas.
 * 
 * CONFIGURACIÓN REAL DEL FRAMEWORK:
 * - cucumber.config.js: Configuración principal de Cucumber
 * - browserFactory.js: Gestión completa del navegador
 * - environmentLoader.js: Configuración de entorno
 * - env.*.js: Variables de entorno por entorno
 * 
 * IMPORTANTE: NO agregar configuración funcional aquí.
 * Cualquier cambio de configuración debe hacerse en los archivos listados arriba.
 */

module.exports = {
  // Configuración mínima para prevenir errores
  testDir: './src',
  timeout: 120000,
  use: {
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  }
};
```

#### 6.2.3 Restricciones Obligatorias
**LO QUE NO DEBE CONTENER:**
- Importación de `@playwright/test`
- Configuración de navegador (esta es responsabilidad de browserFactory.js)
- Array `projects` para multi-navegador (manejado por el Patrón Browser Factory)
- Configuración compleja de opciones de lanzamiento
- Configuración de workers o paralelismo

**LO QUE DEBE CONTENER:**
- Comentarios explicativos claros
- Estructura mínima para prevenir errores
- Referencias a archivos de configuración reales
- Advertencia de NO agregar configuración funcional

## 7. SCRIPTS Y REPORTES

### 7.1 Configuración de Scripts NPM (OBLIGATORIO)
**Estructura de scripts package.json requerida:**
```json
{
  "scripts": {
    // Basic execution scripts (MANDATORY)
    "test": "cucumber-js --config cucumber.config.js",
    "test:smoke": "cucumber-js --config cucumber.config.js --tags @smoke",
    "test:regression": "cucumber-js --config cucumber.config.js --tags @regression",
    "test:dry-run": "cucumber-js --config cucumber.config.js --dry-run",
    
    // Environment-specific scripts
    "test:env": "cucumber-js --config cucumber.config.js --env",
    "test:local": "cross-env ENV=local cucumber-js --config cucumber.config.js",
    "test:test": "cross-env ENV=test cucumber-js --config cucumber.config.js",
    
    // Browser execution modes
    "test:headless": "cross-env HEADLESS=true cucumber-js --config cucumber.config.js",
    "test:headed": "cross-env HEADLESS=false cucumber-js --config cucumber.config.js",
    
    // Multi-browser scripts (MANDATORY)
    "test:chrome": "cross-env BROWSER=chromium cucumber-js --config cucumber.config.js",
    "test:firefox": "cross-env BROWSER=firefox cucumber-js --config cucumber.config.js", 
    "test:webkit": "cross-env BROWSER=webkit cucumber-js --config cucumber.config.js",
    
    // Feature-specific execution examples
    "test:feature:auth": "cucumber-js --config cucumber.config.js src/features/autenticacion-usuario.feature",
    "test:feature:accesos": "cucumber-js --config cucumber.config.js src/features/accesos-directos.feature",
    
    // Report generation scripts
    "report": "node src/support/reportGenerator.js",
    "report:generate": "cucumber-html-reporter",
    "report:open": "npx http-server reports/html -p 8080 -o",
    
    // Utility scripts
    "clean": "node clean.js"
  }
}
```

**CRÍTICO**: Todos los scripts usan el comando `cucumber-js --config cucumber.config.js`, NUNCA comandos `playwright` directamente.

### 7.2 Reportes
Después de la ejecución, generar:
- Reporte JSON de Cucumber en /reports/json/ (carpeta creada automáticamente si no existe).
- Reporte HTML generado desde JSON en /reports/html/ (carpeta creada automáticamente si no existe).
- Agregar scripts npm para generación de reportes.
**Nota**: Todos los reportes son generados por la ejecución de Cucumber, no Playwright directamente. Las subcarpetas se crean automáticamente durante la generación de reportes.

## 8. REQUISITOS DE DOCUMENTACIÓN E IDIOMA

### 8.1 Requisitos de README.md
Debe incluir (todo el contenido en español):
- Descripción del proyecto.
- Pasos de instalación.
- **Sección de seguridad** explicando cómo configurar variables de entorno.
- **Instrucciones para crear archivo `.env`**.
- Cómo seleccionar entorno (--env test).
- **Cómo ejecutar todas las pruebas usando comandos de Cucumber** (cucumber-js).
- **Cómo ejecutar pruebas por etiqueta usando Cucumber** (cucumber-js --tags).
- Cómo ver reportes.
- **Mejores prácticas de seguridad** para manejo de credenciales.
- **Énfasis claro de que toda ejecución de pruebas es a través de Cucumber, no Playwright directamente.**

### 8.2 Requisitos de Idioma, Estilo y Licencia
- **Toda documentación, archivos README, comentarios y texto orientado al usuario deben estar escritos en español.**
- **Los comentarios de código deben ser naturales y comprensibles, evitando lenguaje robótico o excesivamente técnico.**
- **Los logs y mensajes de error (console.log, console.error, etc.) deben ser claros, amigables y en español, SIN ICONOS NI EMOJIS.**
- **PROHIBICIÓN: No deben aparecer iconos o emojis en NINGÚN archivo de código (.js, .json, archivos .config), solo permitidos en README.md.**
- **Todos los archivos de código deben estar completamente libres de símbolos visuales, iconos, emojis o caracteres decorativos.**
- Los nombres de variables y funciones pueden estar en inglés para claridad técnica.

### 8.3 Requisitos de Licencia y Autoría
- **La licencia del proyecto debe ser GPLv3.**
- **El campo author en package.json debe ser "Knowmadmood".**
- Incluir encabezados de licencia GPLv3 en archivos fuente cuando sea necesario.

## 9. GUÍAS DE IMPLEMENTACIÓN Y MEJORES PRÁCTICAS

### 9.1 Requisitos de Licencia y Autoría
**Configuración de Licencia:**
- **Usar licencia GPLv3** en package.json
- **El campo author debe ser "Knowmadmood"** en package.json
- Incluir encabezados de licencia apropiados en archivos fuente cuando sea requerido

### 9.2 Mejores Prácticas a Aplicar
**Organización de Código:**
- Agrupar acciones reutilizables en funciones helper en /support
- Mantener las definiciones de pasos simples; toda la lógica en Page Objects  
- Mantener convenciones de nomenclatura consistentes
- Usar CamelCase para nombrar archivos de páginas y pasos
- **NO herencia o clases base**: Cada Page Object debe ser independiente

**Flujo de Implementación:**
- No es necesario pedir crear carpetas o archivos, solo implementar la estructura como se describe
- Implementar toda la estructura dentro de la nueva carpeta especificada
- Copiar archivos .feature sin modificación, análisis o implementación basada en ellos

### 9.3 Guías de Implementación
**Estructura de Trabajo:**
- Crear una nueva carpeta en el directorio raíz del workspace con el nombre especificado
- Usar estas instrucciones de Playwright para configurar la estructura del framework en esa carpeta
- Implementar todo el código generado exclusivamente dentro de la nueva carpeta
- Almacenar todas las salidas y archivos de prueba generados en esa carpeta

**Manejo de Archivos de Características:**
- Copiar archivos .feature de la carpeta del proyecto BDD proporcionada a src/features sin modificación
- **OBLIGATORIO**: NO leer, analizar o crear archivos de prueba basados en estas características
- **SOLO COPIAR** los archivos .feature tal como están

### 9.4 Requisitos de Salida
Cuando se solicite, siempre:

- **Crear la estructura completa de carpetas/archivos** como se describe arriba.
- **SOLO Copiar archivos .feature** del proyecto proporcionado a src/features.
- **Configurar scripts package.json para usar comandos de Cucumber** (cucumber-js) para ejecución de pruebas.
- **Asegurar que npm install && npm run test funciona** usando Cucumber como el ejecutor de pruebas.
- **Escribir toda documentación y comentarios en español.**
- **Enfatizar en la documentación que las pruebas se ejecutan vía Cucumber, no Playwright directamente.**

## 10. SOLUCIÓN DE PROBLEMAS Y CRITERIOS DE CALIDAD

### 10.1 Solución de Problemas de Flujo de Ejecución
**Problemas Comunes de Ejecución y Soluciones:**

**Problema**: Las pruebas no se ejecutan al usar `npm run test`
- **Solución**: Verificar que los scripts package.json usan `cucumber-js`, NO comandos `playwright`
- **Comprobar**: Asegurar que cucumber.config.js está configurado correctamente

**Problema**: Múltiples instancias de navegador o conflictos de navegador
- **Solución**: Verificar que solo `common.steps.js` contiene hooks Before/After para gestión de navegador
- **Comprobar**: Asegurar que los archivos de pasos específicos de características usan `this.page` del contexto compartido

**Problema**: Las variables de entorno no se cargan
- **Solución**: Verificar que el archivo `.env` existe y está formateado correctamente
- **Comprobar**: Asegurar que los archivos de entorno (env.local.js, env.test.js) exportan la configuración correctamente

**Problema**: Browser Factory no funciona
- **Solución**: Verificar que `browserFactory.js` exporta clase/funciones correctamente
- **Comprobar**: Asegurar que `common.steps.js` importa y usa Browser Factory correctamente

**Problema**: Las pruebas cross-browser fallan
- **Solución**: Verificar que la variable de entorno BROWSER está configurada correctamente
- **Comprobar**: Asegurar que los Page Objects funcionan en diferentes tipos de navegador

### 10.2 Objetivo Final de Calidad
Producir una estructura de framework Playwright de alta calidad y mantenible que:

**Arquitectura del Framework:**
- **Se adhiere al patrón de diseño Page Object Model** sin herencia
- **Se integra sin problemas con el flujo de ejecución Cucumber-Playwright**
- **Implementa el Patrón Browser Factory centralizado** para gestión de navegador
- **Mantiene separación clara** entre ejecutor de pruebas (Cucumber) y motor de automatización (Playwright)
- **Soporta configuración de entorno** a través de archivos .env

**Claridad de Ejecución:**
- **Cucumber como ÚNICO ejecutor de pruebas** - Toda ejecución a través de comandos cucumber-js
- **Jerarquía de ejecución clara** - npm → Cucumber → Definiciones de Pasos → Page Objects → Playwright
- **Gestión centralizada de navegador** - Gestor único de ciclo de vida con patrón de contexto compartido
- **Soporte multi-navegador** - Selección de navegador impulsada por variables de entorno
