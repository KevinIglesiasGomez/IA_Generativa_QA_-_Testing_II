---
agent: 'qa_framework-setup'
tools: ['edit/createDirectory', "edit/editFiles", "runCommands", "search", "search/searchResults", "usages", edit/createFile]
description: "Generar Estructura de Playwright"
---

# Prompt: Generate-Playwright-Structure

## 1. PREREQUISITES+CONTEXT

### 1.1 Required-Instruction-Files
TECHNICAL-TRUTH-SOURCE:this-prompt-requires-follow-ALL-instructions-defined-in:
-**`playwright_structure.instructions.md`**:contains-ALL-technical-documentation,architectural-patterns,security-requirements,implementation-guides

CRITICAL:`playwright_structure.instructions.md`=ONLY-truth-source-for:
-folder+file-structure
-architecture-patterns(Browser-Factory,Page-Object-Model)
-Cucumber+Playwright-config
-security-requirements
-code-templates
-best-practices

SCOPE-RESTRICTION:this-prompt-generates-ONLY-framework-structure(NOT-real-BDD-implementations)

### 1.2 Input-Variables
-**${input:playwright_folder}**:project-folder-name
-**${input:project_bdd}**:folder-containing-existing-.feature-files
-**${input:environment_url}**:base-URL-for-test-environment
-**${input:username}**:username(s)-for-example-config(single/multiple-comma-separated)
-**${input:password}**:password(s)-for-example-config(single/multiple-comma-separated,corresponding-to-usernames)
-**${input:role}**:role(s)-for-users(optional-single/multiple-comma-separated/empty-if-no-roles-required)

### 1.3 Project-Context
Read-complete-prompt-before-instructions.Task:generate-ONLY-base-Playwright-automated-framework-structure

IMPORTANT:framework-uses-Cucumber-as-ONLY-test-runner

EXECUTION-FLOW-HIERARCHY:
1.user-executes-npm-command→calls-cucumber-js(NEVER-playwright-directly)
2.Cucumber-reads-.feature-files→parses-Gherkin-scenarios
3.Cucumber-executes-step-definitions→translates-Gherkin-to-JavaScript-actions
4.step-definitions-use-Page-Objects→pass-shared-context-`this.page`
5.Page-Objects-call-Playwright→perform-browser-automation-internally
6.Browser-Factory-manages-lifecycle→centralized-browser-creation/cleanup
7.Cucumber-generates-reports→JSON/HTML-reports(NOT-Playwright-reports)

CRITICAL:Playwright-used-ONLY-internally-by-Page-Objects(NEVER-called-directly-by-users/npm-scripts)

## 2. OBJECTIVES+CRITICAL-RESTRICTIONS

### 2.1 Main-Objective
Generate-ONLY-base-Playwright-automated-framework-structure.NO-create-real-tests,scenarios,app-specific-implementations

### 2.2 Explicit-Prohibitions
Consult-`playwright_structure.instructions.md`-section-2-for-complete-restrictions.Summary:

-ONLY-unique-example-files:NO-create-real-tests/app-specific-code
-ONLY-copy-.feature-files:NO-read,analyze,create-implementations-based-on-them
-NO-specific-pages:NO-create-LoginPage.js,HomePage.js,specific-page-classes
-NO-specific-steps:NO-create-LoginSteps.js,HomeSteps.js,specific-step-definition-files

### 2.3 Critical-Architecture-Requirements
BROWSER-FACTORY-PATTERN(MANDATORY):
-implement-`src/support/browserFactory.js`-for-centralized-browser-management
-ONLY-ONE-file(`common.steps.js`)-manages-browser-lifecycle-with-Before/After-hooks
-all-step-files-use-`this.page`-from-shared-context
-multi-browser-support:chromium,firefox,webkit

ENHANCED-CUCUMBER-CONFIG:
-scalable-step-loading:`'src/steps/**/*.js'`-pattern
-unique-report-generation:timestamp-based-naming
-automatic-directory-creation:screenshots,videos,JSON,HTML
-post-execution-feedback:handler-with-report-locations

