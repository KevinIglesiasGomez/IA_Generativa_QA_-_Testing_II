# Playwright-Framework-Structure-Instructions

## 1. OVERVIEW+OBJECTIVES

### 1.1 Main-Objective
Create-ONLY-base-automated-test-framework-structure-using:

-Cucumber=main-test-runner-with-.feature-template-files
-Playwright-for-e2e-functional-automation(used-by-Cucumber-step-definitions)
-JavaScript-as-programming-language+use-CommonJS
-Page-Object-Model(POM)-design-pattern-for-maintainability+reusability
-Configure-Cucumber-to-relate-Gherkin-steps-with-Playwright-actions-but-NOT-specific-pages/steps
-ALL-test-execution-via-Cucumber-commands(NOT-Playwright-directly)
-NO-generate-installation-scripts.All-required-via-native-commands+documented-in-README

CRITICAL:generate-ONLY-UNIQUE-example-files.NO-create-real-tests,scenarios,app-specific-implementations-based-on-gherkin-features

## 2. CRITICAL-RESTRICTIONS

### 2.1 File+Content-Restrictions
-ONLY-unique-example-files:NO-create-real-tests,scenarios,app-specific-implementations
-specific-pages-FORBIDDEN:NO-create-LoginPage.js,HomePage.js,specific-page-classes
-specific-steps-FORBIDDEN:NO-create-LoginSteps.js,HomeSteps.js,specific-step-definition-files
-ONLY-generic-templates:create-ONE-ExamplePage.js+ONE-example.steps.js-as-templates
-NO-feature-analysis:copy-.feature-files-without-reading,analyzing,creating-implementations-based-on-them

### 2.2 Security-Restrictions
-NEVER-hardcode-sensitive-info:URLs,credentials,env-specific-data-in-config-files
-environment-variables-MANDATORY:all-sensitive-config-must-use-`process.env`-with-sensible-defaults
-add-.env-to-.gitignore:prevent-accidental-commits-of-sensitive-info

### 2.3 Execution-Restrictions
-Cucumber=ONLY-test-runner:all-execution-flows-through-Cucumber-commands(NOT-Playwright-directly)
-npm-scripts-with-cucumber-js:NO-use-playwright-commands-in-package.json
-Browser-Factory-Pattern-MANDATORY:centralized-browser-management-via-single-browserFactory.js-file(NOT-multiple-instances)

### 2.4 Implementation-Restrictions
-NO-installation-scripts:all-via-native-commands-documented-in-README
-Spanish-documentation-MANDATORY:README,comments,user-facing-text
-naming-conventions:CamelCase-for-page+step-files

## 3. ARCHITECTURE+STRUCTURE

### 3.1 Project-Structure
```
/project-root
├── /src
│   ├── /pages          # POM classes
│   │   └── ExamplePage.js
│   ├── /steps          # Cucumber step definitions
│   │   ├── common.steps.js      # Browser lifecycle (REQUIRED)
│   │   └── example.steps.js
│   ├── /support        # Test support files
│   │   ├── commands.js
│   │   ├── browserFactory.js    # Browser Factory (REQUIRED)
│   │   ├── environmentLoader.js # Env config loader (REQUIRED)
│   │   └── reportGenerator.js
│   ├── /utils
│   │   └── dataGenerator.js
│   └── /features       # BDD Gherkin .feature files
├── /reports
├── env.local.js
├── env.test.js
├── cucumber.config.js
├── playwright.config.js
├── package.json
├── .gitignore
└── README.md
```

### 3.2 Enhanced-Cucumber-Configuration
cucumber.config.js-MUST-implement:

KEY-REQUIREMENTS:
-modern-config-format:use-`module.exports={default:{...}}`-structure
-scalable-step-loading:use-`'src/steps/**/*.js'`-pattern→auto-load-ALL-step-definition-files
-support-file-integration:include-`'src/support/**/*.js'`→auto-load-support-files
-unique-report-generation:implement-timestamp-based-report-naming→prevent-overwrites
-enhanced-directory-structure:auto-create-directories-for-screenshots,videos,JSON+HTML-reports
-comprehensive-feedback:provide-detailed-config-info-during-initialization
-post-execution-reports:include-process.on('exit')-handler-with-report-location-info
-extended-worldParameters:include-comprehensive-config-sharing-with-step-definitions
-error-handling:include-try-catch-blocks-for-config-loading-with-appropriate-error-messages
-visual-config-feedback:provide-clear+friendly-console-output-with-config-status

