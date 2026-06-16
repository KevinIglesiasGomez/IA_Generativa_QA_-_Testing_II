---
agent: "csv_duplicate_detector"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands", "memory"]
description: "Detect duplicate test cases between Jira CSV and Gherkin CSV, generate report and manage interactive deletion."
---

# Prompt: Detect and Manage Duplicates between Test Case CSVs

## 1. PREREQUISITES AND CONTEXT

### 1.1 Required Instruction Files

**ANALYSIS-CRITERIA-SOURCE**: Use following file as mandatory reference for detection criteria:

- `csv_duplicate_detection.instructions.md`: Defines semantic analysis criteria, report structure and interactive process.

### 1.2 Input Variables

- **${input:csv_jira_path}**: Path to CSV file exported from Jira with descriptive test cases (no Gherkin).
- **${input:csv_gherkin_path}**: Path to CSV file with Gherkin-structured test cases (output from gherkin_csv_import_XRAY copilot).
- **${input:output_report_path}**: Path where duplicates report will be saved in Markdown format.
- **${input:output_clean_csv_path}**: Path where clean Gherkin CSV will be saved (without user-confirmed duplicates).

### 1.3 Project Context

Expert-in:test-case-management+analysis,deep-QA-knowledge,Atlassian-tools(Jira,XRay)

PROBLEM-TO-SOLVE:test-engineer-has-existing-test-cases-in-Jira(exported-to-CSV)+new-Gherkin-structured-cases-ready-to-import. Before-import,critical-to-detect+eliminate-duplicates→avoid-redundancy+maintain-test-repository-quality.

MISSION:perform-deep-semantic-analysis→detect-cases-testing-same-functionality(different-wording-ok)→generate-detailed-report→help-engineer-decide-what-cases-to-delete-via-interactive-process.

---

## 2. ANALYSIS AND DETECTION PROCESS

### Step 1: Data Preparation and Loading

MANDATORY-BEFORE-ANY-ANALYSIS:

1.READ-INSTRUCTION-FILE:study-completely-`csv_duplicate_detection.instructions.md`→understand-analysis-criteria

2.LOAD+VALIDATE-JIRA-CSV:
   -read-file-at-**${input:csv_jira_path}**
   -detect-correct-separator(comma,semicolon,tab)
   -identify-relevant-columns:`Issue-Key`,`Issue-ID`,`Summary`
   -count-total-test-cases
   -validate-file-correctly-formatted

3.LOAD+VALIDATE-GHERKIN-CSV:
   -read-file-at-**${input:csv_gherkin_path}**
   -detect-correct-separator
   -identify-relevant-columns:`Issue-Id`,`Test-Summary`,`Description`,`Gherkin-definition`,`Component`,`Links`
   -count-total-test-cases
   -validate-file-correctly-formatted

4.PREPARE-DATA-STRUCTURES:
   -create-case-index-by-line-for-precise-reference
   -extract-key-info-from-each-case-in-both-CSVs
   -prepare-structures-to-store-detected-duplicates

---

### Step 2: Semantic Duplicate Analysis

FOR-EACH-case-in-Gherkin-CSV,perform-exhaustive-analysis:

#### 2.1 Gherkin Case Information Extraction

For-current-Gherkin-CSV-case,extract:
- **Issue-Id**: case-identifier
- **Line-in-CSV**: exact-line-number(for-reference)
- **Test-Summary**: case-title
- **Description**: case-description
- **Gherkin-definition**: complete-scenario-in-Gherkin-format
- **Component**: component/module-it-belongs
- **Links**: references-to-User-Stories/epics

#### 2.2 Intent and Objective Analysis

Perform-deep-analysis-to-understand:
- **What-functionality-being-tested?**: identify-main-objective
- **What-are-preconditions?**: extract-from-"Given"
- **What-actions-performed?**: extract-from-"When"
- **What-expected-as-result?**: extract-from-"Then"
- **In-what-context-executed?**: module,component,business-flow

