<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Mini-Synthetic-Data-Generation-Copilot

Token-reduced,feature-equivalent-version-of-parent-`.github`-copilot.Uses-compact-English,hyphenated-concepts,`+`-conjunctions+single-source-contracts-without-removing-behavior.

## Features

-3-input-flows:functional-documentation,existing-client-instructions,interactive-creation
-5-mandatory-steps:configure,model,plan,generate,validate/document
-10-generation-strategies+6-output-formats
-6-quality-dimensions,privacy/governance+reproducibility
-Script-based-generation/validation-without-loading-datasets-into-chat
-Token-economy-for-questions,confirmations,reports+tool-output

## Structure

```text
.github/
├── LICENSE
├── agents/generate_synthetic.agent.md
├── instructions/
│   ├── generate_synthetic_estandares_buenas_practicas.instructions.md
│   ├── generate_synthetic_gobernanza.instructions.md
│   ├── generate_synthetic_calidad_verificacion.instructions.md
│   └── generate_synthetic_readme.instructions.md
├── prompts/generate_synthetic_data_step{0..4}.prompt.md
├── scripts/
│   ├── generate_synthetic_data_generador.example.py
│   ├── generate_synthetic_data_generator2.example.py
│   ├── generate_synthetic_data_validador.example.py
│   └── generate_synthetic_data_validator2.example.py
└── templates/
    ├── generate_synthetic_data_template.instructions.md
    └── diccionarios/{nombres_es,apellidos_es,calles_es,ciudades_provincias_es,descripciones_seguros,accidentes}.json
```

## Roles+Bias-Control

|Step|Role|Mandatory-control|
|----|----|-----------------|
|0|Consultant|Resolve-ambiguity|
|1|Business-analyst|Separate-facts/inferences|
|2|Data-architect|Minimal-requirement-driven-complexity|
|3|Data-engineer|Cross-check-before-execution|
|4|Quality-auditor|Actively-seek-failures|

## Workflow

1.**Step-0**:collect-missing-project/config-values,apply-safe-defaults,create-output-structure+`generation_config.json`.
2.**Step-1**:analyze-functional-docs/client-file-or-interview-user;write-client-instructions,schema+validation-rules.
3.**Step-2**:assign-strategies,order-dependencies,prepare-dictionaries+confirm-plan.
4.**Step-3**:generate-by-script/batch,export-confirmed-formats,write-samples+lineage.
5.**Step-4**:validate-by-script,write-full-reports+README,decide-approved/warnings/rejected.

## Input-Flows

-**A Documentation**:functional-docs-are-primary;technical-docs-only-context;cross-reference+confirm-inferences.
-**B Existing-file**:use-`.github/templates/generate_synthetic_data_template.instructions.md`;validate-required-contract.
-**C Interactive**:collect-entities,fields,relationships,rules+special-cases-in-dependent-batches.

## Output

```text
output_directory/
├── README.md
├── schemas/{schema.json,validation_rules.json}
├── instructions/client_specific_data.instructions.md
├── metadata/{generation_config.json,data_dictionary.json,lineage.json,dictionaries/}
├── datasets/{csv,json,jsonl,sql,excel,parquet}/
├── samples/
└── validation/{quality_report.json,validation_errors.json}
```

## Quality

|Dimension|Approval|
|---------|--------|
|Completeness|≥99%|
|Validity|≥99%|
|Uniqueness|PK=100%,unique≥99%|
|Consistency|≥95%|
|Referential-integrity|100%|
|Accuracy|Qualitative|

Global-score:approved-≥98%;warnings-95-98%;rejected-<95%.

## Strategies

`UUID`,`SEQUENTIAL`,`RANDOM`,`PATTERN`,`DICTIONARY`,`FAKER`,`ENUM`,`DATE_RANGE`,`RELATED`,`CALCULATED`.

Default-scenarios:70%-normal,20%-boundary,10%-exceptional.

## Formats

CSV(RFC-4180),JSON(ECMA-404),JSONL,SQL,XLSX(<100K),Parquet(>10K-recommended).

## Privacy

Only-fictional-data.No-real-valid-identifiers,financial-data,personal-data-or-confidential-business-info.Use-example-domains+fictional-phone-ranges.Include-synthetic-data-disclaimer.

## Changelog

### v1.3.0-2026-06-19
-Synchronized-with-verbose-copilot
-GPL-3.0-only+Knowmadmood-Comunidad-QA-authorship
-Added-complete-scripts,dictionaries+client-template
-Added-token-economy+compact-single-source-rules
-Normalized-paths,70/20/10-distribution+report-aggregation

## License

GNU-General-Public-License-v3-only(`GPL-3.0-only`).Copyright-(C)-2026-Knowmadmood-Comunidad-QA.Redistributions+modifications-must-preserve-copyright,authorship+license-notices.See-[LICENSE](LICENSE).
