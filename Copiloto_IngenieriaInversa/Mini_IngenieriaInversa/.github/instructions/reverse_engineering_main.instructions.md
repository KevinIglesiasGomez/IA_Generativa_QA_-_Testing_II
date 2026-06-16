# Main-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-criteria+standards-agent-must-follow-when-analyzing-source-code-to-extract-complete-functional-documentation.Agent-produces-three-artifact-types:

1.**General-Document(Overview)**-Complete-app-vision-with-all-epics+stories-summarized
2.**Epic-Documents(Epic)**-Complex-functional-domain-vision-grouping-multiple-related-stories,with-sub-story-map
3.**Story-Documents(Story)**-Exhaustive-detail-of-individual-user-story-with-functional-cases,views,modals,endpoints+business-rules

---

## 1. PROJECT-STRUCTURAL-ANALYSIS

### A)Architecture-Discovery

1.**Folder-structure**:
   -Identify-architectural-pattern(feature-modules,domain-driven,layered,etc.)
   -Map-folders-to-functional-domains(e.g:`domain/inspeccion`,`domain/tasaciones`)
   -Identify-shared-folders(`shared/`,`core/`,`common/`)

2.**Project-config**:
   -Read-`angular.json`,`package.json`,`tsconfig.json`-or-equivalents
   -Identify-base-technology(Angular,React,Vue,Ionic,etc.)
   -Identify-framework+relevant-dependency-versions

3.**Main-routing**:
   -Locate-root+feature-route-modules
   -Build-complete-navigation-tree
   -Identify-lazy-loading+protected-routes

### B)Functional-Module-Discovery

For-each-identified-module/domain:
-Module-name+project-location
-Exposed-routes(with-dynamic-parameters)
-Guards-protecting-routes
-Main-components(pages+modals)
-Consumed-services
-Involved-stores/state-management

---

## 2. FUNCTIONAL-EXTRACTION-BY-LAYERS

### A)Routing-Layer(Navigation)

For-each-route-module:
1.Extract-ALL-routes-with-complete-paths
2.Identify-dynamic-parameters(`:id`,`:matricula`,etc.)
3.Register-guards-associated-to-each-route
4.Determine-parent/child-route-hierarchy
5.Identify-redirects+default-routes

### B)Component-Layer(Views)

For-each-page-component:
1.Read-HTML-template-to-identify-UI-elements
2.Read-TypeScript-class-to-understand-logic
3.Document:
   -**Interface-states**:LOADING(skeleton/spinner),NO-DATA(empty/error),WITH-DATA(loaded-data)
   -**Interactive-elements**:buttons,forms,lists,tabs,segments
   -**Gestures**:swipe,pull-to-refresh,infinite-scroll
   -**Modals**:which-modals-can-open+from-where
   -**Navigation**:where-each-user-action-navigates
   -**Displayed-data**:which-fields-visualized+format

### C)Service-Layer(API)

For-each-service/adapter:
1.Extract-ALL-HTTP-methods-with-complete-endpoints
2.Document:
   -Descriptive-operation
   -HTTP-method(GET,POST,PUT,DELETE,PATCH)
   -Endpoint-URL(with-parameters+query-strings)
   -Input-payload(if-applicable)
   -Response-structure(if-identifiable)

### D)Model-Layer(Data)

For-each-interface/domain-class:
1.Extract-fields-with-data-types
2.Identify-optional-vs-required-fields
3.Document-enumerations+values
4.Register-model-relationships

### E)Guard-Layer(Security+Preconditions)

For-each-guard:
1.Name+type(CanActivate,CanDeactivate,etc.)
2.Evaluated-condition
3.Behavior-when-fails(redirect,message,block)
4.Protected-routes

### F)State-Management-Layer(Stores)

For-each-store:
1.Managed-state
2.Available-actions/mutations
3.Exposed-selectors
4.Side-effects(API-calls-from-store)

---

## 3. FUNCTIONAL-MODEL-USER-STORY

### 3.1 General-Document-Structure

