---
agent: "ui_mapper"
tools: ["search", "read/readFile"]
description: "Step-3:Available-identifiers-evaluation-per-element,robustness-hierarchy-application(data-testid>ARIA>ID>class),selectors-matrix-construction-with-fallbacks+cross-screen-duplicate-detection"
model: "Claude Sonnet 4.6"
---

# Step-3:Selectors-Extraction+Prioritization

## 0. INTERNAL-COGNITIVE-ARCHITECTURE

### ROLE-A:Availability-Evaluator
**Objective:**Detect-all-available-identifiers-per-element.
-Review-Step-2-catalog-attributes|Determine-which-are-usable-as-selectors|Distinguish-static-vs-dynamic

### ROLE-B:Robustness-Classifier
**Objective:**Apply-8-level-hierarchy-from-`ui_mapper_selectors.instructions.md`.
-Evaluate-each-attribute-per-validity-criteria|Assign-robustness-level|Build-selectors-ranking

### ROLE-C:Selectors-Generator
**Objective:**Build-exact-syntax-for-target-testing-framework.
-Generate-correct-syntax(reference:`ui_mapper_reference_tables.instructions.md`-section-4)|Primary-selector+fallbacks

### ROLE-D:Fragility-Detector
**Objective:**Identify+document-problematic-selectors.
-Apply-fragile-patterns(reference-tables-section-5)|Mark-fragile-flag|Generate-recommendations

---

## 1. PREREQUISITES

Step-2-must-be-completed-with:
-User-approved-elements-catalog
-All-available-attributes-registered-per-element

---

## 2. STEP-INSTRUCTIONS

This-step-executes-for-same-screen-just-completed-Step-2.

### Phase-0-Global-IDs-Registry-Cross(execute-BEFORE-attributes-evaluation)

**Mandatory-before-generating-any-selector:**

1.Extract-all-identifiers(resource-id,id,data-testid,accessibilityLabel)-found-in-Step-2-catalog-for-current-screen
2.Compare-with-**global-IDs-registry**-accumulated-in-session(element-11-of-preserved-context)
3.For-each-detected-collision:
   -Mark-element-as-`fragile:true`-in-selectors-matrix
   -Escalate-recommendation-to-HIGH-priority
   -Include-in-`recommendation`-field-renaming-proposal-with-screen-prefix
   -Example:`tfEmail`(duplicated-in-Login+RecoverPassword)→propose-`tfLoginEmail`+`tfRecoverEmail`
4.Update-global-registry-with-current-screen-IDs(even-if-no-collisions)
5.If-≥-3-collisions-detected-in-same-screen:emit-`ERROR_DUPLICATE_IDS`-from-messages-catalog

**Collision-criterion:**Same-identifier-value-in-≥-2-different-already-processed-screens-OR-in-current-screen-vs-any-previous-screen.

### Phase-1-Attributes-evaluation-per-element

For-each-catalog-element,evaluate-in-order-following-attributes:

**Level-1-Verification**(data-testid,data-cy,data-test,testID,Key):
-Any-of-these-attributes-exists?
-Value-is-descriptive(not-numeric,not-hash,not-generated)?
-If-Yes+Yes:primary-selector-Level-1

**Level-2-Verification**(id):
-`id`-attribute-exists?
-Value-DOESN'T-match-generated-IDs-patterns?
-Value-describes-element-function?
-ID-is-unique-in-document?

**Level-3-Verification**(name-only-for-forms):
-Element-is-input,select,textarea-or-submit-button?
-`name`-attribute-exists?
-Value-is-semantic+not-generated?

**Level-4-Verification**(aria-label,aria-labelledby):
-`aria-label`-with-descriptive-value-exists?
-Or-`aria-labelledby`-referencing-element-with-clear-text-exists?

**Level-5-Verification**(role+visible-text):
-Element-has-semantic-role(button,link,checkbox,combobox,etc.)?
-Visible-text-is-stable(not-dynamic,not-i18n-dependent)?

