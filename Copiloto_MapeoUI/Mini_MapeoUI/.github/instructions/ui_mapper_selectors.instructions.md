---
applyTo: "**"
description: "Robustness-hierarchy+selectors-prioritization-for-UI-elements.Apply-in-Step-3(extraction)+Step-4(normalization)-of-UI-Mapper-flow."
---
# Selectors-Instructions+Robustness-Hierarchy

## Objective

Define-hierarchy-of-selector-evaluation+prioritization-for-interface-elements.Agent-must-apply-these-rules-systematically-in-Step-3(Selectors-Extraction)+Step-4(Normalization).

---

## 1. SELECTOR-ROBUSTNESS-HIERARCHY

Selectors-evaluated-in-this-strict-order.First-available+valid-selector-at-highest-hierarchy-level-becomes-primary-selector.

### Level-1-Maximum-stability:Dedicated-Testing-Attributes

**Criterion**:Element-has-attribute-explicitly-defined-for-testing.

|Attribute|Ecosystems|Example|
|----------|------------|---------|
|`data-testid`|React,Angular,Vue,generic-HTML|`[data-testid="login-submit-button"]`|
|`data-cy`|Cypress,any-framework|`[data-cy="username-input"]`|
|`data-test`|Generic-variant|`[data-test="password-field"]`|
|`testID`|React-Native(native-prop)|Not-CSS;used-as-direct-prop|
|`Key(value)`|Flutter|Not-CSS;Key-value-used|
|`accessibilityIdentifier`|Native-iOS|Not-CSS;only-Appium|

Validity-condition:Attribute-value-is-descriptive(not-numeric-or-auto-generated).

Valid-values-EXAMPLES:`"login-submit-btn"`,`"user-email-input"`,`"nav-home-link"`
Invalid-values-EXAMPLES:`"btn-1234"`,`"auto-generated-abc9f"`,`"12345"`

### Level-2-High-stability:Semantic-ID

**Criterion**:Element-has-`id`-attribute-with-descriptive+non-dynamic-value.

Validity-conditions:
-Value-doesn't-contain-generated-sequential-numbers(e.g:`input-3f8a`,`field__1`,`react-12`)
-Value-describes-element-function(e.g:`username`,`email-field`,`submit-btn`)
-ID-doesn't-repeat-in-same-document
-Not-auto-generated-by-UI-framework(Material-UI,PrimeNG,etc.)

Auto-generated-IDs-signatures(INVALID):
-Contain-hashes:`mat-input-4`,`p-inputtext-5`,`ng-select-1`
-Start-with-framework-name:`react-select-`,`ng-`,`mat-`
-Purely-numeric-or-alphanumeric-without-semantics

Syntax:`#username`,`#submit-btn`,`#email-field`

### Level-3-High-stability:Name-attribute-in-forms

**Criterion**:Form-element-has-`name`-attribute-with-descriptive-value.

Valid-only-for:`<input>`,`<select>`,`<textarea>`,`<button-type="submit">`

Validity-conditions:
-Value-is-semantic+describes-field(e.g:`username`,`password`,`country`)
-Not-dynamically-generated-by-form-builder
-Matches-field-name-in-data-model

Playwright-syntax:`[name="username"]`
Appium-syntax:`android.widget.EditText`-with-filter-by-`content-desc`

### Level-4-High-stability:ARIA-attributes

**Criterion**:Element-has-semantic-accessibility-attributes.

|Attribute|Use|Example|
|----------|-----|---------|
|`aria-label`|Describes-element-without-visible-text|`[aria-label="Cerrar-sesion"]`|
|`aria-labelledby`|References-another-element-labeling-it|Use-referenced-label-text|
|`role`-with-text|Element-with-explicit-ARIA-role|`[role="button"][aria-label="Guardar"]`|

Validity-conditions:
-`aria-label`-value-is-descriptive+in-app-language
-Value-won't-change-with-language-changes-if-app-has-i18n(consider-level-5-as-alternative)

### Level-5-Medium-High-stability:Role+visible-text-combination

**Criterion**:Element-has-implicit-or-explicit-role-combined-with-stable-visible-text.

Valid-when:Levels-1-4-not-available+element-text-is-fixed(not-dynamic).

Playwright-syntax:`page.getByRole('button',{-name:'Iniciar-sesion'-})`
Cypress-syntax:`cy.contains('button','Iniciar-sesion')`

Restrictions:
-Don't-use-if-text-is-dynamic(changes-per-app-state)
-Don't-use-if-app-has-multi-language-support(i18n)+text-changes
-Only-applicable-to-elements-with-semantic-roles:button,link,checkbox,radio,combobox,textbox

### Level-6-Medium-stability:Functional-CSS-class

**Criterion**:Element-has-CSS-class-whose-name-describes-its-function,not-appearance.

Strict-validity-conditions:
-Class-describes-element-function:`.btn-submit`,`.nav-logo`,`.user-menu-toggle`
-Class-DOESN'T-describe-appearance:DON'T-use-`.text-red`,`.mt-4`,`.flex`,`.p-2`
-Class-is-NOT-generic-UI-framework-class:DON'T-use-`.btn`,`.form-control`,`.input`
-Class-is-unique-in-screen-context-or-combined-with-another-stable-selector

