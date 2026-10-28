---
agent: "Playwright Automation"
tools: ["edit/editFiles", "search", "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection", "search/usages"]
description: "Step 0 — Analizar el framework Playwright existente y el escenario BDD a automatizar"
---

# Step 0: Analyze Existing Playwright Framework + BDD Scenario to Implement

CONTEXT-INSTRUCTIONS-FOR-THIS-STEP:

LOAD-mandatorily:
-playwright_auto_framework.instructions.md  # existing-framework-architecture+structure
-playwright_auto_buenas_practicas.instructions.md  # mandatory-JavaScript/Playwright-patterns

DO-NOT-load-in-this-step:
-playwright_auto_calidad_verificacion.instructions.md
-playwright_auto_bitacora.instructions.md

---

INPUT-VARIABLES:
-${input:feature_name}:BDD-.feature-file-name-to-implement
-${input:project_bdd}:BDD-project-root-folder(contains-.feature-files)
-${input:playwright_folder}:existing-Playwright-framework-root-folder
-${input:code_folder}(OPTIONAL):folder-with-HTML/JSP-pages|relevant-app-source-code.If-not-available=>use-dynamic-DOM-inspection.If-contains-README=>read-completely(understand-initial-navigation)

---

PROJECT-CONTEXT:

Task=generate-Playwright-automated-tests(JavaScript,based-on-BDD-feature-scenario-${input:feature_name},located-in-${input:project_bdd})

-read+analyze-ONLY-feature-file-${input:feature_name}(in-full)
-all-Gherkin-steps=>implemented-as-JS-step-files(*.steps.js,inside-existing-framework-in-${input:playwright_folder})
-framework-uses:JavaScript+Playwright+Cucumber-JS+npm

---

CRITICAL-CONSTRAINTS:
-use-existing-structure+config-files(in-${input:playwright_folder})
-analyze-existing-Steps(src/steps/*.js)+Page-Objects(src/pages/*.js,for-reusable-code,before-creating-new-classes)
-ONLY-common.steps.js-manages-browser-lifecycle(Before/After)
-NEVER-create-browser-instances(in-Step-files!=common.steps.js)
-NEVER-create-browser-instances-in-Page-Objects  # POs-receive-page-via-constructor
-page-shared-between-Steps-via-shared-context-this.page

---

ANALYSIS-ORDER:

1.ANALYZE-existing-framework(in-${input:playwright_folder}):
  -read-src/support/browserFactory.js  # understand-centralized-browser-management
  -read-src/steps/common.steps.js  # understand-browser-lifecycle-pattern
  -review-Data-classes(e.g.LoginData.js,UsuarioData.js,understand-scenario-data-storage)
  -review-src/support/environmentLoader.js  # understand-env-config-loading
  -identify-reusable-existing-Page-Objects+Steps(for-feature-to-implement)

2.ANALYZE-feature-file-${input:feature_name}(in-${input:project_bdd}):
  -identify-all-Gherkin-steps-to-implement
  -detect-already-implemented-steps(in-existing-Steps,reuse-them)
  -detect-new-steps(require-code-creation)
  -identify-required-test-data(if-DB-queries-needed-via-AtDBConnector.js)

3.OBTAIN-app-element-locators(two-approaches):

  APPROACH-A:static-source-code-analysis(if-${input:code_folder}-available):
  -review-HTML-pages|source-code(in-${input:code_folder},obtain-precise-locators-for-interactive-elements)
  -read-README-if-exists(understand-initial-navigation)
  -identify-relevant-interactive-elements(per-Gherkin-step)

  APPROACH-B:dynamic-DOM-inspection(without-${input:code_folder}|for-legacy-apps/framesets):
  -create-temp-inspection-scripts(inspect_*.js,in-Playwright-project-root)
  -exec-browser(analyze-actual-rendered-DOM-structure)
  -detect-frames,dynamic-elements,JS-functions
  -extract-precise-selectors(from-final-HTML)
  -EXAMPLE-SCRIPT:see-[snippet:inspeccion-dinamica]

---

ARCHITECTURE-PATTERN(MANDATORY):

See-full-examples:.github/snippets/playwright_auto_code_snippets.md

MANDATORY-PATTERNS:
-Page-Object-receives-this.page(via-constructor,defines-locators-in-separate-file,[snippet:page-object-basico])
-Steps-use-this.page(from-shared-context,never-create-browser,[snippet:steps-playwright])
-ONLY-common.steps.js-manages-Before/After+browser-lifecycle([snippet:common-steps])

---

ANALYSIS-GOALS:

At-step-end=>must-have-produced:

1.Gherkin-steps-inventory(from-feature-${input:feature_name}):
  -already-implemented-steps(with-reference-to-existing-Step-file)
  -new-steps-to-implement(with-description-of-needed-Page-Object+logic)

2.Page-Objects-list(to-create|extend,with-locators-identified-via-static-source-code-analysis|dynamic-DOM-inspection)

3.detected-technical-risks+concrete-solution-proposal

4.implementation-proposal(for-first-scenario,ready-to-present-to-engineer,before-writing-code)

---

SECURITY:
-NEVER-hardcode-URLs,credentials,env-data(in-source-code)
-all-sensitive-config=loaded-from-env-files(env.*.js)|process.env
-test-data-requiring-DB=obtained-with-AtDBConnector.js(using-active-env-config)
-SQL-queries=maintained-in-src/utils/QueryDeposit.js(never-inline)
