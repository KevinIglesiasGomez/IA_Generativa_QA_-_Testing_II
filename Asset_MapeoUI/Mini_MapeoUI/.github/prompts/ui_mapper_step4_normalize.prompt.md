---
agent: "ui_mapper"
tools: ["edit/editFiles", "read/readFile", "search"]
description: "Step-4:Identifiers-normalization-per-naming-convention(camelCase/SCREAMING_SNAKE_CASE),cross-screen-semantic-consistency-validation,collisions-resolution+final-normalized-selectors-registry-generation"
model: "Claude Sonnet 4.6"
---

# Step-4:Identifiers-Normalization

## 0. INTERNAL-COGNITIVE-ARCHITECTURE

### ROLE-A:Conventions-Auditor
**Objective:**Verify-all-IDs+constants-follow-agreed-convention.
-Apply-kebab-case+UPPER_SNAKE_CASE-format(reference:`ui_mapper_reference_tables.instructions.md`-section-3)|Detect-inconsistencies|Correct-provisional-IDs

### ROLE-B:Duplicates-Detector+Semantic-Consistency-Validator
**Objective:**Guarantee-no-repeated-IDs-or-semantic-inconsistencies-between-screens.
-Compare-with-accumulated-global-registry|Detect-name-collisions|Detect-equivalent-elements-with-divergent-nomenclature|Propose-unification

### ROLE-C:Completeness-Verifier
**Objective:**Confirm-registry-is-complete+without-gaps.
-Verify-all-elements-have-selector|Verify-fragile-selectors-have-recommendation|Verify-conditional-elements-have-annotated-condition

### ROLE-D:Global-Registry-Accumulator
**Objective:**Incorporate-registry-into-session-cumulative.
-Merge-with-global-registry|Update-coverage-statistics|Update-fragile-counter|Verify-pending-screens

---

## 1. PREREQUISITES

Step-3-must-be-completed-with:
-User-approved-selectors-matrix
-All-elements-with-defined-primary-selector+fallbacks
-Documented-fragile-selectors

---

## 2. STEP-INSTRUCTIONS

### Phase-1-Naming-convention-application

For-each-element,verify+correct-if-needed:

**Identifier-name(element-ID)**:
-Format:`[screen-name]-[type]-[description]`
-`screen-name`:screen-short-name-in-kebab-case(e.g:`login`,`user-profile`,`product-list`)
-`type`:per-Step-2-abbreviated-types-table
-`description`:brief-functional-description-in-kebab-case

Type-abbreviations-table:
|Full-type|Abbreviation|
|---------------|-------------|
|Text-input|`input`|
|Password-input|`input`|
|Button/Boton|`btn`|
|Link/Enlace|`link`|
|Select/Dropdown|`select`|
|Checkbox|`chk`|
|Radio-button|`radio`|
|Toggle/Switch|`toggle`|
|Textarea|`textarea`|
|Status-message|`label`|
|List-container|`container`|
|List-item(pattern)|`item`|
|Modal-trigger|`btn`(opens-it)|

**Constant-name(for-JavaScript-locator-file)**:
-Format:`[SCREEN]_[TYPE]_[DESCRIPTION]`
-Same-content-as-element-ID-but-in-UPPER_SNAKE_CASE
-Example:`login-btn-submit`→`LOGIN_BTN_SUBMIT`

### Phase-2-Cross-screen-semantic-consistency-validation

**Note:**Literal-duplicate-detection(identical-resource-id/id-collisions)-done-in-Step-3(Phase-0)-before-generating-selectors-matrix.In-this-Step-4-only-semantic-consistency-validation-executed.

**Semantic-consistency-validation(Step-2b):**

Detect-equivalent-elements-with-divergent-nomenclature-between-screens:

-**Case-1:Same-functional-element,different-names**
  -Detected-example:`login-btn-submit`(Login-screen)-vs-`auth-button-login`(Register-screen)
  -Action:Propose-unification-to-`[screen]-btn-submit`-in-both-screens

-**Case-2:Navigation-elements-with-inconsistent-patterns**
  -Example:`home-link-profile`-vs-`settings-profile-link`(inverted-order)
  -Action:Propose-consistent-pattern-`[screen]-link-[destination]`

-**Case-3:Inconsistent-abbreviations**
  -Example:`user-btn-delete`-vs-`products-button-remove`(btn-vs-button)
  -Action:Unify-to-abbreviation-agreed-in-reference-tables-section-3

