---
description: Biblioteca de snippets de código reutilizables para el copiloto Playwright Automation
version: 1.0
lastUpdated: 2026-04-23
---

# Snippets de Código Reutilizables - Playwright Automation

Este fichero contiene todos los snippets de código JavaScript reutilizables del copiloto.
**Referencia desde otros ficheros usando:** `[Ver snippet: <nombre-snippet>]`

---

## [snippet:page-object-basico]
### Page Object Model Básico

```javascript
// src/pages/LoginPage.js
// Correcto — Page Object recibe page por constructor y usa localizadores separados

const LoginPageLocators = require('./pagesLocators/LoginPageLocators');

class LoginPage {

  /**
   * Constructor del Page Object de Login
   * @param {Page} page - Instancia de pagina de Playwright desde contexto compartido
   * @param {string} [baseUrl] - URL base del entorno de pruebas (opcional)
   */
  constructor(page, baseUrl) {
    this.page = page;
    this.baseUrl = baseUrl || null;
    this.initializeLocators();
  }

  initializeLocators() {
    this.locators = {
      usernameInput:  LoginPageLocators.USERNAME_INPUT,
      passwordInput:  LoginPageLocators.PASSWORD_INPUT,
      loginButton:    LoginPageLocators.LOGIN_BUTTON,
      errorMessage:   LoginPageLocators.ERROR_MESSAGE
    };
  }

  async navigate() {
    console.log('Navegando a la pagina de login...');
    try {
      const url = this.baseUrl || 'http://localhost:3000';
      await this.page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await this.page.waitForSelector(this.locators.usernameInput, { timeout: 30000 });
      console.log('Navegacion a la pagina de login completada');
    } catch (error) {
      throw new Error(`Error al navegar a la pagina de login: ${error.message}`);
    }
  }

  async fillUsername(username) {
    console.log(`Ingresando nombre de usuario: ${username}`);
    try {
      const element = this.page.locator(this.locators.usernameInput).first();
      await element.waitFor({ state: 'visible', timeout: 15000 });
      await element.fill(username);
      console.log('Usuario ingresado correctamente');
    } catch (error) {
      throw new Error(`Error al ingresar el nombre de usuario: ${error.message}`);
    }
  }

  async fillPassword(password) {
    console.log('Ingresando contrasenia...');
    try {
      const element = this.page.locator(this.locators.passwordInput).first();
      await element.waitFor({ state: 'visible', timeout: 15000 });
      await element.fill(password);
      console.log('Contrasenia ingresada correctamente');
    } catch (error) {
      throw new Error(`Error al ingresar la contrasenia: ${error.message}`);
    }
  }

  async clickLoginButton() {
    console.log('Haciendo clic en el boton de login...');
    try {
      const button = this.page.locator(this.locators.loginButton).first();
      await button.waitFor({ state: 'visible', timeout: 10000 });
      await button.click();
      console.log('Clic en boton de login ejecutado');
    } catch (error) {
      throw new Error(`Error al hacer clic en el boton de login: ${error.message}`);
    }
  }

  async isLoggedIn() {
    try {
      await this.page.waitForURL(/dashboard|inicio|home/, { timeout: 15000 });
      return true;
    } catch {
      return false;
    }
  }
}

module.exports = LoginPage;

// Incorrecto — Nunca crear instancias de Playwright en el Page Object
class LoginPage {
  constructor() {
    const { chromium } = require('playwright');
    this.browser = await chromium.launch(); // NUNCA
  }
}
```

---

## [snippet:localizadores-constantes]
### Localizadores como Constantes en Archivo Separado

