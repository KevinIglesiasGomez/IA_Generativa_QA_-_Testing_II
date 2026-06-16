# Synthetic-Data-Generation-Copilot

## Description

GitHub-Copilot-generates-high-quality-synthetic-data-for-software-testing.Completely-application-independent+adaptable-to-any-business-domain.

## Key-Features

-**Functional-documentation-analysis**:Reads+analyzes-project-documentation-automatically(FLOW-A)
-**Application+data-independent**:Configurable-for-any-domain
-**3-workflows**:Functional-documentation,instruction-file,or-interactive-creation
-**Interactive+guided**:Step-by-step-conversation-with-validations+confirmations
-**High-quality**:Exhaustive-validations-in-6-quality-dimensions
-**Multiple-formats**:CSV,JSON,JSONL,SQL,Excel,Parquet
-**Complete-governance**:Metadata,lineage,traceability+automatic-documentation
-**GDPR-compliance**:Completely-fictional+safe-data
-**Reproducible**:Seed-usage-for-deterministic-generation
-**Client-template**:~40%-reduced-client-data-template-to-facilitate-use
-**Automatic-documentation**:Complete-README-generation-for-each-dataset-using-specific-template

## Architecture

```
.github/
├──agents/
│  └──generate_synthetic.agent.md                              #Main-agent(mode:"Synthetic-Data-Generator")
├──instructions/
│  ├──generate_synthetic_estandares_buenas_practicas.instructions.md  #Quality-standards+types
│  ├──generate_synthetic_gobernanza.instructions.md                   #Governance,formats+traceability
│  ├──generate_synthetic_calidad_verificacion.instructions.md         #Validations+quality-dimensions
│  └──generate_synthetic_readme.instructions.md                       #Template-for-dataset-README
├──prompts/
│  ├──generate_synthetic_data_step0.prompt.md  #Configuration+context
│  ├──generate_synthetic_data_step1.prompt.md  #Requirements-analysis(3-flows)
│  ├──generate_synthetic_data_step2.prompt.md  #Schema+strategy-definition
│  ├──generate_synthetic_data_step3.prompt.md  #Synthetic-data-generation
│  └──generate_synthetic_data_step4.prompt.md  #Validation+documentation
├──scripts/
│  ├──generate_synthetic_data_generador.example.py  #Python-generator-example(596-lines)
│  └──generate_synthetic_data_validador.example.py  #Python-validator-example(349-lines)
└──templates/
    ├──generate_synthetic_data_template.instructions.md  #Client-instruction-template
    └──diccionarios/                                     #Predefined-data-dictionaries
        ├──nombres_es.json,apellidos_es.json,calles_es.json
        ├──ciudades_provincias_es.json
        ├──descripciones_seguros.json,accidentes.json
```

### Cognitive-Roles-per-Step

Each-prompt-activates-specific-cognitive-profile-adapted-to-task-nature:

|Step|Cognitive-Role|Main-Capability|
|------|--------------|---------------------|
|Step-0|Data-specialist-consultant|Active-listening,client-orientation,requirements-capture|
|Step-1|Business-analyst/information-archaeologist|Cross-documentation-reading,data-model-inference|
|Step-2|Data-architect|Systemic-design,strategy-optimization,dependency-modeling|
|Step-3|Data-engineer|Reliable-execution,batch-processing,multi-format-export|
|Step-4|Data-quality-auditor|Quality-certification,problem-diagnosis,final-documentation|

Agent-maintains-**Data-Quality-Engineer**-base-profile,each-prompt-refines-role-for-specific-phase-context.

### Cognitive-Debt+Bias-Control

Main-agent-actively-supervises-bias-risks-each-specialized-role-introduces:

|Step|Bias-Risk|Applied-Control|
|------|----------------|------------------|
|Step-0|Complacency:accept-vague-requirements|Validate-precision-before-advancing|
|Step-1|Interpretation:add-undocumented-assumptions|Distinguish-facts-from-inferences+confirm-latter|
|Step-2|Overengineering:unnecessary-complexity|Justify-each-decision-in-concrete-requirement|
|Step-3|Blind-execution:implement-without-verifying|Review-schema-consistency-before-generating|
|Step-4|Confirmation:seek-success-instead-of-failures|Active-critical-stance-oriented-to-detect-problems|

