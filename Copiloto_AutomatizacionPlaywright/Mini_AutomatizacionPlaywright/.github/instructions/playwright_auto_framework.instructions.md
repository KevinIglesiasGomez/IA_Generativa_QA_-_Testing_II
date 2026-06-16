---
description: Instrucciones de estructura del framework Playwright existente
applyTo: "**/*.js,**/package.json,**/*.feature,**/cucumber.config.js"
---

# Playwright Framework Structure

KEY-FEATURES(Existing-Framework):
-Playwright(e2e-multi-browser:chromium,firefox,webkit)
-Cucumber-JS(test-runner,main:.feature-files)
-JavaScript/Node.js(programming-lang)
-Page-Object-Model(POM,for=maintainability+reusability)
-Browser-Factory-Pattern(centralized-browser-management)
-SQL-dataset-management(via=AtDBConnector.js+QueryDeposit.js)
-CI/CD-integration(automated-exec)
-multi-env-support(via=env.local.js+env.test.js)

IMPORTANT:if-actual-workspace-framework!=described-here=>STOP-flow+review-with-engineer(validate=adapt-existing-framework|follow-these-instructions)

---

ARCHITECTURE+FRAMEWORK-STRUCTURE:

PROJECT-STRUCTURE:

```
framework-playwright/
├─cucumber.config.js  # main-Cucumber-config
├─playwright.config.js  # minimal-Playwright-config(NOT-executed)
├─package.json  # dependencies+npm-scripts
├─env.local.js  # local-env-config
├─env.test.js  # test-env-config
├─clean.js  # report-cleanup-script
├─/src/
│ ├─/features/  # BDD-Cucumber/Gherkin-files
│ │ ├─Login.feature  # auth-scenarios
│ │ ├─authentication.feature  # extended-auth-scenarios
│ │ └─[features-per-module...]  # features-per-functional-module
│ ├─/pages/  # Page-Object-Model-classes
│ │ ├─LoginPage.js  # POM-for-login-functionality
│ │ ├─MenuPage.js  # POM-for-main-menu-nav
│ │ └─/pagesLocators/  # separate-element-locators
│ │   ├─LoginPageLocators.js  # login-page-locators
│ │   └─MenuPageLocators.js  # main-menu-locators
│ ├─/steps/  # Cucumber-step-definitions
│ │ ├─common.steps.js  # common-steps+browser-lifecycle-management
│ │ ├─login.steps.js  # auth-steps
│ │ └─[funcionalidad].steps.js  # functionality-specific-steps
│ ├─/support/  # framework-support-files
│ │ ├─browserFactory.js  # Browser-Factory-Pattern(MANDATORY)
│ │ ├─environmentLoader.js  # env-config-loader
│ │ ├─commands.js  # reusable-custom-commands
│ │ └─reportGenerator.js  # HTML-report-generator
│ ├─/utils/  # utility-functions
│ │ ├─AtDBConnector.js  # MySQL-connector-for-tests
│ │ ├─CommonUtilities.js  # common-reusable-utilities
│ │ └─QueryDeposit.js  # SQL-query-repository
│ ├─/datas/  # data-classes-for-shared-context
│ │ ├─LoginData.js  # auth-data
│ │ └─UsuarioData.js  # user-data
│ ├─/models/  # data-models
│ │ └─Usuario.js  # system-user-model
│ └─/constantes/  # framework-constants
│   └─RolesConstantes.js  # user-role-constants
└─/reports/  # auto-generated-reports
  ├─/json/  # Cucumber-JSON-reports
  ├─/html/  # navigable-HTML-reports
  ├─/screenshots/  # failure-screenshots
  └─/videos/  # execution-videos
```

---

TEMPORAL-INSPECTION-SCRIPTS(Optional):

For-apps(no-source-code-access|complex-architectures:framesets,dynamic-SPAs)=>create-temp-inspection-scripts(in-project-root).These-scripts=use-Playwright(launch-browser,analyze-rendered-DOM,detect-frames,dynamic-elements,generate-precise-selectors).

WHEN-TO-USE:
-legacy-apps(framesets|iframes)
-JSP/Servlet-architectures(server-side-rendering)
-dynamically-generated-elements(JavaScript/AJAX)
-no-access-to-HTML/JSX-source-code
-need-to-verify-final-DOM-selectors

See-snippet:[snippet:inspeccion-dinamica](full-pattern)

---

DEPENDENCIES+TECHNOLOGIES:

MAIN-DEPENDENCIES(package.json):
-Playwright-1.41.2:multi-browser-web-automation-engine
-@cucumber/cucumber-10.3.1:BDD-framework-for-JavaScript
-mysql2-3.20.0:MySQL-database-connectivity
-dotenv-16.0.0:env-var-loading
-cross-env-7.0.3:cross-platform-env-vars
-cucumber-html-reporter-7.1.1:HTML-report-generation
-http-server-14.1.1:server-for-report-viewing

---

MULTI-ENV-CONFIG:

CONFIG-FILES:
-env.local.js:local-dev-env
-env.test.js:testing-env

PER-ENV-CONFIG-INCLUDES:
-baseUrl:app-base-URL
-username/password:test-credentials(from-process.env)
-browser:browser-type(chromium,firefox,webkit)
-headless:no-GUI-mode
-timeout/slowMo:wait-times
-screenshotOnFailure/videoOnFailure:evidence-capture
-workers/retries:parallelism+retries

---

ARCHITECTURE-PATTERN:

BROWSER-FACTORY(central-manager):
-browserFactory.js=manages-browser-instance-creation+closure
-methods:createBrowser(browserType,options),closeBrowser(browser,context)
-returns:{browser,context,page}(for-use-in-common.steps.js)
-multi-browser-support:chromium,firefox,webkit

PAGE-OBJECTS:
-receive-this.page(from-shared-context,via-constructor)
-define-locators(in-separate-*PageLocators.js-files)
-initialize-locators(in-initializeLocators()-method)
-functionality-specific-methods(per-Page-Object)
-failure-screenshots-captured-directly-from-PO(via-this.page.screenshot())

SHARED-CONTEXT(this):
-this.page:Playwright-page-instance(shared-across-all-Steps)
-this.browser:browser-instance(only-for-After-closure)
-this.context:browser-context(only-for-After-closure)
-this.baseUrl:app-base-URL
-this.config:active-env-complete-config
-this.scenarioName:executing-scenario-name

DATA-CLASSES(scenario-data):
-simple-JS-classes(NO-access-to-this.page)
-store-domain-data(generated|used-during-scenario)
-instantiated-in-Steps,passed-between-methods(when-needed)
-examples:LoginData,UsuarioData

CENTRALIZED-SQL-QUERIES:
-src/utils/QueryDeposit.js:reusable-SQL-query-repository
-src/utils/AtDBConnector.js:MySQL-database-connector
-NEVER-write-inline-SQL-queries(in-Steps|Page-Objects)
