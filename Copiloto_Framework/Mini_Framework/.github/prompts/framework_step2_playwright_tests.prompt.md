---
agent: "agent"
tools: ["edit/editFiles", "search", "microsoft/playwright-mcp/*", "runCommands", "usages"]
description: "Generar Pruebas de Playwright"
---

# Prompt: Generate-Playwright-Tests

## 1. PREREQUISITES+CONTEXT

### 1.1 Required-Instruction-Files

TECHNICAL-TRUTH-SOURCE:this-prompt-requires-follow-ALL-instructions-defined-in:

-**`playwright_tests.instructions.md`**:contains-ALL-test-patterns,browser-management-architecture,security-requirements,implementation-guides

CRITICAL:`playwright_tests.instructions.md`=ONLY-truth-source-for:

-Browser-Factory-Pattern(mandatory-usage)
-browser-management-architecture
-Page-Object-Model(POM)-without-inheritance
-security-requirements
-test-best-practices
-shared-context-patterns

### 1.2 Input-Variables

-**${input:feature_name}**:BDD-.feature-file-name-to-implement
-**${input:project_bdd}**:folder-containing-existing-.feature-files
-**${input:playwright_folder}**:existing-Playwright-framework-folder
-**${input:JSP_folder}**:folder-containing-JSP/static-HTML-pages-for-reference

### 1.3 Project-Context

Read-complete-prompt-before-instructions.Task:generate-Playwright-automated-tests-based-on-BDD-feature-scenario-called-**${input:feature_name}**-located-in-folder:**${input:project_bdd}**,read+analyze-ONLY-this-.feature-file-completely.All-steps-described-in-Gherkin-BDD-feature-**${input:feature_name}**-must-be-implemented-as-.js-files-in-src/pages-folder-with-corresponding-src/steps

IMPORTANT:framework-uses-Cucumber-as-main-test-runner.All-test-execution-via-Cucumber-commands(cucumber-js)(NOT-Playwright-commands-directly).Playwright-used-internally-by-step-definitions-for-browser-automation

## 2. CRITICAL-RESTRICTIONS

-use-existing-Playwright-framework-structure+config-files-in-**${input:playwright_folder}**
-analyze-previous-Pages(src/pages)+step-definitions(src/steps)-for-reusable-code
-MANDATORY:use-existing-Browser-Factory-Pattern→never-create-direct-browser-instances
-NEVER-create-duplicate-browser-initialization→use-existing-browser-context-from-`this.page`
-NO-add-Before/After-hooks-for-browser-management-in-feature-specific-step-files
-feature-step-files-must-ONLY-use-`this.page`-from-shared-context(never-initialize-browsers)
-leverage-existing-browserFactory.js-for-consistent-browser-management-patterns

## 3. PROJECT-CONFIG

### 3.1 Development-Resources

-review-JSP/static-HTML-pages-available-in-**${input:JSP_folder}**→get-info-about-app-structure+behavior.IF-README-in-this-directory→read-completely-for-initial-navigation-details
-test-framework-must-strictly-follow-Page-Object-Model(POM)-design
-test-execution-via-Cucumber-commands(cucumber-js),with-Playwright-used-internally-for-browser-automation
-review-existing-files-in-**${input:playwright_folder}**-folder→understand-how-pages(src/pages)+steps(src/steps)-work
-apply-ALL-security-requirements-from-`playwright_tests.instructions.md`-for-env-variable-configuration

## 4. BROWSER-MANAGEMENT-ARCHITECTURE-PATTERN

CRITICAL-RULES:

1.BROWSER-FACTORY-PATTERN:always-use-existing-browserFactory.js-for-browser-management→never-create-direct-instances
2.SINGLE-BROWSER-INSTANCE:ONLY-ONE-step-file(typically-`autenticacion.steps.js`)-should-initialize+manage-browser-lifecycle-using-Browser-Factory
3.SHARED-CONTEXT:all-feature-specific-step-files-must-use-`this.page`-from-Cucumber-shared-context
4.PAGE-OBJECT-PATTERN:

```javascript
// ✅ CORRECT - Feature step file
const BrowserFactory=require("../support/browserFactory");
let myPage;
Given("some step",async function(){
  if(!myPage){
    myPage=new MyPage(this.page); // Use shared context
  }
});

// ❌ WRONG - Never do in feature step files
Before(async function(){
  browser=await chromium.launch(); // Creates duplicate browser
});

// ❌ WRONG - Direct browser creation
const browser=await chromium.launch();

// ✅ CORRECT - Use Browser Factory (only in main step file)
const browser=await BrowserFactory.createBrowser();
```

