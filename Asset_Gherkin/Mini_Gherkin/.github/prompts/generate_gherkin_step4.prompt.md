---
agent: "Gherkin-Scenario-Generator"
description: "Analyze-documentation+generate-BDD-use-cases"
model: "Claude Sonnet 4.6"
---

### Step-4:Use-Case-Extraction+BDD-Feature-Generation

Now,using-identified-document-type-**${input:document_type}**+complete-documentation-analysis(including-external-tool-data-when-available),complete-following:

1.Review-all-documents+identify-main-workflows,rules,use-cases.
2.**Integrate-external-tool-data**(OPCIONAL-only-if-available)-to-enrich-understanding+use-case-validation.
3.Cross-reference-with-system-code-available-in-workspace.
4.Write-`.feature`-file(in-**Cucumber-BDD**,in-**Spanish**)-for-each-main-functional-case,using-same-terminology-as-documents.
5.**MANDATORY**-For-each-generated-.feature-file-ensure-**review-quality+verification-instructions**-defined-in-corresponding-instruction-file+apply-all-defined-quality-assurance-criteria-BEFORE-proceeding-to-next-feature.NOT-advance-to-next-.feature-file-until-current-meets-ALL-quality+verification-criteria.This-is-crucial-to-ensure-effectiveness+maintainability-of-generated-features.
6.**MANDATORY**-Each-.feature-file-must-generate-**more-than-15-different-scenarios**-covering:
   -Positive+negative-flows
   -Boundary-cases
   -Business-rule-validations
   -Key-user-interactions
   -Form-validations
   6.1.**If-documentation-contains-User-Stories**,ensure-generate-scenarios-covering-ALL-acceptance-criteria-defined-in-each-story.Minimum-3-scenarios-per-story.Prioritize-quality+coverage-over-quantity,but-NOT-limit-to-few-scenarios-per-story-if-acceptance-criteria-requires-more.
   6.2.**If-documentation-contains-User-Stories**,scenarios-must-be-ordered-in-each-feature-by-user-story-ID-they-correspond-to.
7.**IMPORTANT**-NOT-limit-to-15-scenarios;if-use-case-requires,**generate-as-many-scenarios-as-needed-for-complete-coverage**.NOT-limit-to-simple-scenarios;include-complex-scenarios-reflecting-real-world-interactions.
8.**IMPORTANT-Sensitive-Data**:BDD-scenarios-NOT-contain-hardcoded-sensitive-data(credentials,NIFs,license-plates,phone-numbers,specific-rule-codes,etc.).Use-generic-references-like-"valid-credentials","valid-NIF","test-license-plate".Real-data-must-be-configured-in-`.env`-files.
9.**Save-.feature-files-in**:**${input:e2e_repo}**(only-.feature-files-in-this-directory)
10.**Create-comprehensive-INFORME_<fecha_hora>.md-file**(filename-must-include-creation-date+time,format-`YYYY-MM-DD_HH-mm-ss`)-in-root-of-**${input:e2e_repo}/**-following-ALL-documentation-requirements-defined-in-instructions.
   -Include-references-to-external-tool-sources-when-used
   -Document-any-external-validation/cross-references-applied
   -Clarify-technical-documentation-used-only-as-context
11.Apply-ALL-naming-conventions,file-organization+tagging-strategies-defined-in-instructions.

---
