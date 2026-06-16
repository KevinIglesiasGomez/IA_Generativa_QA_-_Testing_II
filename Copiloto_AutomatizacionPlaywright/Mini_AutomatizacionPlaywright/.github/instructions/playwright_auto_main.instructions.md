---
description: Patrones de configuración, ejecución e integración del framework Playwright existente
applyTo: "**/*.js,**/package.json,**/cucumber.config.js"
---

# Playwright Framework Config+Execution Patterns

TECHNOLOGY+LANGUAGE:
-lang:JavaScript/Node.js(NOT-Java,NOT-TypeScript)
-automation-engine:Playwright-1.41.2
-BDD-framework:Cucumber-JS-10.3.1
-package-manager:npm
-browser-management:Browser-Factory-Pattern(centralized-in-src/support/browserFactory.js)

ALL-test-execution=flows-through-npm/cucumber-js-commands(NEVER-direct-playwright-commands)

---

NPM-EXECUTION-COMMANDS:

```bash
npm run test  # all-tests
npm run test:smoke  # specific-tag
npm run test:regression
npm run test:dry-run  # validation-without-executing
npm run test:local  # by-env
npm run test:test
npm run test:chrome  # by-browser
npm run test:firefox
npm run test:webkit
npm run test:headed  # visible-mode(no-headless)
npx cucumber-js --config cucumber.config.js src/features/Login.feature  # specific-feature
npx cucumber-js --config cucumber.config.js --tags "@smoke"  # inline-tag
npm run report  # generate-HTML-report
```

---

MAIN-CUCUMBER-CONFIG(cucumber.config.js):

```javascript
module.exports={
  default:{
    features:['src/features/*.feature'],
    require:['src/steps/**/*.js','src/support/**/*.js'],
    format:['progress-bar',`json:reports/json/${reportName}.json`,`html:reports/html/${reportName}.html`],
    worldParameters:{
      environment:config.environment||'local',
      config:config,
      browser:process.env.BROWSER||config.browser||'chromium',
      headless:config.headless,
      baseUrl:config.baseUrl,
      screenshotOnFailure:true,
      videoOnFailure:false,
      timeout:config.timeout||30000,
      slowMo:config.slowMo||100
    },
    formatOptions:{snippetInterface:'async-await'},
    parallel:config.workers||1,
    retry:config.retries||0
  }
};
```

---

BROWSER-FACTORY-PATTERN(MANDATORY):

See-examples:.github/snippets/playwright_auto_code_snippets.md:[snippet:browser-factory],[snippet:common-steps]

KEY-RULE:ONLY-common.steps.js-manages-browser-lifecycle(Before/After).All-other-step-files-receive-page-via-shared-context-this.page

---

PAGE-MANAGEMENT(Page Objects):

See-example:.github/snippets/playwright_auto_code_snippets.md:[snippet:page-object-basico]

NEVER-create-Playwright-browser/page-instances(inside-Page-Objects|Steps!=common.steps.js)

---

MULTI-ENV-CONFIG(env.local.js/env.test.js):

Per-env-config-files(project-root):

```javascript
// env.local.js
module.exports={
  environment:'local',
  baseUrl:process.env.BASE_URL||"http://localhost:3000",
  username:process.env.APP_USERNAME||"usuario_por_defecto",
  password:process.env.APP_PASSWORD||"password_por_defecto",
  browser:process.env.BROWSER||"chromium",
  headless:process.env.HEADLESS==="true"||false,
  timeout:parseInt(process.env.TIMEOUT)||30000,
  slowMo:parseInt(process.env.SLOW_MO)||100
};
```

Code-access(via-worldParameters):

```javascript
// In Steps:this.config+this.baseUrl-available-from-common.steps.js
const username=this.config.username||process.env.APP_USERNAME;
const password=this.config.password||process.env.APP_PASSWORD;
```

NEVER-hardcode-URLs,credentials,env-data(directly-in-source-code)

---

PENDING-SCENARIO-MANAGEMENT:
-tag-non-implemented-scenarios-with-@pendiente(INDIVIDUAL-scenario-level)
-NEVER-use-@pendiente-only-at-Feature-level

```gherkin
@smoke @login @pendiente
Escenario: Login con usuario con cuenta bloqueada
  Dado que el usuario tiene la cuenta bloqueada
  Cuando intenta iniciar sesión
  Entonces el sistema muestra mensaje de cuenta bloqueada
```

---

REPORTS:

Auto-generated-in-reports/(after-each-exec):
-reports/json/cucumber-report-[timestamp].json  # Cucumber-JSON-report
-reports/html/cucumber-report-[timestamp].html  # navigable-HTML-report
-reports/screenshots/  # failure-screenshots
-reports/videos/  # execution-videos(if-enabled)

---

EXECUTION-TAGS:

Tag|Use
@smoke|smoke-tests,basic-validation
@regression|full-regression-suite
@critical|critical-business-tests
@pendiente|not-yet-implemented-scenarios
@debug|scenarios-with-additional-logging

---

SECURITY-REQUIREMENTS:
-NEVER-hardcode-URLs,credentials,passwords(in-source-code|version-control)
-ALWAYS-use-env-files(env.local.js,env.test.js,with-process.env)
-env-selection:via-process.env.ENV|cross-env ENV=local
-NEVER-include-.env-files-with-real-data(in-commits.Use-empty-templates|example-files)

---

CODE-CONVENTIONS:
-documentation,comments,log-msgs:Spanish
-class-names(Page Objects):PascalCase(English,e.g.LoginPage,MenuPage)
-method+variable-names:camelCase(English,e.g.fillUsername(),loginButton)
-constants+locators:UPPER_SNAKE_CASE(English,defined-in-*Locators.js-files,e.g.LOGIN_BUTTON='#loginBtn')
-Step-files:{funcionalidad}.steps.js
-Page-Object-files:{Funcionalidad}Page.js
-Locator-files:{Funcionalidad}PageLocators.js
-Data-files:{Funcionalidad}Data.js