```javascript
// src/pages/pagesLocators/LoginPageLocators.js
// Correcto — Localizadores centralizados en archivo separado como constantes UPPER_SNAKE_CASE

class LoginPageLocators {
  // Campos del formulario de login
  static USERNAME_INPUT   = '#inputLoginUsuario';
  static PASSWORD_INPUT   = '#inputLoginContrasenia';
  static LOGIN_BUTTON     = '[data-testid="login-btn"]';
  static ERROR_MESSAGE    = '.alert-error';
  static BACKGROUND_WEB   = '.formLogin';
}

module.exports = LoginPageLocators;

// Incorrecto — Localizadores inline en Page Objects o Steps
async fillUsername(username) {
  await this.page.fill('#inputLoginUsuario', username); // Evitar
}
```

---

## [snippet:steps-playwright]
### Steps con Contexto Compartido (this.page)

```javascript
// src/steps/login.steps.js
// Correcto — Step usa this.page del contexto compartido

const { Given, When, Then } = require('@cucumber/cucumber');
const LoginPage = require('../pages/LoginPage');

Given('que estoy en la pagina de login', { timeout: 90000 }, async function() {
  console.log('Paso: Navegando a la pagina de login');
  try {
    // Inicializar el Page Object con el contexto compartido
    this.loginPage = new LoginPage(this.page, this.baseUrl);
    await this.loginPage.navigate();
    console.log('Usuario en la pagina de login');
  } catch (error) {
    console.error(`Error en paso "estoy en la pagina de login": ${error.message}`);
    throw error;
  }
});

When('ingreso mis credenciales validas', async function() {
  console.log('Paso: Ingresando credenciales validas');
  try {
    if (!this.loginPage) {
      this.loginPage = new LoginPage(this.page, this.baseUrl);
    }
    // Obtener credenciales desde configuracion del entorno
    const username = this.config.username || process.env.APP_USERNAME;
    const password = this.config.password || process.env.APP_PASSWORD;
    if (!username || !password) {
      throw new Error('No se encontraron credenciales validas en la configuracion');
    }
    await this.loginPage.fillUsername(username);
    await this.loginPage.fillPassword(password);
    console.log('Credenciales validas ingresadas correctamente');
  } catch (error) {
    console.error(`Error al ingresar credenciales: ${error.message}`);
    throw error;
  }
});

Then('el sistema muestra la pagina de inicio', async function() {
  console.log('Verificando acceso al sistema...');
  const isLogged = await this.loginPage.isLoggedIn();
  if (!isLogged) {
    throw new Error('El usuario no fue autenticado correctamente tras el login');
  }
  console.log('Autenticacion correcta. Sistema mostrando pagina de inicio');
});

// Incorrecto — Nunca crear hooks Before/After en Steps que no sean common.steps.js
Before(async function() {
  const { chromium } = require('playwright');
  this.browser = await chromium.launch(); // PROHIBIDO
  this.page = await this.browser.newPage();
});
```

---

## [snippet:common-steps]
### Gestión del Ciclo de Vida del Navegador (Solo en common.steps.js)

