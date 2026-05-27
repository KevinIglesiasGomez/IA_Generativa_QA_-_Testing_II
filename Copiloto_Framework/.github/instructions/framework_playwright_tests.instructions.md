### Objetivo

Crear pruebas utilizando:

- \*_Cucumber como el ejecutor principal de pruebas_### Configuración de Cucumber

- Usar el cucumber.config.js existente que debe:
  - Cargar la configuración de entorno usando el mismo patrón que la configuración de Playwright.
  - **NUNCA codificar valores específicos del entorno.**
  - Establecer las rutas para los archivos de características y definiciones de pasos.
  - Habilitar informes JSON de Cucumber después de cada ejecución.
  - Definir la ubicación de archivos .feature y definiciones de pasos.
  - Generar informes JSON de Cucumber en /reports (subcarpetas creadas automáticamente).
  - Añadir timeout a cucumber.config.js (timeout: 120000,)
  - Permitir ejecutar pruebas filtradas por @tags.
  - Integrarse con el ciclo de vida de pruebas de Playwright.
  - Incluir manejo adecuado de errores para la carga de configuración de entorno.
  - **Configurar Cucumber como el ejecutor principal de pruebas** - toda ejecución de pruebas fluye a través de comandos de Cucumber.ejecución con archivos .feature en sintaxis Gherkin.
- Playwright para automatización funcional e2e (usado por las definiciones de pasos de Cucumber).
- JavaScript como lenguaje de programación y usar CommonJS.
- Patrón de diseño Page Object Model (POM) para mantenibilidad y reutilización
- Configurar Cucumber para relacionar pasos Gherkin con acciones de Playwright.
- **Toda ejecución de pruebas se realiza a través de comandos de Cucumber, no Playwright directamente.**
- No debes generar scripts de instalación. Todo lo requerido debe hacerse usando comandos nativos y debe documentarse en el Readme.
- Usar variables de entorno existentes en archivos de configuración env para toda configuración e información sensible (URLs, credenciales, timeouts).
- Debe incluir informes JSON de Cucumber después de cada ejecución.
- Debe ser fácil de instalar y ejecutar con documentación clara en español.
**IMPORTANTE**: Las pruebas se ejecutan a través de comandos de Cucumber (cucumber-js), no comandos de playwright.

### Requisitos de Análisis

- **Leer y analizar SOLO el archivo .feature **{input:feature_name}** completamente** de la carpeta del proyecto BDD proporcionada para comprender todos los escenarios que necesitan ser implementados.
- **Revisar páginas JSP o HTML estáticas** disponibles en la carpeta proporcionada para obtener información sobre la estructura, localizadores y comportamiento de la aplicación.
- **Todos los pasos descritos en los escenarios de características Gherkin BDD** deben implementarse como archivos .js dentro de la carpeta src/steps con Page Objects correspondientes.

### INFORMACIÓN de Arquitectura

Este proyecto sigue esta estructura:
- `src/features` contiene nuestras pruebas cucumber BDD de la carpeta del proyecto proporcionada, copiadas sin modificación.
- `src/pages` contiene nuestros page objects para las pruebas con métodos de localizadores y acciones, creados basados en análisis JSP/HTML.
- `src/steps` contiene nuestras definiciones de pasos para las pruebas, implementando TODOS los pasos de los archivos .feature analizados.
- `src/support` contiene nuestros archivos de soporte para las pruebas. **DEBE incluir browserFactory.js**
- `src/utils` contiene nuestras funciones de utilidad para las pruebas. Ejemplo: dataGenerator.js
- `fixtures` contiene nuestros fixtures para las pruebas.

### Patrón Browser Factory (OBLIGATORIO PARA TODAS LAS PRUEBAS)

**CRÍTICO**: Todas las implementaciones de pruebas DEBEN usar el Patrón Browser Factory existente:

```javascript
// Use existing browserFactory.js in src/support/
const BrowserFactory = require('../support/browserFactory');

// In step definitions:
Before(async function () {
  const browserName = BrowserFactory.getBrowserFromEnv();
  
  browser = await BrowserFactory.createBrowser(browserName, {
    headless: envConfig.HEADLESS,
    slowMo: envConfig.SLOW_MO
  });
  
  // ...rest of setup...
});
```

**NUNCA crear instancias de navegador directas** - Siempre usar BrowserFactory.createBrowser().

### Requisitos de Seguridad