Each-step-transition,agent-verifies:accumulated-cognitive-debt-absence(unresolved-ambiguities),info-consistency-with-previous-steps,blind-spots-new-role-can-detect-vs-previous.

## Instruction-Files

Copilot-uses-4-instruction-files-in-`.github/instructions/`:

1.**generate_synthetic_estandares_buenas_practicas.instructions.md**(210-lines)
   -Supported-data-types(primitive,specialized,compound)
   -Generation-strategies(random,templates,dictionaries,rules)
   -Data-distribution(60%-valid-normal,20%-boundary,20%-exceptional/negative)
   -Mandatory-pre+post-generation-validations

2.**generate_synthetic_gobernanza.instructions.md**(325-lines)
   -Standard-output-formats(CSV,JSON,JSONL,Parquet,SQL,Excel)
   -Traceability+reuse-principles
   -Metadata+lineage-structure
   -Regulatory-compliance(GDPR,LOPD)

3.**generate_synthetic_calidad_verificacion.instructions.md**(309-lines)
   -6-quality-dimensions-with-specific-thresholds
   -Metrics+validations-per-dimension
   -Global-scoring-system
   -Approval/rejection-criteria

4.**generate_synthetic_readme.instructions.md**(83-lines)
   -Template-to-generate-dataset-README
   -Structure-with-quality-metrics
   -Privacy+compliance-info
   -Usage-examples+configuration

### Client-Template

In-`.github/templates/`-template-clients-complete-to-define-schema:

-**generate_synthetic_data_template.instructions.md**(144-lines)
   -8-sections:basic-info,domain-description,entities+fields,relationship-map,critical-validations,data-distribution,special-requirements+configuration
   -Mandatory-fields-marked-with-`*`
   -Compact-table-format-for-field-definition
   -Quick-reference-of-data-types+common-constraints

### Predefined-Dictionaries

In-`.github/templates/diccionarios/`-6-Spanish-ready-to-use-dictionaries:

|File|Domain|
|---------|---------|
|`nombres_es.json`|Spanish-person-names|
|`apellidos_es.json`|Spanish-surnames|
|`calles_es.json`|Spanish-street-names|
|`ciudades_provincias_es.json`|Spanish-cities+provinces|
|`descripciones_seguros.json`|Insurance-sector-descriptions|
|`accidentes.json`|Accident+claim-types|

Copilot-prioritizes-these-dictionaries-when-client-domain-compatible.For-other-domains-generates-new-dictionaries-using-Faker-library.

### Example-Scripts

In-`.github/scripts/`-two-Python-reference-scripts:

-**generate_synthetic_data_generador.example.py**(596-lines):Reference-implementation-for-massive-data-generation-with-all-supported-strategies,multi-format-export+seed-management.
-**generate_synthetic_data_validador.example.py**(349-lines):Reference-implementation-for-6-quality-dimension-validation+report-generation.

## Workflow

### Step-0:Configuration+Context
-Collects-project-information
-Establishes-generation-parameters
-Creates-directory-structure
-Configures-output-formats

### Step-1:Requirements-Analysis
Copilot-supports-**3-different-flows**-according-starting-point:

-**FLOW-A**:**Functional-documentation-analysis**-Reads+analyzes-project-functional-documentation-automatically(user-manuals,requirements,specifications)-from-`documentation/`-directory-to-extract-entities,fields+business-rules
-**FLOW-B**:**With-existing-instruction-file**-Analyzes-previously-defined-client-instruction-file+requests-clarifications-if-missing-info
-**FLOW-C**:**Interactive-creation-from-scratch**-Creates-schema-through-step-by-step-guided-conversation-when-no-documentation-nor-instruction-file

All-flows-define-entities,fields,data-types,constraints,relationships+specific-business-rules

### Step-2:Schema+Generation-Strategies-Definition
-Assigns-optimal-generation-strategies-per-field(UUID,Faker,Dictionary,Pattern,etc.)
-**Prioritizes-existing-workspace-dictionaries**(`templates/diccionarios/`)-if-domain-compliant
-Generates-new-dictionaries-with-Faker-only-if-necessary
-Determines-generation-order-by-dependencies(graph-analysis)
-Configures-scenario-distributions(normal/boundary/exceptional)
-Generates-formal-JSON-schema-with-strategies

