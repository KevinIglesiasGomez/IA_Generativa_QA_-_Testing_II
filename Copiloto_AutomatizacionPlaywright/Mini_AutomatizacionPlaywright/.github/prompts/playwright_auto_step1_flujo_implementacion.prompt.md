---
agent: "Playwright Automation"
tools: ["edit/editFiles", "search", "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection", "search/usages"]
description: "Step 1 — Implementar pruebas Playwright siguiendo el flujo interactivo, Browser Factory Pattern en JavaScript y buenas prácticas de seguridad"
---

# Step 1: Playwright Test Implementation Flow

CONTEXT-INSTRUCTIONS-FOR-THIS-STEP:

LOAD-mandatorily:
-playwright_auto_main.instructions.md  # framework-config+execution-patterns
-playwright_auto_buenas_practicas.instructions.md  # mandatory-JavaScript/Playwright-patterns
-playwright_auto_interactive_flow.instructions.md  # interactive-approval-flow-with-engineer

DO-NOT-load-in-this-step:
-playwright_auto_calidad_verificacion.instructions.md  # used-in-Step-2
-playwright_auto_bitacora.instructions.md  # used-at-Step-1-end

---

IMPLEMENTATION-ORDER:

1.review-existing-step-files(in-${input:playwright_folder}/src/steps/,reuse-already-implemented-steps,understand-patterns-in-use)
2.identify-shared-context-pattern:how-page-shared-between-Steps(via-this.page,defined-in-common.steps.js)
3.fully-analyze-feature-file-${input:feature_name}(in-${input:project_bdd},determine-total-implementation-scope)
4.obtain-precise-element-locators(one-of-these-approaches):
  -if-${input:code_folder}-available:review-static-pages|relevant-code(extract-selectors)
  -if-no-source-code-access:create-dynamic-inspection-scripts(inspect_*.js,exec-browser,analyze-actual-rendered-DOM).See-[snippet:inspeccion-dinamica]-for-pattern
5.create|extend-Page-Objects(receive-page-instance-via-constructor.Never-instantiate-Playwright-browser/page-inside-POs)
6.create|extend-Step-files(use-this.page-from-shared-context.Step-files-never-create-own-browser-instances)
7.work-strictly-one-scenario-at-a-time(follow-interactive-flow-from-playwright_auto_interactive_flow.instructions.md)
8.MANDATORY-INTERACTIVE-FLOW(after-implementing-each-scenario):
  a.implement-scenario-code
  b.ASK:"Execute test now?(yes/no)"
  c.WAIT-for-user-confirmation
  d.ONLY-after-confirmation=>execute-with-npm
  e.WAIT-for-complete-execution-finish
  f.ASK:"Test worked correctly?(yes/no/error)"
  g.WAIT-for-user-response  # NEVER-assume-result
  h.if-error=>ASK-before-each-correction+retry
9.FAILURE-PROTOCOL:
  -max-3-correction-attempts
  -ASK-before-each-correction:"Apply this correction?(yes/no)"
  -ASK-before-each-retry:"Execute again?(yes/no)"
  -NEVER-execute-multiple-times-without-confirmation
10.repeat-for-each-remaining-scenario(until-all-implemented+validated)

---

GOALS:
-implement-ALL-Gherkin-steps(from-.feature,as-JavaScript-files-*.steps.js)
-strictly-follow-Page-Object-Model-pattern(JavaScript,with-locators-in-separate-files)
-ONLY-common.steps.js-manages-browser:setup-with-Before,teardown-with-After
-ensure-complete-coverage(all-BDD-functionalities-described-in-feature)
-implement-explicit-waits-with-conditions  # never-page.waitForTimeout()-with-fixed-values
-NO-sensitive-data-in-code:URLs+credentials-via-env-files|process.env
-use-console.log(descriptive-msgs,facilitate-debugging)

---

IMPLEMENTATION-RULES:
1.all-new-code=generated-inside-${input:playwright_folder}
2.locators-as-constants(in-separate-*PageLocators.js-files,UPPER_SNAKE_CASE)
3.business-logic-in-Page-Objects;Steps-only-orchestrate-PO-method-calls
4.documentation,comments,log-msgs:Spanish
5.SECURITY:never-hardcode-URLs,passwords,env-data;use-env-files|process.env
6.mark-with-@pendiente(scenarios-that-cannot-be-fully-implemented,individual-level)
7..feature-file-NOT-modified(except-to-add-@pendiente-tags)
8.SQL-queries=must-be-in-src/utils/QueryDeposit.js(never-inline-in-Steps|POs)

---

VALIDATION-BEFORE-APPROVING-EACH-SCENARIO:
-no-duplicate-browser-instances(only-one-per-scenario,managed-in-common.steps.js)
-no-Before/After-hooks(in-Step-files!=common.steps.js)
-POs-receive-page-instance-via-constructor(not-instantiate-it)
-no-page.waitForTimeout()  # fixed-values,use-waits-with-state-conditions
-no-hardcoded-sensitive-data
-scenario-executes-correctly-with-npm,browser-visible(HEADLESS=false)

---

FINAL-QUALITY-GOAL:

Produce-high-quality-Playwright-JavaScript-tests-that:
-implement-all-Gherkin-scenarios(from-${input:feature_name})
-adhere-to-Page-Object-Model-pattern(JavaScript)
-integrate-correctly-in-${input:playwright_folder}(without-breaking-existing-tests)
-use-precise-locators(obtained-from-${input:code_folder}-analysis)
-contain-NO-hardcoded-sensitive-data
-are-executable-with-npm run test,produce-reports-in-reports/
