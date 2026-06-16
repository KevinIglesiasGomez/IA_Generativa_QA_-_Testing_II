# Playwright-Tests-Instructions

## OBJECTIVE

Create-tests-using:
-Cucumber-as-main-test-runner-with-.feature-file-execution-in-Gherkin-syntax
-Playwright-for-e2e-functional-automation(used-by-Cucumber-step-definitions)
-JavaScript-as-programming-language+use-CommonJS
-Page-Object-Model(POM)-design-pattern-for-maintainability+reusability
-configure-Cucumber-to-relate-Gherkin-steps-with-Playwright-actions
-ALL-test-execution-via-Cucumber-commands(NOT-Playwright-directly)
-NO-generate-installation-scripts.All-required-via-native-commands+documented-in-README
-use-existing-env-variable-files-for-all-config+sensitive-info(URLs,credentials,timeouts)
-must-include-Cucumber-JSON-reports-after-each-execution
-must-be-easy-to-install+run-with-clear-Spanish-documentation
IMPORTANT:tests-execute-via-Cucumber-commands(cucumber-js)(NOT-playwright-commands)

## CUCUMBER-CONFIG

Use-existing-cucumber.config.js-that-must:
-load-env-config-using-same-pattern-as-Playwright-config
-NEVER-hardcode-env-specific-values
-set-paths-for-.feature-files+step-definitions
-enable-Cucumber-JSON-reporting-after-each-execution
-define-.feature-files+step-definitions-location
-generate-Cucumber-JSON-reports-in-/reports(subfolders-auto-created)
-add-timeout-to-cucumber.config.js(timeout:120000)
-allow-running-tests-filtered-by-@tags
-integrate-with-Playwright-test-lifecycle
-include-proper-error-handling-for-env-config-loading
-configure-Cucumber-as-main-test-runner→all-test-execution-flows-through-Cucumber-commands

## ANALYSIS-REQUIREMENTS

-read+analyze-ONLY-.feature-file-**{input:feature_name}**-completely-from-provided-BDD-project-folder→understand-all-scenarios-needing-implementation
-review-JSP/static-HTML-pages-available-in-provided-folder→get-info-about-app-structure,locators,behavior
-ALL-steps-described-in-Gherkin-BDD-feature-scenarios-must-be-implemented-as-.js-files-in-src/steps-folder-with-corresponding-Page-Objects

## ARCHITECTURE-INFO

Project-follows-structure:
-`src/features`:contains-cucumber-BDD-tests-from-provided-project-folder,copied-without-modification
-`src/pages`:contains-page-objects-for-tests-with-locator+action-methods,created-based-on-JSP/HTML-analysis
-`src/steps`:contains-step-definitions-for-tests,implementing-ALL-steps-from-analyzed-.feature-files
-`src/support`:contains-support-files-for-tests.MUST-include-browserFactory.js
-`src/utils`:contains-utility-functions-for-tests.Example:dataGenerator.js
-`fixtures`:contains-test-fixtures

## BROWSER-FACTORY-PATTERN(MANDATORY-FOR-ALL-TESTS)

CRITICAL:all-test-implementations-MUST-use-existing-Browser-Factory-Pattern:

```javascript
// Use existing browserFactory.js in src/support/
const BrowserFactory=require('../support/browserFactory');

// In step definitions:
Before(async function(){
  const browserName=BrowserFactory.getBrowserFromEnv();
  browser=await BrowserFactory.createBrowser(browserName,{
    headless:envConfig.HEADLESS,
    slowMo:envConfig.SLOW_MO
  });
  // ...rest of setup...
});
```

NEVER-create-direct-browser-instances→always-use-BrowserFactory.createBrowser()

## SECURITY-REQUIREMENTS

-NEVER-hardcode-sensitive-info-in-any-file-committed-to-version-control
-ALL-URLs,credentials,env-specific-data-must-use-env-variables
-provide-clear-documentation-about-how-to-configure-env-variables-securely