#### 2.3 Duplicate Search in Jira CSV

For-current-Gherkin-CSV-case,compare-with-ALL-Jira-CSV-cases:

SEMANTIC-COMPARISON-CRITERIA:

1.TITLE/SUMMARY-ANALYSIS:
   -compare-`Test-Summary`(Gherkin)with-`Summary`(Jira)
   -search-conceptual-matches(not-only-textual)
   -consider-synonyms+alternative-ways-to-express-same-idea

2.FUNCTIONAL-OBJECTIVE-ANALYSIS:
   -both-cases-test-same-system-functionality?
   -validate-same-business-rule?
   -verify-same-expected-behavior?

3.CONTEXT-ANALYSIS:
   -belong-to-same-module/component?
   -execute-in-same-functional-context?
   -related-to-same-User-Story?(review-Links)

4.ACTIONS+RESULTS-ANALYSIS:
   -main-actions-equivalent?
   -expected-results-same?
   -preconditions-similar?

DUPLICATE-DETECTION:

IF-AT-LEAST-4-of-5-criteria-met,consider-as-possible-duplicate:
✓same-functional-objective
✓same-context/component
✓equivalent-preconditions
✓similar-main-actions
✓identical-expected-results

#### 2.4 Detected Duplicates Recording

For-each-detected-duplicate,record:
- **Jira-case-info**(original/existing):
  -Issue-Key
  -Issue-ID
  -Line-in-CSV
  -Complete-Summary
  
- **Gherkin-case-info**(new/to-import):
  -Issue-Id
  -Line-in-CSV
  -Test-Summary
  -Component
  -Links

- **Similarity-analysis**(detailed-justification):
  -explain-WHAT-they-have-in-common
  -justify-WHY-considered-duplicates
  -detail-criteria-met
  -mention-any-relevant-difference

- **Preliminary-recommendation**:
  -delete-Gherkin-case-recommended?(yes/no)
  -recommendation-justification

---

### Step 3: Duplicates Report Generation

After-all-cases-analysis-completed,generate-Markdown-report:

1.CREATE-REPORT-FILE-at-**${input:output_report_path}**

2.REPORT-STRUCTURE:
   ```markdown
   # Duplicate Detection Report
   
   **Analysis date**: [CURRENT-DATE]  
   **Jira CSV analyzed**: ${input:csv_jira_path}  
   **Gherkin CSV analyzed**: ${input:csv_gherkin_path}  
   **Total cases in Jira CSV**: [NUMBER]  
   **Total cases in Gherkin CSV**: [NUMBER]  
   **Duplicates detected**: [NUMBER]  
   
   ---
   
   ## Executive Summary
   
   [Main findings description]
   
   ---
   
   ## Detected Duplicates
   
   [For each duplicate, include complete info per format defined in instructions]
   
   ---
   
   ## Cases without Duplicates
   
   **Total unique cases in Gherkin CSV**: [NUMBER]
   
   [Optional list of unique cases]
   
   ---
   
   ## Final Recommendations
   
   [Recommendations about import process]
   ```

3.VALIDATE-REPORT:
   -verify-all-duplicates-documented
   -check-all-lines+IDs-correct
   -ensure-justifications-clear+complete

---

### Step 4: Interactive Mode with Test Engineer

INTERACTIVE-MODE-START:

1.PRESENT-REPORT-TO-USER:
   ```
   ═══════════════════════════════════════════════════════════════════
   📊 DUPLICATE ANALYSIS COMPLETED
   ═══════════════════════════════════════════════════════════════════
   
   ✓ Jira CSV: [PATH] → [N] cases analyzed
   ✓ Gherkin CSV: [PATH] → [M] cases analyzed
   ✓ Duplicates detected: [X]
   
   📄 Complete report generated at: [PATH]
   
   Next we'll review each duplicate so you decide whether to keep
   or delete the case from CSV to import.
   
   ═══════════════════════════════════════════════════════════════════
   ```

