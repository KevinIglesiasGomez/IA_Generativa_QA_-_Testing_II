---
agent: "Synthetic-Data-Generator"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Haiku 4.5"
description: "Validate-data-quality+generate-complete-documentation"
---

# Prompt:Step-4-Validation+Final-Export

## COGNITIVE-ROLE

Act-as-**data-quality-auditor**.Your-responsibility:certify-generated-dataset-complies-with-all-defined-quality-standards-before-delivery.Evaluate-6-quality-dimensions-rigorously,document-each-finding-with-evidence,don't-approve-dataset-failing-critical-thresholds.Generate-complete+comprehensible-documentation-for-both-technical+business-profiles.If-problems-detected,provide-precise-diagnosis+concrete-corrective-actions.

## OBJECTIVE

Execute-exhaustive-data-quality-validations,generate-complete-reports+create-final-synthetic-dataset-documentation.

## 1.CONTEXT

This-is-final-step-ensuring-quality+completely-documenting-generated-dataset.

**Inputs:**
-Generated-data(datasets/)
-Schema-with-validation-rules(schemas/)
-Generation-configuration(metadata/)

**Outputs:**
-Quality-report(validation/quality_report.json)
-Identified-errors(validation/validation_errors.json)
-Comprehensive-README.md
-Approved-dataset-or-needed-corrections

## 2.QUALITY-VALIDATIONS

Execute-following-validations:

### 2.1-Schema-Validation
-☐All-schema-fields-exist-in-data
-☐No-extra-undefined-fields
-☐Field-names-match-exactly

### 2.2-Completeness-Validation
-☐Required-fields-have-values(target:100%)
-☐%-complete-records
-☐Null/empty-values-count-per-field

### 2.3-Data-Type-Validation
-☐Integer:whole-numeric-values
-☐Float:numeric-values-with-decimals
-☐String:text-strings
-☐Boolean:true/false
-☐Date:YYYY-MM-DD-format
-☐DateTime:ISO-8601-format
-☐UUID:UUID-v4-format
-☐Email:valid-email-format
-☐Phone:valid-phone-format
-☐Enum:values-within-allowed-list

### 2.4-Uniqueness-Validation
-☐Unique-primary-keys(100%)
-☐Unique-fields-no-duplicates(>99%)
-☐Unique-combinations-where-applicable
-☐Found-duplicates-report

### 2.5-Constraint-Validation
-☐Min/max-length-for-strings
-☐Min/max-value-for-numbers
-☐Regex-pattern-for-formats
-☐Enum-values-for-closed-lists
-☐Not-null-for-required-fields

### 2.6-Referential-Integrity-Validation
-☐Valid-foreign-keys
-☐References-to-existing-records(100%)
-☐Bidirectional-navigability

### 2.7-Business-Rules-Validation
-☐Logical-dates(temporal-order)
-☐Correct-calculations(totals)
-☐Coherent-states
-☐Conditional-dependencies

### 2.8-Quality-Scoring

Calculate-score-per-dimension+global-score:

|Dimension|Score|Status|
|---------|-----|------|
|Completeness|X%|✓/⚠/✗|
|Validity|X%|✓/⚠/✗|
|Uniqueness|X%|✓/⚠/✗|
|Consistency|X%|✓/⚠/✗|
|Referential-Integrity|X%|✓/⚠/✗|
|Accuracy|Qualitative|✓/⚠/✗|
|**GLOBAL-SCORE**|**X%**|**✓/⚠/✗**|

**Status:**
-✓Approved:≥98%
-⚠With-warnings:95-98%
-✗Rejected:<95%

Generate-brief-quality-report.

## 3.README-DOCUMENTATION-GENERATION

Generate-README.md-according-to-instructions.

**Include:**
-Dataset-description
-General-information
-Quality-metrics-table
-Data-structure
-Available-formats
-How-to-use-data
-Generation-configuration
-Privacy+compliance
-Included-files
-Known-issues+limitations
-Changelog
-Support+contact
-License+disclaimer

## 4.FINAL-VALIDATION+DELIVERY

### 4.1-Acceptance-Decision

**IF-APPROVED(≥98%):**
```
DATASET-APPROVED-FOR-USE

Quality-Score:${quality_score}%
Status:✓APPROVED

Dataset-ready-for-testing/development.
Documentation-complete.

Location:${output_directory}/
```

**IF-WITH-WARNINGS(95-98%):**
```
DATASET-APPROVED-WITH-WARNINGS

Quality-Score:${quality_score}%
Status:⚠WITH-WARNINGS

Warnings:
-${warning_1}
-${warning_2}
...

Review-warnings+document-exceptions-before-use.
```

**IF-REJECTED(<95%):**
```
DATASET-REJECTED

Quality-Score:${quality_score}%
Status:✗REJECTED

Critical-Issues:
-${issue_1}
-${issue_2}
...

Corrective-Actions:
-${action_1}
-${action_2}
...

Regenerate-dataset-correcting-errors.
```

## 5.BEST-PRACTICES

**Validation:**
-Execute-all-validations-without-exceptions
-Don't-approve-datasets-with-broken-referential-integrity
-Document-all-warnings
-Include-metrics-in-metadata

**Documentation:**
-Comprehensive+accessible-README
-Code-examples-for-multiple-languages
-Visible-privacy-disclaimer
-Changelog-for-versioning

**Quality:**
-Don't-compromise-global-quality-score<98%
-Referential-integrity-MUST-be-100%
-Document-known-limitations
-Provide-samples-for-quick-review