## TEST-EXECUTION-ARCHITECTURE

-Cucumber=main-test-runner→all-test-execution-flows-through-Cucumber-commands
-Playwright-used-internally-by-step-definitions-to-perform-browser-automation
-Browser-Factory-Pattern-centralizes-browser-management-for-multi-browser-support
-npm-scripts-must-use-cucumber-js-commands(NOT-playwright-commands)
-use-HEADLESS-false-to-always-see-test-execution-in-browser
-TEST-EXECUTION-EXAMPLES:
  *`npm run test`→`cucumber-js`(runs all features)
  *`npm run test:smoke`→`cucumber-js --tags @smoke`
  *`npm run test:feature`→`cucumber-js src/features/specific.feature`
  *`npx cucumber-js --name "Scenario name"`→run-specific-scenario
  
  MULTI-BROWSER-EXECUTION(AVAILABLE):
  *`npm run test:chrome`→run-tests-in-Chromium
  *`npm run test:firefox`→run-tests-in-Firefox
  *`npm run test:safari`→run-tests-in-WebKit/Safari
  *`npm run test:all-browsers`→run-tests-in-all-browsers-sequentially
  *`npm run test:browsers-parallel`→run-tests-in-all-browsers-in-parallel
  *`CICOSTOOLS_BROWSER=firefox npm run test`→run-with-specific-browser-via-env-variable

-step-definitions-connect-Gherkin-steps-with-Playwright-actions-inside-Page-Objects

## ENV-CONFIG
-NEVER-hardcode-sensitive-info-like-URLs,usernames,passwords,env-specific-data.Use-existing-env-config-files
-always-use-`process.env`-variables-with-sensible-defaults

## PLAYWRIGHT-CONFIG

-playwright.config.js-NOT-USED-by-framework-but-exists-to-prevent-dependency-errors:
  *file-has-NO-functional-purpose-in-test-execution-flow
  *all-browser-config-managed-via-browserFactory.js
  *NEVER-hardcode-values-in-playwright.config.js-as-it's-not-executed
  *env-config-handled-by-cucumber.config.js+browserFactory.js

-add-hook-config-in-'common.steps.js':
```javascript
const{Before,After,BeforeAll,AfterAll,setDefaultTimeout}=require('@cucumber/cucumber');
```

-MANDATORY:set-global-timeout-for-steps-in-'common.steps.js':
```javascript
setDefaultTimeout(120000);
```
-MANDATORY:install-@playwright/test-dependency-'npm install @playwright/test --save'-if-not-already-installed
-MANDATORY:install-cucumber-html-reporter-package-'npm install cucumber-html-reporter --save'-if-not-already-installed

## REPORTS

After-execution→generate:
-Cucumber-JSON-report-in-/reports/json/(auto-created-if-not-exists)
-HTML-report-generated-from-JSON-in-/reports/html/(auto-created-if-not-exists)
-add-npm-scripts-for-report-generation
NOTE:all-reports-generated-by-Cucumber-execution(NOT-Playwright-directly).Subfolders-auto-created-during-report-generation

## PENDING-SCENARIOS-MANAGEMENT

-MANDATORY:tag-non-implemented-scenarios-with-`@pendiente`-at-individual-scenario-level
-NEVER-use-`@pendiente`-only-at-Feature-level→must-apply-to-each-scenario-individually
-scenarios-marked-with-`@pendiente`-appear-as-"pending"-in-reports-instead-of-"undefined"
-CORRECT-PATTERN-for-pending-scenarios:
  ```gherkin
  @smoke @feature-tag @pendiente
  Escenario: Scenario name
    Dado que...
  ```
