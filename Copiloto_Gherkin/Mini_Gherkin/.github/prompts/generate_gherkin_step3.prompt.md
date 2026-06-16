---
agent: "Gherkin-Scenario-Generator"
description: "Analyze-documentation+generate-BDD-use-cases"
model: "Claude Haiku 4.5"
---

### Step-3:Document-Type-Identification

After-completing-complete-documentation-review+optional-external-tools-integration,analyze-document-content-located-in-**${input:document_location}**.

Based-on-structure,content+language,determine-most-appropriate-document-type-among:

-`user_manual`
-`business_requirements`
-`functional_specification`
-`technical_specification`
-`test_plan`
-`process_documentation`
-`system_manual`
-`tutorial`
-`user_stories`
-_(or-suggest-new-more-appropriate-label-if-needed)_

Set-this-value-as-`${input:document_type}`

**IMPORTANT**-If-documentation-is-**CSV-with-User-Stories**,generate-all-necessary-BDD-scenarios-to-test-each-story,using-Jira-ID-as-tag+following-quality-assurance-criteria-defined-in-`generate_gherkin_quality_verification.instructions.md`.

---
