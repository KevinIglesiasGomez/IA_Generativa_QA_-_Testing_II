# Reverse-Engineering-Functional-Analyst—GitHub-Copilot-Agent

> AI-agent-specialized-in-functional-reverse-engineering:extracts-complete-functional-documentation(user-stories,functional-cases,endpoints,business-rules+architecture)-from-source-code-of-web/mobile-apps.

---

## 🎯 General-Objective

Project-contains-custom-GitHub-Copilot-agent,designed-to-act-as-expert-functional-analyst-in-software-reverse-engineering.Integrates-directly-in-VS-Code+provides:

### Main-Capabilities

-Exhaustive-source-code-exploration-to-discover-all-implemented-functionality
-Architectural-understanding-of-used-framework(Angular,React,Vue,Ionic,Next.js,Flutter,etc.)
-Functional-extraction-by-layers:routing,components,services,models,guards,stores
-Functional-documentation-generation-in-Markdown-format,ready-for-PDF-conversion
-Incremental-user-stories-proposal-with-individual-approval
-Dual-documentation:general-document(complete-vision)+detailed-documents-per-epic/story
-Advanced-context-management:state-persistence-in-session-memory+post-compact-recovery
-Only-verifiable-cases:NOT-document-inferred-behaviors,only-what's-completely-verifiable-in-code

### Supported-Frameworks

Angular • Angular+Ionic • React • React-Native • Vue.js • Next.js • Nuxt • Flutter

---

## 📁 Project-Architecture

```
Demo_IngenieriaInversa/
├── .github/                                   Agent-configuration
│   ├── agents/
│   │   └── reverse_engineering_analyst.agent.md              Agent-definition
│   ├── instructions/                          Modular-instructions-set
│   │   ├── reverse_engineering_main.instructions.md          Main-criteria+standards
│   │   ├── reverse_engineering_code_analysis.instructions.md Layer-by-layer-analysis-techniques
│   │   ├── reverse_engineering_interactive_flow.instructions.md Interactive-protocol
│   │   ├── reverse_engineering_document_generation.instructions.md Format+quality
│   │   ├── reverse_engineering_context_management.instructions.md State-management
│   │   └── reverse_engineering_quality_verification.instructions.md Quality-checklist
│   ├── prompts/                               Workflow-prompts
│   │   ├── reverse_engineering_step0_discovery.prompt.md    Project-discovery
│   │   ├── reverse_engineering_step1_general.prompt.md      General-document(overview)
│   │   └── reverse_engineering_step2_detail.prompt.md       Detailed-document-per-story
│   └── README.md                              This-guide
├── .gitignore                                 Version-control
└── Demo_IngenieriaInversa.code-workspace      VS-Code-workspace-config
```

### System-Components

|Component|Purpose|Location|
|----------|---------|----------|
|**Agent**|Agent-definition-with-role,tools+model|`agents/reverse_engineering_analyst.agent.md`|
|**Instructions**|Modular-set-of-analysis-criteria+standards|`instructions/*.instructions.md`|
|**Prompts**|3-step-workflow(discovery→general→detail)|`prompts/*.prompt.md`|
|**Workspace**|VS-Code-config-with-enabled-agent|`Demo_IngenieriaInversa.code-workspace`|

---

## 📚 Components-Description

### 🤖 Agent:`reverse_engineering_analyst.agent.md`

Defines-identity,role+behavior-of-GitHub-Copilot-agent.

#### Configuration

|Parameter|Value|
|----------|------|
|**Name**|Reverse-Engineering-Functional-Analyst|
|**Model**|Claude-Sonnet-4.6|
|**Skills**|`/explain`,`/search`,`/review`|
|**Language**|Spanish(complete-spelling)|

#### Enabled-Tools

-`edit/createDirectory`—Create-folder-structure-for-documentation
-`edit/editFiles`—Generate+modify-Markdown-documents
-`search`—Exhaustive-source-code-exploration
-`read/readFile`—Code-file-reading
-`vscode/getProjectSetupInfo`—Project-config-detection
-`execute/runInTerminal`—Command-execution-when-needed
-`usages`—Cross-reference-analysis

#### Methodological-Approach

Layer-by-layer-analysis-in-priority-order:
1.Routing-modules→navigation-discovery
2.Guards→access-control+profiles
3.Enums→states+catalogs
4.Services/Adapters→API-contracts
5.Stores→state-management
6.Components→views+interactions
7.Models→data-structures

---

### 📋 Instructions

#### `reverse_engineering_main.instructions.md`

**Central-instructions**-defining-analysis-criteria+standards.

**Content:**
-Project-structural-analysis(architecture,modules,routing)
-Functional-extraction-by-layers(routing→guards→services→components)
-User-Stories-model(Given/When/Then-format)
-Epic-vs-Story-classification(with-quantitative-thresholds)
-Exploration+prioritization-strategy
-File-nomenclature:`Recovered_Backlog_<App>_[Overview|Epic|Story]_...`

