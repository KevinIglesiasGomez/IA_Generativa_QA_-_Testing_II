---
applyTo: "**"
description: "Framework-detection-tables,testing-tools-compatibility,naming-conventions+technical-mappings.Essential-for-Step-0(discovery)+Step-1(screens)."
---
# Consolidated-Reference-Tables-UI-Mapper

## Objective

Centralizes-all-framework-compatibility-tables,naming-conventions+technical-mappings-reused-in-multiple-copilot-steps.Prompts+other-instruction-files-reference-this-document-to-avoid-duplication.

---

## 1. FRAMEWORK-DETECTION-TABLE

### Static-Mode(source-code-analysis)

|Dependency-found-in-package.json/pubspec.yaml|Detected-framework|File-extensions|Where-to-search-routes|
|-----------------------------------------------------|---------------------|------------------------|-------------------|
|`react`,`react-dom`|React|`.jsx`,`.tsx`|`App.jsx`,routers,`Route`|
|`next`|Next.js(React)|`.jsx`,`.tsx`|`/pages/`,`/app/`,`createBrowserRouter`|
|`@angular/core`|Angular|`.html`(template)+`.ts`|`app-routing.module.ts`,`Routes[]`|
|`vue`|Vue.js|`.vue`(SFC)|`router/index.js`,`routes[]`|
|`@ionic/angular`-or-`@ionic/react`|Ionic|`.html`+`.ts`-or-`.jsx`|`app-routing.module.ts`|
|`react-native`|React-Native|`.tsx`-with-RN-components|`navigation/`,`Stack.Screen`|
|(pubspec.yaml-with-`flutter`)|Flutter|`.dart`|`GoRouter`,`MaterialApp-routes`|
|`nuxt`|Nuxt.js(Vue)|`.vue`|`/pages/`,`router/index.js`|

### Dynamic-Mode(DOM-inference)

|Pattern-detected-in-DOM|Inferred-framework|
|-------------------------|-------------------|
|Attributes-`ng-`,`data-ng-`|Angular|
|Script-`__NEXT_DATA__`|Next.js|
|Attribute-`data-reactroot`|React|
|Attribute-`data-v-`|Vue|
|No-recognizable-patterns|Generic-HTML|

---

## 2. TESTING-ATTRIBUTES-PER-FRAMEWORK

|Framework|Recommended-testing-attribute|Syntax-in-code|Alternative|
|-----------|---------------------------------|-------------------|-------------|
|React|`data-testid`|`<button-data-testid="login-btn-submit">`|`data-cy`,`data-test`|
|Angular|`data-testid`|`<button-data-testid="login-btn-submit">`|`id`,`#templateRef`|
|Vue|`data-testid`|`<button-data-testid="login-btn-submit">`|`data-cy`|
|React-Native|`testID`(native-prop)|`<Button-testID="login-btn-submit"-/>`|`accessibilityLabel`|
|Flutter|`Key(value)`|`Button(key:Key('login-btn-submit'))`|`Semantics(label:)`|
|Ionic|`data-testid`|`<ion-button-data-testid="login-btn-submit">`|`id`,ion-*-attributes|

---

## 3. IDENTIFIER-NAMING-CONVENTION

### Element-IDs-format(kebab-case)

**Format:**`[screen]-[type]-[description]`

**Examples:**
-`login-btn-submit`:submit-button-in-login-screen
-`profile-input-email`:email-field-in-profile-screen
-`home-link-dashboard`:dashboard-link-in-home-screen
-`products-select-category`:category-selector-in-products-screen

**Rules:**
-Only-lowercase+hyphens
-No-articles-or-prepositions
-Maximum-5-words
-Always-start-with-screen-name

### Locator-constants-format(UPPER_SNAKE_CASE)

**Format:**`[SCREEN]_[TYPE]_[DESCRIPTION]`

**Examples:**
-`LOGIN_BTN_SUBMIT`
-`PROFILE_INPUT_EMAIL`
-`HOME_LINK_DASHBOARD`

### Type-abbreviations-table

|Full-type|ID-abbreviation|Constant-suffix|
|---------------|---------------------|----------------------|
|Text-input|`input`|`INPUT`|
|Password-input|`input`|`INPUT`|
|Email-input|`input`|`INPUT`|
|Number-input|`input`|`INPUT`|
|Button/Boton|`btn`|`BTN`|
|Link/Enlace|`link`|`LINK`|
|Select/Dropdown|`select`|`SELECT`|
|Checkbox|`chk`|`CHK`|
|Radio-button|`radio`|`RADIO`|
|Toggle/Switch|`toggle`|`TOGGLE`|
|Textarea|`textarea`|`TEXTAREA`|
|Status-message|`label`|`LABEL`|
|List-container|`container`|`CONTAINER`|
|List-item(pattern)|`item`|`ITEM`|
|Modal-trigger|`btn`|`BTN`|