### Step-3:Data-Generation
-Executes-massive-batch-data-generation
-Applies-all-defined-strategies-per-field
-Maintains-referential-integrity-between-entities
-Exports-simultaneously-to-multiple-formats(CSV,JSON,SQL,etc.)
-Generates-10-record-samples-per-entity

### Step-4:Validation+Documentation
-Executes-exhaustive-validations-in-6-quality-dimensions
-Generates-detailed-quality-reports-with-metrics
-**Automatically-generates-dataset-README.md**-using-formal-template-defined-in-`readme.instructions.md`
-Updates-metadata-with-final-metrics+complete-lineage

## How-to-Use-Copilot

Copilot-supports-**3-workflows**-according-starting-point:

### FLOW-A:With-Project-Functional-Documentation

**Use-case**:Have-functional-documentation(manuals,requirements,specifications)-but-not-structured-instruction-file

1.**Organize-documentation**-in-`documentation/`-directory-in-workspace:
   -User-manuals,functional-requirements,functional-specifications,entity-relationship-diagrams

2.**Invoke-agent**-from-Copilot-Chat:
   -Open-Copilot-Chat-in-VS-Code
   -Select-**"Synthetic-Data-Generator"**-mode-in-agent-selector
   -Write-as-first-message:`I-have-functional-documentation-in-documentation/-directory`

3.**Agent-automatically**:
   -Reads-**all-available-functional-documentation**
   -Makes-**cross-references**-between-documents
   -Identifies-**document-type**(manual,specification,etc.)
   -Extracts-entities,fields,types+business-rules
   -**Requests-clarifications**-if-missing-critical-info
   -Generates-structured-instruction-file
   -Proceeds-with-data-generation

### FLOW-B:With-Existing-Client-Instruction-File

**Use-case**:Already-have-structured-instruction-file-or-want-to-regenerate-data

1.**Prepare-instruction-file**-using-template-available-at:
   `.github/templates/generate_synthetic_data_template.instructions.md`
   Template-optimized(~40%-shorter)-with-8-well-defined-sections-to-facilitate-use.

2.**Invoke-agent**-from-Copilot-Chat:
   -Select-**"Synthetic-Data-Generator"**-mode
   -Write:`Instruction-file:./config/my_client_data.instructions.md`

3.**Agent**:
   -Analyzes-instruction-file
   -Validates-info-completeness
   -**Requests-clarifications**-if-missing-critical-info
   -Confirms-analysis-before-proceeding
   -Generates-data-per-specifications
   -Executes-automatic-quality-validations
   -Creates-complete-dataset-README-documentation

### FLOW-C:Interactive-Creation-from-Scratch

**Use-case**:First-time-generating-data,without-documentation-nor-instruction-file

1.**Open-agent**-in-GitHub-Copilot-Chat:Select-**"Synthetic-Data-Generator"**-mode

2.**Agent-guides-interactively**-asking:
   -Project-name+business-domain
   -Data-purpose(testing,demo,development)
   -Needed-record-quantity
   -Preferred-locale+language
   -Desired-output-formats(CSV,JSON,SQL,etc.)
   -Output-directory
   -Advanced-configuration(optional):seed,distributions,date-range

3.**Define-schema-collaboratively**-field-by-field:
   -Needed-entities+priority
   -Each-entity-fields-with-specific-types
   -Detailed-constraints(min/max,patterns,enums)
   -If-each-field-required,unique-or-primary-key
   -Relationships+foreign-keys-between-entities
   -Domain-specific-business-rules

4.**Agent-automatically-generates**:
   -Client-instruction-file(structured)
   -Formal-JSON-schema-with-generation-strategies
   -Necessary-data-dictionaries
   -Data-in-all-requested-formats
   -Exhaustive-validations-with-reports
   -Complete-generated-dataset-README
   -Lineage+traceability-metadata

## Output-Structure