#### `reverse_engineering_code_analysis.instructions.md`

**Analysis-techniques**-to-extract-functional-info-from-each-code-artifact.

**Content:**
-Routing-modules:routes,guards,parameters,lazy-loading
-Components:interface-states,interactive-elements,lifecycle
-Services:HTTP-endpoints,payloads,responses
-Models:fields,types,relationships
-Enumerations:states,codes,values
-Guards:conditions,redirects,side-effects
-Stores:state,actions,selectors,effects
-Framework-patterns:Angular,Ionic,React,Vue

#### `reverse_engineering_interactive_flow.instructions.md`

**Interaction-protocol**-between-agent+user.

**Content:**
-Flow-phases:Confirmation→Discovery→General→Detail
-Generation-modes:Summary(automatic)-vs-Complete(approval)
-Individual-story-approval-protocol
-Ambiguity-management-with-questions-table
-Interactive-commands:"Next-story","Detail-this","Show-questions"
-`/compact`-management:when-to-suggest,post-compact-recovery

#### `reverse_engineering_document_generation.instructions.md`

**Format-rules**+structure-of-generated-documents.

**Content:**
-**General-document**(overview)-structure:header,index,architecture,profiles,summarized-stories,global-endpoints,questions-table
-**Epic-documents**-structure:header,sub-stories-map,navigation-flow,shared-endpoints
-**Story-documents**-structure:header,detailed-index,description,routes,functional-cases,services/API,views-with-states,modals,business-rules
-Markdown-format:headings,tables,inline-code,HTML-in-cells
-Spanish-spelling:complete-in-content,no-accents-in-filenames
-Standardized-file-nomenclature

#### `reverse_engineering_context_management.instructions.md`

**Context-management**+state-persistence-during-analysis.

**Content:**
-Session-memory-persistence:mandatory-save-moments
-State-file-format-with-critical-info
-Post-`/compact`-recovery-protocol:read+confirmation
-Critical-points-to-suggest-compacting(every-3-4-stories)
-Info-to-preserve:PROJECT_ROOT,modules-map,phase,progress

#### `reverse_engineering_quality_verification.instructions.md`

**Quality-checklist**-pre-document-delivery.

**Content:**
-Structural-verification:index,Markdown-format,section-order
-Content-verification:code-traceability,spelling
-Completeness-verification:minimum-coverage-thresholds
-Mandatory-functional-cases-per-view:happy-path,loading,error,no-data
-Inter-document-coherence:general-vs-detailed,epic-vs-sub-stories
-Anti-patterns:inferred-cases,assumptions,commented-code
-Quality-report:summary-format-with-metrics

---

### 🎬 Prompts(Workflow)

Analysis-structured-in-**3-sequential-steps**:

#### Step-0:`reverse_engineering_step0_discovery.prompt.md`

**Project-discovery**-phase-to-analyze.

**Actions:**
1.Request-root-directory-path-of-project(`PROJECT_ROOT`)
2.Identify-technology+framework(Angular,React,Vue,etc.)
3.Explore-folder+module-structure
4.Map-routes+security-guards
5.Classify-modules-in-Epics-vs-Stories(per-quantitative-thresholds)
6.Present-project-map-for-user-confirmation

#### Step-1:`reverse_engineering_step1_general.prompt.md`

**General-document-generation**-with-complete-app-vision.

**Execution-modes:**
-**Summary-Mode**:Generates-complete-document-automatically(summarized-stories)
-**Complete-Mode**:Proposes-each-story-individually-for-approval

**Generated-artifact:**  
`Recovered_Backlog_<App>_Overview.md`

**Content:**
-Header-with-project-metadata
-Complete-stories/epics-index
-Navigation-architecture(routing-tree)
-User-profiles+guards
-Summarized-stories-with-main-functional-cases
-Global-endpoints-inventory-by-domain
-Technical-questions-table

#### Step-2:`reverse_engineering_step2_detail.prompt.md`

**Detailed-documents-generation**-per-epic-or-individual-story.

**Generated-artifacts:**  
-Epics:`Recovered_Backlog_<App>_Epic_E<XX>_<Name>.md`
-Stories:`Recovered_Backlog_<App>_Story_H<XX>_<Name>.md`

**Story-document-content:**
1.Header-with-metadata
2.Detailed-index-with-anchors
3.Story-functional-description
4.Associated-routes(with-parameters)
5.**Functional-cases**(Given/When/Then)—positioned-BEFORE-services
6.Consumed-services/API(complete-endpoints)
7.Views-with-**3-interface-states**:
   -🔄 LOADING(skeleton/spinner)
   -⚠️ NO-DATA(empty/error)
   -✅ WITH-DATA(data-loaded)
8.Modals(forms,validations,actions)
9.Business-rules+conditions

---

## 🚀 How-to-Use

### Step-1:Prepare-Workspace