If-semantic-inconsistencies-detected:
1.List-found-divergences
2.Propose-renaming-to-unify-pattern
3.Request-user-confirmation-before-applying-changes-to-global-registry

### Phase-3-Screen-normalized-registry-generation

Normalized-registry-is-definitive-version-to-be-used-in-Step-5-for-artifacts-generation.

Registry-structure:
```
Normalized-registry:[screen-name]

  [element-id]
    ID:              [screen-name]-[type]-[description]
    Constant:       [SCREEN_TYPE_DESCRIPTION]
    Type:            [full-type]
    Description:     [functional-description-in-Spanish]
    Primary-selector: [exact-selector]
    Primary-level:    [1-8]
    Fallback-selector: [fallback-selector]
    Fallback-level:    [1-8]
    Fragile:            [true|false]
    Condition:         [null|description-of-when-visible]
    Recommendation:     [null|recommendation-text-for-dev-team]
```

### Phase-4-Global-registry-update+continuation-decision

After-incorporating-screen-to-global-registry:
1.Show-global-status-summary(processed-vs-pending-screens)
2.If-pending-screens:propose-next-screen-for-Step-2-3-4-cycle
3.If-all-scope-screens-processed:propose-advancing-to-Step-5

---

## 3. EXPECTED-OUTPUT

### COMPLETE-EXAMPLE(continuation-of-Login-screen-from-Step-3)

**Input:**Step-3-selectors-matrix-with-6-validated-elements

**Step-4-output:**

```
## Normalized-Registry-Login

|Element-ID|Constant|Type|Primary-Selector|Level|Fallback-Selector|Fragile|Condition|
|-------------|-----------|------|------------------|-------|------------------|--------|-----------|
|login-input-username|LOGIN_INPUT_USERNAME|Text-input|[data-testid="login-input-username"]|1|[name="username"]|No|-|
|login-input-password|LOGIN_INPUT_PASSWORD|Password-input|[data-testid="login-input-password"]|1|[name="password"]|No|-|
|login-btn-submit|LOGIN_BTN_SUBMIT|Primary-button|[data-testid="login-btn-submit"]|1|button[type="submit"]|No|-|
|login-link-forgot-password|LOGIN_LINK_FORGOT_PASSWORD|Action-link|a[href="/forgot-password"]|6|//a[text()="Olvidaste..."]|Yes|-|
|login-label-error|LOGIN_LABEL_ERROR|Error-message|.login-error|6|[role="alert"]|Yes|Only-if-authentication-error|
|login-chk-remember|LOGIN_CHK_REMEMBER|Checkbox|#remember-me|2|[name="rememberMe"]|No|-|

### Recommendations-for-dev-team

|#|Element|Recommended-action|Suggested-code|
|---|---------|-------------------|----------------|
|1|login-link-forgot-password|Add-data-testid|`<a-data-testid="login-link-forgot-password"-...>`|
|2|login-label-error|Add-data-testid|`<div-data-testid="login-label-error"-...>`|

### Semantic-consistency-validation

**Comparison-with-previous-screens-from-global-registry:**(doesn't-apply,is-first-processed-screen)

### Global-registry-status

|Screen|Status|
|----------|--------|
|login|Completed|
|home|Pending|
|users-list|Pending|
|users-detail|Pending|
|users-edit|Pending|

**Completed-screens**:1-of-5
**Accumulated-fragile-selectors**:2

---

Confirm-normalized-registry.
Next-screen-to-process:**Home**(return-to-Step-2-with-this-screen).
Or-write-"Step-5"-if-you-want-to-generate-artifacts-with-screens-processed-so-far.
```

### FORMAT-FOR-YOUR-CURRENT-SCREEN

```
## Normalized-Registry-[Screen-Name]

|Element-ID|Constant|Type|Primary-Selector|Level|Fallback-Selector|Fragile|Condition|
|-------------|-----------|------|------------------|-------|------------------|--------|-----------|

---

## 4. PREREQUISITES-TO-ADVANCE-TO-STEP-5

-All-scope-screens-in-"Completed"-status-in-global-registry
-Or-user-decided-to-generate-partial-artifacts-with-already-processed-screens
-Global-registry-has-no-duplicate-IDs
-All-normalized-registries-approved