TEMPLATE-STRUCTURE:
```javascript
const fs=require('fs');
const EnvironmentLoader=require('./src/support/environmentLoader');

let config;
try{
  config=EnvironmentLoader.getCurrentEnvironmentConfig();
  console.log(`Config loaded for environment: ${config.environment||'local'}`);
}catch(error){
  console.error('Error loading config:',error.message);
  process.exit(1);
}

const timestamp=new Date().toISOString().replace(/[:.]/g,'-');
const reportName=`cucumber-report-${timestamp}`;

module.exports={
  default:{
    features:['src/features/**/*.feature'],
    require:['src/steps/**/*.js','src/support/**/*.js'], // AUTO-LOAD
    format:[
      'progress-bar',
      `json:reports/json/${reportName}.json`,
      `html:reports/html/${reportName}.html`
    ],
    worldParameters:{
      environment:config.environment||'local',
      config:config,
      browser:process.env.BROWSER||config.browser,
      headless:process.env.HEADLESS==='true'||config.headless,
      baseUrl:config.baseUrl,
      screenshotOnFailure:config.screenshotOnFailure||true
    },
    formatOptions:{snippetInterface:'async-await'},
    parallel:config.workers||1,
    retry:config.retries||0,
    timeout:config.timeout||60000,
    tags:process.env.TAGS||'not @skip'
  }
};

const dirs=['reports','reports/json','reports/html','reports/screenshots','reports/videos'];
dirs.forEach(dir=>{
  if(!fs.existsSync(dir)){
    fs.mkdirSync(dir,{recursive:true});
    console.log(`Directory created: ${dir}`);
  }
});

process.on('exit',()=>{
  console.log('Execution completed');
  console.log(`Reports available at: reports/`);
});
```

CRITICAL:all-npm-scripts-must-reference-`cucumber.config.js`-using-`--config cucumber.config.js`-parameter

## 4. BROWSER-FACTORY-PATTERN(MANDATORY)

### 4.1 Overview
MANDATORY-for-centralized-browser-management.Prevents-multiple-browser-instances+ensures-consistent-browser-lifecycle-management-across-all-tests

### 4.2 Key-Components
-`src/support/browserFactory.js`:central-browser-factory-to-create+manage-browser-instances
-`src/steps/common.steps.js`:ONLY-file-responsible-for-browser-lifecycle-management(Before/After-hooks)
-shared-context(`this.page`):all-step-files-use-shared-page-instance(never-create-own-browsers)

### 4.3 Implementation-Rules
-ONLY-ONE-file-manages-browser-lifecycle:typically-`common.steps.js`-with-Before/After-hooks
-MANDATORY:must-include-in-`common.steps.js`-"setDefaultTimeout":
```javascript
const{Before,After,BeforeAll,AfterAll,Status,setDefaultTimeout}=require('@cucumber/cucumber');
setDefaultTimeout(120000); // MUST be 120000 (120 seconds)
```
-feature-specific-step-files-must-NOT-initialize-browsers:use-`this.page`-from-shared-context
-NO-duplicate-Before/After-hooks:only-one-set-of-browser-management-hooks-across-all-step-files
-Page-Objects-receive-`this.page`-parameter:from-shared-context(never-create-own-browser-instances)
-global-page-instances-scoped-per-step-file:initialized-with-`this.page`-when-needed

### 4.4 Multi-browser-Support-Requirements
-support-chromium,firefox,webkit:browser-selection-via-env-variable
-cross-browser-compatibility:all-Page-Objects-must-work-across-different-browser-types
-npm-scripts-per-browser:separate-commands-to-test-different-browsers

### 4.5 Browser-Factory-Structure
```javascript
class BrowserFactory{
  static async createBrowser(browserType='chromium'){
    // Browser creation logic with multi-browser support
  }
  static async closeBrowser(browser){
    // Clean browser closure logic
  }
}
```

### 4.6 Browser-Factory-Execution-Flow
1.test-starts:Cucumber-executes-Before-hook-in-`common.steps.js`
2.browser-creation:`common.steps.js`-calls-`BrowserFactory.createBrowser()`
3.browser-sharing:browser-instance-stored-in-shared-context(`this.page`)
4.step-execution:all-step-files-use-shared-`this.page`(never-create-browsers)
5.Page-Object-usage:Page-Objects-receive-`this.page`-parameter-from-step-files
6.test-finish:Cucumber-executes-After-hook-in-`common.steps.js`
7.browser-cleanup:`common.steps.js`-calls-`BrowserFactory.closeBrowser()`

CRITICAL:ONLY-`common.steps.js`-manages-browser-lifecycle.Feature-specific-step-files-use-ONLY-shared-context