- **NUNCA codificar información sensible** en ningún archivo que será confirmado en control de versiones.
- **Todas las URLs, credenciales y datos específicos del entorno** deben usar variables de entorno.
- **Proporcionar documentación clara** sobre cómo configurar variables de entorno de forma segura.

### Arquitectura de Ejecución de Pruebas

- **Cucumber es el ejecutor principal de pruebas** - toda ejecución de pruebas fluye a través de comandos de Cucumber.
- **Playwright se usa internamente** por las definiciones de pasos para realizar automatización del navegador.
- **El Patrón Browser Factory** centraliza la gestión del navegador para soporte multi-navegador.
- **Los scripts npm deben usar comandos cucumber-js**, no comandos playwright.
- **Utilizar HEADLESS false** para ver en todo momento la ejecución de las pruebas en el navegador.
- **Ejemplos de ejecución de pruebas**:
  - `npm run test` → `cucumber-js` (runs all features)
  - `npm run test:smoke` → `cucumber-js --tags @smoke`
  - `npm run test:feature` → `cucumber-js src/features/specific.feature`
  - `npx cucumber-js --name "Nombre del escenario"` → Run an specific scenario
  
  **Ejecución multi-navegador (DISPONIBLE)**:
  - `npm run test:chrome` → Ejecutar pruebas en Chromium
  - `npm run test:firefox` → Ejecutar pruebas en Firefox  
  - `npm run test:safari` → Ejecutar pruebas en WebKit/Safari
  - `npm run test:all-browsers` → Ejecutar pruebas en todos los navegadores secuencialmente
  - `npm run test:browsers-parallel` → Ejecutar pruebas en todos los navegadores en paralelo
  - `CICOSTOOLS_BROWSER=firefox npm run test` → Ejecutar con navegador específico vía variable de entorno

- **Las definiciones de pasos conectan los pasos Gherkin con acciones de Playwright** dentro de Page Objects.

### Configuración de Entorno
- **NUNCA codificar información sensible** como URLs, nombres de usuario, contraseñas o datos específicos del entorno. Usar archivos de configuración env existentes.
- Siempre usar variables `process.env` con valores predeterminados sensatos.

### Configuración de Playwright

- **playwright.config.js NO ES USADO por el framework** pero existe para prevenir errores de dependencias:
  - **El archivo NO tiene propósito funcional** en el flujo de ejecución de pruebas.
  - Toda la configuración del navegador se gestiona a través de browserFactory.js.
  - **NUNCA codificar valores** en playwright.config.js ya que no se ejecuta.
  - La configuración de entorno se maneja por cucumber.config.js y browserFactory.js.

  - Anadir configuración de hooks en 'common.steps.js':
```javascript
  const { Before, After, BeforeAll, AfterAll, setDefaultTimeout } = require('@cucumber/cucumber');
```

  - **OBLIGATORIO**: Establecer timeout global para pasos en 'common.steps.js':
```javascript 
  setDefaultTimeout(120000);
```
- **OBLIGATORIO**: Instala la dependencia @playwright/test 'npm install @playwright/test --save' si no está ya instalada.
- **OBLIGATORIO**: Instala el paquetes cucumber-html-reporter 'npm install cucumber-html-reporter --save' si no está ya instalado.

### Reportes

    Después de la ejecución, generar:
    - Informe JSON de Cucumber en /reports/json/ (carpeta creada automáticamente si no existe).
    - Informe HTML generado desde JSON en /reports/html/ (carpeta creada automáticamente si no existe).
    - Agregar scripts npm para generación de reportes.
    **Nota**: Todos los reportes son generados por la ejecución de Cucumber, no Playwright directamente. Las subcarpetas se crean automáticamente durante la generación de reportes.

### Gestión de Escenarios Pendientes

- **OBLIGATORIO: Etiquetar escenarios no implementados con `@pendiente`** a nivel individual de cada escenario.
- **NUNCA usar `@pendiente` solo a nivel de Característica** - debe aplicarse a cada escenario individualmente.
- **Los escenarios marcados con `@pendiente`** aparecerán como "pendiente" en los reportes en lugar de "undefined".
- **Patrón correcto para escenarios pendientes**:
  ```gherkin
  @smoke @feature-tag @pendiente
  Escenario: Nombre del escenario
    Dado que...
  ```