```javascript
// src/steps/common.steps.js
// Unico archivo que gestiona el ciclo de vida del navegador

const { Before, After, BeforeAll, AfterAll } = require('@cucumber/cucumber');
const BrowserFactory = require('../support/browserFactory');

BeforeAll(async function() {
  console.log('\n=== INICIANDO SUITE DE PRUEBAS ===');
  console.log('Framework: Cucumber + Playwright');
  console.log('Patron: Page Object Model + Browser Factory');
  console.log('===================================\n');
});

Before(async function(scenario) {
  console.log(`\n=== INICIANDO ESCENARIO: ${scenario.pickle.name} ===`);
  await new Promise(resolve => setTimeout(resolve, 2000)); // Delay de seguridad para ejecucion batch
  try {
    const worldParams = this.parameters;
    const browserType  = worldParams.browser   || 'chromium';
    const headlessMode = worldParams.headless  !== undefined ? worldParams.headless : true;
    const slowMo       = worldParams.slowMo    || 100;

    const browserInstance = await BrowserFactory.createBrowser(browserType, {
      headless:        headlessMode,
      slowMo:          slowMo,
      timeout:         worldParams.timeout,
      viewportWidth:   worldParams.viewportWidth,
      viewportHeight:  worldParams.viewportHeight,
      recordVideo:     worldParams.videoOnFailure
    });

    // Compartir instancias con todos los archivos de pasos
    this.page          = browserInstance.page;
    this.browser       = browserInstance.browser;
    this.context       = browserInstance.context;
    this.baseUrl       = worldParams.baseUrl;
    this.config        = worldParams.config;
    this.scenarioName  = scenario.pickle.name;

    console.log('Navegador iniciado y contexto compartido configurado');
  } catch (error) {
    console.error('Error al inicializar navegador:', error.message);
    throw error;
  }
});

After(async function(scenario) {
  console.log(`\n=== FINALIZANDO ESCENARIO: ${scenario.pickle.name} ===`);
  try {
    if (scenario.result?.status === 'failed' && this.page && !this.page.isClosed()) {
      await BrowserFactory.captureFailureScreenshot(this.page, this.scenarioName);
    }
    const browserToClose = this.browser;
    const contextToClose = this.context;
    this.page = null; this.browser = null; this.context = null;
    this.baseUrl = null; this.config = null; this.scenarioName = null;
    await BrowserFactory.closeBrowser(browserToClose, contextToClose);
    console.log(`Estado del escenario: ${scenario.result?.status || 'completado'}`);
  } catch (error) {
    console.error('Error al finalizar escenario:', error.message);
  }
});
```

---

## [snippet:browser-factory]
### Browser Factory Pattern

```javascript
// src/support/browserFactory.js
// Correcto — Factory central, variables locales (NO estaticas)

const { chromium, firefox, webkit } = require('playwright');

class BrowserFactory {

  static async createBrowser(browserType = 'chromium', options = {}) {
    console.log(`Iniciando navegador: ${browserType}`);
    const defaultOptions = {
      headless: options.headless !== undefined ? options.headless : true,
      slowMo: options.slowMo || 100,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    };
    let browserInstance;
    switch (browserType.toLowerCase()) {
      case 'chromium': browserInstance = await chromium.launch(defaultOptions); break;
      case 'firefox':  browserInstance = await firefox.launch(defaultOptions);  break;
      case 'webkit':   browserInstance = await webkit.launch(defaultOptions);   break;
      default: throw new Error(`Navegador no soportado: ${browserType}`);
    }
    const contextInstance = await browserInstance.newContext({
      viewport: { width: options.viewportWidth || 1280, height: options.viewportHeight || 720 },
      locale: 'es-ES',
      timezoneId: 'Europe/Madrid'
    });
    const pageInstance = await contextInstance.newPage();
    pageInstance.setDefaultTimeout(options.timeout || 30000);
    console.log(`Navegador ${browserType} iniciado exitosamente`);
    return { browser: browserInstance, context: contextInstance, page: pageInstance };
  }

  static async closeBrowser(browser, context) {
    try {
      if (context) await context.close();
      if (browser) await browser.close();
      console.log('Navegador cerrado correctamente');
    } catch (error) {
      console.error('Error al cerrar el navegador:', error.message);
    }
  }

  static async captureFailureScreenshot(page, scenarioName) {
    try {
      const safeName = scenarioName.replace(/[^a-zA-Z0-9]/g, '_');
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      const screenshotPath = `reports/screenshots/fallo_${safeName}_${timestamp}.png`;
      await page.screenshot({ path: screenshotPath, fullPage: true });
      console.log(`Screenshot de fallo guardado: ${screenshotPath}`);
    } catch (error) {
      console.error('No se pudo capturar el screenshot de fallo:', error.message);
    }
  }
}

module.exports = BrowserFactory;
```

---

## [snippet:waits-playwright]
### Esperas Explícitas con Condiciones de Estado