### 4.7 Browser-Factory-Config-Integration
IMPORTANT:since-browser-management-centralized-via-Browser-Factory-Pattern:
-playwright.config.js-NOT-functionally-used→exists-ONLY-to-prevent-Playwright-dependency-errors
-browserFactory.js-manages-ALL→complete-browser-config,launch-options
-playwright.config.js-is-MINIMAL→only-basic-config-to-satisfy-dependencies
-multi-browser-support-via-env-variables→BROWSER=chromium|firefox|webkit-passed-to-browserFactory.js
-NO-complex-browser-launch-options-in-playwright.config.js→all-browser-specific-config-in-browserFactory.js
-keep-playwright.config.js-MINIMAL→only-basic-framework-configs(NOT-browser-management)

CRITICAL:playwright.config.js-NOT-executed-during-tests→all-config-via-Cucumber+Browser-Factory

## 5. TEST-EXECUTION-ARCHITECTURE

### 5.1 Execution-Flow-Hierarchy
1.Cucumber(Test-Runner)→main-entry-point-for-all-test-execution
2.Step-Definitions→translate-Gherkin-steps-into-JavaScript-actions
3.Page-Objects→encapsulate-browser-interactions-using-Playwright
4.Playwright→performs-actual-browser-automation(internal-use-only)

### 5.2 Clear-Responsibility-Separation
-Cucumber=ONLY-test-runner→ALL-execution-flows-through-Cucumber-commands(NEVER-Playwright-directly)
-Playwright-used-internally-by-step-definitions-through-Page-Objects-for-browser-automation
-npm-scripts-MUST-use-cucumber-js-commands(NEVER-playwright-commands)
-step-definitions-act-as-bridge-connecting-Gherkin-steps-with-Playwright-actions-inside-Page-Objects

### 5.3 Test-Execution-Command-Examples
```bash
# Basic
npm run test→cucumber-js (runs all features)
npm run test:smoke→cucumber-js --tags @smoke
npm run test:feature→cucumber-js src/features/specific.feature

# Multi-browser (MANDATORY support)
npm run test:chrome→BROWSER=chromium cucumber-js
npm run test:firefox→BROWSER=firefox cucumber-js
npm run test:webkit→BROWSER=webkit cucumber-js

# Environment-specific
npm run test:local→NODE_ENV=local cucumber-js
npm run test:staging→NODE_ENV=test cucumber-js
```

### 5.4 Execution-Flow-Sequence
1.user-executes-npm-command→calls-cucumber-js(NOT-playwright)
2.Cucumber-reads-.feature-files→parses-Gherkin-scenarios
3.Cucumber-executes-step-definitions→matches-Gherkin-steps-with-JavaScript-functions
4.step-definitions-call-Page-Objects→pass-shared-context-`this.page`
5.Page-Objects-use-Playwright→perform-browser-actions(click,type,navigate,etc)
6.Browser-Factory-manages-browser-lifecycle→creates/closes-browsers-centrally
7.Cucumber-generates-reports→JSON+HTML-reports(NOT-Playwright-reports)

## 6. CONFIG-MANAGEMENT

### 6.1 Environment-Config
Each-env-file(env.local.js,env.test.js)-must-export-config-using-env-variables

CRITICAL:`environmentLoader.js`-MANDATORY-for-centralized-env-config-management:
-location:`src/support/environmentLoader.js`
-purpose:provides-centralized-loading+validation-of-env-configs
-integration:must-be-used-by-cucumber.config.js+other-config-files
-error-handling:must-include-proper-error-handling-for-missing/invalid-configs
-multi-env-support:must-support-loading-different-env-files(env.local.js,env.test.js)

```javascript
// Standard config example (env.local.js, env.test.js)
module.exports={
  BASE_URL:process.env.BASE_URL||"https://...",
  USERNAME:process.env.USERNAME||"...",
  PASSWORD:process.env.PASSWORD||"...",
  HEADLESS:process.env.HEADLESS==="true"||false,
  BROWSER:process.env.BROWSER||"chromium",
  TIMEOUT:parseInt(process.env.TIMEOUT)||30000,
  SUPPORTED_BROWSERS:["chromium","firefox","webkit"],
  VIEWPORT_WIDTH:1280,
  VIEWPORT_HEIGHT:720,
  SCREENSHOT_ON_FAILURE:true,
  VIDEO_ON_FAILURE:false,
  WORKERS:1,
  RETRIES:0,
  SLOW_MO:parseInt(process.env.SLOW_MO)||100
};
```

### 6.2 Playwright-Config-File
CRITICAL-CLARIFICATION:`playwright.config.js`-exists-ONLY-to-prevent-Playwright-dependency-errors(NOT-used-by-framework-for-functional-config)

