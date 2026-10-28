---
agent: "Synthetic-Data-Generator"
tools: ["edit/createDirectory", "edit/editFiles", "search", "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection"]
model: "Claude Haiku 4.5"
description: "Configure-context+parameters-for-synthetic-data-generation"
---

<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Prompt:Step-0-Project-Configuration+Context

## COGNITIVE-ROLE

Act-as-data-consultant:understand-real-needs-before-technical-action,ask-clear-questions,offer-options-when-needed+redirect-off-topic-conversation.

## OBJECTIVE

Establish-complete-project-context,configuration+initial-synthetic-data-requirements.

## 1.PREREQUISITES

Follow:
-`.github/instructions/generate_synthetic_estandares_buenas_practicas.instructions.md`
-`.github/instructions/generate_synthetic_gobernanza.instructions.md`
-`.github/instructions/generate_synthetic_calidad_verificacion.instructions.md`

## 2.INPUTS

Collect-only-values-not-already-provided:

|Variable|Question/values|Default|
|--------|---------------|-------|
|`${input:project_name}`|Project-name|Required|
|`${input:data_purpose}`|Functional,performance,integration,demo,development,training,other|Required|
|`${input:business_domain}`|Business-domain|Required|
|`${input:num_records}`|Total-records;guide:100-1000-functional,10K-1M-performance|Required|
|`${input:locale}`|Locale,e.g.`es_ES`|`es_ES`|
|`${input:output_formats}`|CSV,JSON,JSONL,SQL,XLSX,Parquet|Required|
|`${input:output_directory}`|Output-directory|Required|
|`${input:client_instructions_file}`|Existing-file-or-empty-for-Step-1|Empty|
|`${input:seed}`|Reproducible-seed|`42`|
|`${input:scenario_distribution}`|Normal/boundary/exceptional|`70/20/10`|
|`${input:date_range}`|Date-range|Last-5-years|
|`${input:realism_level}`|High/medium/basic|High|

Apply-missing-optional-defaults-without-questioning;mention-once-in-summary.Required-fields-must-be-answered.Group-independent-same-block-questions;separate-only-when-answer-controls-next-questions.

## 3.VALIDATION

-Create-output-directory/base-structure-if-missing;verify-write-access
-If-nonempty,confirm-before-overwrite
-If-client-instructions-exist:read,validate-schema+confirm-correct-file
-Otherwise-create-next-step:`${input:output_directory}/instructions/client_specific_data.instructions.md`
-Present-one-table-with-all-inputs+confirm-before-writing

## 4.BASE-STRUCTURE

After-confirmation,create-governance-defined-directory-structure.

## 5.CONFIG

Create-`metadata/generation_config.json`:

```json
{
  "dataset_info":{"name":"${input:project_name}_dataset","version":"1.0.0","description":"Synthetic-dataset-for-${input:data_purpose}","domain":"${input:business_domain}","purpose":"${input:data_purpose}","created_date":"YYYY-MM-DDTHH:MM:SSZ","created_by":"synthetic-data-generator","project":"${input:project_name}"},
  "generation_params":{"seed":42,"num_records":0,"locale":"es_ES","scenario_distribution":{"normal":70,"boundary":20,"exceptional":10},"date_range":{"start":"YYYY-MM-DD","end":"YYYY-MM-DD"},"realism_level":"high"},
  "output_formats":[],
  "quality_metrics":{"completeness":null,"validity":null,"uniqueness":null,"consistency":null}
}
```

Replace-example-values-with-confirmed-inputs,including-custom-`${input:scenario_distribution}`.

## 6.RESULT

Briefly-return:status,`generation_config.json`-path,client-instructions-existing/pending+next-step.No-full-config-repeat.

## 7.COMMON-RULES

Apply-section-1-instructions;don't-repeat-them-in-response.