```javascript
// Correcto — Esperas con condiciones de estado usando Playwright

// Esperar visibilidad de un elemento con locator
const element = page.locator('#elemento');
await element.waitFor({ state: 'visible', timeout: 15000 });

// Esperar que un elemento sea clickable (visible + enabled)
await page.locator('#boton').waitFor({ state: 'visible', timeout: 10000 });

// Esperar que la URL cambie tras navegacion
await page.waitForURL(/dashboard|inicio/, { timeout: 20000 });

// Esperar estado de carga de la pagina
await page.waitForLoadState('domcontentloaded', { timeout: 30000 });

// Esperar que aparezca un texto especifico
await page.getByText('Texto esperado').waitFor({ state: 'visible', timeout: 10000 });

// Esperar que desaparezca un elemento (carga, spinner, etc.)
await page.locator('.loading-spinner').waitFor({ state: 'hidden', timeout: 20000 });

// Incorrecto — Nunca usar esperas fijas
await page.waitForTimeout(3000); // NUNCA
```

---

## [snippet:inspeccion-dinamica]
### Script de Inspección Dinámica del DOM

Script temporal para inspeccionar elementos del DOM real cuando no hay acceso al código fuente o para aplicaciones con framesets/elementos dinámicos.

```javascript
// inspect_{elemento}.js
// Script temporal para inspección de elementos de la página
// Útil para aplicaciones legacy, framesets, o sin acceso al código fuente

const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ 
    headless: false,
    slowMo: 1000 
  });
  
  const context = await browser.newContext();
  const page = await context.newPage();
  
  console.log('Navegando a la página...');
  await page.goto('https://tu-aplicacion.com', { waitUntil: 'domcontentloaded' });
  await page.waitForLoadState('networkidle');
  
  // Esperar carga adicional de JavaScript
  await page.waitForTimeout(3000);
  
  console.log('\n=== ANÁLISIS DE LA PÁGINA ===\n');
  
  // Detectar frames
  const frames = page.frames();
  console.log(`Total de frames: ${frames.length}`);
  
  // Inspeccionar cada frame
  for (let i = 0; i < frames.length; i++) {
    const frame = frames[i];
    console.log(`\n--- FRAME ${i + 1} ---`);
    console.log(`URL: ${frame.url()}`);
    console.log(`Nombre: ${frame.name() || 'sin-nombre'}`);
    
    try {
      // Buscar inputs
      const inputs = await frame.locator('input').all();
      console.log(`Inputs encontrados: ${inputs.length}`);
      
      for (let j = 0; j < Math.min(inputs.length, 5); j++) {
        const input = inputs[j];
        const id = await input.getAttribute('id').catch(() => 'sin-id');
        const name = await input.getAttribute('name').catch(() => 'sin-name');
        const type = await input.getAttribute('type').catch(() => 'sin-type');
        console.log(`  Input ${j + 1}: id="${id}", name="${name}", type="${type}"`);
      }
      
      // Buscar botones
      const buttons = await frame.locator('button, input[type="submit"]').all();
      console.log(`Botones encontrados: ${buttons.length}`);
      
      for (let j = 0; j < Math.min(buttons.length, 5); j++) {
        const button = buttons[j];
        const id = await button.getAttribute('id').catch(() => 'sin-id');
        const text = await button.textContent().catch(() => '');
        console.log(`  Botón ${j + 1}: id="${id}", texto="${text.trim()}"`);
      }
      
      // Buscar enlaces (útil para menús)
      const links = await frame.locator('a').all();
      console.log(`Enlaces encontrados: ${links.length}`);
      
      for (let j = 0; j < Math.min(links.length, 5); j++) {
        const link = links[j];
        const href = await link.getAttribute('href').catch(() => '');
        const text = await link.textContent().catch(() => '');
        console.log(`  Link ${j + 1}: href="${href}", texto="${text.trim()}"`);
      }
      
    } catch (error) {
      console.log(`Error al inspeccionar frame ${i + 1}: ${error.message}`);
    }
  }
  
  console.log('\n=== Inspección completada ===');
  console.log('Presiona ENTER para cerrar el navegador...');
  
  // Mantener navegador abierto para inspección manual
  await new Promise(resolve => {
    process.stdin.once('data', resolve);
  });
  
  await browser.close();
  console.log('Navegador cerrado.');
})();
```