General-document-must-contain:

1.**Project-header**:
   -App-name
   -Company
   -Version
   -Technology(framework+version)
   -Analysis-date

2.**Designs+Architecture**:
   -API-Base-URL
   -Navigation-architecture(tabs,sidebar-menu,etc.)
   -Profiles-vs-functionalities-table
   -Identified-security-guards

3.**User-Profiles**:
   -Table-with:Profile|Description|Main-permissions

4.**Per-User-Story**(summary):
   -Descriptive-title
   -User-story-format:"As-[profile],I-want-[action],to-[benefit]"
   -Brief-general-description
   -General-requirements(list)
   -Available-routes(table)
   -**Functional-cases**(narrative-format,BEFORE-endpoints)

5.**Services+Endpoints**:
   -Global-summary(table:Domain|GET|POST|PUT|DELETE|Total)
   -Detail-by-domain(table:Operation|Method|Endpoint)

6.**Questions-Table**:
   -Table-with:#|Area|Question/Doubt

### 3.2 Story-Document-Structure(Detailed)

Each-specific-document-must-contain:

1.**Story-header**:
   -App-name(with-technical-project-name)
   -Main-interacting-profile
   -Source-code-module
   -Applying-guards
   -Analysis-date

2.**Detailed-index**-with-anchors-to-each-section

3.**General-description**-of-functional-module

4.**Available-routes**-Complete-table-with-ALL-module-routes

5.**Functional-cases**-In-narrative-Given/When/Then-format(see-section-4),positioned-BEFORE-services+endpoints

6.**Involved-API-services**-Table-with-ALL-module-endpoints

7.**States**-State/transition-table(if-applicable)-with-CSS-class+description

8.**Per-Main-View/Component**:
   -View-route
   -Functional-cases-in-narrative-format
   -Positioned-BEFORE-service-calls+petitions

9.**Per-Modal**:
   -Same-structure-as-views

10.**Business-rules+conditions-table**

### 3.3 CLASSIFICATION:EPIC-vs-STORY

Before-generating-any-detailed-document,agent-must-**classify-each-module**-as-EPIC-or-STORY.

Module-documented-as-**Epic**-when-meets-**2-or-more**-criteria:

|#|Criterion|Epic-Threshold|
|---|----------|-----------------------|
|1|Independent-views/pages-in-module|More-than-5|
|2|Endpoints-in-module-services|More-than-10|
|3|User-profiles-with-completely-different-flows|More-than-2|
|4|Contains-sub-modules-with-own-routing(lazy-load-to-children)|Yes|
|5|Total-functional-cases-estimation|More-than-25|
|6|Covers-completely-disconnected-flows(e.g:list+detail+creation+config)|Yes|

Module-documented-as-**Story**-when-meets-**0-or-1**-criteria+can-be-completely-documented-in-single-file-without-losing-clarity/coherence.

### Epic-Decomposition-Process

When-module-classified-as-Epic:
1.Identify-module's-**independent-functional-flows**
2.Propose-to-user-decomposition-into-sub-stories-with-descriptive-names
3.**AWAIT-APPROVAL**-of-proposed-decomposition-before-continuing
4.Generate-Epic-file-first(header+sub-story-map+shared-endpoints)
5.Document-each-sub-story-independently,in-approval-order

### Module,Epic+sub-story-Numbering

-Each-identified-module-receives-main-sequence-number-with-prefix-**`M`**(M=Module):`M01`,`M02`,`M03`,etc.
  -`M`-prefix-explicitly-differentiates-module-identifier-from-Story(`HU-`)or-Epic-concept
  -Numbering-consecutive-according-to-routing-discovery-order
-Epic-sub-stories-identified-with-user-story-code:`M02.HU-COD-01`,`M02.HU-COD-02`,etc.
  -`COD`=module's-3-letter-identifying-code-in-uppercase(e.g:TAS,INS,TAL)
-Independent-Stories(without-parent-Epic)-use-only-module-number:`M01`,`M03`,etc.

---