CONFIG-SEPARATION(CRITICAL):
-`playwright.config.js`-NOT-USED:exists-ONLY-to-prevent-dependency-errors
-`browserFactory.js`-MANAGES-BROWSERS:all-creation-logic+launch-options
-`environmentLoader.js`-REQUIRED:centralized-env-config-loading

## 3. PROJECT-CONFIG

### 3.1 Environment-Info
-follow-ALL-context+resource-guides-defined-in-`playwright_structure.instructions.md`
-test-environment-base-URL:**${input:environment_url}**
-can-use-URL-to-verify-app-behavior+structure
-can-use-URL-to-verify-locators+actions-in-app

### 3.2 Credentials+URLs
May-have-single/multiple-user-role-credentials-for-app:
-username(s):**${input:username}**(config-via-env-variables-single/multiple-users)
-password(s):**${input:password}**(config-via-env-variables-passwords-corresponding-to-each-username)
-role(s):**${input:role}**(optional-config-via-env-variables-single/multiple-roles/no-roles)

NOTE:when-multiple-users-provided→must-be-comma-separated-in-input-variables+framework-must-configure-to-handle-multiple-credential-sets-for-different-test-scenarios.Roles-optional+may/may-not-be-required-depending-on-app-authentication-system

### 3.3 Security-Config
-CRITICAL:apply-ALL-security-requirements-from-`playwright_structure.instructions.md`-for-env-variable-configuration
-implement-security-best-practices-using-env-variables-for-all-config

### 3.4 Framework-Goals
-follow-Page-Object-Model(POM)-pattern-strictly-with-ONLY-ONE-example-file
-create-base-framework-structure-with-unique-example-files-for-future-test-development
-implement-Browser-Factory-Pattern-for-centralized-multi-browser-management
-clearly-document-shared-context-pattern-for-`this.page`-usage-in-step-files

## 4. IMPLEMENTATION-RULES

### 4.1 Folder-Structure
1.create-new-folder-in-workspace-root-directory-called-**${input:playwright_folder}**
2.use-Playwright-structure-instructions-to-configure-framework-structure-in-this-folder
3.implement-all-generated-code-exclusively-within-this-new-folder
4.store-ALL-outputs+generated-files-in-this-folder

### 4.2 NPM-Scripts+Config-Requirements
CRITICAL:implement-enhanced-npm-scripts+cucumber-config-as-defined-in-`playwright_structure.instructions.md`:

KEY-REQUIREMENTS:
-ALL-scripts-MUST-use-`--config cucumber.config.js`:ensures-enhanced-config-loads
-enhanced-cucumber.config.js:use-validated-template-from-instruction-file
-cross-browser-support:env-variables-for-browser-selection
-multi-env-support:ENV-variables-for-different-test-environments
-scalable-step-loading:auto-load-all-step-definition-files
-unique-report-generation:timestamp-based-report-naming
-enhanced-directory-structure:auto-create-all-necessary-directories

### 4.3 Language,Style+License-Requirements
-all-documentation,README-files,comments,user-facing-text-written-in-Spanish
-code-comments-natural+understandable(avoid-robotic/overly-technical-language)
-logs+error-messages(console.log,console.error)-clear,friendly,Spanish,NO-ICONS-NO-EMOJIS
-PROHIBITION:NO-icons/emojis-in-ANY-code-file(.js,.json,config-files)→only-allowed-in-README.md
-all-code-files-completely-free-of-visual-symbols,icons,emojis,decorative-characters
-project-license-must-be-GPLv3+author-field-in-package.json-must-be-"Knowmadmood"
-add-.env-to-.gitignore+include-appropriate-security-documentation-in-README

