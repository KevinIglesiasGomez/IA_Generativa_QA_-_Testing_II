# Report-Generation-Instructions:Creative-Tester-Agent

## 1.Report

After-completing-full-analysis+generating-all-creative-scenarios,generate-**concise+actionable-report**-per-page/component/functionality-analyzed.

-Markdown-format
-New-directory-"informes/"-at-**workspace-root**
-Filename:`informe_<page_component_name>.md`
-**Recommended-max-extension**:4-6-printed-pages
-Prioritize-quality-over-quantity:focus-on-highest-value-scenarios
-Visual+scannable-format:use-tables,lists+clear-structure
-Complete-details-only-for-high-priority-scenarios(score>=6.0)
-Medium/low-priority-scenarios-in-compact-table-format

### 1.1-Report-Structure(Simplified)

```markdown
# Creative-Testing-Report:<name>

**Source**:<screenshot/documentation/code/HTML>|**Date**:<date>|**Complexity**:<low/medium/high>

## 1.Description+Key-Elements
<Brief-functional-description(2-3-paragraphs)+main-identified-elements>

## 2.EXPLORA-Coverage-Summary

|Category|Risks|Scenarios|Priority|
|---|:---:|:---:|---|
|E-Extremes+Limits|X|Y|High/Medium/Low|
|X-Cross-cutting|X|Y|High/Medium/Low|
|P-User-Perception|X|Y|High/Medium/Low|
|L-Business-Logic|X|Y|High/Medium/Low|
|O-Concurrent-Operations|X|Y|High/Medium/Low|
|R-Resilience|X|Y|High/Medium/Low|
|A-Adversarial|X|Y|High/Medium/Low|
|**TOTAL**|**X**|**Y**|-|

## 3.Top-10-15-Main-Risks
<Only-most-critical-risks-with-score>=6.0,ordered-highest-to-lowest>

## 4.Creative-Scenarios(only-high-priority)

### Scenario-X:<title>
**Category**:<E/X/P/L/O/R/A>|**Priority**:<score>|**Confidence**:<X%>

**What-to-test**:<brief-description-in-1-2-lines>

**Steps**:
1.<concise-step>
2.<concise-step>
3....

**Expected-result**:<brief-description>
**Risk-mitigated**:<brief-description>

---

## 5.Additional-Scenarios(medium/low-priority)

<Compact-listing-in-table-format>

|#|Title|Category|Priority|Brief-Description|
|---|---|---|---|---|
|X|...|E|5.2|...|
|Y|...|P|4.8|...|

## 6.🚀-Extreme+Unexpected-Tests(5-8-scenarios)

<Creative-"very-crazy"-scenarios-challenging-assumptions+exploring-improbable>

### 🚀-Extreme-Test-X:<provocative-title>
**Type**:<Chaotic-User/Temporal/Multilanguage/Absurd-Hacker/etc.>
**Probability**:Extremely-low|**Impact**:<Low/Medium/High/Critical>

**Scenario**:<Brief-description-absurd-situation>

**How-to-execute**:
1.<Concise-step>
2.<Concise-step>

**What-could-break?**:<Brief-speculation>
**Value**:<What-assumption-challenges>

---

## 7.Recommendations
-<Top-3-5-concise-recommendations>
```

### 1.2-Report-Update

1.Report-generated-once-complete+concise-with-prioritized-scenarios.

2.If-future-updates-required-or-want-to-add-new-scenarios,can-generate-additional-**log**-file-to-record-incremental-changes.
   -Filename:`bitacora_<page_component_name>.md`
   -This-file-optional+only-created-if-updates-after-initial-report.

3.**Initial-report**-must-be-concise,actionable+focused-on-high-priority-scenarios.

## 1.3-Report-Generation-Rules

-**Prioritize-quality-over-quantity**:Focus-on-highest-value-scenarios(priority>=6.0)
-**Complete-details-only-for-high-priority**:Scenarios-with-score>=6.0-must-have-all-detailed-steps
-**Medium/low-priority-scenarios**:Compact-format-in-summary-table
-**Recommended-limit**:10-20-scenarios-with-complete-detail+summary-table-with-rest
-**Risks**:Only-show-top-10-15-most-critical-risks,not-all-detected
-Report-must-be-clear,concise+actionable
-Avoid-repetition:don't-detail-same-info-in-multiple-sections
-Use-visual-format(tables,lists)-for-quick-reading
-Before-generating,verify-if-report-already-exists-for-that-page/component
-If-changing-page/component/functionality,must-generate-new-specific-report

## 1.4-Conciseness-Principles

-**Brevity**:Functional-description-in-2-3-paragraphs-max
-**Focus**:Prioritize-creative-scenarios-over-exhaustive-documentation
-**Balanced-coverage**:10-20-detailed-scenarios-for-adequate-coverage-without-being-exhaustive
-**Readability**:Use-format-allowing-quick-scan(tables,bullets,clear-titles)
-**Actionability**:Each-scenario-must-be-clear+executable-without-ambiguities
-**Noise-elimination**:Don't-include-info-not-adding-direct-value-to-tests

## 1.5-Verification-Before-Delivering-Report

Before-delivering-report-to-engineer,verify:
-✅Reasonable-length:report-shouldn't-exceed-4-6-printed-pages
-✅Top-scenarios-highlighted:10-20-highest-priority-scenarios-have-complete-detail
-✅Calculated-scores:priorities-correctly-assigned(>=6.0-for-high)
-✅Consistent+visual-format:uses-tables+lists-for-quick-reading
-✅No-redundant-info:each-data-appears-only-once
-✅Actionable:anyone-can-execute-scenarios-without-ambiguities