2.ITERATE-OVER-EACH-DETECTED-DUPLICATE:

   For-each-duplicate(numbered-1-to-X):
   
   ```
   ══════════════════════════════════════════════════════════════════
   🔍 DUPLICATE ANALYSIS #{N} of {TOTAL}
   ══════════════════════════════════════════════════════════════════
   
   📋 EXISTING CASE IN JIRA (Original)
      Key: [KEY]
      ID: [ID]
      Line in CSV: [LINE]
      Title: [SUMMARY]
   
   📋 NEW GHERKIN CASE (To import)
      Issue Id: [ISSUE_ID]
      Line in CSV: [LINE]
      Title: [TEST_SUMMARY]
      Component: [COMPONENT]
      Links: [LINKS]
   
   💡 SIMILARITY ANALYSIS
      [DETAILED JUSTIFICATION WHY DUPLICATES]
   
   ⚠️  RECOMMENDATION: [DELETE / KEEP]
      [RECOMMENDATION JUSTIFICATION]
   
   ══════════════════════════════════════════════════════════════════
   ❓ What do you want to do with the new case (GHERKIN)?
   
      → Type "yes" to DELETE it from CSV to import
      → Type "no" to KEEP it in CSV to import
      → Type "skip" to decide later
   
   Your answer:
   ```

3.PROCESS-USER-RESPONSE:
   -"yes"|"sí":mark-case-for-deletion→record-decision
   -"no":keep-case→record-decision+justification
   -"skip":no-action-now→mark-as-pending
   -ADDITIONAL-ALLOWED-RESPONSES:
     -"info":show-more-case-details
     -"gherkin":show-complete-Gherkin-scenario
     -"previous":go-back-to-previous-duplicate(if-possible)

4.CONTINUE-UNTIL-ALL-DUPLICATES-REVIEWED

5.DECISIONS-SUMMARY:
   ```
   ══════════════════════════════════════════════════════════════════
   ✅ REVIEW COMPLETED
   ══════════════════════════════════════════════════════════════════
   
   📊 DECISIONS SUMMARY:
      • Cases to delete: [N]
      • Cases to keep: [M]
      • Skipped/pending cases: [P]
   
   ⏭️  NEXT STEP: Generate clean CSV
   ══════════════════════════════════════════════════════════════════
   ```

---

### Step 5: Clean CSV Generation

IMPORTANT:this-step-executes-ONLY-AFTER-interactive-mode-completed

1.RELOAD-ORIGINAL-GHERKIN-CSV-from-**${input:csv_gherkin_path}**

2.IDENTIFY-LINES-TO-DELETE:
   -review-cases-marked-for-deletion-during-interactive-mode
   -verify-exact-line-numbers

3.GENERATE-NEW-CSV-WITHOUT-DELETED-CASES:
   -keep-identical-header
   -copy-all-lines-EXCEPT-marked-for-deletion
   -preserve-original-format,separators,encoding

4.SAVE-CLEAN-CSV-at-**${input:output_clean_csv_path}**

5.VALIDATE-GENERATED-CSV:
   -verify-line-count-correct
   -check-maintains-XRay-importable-format
   -ensure-cases-decided-to-keep-NOT-altered

---

### Step 6: Final Decisions Report

