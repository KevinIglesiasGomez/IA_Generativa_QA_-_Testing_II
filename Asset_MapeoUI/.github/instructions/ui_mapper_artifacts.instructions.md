---
applyTo: "ui-map/**"
description: "Plantillas, estructuras y convenciones para generacion de artefactos de testing en Step 5: Page Objects (Playwright/Cypress/Selenium/Appium), locator files (.locators.json), mapas UI JSON e informes de recomendaciones."
---
# Instrucciones de Generacion de Artefactos para Testing

## Objetivo

Estas instrucciones definen las plantillas y convenciones para la generacion de artefactos de testing en el Step 5. Define los formatos exactos de Page Objects, locator files, mapas UI JSON e informes de recomendaciones.

---

## 1. ESTRUCTURA DE CARPETAS DE SALIDA

Todos los artefactos se generan en la carpeta `ui-map/` dentro del directorio de trabajo del copiloto (no en el proyecto analizado).

```
ui-map/
|-- [nombre-app]/
    |-- pages/
        |-- LoginPage.js              (Page Object Playwright)
        |-- LoginPage.cy.js           (Page Object Cypress)
        |-- LoginPage.java            (Page Object Selenium/Appium)
    |-- locators/
        |-- login.locators.js         (Locator constants Playwright/Cypress)
        |-- login.locators.json       (Locator file Appium)
        |-- login.locators.ts         (Locator constants TypeScript)
    |-- ui-map.json                   (Mapa UI completo en JSON)
    |-- recommendations.md           (Informe de selectores fragiles)
```

---

## 2. PLANTILLA PAGE OBJECT PARA PLAYWRIGHT (JavaScript)

### Convencion de nombres de fichero

`[NombrePantalla]Page.js` en PascalCase.
Ejemplos: `LoginPage.js`, `UserProfilePage.js`, `ProductListPage.js`

### Plantilla

```javascript
// Pagina: [Nombre de la pantalla en el idioma de la aplicacion]
// Ruta de la aplicacion: [ruta o URL de la pantalla]
// Generado por: UI Mapper Copilot
// Fecha: [fecha de generacion]

const { LOCATORS } = require('../locators/[nombre-pantalla].locators');

class [NombrePantalla]Page {

  constructor(page) {
    this.page = page;
  }

  // Elementos de la pantalla
  get [nombreElemento]() {
    return this.page.locator(LOCATORS.[NOMBRE_CONSTANTE]);
  }

  // Acciones de la pantalla
  async [accionDescriptiva]([parametros]) {
    // [descripcion de la accion en espanol]
    await this.[nombreElemento].fill([parametros]);
  }

  async [accionDescriptiva2]() {
    // [descripcion de la accion en espanol]
    await this.[nombreElemento].click();
  }

  // Verificaciones de la pantalla
  async verificar[Estado]() {
    // [descripcion de lo que se verifica]
    return this.[nombreElemento].isVisible();
  }

}

module.exports = { [NombrePantalla]Page };
```

### Ejemplo generado (pantalla Login, app React)

```javascript
// Pagina: Login
// Ruta de la aplicacion: /login
// Generado por: UI Mapper Copilot

const { LOCATORS } = require('../locators/login.locators');

class LoginPage {

  constructor(page) {
    this.page = page;
  }

  // Elementos de la pantalla
  get usernameInput() {
    return this.page.locator(LOCATORS.USERNAME_INPUT);
  }

  get passwordInput() {
    return this.page.locator(LOCATORS.PASSWORD_INPUT);
  }

  get submitButton() {
    return this.page.locator(LOCATORS.SUBMIT_BUTTON);
  }

  get forgotPasswordLink() {
    return this.page.locator(LOCATORS.FORGOT_PASSWORD_LINK);
  }

  get errorMessage() {
    return this.page.locator(LOCATORS.ERROR_MESSAGE);
  }

  // Acciones de la pantalla
  async introducirUsuario(usuario) {
    // Rellena el campo de nombre de usuario
    await this.usernameInput.fill(usuario);
  }

  async introducirPassword(password) {
    // Rellena el campo de contrasena
    await this.passwordInput.fill(password);
  }

  async clickSubmit() {
    // Hace click en el boton de inicio de sesion
    await this.submitButton.click();
  }

  async iniciarSesion(usuario, password) {
    // Flujo completo de inicio de sesion
    await this.introducirUsuario(usuario);
    await this.introducirPassword(password);
    await this.clickSubmit();
  }

  // Verificaciones de la pantalla
  async verificarErrorVisible() {
    return this.errorMessage.isVisible();
  }

  async verificarTextdoError() {
    return this.errorMessage.textContent();
  }
}

module.exports = { LoginPage };
```

---

## 3. PLANTILLA LOCATOR CONSTANTS PARA PLAYWRIGHT/CYPRESS (JavaScript)

### Convencion de nombres de fichero

`[nombre-pantalla].locators.js` en kebab-case.

### Plantilla

