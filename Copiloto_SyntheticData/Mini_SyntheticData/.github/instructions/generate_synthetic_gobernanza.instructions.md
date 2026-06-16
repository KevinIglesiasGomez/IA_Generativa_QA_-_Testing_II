### Objective

Establish-governance-guidelines,standard-formats+traceability-for-synthetic-datasets,ensuring-reuse,regulatory-compliance+complete-traceability.

## Data-Governance-Principles

**FUNDAMENTALS:**
-**Traceability**:Every-dataset-must-have-clear-origin,purpose+version
-**Reuse**:Datasets-must-be-self-descriptive+reusable
-**Compliance**:Adherence-to-GDPR,LOPD+sectoral-regulations
-**Quality**:Complete-metadata+documented-validations
-**Security**:Don't-include-real-sensitive-data-or-classified-info
-**Auditability**:Complete-generation+changes-history

## Standard-Output-Formats

**1.CSV**
-Standard:RFC-4180,Encoding:UTF-8,Delimiter:comma,Quoting:double-quotes-when-needed,First-line:column-names,Date:ISO-8601(YYYY-MM-DD)
-Use:Universal-exchange,Excel/DB-import
-Advantages:Simple,universal,readable
-Limitations:No-complex-types-support,no-embedded-metadata

**2.JSON**
-Standard:ECMA-404,Encoding:UTF-8,Arrays-for-collections
-Use:APIs,web-apps,hierarchical-data
-Advantages:Nested-structures,data-types,readable
-Limitations:Larger-size-than-other-formats

**3.JSON-Lines(JSONL/NDJSON)**
-One-valid-JSON-object-per-line,Newline(\n)-as-separator,No-commas-between-objects
-Use:Big-data,batch-processing,logs
-Advantages:Line-by-line-processable,memory-efficient
-Limitations:Less-human-readable

**4.Parquet**
-Binary-columnar-format,Efficient-compression(Snappy,GZIP),Embedded-schema,Strongly-typed-data
-Use:Data-lakes,analytics,big-data
-Advantages:Very-efficient,compressed,strong-typing
-Limitations:Requires-specialized-libraries,not-readable

**5.SQL-Script**
-Standard-SQL-INSERT-statements,Multi-RDBMS-compatible,Include-CREATE-TABLE,Optional-transactions
-Use:Test-database-population
-Advantages:Direct-to-DB,includes-schema
-Limitations:SQL-specific,can-be-large

**6.Excel(XLSX)**
-Office-Open-XML-format,Multiple-sheets,Preserved-data-types,Metadata-in-separate-sheet
-Use:Reporting,visual-analysis,documentation
-Advantages:Familiar-for-business-users,visual
-Limitations:Row-limit(1M),proprietary

## Directory-Structure

**Standard-Organization:**
```
synthetic-data/
├──README.md                          #General-documentation
├──schemas/                           #Schema-definitions
│  ├──schema.json                   #Main-schema
│  └──validation_rules.json         #Validation-rules
├──metadata/                          #Metadata+governance
│  ├──generation_config.json        #Generation-config
│  ├──data_dictionary.json          #Data-dictionary
│  └──lineage.json                  #Data-lineage
├──datasets/                          #Generated-datasets
│  ├──csv/,json/,jsonl/,parquet/,sql/,excel/
├──samples/                           #Sample-datasets(small)
│  └──sample_10_records.csv         #First-10-records
└──validation/                        #Validation-results
    ├──quality_report.json           #Quality-report
    └──validation_errors.json        #Detected-errors
```

## Mandatory-Metadata

**1.File:metadata/generation_config.json**
```json
{
  "dataset_info":{
    "name":"users_dataset",
    "version":"1.0.0",
    "description":"Synthetic-users-dataset-for-testing",
    "domain":"users",
    "purpose":"functional_testing",
    "created_date":"2026-03-06T10:30:00Z",
    "created_by":"synthetic-data-generator",
    "project":"project_name"
  },
  "generation_params":{
    "seed":42,
    "num_records":1000,
    "locale":"es_ES",
    "date_range":{"start":"2020-01-01","end":"2026-03-06"}
  },
  "quality_metrics":{
    "completeness":100.0,
    "validity":99.8,
    "uniqueness":100.0,
    "consistency":99.5
  }
}
```

**2.File:metadata/data_dictionary.json**
```json
{
  "entity":"User",
  "fields":[
    {
      "name":"user_id",
      "type":"uuid",
      "description":"User-unique-identifier",
      "required":true,
      "unique":true,
      "primary_key":true,
      "example":"550e8400-e29b-41d4-a716-446655440000"
    }
  ]
}
```

**3.File:metadata/lineage.json**
```json
{
  "source":{
    "type":"synthetic_generation",
    "generator":"qa_synthetic-data-generator",
    "version":"1.0.0",
    "base_schema":"schemas/schema.json",
    "instructions":"instructions/client_specific_data.instructions.md"
  },
  "transformations":[
    {"step":1,"operation":"generate_base_data","timestamp":"2026-03-06T10:30:00Z"}
  ],
  "dependencies":{"related_datasets":["roles_dataset"]}
}
```

## File-Naming

**Conventions:**
Format:{entity}_{variant}_{date}_{version}.{extension}

Examples:users_base_20260306_v1.csv

Components:entity,variant(optional),date(YYYYMMDD),version(vN),extension

## Dataset-Versioning

**Version-Schema:**
Semantic-Versioning:MAJOR.MINOR.PATCH

-MAJOR:Incompatible-schema-changes
-MINOR:Add-fields-or-data(backward-compatible)
-PATCH:Data-corrections-without-schema-changes

## Privacy+Compliance

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