## 4. FUNCTIONAL-CASE-FORMAT

### Document-Position

Functional-cases-MUST-appear-BEFORE-services,endpoints+API-calls-sections,both-in-general-document+detailed-story-documents.

### Mandatory-Narrative-Format

Functional-cases-NOT-documented-in-table-format.Use-narrative-Given/When/Then-format-with-template:

```markdown
### Functional-Case-[N]

**Given**
"[Context:who-is-user,what-state,what-done-previously]"

**When**
"[Concrete-user-action,indicating-button,link,element-interacted-with,view-located+functionality-belongs-to]"

**Then**
"[Detailed-observable-result-description.Must-include:

-Shown-view-name.
-Complete-list-of-all-visible-interface-elements,with:
  -Exact-displayed-text.
  -Text-field-default-value.
  -Text-field-placeholder.
  -Button-default-state(enabled/disabled).
  -Button-style(primary,secondary,link).
  -Password-field-behavior(default-obfuscated,visibility-icon).
-View-sections(animations,spaces,groupings).
-Important-notes-about-functional-implications.]"
```

### "Then"-Field-Detail-Level

Functional-cases-in-detailed-story-document-must-include-in-"Then"-field:

1.**Complete-narrative-description**-of-what-happens
2.**All-interface-elements**-with-exact-properties(text,placeholder,default-value,state,style)
3.**Interface-states**-when-relevant:
   -LOADING:what-shown-while-waiting-data
   -NO-DATA(KO):what-shown-when-no-data
   -WITH-DATA(OK):what-shown-with-available-data
4.**API-calls**-in-format-`METHOD-endpoint`
5.**Resulting-navigation**-with-destination-route
6.**Important-notes**-about-functional/technical-implications

---

## 5. CODE-EXPLORATION-STRATEGY

### Recommended-Analysis-Order

1.**Phase-1-Discovery**:`routing-modules`→`guards`→`enums/models`
2.**Phase-2-Services**:`services/adapters`→`interceptors`→`stores`
3.**Phase-3-Views**:`page-components`(HTML+TS)→`modal-components`
4.**Phase-4-Correlation**:Cross-data-between-layers-to-complete-functional-puzzle
5.**Phase-5-Validation**:Review-pipes,directives+relevant-shared-components

---

## 6. BEST-PRACTICES

### 6.1 Precision

-Use-exact-source-code-names(components,services,variables)
-Cite-file-path-when-referencing-specific-logic
-NO-invent-routes,endpoints,behaviors-not-in-code

### 6.2 Completeness

-Document-ALL-found-routes,not-only-main-ones
-Document-ALL-endpoints-of-each-service
-Document-ALL-fields-of-relevant-interfaces
-Include-intermediate-states,exceptions+error-cases

### 6.3 Coherence

-Use-same-terminology-throughout-document
-Maintain-consistent-format-between-stories
-Number-functional-cases-continuously-within-each-story

### 6.4 Traceability

-Indicate-source-file-of-each-info-piece-when-relevant
-**NO-document-inferred-functional-cases**:Only-document-completely-verifiable-behaviors-in-source-code
-Register-in-questions-table-any-ambiguity/behavior-not-100%-verifiable

---

## 7. RESTRICTIONS

-NO-generate-functionality-documentation-not-existing-in-code
-NO-assume-business-rules-not-expressed-in-source-code
-NO-omit-routes,endpoints,states-considering-them-minor
-Keep-questions-table-updated-with-each-new-found-ambiguity
-Respect-valid-Markdown-format-for-PDF-conversion
-NO-include-emojis/decorative-icons-in-final-generated-documentation
-**Complete-Spanish-spelling**:All-content-of-generated-.md-files-MUST-use-ñ,accents(á,é,í,ó,ú),diaeresis(ü)+other-Spanish-chars."Without-accents"-restriction-applies-ONLY-to-filenames,never-content
-Functional-cases-must-follow-narrative-Given/When/Then-format(not-table-format)+appear-BEFORE-services+endpoints-sections
