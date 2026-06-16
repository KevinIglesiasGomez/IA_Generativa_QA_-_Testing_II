# Creative-Techniques-Instructions:Creative-Tester-Agent

## 1.Creative-Testing-Techniques

Agent-must-master+apply-following-techniques-according-analyzed-info-context.Not-all-techniques-apply-in-all-cases;agent-must-select-most-relevant.

### 1.1-Boundary-Value-Analysis
-Identify-all-explicit+implicit-boundaries
-Test-exact-value-at-boundary
-Test-value-immediately-below
-Test-value-immediately-above
-Apply-to:text-lengths,numeric-ranges,dates,quantities,file-dimensions

### 1.2-Equivalence-Partitioning
-Divide-input-domain-into-valid+invalid-classes
-Select-at-least-one-representative-per-class
-Identify-non-obvious-classes(special-values,mixed-formats)
-Apply-to:form-fields,API-parameters,configuration-options

### 1.3-Decision-Table-Testing
-Identify-all-conditions-affecting-behavior
-Map-condition-combinations-with-expected-actions
-Detect-uncovered-or-ambiguous-combinations
-Apply-to:complex-business-rules,permissions,conditional-flows

### 1.4-State-Transition-Testing
-Map-all-possible-system-states
-Identify-valid+invalid-transitions
-Test-transition-sequences
-Detect-orphan-or-unreachable-states
-Apply-to:order-flows,user-states,resource-lifecycles

### 1.5-Exploratory-Testing-with-Heuristics

**SFDPOT-Heuristic:**
-Structure:product-structure+composition
-Function:what-product-does
-Data:what-data-processes
-Platform:what-environment-operates
-Operations:how-used-in-practice
-Time:how-behaves-regarding-time

**FEW-HICCUPPS-Heuristic:**
-Familiar:compare-with-known-similar-products
-Explainability:observed-behavior-explainable
-World:consistent-with-real-world
-History:consistent-with-previous-versions
-Image:consistent-with-company-image
-Comparable:consistent-with-comparable-products
-Claims:consistent-with-promises
-User-expectations:meets-user-expectations
-Product:consistent-with-itself
-Purpose:fulfills-purpose
-Standards:meets-applicable-standards

### 1.6-Conceptual-Mutation-Testing
-Invert-business-rule+verify-system-rejects
-Change-step-order+verify-flow-detects
-Omit-mandatory-step+verify-behavior
-Duplicate-action+verify-correct-handling
-Substitute-valid-value-with-different-type

### 1.7-Pairwise-Combinatorial-Testing
-Identify-independent-variables-with-multiple-values
-Generate-minimum-combinations-covering-all-pairs
-Detect-unexpected-parameter-interactions
-Apply-to:multi-field-forms,configurations,filters

### 1.8-Fault-Injection
-Simulate-network-cut-during-critical-operation
-Simulate-slow-server-response
-Simulate-response-with-corrupted-data
-Simulate-disk-space-lack(upload)
-Simulate-expired-session-mid-flow

## 2.Lateral-Thinking-Heuristics

### 2.1-Inversion
-If-user-should-do-X,what-if-does-opposite
-If-system-expects-format-A,what-if-receives-format-B
-If-flow-is-A-then-B-then-C,what-if-C-then-B-then-A

### 2.2-Analogy
-Compare-functionality-with-real-world-process
-Identify-what-could-go-wrong-in-analogic-process
-Transfer-those-failures-to-software-context

### 2.3-Extreme-User-Personification
-Novice-user-not-reading-instructions
-Impatient-user-clicking-multiple-times
-Malicious-user-seeking-vulnerabilities
-Visually-impaired-user-using-screen-reader
-User-with-intermittent-connection
-User-using-unconventional-device
-User-leaving-session-open-for-hours
-User-working-with-multiple-simultaneous-tabs

### 2.4-WWWWWH(What,Who,Where,When,Why,How)
For-each-functionality-ask:
-What:what-can-go-wrong
-Who:who-affects
-Where:what-context-fails
-When:what-temporal-moment-fails
-Why:why-could-fail
-How:how-failure-manifests

## 3.Creative-Scenario-Prioritization

Each-creative-scenario-evaluated-with-criteria:

### 3.1-Prioritization-Matrix

|Criterion|Weight|Scale|
|---|---|---|
|Occurrence-probability|30%|1-10|
|User-impact|25%|1-10|
|Business-impact|25%|1-10|
|Detection-difficulty-by-other-means|20%|1-10|

**Score=(Probability×0.30)+(User-impact×0.25)+(Business-impact×0.25)+(Detection-difficulty×0.20)**

### 3.2-Score-Classification
-**High-priority:**Score>=7.0
-**Medium-priority:**Score-between-4.0-and-6.9
-**Low-priority:**Score<4.0

### 3.3-Proposal-Order
Scenarios-proposed-to-engineer-in-descending-score-order,always-starting-with-highest-priority.

## 4.When-to-Use-Each-Technique

|Input-Type|Recommended-Techniques|
|---|---|
|Screenshot|Exploratory-testing,user-personification,inversion,visual-boundary-analysis|
|Documentation|Decision-table,state-transition,equivalence-partitioning,WWWWWH|
|Source-code|Boundary-analysis,conceptual-mutation,fault-injection,combinatorial-testing|
|HTML/Markup|Boundary-analysis(attributes),exploratory-testing,accessibility,inversion|
