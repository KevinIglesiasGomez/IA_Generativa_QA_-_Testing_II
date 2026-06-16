---
description: Instrucciones de verificación de calidad para automatización de pruebas Playwright
applyTo: "**/*.steps.js,**/*Page.js,**/cucumber.config.js"
---

# Quality Verification for Playwright Test Automation

QUALITY-CRITERIA:

SYNTAX+STRUCTURE-VALIDATION:

CRITICAL-VALIDATIONS-CHECKLIST:
-[x]clean-syntax:npm run test:dry-run(no-errors,no-warnings)
-[x]Browser-Factory-pattern:ONLY-common.steps.js-creates+closes-browser
-[x]NO-browser-instances-in-POs:POs-receive-this.page-from-shared-context
-[x]NO-duplicate-Before/After-hooks:ONLY-common.steps.js-defines-Cucumber-hooks
-[x]correct-shared-context:Steps-use-this.page,this.baseUrl,this.config(from-shared-context)
-[x]NO-page.waitForTimeout()  # fixed-values,ALWAYS-use-waits-with-state-conditions
-[x]locators-in-separate-files:selectors-in-*PageLocators.js(NOT-inline-in-POs/Steps)
-[x]business-logic-in-POs:Steps-only-orchestrate,interaction-logic=>Page-Object
-[x]correct-scenario-tags:use-@smoke,@regression,@critical,@pendiente(as-needed)
-[x]pending-scenarios-tagged-individually:@pendiente-per-scenario(NEVER-only-Feature-level)
-[x]NO-sensitive-data-in-code:URLs,credentials,env-config-loaded-from-env.*.js|process.env
-[x]style-compliance:NO-emojis,icons,decorative-chars(in-code-files,logs)

EXECUTION-VALIDATION:
-[x]scenario-executes-correctly:npx cucumber-js --config cucumber.config.js --tags "@<tag>"(passes-no-errors)
-[x]browser-closes-correctly:no-orphaned-Playwright-processes-after-exec
-[x]reports-generated:reports/json/+reports/html/(created-after-exec)
-[x]no-headless-mode-active:browser-visible-during-exec(HEADLESS=false,unless-CI)
-[x]NO-UNDEFINED-steps-in-report:all-Gherkin-steps-in-.feature=have-implementation

---

FINAL-VALIDATIONS-CHECKLIST:
-[x]framework-runs-dry-run:npm run test:dry-run
-[x]ONLY-common.steps.js-manages-browser-lifecycle(Before/After)
-[x]all-other-Steps-receive-browser-via-this.page(shared-context)
-[x]POs-receive-page-instance-via-constructor(never-create-it)
-[x]step-definitions-use-shared-context(not-create-own-browser)
-[x]NO-hardcoded-sensitive-data:URLs+credentials-in-env-files|process.env
-[x]non-implemented-scenarios-marked-with-@pendiente(individually)
-[x]each-scenario-executed+validated-before-moving-to-next
-[x]automation-log-updated-with-session-changes

---

PROHIBITED-PATTERNS:

See-full-examples:.github/snippets/playwright_auto_code_snippets.md:[snippet:patron-antipatron]

QUICK-SUMMARY:
-const {chromium}=require('playwright');await chromium.launch()  # outside-browserFactory.js
-page.waitForTimeout(3000)  # fixed-values
-inline-CSS/XPath-locators(in-Steps|POs)  # extract=>*PageLocators.js
-Before/After-hooks(in-step-files!=common.steps.js)
-hardcoded-URLs|credentials:baseUrl='https://app.example.com'

---

FINAL-QUALITY-GOAL:

Produce-high-quality+maintainable-Playwright-tests-that:
-implement-all-Gherkin-scenarios(from-analyzed-.feature-file)
-adhere-to-Page-Object-Model-design-pattern(JavaScript)
-integrate-correctly-with-existing-Playwright-framework-structure
-automate-navigation+interactions(using-precise-locators-from-app-analysis)
-contain-NO-hardcoded-sensitive-data(URLs,credentials,environments)
-include-failure-evidence-capture(screenshots,correctly-configured)
-follow-established-browser-management-architecture(Browser Factory Pattern,avoid-conflicts+duplicate-instances)
