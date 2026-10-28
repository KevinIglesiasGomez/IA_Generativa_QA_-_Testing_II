<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Client-Data-Template

Complete-`*`-sections;use-`N/A`-when-not-applicable.

## 1.Basic-Info*

|Field|Value|
|-----|-----|
|Project-name||
|Business-domain||
|Dataset-purpose||
|Contact/owner||

## 2.Domain-Description*

-Business-context:
-Processes-covered:
-Expected-test-use:

## 3.Entities+Fields*

### [Entity-1]

Description:

|Field|Type|Required|Unique|Constraints|Example|Description|
|-----|----|--------|------|-----------|-------|-----------|
||||||||

Primary-key:
Business-rules:

### [Entity-2]

Description:

|Field|Type|Required|Unique|Constraints|Example|Description|
|-----|----|--------|------|-----------|-------|-----------|
||||||||

Primary-key:
Business-rules:

#### Example-Dataset(Optional)

Provide-5-10-representative-records-or-path-to-existing-sample.

## 4.Relationship-Map

|Source|Target|Cardinality|FK|Rule|
|------|------|-----------|--|----|
||||||

## 5.Critical-Validations*

|Rule|Entity/field|Expected-result|Severity|
|----|------------|---------------|--------|
|||||

## 6.Data-Distribution(Optional)

Default:normal-70%,boundary-20%,exceptional-10%.

|Scenario|Percentage|Examples|
|--------|----------|--------|
||||

## 7.Special-Requirements(Optional)

-Privacy/security:
-Negative/security-cases:
-Geographic/cultural-coherence:
-Other:

## 8.Configuration(Optional)

|Parameter|Value/Default|
|---------|-------------|
|Records|Required|
|Locale|`es_ES`|
|Seed|`42`|
|Date-range|Last-5-years|
|Formats|CSV/JSON/JSONL/SQL/XLSX/Parquet|
|Output-directory||

## Notes

## Type-Reference

Primitive:`string`,`integer`,`float`,`decimal`,`boolean`,`date`,`datetime`,`timestamp`,`uuid`.
Specialized:`email`,`phone`,`url`,`ip_address`,`credit_card`,`iban`,`dni`,`nif`,`cif`,`nie`,`postal_code`,`country_code`,`currency_code`.
Compound:`address`,`person`,`company`,`geolocation`.

## Constraint-Reference

`min_length`,`max_length`,`min_value`,`max_value`,`pattern`,`values`,`foreign_key`,`default`,`nullable`,`required`,`unique`.
