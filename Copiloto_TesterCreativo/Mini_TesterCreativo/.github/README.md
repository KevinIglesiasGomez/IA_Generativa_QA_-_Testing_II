# Creative-Tester

VS-Code-copilot-specialized-in-generating-creative+innovative-tests-ensuring-software-quality,exploring-edge-cases+unconventional-scenarios.

**Automatically-generates-concise-reports(4-6-pages)-with-10-20-prioritized-test-scenarios+5-8-extreme-"very-crazy"-tests-challenging-conventional-limits.**

## What-It-Does

Analyzes-screenshots,documentation,source-code-or-HTML-of-application+generates-complete-report-with-test-scenarios-conventional-tests-don't-cover:edge-cases,non-obvious-interactions,adversarial-behaviors+concurrency-situations,among-others.

Uses-**EXPLORA-model**-to-classify+prioritize-creative-scenarios,focusing-on-highest-value(high-priority)+presenting-rest-in-compact-format.

**NEW**:Includes-special-**Extreme+Unexpected-Tests**-section-with-highly-creative-scenarios-exploring-improbable-but-technically-possible.

**Result**:Actionable,scannable+non-overwhelming-report,ready-for-QA-team-use.

## Key-Features

-✅**Automatic**:generates-complete-report-without-iterative-approval
-✅**Concise**:maximum-4-6-pages,quickly-scannable
-✅**Prioritized**:10-20-high-priority-scenarios-with-complete-detail
-✅**Visual**:tables+lists-for-quick-reading
-✅**Actionable**:each-scenario-includes-clear+executable-steps
-✅**Creative**:edge-case+unconventional-scenario-exploration
-✅**EXPLORA-model-based**:systematic-coverage-7-risk-categories
-🚀**NEW:Extreme-Tests**:5-8-"very-crazy"-scenarios-challenging-implicit-assumptions

### Why-This-Approach

**Speed**:get-complete-report-in-single-execution,no-iterations.
**Clarity**:concise+visual-format-facilitating-quick-team-review.
**Focus**:automatically-prioritizes-highest-value-scenarios,avoiding-noise.
**Balanced-coverage**:10-20-detailed-scenarios-provide-adequate-coverage-without-overwhelming.

## EXPLORA-Model

|Letter|Category|Covers|
|---|---|---|
|**E**|Extremes+Limits|Boundary-values,unexpected-types,extreme-volumes|
|**X**|Cross-cutting|Security,perceived-performance,accessibility,compatibility|
|**P**|User-Perception|Non-obvious-usability,feedback,first-impression|
|**L**|Business-Logic|Business-rules,complex-flows,data-coherence|
|**O**|Concurrent-Operations+State|Concurrency,state-management,interruptions|
|**R**|Resilience+Recovery|Error-handling,recovery,graceful-degradation|
|**A**|Adversarial/Antagonist|Malicious-use,system-abuse,social-engineering|

## 🚀-Extreme+Unexpected-Tests(NEW)

Beyond-structured-EXPLORA-model,agent-generates-special-**extremely-creative-tests**-section-challenging-imagination-limits:

### Characteristics
-**Highly-improbable-but-technically-possible**
-**Unexpected-action-combinations**
-**Absurd-but-technically-valid-behaviors**
-**Challenge-developer's-implicit-assumptions**

### Extreme-Test-Categories

1.**Chaotic-User**:random-actions,multiple-clicks,constant-reload,language-changes-mid-flow
2.**Temporal-User**:forms-open-7-days,system-date-changes,suspend/resume-system
3.**Extreme-Multilanguage**:RTL+LTR+emojis-mix,rare-Unicode-characters,invisible-directionals
4.**Absurd-Hacker**:DOM-manipulation-with-DevTools,HTTP-method-changes,invisible-CSS-injection
5.**Extreme-Volume**:1-million-characters,10,000-simultaneous-files,500-cart-items
6.**Past/Future-User**:IE5,disabled-JavaScript,320x240-pixels,56k-connection
7.**Impossible-Combinations**:race-conditions,simultaneous-contradictory-states
8.**Culturally-Unexpected**:1-character-names,5-digit-phones,numberless-addresses
9.**Creative-Saboteur**:5-extensions-simultaneously-modifying-DOM,continuous-rotation,all-accessibility-features-active
10.**Extreme-Real-World**:user-in-airplane-crossing-timezones,space-station(1000ms-ping),massive-event(10,000-same-WiFi)

### Philosophy

>"If-experienced-tester-reads-this-test+says-'I-would-have-never-thought-of-that',then-it's-good-extreme-test."

**Recommended-balance:**
-80-85%-focus-on-EXPLORA(structured+reliable)
-15-20%-focus-on-Extreme-Tests(creative+explorer)

