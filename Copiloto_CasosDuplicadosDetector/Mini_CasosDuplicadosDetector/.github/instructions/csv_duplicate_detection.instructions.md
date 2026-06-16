### OBJECTIVE

Analyze+compare-2-CSVs-test-cases→detect-functional-duplicates→generate-detailed-report→enable-engineer-informed-delete-decisions-before-Jira-import

### CSV-CONTEXT

DUPLICATE-DETECTION-PROCESS-works-with-2-CSV-types:

1.CSV-EXPORTED-FROM-JIRA:
   -descriptive-test-cases,no-concrete-structure,already-in-Jira
   -fields:Issue-Key,Issue-ID,Summary
   -natural-language-description(no-Gherkin-structure)
   -represents-current-test-cases-in-system

2.CSV-WITH-GHERKIN-CASES:
   -structured-Gherkin-format,generated-by-gherkin_csv_import_XRAY-copilot
   -fields:Issue-Id,Test-Summary,Description,Gherkin-definition,Links
   -BDD-structure(Given-When-Then)
   -ready-to-import-to-Jira

### DUPLICATE-DETECTION-CRITERIA

DETECTION≠textual-similarity→DEEP-SEMANTIC-ANALYSIS-of-objective+functionality

MANDATORY-CRITERIA-TO-CONSIDER-DUPLICATE:

☑same-functional-objective:both-validate-same-functionality/system-behavior
☑same-execution-context:run-on-same-module/component/feature
☑same-preconditions:require-same-initial-system-state
☑same-main-actions:performed-actions-functionally-equivalent(different-wording-ok)
☑same-expected-results:verify-same-success-criteria

IMPORTANT:2-cases-can-be-worded-completely-different+still-be-duplicates

EXAMPLE:
-Jira-case:"Verify-system-prevents-save-without-completing-required-fields"
-Gherkin-case:"Scenario:System-prevents-save-when-missing-required-data"
→DUPLICATES:same-functional-objective(different-wording)

---

### DEEP-ANALYSIS-REQUIRED

FOR-EACH-Gherkin-CSV-case,perform-exhaustive-analysis:

1.INTENT-EXTRACTION:identify-main-test-case-objective
   -What-functionality-being-tested?
   -What-expected-system-behavior?
   -What-business-rule-being-validated?

2.COMPONENT-IDENTIFICATION:determine-module/component-belongs
   -review-Component-field-in-Gherkin-CSV
   -review-tags+Links
   -analyze-scenario-context

3.ACTIONS-MAPPING:translate-Gherkin-steps→functional-actions
   -Given=Preconditions
   -When=User-actions
   -Then=Expected-results

4.SEMANTIC-COMPARISON:compare-with-ALL-Jira-CSV-cases
   -search-conceptual-matches(not-literal)
   -consider-synonyms+alternative-expressions-for-same-idea
   -evaluate-if-test-same-functional-flow

---

### DUPLICATES-REPORT-STRUCTURE

GENERATED-REPORT-MUST-BE-Markdown(.md)-file-with-structure:

```markdown
# Duplicate Detection Report

**Analysis date**: [DATE]  
**Jira CSV analyzed**: [PATH]  
**Gherkin CSV analyzed**: [PATH]  
**Total cases in Jira CSV**: [NUMBER]  
**Total cases in Gherkin CSV**: [NUMBER]  
**Duplicates detected**: [NUMBER]  

---

## Executive Summary

[Brief description of main findings]

---

## Detected Duplicates

### Duplicate 1

**Jira CSV (Original)**
- **Key**: [Issue Key]
- **ID**: [Issue ID]
- **Line in CSV**: [Line number]
- **Title**: [Summary]

**Gherkin CSV (New - To import)**
- **Issue Id**: [Issue Id]
- **Line in CSV**: [Line number]
- **Title**: [Test Summary]
- **Component**: [Component]
- **Links**: [Links if exist]

**Similarity analysis**:
[Detailed explanation why considered duplicates, analyzing:
- Common functional objective
- Equivalent actions
- Similar expected results
- Any other relevant criteria]

**Recommendation**: [Delete Gherkin CSV case? Why?]

---

### Duplicate 2

[Repeat structure for each detected duplicate]

---

## Cases without Duplicates

**Total unique cases in Gherkin CSV**: [NUMBER]

[Optional: List of cases without duplicates, ready to import]

---

## Final Recommendations

[General recommendations about import process]
```