Syntax:`.btn-login-submit`,`form.login-form-.btn-submit`

### Level-7-Medium-Low-stability:Contextual-XPath

**Criterion**:No-identifiers-in-higher-levels-available,but-DOM-structure-is-stable.

Contextual-XPath-accepts:
-Relative-paths-to-parent-container-with-ID-or-data-testid:`//form[@id="login-form"]//button[@type="submit"]`
-Using-text:`//button[text()="Guardar"]`(only-if-text-is-fixed)
-Attribute+position-combination-relative-to-immediate-parent

Contextual-XPath-rejects:
-Paths-based-on-absolute-position:`//div[3]/div[1]/button[2]`
-Paths-with->5-depth-levels
-Paths-including-layout-classes(grid,flex,container)

### Level-8-Minimum-stability:Absolute-XPath

**Criterion**:Last-resort.Generated-only-as-documented-fallback+marked-as-FRAGILE.

Always-accompanied-by:
-Fragility-warning
-Recommendation-to-dev-team-to-add-testing-attribute

## 2. SEMANTIC-IDENTIFIER-VALIDATION-BEFORE-ASSIGNING-LEVEL

Before-assigning-robustness-level,apply-these-validations-on-identifier-value:

### Semantic-validation-table

|Value-pattern|Classification|Action|
|-----------------|--------------|--------|
|Length-≤-4-characters(e.g:`ico`,`btn`,`lbl`)|Generic|Reduce-to-level-7,mark-FRAGILE|
|`0_resource_name_obfuscated`|Obfuscated|Discard,use-next-level|
|Matches-`/^(android\|com\.android)/`|System|Ignore-completely|
|Matches-`/^(mat-\|ng-\|p-\|react-select-)[0-9]/`|Framework-generated|Invalid-for-level-1-2|
|Descriptive-value-≥-5-chars-without-hash-numbers|Semantic|Valid-level-per-type|
|Functional-prefix+descriptive-name(e.g:`btnLogin`,`tfEmail`)|Semantic|Valid-level-2|

### Application-in-Android/Appium-mode

For-`resource-id`-in-Android-apps:
-Typical-valid-format:`es.mma.app/btnLogin`-or-simply-`btnLogin`
-**Genericity-criterion:**if-part-after-`/`(or-complete-value)-has-≤-4-chars-or-doesn't-describe-function→level-7
-**Duplicity-criterion:**if-same-resource-id-appears-in-≥-2-already-processed-screens→escalate-recommendation-priority-to-HIGH+mark-in-global-registry

### Early-duplicate-detection(apply-in-Step-3,not-Step-4)

**BEFORE**-generating-screen-selectors-matrix:
1.Extract-all-resource-id/id-found-in-current-screen
2.Cross-with-**global-IDs-registry**-accumulated-in-session
3.For-each-detected-collision:
   -Mark-both-occurrences-as-`fragile:true`
   -Escalate-recommendation-to-HIGH-priority
   -Include-renaming-proposal-in-`recommendation`-field
   -Example:`tfEmail`(duplicated-in-Login+RecoverPassword)→propose-`tfLoginEmail`+`tfRecoverEmail`
4.Update-global-registry-with-current-screen-IDs
5.If-≥-3-collisions-detected-in-same-screen:emit-`ERROR_DUPLICATE_IDS`-from-messages-catalog

**Collision-criterion:**Same-identifier-value-in-≥-2-different-already-processed-screens-OR-in-current-screen-vs-any-previous-screen.

---

## 3. PRIMARY+FALLBACK-SELECTOR-SELECTION-STRATEGY

For-each-element,agent-generates:

```
Primary-selector:   Highest-available-level-selector
Fallback-selector-1: Next-available-level
Fallback-selector-2: Optional,only-if-fallback-1-is-level-6-or-lower
```

### Application-example

Element:"Iniciar-sesion"-button-in-React-login-form

Available-analysis:
-`data-testid="login-submit-btn"`→Level-1-AVAILABLE
-`id="btn-login"`→Level-2,but-id-is-`btn-login`(might-be-valid)
-`type="submit"`→Not-semantic-selector
-Visible-text:"Iniciar-sesion"→Level-5-available

Result:
```
Primary-selector:   [data-testid="login-submit-btn"]     (Level-1)
Fallback-selector-1:#btn-login                           (Level-2)
Fallback-selector-2:button[type="submit"]                (Level-6-fragile,documented)
```

### Context-selector-for-duplicate-IDs(Android/Appium-mode)

When-`resource-id`-appears-in-multiple-screens,primary-selector-must-include-differentiating-container:

```
// Instead-of:id=tfEmail   (ambiguous-between-screens)
// Use:
//android.view.View[@resource-id='inputEmail']//android.widget.EditText[@resource-id='tfEmail']
// Parent-container(inputEmail,inputPassword,etc.)-is-different-per-screen→adds-context-without-absolute-XPath
```
