---
description: Instrucciones de buenas prácticas de Playwright para el agente Playwright Automation
applyTo: "**/*.js,**/*.feature"
---

# Playwright Best Practices for Agent: Playwright Automation

SELECTORS(Playwright+JavaScript):

RECOMMENDED(priority):
1.page.getByTestId('submit-button')  # data-testid-attrs
2.page.locator('#username')  # unique-IDs
3.page.locator('[name="email"]')  # name-attr
4.page.getByRole('button',{name:'Iniciar Sesión'})  # ARIA-roles
5.page.getByText('Texto exacto')  # visible-text
6.page.locator('.selector-css-especifico')  # specific+stable-CSS

AVOID:
-generic-CSS-classes:.btn-primary
-absolute-XPath:/html/body/div[1]/div[2]/button
-numeric-positions:ul>li:nth-child(3)
-frequently-changing-selectors

---

WAITS:

See-example:.github/snippets/playwright_auto_code_snippets.md:[snippet:waits-playwright]

PRINCIPLES:
-use:page.locator().waitFor({state:'visible'})  # wait-visibility
-use:page.waitForSelector(selector,{state:'visible'})  # wait-with-selector
-use:page.waitForURL(pattern)  # navigation-waits
-use:page.waitForLoadState('domcontentloaded')  # after-navigations
-NEVER:page.waitForTimeout()  # fixed-values(equiv=sleep)

---

PAGE-OBJECT-MODEL:

See-example:.github/snippets/playwright_auto_code_snippets.md:[snippet:page-object-basico],[snippet:localizadores-constantes]

PRINCIPLES:
-locators=constants-in-separate-files(*PageLocators.js)
-Page-Objects-NO-assertions(responsibility=Steps)
-page-instance=received-via-constructor(never-created-in-PO)
-method-initializeLocators()=init-locators-from-locator-file
-include-error-handling(each-PO-method,descriptive-msgs)

---

STEP-ORGANIZATION(Cucumber):

```javascript
// login.steps.js — steps for Login.feature
const {Given,When,Then}=require('@cucumber/cucumber');
const LoginPage=require('../pages/LoginPage');

Given('que estoy en la pagina de login',{timeout:90000},async function(){
  this.loginPage=new LoginPage(this.page);
  await this.loginPage.navigate();
});

When('ingreso mis credenciales validas',async function(){
  const username=this.config.username||process.env.APP_USERNAME;
  const password=this.config.password||process.env.APP_PASSWORD;
  await this.loginPage.fillUsername(username);
  await this.loginPage.fillPassword(password);
});

Then('el sistema muestra la pagina de inicio',async function(){
  const isLogged=await this.loginPage.isLoggedIn();
  if(!isLogged){
    throw new Error('El usuario no fue autenticado correctamente');
  }
});
```

NAMING-CONVENTIONS:
-Steps-files:{funcionalidad}.steps.js
-async-methods-in-Steps:camelCase(descriptive-of-Gherkin-step)
-Page-Object-files:{Funcionalidad}Page.js
-Locator-files:{Funcionalidad}PageLocators.js

---

BROWSER-MANAGEMENT(Browser Factory):

See-example:.github/snippets/playwright_auto_code_snippets.md:[snippet:common-steps]

Remember:this-framework=ONLY-common.steps.js-executes-browser-setup/teardown.Cucumber-Before/After-pattern=exclusively-in-that-file.NEVER-duplicate-hooks-in-other-step-files.

---

ERROR-HANDLING(Page Objects):

```javascript
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
```

---

BEST-PRACTICES-VALIDATION:

INDEPENDENCE:
-Incorrect:tests-depend-on-exec-order
-Correct:each-scenario=create-own-test-data
-Correct:state-cleanup-in-After-hook(common.steps.js)

SELECTORS:
-Incorrect:absolute-XPath|generic-CSS-classes
-Correct:IDs,data-testid,ARIA-roles,visible-text

WAITS:
-Incorrect:page.waitForTimeout()  # fixed-values
-Correct:explicit-waits-with-state-conditions

ORGANIZATION:
-Correct:tags(@smoke,@regression,@critical,per-scenario)
-Correct:one-Page-Object-per-app-page
-Correct:locators-in-separate-files(*PageLocators.js)
-Incorrect:duplicate-code-between-Step-files

SECURITY:
-Incorrect:credentials+URLs-directly-in-source-code
-Correct:process-env-vars+environment-files
