# Gherkin-Scenario-Generator

## Version
2.3.0

## Prefix

gherkin-generator

## Keywords

gherkin,bdd,cucumber,qa-automation,testing,escenarios,feature,behavior-driven-development,historias-usuario,jira

## Repository

https://github.com/xxxrepositories/ghb-cop-gherkin-generator.git

## Capabilities

-Analyze-functional-documentation-any-type(user-manuals,business-requirements,functional-specs,user-stories-in-CSV,etc.)+extract-relevant-use-cases-for-testing.
-Generate-`.feature`-files-in-Cucumber-BDD-format-written-in-Spanish,with-15+-scenarios-per-feature-covering-positive-flows,negative-flows,boundary-cases+business-validations.
-Apply-consistent-tagging-strategy-with-primary-tags(`@smoke`,`@regression`)+secondary-tags-by-functional-area+environment.
-Integrate-data-from-external-management-systems(Azure-DevOps,Jira/Confluence,SharePoint)-via-MCP-to-enrich-analysis-with-user-stories,epics+acceptance-criteria.
-Explore-web-applications-automatically-via-MCP-Playwright-to-identify-navigation-flows,forms+UI-behaviors.
-Identify+classify-input-document-type-automatically-to-adapt-scenario-generation-strategy.
-Generate-comprehensive-`README.md`-with-analysis-performed,domain-glossary,coverage-statistics+description-of-each-generated-feature.
-Verify-quality-of-each-`.feature`-file-before-delivery,checking-mandatory-Cucumber-criteria:Given-When-Then-structure,scenario-independence,declarative-language-use+absence-of-hardcoded-sensitive-data.
-Assign-tags-with-Jira-identifiers(`@ID-1234`)-when-input-documentation-user-stories-with-project-management-system-reference.

## Supported-Environments

Visual-Studio-Code-with-GitHub-Copilot,GitHub-Copilot-Workspace

## MCP-Servers

| Name            | Type   | Description                                                                                                                                                              |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mcp-playwright  | local  | Automated-web-app-exploration:navigation,form-interaction,screenshots+DOM-analysis-to-enrich-BDD-scenario-generation.                                                    |
| azure-devops    | remote | Connect-to-Azure-DevOps-organizations-to-retrieve-work-items,user-stories,epics,boards+project-documentation.                                                            |
| jira-confluence | remote | Access-Jira-projects+Confluence-instances-to-obtain-issues,user-stories,acceptance-criteria+functional-documentation-pages.                                              |
| sharepoint      | remote | Access-SharePoint-document-libraries+lists-as-functional+technical-documentation-source.                                                                                 |

## Dependencies

-https://github.com/xxrepositories/ghb-cop-gherkin-generator.git

## Additional-Requirements

-Visual-Studio-Code-1.96+-with-GitHub-Copilot-extension-installed+active.
-Account-with-GitHub-Copilot-access+permissions-to-use-Claude-Sonnet-4.6-model.
-For-MCP-Playwright-integrations:Node.js-18+-and-MCP-Playwright-server-installed-locally.
-For-external-system-integrations(Azure-DevOps,Jira,SharePoint):valid-access-credentials-to-corresponding-service+MCP-remote-server-accessible-from-work-environment.
-Input-documentation-must-be-available-locally-in-workspace-or-accessible-through-configured-MCP-server.

---

## File-Descriptions

### Agent

**`.github/agents/generate_gherkin.agent.md`**

Defines-main-copilot-agent.Establishes-name,description,AI-model(Claude-Sonnet-4.6),available-tools+agent-role-as-QA-Automation-Architect-expert-in-BDD.Describes-target-audience(QA-Engineers,Product-Owners,BDD-developers),working-language(neutral-Spanish),communication-tone+technical-restrictions.Orchestrates-complete-workflow-in-five-sequential-steps-referencing-each-corresponding-prompt.

### Prompts

**`.github/prompts/generate_gherkin_step0.prompt.md`**—Context+Project(required)

First-workflow-step.Defines-required-input-variables:documentation-path-to-analyze(`document_location`),output-repository-path(`e2e_repo`)+optional-variables-for-external-integrations(`project_reference`,`mcp_service`,`URL`,`username`,`password`).Establishes-agent-role-as-Business-Analyst-specialized-in-BDD+references-all-mandatory-quality-criteria.

**`.github/prompts/generate_gherkin_step1.prompt.md`**—Complete-Documentation-Analysis(required)

Second-step.Instructs-agent-to-exhaustively-read-all-functional-documentation-from-input-directory-as-primary-test-case-source,review-technical-documentation-only-as-architectural-context+cross-reference-between-documents-to-ensure-complete-understanding.BDD-scenarios-must-derive-exclusively-from-functional-documentation.

**`.github/prompts/generate_gherkin_step2.prompt.md`**—External-Tools-Integration(optional)

Third-step,executed-only-if-MCP-work-requested.Details-auto-detection-logic-for-external-service-type-from-project-reference-pattern,specific-query-flows-for-Azure-DevOps,Jira/Confluence,SharePoint+generic-URLs,and-complete-automated-web-app-exploration-flow-via-MCP-Playwright.If-no-MCP-service-available,agent-continues-with-local-documentation-only.

**`.github/prompts/generate_gherkin_step3.prompt.md`**—Document-Type-Identification(required)

Fourth-step.Classifies-input-document-into-predefined-categories(user-manual,business-requirements,functional-spec,technical-spec,test-plan,process-documentation,system-manual,tutorial,user-stories,or-other-proposed-category).Sets-`document_type`-variable-that-conditions-generation-strategy-in-next-step.

**`.github/prompts/generate_gherkin_step4.prompt.md`**—Use-Case-Extraction+BDD-Feature-Generation(required)

Fifth+final-step.Generates-`.feature`-files-in-Cucumber/Gherkin-in-Spanish-from-complete-analysis.Requires-minimum-15-scenarios-per-file-covering-positive+negative-flows,boundary-cases,business-validations+user-interactions.For-user-stories,requires-at-least-3-scenarios-per-story-with-defined-acceptance-criteria.Forbids-hardcoded-sensitive-data.Creates-comprehensive-`README.md`-in-output-repository-root+applies-all-quality-criteria-before-finalizing-each-file.

### Instructions

**`.github/instructions/generate_gherkin_standards.instructions.md`**

Defines-mandatory-Cucumber-standards+BDD-writing-best-practices.Includes-complete-tagging-strategy(primary-tags-`@smoke`+`@regression`,secondary-tags-by-environment+functional-area,Jira-identifier-tags),scenario-structure-with-Given-When-Then-pattern-in-Spanish,declarative-writing-principles+naming-conventions+file-organization.

**`.github/instructions/generate_gherkin_quality_verification.instructions.md`**

Establishes-mandatory-quality-assurance-criteria+review-checklist-to-pass-before-delivering-each-`.feature`-file.Covers-criteria-like:all-scenarios-executable,existence-of-at-least-one-`@smoke`-scenario-per-feature,test-data-independence,declarative-language-use,absence-of-unnecessary-line-breaks-between-steps+prohibition-of-non-standard-keywords-at-step-start(only-"Dado","Cuando","Entonces","Y"-allowed).

**`.github/instructions/generate_gherkin_readme.instructions.md`**

Specifies-structure+mandatory-content-of-`README.md`-file-to-generate-in-output-repository-root.Defines-five-mandatory-sections:documentation-analysis-performed,generated-feature-files-description,BDD-tags-used,domain-specific-terminology+coverage-statistics(number-of-features,scenarios+tags).