---

### INTERACTIVE-MODE

AFTER-report-generated,copilot-MUST-enter-INTERACTIVE-MODE-with-test-engineer

MANDATORY-INTERACTIVE-PROCESS:

1.PRESENT-REPORT:show-executive-summary+statistics

2.ITERATE-CASE-BY-CASE:for-each-detected-duplicate:
   -show-duplicate-info(both-cases)
   -show-similarity-analysis
   -ask-engineer:"Delete this case from Gherkin CSV to import? (yes/no/skip)"
   -wait-user-response
   -IF-"yes":mark-case-for-deletion
   -IF-"no":keep-case+justify-in-final-report
   -IF-"skip":pass-to-next-case-without-action

3.GENERATE-CLEAN-CSV:after-all-duplicates-reviewed,generate-new-Gherkin-CSV-without-marked-for-deletion-cases

4.GENERATE-FINAL-REPORT:update-report-with-decisions-taken+final-statistics

INTERACTION-FORMAT:

```
[COPILOT]
══════════════════════════════════════════════════════════════
🔍 DUPLICATE DETECTED #1 of 5
══════════════════════════════════════════════════════════════

📋 EXISTING CASE IN JIRA
   Key: INTA0001-556
   ID: 10748
   Line: 2
   Title: Integral validation detects incomplete elements and prevents validation

📋 NEW CASE (GHERKIN)
   Issue Id: TEST-042
   Line: 43
   Title: System does not allow validation when incomplete elements exist
   Component: fire-test-planning

💡 ANALYSIS
   Both cases verify system prevents validation when data incomplete.
   Different wording but identical functional objective: validate
   integral validation detects incomplete elements and blocks process.

❓ DELETE new case (TEST-042) from CSV to import?
   Answer: yes / no / skip

[USER]
[Wait user response]
```

---

### QUALITY-ASSURANCE-CRITERIA

MANDATORY-CHECKS:

☑ALL-cases-from-both-CSVs-analyzed
☑semantic-analysis(not-only-textual)
☑each-duplicate-has-clear+justified-explanation
☑report-includes-line-number-for-each-case-in-both-CSVs
☑report-includes-all-available-IDs(Key,Issue-Id,etc)
☑complete-titles-shown-for-both-cases
☑interactive-mode-allows-case-by-case-review
☑final-generated-CSV-correctly-excludes-deleted-cases
☑final-report-generated-with-decisions-taken
☑cases-user-decided-to-keep-NOT-modified
☑line-numbering-in-report-accurate+verifiable

TECHNICAL-VALIDATIONS:

☑clean-CSV-maintains-original-structure+format
☑no-encoding-errors-when-processing-CSVs
☑column-separator-correctly-detected
☑fields-with-quotes+line-breaks-handled-correctly
☑report-in-valid-Markdown-format
☑generated-CSV-importable-to-XRay-without-modifications

---

### FALSE-NEGATIVES-DETECTION

Copilot-MUST-be-CONSERVATIVE-in-duplicate-detection
Better:mark-as-possible-duplicate+let-engineer-decide
Than:omit-real-duplicate

SPECIAL-CASES-TO-CONSIDER:

-cases-with-different-detail-level-but-same-objective
-cases-testing-same-flow-with-different-input-data
-cases-validating-same-business-rule-in-different-contexts
-cases-with-different-priority-but-same-functionality
-cases-related-to-same-User-Story/epic

CRITERIA-TO-NOT-MARK-AS-DUPLICATE:

-cases-testing-different-flows(happy-path-vs-error-cases)
-cases-validating-different-aspects-of-same-functionality
-cases-with-different-critical-preconditions
-cases-mentioning-same-component-but-testing-different-functionalities
