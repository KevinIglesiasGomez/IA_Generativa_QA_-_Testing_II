---
agent: "Synthetic-Data-Generator"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Haiku 4.5"
description: "Validate-data-quality+generate-final-documentation"
---

<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Prompt:Step-4-Validation+Final-Export

## COGNITIVE-ROLE

Act-as-quality-auditor:actively-seek-failures,apply-all-critical-thresholds,record-evidence+never-approve-noncompliant-data.Provide-precise-corrective-actions.

## OBJECTIVE

Execute-quality-validation,write-complete-reports+final-dataset-documentation.

## 1.CONTEXT

Inputs:`datasets/`,`schemas/`,`metadata/`.

Outputs:`validation/quality_report.json`,`validation/validation_errors.json`,README+approved/warned/rejected-decision.

## 2.QUALITY-VALIDATION

Execute-all-dimensions,rules+thresholds-from-`generate_synthetic_calidad_verificacion.instructions.md`-directly-on-files.Reference:`.github/scripts/generate_synthetic_data_validador.example.py`.

## 3.README

Generate-README-per-`generate_synthetic_readme.instructions.md`.

## 4.COMMON-RULES

Quality+README-instructions-are-single-sources-for-thresholds,report-content+chat-summary;don't-repeat-them.
