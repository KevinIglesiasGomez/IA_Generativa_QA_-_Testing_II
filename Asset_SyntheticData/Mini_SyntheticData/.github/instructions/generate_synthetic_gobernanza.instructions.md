<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

### Objective

Define-governance,standard-formats+traceability-for-reusable,compliant+auditable-synthetic-datasets.

## Governance-Principles

-**Traceability**:clear-origin,purpose+version
-**Reuse**:self-descriptive+reusable
-**Compliance**:GDPR,LOPD+sector-rules
-**Quality**:complete-metadata+documented-validation
-**Security**:no-real-sensitive/classified-data
-**Auditability**:generation+change-history

## Output-Formats

|Format|Minimum-contract|Use|
|------|----------------|---|
|CSV|RFC-4180,UTF-8,header,ISO-8601-dates|Exchange/Excel/DB|
|JSON|ECMA-404,UTF-8,array/collection|APIs/hierarchical-data|
|JSONL|One-JSON-object/line|Batch/large-volume|
|Parquet|Columnar,embedded-schema,compression|Analytics/data-lakes|
|SQL|`CREATE TABLE`+`INSERT`,optional-transaction|RDBMS-load|
|XLSX|Sheet/entity+metadata-sheet;practical-max-100K-records|Manual-review|

## Directory-Structure

```text
synthetic-data/
├── README.md
├── schemas/{schema.json,validation_rules.json}
├── metadata/{generation_config.json,data_dictionary.json,lineage.json,dictionaries/}
├── datasets/{csv,json,jsonl,parquet,sql,excel}/
├── samples/sample_10_records.csv
└── validation/{quality_report.json,validation_errors.json}
```

## Mandatory-Metadata

|File|Required-content|
|----|----------------|
|`metadata/generation_config.json`|Identity,version,purpose,project,UTC-date;seed,volume,locale,date-range,distribution,formats;quality-metrics|
|`metadata/data_dictionary.json`|Per-entity/field:name,type,description,required,unique,PK/FK,constraints,rules,example|
|`metadata/lineage.json`|Generator+version,source-schema+instructions,UTC-timestamped-transformations,dependencies|

All-must-be-valid-JSON.Use-generated-instructions-path:`instructions/client_specific_data.instructions.md`.

## File-Naming

`{entity}_{variant}_{YYYYMMDD}_vN.{extension}`;keep-singular/plural-consistent.

## Dataset-Versioning

Semantic-Versioning:`MAJOR.MINOR.PATCH`.
-MAJOR:incompatible-schema-change
-MINOR:backward-compatible-fields/data-added
-PATCH:data-fix,no-schema-change

## GDPR+Privacy

-All-personal-data-fictional;no-identifiable-real-people
-No-real-valid-DNI/NIE/CIF,IBAN-or-cards
-Example/test-email-domains+identifiably-fictional-phone-ranges

## README

Generate-per-`generate_synthetic_readme.instructions.md`,single-source-for-sections+content.

## Multi-Format-Export

Generate-only-user-confirmed-formats.Recommend-Parquet->10K-records;XLSX-only-<100K.All-formats-must-contain-same-data;verify-integrity-with-MD5/SHA256-checksums.

## Change-History

Record-version,change,responsible+timestamp.
