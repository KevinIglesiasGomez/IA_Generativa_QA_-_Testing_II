# Quality-Verification-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-quality-verification-protocol-agent-must-execute-before-delivering-any-generated-document.Acts-as-mandatory-checklist-to-ensure-accuracy,completeness+coherence-of-functional-documentation-extracted-via-reverse-engineering.

---

## 1. PRE-DELIVERY-VERIFICATION-CHECKLIST

### 1.1 Structural-Verification

Before-presenting-document-to-user,agent-MUST-verify:

- [ ] All-index-links-point-to-existing-document-sections
- [ ] Markdown-format-valid+renders-correctly(tables,headers,lists)
- [ ] `---`-separators-present-between-main-sections
- [ ] Functional-cases-use-narrative-Given/When/Then-format(not-table)
- [ ] Functional-cases-appear-BEFORE-services+endpoints-sections
- [ ] Filename-nomenclature-follows-pattern-`Recovered_Backlog_<App>_[Overview|Epic|Story]_...`

### 1.2 Content-Verification

- [ ] All-documented-routes-exist-in-analyzed-source-code
- [ ] All-documented-endpoints-exist-in-some-code-service
- [ ] Documented-guards-correspond-to-real-project-classes
- [ ] Listed-enums+states-verifiable-in-source-code
- [ ] NO-invented-functionality-not-in-code
- [ ] Spanish-texts-have-complete-spelling(accents,ñ,ü)

### 1.3 Completeness-Verification

|Metric|Minimum-Threshold|
|---------|--------------|
|Documented-routes-vs-code-routes|100%|
|Documented-endpoints-vs-service-endpoints|100%|
|Main-views-with-documented-interface-states|100%|
|Stories-with-business-rules-table|100%|
|Functional-cases-per-main-view|Minimum-3(happy-path+load+error/empty)|
|Minimum-functional-cases-per-story(general-document)|5|

---

## 2. FUNCTIONAL-CASES-MINIMUM-COVERAGE

### 2.1 Mandatory-Functional-Cases-per-View

Each-main-view-MUST-have-at-least-these-functional-cases:

1.**Happy-path**:User's-main-successful-flow
2.**LOADING-state**:What-shown-while-loading-data(skeleton,spinner)
3.**NO-DATA-state**:What-shown-when-no-data/error
4.**WITH-DATA-state**:What-shown-with-available-data
5.**At-least-one-error/exception-case**:Network-error,failed-validation,denied-access

### 2.2 Additional-Recommended-Functional-Cases

-Navigation-between-views(entry+exit)
-User-actions-on-interactive-elements(buttons,forms,gestures)
-Modal-behavior(open,close,confirm)
-Alternative-flows(different-profiles,different-states)

---

## 3. INTER-DOCUMENT-COHERENCE

### 3.1 General-Document-vs-Detailed-Documents

-Routes-listed-in-general-document-MUST-match-detailed-document
-Endpoints-summarized-in-general-MUST-be-detailed-in-story-documents
-Story-names+numbering-MUST-be-consistent-between-both-levels
-If-detailed-document-updated,verify-if-general-needs-update

### 3.2 Epic-Documents-vs-Sub-stories

-Sub-story-map-in-epic-document-MUST-match-generated-documents
-Epic-shared-endpoints-MUST-appear-referenced-in-sub-stories
-`H<n>.<subnumber>`-numbering-MUST-be-sequential-without-gaps

---

## 4. TRACEABILITY-VALIDATION

### 4.1 Golden-Rule

**Everything-documented-must-be-verifiable-in-source-code.**If-behavior-can't-be-100%-confirmed,register-in-questions-table.

### 4.2 Elements-Requiring-Traceability

|Element|Code-Source|
|----------|-----------------|
|Routes|`*-routing.module.ts`,`*.routes.ts`|
|Guards|`*.guard.ts`|
|Endpoints|`*.service.ts`,`*.adapter.ts`|
|States/Enums|`*.enum.ts`|
|Business-rules|Logic-in-components,guards+services|
|UI-elements|`.html`-templates|

### 4.3 Anti-patterns-to-Avoid

-❌Document-inferred-functional-cases(not-verifiable-in-code)
-❌Assume-business-rules-not-expressed-in-source-code
-❌Extrapolate-backend-behavior-not-reflected-in-frontend
-❌Document-commented-code/apparently-unused
-❌Omit-routes,endpoints,states-considering-them-minor

---

## 5. CORRECTION-PROTOCOL

### 5.1 When-User-Requests-Corrections

1.Apply-requested-correction-to-current-document
2.Verify-if-correction-affects-other-already-generated-documents
3.Register-correction-as-pattern-for-future-stories
4.Confirm-with-user-correction-is-satisfactory

### 5.2 When-Inconsistencies-Detected

1.Inform-user-of-found-inconsistency
2.Propose-correction+await-approval
3.Apply-correction-in-all-affected-documents
4.Update-questions-table-if-inconsistency-can't-be-resolved

---

## 6. QUALITY-REPORT-FORMAT

When-presenting-document-for-approval,agent-MUST-include-metrics-summary:

```
---
**VALIDATION-REQUIRED**
Completed-analysis-of-[Story-XX-Name].
-Identified-routes:X/X-in-code(100%)
-Identified-endpoints:X/X-in-services(100%)
-Documented-functional-cases:X(minimum:Y)
-Views-with-interface-states:X/X(100%)
-Registered-business-rules:X
-Registered-questions:X

Approve-this-story?Need-adjustments?
---
```

---

## 7. SPANISH-SPELLING-VERIFICATION

### 7.1 Mandatory-Rule

ALL-generated-.md-file-content-MUST-use-complete-Spanish-spelling:
-ñ(eñe)
-Accents:á,é,í,ó,ú
-Diaeresis:ü
-All-Spanish-language-chars

### 7.2 Restriction-Scope

"Without-accents/special-chars"-restriction-applies-EXCLUSIVELY-to:
-Filenames-ONLY

NEVER-applies-to:
-File-content
-Document-text
-Tables
-Descriptions
-Functional-cases

### 7.3 Verification-Examples

✅CORRECT:
-Filename:`Recovered_Backlog_App_Historia_Gestion.md`
-Content:"El-usuario-**accede**-a-la-**página**-de-**gestión**"

❌INCORRECT:
-Filename:`Recovered_Backlog_App_Historia_Gestión.md`(accent-in-filename)
-Content:"El-usuario-accede-a-la-pagina-de-gestion"(no-accents-in-content)

---

## 8. FINAL-DELIVERY-CHECKLIST

Before-marking-document-as-complete:

- [ ] Structural-verification-passed
- [ ] Content-verification-passed
- [ ] Completeness-verification-passed
- [ ] Traceability-validation-passed
- [ ] Inter-document-coherence-verified
- [ ] Spanish-spelling-verified(content-WITH-accents,filenames-WITHOUT)
- [ ] Quality-metrics-calculated+documented
- [ ] User-approval-received