#### 6.2.1 File-Purpose
WHY-exists?
-Playwright-as-npm-package-expects-config-file
-without-this-file→warnings/errors-may-appear-when-installing-dependencies
-NOT-executed-during-tests→all-real-config-in-Cucumber+Browser-Factory

WHAT-contains?
-minimal-basic-config-to-satisfy-dependencies
-clear-comments-explaining-NOT-used
-simple-structure-that-doesn't-interfere-with-Cucumber

#### 6.2.2 Mandatory-Template
```javascript
/**
 * FILE NOT USED BY FRAMEWORK
 * Exists ONLY to prevent Playwright dependency errors
 * NOT executed during test execution
 * 
 * REAL FRAMEWORK CONFIG:
 * - cucumber.config.js: Main Cucumber config
 * - browserFactory.js: Complete browser management
 * - environmentLoader.js: Environment config
 * - env.*.js: Per-environment variables
 * 
 * IMPORTANT: NO add functional config here
 * Any config changes must be in files listed above
 */
module.exports={
  testDir:'./src',
  timeout:120000,
  use:{
    screenshot:'only-on-failure',
    video:'retain-on-failure'
  }
};
```

#### 6.2.3 Mandatory-Restrictions
WHAT-must-NOT-contain:
-import-of-`@playwright/test`
-browser-config(browserFactory.js-responsibility)
-`projects`-array-for-multi-browser(handled-by-Browser-Factory-Pattern)
-complex-launch-options-config
-workers/parallelism-config

WHAT-must-contain:
-clear-explanatory-comments
-minimal-structure-to-prevent-errors
-references-to-real-config-files
-warning-NOT-to-add-functional-config

## 7. SCRIPTS+REPORTS

### 7.1 NPM-Scripts-Config(MANDATORY)
```json
{
  "scripts":{
    "test":"cucumber-js --config cucumber.config.js",
    "test:smoke":"cucumber-js --config cucumber.config.js --tags @smoke",
    "test:regression":"cucumber-js --config cucumber.config.js --tags @regression",
    "test:dry-run":"cucumber-js --config cucumber.config.js --dry-run",
    "test:env":"cucumber-js --config cucumber.config.js --env",
    "test:local":"cross-env ENV=local cucumber-js --config cucumber.config.js",
    "test:test":"cross-env ENV=test cucumber-js --config cucumber.config.js",
    "test:headless":"cross-env HEADLESS=true cucumber-js --config cucumber.config.js",
    "test:headed":"cross-env HEADLESS=false cucumber-js --config cucumber.config.js",
    "test:chrome":"cross-env BROWSER=chromium cucumber-js --config cucumber.config.js",
    "test:firefox":"cross-env BROWSER=firefox cucumber-js --config cucumber.config.js",
    "test:webkit":"cross-env BROWSER=webkit cucumber-js --config cucumber.config.js",
    "report":"node src/support/reportGenerator.js",
    "report:generate":"cucumber-html-reporter",
    "report:open":"npx http-server reports/html -p 8080 -o",
    "clean":"node clean.js"
  }
}
```

CRITICAL:all-scripts-use-`cucumber-js --config cucumber.config.js`(NEVER-`playwright`-commands-directly)

### 7.2 Reports
After-execution→generate:
-Cucumber-JSON-report-in-/reports/json/(auto-created-if-not-exists)
-HTML-report-generated-from-JSON-in-/reports/html/(auto-created-if-not-exists)
-add-npm-scripts-for-report-generation
NOTE:all-reports-generated-by-Cucumber-execution(NOT-Playwright-directly).Subfolders-auto-created-during-report-generation

## 8. DOCUMENTATION+LANGUAGE-REQUIREMENTS

### 8.1 README.md-Requirements
Must-include(all-content-in-Spanish):
-project-description
-installation-steps
-security-section-explaining-env-variable-configuration
-instructions-to-create-.env-file
-how-to-select-env(--env test)
-how-to-run-all-tests-using-Cucumber-commands(cucumber-js)
-how-to-run-tests-by-tag-using-Cucumber(cucumber-js --tags)
-how-to-view-reports
-security-best-practices-for-credential-handling
-clear-emphasis-all-test-execution-through-Cucumber(NOT-Playwright-directly)

### 8.2 Language,Style+License-Requirements
-all-documentation,README-files,comments,user-facing-text-written-in-Spanish
-code-comments-natural+understandable(avoid-robotic/overly-technical-language)
-logs+error-messages(console.log,console.error)-clear,friendly,Spanish,NO-ICONS-NO-EMOJIS
-PROHIBITION:NO-icons/emojis-in-ANY-code-file(.js,.json,config-files)→only-allowed-in-README.md
-all-code-files-completely-free-of-visual-symbols,icons,emojis,decorative-characters
-variable+function-names-can-be-English-for-technical-clarity

