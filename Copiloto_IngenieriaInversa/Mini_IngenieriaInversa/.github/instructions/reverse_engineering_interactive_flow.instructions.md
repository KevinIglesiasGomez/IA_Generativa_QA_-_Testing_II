# Interactive-Flow-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-interactive-workflow-agent-must-follow-with-user-during-reverse-engineering-process.Process-is-incremental+requires-validation-at-each-stage.

---

## 1. GENERAL-WORKFLOW

### Phase-0-Project-Confirmation

Before-starting-any-analysis,agent-must:

1.**Ask-user-root-directory-path-of-project-to-analyze**+register-as-`<PROJECT_ROOT>`.First-mandatory-question-before-any-action.
2.Confirm-directory-exists+contains-`package.json`(or-equivalent).If-not-found,inform-user+ask-again.
3.Identify-project-technology(Angular,React,Vue,etc.)
4.Ask-user:
   -Is-there-prior-functional-documentation-to-compare?
   -Want-to-generate-**general-document**(complete-vision-with-all-stories-summarized)or-prefer-go-directly-to-document-**specific-story**?
   -If-chooses-general-document→ask:**In-what-mode?**
     -**Summary-Mode**:generates-complete-document-in-one-go,no-intermediate-approvals,with-each-story/epic-in-standard-summarized-format
     -**Complete-Mode**:generates-story-by-story-with-interactive-approval-at-each-step,with-detailed-documentation-of-views,modals,rules+exhaustive-functional-cases
   -If-chooses-specific-story→Which-module/story-want-to-document-first?
   -Is-there-any-preferred-template/format?

### Phase-1-Discovery

1.Explore-project-folder-structure
2.Identify-all-modules/functional-domains
3.For-each-module,**classify-as-EPIC-or-STORY**-applying-criteria-from-section-3.3-of-main-instructions(count-views,endpoints,profiles,sub-modules,estimated-cases+disconnected-flows-epic-if-≥2-criteria-exceed-threshold)
4.Present-module-map-to-user-with-classification(Epic/Story)
5.**AWAIT-APPROVAL**-before-continuing

### Phase-2-General-Document

**BEFORE-starting-analysis**,agent-must-mandatorily-ask-user-which-generation-mode-desires:

>**In-what-mode-want-to-generate-document?**
>-**Summary-Mode**-Generates-complete-general-document-in-one-go,no-intermediate-stops.Each-story/epic-documented-in-standard-summarized-format(description,routes,endpoints,functional-cases).No-approval-per-story-required.On-finishing,saves-file-directly.
>-**Complete-Mode**-Generates-document-story-by-story-with-interactive-approval-at-each-step.Includes-detailed-documentation-of-all-views,modals,business-rules+exhaustive-functional-cases.User-confirmation-expected-after-each-story-before-continuing.

**Summary-Mode**(no-interaction-per-story):
1.Analyze-general-architecture(root-routing,global-guards,profiles)
2.Analyze-all-functional-modules-in-single-reading-step
3.Generate-complete-document-in-one-go-with:header,architecture,profiles,all-stories/epics-summarized,global-services+endpoints,questions-table
4.Save-file-in-`<PROJECT_ROOT>/documentacion/Recovered_Backlog_<App>_Overview.md`
5.**AWAIT-FINAL-APPROVAL**+apply-corrections-if-any

**Complete-Mode**(interactive-per-story):
1.Analyze-general-architecture(root-routing,global-guards,profiles)
2.Generate-general-document-header(project-data,architecture,profiles)
3.**AWAIT-APPROVAL**-of-header
4.For-each-functional-module:
   a.Analyze-module-in-depth
   b.Present-**ONLY-functional-cases-table**-of-module-for-approval
   c.**AWAIT-APPROVAL**-of-functional-cases
   d.After-approval,generate-complete-story-summary-with-all-views,modals,endpoints+business-rules-functional-cases-in-exhaustive-table-format
5.Generate-global-services+endpoints-section
6.Generate-questions-table
7.**AWAIT-FINAL-APPROVAL**-of-general-document
8.Save-file-in-`<PROJECT_ROOT>/documentacion/Recovered_Backlog_<App>_Overview.md`

### Phase-3-Story-Documents