- **Los escenarios con `@pendiente` se ejecutarán pero saltarán la implementación real**, mostrando estado "pendiente" en reportes.
- **Ventajas del uso de `@pendiente`**:
  - Diferencia clara entre escenarios no implementados (pendiente) vs errores de implementación (undefined).
  - Permite tracking de cobertura de pruebas planificadas vs implementadas.
  - Los reportes muestran claramente el estado de cada escenario.

### Requisitos de Idioma

- **Toda documentación, archivos README, comentarios y texto orientado al usuario deben estar escritos en español.**
- Los comentarios de código deben estar en español.
- Los nombres de variables y funciones pueden permanecer en inglés para claridad técnica.

### Mejores Prácticas a Aplicar

- **Nunca codificar URLs, credenciales o variables de entorno** en ningún archivo de configuración.
- **Siempre usar variables de entorno** con `process.env` y proporcionar valores predeterminados sensatos.
- **Incluir el paquete `dotenv`** para cargar variables de entorno desde archivos `.env`.
- **OBLIGATORIO: Usar el Patrón Browser Factory existente** - Nunca crear instancias de navegador directas.
- **OBLIGATORIO: Aprovechar capacidades multi-navegador** - Usar scripts npm proporcionados para pruebas cross-browser.
- **OBLIGATORIO: Etiquetar escenarios no implementados con `@pending`** a nivel individual de cada escenario.
- Analizar las Pages previas (src/pages) y definiciones de pasos previas (src/steps) para código reutilizable.
- **Analizar browserFactory.js existente** para patrones de gestión de navegador consistentes.
- Usar constantes para localizadores dentro de Page Objects.
- Agrupar acciones reutilizables en funciones helper en /support.
- Mantener las definiciones de pasos simples; toda la lógica en Page Objects.
- Mantener convenciones de nomenclatura consistentes.
- **Analizar archivos JSP/HTML existentes para identificar localizadores correctos y comprender el flujo de la aplicación.**
- **Crear Page Objects que reflejen con precisión la estructura de la aplicación basado en análisis JSP.**
- **Implementar TODOS los pasos Gherkin encontrados en el archivo .feature proporcionado **{input:feature_name}**.**
- **Si un escenario no puede implementarse completamente, marcarlo con `@pending` individual** para tracking correcto.

### Reglas de Gestión de Navegador (CRÍTICO)

**NUNCA hacer esto:**
```javascript
// ❌ INCORRECTO - Creación directa de navegador
const browser = await chromium.launch();
```

**SIEMPRE hacer esto:**
```javascript
// ✅ CORRECTO - Usar Browser Factory
const BrowserFactory = require('../support/browserFactory');
const browser = await BrowserFactory.createBrowser();
```

### Guías de Implementación

- **Usar estas instrucciones de pruebas de Playwright** para implementar las pruebas en la carpeta existente **${input:playwright_folder}**.
- **Implementar todo el código generado exclusivamente** dentro de la nueva carpeta.
- **Almacenar todas las salidas y archivos de prueba generados** en esa carpeta.
- **Usar el archivo .feature** proporcionado sin modificaciones.
- **Analizar archivos JSP/HTML** para entender la estructura de la aplicación y crear Page Objects precisos.
- **Implementar definiciones de pasos** para cada paso Gherkin encontrado en el archivo de características **{input:feature_name}**.

### Requisito de Salida

Cuando se solicite, siempre:

- **Analizar el archivo de características proporcionado** llamado **{input:feature_name}** para comprender el alcance completo de los requisitos de prueba.
- **Revisar archivos JSP/HTML** para entender la estructura de la aplicación e identificar localizadores precisos.
- **Implementar Page Objects** basados en análisis JSP/HTML con localizadores y acciones precisas.
- **Crear definiciones de pasos** para cada paso Gherkin encontrado en el archivo de características.
- **Configurar scripts package.json para usar comandos de Cucumber** (cucumber-js) para ejecución de pruebas.
- **Asegurar que npm install && npm run test funcione** usando Cucumber como ejecutor de pruebas.
- **Escribir toda documentación y comentarios en español.**
- **Enfatizar en la documentación que las pruebas se ejecutan vía Cucumber, no Playwright directamente.**

### Objetivo

Producir scripts de prueba Playwright de alta calidad y mantenibles que:

- **Implementen TODOS los escenarios Gherkin proporcionados** de los archivos .feature.
- **Se adhieran al patrón de diseño Page Object Model.**
- **Se integren sin problemas con la estructura existente del framework Playwright.**
- **Automaticen correctamente navegación e interacciones** usando análisis JSP/HTML para localizadores precisos.