```
output_directory/
├──README.md                          #Complete-dataset+client-specs-documentation
├──schemas/
│  ├──schema.json                   #Formal-schema-with-generation-strategies
│  └──validation_rules.json         #Defined-validation-rules
├──metadata/
│  ├──generation_config.json        #Complete-generation-config
│  ├──data_dictionary.json          #Data-dictionary-per-entity
│  ├──lineage.json                  #Dataset-lineage+traceability
│  └──dictionaries/                 #Dictionaries-used-in-generation
├──datasets/
│  ├──csv/,json/,jsonl/,sql/,excel/,parquet/
├──samples/                           #10-record-samples-per-entity
└──validation/
    ├──quality_report.json           #Complete-quality-report(6-dimensions)
    └──validation_errors.json        #Identified-errors(if-any)
```

## Quality-Dimensions

Copilot-automatically-validates-6-quality-dimensions:

|Dimension|Validates|Threshold|
|-----------|------------|--------|
|**Completeness**|Required-fields-filled|≥99%|
|**Validity**|Correct-types+formats|≥99%|
|**Uniqueness**|PKs+unique-fields-no-duplicates|100%|
|**Consistency**|Field-coherence|≥95%|
|**Referential-Integrity**|Valid-FKs|100%|
|**Accuracy**|Realism+business-logic|Qualitative|

**Global-Quality-Score**:All-dimensions-average
-**≥98%**:Dataset-APPROVED
-**95-98%**:Dataset-APPROVED-with-warnings
-**<95%**:Dataset-REJECTED-requires-correction

## Generation-Strategies

Copilot-supports-10-generation-strategies:

1.**UUID**:Universal-unique-identifiers
2.**SEQUENTIAL**:Auto-incremental-sequences
3.**FAKER**:Realistic-data-via-Faker-library
4.**DICTIONARY**:Values-from-curated-dictionaries
5.**PATTERN**:Template-based(e.g:PROD-{year}-{number})
6.**ENUM**:Closed-value-lists
7.**DATE_RANGE**:Dates-in-range-with-distribution
8.**RANDOM**:Controlled-random-values
9.**RELATED**:Foreign-keys-to-related-entities
10.**CALCULATED**:Values-derived-from-other-fields

## Output-Formats

**CSV**:Universal,Excel,pandas|UTF-8-with-BOM|RFC-4180
**JSON**:APIs,web-apps|Pretty-print|Arrays-for-collections
**JSON-Lines**:Big-data,batch-processing|Stream-friendly|One-object-per-line
**SQL**:Direct-DB-load|Includes-CREATE-TABLE+INSERTs|MySQL,PostgreSQL-compatible
**Excel**:Manual-review,reports|Limit:<100K-records|Multiple-sheets
**Parquet**:Data-lakes,analytics|Snappy-compression|Columnar

## Privacy+Compliance

### GDPR-Compliance
-All-data-**completely-fictional**
-No-real-personal-data-used
-Generated-DNI/NIE/CIF-**invalid**
-Emails-in-fictional-domains(example.com)
-Phones-in-fictional-ranges(555-xxxx)
-Fictional-or-anonymized-addresses

### Mandatory-Disclaimer
All-datasets-include-clear-notice:
>**WARNING**:This-dataset-contains-synthetically-generated-artificial-data-for-testing+development-purposes.No-data-corresponds-to-real-people,organizations-or-events.

## FAQ

**How-does-functional-documentation-analysis-work(FLOW-A)?**
Copilot-automatically-reads-all-docs-from-`documentation/`-directory,identifies-type(manual,requirements,specifications),cross-references-between-them+extracts-entities,fields,types+business-rules.Generates-structured-instruction-file-without-manual-intervention.

**Can-I-regenerate-same-data?**
Yes.Use-same-**seed**-in-configuration.Data-will-be-identical.

**Need-more-fields-after?**
1.Edit-client-instruction-file
2.Add-new-fields
3.Re-execute-agent
4.Version-dataset(v1.1.0)

**Can-I-use-own-dictionaries?**
Yes.Place-them-in-`metadata/dictionaries/`-in-JSON-format+reference-in-generation-strategies.Copilot-prioritizes-existing-workspace-dictionaries-if-domain-relevant.

**What-if-validation-fails?**
1.Review-`validation/quality_report.json`
2.Identify-errors
3.Adjust-schema-or-instructions
4.Regenerate-data