### 8.3 License+Authorship-Requirements
-project-license-must-be-GPLv3
-author-field-in-package.json-must-be-"Knowmadmood"
-include-GPLv3-license-headers-in-source-files-when-needed

## 9. IMPLEMENTATION-GUIDES+BEST-PRACTICES

### 9.1 License+Authorship-Requirements
LICENSE-CONFIG:
-use-GPLv3-license-in-package.json
-author-field-must-be-"Knowmadmood"-in-package.json
-include-appropriate-license-headers-in-source-files-when-required

### 9.2 Best-Practices-to-Apply
CODE-ORGANIZATION:
-group-reusable-actions-in-helper-functions-in-/support
-keep-step-definitions-simple→all-logic-in-Page-Objects
-maintain-consistent-naming-conventions
-use-CamelCase-for-page+step-file-naming
-NO-inheritance/base-classes:each-Page-Object-independent

IMPLEMENTATION-FLOW:
-not-necessary-to-ask-to-create-folders/files→just-implement-structure-as-described
-implement-entire-structure-within-specified-new-folder
-copy-.feature-files-without-modification,analysis,implementation-based-on-them

### 9.3 Implementation-Guidelines
WORK-STRUCTURE:
-create-new-folder-in-workspace-root-directory-with-specified-name
-use-these-Playwright-instructions-to-configure-framework-structure-in-that-folder
-implement-all-generated-code-exclusively-within-new-folder
-store-all-outputs+generated-test-files-in-that-folder

FEATURE-FILE-HANDLING:
-copy-.feature-files-from-provided-BDD-project-folder-to-src/features-without-modification
-MANDATORY:NO-read,analyze,create-test-files-based-on-these-features
-ONLY-COPY-.feature-files-as-is

### 9.4 Output-Requirements
When-requested→always:
-create-complete-folder/file-structure-as-described-above
-ONLY-copy-.feature-files-from-provided-project-to-src/features
-configure-package.json-scripts-to-use-Cucumber-commands(cucumber-js)-for-test-execution
-ensure-npm-install&&npm-run-test-works-using-Cucumber-as-test-runner
-write-all-documentation+comments-in-Spanish
-emphasize-in-documentation-tests-execute-via-Cucumber(NOT-Playwright-directly)

## 10. TROUBLESHOOTING+QUALITY-CRITERIA

### 10.1 Execution-Flow-Troubleshooting
COMMON-PROBLEMS+SOLUTIONS:

PROBLEM:tests-don't-run-when-using-`npm run test`
-SOLUTION:verify-package.json-scripts-use-`cucumber-js`(NOT-`playwright`-commands)
-CHECK:ensure-cucumber.config.js-configured-correctly

PROBLEM:multiple-browser-instances/browser-conflicts
-SOLUTION:verify-only-`common.steps.js`-contains-Before/After-hooks-for-browser-management
-CHECK:ensure-feature-specific-step-files-use-`this.page`-from-shared-context

PROBLEM:env-variables-not-loading
-SOLUTION:verify-.env-file-exists+formatted-correctly
-CHECK:ensure-env-files(env.local.js,env.test.js)-export-config-correctly

PROBLEM:Browser-Factory-not-working
-SOLUTION:verify-`browserFactory.js`-exports-class/functions-correctly
-CHECK:ensure-`common.steps.js`-imports+uses-Browser-Factory-correctly

PROBLEM:cross-browser-tests-fail
-SOLUTION:verify-BROWSER-env-variable-set-correctly
-CHECK:ensure-Page-Objects-work-across-different-browser-types

### 10.2 Final-Quality-Objective
Produce-high-quality+maintainable-Playwright-framework-structure-that:

FRAMEWORK-ARCHITECTURE:
-adheres-to-Page-Object-Model-design-pattern-without-inheritance
-integrates-seamlessly-with-Cucumber-Playwright-execution-flow
-implements-centralized-Browser-Factory-Pattern-for-browser-management
-maintains-clear-separation-between-test-runner(Cucumber)+automation-engine(Playwright)
-supports-env-configuration-via-.env-files

EXECUTION-CLARITY:
-Cucumber-as-ONLY-test-runner→all-execution-via-cucumber-js-commands
-clear-execution-hierarchy→npm→Cucumber→Step-Definitions→Page-Objects→Playwright
-centralized-browser-management→single-lifecycle-manager-with-shared-context-pattern
-multi-browser-support→env-variable-driven-browser-selection