---

## 4. SELECTOR-SYNTAX-PER-TESTING-FRAMEWORK

### Playwright(JavaScript/TypeScript)

|Level|Selector-type|Syntax|
|-------|-----------------|----------|
|1|data-testid|`page.locator('[data-testid="login-btn-submit"]')`|
|2|id|`page.locator('#username')`|
|3|name|`page.locator('[name="username"]')`|
|4|aria-label|`page.locator('[aria-label="Cerrar-sesion"]')`|
|5|role+text|`page.getByRole('button',{-name:'Iniciar-sesion'-})`|
|6|Functional-CSS|`page.locator('.btn-login-submit')`|
|7|Contextual-XPath|`page.locator('//form[@id="login"]//button')`|

### Cypress(JavaScript)

|Level|Selector-type|Syntax|
|-------|-----------------|----------|
|1|data-testid|`cy.get('[data-testid="login-btn-submit"]')`|
|2|id|`cy.get('#username')`|
|3|name|`cy.get('[name="username"]')`|
|4|aria-label|`cy.get('[aria-label="Cerrar-sesion"]')`|
|5|role+text|`cy.contains('button','Iniciar-sesion')`|
|6|Functional-CSS|`cy.get('.btn-login-submit')`|
|7|Contextual-XPath|`cy.xpath('//form[@id="login"]//button')`|

### Appium(Android-UiSelector)

|Level|Selector-type|Syntax|
|-------|-----------------|----------|
|1|testID(content-desc)|`new-UiSelector().description("login-btn-submit")`|
|2|resource-id|`new-UiSelector().resourceId("com.app:id/username")`|
|3|Semantic-content-desc|`new-UiSelector().description("Campo-de-usuario")`|
|5|Visible-text|`new-UiSelector().text("Iniciar-sesion")`|

### Selenium(Java)

|Level|Selector-type|Syntax|
|-------|-----------------|----------|
|1|data-testid|`By.cssSelector("[data-testid='login-btn-submit']")`|
|2|id|`By.id("username")`|
|3|name|`By.name("username")`|
|4|aria-label|`By.cssSelector("[aria-label='Cerrar-sesion']")`|
|6|Functional-CSS|`By.className("btn-login-submit")`|
|7|XPath|`By.xpath("//form[@id='login']//button")`|

---

## 5. AUTOMATICALLY-DETECTED-FRAGILE-PATTERNS(REGEX)

```regex
# Auto-generated-IDs(reject-as-Level-2)
^(mat-|ng-|p-|react-select-|v-select-)[0-9]

# Utility-classes(reject-as-Level-6)
^(mt-|mb-|pt-|pb-|px-|py-|flex|grid|text-|bg-|border-)[a-z0-9]

# Generic-Bootstrap-classes(reject-as-Level-6)
^(col-|row|container|btn$|form-control$|card$)

# Positional-XPath(mark-as-fragile-in-Level-7-8)
\[\d+\]
```

---

## 6. SCREEN-COMPLEXITY-CLASSIFICATION

|Classification|Criterion|Flow-Impact|
|---------------|----------|---------------------|
|**Simple**|<10-interactive-elements,no-complex-forms|Processed-in-single-Steps-2-3-4-cycle|
|**Complex**|10-30-interactive-elements,forms-with-validations|May-require-subdivision-by-sections|
|**Module**|>30-elements-or-multiple-sub-views-within-same-route|Divided-into-sub-screens-before-processing|

### Automatic-subdivision-conditions

Screen-subdivided-automatically-if:
-Contains-tabs(tabs)-with-independent-contents(each-tab=sub-screen)
-Contains-multi-step-wizard/stepper(each-step=sub-screen)
-Contains-collapsible-sections-with->5-elements-each(each-section=sub-screen)

---

## 7. INTERACTIVE-ELEMENTS-TAXONOMY

### Form-Elements

|Type|Common-identifiers|Notes|
|------|------------------------|-------|
|Text-input|`<input-type="text">`,`TextField`,`TextInput`|Include-placeholders+associated-labels|
|Password-input|`<input-type="password">`,`PasswordField`|Note-if-has-visibility-toggle|
|Email-input|`<input-type="email">`||
|Number-input|`<input-type="number">`,`NumberInput`||
|Textarea|`<textarea>`,`TextArea`||
|Select/Dropdown|`<select>`,`Dropdown`,`Picker`|Catalog-options-if-static|
|Checkbox|`<input-type="checkbox">`,`Checkbox`||
|Radio-button|`<input-type="radio">`,`RadioButton`||
|Toggle/Switch|`<input-type="checkbox"-role="switch">`,`Switch`||
