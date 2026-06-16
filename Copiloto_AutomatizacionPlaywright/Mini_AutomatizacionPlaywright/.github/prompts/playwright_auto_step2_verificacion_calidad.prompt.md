---
agent: "Playwright Automation"
tools: ["edit/editFiles", "search", "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection", "search/usages"]
description: "Step 2 — Verificación de calidad del test Playwright automatizado e integración en framework existente"
---

# Step 2: Automated Playwright Test Quality Verification

CONTEXT-INSTRUCTIONS-FOR-THIS-STEP:

LOAD-mandatorily:
-playwright_auto_calidad_verificacion.instructions.md  # Playwright-quality-checklist
-playwright_auto_buenas_practicas.instructions.md  # mandatory-JavaScript/Playwright-patterns
-playwright_auto_bitacora.instructions.md  # log-update-instructions

DO-NOT-load-in-this-step:
-playwright_auto_framework.instructions.md  # architecture-already-known-from-previous-step
-playwright_auto_interactive_flow.instructions.md

---

QUALITY-VALIDATION:

SYNTAX+STRUCTURE-VERIFICATIONS:
-[x]clean-syntax:npm run test:dry-run(executes-without-errors)
-[x]Browser-Factory-pattern-applied:ONLY-common.steps.js-creates+closes-browser
-[x]page-correctly-managed:all-other-Steps-use-this.page(from-shared-context)
-[x]NO-duplicate-browser-instances:single-active-browser-per-scenario
-[x]NO-page.waitForTimeout()  # fixed-values,only-waits-with-state-conditions
-[x]locators-in-separate-files:defined-in-*PageLocators.js(as-UPPER_SNAKE_CASE-constants)
-[x]logic-in-Page-Objects:Steps-only-call-PO-methods(not-directly-interact-with-page)
-[x]NO-sensitive-data:no-hardcoded-URLs,credentials,passwords(in-source-code)
-[x]individual-@pendiente:non-implemented-scenarios-have-tag(on-specific-scenario,not-entire-Feature)
-[x]NO-emojis-nor-decorative-chars(in-source-code,log-msgs)

EXECUTION-VERIFICATION:
-[x]scenario-passes:npx cucumber-js --config cucumber.config.js --tags "@<tag>"(no-errors)
-[x]browser-closes-correctly:no-orphaned-Playwright-processes-after-exec
-[x]reports-generated:reports/json/+reports/html/(correctly-created)
-[x]visible-browser:no-headless-mode-active(engineer-can-observe-execution)
-[x]NO-UNDEFINED-steps-in-report:all-Gherkin-steps-from-.feature=have-implementation

---

FRAMEWORK-INTEGRATION-VERIFICATION:
-[x]new-files-do-not-break-existing-features-exec:npm run test(passes-globally)
-[x]new-Steps-correctly-loaded-by-cucumber.config.js(auto-load-src/steps/**/*.js)
-[x]new-Page-Objects-follow-framework-naming-conventions({Funcionalidad}Page.js)
-[x]new-Steps-follow-naming-conventions({funcionalidad}.steps.js)
-[x]new-locator-files-follow-naming({Funcionalidad}PageLocators.js)
-[x]NO-duplicated-code(already-existing-in-other-Steps|POs)

---

PROHIBITED-PATTERNS-VERIFY-ABSENCE:

```javascript
// MUST-NEVER-appear-in-generated-code
await page.waitForTimeout(3000);  # fixed-wait

const {chromium}=require('playwright');  # outside-browserFactory.js
const browser=await chromium.launch();  # outside-browserFactory.js

Before(async function(){this.page=...});  # hooks-in-steps!=common.steps.js

const baseUrl='https://app.example.com';  # hardcoded-URL
const password='micontrasenia123';  # hardcoded-credential

// inline-locator-in-Steps(must-be-in-*PageLocators.js)
await this.page.click('#loginButton');  # direct-page-access-in-Step
```

---

LOG-UPDATE:

Once-all-previous-points-validated=>update-automation_logs/automation_bitacora.md(follow-playwright_auto_bitacora.instructions.md):
-record-each-automated-scenario(date,modified-files,challenges-found)
-record=brief+sufficiently-clear(for-any-team-engineer)

---

FINAL-QUALITY-GOAL:

Generated-Playwright-tests-must:
-correctly-implement-all-Gherkin-scenarios(from-${input:feature_name})
-integrate-in-${input:playwright_folder}(without-breaking-existing-suite)
-follow-Page-Object-Model-pattern(JavaScript,with-separate-locators)
-contain-NO-hardcoded-sensitive-data;all-config-via-env-files|process.env
-be-executable-with-npm run test,produce-reports-in-reports/