```javascript
// Localizadores de: [Nombre de la pantalla]
// Ruta de la aplicacion: [ruta o URL]
// Generado por: UI Mapper Copilot
// Selectores ordenados por jerarquia de robustez (Nivel 1 = maxima estabilidad)

const LOCATORS = {

  // [Nombre del elemento en espanol]
  // Nivel: [1-8] | Atributo: [tipo de atributo usado]
  // Fallback: [selector de fallback si el primario falla]
  [NOMBRE_CONSTANTE]: '[selector-primario]',

};

module.exports = { LOCATORS };
```

### Ejemplo generado (pantalla Login)

```javascript
// Localizadores de: Login
// Ruta de la aplicacion: /login
// Generado por: UI Mapper Copilot

const LOCATORS = {

  // Campo de nombre de usuario
  // Nivel: 1 | Atributo: data-testid
  // Fallback: [name="username"]
  USERNAME_INPUT: '[data-testid="login-input-username"]',

  // Campo de contrasena
  // Nivel: 1 | Atributo: data-testid
  // Fallback: [name="password"]
  PASSWORD_INPUT: '[data-testid="login-input-password"]',

  // Boton de envio del formulario
  // Nivel: 1 | Atributo: data-testid
  // Fallback: button[type="submit"]
  SUBMIT_BUTTON: '[data-testid="login-btn-submit"]',

  // Enlace a recuperacion de contrasena
  // Nivel: 5 | Atributo: role + texto visible
  // ADVERTENCIA: Fragil si el texto cambia con i18n
  // Fallback: a[href="/forgot-password"]
  FORGOT_PASSWORD_LINK: 'a[href="/forgot-password"]',

  // Mensaje de error de autenticacion
  // Nivel: 6 | Atributo: clase CSS funcional
  // ADVERTENCIA: Puede ser fragil si se cambia la clase
  // Recomendacion: Agregar data-testid="login-error-message"
  ERROR_MESSAGE: '.login-error-message',

};

module.exports = { LOCATORS };
```

---

## 4. PLANTILLA PAGE OBJECT PARA CYPRESS (JavaScript)

### Convencion de nombres de fichero

`[NombrePantalla]Page.cy.js` en PascalCase.

### Plantilla

```javascript
// Pagina: [Nombre de la pantalla]
// Ruta de la aplicacion: [ruta]
// Generado por: UI Mapper Copilot

import { LOCATORS } from '../locators/[nombre-pantalla].locators';

const [NombrePantalla]Page = {

  visitar() {
    cy.visit('[ruta]');
  },

  get[NombreElemento]() {
    return cy.get(LOCATORS.[NOMBRE_CONSTANTE]);
  },

  [accionDescriptiva]([parametro]) {
    this.get[NombreElemento]().type([parametro]);
  },

};

export { [NombrePantalla]Page };
```

---

## 5. LOCATOR FILE PARA APPIUM (JSON)

### Convencion de nombres de fichero

`[nombre-pantalla].locators.json` en kebab-case.

### Plantilla JSON

```json
{
  "screen": "[Nombre de la pantalla]",
  "platform": "android | ios | web",
  "route": "[ruta o actividad]",
  "elements": [
    {
      "name": "[nombre-descriptivo-del-elemento]",
      "description": "[descripcion funcional en espanol]",
      "initial_state": "enabled | disabled | hidden",
      "enabled_condition": "[null si siempre activo | descripcion de la condicion de habilitacion]",
      "selectors": {
        "primary": {
          "strategy": "[accessibility_id | id | xpath | class_chain | predicate_string]",
          "value": "[valor del selector]",
          "robustness_level": [1-8]
        },
        "fallback": {
          "strategy": "[estrategia alternativa]",
          "value": "[valor alternativo]",
          "robustness_level": [1-8]
        },
        "absolute_fallback": {
          "strategy": "xpath",
          "value": "[XPath absoluto generado como ultimo recurso]",
          "robustness_level": 8,
          "x_ratio": "[coordenada X normalizada 0.0-1.0 relativa al ancho de pantalla]",
          "y_ratio": "[coordenada Y normalizada 0.0-1.0 relativa al alto de pantalla]",
          "warning": "FRAGIL: Coordenadas absolutas invalidas si cambia resolucion o layout"
        }
      },
      "fragile": false,
      "recommendation": "[null o texto de recomendacion si es fragil]"
    }
  ]
}
```

---

## 6. MAPA UI COMPLETO EN JSON

### Convencion de nombres de fichero

`ui-map.json` en la raiz de la carpeta del proyecto.

### Estructura JSON

