# Document-Generation-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-format,structure+quality-rules-that-documents-generated-by-agent-must-meet,both-general-document+detailed-story-documents.

---

## 1. GENERAL-DOCUMENT-MANDATORY-STRUCTURE

### 1.1 Header

```markdown
# Functional-Cases-[Application-Name]

**Application**:[Readable-name](`technical-project-name`)
**Company**:[Company-name]
**Version**:[Version-identified-in-package.json-or-equivalent]
**Technology**:[Main-framework+version](e.g:Angular-18.2.14+Ionic)
**Analysis-date**:[Current-date]

---
```

### 1.2 Index

Markdown-links-generated-index-to-each-section:
```markdown
## Index

-[Designs+Architecture](#designs+architecture)
-[User-Profiles](#user-profiles)
-[Story-01-Name](#story-01--name)
-...
-[Services+Endpoints](#services+endpoints)
-[Questions-Table](#questions-table)
```

### 1.3 Designs+Architecture

-API-Base-URL(extracted-from-services/config)
-Navigation-architecture(tabs,drawer,etc.)
-Tabs/functionalities-by-profile-table
-Security-guards-list-with-brief-description

### 1.4 User-Profiles

```markdown
|Profile|Description|Main-permissions|
|--------|-------------|----------------------|
|**Name**|Description|Permissions-list|
```

### 1.5 User-Stories(summary)

For-each-story:
```markdown
## Story-XX-Descriptive-Name

As-[profile]
I-want-[action]
To-[benefit]

**General-description**:[Descriptive-paragraph]

### General-requirements
-[Requirement-1]
-[Requirement-2]

### Available-routes
|Screen|Route|
|----------|------|
|Name|`/route/{param}`|

### Functional-cases

|#|Given|When|Then|
|---|------|--------|----------|
|1|[User-context+previous-state]|[Concrete-action-user-performs,indicating-button/element,view+functionality]|[Observable-result-description-with-main-interface-elements,states+API-calls]|
|2|...|...|...|
```

>**IMPORTANT**:Functional-cases-positioned-BEFORE-Services+Endpoints-section.

### 1.6 Services+Endpoints

```markdown
## Services+Endpoints

**Base-URL**:`https://...`

### Global-endpoints-summary
|Domain|GET|POST|PUT|DELETE|Total|
|---------|-----|------|-----|--------|-------|

### Main-endpoints-[Domain]
|Operation|Method|Endpoint|
|-----------|--------|----------|
```

### 1.7 Questions-Table

```markdown
## Questions-Table

|#|Area|Question/Doubt|
|---|------|-----------------|
|1|...|...|
```

---

### 1.8 EPIC-DOCUMENT-MANDATORY-STRUCTURE

>Apply-when-module-classified-as-EPIC-according-to-criteria-in-section-3.3-of-main-instructions.

#### 1.8.1 Header

```markdown
# Epic-M<number>-<DescriptiveName>

**Application**:[Name](`technical-name`)
**Type**:EPIC
**Module**:`module/path`
**Guards**:`Guard1`,`Guard2`
**Sub-stories**:`M<n>.HU-COD-01-Name`,`M<n>.HU-COD-02-Name`,...
**Date**:[Current-date]

---
```

#### 1.8.2 Epic-Description

Descriptive-paragraph-of-complete-functional-domain-epic-covers.Must-answer:what-problem-solves,which-profiles-use-it+which-main-flows-contains.

#### 1.8.3 Involved-Profiles

```markdown
|Profile|Applicable-sub-stories|
|--------|------------------------------|
|**Name**|H<n>.01,H<n>.02|
```

#### 1.8.4 Sub-stories-Map

```markdown
|Sub-story|Descriptive-name|Brief-description|Main-routes|
|:------------:|--------------------|-------------------|-------------------|
|M<n>.HU-COD-01|Name|Description|`/route/...`|
|M<n>.HU-COD-02|Name|Description|`/route/...`|
```

#### 1.8.5 Sub-stories-Navigation-Flow

Textual-description/table-of-how-user-transits-between-sub-stories-within-epic(entry+exit-points,shared-routes).

#### 1.8.6 Shared-Endpoints-Between-Sub-stories

```markdown
|Operation|Method|Endpoint|
|-----------|--------|----------|
```

#### 1.8.7 Epic-Questions-Table

```markdown
|#|Area|Question/Doubt|
|---|------|-----------------|
```

---

## 2. STORY-DOCUMENT-MANDATORY-STRUCTURE

### 2.1 Header

```markdown
# Story-XX-Descriptive-Name

**Application**:[Name](`technical-name`)
**Profile**:[Main-profile]([roles])
**Module**:`module/path`
**Guards**:`Guard1`,`Guard2`
**Date**:[Current-date]

---
```

### 2.2 Detailed-Index

Include-ALL-sections-with-anchors:
```markdown
## Index

-[General-description](#general-description)
-[Available-routes](#available-routes)
-[Functional-cases](#functional-cases)
-[Involved-API-services](#involved-api-services)
-[States](#states)
-[View:VIEW-NAME](#view-name)
```

### 2.3 Available-Routes

Complete-table-with-ALL-module-routes

### 2.4 Functional-Cases

In-narrative-Given/When/Then-format(see-section-4-of-main-instructions),positioned-BEFORE-services+endpoints

### 2.5 Involved-API-Services

Complete-table-with-ALL-module-endpoints

### 2.6 States

State/transition-table(if-applicable)-with-CSS-class+description

### 2.7 Per-Main-View/Component

-View-route
-Functional-cases-in-narrative-format
-Positioned-BEFORE-service-calls

### 2.8 Per-Modal

Same-structure-as-views

### 2.9 Business-Rules+Conditions-Table

Table-with:Rule|Condition|Behavior

---

## 3. QUALITY-CRITERIA

### 3.1 Markdown-Validity

-All-tables-properly-formatted
-All-index-links-pointing-to-existing-sections
-Headers-correctly-hierarchical
-Code-blocks-with-proper-syntax

### 3.2 Content-Completeness

-ALL-code-routes-documented
-ALL-service-endpoints-documented
-ALL-guards-documented
-ALL-main-views-with-functional-cases

### 3.3 Spanish-Spelling

-ALL-generated-.md-file-content-MUST-use-complete-Spanish-spelling:ñ,accents(á,é,í,ó,ú),diaeresis(ü)
-"Without-accents"-restriction-applies-ONLY-to-filenames,NEVER-to-content

---

## 4. FILENAME-CONVENTIONS

-General-document:`Recovered_Backlog_<App>_Overview.md`
-Epic:`Recovered_Backlog_<App>_M<number>_Epica_<Name>.md`
-Independent-story:`Recovered_Backlog_<App>_M<number>_HU-<COD>-<NN>_<Name>.md`
-Epic-sub-story:`Recovered_Backlog_<App>_M<number>_HU-<COD>-<NN>_<Name>.md`

Filenames-WITHOUT-accents/special-chars.Content-WITH-complete-Spanish-spelling.