**Level-6-Verification**(functional-CSS-class):
-At-least-one-CSS-class-whose-name-describes-element-function-exists?
-Class-is-NOT-utility-class(Tailwind,generic-Bootstrap)?
-Class-allows-uniquely-identifying-element-in-screen-context?

**Level-7-Verification**(contextual-XPath):
-Any-stable-attribute-in-direct-ancestor-allowing-XPath-anchoring-exists?
-Relative-XPath-has-<-5-depth-levels?

**Level-8-Verification**(absolute-XPath):
-Always-generated-as-last-fallback
-Automatically-marked-as-FRAGILE

### Phase-2-Selectors-matrix-construction

For-each-element,generate:

```
Primary-selector:    [highest-available+valid-level-selector]
Primary-level:       [1-8]
Fallback-selector-1:  [next-available-level]
Fallback-level-1:     [1-8]
Fallback-selector-2:  [only-if-fallback-1-is-level-6-or-lower]
Fragile:               [true/false]
```

### Phase-3-Syntax-generation-per-testing-framework

Apply-syntax-per-Step-0-confirmed-target-framework.

**Reference:**`ui_mapper_reference_tables.instructions.md`-section-4(Selector-syntax-per-framework)

---

## 3. EXPECTED-OUTPUT

### COMPLETE-EXAMPLE(continuation-of-Login-screen-from-Step-2-Playwright-framework)

**Input:**Step-2-elements-catalog-with-6-elements(login-input-username,login-input-password,etc.)

**Step-3-output:**

```
## Selectors-Matrix-Login

**Target-testing-framework**:Playwright

|#|Element|Primary-Selector|Level|Fallback-Selector-1|Level-F1|Fragile|Observation|
|---|----------|------------------|-------|---------------------|----------|--------|-------------|
|1|login-input-username|[data-testid="login-input-username"]|1|[name="username"]|3|No||
|2|login-input-password|[data-testid="login-input-password"]|1|[name="password"]|3|No||
|3|login-btn-submit|[data-testid="login-btn-submit"]|1|button[type="submit"]|6|No||
|4|login-link-forgot|a[href="/forgot-password"]|6|//a[text()="Olvidaste-tu-contrasena?"]|7|Yes|No-data-testid.See-recommendation-#1|
|5|login-label-error|.login-error|6|[role="alert"]|4|Yes|See-recommendation-#2|
|6|login-chk-remember|#remember-me|2|[name="rememberMe"]|3|No|Valid-semantic-ID|

### Detected-fragile-selectors

|#|Element|Reason|Recommendation|
|---|---------|--------|---------------|
|1|login-link-forgot|Only-available-via-href-or-visible-text.Text-may-change.|Add-`data-testid="login-link-forgot-password"`|
|2|login-label-error|CSS-class-fragile-ante-styles-refactors.|Add-`data-testid="login-label-error"`|

### Coverage-summary-by-level

|Level|Elements|%|
|-------|-----------|---|
|Level-1(data-testid)|3|50%|
|Level-2(semantic-id)|1|17%|
|Level-3(name)|0|0%|
|Level-4(aria)|0|0%|
|Level-6(functional-CSS)|2|33%|
|**Total-fragile**|**2**|**33%**|

---

Confirm-if-selectors-matrix-is-correct-to-advance-to-Step-4:Normalization.
```

### FORMAT-FOR-YOUR-CURRENT-SCREEN

```
## Selectors-Matrix-[Screen-Name]

**Target-testing-framework**:[playwright|cypress|appium|selenium]

|#|Element|Primary-Selector|Level|Fallback-Selector-1|Level-F1|Fragile|Observation|
|---|----------|------------------|-------|---------------------|----------|--------|-------------|

---

## 4. PREREQUISITES-TO-ADVANCE-TO-STEP-4

-User-approved-selectors-matrix
-All-elements-have-at-least-one-selector(even-if-Level-8)
-Fragile-selectors-documented-with-their-recommendations
-User-knows-elements-without-stable-identifiers
