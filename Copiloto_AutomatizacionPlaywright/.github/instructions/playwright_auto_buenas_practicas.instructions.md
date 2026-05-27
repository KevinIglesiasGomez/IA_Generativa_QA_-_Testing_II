---
description: Instrucciones de buenas prácticas de Playwright para el agente Playwright Automation
applyTo: "**/*.js,**/*.feature"
---

# Instrucciones de Buenas Prácticas de Playwright para el Agente: Playwright Automation

## 1. Selectores (Playwright con JavaScript)

### Recomendados (prioridad)
1. `page.getByTestId('submit-button')` - Atributos data-testid
2. `page.locator('#username')` - IDs únicos
3. `page.locator('[name="email"]')` - Atributo name
4. `page.getByRole('button', { name: 'Iniciar Sesión' })` - ARIA roles
5. `page.getByText('Texto exacto')` - Texto visible
6. `page.locator('.selector-css-especifico')` - CSS específico y estable

### Evitar
- Clases CSS genéricas: `.btn-primary`
- XPath absolutos: `/html/body/div[1]/div[2]/button`
- Posiciones numéricas: `ul > li:nth-child(3)`
- Selectores que cambien con frecuencia

---

## 2. Waits (Esperas)

Ver ejemplo en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:waits-playwright]`

**Principios:**
- Usar `page.locator().waitFor({ state: 'visible' })` para esperar visibilidad
- Usar `page.waitForSelector(selector, { state: 'visible' })` para espera con selector
- Usar `page.waitForURL(pattern)` para esperas de navegación
- Usar `page.waitForLoadState('domcontentloaded')` tras navegaciones
- **NUNCA** usar `page.waitForTimeout()` con valores fijos (equivalente a sleep)

---

## 3. Page Object Model

Ver ejemplo en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:page-object-basico]` y `[snippet:localizadores-constantes]`

**Principios:**
- Localizadores definidos como constantes en archivos `*PageLocators.js` separados
- Los Page Objects NO hacen aserciones (esa responsabilidad es del Step)
- La instancia de `page` se recibe por constructor, nunca se crea en el Page Object
- Método `initializeLocators()` inicializa los localizadores desde el archivo de localizadores
- Incluir manejo de errores en cada método del Page Object con mensajes descriptivos

---

## 4. Organización de Steps (Cucumber)

```javascript
// login.steps.js — Pasos del escenario Login.feature
const { Given, When, Then } = require('@cucumber/cucumber');
const LoginPage = require('../pages/LoginPage');

Given('que estoy en la pagina de login', { timeout: 90000 }, async function() {
  this.loginPage = new LoginPage(this.page);
  await this.loginPage.navigate();
});

When('ingreso mis credenciales validas', async function() {
  const username = this.config.username || process.env.APP_USERNAME;
  const password = this.config.password || process.env.APP_PASSWORD;
  await this.loginPage.fillUsername(username);
  await this.loginPage.fillPassword(password);
});

Then('el sistema muestra la pagina de inicio', async function() {
  const isLogged = await this.loginPage.isLoggedIn();
  if (!isLogged) {
    throw new Error('El usuario no fue autenticado correctamente');
  }
});
```

**Naming conventions:**
- Archivos Steps: `{funcionalidad}.steps.js`
- Métodos async en Steps: descriptivos del paso Gherkin en camelCase
- Archivos Page Objects: `{Funcionalidad}Page.js`
- Archivos Localizadores: `{Funcionalidad}PageLocators.js`

---

## 5. Gestión del Navegador (Browser Factory)

Ver ejemplo en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:common-steps]`

Recuerda: en este framework solo `common.steps.js` ejecuta setup/teardown del navegador. El patrón `Before`/`After` de Cucumber se usa exclusivamente en ese archivo. **NUNCA** duplicar estos hooks en otros archivos de steps.

---

## 6. Manejo de Errores en Page Objects

```javascript
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
```

---

## 7. Buenas prácticas a validar

### Independencia
- Incorrecto: Tests que dependen del orden de ejecución
- Correcto: Cada escenario crea sus propios datos de prueba
- Correcto: Limpieza del estado en el hook After de `common.steps.js`

### Selectores
- Incorrecto: XPath absolutos o clases CSS genéricas
- Correcto: IDs, data-testid, ARIA roles, texto visible

### Waits
- Incorrecto: `page.waitForTimeout()` con valores fijos
- Correcto: Esperas explícitas con condiciones de estado

### Organización
- Correcto: Tags @smoke, @regression, @critical por escenario
- Correcto: Un Page Object por página de la aplicación
- Correcto: Localizadores en archivos separados `*PageLocators.js`
- Incorrecto: Duplicar código entre archivos de Steps

### Seguridad
- Incorrecto: Credenciales y URLs directamente en el código fuente
- Correcto: Variables de proceso `process.env` y archivos de entorno

---
