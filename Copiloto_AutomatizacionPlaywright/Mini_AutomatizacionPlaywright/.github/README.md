# Playwright Automation Copilot

GitHub-Copilot-agent-specialized-in-Playwright-automated-test-generation(for-existing-BDD-framework:Cucumber-JS+Node.js)

---

FEATURES+CAPABILITIES:
-interactive-Playwright-test-generation(Page-Object-Model-pattern,JavaScript)
-analyze-existing-Playwright-framework(before-proposing-implementation)
-scenario-by-scenario-approval-flow:never-generates-multiple-implementations(without-engineer-validation)
-fully-adapted-to-project-Playwright-framework:Browser-Factory-Pattern,shared-context-this.page,locators-in-separate-*PageLocators.js-files
-multi-browser-support:chromium,firefox,webkit
-terminal-test-execution:npm run test(visible-mode,no-headless,for-engineer-review)
-auto-update-automation-log(after-each-session)
-structured-failure-protocol:max-2-autonomous-retries,engineer-diagnosis-on-third

---

COPILOT-FILES:

MAIN-AGENT:
agents/playwright_auto_generation.agent.md:agent-definition(role,model,allowed-tools,tone,restrictions)

INSTRUCTIONS:
instructions/playwright_auto_framework.instructions.md:complete-Playwright-framework-structure(folders,dependencies,architecture-patterns,multi-env-config)|applies-to:**/*.js,**/package.json,**/*.feature
instructions/playwright_auto_main.instructions.md:config+execution-patterns(npm-commands,Browser-Factory,env-management,code-conventions)|applies-to:**/*.js,**/package.json,**/cucumber.config.js
instructions/playwright_auto_buenas_practicas.instructions.md:recommended-selectors,explicit-waits,Step-organization,PO-error-handling|applies-to:**/*.js,**/*.feature
instructions/playwright_auto_calidad_verificacion.instructions.md:quality-checklist(validate-each-test-before-approval,prohibited-patterns)|applies-to:**/*.steps.js,**/*Page.js,**/cucumber.config.js
instructions/playwright_auto_bitacora.instructions.md:automation-log-format+rules(automation_logs/automation_bitacora.md)|applies-to:**/automation_bitacora.md
instructions/playwright_auto_interactive_flow.instructions.md:mandatory-interactive-flow(process-steps,engineer-orders,failure-protocol)|applies-to:**

PROMPTS:
prompts/playwright_auto_step0_contexto_analisis.prompt.md:framework+BDD-scenario-analysis(produces:step-inventory,needed-Page-Objects,detected-risks)
prompts/playwright_auto_step1_flujo_implementacion.prompt.md:interactive-scenario-by-scenario-implementation(following-approval-flow)
prompts/playwright_auto_step2_verificacion_calidad.prompt.md:final-quality-verification,integration-validation,log-update

SNIPPETS:
snippets/playwright_auto_code_snippets.md:reusable-JS-snippets-library(Page-Object,Steps,Browser-Factory,locators,waits,data,prohibited-patterns)

---

COPILOT-USAGE:

TEST-CASE-ORIGIN:
Copilot-DOES-NOT-generate|invent-test-cases.Cases-to-automate=always-defined-by-QA-engineer(in-.feature-files,written-in-Gherkin).Copilot-reads-these-files+converts-them-to-executable-Playwright-code.

.feature-file=MUST-exist-before-starting-work-session.Copilot-analyzes-scenarios,identifies-already-implemented-steps-in-framework,proposes-implementation-of-new-ones(one-at-a-time,with-explicit-engineer-approval).

WORK-SESSION-START:
1.open-GitHub-Copilot-Chat-panel(VS Code)
2.select-agent:Playwright Automation(in-agent-selector)
3.tell-it:"Comenzar"

Copilot-operates-in-two-modes(depending-on-context):

MODE-A:with-source-code-access
-requests-vars:feature_name,project_bdd,playwright_folder,code_folder
-analyzes-static-source-code(extract-locators)
-useful-for:modern-apps-with-accessible-code

MODE-B:without-source-code-access(legacy-apps,framesets)
-auto-detects-workspace+active-feature
-creates-temp-inspection-scripts(inspect_*.js)
-executes-browser(analyze-actual-rendered-DOM)
-extracts-selectors-from-runtime-HTML

4.review-analysis+continue-with-implementation-flow

LOCATOR-OBTAINING-METHODS:

Copilot-supports-two-complementary-approaches:

A.static-source-code-analysis(code_folder-var):
-WHEN-TO-USE:modern-apps-with-accessible-source-code(React,Vue,Angular)
-HOW-IT-WORKS:analyzes-HTML/JSX/template-files(extract-selectors)
-ADVANTAGES:no-need-to-run-app,fast-analysis
-LIMITATIONS:does-not-detect-dynamically-generated-elements(JavaScript)

B.dynamic-DOM-inspection(without-code_folder):
-WHEN-TO-USE:legacy-apps,framesets,no-source-code-access
-HOW-IT-WORKS:
  1.creates-temp-scripts(launch-browser)
  2.inspects-rendered-DOM-in-real-time
  3.detects-frames,dynamic-elements,actual-structure
  4.extracts-precise-selectors(from-final-HTML)
