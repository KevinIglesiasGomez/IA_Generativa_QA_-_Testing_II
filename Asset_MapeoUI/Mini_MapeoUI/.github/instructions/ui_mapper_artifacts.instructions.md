---
applyTo: "ui-map/**"
description: "Templates,structures+conventions-for-testing-artifacts-generation-in-Step-5:Page-Objects(Playwright/Cypress/Selenium/Appium),locator-files(.locators.json),JSON-UI-maps+recommendations-reports."
---
# Testing-Artifacts-Generation-Instructions

## Objective

Define-templates+conventions-for-testing-artifacts-generation-in-Step-5.Defines-exact-formats-of-Page-Objects,locator-files,JSON-UI-maps+recommendations-reports.

---

## 1. OUTPUT-FOLDERS-STRUCTURE

All-artifacts-generated-in-`ui-map/`-folder-within-copilot-working-directory(not-in-analyzed-project).

```
ui-map/
|--[app-name]/
    |--pages/
        |--LoginPage.js              (Playwright-Page-Object)
        |--LoginPage.cy.js           (Cypress-Page-Object)
        |--LoginPage.java            (Selenium/Appium-Page-Object)
    |--locators/
        |--login.locators.js         (Playwright/Cypress-Locator-constants)
        |--login.locators.json       (Appium-Locator-file)
        |--login.locators.ts         (TypeScript-Locator-constants)
    |--ui-map.json                   (Complete-JSON-UI-map)
    |--recommendations.md           (Fragile-selectors-report)
```

---

## 2. PAGE-OBJECT-TEMPLATE-FOR-PLAYWRIGHT(JavaScript)

### File-naming-convention

`[ScreenName]Page.js`-in-PascalCase.
Examples:`LoginPage.js`,`UserProfilePage.js`,`ProductListPage.js`

### Template

```javascript
// Page:[Screen-name-in-app-language]
// App-route:[screen-route-or-URL]
// Generated-by:UI-Mapper-Copilot
// Date:[generation-date]

const-{-LOCATORS-}-=-require('../locators/[screen-name].locators');

class-[ScreenName]Page-{

  constructor(page)-{
    this.page-=-page;
  }

  // Screen-elements
  get-[elementName]()-{
    return-this.page.locator(LOCATORS.[CONSTANT_NAME]);
  }

  // Screen-actions
  async-[descriptiveAction]([parameters])-{
    // [action-description-in-Spanish]
    await-this.[elementName].fill([parameters]);
  }

  async-[descriptiveAction2]()-{
    // [action-description-in-Spanish]
    await-this.[elementName].click();
  }

  // Screen-verifications
  async-verify[State]()-{
    // [description-of-what-is-verified]
    return-this.[elementName].isVisible();
  }

}

module.exports-=-{-[ScreenName]Page-};
```

### Generated-example(Login-screen,React-app)

```javascript
// Page:Login
// App-route:/login
// Generated-by:UI-Mapper-Copilot

const-{-LOCATORS-}-=-require('../locators/login.locators');

class-LoginPage-{

  constructor(page)-{
    this.page-=-page;
  }

  // Screen-elements
  get-usernameInput()-{
    return-this.page.locator(LOCATORS.USERNAME_INPUT);
  }

  get-passwordInput()-{
    return-this.page.locator(LOCATORS.PASSWORD_INPUT);
  }

  get-submitButton()-{
    return-this.page.locator(LOCATORS.SUBMIT_BUTTON);
  }

  get-forgotPasswordLink()-{
    return-this.page.locator(LOCATORS.FORGOT_PASSWORD_LINK);
  }

  get-errorMessage()-{
    return-this.page.locator(LOCATORS.ERROR_MESSAGE);
  }

  // Screen-actions
  async-enterUsername(username)-{
    // Fills-username-field
    await-this.usernameInput.fill(username);
  }

  async-enterPassword(password)-{
    // Fills-password-field
    await-this.passwordInput.fill(password);
  }

  async-clickSubmit()-{
    // Clicks-login-button
    await-this.submitButton.click();
  }

  async-login(username,-password)-{
    // Complete-login-flow
    await-this.enterUsername(username);
    await-this.enterPassword(password);
    await-this.clickSubmit();
  }

  // Screen-verifications
  async-verifyErrorVisible()-{
    return-this.errorMessage.isVisible();
  }

  async-verifyErrorText()-{
    return-this.errorMessage.textContent();
  }
}

module.exports-=-{-LoginPage-};
```

---

## 3. LOCATOR-CONSTANTS-TEMPLATE-FOR-PLAYWRIGHT/CYPRESS(JavaScript)

### File-naming-convention

`[screen-name].locators.js`-in-kebab-case.

### Template

```javascript
// Locators-for:[Screen-name]
// App-route:[route-or-URL]
// Generated-by:UI-Mapper-Copilot
// Selectors-ordered-by-robustness-hierarchy(Level-1-=-maximum-stability)

const-LOCATORS-=-{

  // [Element-name-in-Spanish]
  // Level:[1-8]|Attribute:[attribute-type-used]
  // Fallback:[fallback-selector-if-primary-fails]
  [CONSTANT_NAME]:'[primary-selector]',

};

module.exports-=-{-LOCATORS-};
```

### Generated-example(Login-screen)