**Cuándo usar este enfoque:**
- Aplicaciones legacy con framesets
- Arquitecturas JSP/Servlets con renderizado servidor
- Elementos generados dinámicamente por JavaScript
- Sin acceso al código fuente de la aplicación
- Necesidad de detectar selectores del HTML real renderizado

**Convención de nombres:**
- `inspect_login.js` - Inspección de página de login
- `inspect_menu.js` - Inspección del menú lateral/navegación
- `inspect_{elemento}.js` - Patrón general

**Ejecución:**
```bash
node inspect_login.js
```

---

## [snippet:datos-clase]
### Clase de Datos para el Escenario

```javascript
// src/datas/LoginData.js
// Clase de datos simple para compartir informacion entre pasos del escenario

class LoginData {

  constructor() {
    this.usuarios = [];
  }

  addUsername(username) {
    this.usuarios.push(username);
  }

  getFirstUsername() {
    return this.usuarios[0];
  }

  getUsernameByPosition(position) {
    return this.usuarios[position];
  }

  getAllUsers() {
    return this.usuarios;
  }
}

module.exports = LoginData;
```

---

## [snippet:npm-commands]
### Comandos de Ejecución con npm

```bash
# Ejecutar todos los tests
npm run test

# Ejecutar con tag especifico
npm run test:smoke
npm run test:regression

# Ejecutar modo headless (CI)
npm run test:headless

# Ejecutar modo visible (para revisión del ingeniero)
npm run test:headed

# Ejecutar en navegador especifico
npm run test:chrome
npm run test:firefox
npm run test:webkit

# Ejecutar por entorno
npm run test:local
npm run test:test

# Ejecutar una feature especifica inline
npx cucumber-js --config cucumber.config.js src/features/Login.feature

# Ejecutar un tag especifico inline
npx cucumber-js --config cucumber.config.js --tags "@smoke"

# Validar sin ejecutar (dry-run)
npm run test:dry-run

# Generar reporte HTML desde JSON
npm run report
```

---

## [snippet:cucumber-tags]
### Tags de Cucumber para Ejecución Selectiva

```gherkin
# Correcto — Tags a nivel de escenario individual
@smoke @login
Escenario: Login con credenciales validas
  Dado que estoy en la pagina de login
  Cuando ingreso mis credenciales validas
  Entonces el sistema muestra la pagina de inicio

@regression @login @pendiente
Escenario: Login con cuenta bloqueada
  Dado que el usuario tiene la cuenta bloqueada
  Cuando intenta iniciar sesion
  Entonces el sistema muestra mensaje de cuenta bloqueada

# Incorrecto — @pendiente solo a nivel de Feature
@pendiente
Caracteristica: Login
  # Todos los escenarios heredan @pendiente (no granular)
```

---

## [snippet:patron-antipatron]
### Patrones Prohibidos — Referencia Rápida

```javascript
// PROHIBIDO — Crear navegador fuera de browserFactory.js
const { chromium } = require('playwright');
const browser = await chromium.launch();           // fuera de browserFactory.js

// PROHIBIDO — Espera fija
await page.waitForTimeout(3000);                   // equivalente a sleep

// PROHIBIDO — Hooks Before/After fuera de common.steps.js
Before(async function() {
  this.browser = await chromium.launch();          // solo en common.steps.js
  this.page = await this.browser.newPage();
});

// PROHIBIDO — URL o credenciales hardcodeadas
const baseUrl = 'https://app.example.com';         // usar process.env o archivos de entorno
const password = 'micontrasenia123';               // NUNCA en codigo fuente

// PROHIBIDO — Localizador inline en Steps (debe estar en *PageLocators.js)
await this.page.click('#loginButton');             // acceso directo a page en Step

// PROHIBIDO — Queries SQL inline
const result = await db.query("SELECT * FROM usuarios WHERE id = 1"); // usar QueryDeposit.js
```
