---
agent: "ui_mapper"
tools: ["search", "read/readFile"]
description: "Step-1:Complete-screens-tree-construction,routes-extraction-from-navigation-system(React-Router/Angular-Router/Vue-Router/GoRouter),navigation-hierarchy+initial-screen-complexity-classification"
model: "Claude Sonnet 4.6"
---

# Step-1:Screen-Detection+Navigation-Tree

## 0. INTERNAL-COGNITIVE-ARCHITECTURE

### ROLE-A:Routes-Cartographer
**Objective:**Extract-complete-app-routes-map.
-Read-project-routes-files|Build-tree-with-parent/child-routes|Identify-dynamic-parameters,protected-routes+lazy-loading

### ROLE-B:Views-Identifier
**Objective:**Associate-each-route-with-its-main-view-component.
-For-each-route,find-assigned-component|Verify-it-exists|Determine-view-type:screen,modal,tab,drawer

### ROLE-C:Complexity-Classifier
**Objective:**Estimate-each-screen-complexity-before-detailed-analysis.
-Count-interactive-elements-in-template|Detect-sub-views|Classify-per-`ui_mapper_reference_tables.instructions.md`-section-6-criteria

### ROLE-D:Scope-Validator
**Objective:**Confirm-with-user-screens-subset-to-process.
-Present-complete-tree-with-classifications|Identify-screens-in-Step-0-defined-scope|Detect-duplicates|Propose-logical-order

---

## 1. PREREQUISITES

Step-0-must-be-completed-with:
-`<PROJECT_ROOT>`-or-`<APP_URL>`-confirmed
-Project-framework-identified
-Operation-mode-defined(static-or-dynamic)
-Analysis-scope-defined

---

## 2. STEP-INSTRUCTIONS

### Phase-1-Routes-system-reading

**If-Static-mode(React/Next.js)**:
-Search-files-with-patterns:`<Route-path=`,`createBrowserRouter`,`<Routes>`,`/pages/`(Next.js)
-For-Next.js:file-system-in-`/pages/`-or-`/app/`-already-defines-routes-directly
-Build-routes-tree-with-complete-path

**If-Static-mode(Angular)**:
-Search-`app-routing.module.ts`+all-`*-routing.module.ts`-files
-Read-each-file's-`Routes[]`-array
-Build-routes-tree-with-resolved-lazy-loading

**If-Static-mode(Vue/Nuxt)**:
-Search-`router/index.js`-or-`router/index.ts`
-For-Nuxt:analyze-`/pages/`-directory
-Extract-routes-array-with-assigned-components

**If-Static-mode(React-Native)**:
-Search-navigation-files-in-`/navigation/`-or-`/screens/`
-Identify-Stack,Tab+Drawer-navigators
-Each-Screen-within-navigators-is-a-screen

**If-Static-mode(Flutter)**:
-Search-`GoRouter`,`MaterialApp-routes`-or-`Navigator`-configuration
-Extract-routes-list+associated-widgets

**If-Dynamic-mode**:
-Analyze-current-page-DOM-to-identify-internal-navigation-links
-Record-accessible-routes-from-current-page
-Document-tree-only-includes-discovered-routes

**If-Dynamic-Mobile-mode(Appium/Android/iOS-Jetpack-Compose,React-Native,Flutter):**
-Screens-don't-have-URL-routes;identified-by-framework-navigation-state
-For-each-accessible-screen,capture-UI-tree(XML/JSON)+extract-unique-`resource-id`s
-Build-**active-screen-detection-landmarks-table**(reference:`ui_mapper_reference_tables.instructions.md`-section-9):
  -Per-screen:identify-1-2-resource-ids-uniquely-identifying-it
  -Identify-resource-ids-that-MUST-be-absent-to-distinguish-from-similar-screens
  -Register-table-in-session-context-for-use-in-Steps-2+3
-Document-if-app-uses-Compose-NavHost,Stack-Navigator-or-other-mechanism-based-navigation(affects-how-to-navigate-between-screens-in-capture-script)

### Phase-2-Screens-tree-construction

For-each-identified-route:
1.Register-complete-path(e.g:`/usuarios/:id/editar`)
2.Identify-assigned-main-component
3.Detect-screen-type:
   -**Full-page**:occupies-full-screen,has-own-route
   -**Modal**:overlays-another-screen,may-or-may-not-have-own-route
   -**Tab**:content-within-tab-bar-or-tabs
   -**Wizard-step**:step-within-multi-step-form
4.Determine-parent-screen(if-applies)
5.Estimate-complexity(Simple/Complex/Module)

### Phase-3-Sub-screens-detection-in-complex-modules

For-screens-classified-as-Module:
-Read-main-component-template
-Identify-sub-screens-per-automatic-subdivision-conditions(**`ui_mapper_reference_tables.instructions.md`-section-6**)
-Propose-subdivision-to-user+wait-approval

### Phase-4-Final-scope-confirmation

Present-complete-tree-to-user+request:
1.Confirmation-tree-is-correct
2.Mark-which-screens-within-this-analysis-scope
3.Preferred-processing-order

---

## 3. EXPECTED-OUTPUT

```
## Screens-Tree-Step-1-Completed

### Identified-screens

|#|Screen-ID|Name|Route|Type|Complexity|Parent|In-scope|
|---|-------------|--------|------|------|-------------|-------|-----------|
|1|login|Login|/login|Page|Simple|-|Yes|
|2|home|Home|/home|Page|Complex|-|Yes|
|3|home-tab-tasks|Home-Tab-Tasks|/home(tab-1)|Tab|Simple|home|Yes|
|4|home-tab-calendar|Home-Tab-Calendar|/home(tab-2)|Tab|Simple|home|Yes|
|5|users-list|Users-List|/usuarios|Page|Simple|-|Yes|
|6|users-detail|User-Detail|/usuarios/:id|Page|Complex|users-list|Yes|
|7|users-edit|User-Edit|/usuarios/:id/editar|Page|Complex|users-detail|Yes|
|8|settings|Settings|/ajustes|Page|Simple|-|No(out-of-scope)|

### Summary

**Total-identified-screens**:8
**In-scope-screens**:7
**Out-of-scope-screens**:1
**Estimated-processing**:7-Steps-2-3-4-cycles

### Proposed-processing-order

1.login(authentication-prerequisite-for-other-screens)
2.home/home-tab-tasks/home-tab-calendar
3.users-list
4.users-detail
5.users-edit

---

Confirm-if-this-tree+processing-order-are-correct-to-advance-to-Step-2-3-4-cycle.
```

---

## 4. PREREQUISITES-TO-ADVANCE-TO-STEP-2

-Screens-tree-approved-by-user
-In-scope-screens-clearly-identified
-Processing-order-confirmed
-First-screen-to-process-selected