### 4.4 Final-Validations
-ensure-framework-works-end-to-end-with-appropriate-npm-scripts
-validate-Browser-Factory-implementation-prevents-multiple-browser-instances
-verify-enhanced-Cucumber-config-works-correctly-with-dry-run-execution
-validate-auto-step-loading:verify-`src/steps/**/*.js`-pattern-loads-all-step-files
-test-unique-report-generation:confirm-timestamp-based-report-names-prevent-overwrites
-validate-complete-directory-creation:ensure-all-report-directories-auto-created
-verify-post-execution-feedback:confirm-process.on('exit')-handler-provides-report-locations
-validate-playwright.config.js-exists-but-NOT-USED:must-exist-to-prevent-dependency-errors-but-not-executed-by-framework
-confirm-browserFactory.js-responsibility:all-browser-management-logic-centralized,completely-isolated-from-playwright.config.js
-test-config-separation:browser-creation-via-browserFactory-ONLY,playwright.config.js-serves-NO-functional-purpose

## 5. QUALITY-CRITERIA

### 5.1 Technical-Standards
Produce-high-quality+maintainable-Playwright-framework-structure-that:

FRAMEWORK-REQUIREMENTS:
-complete-base-framework-structure-with-only-unique-example-files
-adheres-to-Page-Object-Model-design-pattern-WITHOUT-base-classes/inheritance
-includes-browserFactory.js-in-src/support/+common.steps.js-for-centralized-browser-management
-includes-environmentLoader.js-in-src/support/-for-centralized-env-config-management
-uses-env-variables-for-all-sensitive-config
-includes-multi-browser-npm-scripts(chromium,firefox,webkit)-using-env-variables

### 5.2 Required-Documentation+Style
-all-documentation,README-files,comments-written-in-Spanish
-code-comments-use-natural+conversational-tone→avoid-robotic-language
-console-logs+error-messages-friendly+understandable
-PROHIBITION:NO-icons/emojis-in-ANY-code-file(.js,.json,config-files)→only-allowed-in-README.md-files
-all-code-files-completely-free-of-visual-symbols,icons,emojis,decorative-characters
-GPLv3-license-config-with-"Knowmadmood"-as-author-in-package.json
-clear-documentation-for-secure-env-setup
-document-shared-context-pattern-for-`this.page`-usage-in-step-files
-security-best-practices-documentation-for-credential-handling

### 5.3 Functionality-Validation

CRITICAL-VALIDATIONS:
-Cucumber-dry-run-passes:`npx cucumber-js --config cucumber.config.js --dry-run`-runs-without-errors
-enhanced-step-loading-works:verify-`'src/steps/**/*.js'`-pattern-auto-loads-ALL-step-definition-files
-support-file-integration:confirm-`'src/support/**/*.js'`-pattern-includes-all-support-files-automatically
-unique-report-generation:validate-timestamp-based-report-naming-prevents-overwriting-previous-reports
-complete-directory-creation:ensure-auto-creation-of-screenshots,videos,JSON,HTML-directories
-post-execution-feedback:verify-process.on('exit')-handler-provides-clear-report-location-info
-single-browser-lifecycle-manager:only-common.steps.js-contains-Before/After-hooks
-shared-context-pattern-works:step-files-use-`this.page`(never-create-browsers-directly)
-multi-browser-execution:scripts-work-with-BROWSER-env-variable-using-`--config cucumber.config.js`
-enhanced-worldParameters:verify-comprehensive-config-object-sharing-with-step-definitions
-end-to-end-validation:`npm install&&npm run test:dry-run`-succeeds
-scalability-validation:adding-new-step-files-requires-NO-config-changes
-playwright.config.js-NOT-USED-by-framework:exists-only-to-prevent-dependency-errors(NOT-functional-config)
-Browser-Factory-Pattern-enforced:ALL-browser-management-through-browserFactory.js-EXCLUSIVELY
-environmentLoader.js-validation:centralized-env-config-loading-works-correctly
-config-separation:playwright.config.js-serves-NO-functional-purpose,browserFactory.js-handles-ALL-browser-operations
-visual-feedback-validation:confirm-clear+friendly-console-output-during-framework-initialization
-error-handling-validation:verify-try-catch-blocks-provide-meaningful-error-messages
-code-style-compliance:ALL-code-files-completely-free-of-icons,emojis,decorative-characters
-all-CRITICAL-RESTRICTIONS-followed:no-violations-of-framework-scope,file-creation,architecture-requirements
