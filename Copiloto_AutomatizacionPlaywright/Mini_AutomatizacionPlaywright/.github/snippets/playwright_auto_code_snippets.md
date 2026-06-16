---
description: Biblioteca de snippets de código reutilizables para el copiloto Playwright Automation
version: 1.0
lastUpdated: 2026-04-23
---

# Reusable Code Snippets - Playwright Automation

This-file=all-reusable-JS-snippets-for-copilot.
REFERENCE-from-other-files:[Ver snippet:<snippet-name>]

---

[snippet:page-object-basico]
PAGE-OBJECT-MODEL-BASIC:

```javascript
// src/pages/LoginPage.js
// CORRECT:PO-receives-page-via-constructor+uses-separate-locators

const LoginPageLocators=require('./pagesLocators/LoginPageLocators');

class LoginPage{
  /**@param{Page}page-Playwright-page-instance-from-shared-context
     @param{string}[baseUrl]-test-env-base-URL(optional)*/
  constructor(page,baseUrl){
    this.page=page;
    this.baseUrl=baseUrl||null;
    this.initializeLocators();
  }

  initializeLocators(){
    this.locators={
      usernameInput:LoginPageLocators.USERNAME_INPUT,
      passwordInput:LoginPageLocators.PASSWORD_INPUT,
      loginButton:LoginPageLocators.LOGIN_BUTTON,
      errorMessage:LoginPageLocators.ERROR_MESSAGE
    };
  }

  async navigate(){
    console.log('Navegando a la pagina de login...');
    try{
      const url=this.baseUrl||'http://localhost:3000';
      await this.page.goto(url,{waitUntil:'domcontentloaded',timeout:60000});
      await this.page.waitForSelector(this.locators.usernameInput,{timeout:30000});
      console.log('Navegacion a la pagina de login completada');
    }catch(error){
      throw new Error(`Error al navegar a la pagina de login: ${error.message}`);
    }
  }

  async fillUsername(username){
    console.log(`Ingresando nombre de usuario: ${username}`);
    try{
      const element=this.page.locator(this.locators.usernameInput).first();
      await element.waitFor({state:'visible',timeout:15000});
      await element.fill(username);
      console.log('Usuario ingresado correctamente');
    }catch(error){
      throw new Error(`Error al ingresar el nombre de usuario: ${error.message}`);
    }
  }

  async fillPassword(password){
    console.log('Ingresando contrasenia...');
    try{
      const element=this.page.locator(this.locators.passwordInput).first();
      await element.waitFor({state:'visible',timeout:15000});
      await element.fill(password);
      console.log('Contrasenia ingresada correctamente');
    }catch(error){
      throw new Error(`Error al ingresar la contrasenia: ${error.message}`);
    }
  }

  async clickLoginButton(){
    console.log('Haciendo clic en el boton de login...');
    try{
      const button=this.page.locator(this.locators.loginButton).first();
      await button.waitFor({state:'visible',timeout:10000});
      await button.click();
      console.log('Clic en boton de login ejecutado');
    }catch(error){
      throw new Error(`Error al hacer clic en el boton de login: ${error.message}`);
    }
  }

  async isLoggedIn(){
    try{
      await this.page.waitForURL(/dashboard|inicio|home/,{timeout:15000});
      return true;
    }catch{
      return false;
    }
  }
}

module.exports=LoginPage;

// INCORRECT:NEVER-create-Playwright-instances-in-PO
class LoginPage{
  constructor(){
    const {chromium}=require('playwright');
    this.browser=await chromium.launch();  // NEVER
  }
}
```

---

[snippet:localizadores-constantes]
LOCATORS-AS-CONSTANTS-IN-SEPARATE-FILE:

```javascript
// src/pages/pagesLocators/LoginPageLocators.js
// CORRECT:centralized-locators-in-separate-file(UPPER_SNAKE_CASE-constants)

class LoginPageLocators{
  static USERNAME_INPUT='#inputLoginUsuario';
  static PASSWORD_INPUT='#inputLoginContrasenia';
  static LOGIN_BUTTON='[data-testid="login-btn"]';
  static ERROR_MESSAGE='.alert-error';
  static BACKGROUND_WEB='.formLogin';
}

module.exports=LoginPageLocators;

// INCORRECT:inline-locators(in-POs|Steps)
async fillUsername(username){
  await this.page.fill('#inputLoginUsuario',username);  // AVOID
}
```

---

[snippet:steps-playwright]
STEPS-WITH-SHARED-CONTEXT(this.page):