```javascript
// Locators-for:Login
// App-route:/login
// Generated-by:UI-Mapper-Copilot

const-LOCATORS-=-{

  // Username-field
  // Level:1|Attribute:data-testid
  // Fallback:[name="username"]
  USERNAME_INPUT:'[data-testid="login-input-username"]',

  // Password-field
  // Level:1|Attribute:data-testid
  // Fallback:[name="password"]
  PASSWORD_INPUT:'[data-testid="login-input-password"]',

  // Submit-button
  // Level:1|Attribute:data-testid
  // Fallback:button[type="submit"]
  SUBMIT_BUTTON:'[data-testid="login-btn-submit"]',

  // Forgot-password-link
  // Level:6|Attribute:CSS-functional
  // Fallback://a[text()="Forgot..."]
  // WARNING:Fragile-selector
  FORGOT_PASSWORD_LINK:'a[href="/forgot-password"]',

  // Error-message
  // Level:6|Attribute:CSS-class
  // Fallback:[role="alert"]
  // WARNING:Fragile-selector
  ERROR_MESSAGE:'.login-error',

  // Remember-me-checkbox
  // Level:2|Attribute:id
  // Fallback:[name="rememberMe"]
  REMEMBER_CHECKBOX:'#remember-me',

};

module.exports-=-{-LOCATORS-};
```

---

## 4. JSON-UI-MAP-TEMPLATE

### File-name

`ui-map.json`

### Structure

```json
{
  "app":{
    "name":"[app-name]",
    "framework":"[detected-framework]",
    "version":"[version-if-available]",
    "analysis-mode":"static|dynamic",
    "analysis-date":"[ISO-date]"
  },
  "screens":[
    {
      "id":"[screen-id-kebab-case]",
      "name":"[Screen-Name]",
      "route":"[route-or-URL]",
      "type":"page|modal|tab|wizard-step",
      "complexity":"simple|complex|module",
      "elements":[
        {
          "id":"[screen-type-description]",
          "constant":"[SCREEN_TYPE_DESCRIPTION]",
          "type":"[element-type]",
          "description":"[functional-description-Spanish]",
          "selector-primary":"[selector]",
          "selector-level":1-8,
          "selector-fallback":"[fallback-selector]",
          "fragile":true-false,
          "condition":"[visibility-condition-or-null]",
          "recommendation":"[dev-team-recommendation-or-null]"
        }
      ]
    }
  ],
  "summary":{
    "total-screens":0,
    "total-elements":0,
    "coverage-by-level":{
      "level-1":0,
      "level-2":0,
      "level-3":0,
      "level-4":0,
      "level-5":0,
      "level-6":0,
      "level-7":0,
      "level-8":0
    },
    "fragile-selectors":0,
    "testability-score":"[percentage]"
  }
}
```

---

## 5. RECOMMENDATIONS-REPORT-TEMPLATE

### File-name

`recommendations.md`

### Structure

```markdown
# Testability-Improvement-Recommendations-Report

**App**:[app-name]
**Framework**:[framework]
**Analysis-date**:[date]

## Executive-Summary

**Testability-score**:[X]%
**Fragile-selectors**:[N]-elements
**High-priority-recommendations**:[N]

---

## Prioritized-Fragile-Selectors

### Priority:HIGH(implement-immediately)

|#|Screen|Element|Current-Selector|Level|Recommendation|
|---|------|-------|---------------|-----|--------------|

### Priority:MEDIUM(implement-next-sprint)

|#|Screen|Element|Current-Selector|Level|Recommendation|
|---|------|-------|---------------|-----|--------------|

### Priority:LOW(continuous-improvement-backlog)

|#|Screen|Element|Current-Selector|Level|Recommendation|
|---|------|-------|---------------|-----|--------------|

---

## Implementation-Guide

### For-[Framework]-projects

1.[Step-by-step-instructions]
2.[Code-examples]
3.[Best-practices]

---

## Coverage-Metrics

|Level|Elements|%|
|-----|--------|--|
|Level-1(data-testid)|[N]|[%]|
|Level-2(semantic-id)|[N]|[%]|
|Level-6(CSS-functional)|[N]|[%]|
|**Fragile-total**|**[N]**|**[%]**|

---

## Adopted-Naming-Convention

[Convention-description-used-during-analysis]

---

## Post-Implementation-Integration-Checklist

### Step-1:Import-artifacts-in-testing-project

-[-]-Copy-`ui-map/[app]/pages/`-to-`[your-project]/tests/pages/`
-[-]-Copy-`ui-map/[app]/locators/`-to-`[your-project]/tests/locators/`
-[-]-Verify-import-paths-are-correct

### Step-2:Verify-version-compatibility

-[-]-Verify-[Playwright/Cypress/Selenium/Appium]-version-compatible
-[-]-Install-dependencies-if-needed:`npm-install`-or-equivalent
-[-]-Verify-Page-Objects-imports-work-without-errors

### Step-3:Run-initial-smoke-test

-[-]-Create-basic-test-importing-1-Page-Object
-[-]-Run-test-against-app-in-development
-[-]-Verify-selectors-find-elements-correctly
-[-]-If-fails:review-app-is-in-analyzed-version

### Step-4:Implement-priority-recommendations(HIGH)

-[-]-Share-`recommendations.md`-with-dev-team
-[-]-Create-issues/tasks-for-[X]-HIGH-priority-recommendations
-[-]-Assign-owner-to-each-task
-[-]-Estimate-implementation-effort

### Step-5:Re-analyze-to-measure-improvement

-[-]-After-implementing-HIGH-recommendations,re-run-UI-Mapper-on-same-project
-[-]-Compare-previous-vs-new-testability-score
-[-]-Goal:go-from-[X]%-to-85%+-testability
```
