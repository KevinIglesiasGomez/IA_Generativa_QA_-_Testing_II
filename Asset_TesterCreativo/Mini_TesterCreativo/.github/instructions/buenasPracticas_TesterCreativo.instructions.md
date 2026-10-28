# Best-Practices-Instructions:Creative-Tester-Agent

## 1.Mandatory-Best-Practices

### 1.1-Scenario-Foundation
-Each-creative-scenario-must-be-technically-justified
-Don't-propose-tests-just-for-originality;must-add-real-value
-Link-each-scenario-to-concrete-identified-risk
-Avoid-redundant-tests-covering-same-risk-from-same-angle

### 1.2-Scenario-Independence
-Each-scenario-must-execute-in-isolation
-Don't-depend-on-other-scenario-results
-Define-clear-preconditions-per-case
-Don't-assume-undeclared-previous-state

### 1.3-Reproducibility
-Steps-detailed-enough-for-anyone-to-execute
-Avoid-ambiguous-instructions-like-"test-different-values"
-Specify-concrete-test-data-when-necessary
-Indicate-required-initial-system-state

### 1.4-Traceability
-Each-scenario-unique-identifier
-Link-to-corresponding-EXPLORA-category
-Indicate-info-source-derived-from(screenshot,document,code,HTML)
-Record-creative-technique-used

### 1.5-Realism
-Don't-propose-tests-requiring-nonexistent-tools
-Ensure-scenario-executable-with-reasonable-resources
-Don't-invent-functionalities-or-behaviors-not-deducible-from-input
-Consider-environment-technical-limitations

### 1.6-Cost-Benefit-Balance
-Evaluate-execution-effort-vs-detection-value
-Prioritize-high-impact-scenarios-with-low-execution-cost
-Mark-costly-scenarios-applicable-only-in-critical-contexts
-Don't-generate-more-scenarios-than-team-can-manage

### 1.7-Report-Conciseness
-**Maximum-4-6-pages**:report-must-be-quickly-scannable
-**10-20-detailed-scenarios**:only-high-priority(score>=6.0)
-**Rest-in-compact-table**:summary-format-for-secondary-scenarios
-**Avoid-redundancy**:each-info-appears-once
-**Top-risks**:show-only-10-15-most-critical-risks
-**Visual+structured**:use-tables+lists-for-easy-reading

## 2.Cross-Cutting-Aspects

### 2.1-Accessibility
-Keyboard-only-navigation
-Screen-reader-compatibility
-Color-contrast(WCAG-2.1-level-AA-minimum)
-Alternative-texts-non-textual-content
-Logical-tab-order
-Form-field-associated-labels
-Error-messages-communicated-to-assistive-technologies
-Minimum-interactive-area-size(44x44-px)

### 2.2-Internationalization(i18n)
-Non-Latin-alphabet-characters(Cyrillic,Arabic,Chinese,Japanese)
-RTL-texts(right-to-left)
-Date-formats-by-locale
-Numeric-formats(decimal-separator,thousands-separator)
-Currencies+symbols
-Correct-pluralization
-Strings-expanding-significantly-when-translated(German,Finnish)

### 2.3-Privacy+Personal-Data
-Sensitive-data-not-visible-in-logs-or-URLs
-Masked-password-fields
-Sessions-expire-correctly
-Option-to-delete-personal-data(right-to-erasure)
-Explicit-consent-for-data-collection

### 2.4-Perceived-Performance
-Acceptable-initial-load-time
-Visual-feedback-during-slow-operations
-Above-the-fold-content-loads-first
-No-interface-blocking-during-processing
-Progress-indicators-long-operations

### 2.5-Consistency
-Uniform-terminology-throughout-application
-Predictable-behavior-similar-elements
-Error-messages-consistent-format+tone
-Repeated-interaction-patterns(confirmation-before-delete,etc.)
-Coherent-visual-hierarchy

## 3.Antipatterns-to-Avoid

### 3.1-Scenario-Generation
-Don't-generate-generic-scenarios-without-specific-context
-Don't-copy-test-lists-from-templates-without-adaptation
-Don't-propose-same-scenario-with-insignificant-variations
-Don't-ignore-business-context-when-proposing-technical-tests
-Don't-generate-impossible-to-verify-scenarios
-**Don't-generate-too-many-scenarios**:quality-over-quantity(10-20-detailed-offers-good-coverage)

### 3.2-Engineer-Communication
-Don't-present-overwhelming-reports-with-dozens-detailed-scenarios
-Don't-omit-technical-justification-for-scenario
-Don't-mix-priority-levels-without-clear-context
-Don't-use-technical-jargon-without-explanation-when-necessary
-**Don't-generate-reports-over-4-6-pages**:maintain-conciseness-with-adequate-coverage

### 3.3-Documentation
-Don't-leave-uncategorized-scenarios
-Don't-omit-critical-preconditions-in-high-priority-scenarios
-Don't-use-ambiguous-or-incomplete-steps
-Don't-forget-expected-result
-**Don't-exhaustively-document-low-priority-scenarios**:use-compact-table
-**Don't-include-redundant-info**:each-data-appears-once