For-each-story-user-requests-to-detail:
1.Analyze-corresponding-module-in-depth
2.Read-ALL-relevant-files(components,services,models,templates)
3.**Create-module-directory**-before-generating-any-file:
   -Path:`<PROJECT_ROOT>/documentacion/M<number>-epic-<name>/`
   -Example:`M05-epic-talleres/`
   -If-directory-exists,continue-without-error
4.Present-**ONLY-identified-functional-cases-table**-for-approval
5.**AWAIT-APPROVAL**-of-functional-cases
6.After-approval,generate-complete-detailed-document-with-all-views,modals,business-rules,endpoints+functional-cases-in-exhaustive-table-format
7.Save-file
8.Register-questions-found-during-analysis

---

## 2. INTERACTION-PROTOCOL

### Individual-Proposal

Agent-NEVER-must-generate-multiple-stories-without-approval.Flow-is:

1.Analyze-ONE-complete-module(routes,guards,services,components)
2.Present-**ONLY-identified-functional-cases**-in-table-format-for-review+approval(NOT-complete-document)
3.Ask:"Approve-these-functional-cases?Any-corrections/additional-cases?"
4.If-approves→Generate-complete-document-with-all-documentation(exhaustive-functional-cases-table-with-detailed-"Then",routes,endpoints,rules,etc.)+save-file
5.If-rejects→Ask-what-to-adjust+regenerate-ONLY-functional-cases-table

### Guidance-Questions

When-code-is-ambiguous,agent-must-ask:
-"Found-endpoint-`/endpoint/{param}`-but-couldn't-determine-exact-payload.Have-that-info?"
-"Guard-`NombreGuard`-seems-to-validate-`condición`,but-alternative-flow-unclear-in-code.Can-confirm?"
-"Identified-these-states:[list].Any-missing/non-applicable?"

### User-Question-Format

>**CRITICAL-RULE**:In-approval-step,agent-shows-EXCLUSIVELY-functional-cases-table.Complete-document/any-other-section-NOT-shown-until-approval-received.

```
---
**VALIDATION-REQUIRED-[Story-XX-Name]**

Identified-functional-cases:

|#|Given|When|Then|
|---|------|--------|----------|
|1|[User-context+previous-state]|[Concrete-user-action]|[Observable-result]|
|2|...|...|...|
|N|...|...|...|

Once-functional-cases-approved,complete-document-with-all-documentation-will-be-generated.
Approve-these-functional-cases?Need-to-add,remove,correct-any?
---
```

---

## 3. AMBIGUITY-MANAGEMENT

### Golden-Rule

**If-code-doesn't-provide-enough-info-to-document-behavior-with-certainty,register-in-questions-table.**Don't-invent/assume.

### Questions-Table

Format:

|#|Area|Question/Doubt|
|---|------|-----------------|
|1|[Module]|[Specific-question]|

### When-to-Register-Question

-Backend-behavior-not-visible-in-frontend
-Server-side-validations-not-replicated-in-client
-Ambiguous-error-handling
-Unclear-business-rules-from-code-alone

---

## 4. EPIC-MANAGEMENT

### Epic-Identification

Apply-criteria-from-section-3.3-of-main-instructions.If-module-meets-2+-thresholds→EPIC.

### Epic-Decomposition-Process

When-classified-as-Epic:
1.Identify-independent-functional-flows-within-module
2.Propose-to-user-decomposition-into-sub-stories-with-descriptive-names
3.**AWAIT-APPROVAL**-of-proposed-decomposition
4.Generate-Epic-file-with:header,sub-story-map,shared-endpoints
5.Document-each-sub-story-independently-following-same-process

---

## 5. STATE-PERSISTENCE+COMPACTING

### State-Save-Points

-After-Phase-0(approved-discovery)
-After-each-approved-story
-Before-suggesting-`/compact`
-After-generating-each-file

### Compacting-Suggestions

Suggest-`/compact`-at:
-After-Phase-0-completion
-Each-3-4-approved-stories
-After-general-document-generation
-Before-complex-epic

See-context_management-instructions-for-complete-protocol.

---

## 6. APPROVAL-VALIDATION-FORMAT

At-each-approval-point,agent-MUST-present-metrics:

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
