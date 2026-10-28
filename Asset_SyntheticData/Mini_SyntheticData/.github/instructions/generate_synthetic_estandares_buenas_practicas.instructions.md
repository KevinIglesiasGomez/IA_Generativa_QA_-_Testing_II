<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

### Objective

Define-standards+best-practices-to-generate-high-quality-synthetic-data-for-software-testing.

## Fundamental-Synthetic-Data-Principles

**MANDATORY-REQUIREMENTS:**
-Data-MUST-be-**realistic**+coherent-with-business-domain
-Data-MUST-maintain-**referential-integrity**-between-related-entities
-Data-MUST-NOT-contain-**real-sensitive-info**
-Data-MUST-be-**reproducible**(controlled-seed)
-Datasets-MUST-include-**complete-metadata**
-Data-MUST-cover-**normal,boundary+exceptional-cases**
-Data-MUST-comply-with-**GDPR**+data-protection-regulations

Quality-dimensions,thresholds+validations-source:`generate_synthetic_calidad_verificacion.instructions.md`.

## Supported-Data-Types

**Primitive-Types:**
-`string`,`integer`,`float`/`decimal`,`boolean`,`date`(YYYY-MM-DD),`datetime`(ISO-8601),`timestamp`,`uuid`

**Specialized-Types:**
-`email`(happy-path:no-special-chars-like-tildes/eñes;negative-cases:special-chars-for-validation-testing)
-`phone`,`url`,`ip_address`,`credit_card`(masked),`iban`,`dni`/`nif`(Spain-with-letter),`cif`(Spain-company),`nie`(Spain-foreigner),`postal_code`,`country_code`,`currency_code`

**Compound-Types:**
-`address`(complete:street,city,postal-code,country)
-`person`(personal-data:name,surnames,birth-date)
-`company`(business-data:name,CIF,address)
-`geolocation`(geographic-coordinates:lat,lon)

## Generation-Strategies

**1.Controlled-Random-Generation:**
-Create-parameter-controlled-random-data-generation-scripts
-Save-all-scripts-in-workspace-for-reuse
-Use-seed-for-reproducibility
-Apply-appropriate-distributions(normal,uniform,exponential,poisson)
-Respect-defined-ranges+limits

**2.Template-Based-Generation:**
-Use-predefined-patterns(e.g:"PROD-{number:5}")
-Apply-format-masks
-Combine-fixed+variable-elements

**3.Dictionary-Based-Generation:**
-Use-existing-`templates/diccionarios`-dictionaries-if-domain-relevant
-Use-curated-lists-of-real-values(names,cities,etc.)
-Combine-elements-from-multiple-dictionaries
-Maintain-cultural+geographic-coherence
-Save-newly-generated-dictionaries-in-workspace-for-reuse

**4.Rule-Based-Generation:**
-Apply-business-logic
-Maintain-field-relationships
-Calculate-derived-fields

## Data-Distribution

**Test-Scenarios:**
-**70%**-Valid-normal-cases(happy-path)
-**20%**-Boundary-value-cases
-**10%**-Exceptional/invalid-cases(for-negative-testing)

**Data-Variety:**
-Include-different-text-lengths(short,medium,long)
-Include-special-chars+unicode-when-appropriate
-Include-values-in-different-languages-if-applicable
-Include-recent,past+future-dates-according-context

## Data-Schema-Format

**Field-Definition:**
```json
{
  "field_name":{
    "type":"string",
    "description":"Field-description",
    "required":true,
    "unique":false,
    "constraints":{
      "min_length":3,
      "max_length":50,
      "pattern":"^[A-Z]{3}-[0-9]{4}$",
      "values":["option1","option2","option3"]
    },
    "generation_strategy":"pattern",
    "example":"ABC-1234"
  }
}
```

**Common-Constraints:**
-`min_length`/`max_length`-For-strings
-`min_value`/`max_value`-For-numbers
-`pattern`-Regular-expression
-`values`-Allowed-values-list(enum)
-`foreign_key`-Reference-to-another-entity
-`default`-Default-value
-`nullable`-Allows-null-values

## Best-Practices

**Correct:**
-Use-descriptive+consistent-field-names
-Document-each-field-with-clear-description
-Include-representative-examples
-Maintain-entity-relationships
-Validate-generated-data-against-schema
-Include-generation-metadata(date,version,seed)
-Use-identifiers-that-don't-collide-with-real-data

**Incorrect:**
-Use-real-personal-data
-Generate-real-IBANs,credit-cards-or-DNIs
-Include-confidential-info-in-examples
-Create-inconsistent-entity-relationships
-Ignore-business-constraints
-Generate-data-without-validation
-Omit-documentation

## Typical-Use-Cases

**Functional-Testing:**
-Valid-data-for-happy-path
-Data-covering-all-functionalities
-Moderate-volume(10-1000-records)

**Performance-Testing:**
-Large-data-volume(1M+-records)
-Realistic-data-simulating-production
-Representative-distribution

**Security-Testing:**
-Data-with-SQL-injection-attempts
-Data-with-XSS+malicious-scripts
-Data-with-problematic-special-chars

**Integration-Testing:**
-Data-respecting-inter-system-interfaces
-Data-with-all-necessary-relationships
-Synchronized-data-between-entities

**Demos+Training:**
-Realistic-but-fictional-data
-Data-illustrating-all-features
-Moderate+easy-to-understand-volume
