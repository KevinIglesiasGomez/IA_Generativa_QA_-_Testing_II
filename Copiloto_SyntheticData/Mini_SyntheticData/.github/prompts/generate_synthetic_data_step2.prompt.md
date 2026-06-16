---
agent: "Synthetic-Data-Generator"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Sonnet 4.6"
description: "Define-generation-strategies+prepare-data-dictionaries"
---

# Prompt:Step-2-Schema+Generation-Strategies-Definition

## COGNITIVE-ROLE

Act-as-**data-architect**-with-systemic-thinking+optimization-orientation.Your-responsibility:design-most-efficient+coherent-generation-plan:select-optimal-strategy-for-each-field,model-entity-dependencies,guarantee-generation-order-respects-referential-integrity.Prioritize-existing-resource-reuse(workspace-dictionaries)-before-creating-new-ones.Present-design-decisions-clearly+request-confirmation-before-advancing.

## OBJECTIVE

Define-specific-generation-strategies-for-each-schema-field,prepare-necessary-data-dictionaries+optimize-generation-plan.

## 1.CONTEXT

In-this-step-must-analyze-schema-defined-in-Step-1+determine:
-Optimal-generation-strategy-for-each-field
-Necessary-data-dictionaries.Use-workspace-dictionaries-if-domain-compliant,otherwise-generate-new-dictionaries-using-Faker
-Entity-generation-order(dependencies)
-Value+scenario-distribution
-Reproducibility-configuration(seeds)

## 2.SCHEMA-ANALYSIS

### 2.1-Schema-Loading

```
Read:${input:output_directory}/schemas/schema.json
Read:${input:output_directory}/instructions/client_specific_data.instructions.md
Read:${input:output_directory}/metadata/generation_config.json
```

### 2.2-Dependency-Analysis

Determine-generation-order-based-on-relationships:

Analyze-dependencies+relationships+determine-generation-order

Rules:
-Entities-without-FK-generated-first
-Entities-with-FK-generated-after-their-references
-Detect-cycles(circular-relationships)
-Build-dependency-graph

**Present-to-user:**
```markdown
##Entity-Generation-Order

Based-on-detected-dependencies,entities-will-be-generated-in-this-order:

1.${entity_1}(no-dependencies)
2.${entity_2}(depends-on-${entity_1})
3.${entity_3}(depends-on-${entity_1},${entity_2})
...

Does-this-order-make-sense-for-your-domain?(y/n)
```

## 3.GENERATION-STRATEGY-ASSIGNMENT

For-each-field-of-each-entity,assign-most-appropriate-strategy.

### 3.1-Available-Strategies

**1.RANDOM(Controlled-random)**
Use:Numbers,booleans,random-selection
Parameters:seed,min,max,distribution
Example:age(18-80,normal-distribution-mean-35)

**2.PATTERN(Pattern-based)**
Use:Codes,identifiers-with-specific-format
Parameters:pattern_template,counters
Example:"CUST-{year:4}-{number:6}"→"CUST-2026-000001"

**3.DICTIONARY(Dictionary-based)**
Use-workspace-provided-dictionaries-if-relevant-for-domain.Otherwise-generate-new-dictionaries-using-Faker.
Use:Names,cities,countries,domain-words
Parameters:dictionary_name,locale
Example:first_name(Spanish-names-dictionary)

**4.CALCULATED(Calculated/Derived)**
Use:Fields-depending-on-other-fields
Parameters:formula,source_fields
Example:total=subtotal*(1+iva_rate)

**5.SEQUENTIAL**
Use:Auto-incremental-IDs,order-numbers
Parameters:start,increment
Example:id(1,2,3,4,...)

**6.UUID(Universal-unique-identifier)**
Use:Primary-keys,global-identifiers
Parameters:version(uuid4)
Example:550e8400-e29b-41d4-a716-446655440000

**7.FAKER(Faker-library)**
Use:Complex-realistic-data(emails,phones,addresses)
Parameters:faker_method,locale
Example:email()→juan.perez@example.com

**8.ENUM(Closed-value-list)**
Use:States,categories,fixed-options
Parameters:values,weights(optional)
Example:status["ACTIVE","INACTIVE","SUSPENDED"]-weights[70,20,10]

**9.DATE_RANGE**
Use:Dates,timestamps
Parameters:start_date,end_date,distribution
Example:registration_date(2020-01-01-to-2026-03-06)

**10.RELATED(Related-value)**
Use:Foreign-keys,inter-entity-relationships
Parameters:referenced_entity,referenced_field
Example:customer_id(references-customers.id)

### 3.2-Automatic-Assignment

For-each-field,automatically-determine-best-strategy.

### 3.3-User-Review

Present-assigned-strategies+allow-adjustments.

```markdown
##Assigned-Generation-Strategies

###Entity:${entity_name}

|Field|Type|Strategy|Parameters|
|-----|----|---------|-----------
|user_id|uuid|UUID|version:4|
|name|string|DICTIONARY|dict:nombres_es.json|
|email|email|FAKER|method:email,locale:es_ES|
|age|integer|RANDOM|min:18,max:80,distribution:normal|
|created_at|datetime|DATE_RANGE|start:2020-01-01,end:2026-03-06|
...

Adjustments-needed?(y/n)
```

## 4.DICTIONARY-PREPARATION

### 4.1-Identify-Needed-Dictionaries

List-all-fields-using-DICTIONARY-strategy.

### 4.2-Check-Workspace-Dictionaries

Search-available-dictionaries-in-workspace(`templates/diccionarios/`):
-nombres_es.json
-apellidos_es.json
-calles_es.json
-ciudades_provincias_es.json
-descripciones_seguros.json
-accidentes.json

**If-workspace-dictionaries-applicable-to-domain:**
-Copy-to-`${output_directory}/metadata/dictionaries/`
-Register-in-metadata

**If-not-applicable-or-missing:**
-Generate-new-dictionaries-using-Faker
-Save-to-`${output_directory}/metadata/dictionaries/`

### 4.3-User-Confirmation

```markdown
##Dictionary-Configuration

###Using-Workspace-Dictionaries:
-nombres_es.json(Spanish-names)
-apellidos_es.json(Spanish-surnames)
...

###New-Dictionaries-to-Generate:
-product_categories.json(200-values)
-company_types.json(50-values)
...

Proceed-with-this-configuration?(y/n)
```

## 5.SCENARIO-DISTRIBUTION-CONFIGURATION

Define-data-distribution-for-testing:

```
Scenario-Distribution:
-Normal-cases(happy-path):60%
-Boundary-cases:20%
-Exceptional/invalid-cases:20%

Adjust-distribution?(y/n)
```

## 6.ENRICHED-SCHEMA-GENERATION

Update:`${output_directory}/schemas/schema.json`-with:
-Assigned-strategies
-Strategy-parameters
-Generation-order
-Dictionary-references

## 7.STEP-COMPLETION

**User-message:**
```
STEP-2-COMPLETED-SUCCESSFULLY

Generation-strategies-defined+optimized.

Entities-in-generation-order:${num_entities}
Total-fields:${total_fields}
Strategies-assigned:${num_strategies}
Dictionaries-prepared:${num_dictionaries}

Next-step:We'll-generate-synthetic-data(Step-3)

Ready-to-continue?(y/n)
```
