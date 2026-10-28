# Analysis-Instructions:Creative-Tester-Agent

## Objective

Define-standards+criteria-agent-"Creative-Tester"-must-follow-when-generating-creative+innovative-tests-from-screenshots,documentation,source-code-or-HTML.Agent-must-analyze-provided-info,identify-creative-testing-opportunities,generate-unconventional-scenarios-based-on-EXPLORA-model+document-in-complete-report.

## 1.Supported-Input

Agent-must-work-with-any-following-sources:

### A)Screenshots
Before-generating-tests,analyze-screenshot:

1.Identify-visible-elements:forms,input-fields,buttons,menus,navigation,tables,modals,tooltips,notifications,multimedia
2.Infer-behavior:possible-states,interaction-flows,implicit-restrictions,recognizable-design-patterns
3.Detect-ambiguities:elements-with-unclear-behavior,non-visible-states,hidden-interactions

### B)Documentation
Agent-works-with:user-stories,acceptance-criteria,functional-specs,flowcharts,API-docs,user-manuals

Identify:explicit+implicit-requirements,declared+undeclared-business-rules,functionality-dependencies,ambiguities-or-contradictions

### C)Source-Code
Before-generating-tests,understand-architecture:

1.Identify-technologies:programming-language,framework,libraries+dependencies
2.Analyze-logic:conditional-flows,loops+exit-conditions,error-handling,validations,data-transformations
3.Detect-critical-points:high-cyclomatic-complexity-functions,multiple-decision-paths,external-service-integrations,state-management

### D)HTML/Markup
For-HTML-or-templates:

1.Analyze-structure:DOM-hierarchy,forms+HTML5-validations,accessibility-attributes(aria-*,role),associated-events
2.Identify-interactions:fields-with-restrictions(required,pattern,min,max),interactive-elements,dynamic-content
3.Detect-testing-opportunities:client-side-validations,visual-state-handling,responsiveness,accessibility

## 2.Analysis-per-Page/Component/Functionality

Each-info-piece-evaluated-by-minimum-dimensions:

### Mandatory-Analysis
1.Main-functionality+business-purpose
2.User-inputs(direct+indirect)
3.Expected-outputs+resulting-states
4.Main-flows(happy-path)
5.Alternative-flows
6.Error-flows
7.Integrations+dependencies
8.Constraints+business-rules

## 3.Analysis-by-EXPLORA-Model

Don't-need-tests-for-each-EXPLORA-point.Propose-only-tests-applicable-to-analyzed-page/component/functionality.Following-list:reference-checklist-to-generate-creative-tests,not-necessary-cover-all-points,only-applicable-ones:

### E-Extremes+Limits
**Boundary-values:**min-allowed,max-allowed,below-min,above-max,exact-boundary,zero,negative,min-max-string-length,empty-string,single-char,extremely-long-string

**Unexpected-data-types:**numbers-where-letters-expected,letters-where-numbers-expected,special-chars,extended-Unicode,emojis,control-chars,null/undefined/NaN,strings-with-spaces,data-in-unexpected-formats

**Extreme-volumes:**zero-elements,single-element,thousands-or-millions,0-byte-files,extremely-large-files,many-form-fields-filled-simultaneously

### X-Cross-cutting
**Security:**XSS-injection,SQL-injection,CSRF,URL-parameter-manipulation,privilege-escalation,unauthorized-resource-access,plaintext-sensitive-data,cookies-without-security-flags

**Perceived-performance:**normal-load-response,slow-connection,multiple-rapid-clicks,multiple-form-submits,infinite-scroll-with-lots-data,heavy-image-loading

**Accessibility:**keyboard-only-navigation,screen-readers,sufficient-color-contrast,alternative-image-texts,visible-focus,logical-tab-order,form-labels,accessible-error-messages

**Compatibility:**different-browsers,screen-resolutions,dark/light-mode,vertical/horizontal-orientation,browser-zoom,active-ad-blocker,disabled-JavaScript

### P-User-Perception(UX)
**Non-obvious-usability:**flow-with-interruptions,browser-back-button-mid-flow,same-page-multiple-tabs,copy-paste-in-restricted-fields,drag-elements-unexpected-zones,resize-during-operation,change-language-during-use,print-page

**Feedback+communication:**understandable-error-messages,clear-required-field-indication,confirmation-before-destructive-actions,visual-feedback-progress,successful-save-indication,data-recovery-on-connection-loss

### L-Business-Logic
**Business-rules:**explicit+implicit-rule-validation,field-interdependency,derived-calculations,validation-sequences,conditional-states,referential-integrity

**Complex-flows:**multipath-navigation,conditional-branching,role-dependent-flows,sequential-step-dependencies,partial-completion-save

### O-Concurrent-Operations+State
**Concurrency:**simultaneous-operations-same-resource,race-conditions,state-conflicts,optimistic/pessimistic-locking,transaction-management

**State-management:**state-transitions,session-persistence,cache-consistency,browser-history,local-storage,cookies

### R-Resilience+Recovery
**Error-handling:**input-validation-errors,server-errors,network-errors,timeout-handling,graceful-degradation,user-error-communication

**Recovery:**network-interruption-recovery,data-loss-recovery,session-recovery,automatic-retry,rollback-mechanisms

### A-Adversarial/Antagonist
**Malicious-use:**system-abuse,social-engineering,malicious-input,security-bypass,automated-attack-scripts,resource-exhaustion

**Boundary-exploration:**permission-limits,restriction-bypass,API-manipulation,unauthorized-state-changes