5.NO-DUPLICATE-HOOKS:feature-specific-step-files-must-NOT-have-Before/After-hooks-for-browser-management
6.INITIALIZATION-PATTERN:initialize-Page-Objects-within-step-definitions-using-`this.page`-parameter-only
7.MULTI-BROWSER-SUPPORT:leverage-existing-Browser-Factory-for-cross-browser-test-capabilities

## 5. IMPLEMENTATION-ORDER

1.FIRST:review-existing-step-files→understand-browser-management-pattern(typically-in-autenticacion.steps.js)
2.IDENTIFY-shared-context-pattern→how-`this.page`-provided-to-step-definitions
3.analyze-provided-.feature-file-**${input:feature_name}**→fully-understand-requirements+test-scope
4.review-ONLY-relevant-JSP/static-HTML-pages-in-**${input:JSP_folder}**→gather-info-about-app-structure,element-locators,behavior.Read-any-README-in-folder-for-initial-navigation-details
5.create-Page-Objects-accepting-`this.page`-parameter→never-initialize-browsers-inside-Page-Objects
6.create-step-definitions-using-shared-context→initialize-Page-Objects-with-`this.page`-only
7.work-strictly-one-scenario-at-a-time
8.create-single-scenario,execute-it+confirm-works-correctly-before-proceeding.Must-NOT-create/move-to-next-scenario-until-current-fully-functional
9.to-execute-specific-scenario→ensure-in-correct-directory+use-cucumber-command:
`cucumber-js --config cucumber.config.js src/features/Login.feature`
10.repeat-process-for-each-remaining-scenario-in-.feature-file-until-all-implemented+validated-successfully

## 6. OBJECTIVES

-implement-ALL-BDD-scenario-steps-using-Cucumber.js-step-definitions
-strictly-follow-Page-Object-Model(POM)-pattern
-MANDATORY:use-existing-Browser-Factory-Pattern→never-create-direct-browser-instances
-ensure-tests-cover-ALL-described-BDD-functionalities
-create-robust+maintainable-test-automation
-implement-appropriate-error-handling+wait-strategies
-CRITICAL:implement-security-best-practices→NO-hardcoded-credentials,URLs,sensitive-data
-use-env-variables-for-all-config+sensitive-info
-FOLLOW-established-browser-management-patterns→use-only-shared-context-`this.page`
-LEVERAGE-multi-browser-capabilities→tests-must-work-in-chromium,firefox,webkit
-AVOID-duplicate-browser-instances→feature-step-files-never-initialize-browsers
-MAINTAIN-cross-browser-compatibility→all-Page-Objects-must-work-with-Browser-Factory-pattern

## 7. IMPLEMENTATION-RULES

1.use-Playwright-test-instructions-to-implement-tests-in-existing-**${input:playwright_folder}**-folder
2.implement-all-generated-code-exclusively-within-this-folder
3.store-ALL-outputs+generated-test-files-in-this-folder
4.all-documentation,README-files,comments,user-facing-text-written-in-Spanish
5.SECURITY-REQUIREMENT:never-hardcode-sensitive-info-like-URLs,usernames,passwords,env-specific-data-in-any-config-file.Always-use-env-variables-with-`process.env`+provide-sensible-defaults
6.include-appropriate-security-documentation-in-README-explaining-how-to-configure-env-variables-securely
7.TAGGING-REQUIREMENT:mark-non-implemented-scenarios-with-`@pendiente`-at-individual-scenario-level(never-only-at-Feature-level)

## 8. VALIDATION

### 8.1 Checklist

-NO-duplicate-browser-instances:only-one-browser-should-open-during-test-execution
-NO-Before/After-hooks-in-feature-specific-step-files-for-browser-management
-Page-Objects-receive-`this.page`-parameter(never-initialize-own-browsers)
-step-definitions-use-shared-context:`this.page`-comes-from-global-context
-NO-hardcoded-sensitive-data:all-URLs,credentials-use-env-variables
-non-implemented-scenarios-marked-with-`@pendiente`:at-individual-scenario-level
-single-scenario-execution:test-one-scenario-completely-before-moving-to-next

### 8.2 Final-Quality-Objective

Produce-high-quality+maintainable-Playwright-test-scripts-that:

-implement-Gherkin-scenarios-from-**${input:feature_name}**
-adhere-to-Page-Object-Model-design-pattern
-integrate-seamlessly-with-Playwright-framework-structure-in-**${input:playwright_folder}**
-correctly-automate-navigation+interactions-using-JSP-references-from-**${input:JSP_folder}**
-use-env-variables-for-all-sensitive-config(URLs,credentials,timeouts)
-include-appropriate-security-measures-to-prevent-hardcoded-sensitive-info
-provide-clear-documentation-for-secure-env-setup
-follow-established-browser-management-architecture-to-prevent-conflicts+duplicate-instances