1.Open-VS-Code
2.Open-file-`Demo_IngenieriaInversa.code-workspace`
3.Ensure-**GitHub-Copilot**-extension-installed-with-Claude-Sonnet-4.6-access

### Step-2:Configure-Project-to-Analyze

Project-for-reverse-engineering-must-be-available-in-workspace.You-can:
-Add-project-folder-to-current-workspace
-Or-have-code-already-open-in-VS-Code

### Step-3:Invoke-Agent

In-GitHub-Copilot-chat,write:

```
@reverse_engineering_analyst
```

### Step-4:Start-Discovery

Use-**Phase-0**-prompt-to-start-analysis:

```
Use reverse_engineering_step0_discovery prompt to discover project
```

Agent-will-ask:
1.**Root-path**-of-project-to-analyze
2.Confirmation-of-discovered-modules-map

### Step-5:Generate-Documentation

Per-your-needs,agent-will-offer:

#### Option-A:General-Document-First

```
Generate general document in Summary mode
```
or
```
Generate general document in Complete mode (with approval per story)
```

#### Option-B:Detailed-Documents-per-Story

```
Detail story H01: Inspections Management
```

### Step-6:Manage-Context

When-agent-suggests-using-`/compact`,write-in-chat:

```
/compact
```

After-compacting,agent-will-auto-recover-state-from-session-memory.

---

## 📊 Generated-Artifacts

### 1.General-Document(Overview)

**File-name:**  
`Recovered_Backlog_<AppName>_Overview.md`

**Example:**  
`Recovered_Backlog_SOLHibrida_Overview.md`

**Content:**
-**Header**:App-name,version,technology,analysis-date
-**Index**:Complete-epics+stories-list
-**Architecture**:Navigation-tree(routing-tree)
-**Profiles+Guards**:User-roles+access-conditions
-**Summarized-Stories**:Table-with-#|Story|Functional-Cases(Given/When/Then-format)
-**Global-Endpoints**:API-inventory-by-domain
-**Questions-Table**:Non-verifiable-behaviors-in-code

### 2.Epic-Documents

**File-name:**  
`Recovered_Backlog_<AppName>_Epic_E<XX>_<EpicName>.md`

**Example:**  
`Recovered_Backlog_SOLHibrida_Epic_E01_Technical_Inspection_Workshops.md`

**Content:**
-Epic-description
-Contained-sub-stories-map
-Navigation-flow-between-sub-stories
-Shared-endpoints
-Reusable-components

### 3.Story-Documents

**File-name:**  
`Recovered_Backlog_<AppName>_Story_H<XX>_<StoryName>.md`

**Example:**  
`Recovered_Backlog_SOLHibrida_Story_H13_Pending_Inspections_List.md`

**Content:**
-Exhaustive-analysis-of-ONE-functional-module
-All-consumed-endpoints
-All-views-with-their-3-interface-states
-Detailed-functional-cases(Given/When/Then)
-Modals-with-forms+validations
-Applied-business-rules

---

## ✅ Main-Features

|Feature|Description|
|---------------|-------------|
|**Interactive-Flow**|Proposes-stories-individually+waits-approval-before-continuing|
|**Layer-by-Layer-Analysis**|Routing→Guards→Enums→Services→Stores→Components→Modals|
|**Dual-Documentation**|General-document(overview)+detailed-documents(epic/story)|
|**Multi-Framework**|Angular,Ionic,React,React-Native,Vue,Next.js,Nuxt,Flutter|
|**Traceability**|Source-code-references+questions-table-for-non-verifiable-behaviors|
|**Only-Verifiable-Cases**|NOT-document-inferred-cases—only-verifiable-behaviors-in-code|
|**QA-Ready-Format**|Functional-cases-in-Given/When/Then-format,ready-for-test-design|
|**Context-Management**|Session-memory-persistence+post-`/compact`-recovery|

---

## 📋 Requirements

-**Editor**:VS-Code(recent-version)
-**Extension**:GitHub-Copilot-active
-**Model**:Claude-Sonnet-4.6-configured
-**Project**:App-source-code-to-analyze(accessible-in-workspace)

---

## 🎯 Target-Audience

Agent-designed-for:

-**QA-Engineers**—Understand-undocumented-apps-to-design-test-cases
-**Functional-Analysts**—Validate-or-complete-existing-documentation
-**Testing-Teams**—Identify-test-scenarios-from-source-code
-**Product-Owners**—Obtain-updated-functional-vision-of-what's-implemented
-**Developers**—Document-legacy-projects-or-without-documentation

---

## 📝 Important-Notes

### Golden-Rule:Only-Verifiable-Cases

Agent-**NOT**-documents:
-Inferred-or-assumed-cases
-Behaviors-that-cannot-be-confirmed-in-code
-States-or-transitions-not-implemented

**If-behavior-not-clear-in-code**→registered-in-questions-table,**NOT**-documented-as-functional-case.