```javascript
// src/steps/login.steps.js
// CORRECT:Step-uses-this.page-from-shared-context

const {Given,When,Then}=require('@cucumber/cucumber');
const LoginPage=require('../pages/LoginPage');

Given('que estoy en la pagina de login',{timeout:90000},async function(){
  console.log('Paso: Navegando a la pagina de login');
  try{
    this.loginPage=new LoginPage(this.page,this.baseUrl);
    await this.loginPage.navigate();
    console.log('Usuario en la pagina de login');
  }catch(error){
    console.error(`Error en paso "estoy en la pagina de login": ${error.message}`);
    throw error;
  }
});

When('ingreso mis credenciales validas',async function(){
  console.log('Paso: Ingresando credenciales validas');
  try{
    if(!this.loginPage){
      this.loginPage=new LoginPage(this.page,this.baseUrl);
    }
    const username=this.config.username||process.env.APP_USERNAME;
    const password=this.config.password||process.env.APP_PASSWORD;
    if(!username||!password){
      throw new Error('No se encontraron credenciales validas en la configuracion');
    }
    await this.loginPage.fillUsername(username);
    await this.loginPage.fillPassword(password);
    console.log('Credenciales validas ingresadas correctamente');
  }catch(error){
    console.error(`Error al ingresar credenciales: ${error.message}`);
    throw error;
  }
});

Then('el sistema muestra la pagina de inicio',async function(){
  console.log('Verificando acceso al sistema...');
  const isLogged=await this.loginPage.isLoggedIn();
  if(!isLogged){
    throw new Error('El usuario no fue autenticado correctamente tras el login');
  }
  console.log('Autenticacion correcta. Sistema mostrando pagina de inicio');
});

// INCORRECT:NEVER-create-Before/After-hooks(in-Steps!=common.steps.js)
Before(async function(){
  const {chromium}=require('playwright');
  this.browser=await chromium.launch();  // PROHIBITED
  this.page=await this.browser.newPage();
});
```

---

[snippet:common-steps]
BROWSER-LIFECYCLE-MANAGEMENT(ONLY-in-common.steps.js):

```javascript
// src/steps/common.steps.js
// ONLY-file-managing-browser-lifecycle

const {Before,After,BeforeAll,AfterAll}=require('@cucumber/cucumber');
const BrowserFactory=require('../support/browserFactory');

BeforeAll(async function(){
  console.log('\n=== INICIANDO SUITE DE PRUEBAS ===');
  console.log('Framework: Cucumber + Playwright');
  console.log('Patron: Page Object Model + Browser Factory');
  console.log('===================================\n');
});

Before(async function(scenario){
  console.log(`\n=== INICIANDO ESCENARIO: ${scenario.pickle.name} ===`);
  await new Promise(resolve=>setTimeout(resolve,2000));  // safety-delay-for-batch-exec
  try{
    const worldParams=this.parameters;
    const browserType=worldParams.browser||'chromium';
    const headlessMode=worldParams.headless!==undefined?worldParams.headless:true;
    const slowMo=worldParams.slowMo||100;

    const browserInstance=await BrowserFactory.createBrowser(browserType,{
      headless:headlessMode,
      slowMo:slowMo,
      timeout:worldParams.timeout,
      viewportWidth:worldParams.viewportWidth,
      viewportHeight:worldParams.viewportHeight,
      recordVideo:worldParams.videoOnFailure
    });

    // share-instances-with-all-step-files
    this.page=browserInstance.page;
    this.browser=browserInstance.browser;
    this.context=browserInstance.context;
    this.baseUrl=worldParams.baseUrl;
    this.config=worldParams.config;
    this.scenarioName=scenario.pickle.name;

    console.log('Navegador iniciado y contexto compartido configurado');
  }catch(error){
    console.error('Error al inicializar navegador:',error.message);
    throw error;
  }
});

After(async function(scenario){
  console.log(`\n=== FINALIZANDO ESCENARIO: ${scenario.pickle.name} ===`);
  try{
    if(scenario.result?.status==='failed'&&this.page&&!this.page.isClosed()){
      await BrowserFactory.captureFailureScreenshot(this.page,this.scenarioName);
    }
    const browserToClose=this.browser;
    const contextToClose=this.context;
    this.page=null;this.browser=null;this.context=null;
    this.baseUrl=null;this.config=null;this.scenarioName=null;
    await BrowserFactory.closeBrowser(browserToClose,contextToClose);
    console.log(`Estado del escenario: ${scenario.result?.status||'completado'}`);
  }catch(error){
    console.error('Error al finalizar escenario:',error.message);
  }
});
```

---

[snippet:browser-factory]
BROWSER-FACTORY-PATTERN:

```javascript
// src/support/browserFactory.js
// CORRECT:central-factory,local-vars(NOT-static)

const {chromium,firefox,webkit}=require('playwright');

class BrowserFactory{

  static async createBrowser(browserType='chromium',options={}){
    console.log(`Iniciando navegador: ${browserType}`);
    const defaultOptions={
      headless:options.headless!==undefined?options.headless:true,
      slowMo:options.slowMo||100,
      args:['--no-sandbox','--disable-setuid-sandbox']
    };
    let browserInstance;
    switch(browserType.toLowerCase()){
      case 'chromium':browserInstance=await chromium.launch(defaultOptions);break;
      case 'firefox':browserInstance=await firefox.launch(defaultOptions);break;
      case 'webkit':browserInstance=await webkit.launch(defaultOptions);break;
      default:throw new Error(`Navegador no soportado: ${browserType}`);
    }
    const contextInstance=await browserInstance.newContext({
      viewport:{width:options.viewportWidth||1280,height:options.viewportHeight||720},
      locale:'es-ES',
      timezoneId:'Europe/Madrid'
    });
    const pageInstance=await contextInstance.newPage();
    pageInstance.setDefaultTimeout(options.timeout||30000);
    console.log(`Navegador ${browserType} iniciado exitosamente`);
    return {browser:browserInstance,context:contextInstance,page:pageInstance};
  }

  static async closeBrowser(browser,context){
    try{
      if(context)await context.close();
      if(browser)await browser.close();
      console.log('Navegador cerrado correctamente');
    }catch(error){
      console.error('Error al cerrar el navegador:',error.message);
    }
  }

  static async captureFailureScreenshot(page,scenarioName){
    try{
      const safeName=scenarioName.replace(/[^a-zA-Z0-9]/g,'_');
      const timestamp=new Date().toISOString().replace(/[:.]/g,'-');
      const screenshotPath=`reports/screenshots/fallo_${safeName}_${timestamp}.png`;
      await page.screenshot({path:screenshotPath,fullPage:true});
      console.log(`Screenshot de fallo guardado: ${screenshotPath}`);
    }catch(error){
      console.error('No se pudo capturar el screenshot de fallo:',error.message);
    }
  }
}

module.exports=BrowserFactory;
```

---

[snippet:waits-playwright]
EXPLICIT-WAITS-WITH-STATE-CONDITIONS:

```javascript
// CORRECT:waits-with-state-conditions(Playwright)

const element=page.locator('#elemento');
await element.waitFor({state:'visible',timeout:15000});

await page.locator('#boton').waitFor({state:'visible',timeout:10000});  // clickable(visible+enabled)

await page.waitForURL(/dashboard|inicio/,{timeout:20000});  # URL-change-after-nav

await page.waitForLoadState('domcontentloaded',{timeout:30000});  # page-load-state

await page.getByText('Texto esperado').waitFor({state:'visible',timeout:10000});  # specific-text

await page.locator('.loading-spinner').waitFor({state:'hidden',timeout:20000});  # element-disappears(loading,spinner)

// INCORRECT:NEVER-use-fixed-waits
await page.waitForTimeout(3000);  // NEVER
```

---

[snippet:inspeccion-dinamica]
DYNAMIC-DOM-INSPECTION-SCRIPT:

Temp-script-to-inspect-actual-DOM-elements(when-no-source-code-access|framesets/dynamic-elements)