```json
{
  "app": {
    "name": "[nombre de la aplicacion]",
    "framework": "[framework detectado]",
    "version": "[version]",
    "analysis_mode": "static | dynamic",
    "analysis_date": "[fecha ISO]",
    "testing_target": "[playwright | cypress | appium | selenium]"
  },
  "screens": [
    {
      "id": "[nombre-pantalla-kebab-case]",
      "name": "[nombre descriptivo en el idioma de la app]",
      "route": "[ruta o URL]",
      "classification": "simple | complex | module",
      "parent_screen": "[id de la pantalla padre o null]",
      "elements": [
        {
          "id": "[identificador-elemento-kebab-case]",
          "description": "[descripcion funcional]",
          "type": "input | button | link | select | checkbox | radio | toggle | textarea | custom",
          "selector_primary": {
            "value": "[selector]",
            "robustness_level": [1-8],
            "attribute_type": "[data-testid | id | name | aria-label | role | css | xpath-contextual | xpath-absolute]"
          },
          "selector_fallback": [
            {
              "value": "[selector alternativo]",
              "robustness_level": [1-8]
            }
          ],
          "fragile": false,
          "recommendation": null
        }
      ],
      "artifacts_generated": {
        "page_object": "[ruta relativa al fichero]",
        "locators_file": "[ruta relativa al fichero]"
      }
    }
  ],
  "summary": {
    "total_screens": 0,
    "total_elements": 0,
    "fragile_selectors": 0,
    "recommendations_count": 0,
    "coverage_by_level": {
      "level_1": 0,
      "level_2": 0,
      "level_3": 0,
      "level_4": 0,
      "level_5": 0,
      "level_6": 0,
      "level_7": 0,
      "level_8": 0
    }
  }
}
```

---

## 7. INFORME DE RECOMENDACIONES (Markdown)

### Convencion de nombres de fichero

`recommendations.md` en la raiz de la carpeta del proyecto.

### Estructura del informe

```markdown
# Informe de Selectores Fragiles y Recomendaciones

**Aplicacion**: [nombre]
**Fecha de analisis**: [fecha]
**Total de elementos analizados**: [numero]
**Total de selectores fragiles**: [numero]

---

## Resumen Ejecutivo

[Evaluacion general de la testability de la aplicacion: porcentaje de elementos con selectores
estables, principales problemas detectados, impacto en el mantenimiento de las pruebas.]

---

## Selectores Fragiles Detectados

### [Nombre de la Pantalla]

| Elemento | Selector Actual | Motivo de Fragilidad | Recomendacion |
|----------|----------------|---------------------|---------------|
| [descripcion] | [selector] | [motivo] | Agregar `data-testid="[valor]"` |

---

## Guia de Implementacion para el Equipo de Desarrollo

### Como agregar atributos de testing

[Instrucciones especificas segun el framework del proyecto]

### Convencion de nombres adoptada

Formato: `[pantalla]-[tipo]-[descripcion]`
Ejemplos aplicados en este proyecto: [lista de ejemplos reales del proyecto]

---

## Metricas de Testability

| Nivel de Robustez | Elementos | Porcentaje |
|-------------------|-----------|------------|
| Nivel 1 (data-testid, testID) | 0 | 0% |
| Nivel 2 (id semantico) | 0 | 0% |
| Nivel 3 (name) | 0 | 0% |
| Nivel 4 (aria-label) | 0 | 0% |
| Nivel 5 (role + texto) | 0 | 0% |
| Nivel 6 (CSS funcional) | 0 | 0% |
| Nivel 7 (XPath contextual) | 0 | 0% |
| Nivel 8 (XPath absoluto) | 0 | 0% |
| **Total** | **0** | **100%** |
```

---

## 8. CONVENCION DE NOMENCLATURA DE CONSTANTES

### Para locator constants (JavaScript)

Formato: `[PANTALLA]_[TIPO]_[DESCRIPCION]` en UPPER_SNAKE_CASE

| Tipo | Sufijo | Ejemplo |
|------|--------|---------|
| Input | `INPUT` | `LOGIN_INPUT_USERNAME` |
| Button | `BTN` | `LOGIN_BTN_SUBMIT` |
| Link | `LINK` | `LOGIN_LINK_FORGOT_PASSWORD` |
| Select/Dropdown | `SELECT` | `PROFILE_SELECT_COUNTRY` |
| Checkbox | `CHK` | `SETTINGS_CHK_NOTIFICATIONS` |
| Radio | `RADIO` | `PAYMENT_RADIO_CREDIT_CARD` |
| Toggle | `TOGGLE` | `SETTINGS_TOGGLE_DARK_MODE` |
| Textarea | `TEXTAREA` | `SUPPORT_TEXTAREA_MESSAGE` |
| Label/Text | `LABEL` | `LOGIN_LABEL_ERROR` |
| Container | `CONTAINER` | `PRODUCTS_CONTAINER_LIST` |
| Item (patron) | `ITEM` | `PRODUCTS_ITEM_ROW` |

### Para nombres de metodos en Page Objects

Formato: [verbo][Nombre] en camelCase

| Accion | Verbo | Ejemplo |
|--------|-------|---------|
| Rellenar un campo | `introducir` | `introducirUsuario(valor)` |
| Hacer click | `click` | `clickSubmit()` |
| Seleccionar opcion | `seleccionar` | `seleccionarPais(pais)` |
| Marcar checkbox | `marcar` | `marcarTerminos()` |
| Verificar visibilidad | `verificar` | `verificarErrorVisible()` |
| Obtener texto | `obtener` | `obtenerMensajeError()` |
| Esperar elemento | `esperar` | `esperarCargaCompleta()` |
| Navegar a pantalla | `irA` | `irARecuperarPassword()` |