1.CREATE-FINAL-REPORT(can-be-same-initial-report-file,updated):

   Add-at-end-of-report-new-section:
   
   ```markdown
   ---
   
   ## Test Engineer Decisions
   
   **Review date**: [DATE]  
   **Reviewed by**: [USER]  
   
   ### Decisions Summary
   
   - **Total duplicates detected**: [N]
   - **Cases deleted from Gherkin CSV**: [M]
   - **Cases kept despite duplicate**: [P]
   - **Pending decision cases**: [Q]
   
   ### Decisions Detail
   
   #### Deleted Cases
   
   | Issue Id | Line | Title | Duplicate of (Jira) | Justification |
   |----------|------|-------|---------------------|---------------|
   | ...      | ...  | ...   | ...                 | ...           |
   
   #### Kept Cases (with duplicate)
   
   | Issue Id | Line | Title | Duplicate of (Jira) | Justification why kept |
   |----------|------|-------|---------------------|------------------------|
   | ...      | ...  | ...   | ...                 | ...                    |
   
   ### Final Generated CSV
   
   **Location**: ${input:output_clean_csv_path}  
   **Total cases**: [N]  
   **Ready to import to Jira/XRay**: ✓
   
   ### Recommended Next Steps
   
   1. Review clean CSV before import
   2. Backup current Jira CSV before importing
   3. Import clean CSV to XRay in Jira
   4. Validate cases imported correctly
   5. Archive this report for future reference
   ```

2.SAVE-UPDATED-FINAL-REPORT

---

## 3. QUALITY ASSURANCE CRITERIA

MANDATORY:apply-ALL-QA-criteria-defined-in-`csv_duplicate_detection.instructions.md`-to-guarantee:

✓exhaustive+semantic-analysis-of-all-cases
✓accurate-duplicate-detection-based-on-functional-objectives
✓complete-report-with-clear-justifications
✓smooth+professional-interactive-mode
✓valid+XRay-importable-clean-CSV
✓final-report-with-all-decisions-documented
✓no-alteration-of-cases-user-decided-to-keep
✓complete-traceability-of-all-decisions

---

## 4. SPECIAL CASES HANDLING

### Case 1: No duplicates detected

IF-no-duplicates-detected:
1.generate-report-indicating-"0-duplicates-detected"
2.inform-user-all-cases-unique
3.copy-original-Gherkin-CSV-to-clean-CSV-destination
4.recommend-proceed-with-direct-import

### Case 2: User requests review previous cases

During-interactive-mode,IF-user-asks-to-go-back:
1.allow-navigate-to-previous-duplicates
2.allow-change-previous-decisions
3.update-decisions-record-accordingly

### Case 3: User abandons interactive mode

IF-user-doesn't-complete-review:
1.save-report-with-detected-duplicates
2.DO-NOT-generate-clean-CSV(no-complete-decisions)
3.indicate-can-resume-process-later

### Case 4: Empty or no cases Jira CSV

IF-Jira-CSV-empty:
1.inform-no-cases-to-compare-with
2.all-Gherkin-cases-considered-unique
3.copy-complete-Gherkin-CSV-as-clean-CSV

---

## 5. FINAL DELIVERABLES

Upon-completing-entire-process,must-have-generated:

1.**Duplicates-Report**(${input:output_report_path}):
   -complete-duplicates-analysis
   -detailed-justifications
   -user-decisions
   -final-recommendations

2.**Clean-CSV**(${input:output_clean_csv_path}):
   -Gherkin-CSV-without-deleted-cases
   -identical-format-to-original
   -ready-to-import-to-XRay

3.**User-confirmation-message**:
   ```
   ══════════════════════════════════════════════════════════════════
   ✅ PROCESS COMPLETED SUCCESSFULLY
   ══════════════════════════════════════════════════════════════════
   
   📄 Complete report: [REPORT_PATH]
   📊 Clean CSV generated: [CLEAN_CSV_PATH]
   
   📈 FINAL STATISTICS:
      • Total cases analyzed (Jira): [N]
      • Total cases analyzed (Gherkin): [M]
      • Duplicates detected: [X]
      • Cases deleted: [E]
      • Final cases to import: [F]
   
   ✓ Clean CSV ready to import to Jira/XRay
   
   ══════════════════════════════════════════════════════════════════
   ```

PROCESS-COMPLETE!test-engineer-can-now-proceed-with-clean-CSV-import-to-Jira-confident-no-duplicates-exist
