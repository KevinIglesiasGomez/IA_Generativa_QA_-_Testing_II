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

## 8. Reutilización de Código Existente (OBLIGATORIO)

Antes de automatizar un nuevo escenario, es **OBLIGATORIO** verificar y reutilizar lo que ya existe en el framework para evitar duplicación de código:

### 8.1 Reutilización de pasos (Steps)
- **OBLIGATORIO** revisar todos los archivos `*.steps.js` existentes en `src/steps/` antes de crear un paso nuevo.
- **IMPORTANTE** no se deben duplicar pasos que ya existan; si un paso Gherkin coincide (exacto o parametrizable) con uno ya implementado, reutilízalo.
- **OBLIGATORIO** si existe un step con redacción distinta pero que realiza la **misma acción o validación funcional** que necesita el nuevo escenario, generaliza/parametriza la **Cucumber Expression o regex** del step existente para que cubra ambas redacciones, en lugar de crear un step nuevo casi duplicado.
- **PROHIBIDO** modificar el texto del archivo `.feature` para forzar que coincida con un step existente; la adaptación siempre se hace en la definición del step (`*.steps.js`), nunca en el Gherkin.
- **NOTA** la reutilización de pasos es clave para mantener consistencia y reducir esfuerzo de mantenimiento entre features.

### 8.2 Reutilización de Page Objects y Localizadores
- Reutilizar Page Objects existentes en `src/pages/` siempre que la funcionalidad ya esté cubierta; extenderlos con nuevos métodos en lugar de crear un Page Object duplicado para la misma página.
- **OBLIGATORIO** si existe un método de Page Object **funcionalmente equivalente** (misma acción o validación, con distinto nombre, parámetros o alcance) al que necesita el nuevo escenario, generaliza/parametriza ese método existente para cubrir ambos casos, en lugar de crear un método nuevo casi duplicado.
- Reutilizar localizadores ya definidos en `src/pages/pagesLocators/` antes de declarar uno nuevo para el mismo elemento.
- **OBLIGATORIO** si existe un localizador **funcionalmente equivalente** (mismo elemento o mismo tipo de componente, con selector ligeramente distinto) al que necesita el nuevo escenario, reutilízalo o generalízalo (p.ej. parametrizando el selector) en lugar de declarar uno nuevo casi idéntico.

### 8.3 Reutilización de utilidades y métodos comunes
- Reutilizar funciones ya existentes en `src/utils/CommonUtilities.js`, `src/support/commands.js` y demás utilidades del framework antes de escribir lógica nueva equivalente.
- **OBLIGATORIO** si existe una función **funcionalmente equivalente** (misma lógica con distinto nombre, firma o parámetros) a la que necesita el nuevo escenario, generaliza/parametriza esa función existente en lugar de crear una nueva casi duplicada.
- Reutilizar las queries ya definidas en `src/utils/QueryDeposit.js`; solo agregar una query nueva si no existe una equivalente. Si existe una query **funcionalmente equivalente** (mismo resultado con filtros o parámetros distintos), parametrízala en lugar de duplicarla.
- Evitar la duplicación de lógica: si una funcionalidad se repite entre dos o más Steps/Page Objects, extraerla a una utilidad compartida en `src/utils/` o `src/support/`.