-scenarios-with-`@pendiente`-execute-but-skip-real-implementation→show-"pending"-status-in-reports
-ADVANTAGES-of-using-`@pendiente`:
  *clear-differentiation-between-non-implemented-scenarios(pending)-vs-implementation-errors(undefined)
  *allows-tracking-planned-vs-implemented-test-coverage
  *reports-clearly-show-each-scenario-status

## LANGUAGE-REQUIREMENTS

-all-documentation,README-files,comments,user-facing-text-written-in-Spanish
-code-comments-in-Spanish
-variable+function-names-can-remain-in-English-for-technical-clarity

## BEST-PRACTICES-TO-APPLY

-never-hardcode-URLs,credentials,env-variables-in-any-config-file
-always-use-env-variables-with-`process.env`+provide-sensible-defaults
-include-`dotenv`-package-to-load-env-variables-from-.env-files
-MANDATORY:use-existing-Browser-Factory-Pattern→never-create-direct-browser-instances
-MANDATORY:leverage-multi-browser-capabilities→use-provided-npm-scripts-for-cross-browser-tests
-MANDATORY:tag-non-implemented-scenarios-with-`@pending`-at-individual-scenario-level
-analyze-previous-Pages(src/pages)+step-definitions(src/steps)-for-reusable-code
-analyze-existing-browserFactory.js-for-consistent-browser-management-patterns
-use-constants-for-locators-within-Page-Objects
-group-reusable-actions-in-helper-functions-in-/support
-keep-step-definitions-simple→all-logic-in-Page-Objects
-maintain-consistent-naming-conventions
-analyze-existing-JSP/HTML-files-to-identify-correct-locators+understand-app-flow
-create-Page-Objects-accurately-reflecting-app-structure-based-on-JSP-analysis
-implement-ALL-Gherkin-steps-found-in-provided-.feature-file-**{input:feature_name}**
-IF-scenario-cannot-be-fully-implemented→mark-with-individual-`@pending`-for-correct-tracking

## BROWSER-MANAGEMENT-RULES(CRITICAL)

NEVER-do-this:
```javascript
// ❌ WRONG - Direct browser creation
const browser=await chromium.launch();
```

ALWAYS-do-this:
```javascript
// ✅ CORRECT - Use Browser Factory
const BrowserFactory=require('../support/browserFactory');
const browser=await BrowserFactory.createBrowser();
```

## IMPLEMENTATION-GUIDES

-use-these-Playwright-test-instructions-to-implement-tests-in-existing-**${input:playwright_folder}**-folder
-implement-all-generated-code-exclusively-within-new-folder
-store-all-outputs+generated-test-files-in-that-folder
-use-provided-.feature-file-without-modifications
-analyze-JSP/HTML-files-to-understand-app-structure+create-accurate-Page-Objects
-implement-step-definitions-for-each-Gherkin-step-found-in-**{input:feature_name}**-.feature-file

## OUTPUT-REQUIREMENT

When-requested→always:

-analyze-provided-.feature-file-called-**{input:feature_name}**-to-fully-understand-test-requirements-scope
-review-JSP/HTML-files-to-understand-app-structure+identify-accurate-locators
-implement-Page-Objects-based-on-JSP/HTML-analysis-with-accurate-locators+actions
-create-step-definitions-for-each-Gherkin-step-found-in-.feature-file
-configure-package.json-scripts-to-use-Cucumber-commands(cucumber-js)-for-test-execution
-ensure-npm-install&&npm-run-test-works-using-Cucumber-as-test-runner
-write-all-documentation+comments-in-Spanish
-emphasize-in-documentation-tests-execute-via-Cucumber(NOT-Playwright-directly)

## OBJECTIVE

Produce-high-quality+maintainable-Playwright-test-scripts-that:

-implement-ALL-Gherkin-scenarios-provided-in-.feature-files
-adhere-to-Page-Object-Model-design-pattern
-integrate-seamlessly-with-existing-Playwright-framework-structure
-correctly-automate-navigation+interactions-using-JSP/HTML-analysis-for-accurate-locators