## Project-Structure

```
.github/
  agents/
    tester_creativo.agent.md          #Agent-definition
  instructions/
    main_TesterCreativo.instructions.md                  #Central-instructions+EXPLORA-model
    tecnicasCreativas_TesterCreativo.instructions.md     #Creative-testing-techniques+heuristics
    buenasPracticas_TesterCreativo.instructions.md       #Best-practices+antipatterns
    informe_TesterCreativo.instructions.md               #Report-generation+update
    escenariosNoConvencionales_TesterCreativo.instructions.md  #Unconventional-scenarios-catalog
    pruebasExtremas_TesterCreativo.instructions.md       #🚀-Extreme+unexpected-tests(NEW)
  prompts/
    prompt_TesterCreativo.prompt.md              #Complete-agent-prompt
    prompt_TesterCreativo_reducido.prompt.md     #Reduced-version-prompt
```

## Supported-Inputs

Copilot-works-from:

-**Screenshots**:analyzes-visible-elements,infers-behavior,detects-ambiguities
-**Documentation**:user-stories,acceptance-criteria,functional-specs,flowcharts
-**Source-code**:any-language;analyzes-logic,conditional-flows,error-handling,integrations
-**HTML/Markup**:DOM-structure,HTML5-validations,accessibility-attributes,events

## How-It-Works

### Workflow

1.**Initial-confirmation**:agent-asks-what-info-type-will-be-provided+functionality-to-explore
2.**Deep-analysis**:passes-through-4-internal-cognitive-roles(Analyzer,Creative-Generator,Critical-Reviewer,Impact-Evaluator)
3.**Scenario-prioritization**:focus-on-high-priority-scenarios(score>=6.0)-really-adding-value
4.**Extreme-test-generation**:creates-5-8-"very-crazy"-scenarios-challenging-implicit-assumptions(Chaotic-User,Temporal,Multilanguage,Absurd-Hacker,Extreme-Volume,etc.)
5.**Complete-report-generation**:creates-concise-report(4-6-pages)-with:
   -Brief-functional-description(2-3-paragraphs)
   -EXPLORA-coverage-summary-table
   -Top-10-15-most-critical-risks
   -**10-20-high-priority-scenarios**-with-complete-detail(steps,preconditions,expected-results)
   -Medium/low-priority-scenarios-in-compact-table
   -**🚀-5-8-Extreme+Unexpected-Tests**-in-differentiated-format
   -Top-3-5-recommendations
6.**Delivery**:engineer-receives-complete-report,ready-for-review+execution-by-QA-team

### Report-Principles

-**Conciseness**:maximum-4-6-pages,quickly-scannable
-**Quality-over-quantity**:focus-on-10-20-highest-value-scenarios
-**Visual+actionable**:tables+lists-use-for-easy-reading
-**No-redundancy**:each-info-appears-once
-**Prioritized**:scenarios-ordered-by-impact+probability

## Included-Creative-Techniques

-Boundary-Value-Analysis
-Equivalence-Partitioning
-Decision-Table
-State-Transition
-Exploratory-testing-with-heuristics(SFDPOT,FEW-HICCUPPS)
-Conceptual-mutation-testing
-Pairwise-combinatorial-testing
-Fault-injection
-Lateral-thinking-heuristics:inversion,analogy,extreme-user-personification,WWWWWH

## Scenario-Prioritization

Each-scenario-evaluated-with-weighted-matrix:

|Criterion|Weight|
|---|---|
|Occurrence-probability|30%|
|User-impact|25%|
|Business-impact|25%|
|Detection-difficulty-by-other-means|20%|

-**High-priority**:Score>=7.0
-**Medium-priority**:Score-between-4.0-6.9
-**Low-priority**:Score<4.0

## Generated-Reports

Copilot-generates-document-in-`informes/`-directory:

-**Report**(`informe_<name>.md`):concise-document(4-6-pages)-including:
  -Metadata:analyzed-source,date,complexity
  -Brief-functional-description
  -EXPLORA-coverage-summary-table
  -Top-10-15-main-risks(score>=6.0)
  -10-20-high-priority-scenarios-with-complete-detail
  -Additional-scenarios-in-compact-table
  -🚀-5-8-Extreme+Unexpected-Tests
  -Top-3-5-recommendations

**Optional**:If-future-updates-required,can-create-**log**(`bitacora_<name>.md`)-to-record-incremental-changes.

### Report-Structure

Report-designed-to-be:
-**Scannable**:visual-format-with-tables+lists
-**Actionable**:clear+executable-steps-for-each-scenario
-**Concise**:maximum-4-6-pages-without-being-exhaustive
-**Prioritized**:focus-on-highest-impact-scenarios