-ADVANTAGES:100%-accurate-selectors-from-actual-DOM,detects-complex-architectures
-EXAMPLE:frameset-apps,server-rendered-JSP,AJAX-loaded-elements

Copilot-auto-chooses-most-appropriate-approach(based-on-app-type)

STEP-BY-STEP-IMPLEMENTATION-FLOW:
1.copilot-analyzes-framework+feature,identifies-existing+new-steps
2.proposes-first-scenario(with-complete-code)
3.engineer-approves|rejects:"Approve scenario 1(yes/no)"
4.AFTER-APPROVAL=>copilot-asks:"Execute test now?(yes/no)"
5.ONLY-after-confirmation=>executes-test(visible-mode):
  npx cucumber-js --config cucumber.config.js src/features/<feature_name> --tags "@<tag>"
6.WAITS-for-complete-execution-finish
7.ASKS-MANDATORILY:"Test worked correctly?(yes/no/error)"
  -if-"yes":updates-log+proposes-next-scenario
  -if-"no/error":analyzes-error,proposes-correction,ASKS-before-applying
8.IN-CASE-OF-FAILURE:
  -NEVER-retries-without-asking
  -shows-error+proposes-solution
  -asks:"Apply this correction?(yes/no)"
  -if-approved=>asks:"Execute again?(yes/no)"
  -max-3-attempts(with-confirmation-on-each)
9.cycle-repeats-for-each-scenario
10.at-end=>updates-log(automation_logs/automation_bitacora.md)

ENGINEER-AVAILABLE-COMMANDS:
"Approve scenario N(yes/no)":approves|rejects-proposed-implementation
"Execute"/"yes":confirms-test-execution-can-proceed
"Retry"/"yes":confirms-re-execution-after-correction
"error":indicates-execution-error
"stop":stops-current-retry-flow
"Reconsider scenario N":copilot-offers-questions(understand-rejection,improve-proposal)
"End work session":closes-session,updates-log-with-current-state
"Restart work session":resumes-session-from-last-registered-point-in-log
"Change page/component/feature":shifts-work-focus,updates-log,restarts-analysis

---

EXPECTED-OUTPUT:

Each-work-session-produces(within-framework-playwright):
-Step-files(src/steps/{funcionalidad}.steps.js):Gherkin-step-implementation(JavaScript,using-this.page-from-shared-context)
-Page-Objects(src/pages/{Funcionalidad}Page.js):browser-interaction-encapsulation(receiving-page-via-constructor)
-Locators(src/pages/pagesLocators/{Funcionalidad}PageLocators.js):centralized-CSS/ARIA/data-testid-selectors(UPPER_SNAKE_CASE-constants)
-Data-classes(src/datas/{Funcionalidad}Data.js):simple-objects(store-scenario-data-when-needed)
-Log-update(automation_logs/automation_bitacora.md):record-per-automated-scenario(date,modified-files,observations)

Generated-code=directly-executable-with:
npm run test
npm run test:smoke
npm run test:headed

---

CODE-GENERATION-RULES:

MANDATORY-ARCHITECTURE:
1.ONLY-common.steps.js-manages-browser-lifecycle.No-other-Step-file-defines-Before|After-hooks
2.Page-Objects-receive-this.page-via-constructor.Never-instantiate-browser-independently
3.Locators-reside-in-separate-*PageLocators.js-files.Not-defined-inline(in-POs|Steps)
4.Steps-use-shared-context(this.page,this.baseUrl,this.config).Do-not-access-page-directly(without-going-through-Page-Object)
5.SQL-queries=centralized-in-src/utils/QueryDeposit.js.Never-written-inline

WAITS+SYNCHRONIZATION:
6.PROHIBITED:page.waitForTimeout()-with-fixed-values.ALWAYS-use-state-condition-waits:waitFor({state:'visible'}),waitForURL(),waitForLoadState()

SECURITY:
7.PROHIBITED:hardcode-URLs,credentials,env-data(directly-in-code).Use-process.env|env-files(env.local.js,env.test.js)
8..env-files-with-real-data=NOT-included-in-version-control

STYLE+NAMING:
9.comments,documentation,logs:Spanish
10.class-names:PascalCase(English,e.g.LoginPage,MenuPage)
11.methods+variables:camelCase(English,e.g.fillUsername(),loginButton)
12.locator-constants:UPPER_SNAKE_CASE(English,e.g.LOGIN_BUTTON='#loginBtn')
13.NO:emojis,icons,decorative-symbols(in-any-project-file)

WORKFLOW:
14.one-scenario-at-a-time.Copilot-does-not-advance-to-next(without-explicit-engineer-approval)
15.mandatory-execution-after-implementation.Each-scenario=executed-with-npm run test:headed(before-moving-to-next)
16.max-2-autonomous-retries(on-execution-failures).Third-attempt=escalate-to-engineer-with-structured-diagnosis
17.@pendiente=individual-scenario-level(NEVER-at-complete-Feature-level)
