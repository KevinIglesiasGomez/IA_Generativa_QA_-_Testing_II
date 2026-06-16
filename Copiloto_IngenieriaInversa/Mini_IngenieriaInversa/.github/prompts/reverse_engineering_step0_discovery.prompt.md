---
agent: "reverse_engineering_analyst"
tools: ["search", "runCommands"]
description: "Step-0:Initial-project-discovery+scope-confirmation"
model: "Claude Sonnet 4.6"
---

# Prompt-Step-0:Discovery+Project-Context

## 0. INTERNAL-COGNITIVE-ARCHITECTURE

Before-starting-discovery,agent-executes-internally-following-cognitive-phases.NO-skip-phases-allowed.

### ROLE-A:Structure-Explorer
Objective:Map-complete-project-architecture.

-Identify-framework+base-technology
-Traverse-folder-structure-to-discover-modules
-Locate-key-files:routing,guards,configuration

### ROLE-B:Functional-Classifier
Objective:Classify-each-module-as-Epic-or-Story.

For-each-discovered-module:
-Count-views,endpoints,profiles+sub-modules
-Apply-threshold-criteria-from-section-3.3-of-main-instructions
-Assign-classification-with-justification

### ROLE-C:Security-Architect
Objective:Identify-all-access-control-mechanisms.

-Inventory-all-guards+conditions
-Map-guards-to-protected-routes
-Identify-user-profiles+permissions

### ROLE-D:Completeness-Validator
Objective:Verify-project-map-is-complete.

-All-modules-with-lazy-loading-covered?
-All-guards-identified?
-Shared-modules-affecting-transversally?

## Objective

Execute-initial-project-discovery-phase.Agent-explores-source-code-structure,identifies-technology,functional-modules+presents-complete-map-for-user-to-confirm-analysis-scope.

## Instructions

1.**Ask-user**:"What-is-root-directory-path-of-project-to-analyze?"
   -Register-response-as-`<PROJECT_ROOT>`
   -Verify-directory-exists+contains-`package.json`(or-equivalent)
   -If-not-found,inform-user+request-path-again
2.Read-`package.json`-to-identify:
   -Technical-project-name
   -Version
   -Main-framework+version
   -Relevant-dependencies(Ionic,Capacitor,NgRx,etc.)
3.Explore-`src/`-or-equivalent-folder-structure
4.Read-root-routing-to-discover-modules-with-lazy-loading
5.List-ALL-guards-found-in-project
6.Identify-user-profiles-from-authentication-code

## Expected-Output

Present-to-user:

```
## Project-Map

**Application**:[name]
**Technology**:[framework+version]
**Version**:[version]

### Discovered-functional-modules

|#|Module|Folder|Main-routes|Guards|Type|
|---|--------|---------|-------------------|--------|------|
|1|...|...|...|...|Epic/Story|

### Identified-user-profiles

|Profile|Associated-guard|Functionalities|
|--------|----------------|-----------------|

### Security-guards

|Guard|Type|Condition|
|-------|------|-----------|

**Questions:**
1.This-map-correct?Any-missing-module?
2.Want-to-generate-**general-document**(complete-vision-with-all-stories-summarized)or-prefer-go-directly-to-document-**specific-story**?
   -If-choose-**general-document**→continue-with-Step-1.
   -If-choose-**specific-story**→which-module-to-document?Continue-with-Step-2.
```

## State-Save+Compacting

On-completing-this-step+receiving-user-approval:
1.**Save-state**-in-`/memories/session/reverse_engineering_state.md`-with:PROJECT_ROOT,app-name,technology,complete-module-map,epic/story-classification,chosen-mode+next-step
2.**Suggest-`/compact`**-to-user-with-message:

```
---
**📦 COMPACTING-SUGGESTION**

Completed-project-discovery+state-saved.
-Session-memory-saved-state:✅
-Current-phase:Phase-0-completed
-Next-step:[Step-1-or-Step-2-based-on-choice]

Can-execute-`/compact`-to-free-context-before-continuing.
After-compacting,will-auto-recover-state.**No-info-lost.**
---
```

## Post-compact-Recovery

If-when-starting-this-step-context-seems-compacted(prior-summary):
1.Read-`/memories/session/reverse_engineering_state.md`
2.Confirm-recovered-state-with-user-before-continuing

## Content-Rules

-All-generated-text-must-use-complete-Spanish-spelling:ñ,accents(á,é,í,ó,ú),diaeresis(ü)
