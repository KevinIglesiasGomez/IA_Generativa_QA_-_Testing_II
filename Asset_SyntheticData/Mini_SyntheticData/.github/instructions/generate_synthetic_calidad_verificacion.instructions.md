<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Quality-Verification:Mandatory-validations-for-synthetic-datasets

Every-synthetic-dataset-generated-must-comply-with-following-quality+verification-criteria-to-ensure-utility+reliability.

## Data-Quality-Dimensions

**1.COMPLETENESS**
Definition:Percentage-present-values-vs-expected
Metrics:%-required-fields-with-values,%-complete-records,null/empty-values-count
Thresholds:Critical:>99%-mandatory-fields|Acceptable:>95%-optional-fields|Unacceptable:<90%

**2.VALIDITY**
Definition:Conformity-with-business-rules+constraints
Validations:Correct-data-types,valid-formats(email,phone,etc.),values-within-allowed-ranges,regex-compliance,enum-values-in-allowed-lists
Thresholds:Critical:>99.9%|Acceptable:>98%|Unacceptable:<95%

**3.UNIQUENESS**
Definition:Absence-duplicates-in-unique-fields
Validations:Primary-keys-no-duplicates(100%),unique-fields-no-duplicates,unique-combinations-where-applicable
Thresholds:Critical:100%-for-PKs|Acceptable:>99%-unique-fields|Unacceptable:<98%

**4.CONSISTENCY**
Definition:Coherence-between-related-fields
Validations:Logical-dates(end_date>start_date),mathematical-relationships(subtotal+VAT=total),coherent-states(status=SENT→send_date-not-null),consistent-formats
Thresholds:Critical:>99%|Acceptable:>95%|Unacceptable:<90%

**5.REFERENTIAL-INTEGRITY**
Definition:Validity-entity-relationships
Validations:Foreign-keys-point-to-existing-records,bidirectional-relationships-coherent,respected-cardinalities(1:1,1:N,N:M)
Thresholds:Critical:100%|Acceptable:>99.5%|Unacceptable:<98%

**6.ACCURACY**
Definition:Realism+domain-coherence
Validations:Realistic-values-for-context,appropriate-distributions,cultural/geographic-coherence,applied-business-logic
Evaluation:Qualitative+manual-sampling

## Mandatory-Pre-Generation-Validations

**PRE-GENERATION-CHECKLIST:**
-☐Schema-completely-defined-in-schemas/schema.json
-☐All-fields-have-specified-data-type
-☐Required-fields-marked-as-required:true
-☐Unique-fields-marked-as-unique:true
-☐Constraints(min,max,pattern)-defined
-☐Entity-relationships-mapped
-☐Generation-strategies-assigned
-☐Data-dictionaries-available-if-needed
-☐Generation-config(seed,quantity)-defined
-☐Dataset-purpose-documented

## Mandatory-Post-Generation-Validations

**1.SCHEMA-VALIDATION:**
-All-schema-fields-exist-in-data
-No-extra-fields-not-defined-in-schema
-Field-names-match-exactly

**2.TYPE-VALIDATION:**
Verify-Integer,Float,String,Boolean,Date(YYYY-MM-DD),DateTime(ISO-8601),UUID(v4-format),Email(valid-format),Phone(valid-format),Enum(values-within-allowed-list)

**3.CONSTRAINT-VALIDATION:**
-Min/max-length-for-strings
-Min/max-value-for-numbers
-Pattern-regex-for-formats
-Enum-values-for-closed-lists
-Not-null-for-required-fields

**4.UNIQUENESS-VALIDATION:**
-Unique-primary-keys(100%)
-Unique-fields-no-duplicates
-Unique-combinations-where-applicable
-Duplicates-found-report

**5.REFERENTIAL-INTEGRITY-VALIDATION:**
-Valid-foreign-keys
-References-to-existing-records
-Bidirectional-navigability

**6.BUSINESS-RULES-VALIDATION:**
-Logical-dates(temporal-order)
-Correct-calculations(totals)
-Coherent-states
-Conditional-dependencies

## Quality-Report

Write-complete-report:`validation/quality_report.json`+Markdown-when-needed.Chat-only:global-result,per-dimension-metrics,counts+paths.

Human+machine-readable-sections:
-Executive-summary-with-key-metrics
-Validation-details
-Acceptance-checklist

Group-errors-by-rule,entity+field.Chat:count+max-3-examples/group.Store-all-occurrences:`validation/validation_errors.json`.

## Acceptance-Criteria

**APPROVED-DATASET:**
-Completeness:≥99%
-Validity:≥99%
-Uniqueness:100%-for-PKs,≥99%-for-unique-fields
-Consistency:≥95%
-Referential-integrity:100%
-Global-Quality-Score:≥98%

**DATASET-WITH-WARNINGS:**
-Completeness:95-99%
-Validity:95-99%
-Uniqueness:≥98%
-Consistency:90-95%
-Referential-integrity:98-100%
-Global-Quality-Score:95-98%
Action:Review-warnings+document-exceptions

**REJECTED-DATASET:**
-Any-dimension<90%
-Referential-integrity<98%
-Global-Quality-Score<95%
Action:Regenerate-dataset-correcting-errors

## Manual-Expert-Sampling

**Process:**
1.Select-random-sample-50-100-records
2.Manual-review-by-domain-expert
3.Verify-realism+coherence
4.Document-qualitative-findings

**Sampling-Checklist:**
-☐Names-sound-realistic
-☐Addresses-geographically-coherent
-☐Dates-make-logical-sense
-☐Amounts-reasonable
-☐States/flows-logical
-☐No-obvious-artificial-patterns

## Security+Privacy-Validation

**MANDATORY-CHECKLIST:**
-☐No-real-personal-data
-☐No-real-valid-DNI/NIE/NIF
-☐No-real-valid-IBAN
-☐No-real-credit-cards
-☐Emails-in-fictional-domains(example.com,test.com)
-☐Phones-in-fictional-ranges(555-xxxx)
-☐Fictional-or-anonymized-addresses
-☐No-real-confidential-business-info
-☐Synthetic-data-disclaimer-included
-☐GDPR-compliance-documentation-included

## Output-Format-Validation

**For-each-generated-format:**

CSV:
-☐UTF-8-encoding-with-BOM
-☐First-line-with-headers
-☐Proper-comma-delimiter
-☐Quoted-strings-with-special-chars

JSON:
-☐Valid-JSON-syntax
-☐UTF-8-encoding
-☐Proper-data-types

SQL:
-☐Valid-SQL-syntax
-☐Include-CREATE-TABLE
-☐Well-formed-INSERTS+proper-escaping

Excel:
-☐First-row-headers
-☐Preserved-types+consistent-dates
-☐Maximum-1M-rows

## Cross-Format-Validation

Same-record-count+values-across-formats;matching-MD5/SHA256-content-checksum;no-conversion-precision-loss.

## Corrective-Actions

On-failure:review-errors,classify-systematic/random,fix-schema-as-needed,regenerate-only-if-needed,revalidate-until-acceptance.Never-ignore-errors/warnings,manually-patch-data-without-regeneration,skip-validations-or-approve-broken-referential-integrity.

## README-Disclaimer

State-that-algorithmically-generated-data-can-remotely/coincidentally-match-real-combinations;similarity-is-unintentional.Synthetic-data-is-only-for-testing,development+training;never-for-real-person-decisions-or-authentic-data-use-cases.