```javascript
// inspect_{element}.js
// temp-script-for-page-element-inspection
// useful-for:legacy-apps,framesets,no-source-code-access

const {chromium}=require('playwright');

(async()=>{
  const browser=await chromium.launch({headless:false,slowMo:1000});
  const context=await browser.newContext();
  const page=await context.newPage();
  
  console.log('Navegando a la página...');
  await page.goto('https://tu-aplicacion.com',{waitUntil:'domcontentloaded'});
  await page.waitForLoadState('networkidle');
  await page.waitForTimeout(3000);  # additional-JS-loading-wait
  
  console.log('\n=== ANÁLISIS DE LA PÁGINA ===\n');
  
  const frames=page.frames();
  console.log(`Total de frames: ${frames.length}`);
  
  for(let i=0;i<frames.length;i++){
    const frame=frames[i];
    console.log(`\n--- FRAME ${i+1} ---`);
    console.log(`URL: ${frame.url()}`);
    console.log(`Nombre: ${frame.name()||'sin-nombre'}`);
    
    try{
      const inputs=await frame.locator('input').all();
      console.log(`Inputs encontrados: ${inputs.length}`);
      
      for(let j=0;j<Math.min(inputs.length,5);j++){
        const input=inputs[j];
        const id=await input.getAttribute('id').catch(()=>'sin-id');
        const name=await input.getAttribute('name').catch(()=>'sin-name');
        const type=await input.getAttribute('type').catch(()=>'sin-type');
        console.log(`  Input ${j+1}: id="${id}", name="${name}", type="${type}"`);
      }
      
      const buttons=await frame.locator('button, input[type="submit"]').all();
      console.log(`Botones encontrados: ${buttons.length}`);
      
      for(let j=0;j<Math.min(buttons.length,5);j++){
        const button=buttons[j];
        const id=await button.getAttribute('id').catch(()=>'sin-id');
        const text=await button.textContent().catch(()=>'');
        console.log(`  Botón ${j+1}: id="${id}", texto="${text.trim()}"`);
      }
      
      const links=await frame.locator('a').all();
      console.log(`Enlaces encontrados: ${links.length}`);
      
      for(let j=0;j<Math.min(links.length,5);j++){
        const link=links[j];
        const href=await link.getAttribute('href').catch(()=>'');
        const text=await link.textContent().catch(()=>'');
        console.log(`  Link ${j+1}: href="${href}", texto="${text.trim()}"`);
      }
      
    }catch(error){
      console.log(`Error al inspeccionar frame ${i+1}: ${error.message}`);
    }
  }
  
  console.log('\n=== Inspección completada ===');
  console.log('Presiona ENTER para cerrar el navegador...');
  
  await new Promise(resolve=>{
    process.stdin.once('data',resolve);
  });
  
  await browser.close();
  console.log('Navegador cerrado.');
})();
```

WHEN-TO-USE:
-legacy-apps-with-framesets
-JSP/Servlet-architectures(server-side-rendering)
-dynamically-generated-elements(JavaScript)
-no-access-to-app-source-code
-need-to-detect-selectors-from-actual-rendered-HTML

NAMING-CONVENTION:
-inspect_login.js:login-page-inspection
-inspect_menu.js:side-menu/navigation-inspection
-inspect_{element}.js:general-pattern

EXECUTION:
```bash
node inspect_login.js
```

---

[snippet:datos-clase]
DATA-CLASS-FOR-SCENARIO:

```javascript
// src/datas/LoginData.js
// simple-data-class-to-share-info-between-scenario-steps

class LoginData{
  constructor(){
    this.usuarios=[];
  }

  addUsername(username){
    this.usuarios.push(username);
  }

  getFirstUsername(){
    return this.usuarios[0];
  }

  getUsernameByPosition(position){
    return this.usuarios[position];
  }

  getAllUsers(){
    return this.usuarios;
  }
}

module.exports=LoginData;
```

---

[snippet:npm-commands]
NPM-EXECUTION-COMMANDS:

```bash
npm run test  # all-tests
npm run test:smoke  # specific-tag
npm run test:regression
npm run test:headless  # CI-mode
npm run test:headed  # visible-mode(for-engineer-review)
npm run test:chrome  # specific-browser
npm run test:firefox
npm run test:webkit
npm run test:local  # by-env
npm run test:test
npx cucumber-js --config cucumber.config.js src/features/Login.feature  # specific-feature-inline
npx cucumber-js --config cucumber.config.js --tags "@smoke"  # specific-tag-inline
npm run test:dry-run  # validate-without-executing
npm run report  # generate-HTML-report-from-JSON
```

---

[snippet:cucumber-tags]
CUCUMBER-TAGS-FOR-SELECTIVE-EXECUTION:

```gherkin
# CORRECT:tags-at-individual-scenario-level
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

# INCORRECT:@pendiente-only-at-Feature-level
@pendiente
Caracteristica: Login
  # all-scenarios-inherit-@pendiente(not-granular)
```

---

[snippet:patron-antipatron]
PROHIBITED-PATTERNS-QUICK-REFERENCE:

```javascript
// PROHIBITED:create-browser-outside-browserFactory.js
const {chromium}=require('playwright');
const browser=await chromium.launch();  # outside-browserFactory.js

// PROHIBITED:fixed-wait
await page.waitForTimeout(3000);  # equiv-sleep

// PROHIBITED:Before/After-hooks-outside-common.steps.js
Before(async function(){
  this.browser=await chromium.launch();  # only-in-common.steps.js
  this.page=await this.browser.newPage();
});

// PROHIBITED:hardcoded-URL|credentials
const baseUrl='https://app.example.com';  # use-process.env|env-files
const password='micontrasenia123';  # NEVER-in-source-code

// PROHIBITED:inline-locator-in-Steps(must-be-in-*PageLocators.js)
await this.page.click('#loginButton');  # direct-page-access-in-Step

// PROHIBITED:inline-SQL-queries
const result=await db.query("SELECT * FROM usuarios WHERE id = 1");  # use-QueryDeposit.js
```
