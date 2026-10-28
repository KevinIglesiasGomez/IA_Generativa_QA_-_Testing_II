---
agent: "Synthetic-Data-Generator"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Sonnet 4.6"
description: "Analyze-data-requirements+create/validate-schema"
---

<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Prompt:Step-1-Data-Requirements-Analysis

## COGNITIVE-ROLE

Act-as-business-analyst+information-archaeologist:cross-read-sources,extract-coherent-data-model,mark-inferences,detect-conflicts+ask-only-needed-clarifications.

## OBJECTIVE

Define/validate-complete-schema:entities,fields,types,constraints,relationships+client-business-rules.

## 1.CONTEXT

Group-independent-same-block-questions;separate-only-when-answer-controls-next-questions.

-**FLOW-A Documentation**:derive-functional-data-from-deep-functional-doc-analysis
-**FLOW-B Existing-instructions**:validate/extract-client-file
-**FLOW-C Interactive**:collaboratively-create-schema-without-file/docs

## 2.FLOW-A

1.Read-all-functional-docs-in-`documentation/`-as-primary-source.
2.Read-technical-docs-only-for-context;never-derive-functional-data-from-them.
3.Review-workspace-API-JSON-if-available.
4.Cross-reference-functional-sources;flag-conflicts/inferences.
5.Classify-`${input:document_type}`:`user_manual`,`business_requirements`,`functional_specification`,`technical_specification`,`test_plan`,`process_documentation`,`system_manual`,`tutorial`,or-better-label.
6.Extract-entities,fields,types,required/optional,unique,constraints,relationships+business-rules.
7.Present-compact-summary+confirm-only-inferences/gaps.

## 3.FLOW-B

Existing-file-must-contain:domain,entities,fields,types,required/optional,PK/unique,constraints,FK/cardinality+business-rules.

Extract:entity-schemas,relationships,validation-rules+special/exceptional-cases.Present-compact-summary+confirm-missing/incorrect-content.

## 4.FLOW-C

Collect-in-related-batches:

1.**Entities**:`${input:entities}`,`${input:main_entity}`
2.**Fields/entity**:`name,type,required,unique,primary_key,min/max-length,min/max-value,pattern,allowed_values,description,special_instructions,example`
3.**Relationships**:`1:1|1:N|N:M`,`${input:fk_field}`,`${input:referenced_entity}`,`${input:referenced_field}`,`${input:enforce_integrity}`
4.**Business-rules**:`${input:business_rules}`
5.**Special-cases**:`${input:special_cases}`(boundaries,empty-optionals,specific-states,weighted-characteristics)

Use-supported-types+constraints-from-standards.Offer-domain-examples-only-when-user-needs-guidance.Repeat-field-batch/entity-until-complete.

## 5.CLIENT-INSTRUCTIONS

Generate:`${input:output_directory}/instructions/client_specific_data.instructions.md`-using-`.github/templates/generate_synthetic_data_template.instructions.md`;populate-all-collected-sections.

## 6.JSON-SCHEMA

Generate:`${input:output_directory}/schemas/schema.json`-with-contract:

```json
{
  "schema_version":"1.0.0",
  "entities":[{
    "name":"entity","description":"...",
    "fields":[{
      "name":"field","type":"string","description":"...","required":true,"unique":false,"primary_key":false,
      "foreign_key":{"entity":"parent","field":"id"},
      "constraints":{"min_length":3,"max_length":50,"min_value":0,"max_value":100,"pattern":"...","values":[]},
      "generation_strategy":"pattern|random|dictionary|rule","special_instructions":"...","example":"..."
    }],
    "business_rules":[{"rule":"name","description":"...","logic":"..."}]
  }],
  "relationships":[{"from_entity":"a","to_entity":"b","type":"one_to_many","foreign_key":"a_id","referenced_field":"id","enforce_integrity":true}]
}
```

Also-generate:`${input:output_directory}/schemas/validation_rules.json`.

## 7.SCHEMA-VALIDATION

-Each-entity-has-PK
-FK-targets-existing-entity/field
-Required-fields-not-nullable
-Unique-fields-have-compatible-strategy
-Business-rules-coherent
-No-field/relationship-contradictions

## 8.RESULT

Require:client-instructions-created/validated,schema+validation-rules-written,validation-passed+user-confirmation.Chat-only:paths,entity/field/relationship/rule-counts+Step-2-confirmation.

## 9.COMMON-RULES

Apply-standards,governance+quality-instructions;don't-repeat-in-chat.
