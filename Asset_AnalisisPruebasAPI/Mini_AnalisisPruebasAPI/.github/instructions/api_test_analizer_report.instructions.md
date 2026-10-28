# Report Generation Instructions: API Test Quality Analizer

## 1. REPORT

Before-interacting-with-engineer,generate-report-per-page/component/feature:

-format:Markdown
-directory:new-"informes/"-in-**workspace-root**
-file-name:"informe_[page_component_name].md"(ex:informe_login.md)
-functional-description:page/component
-identified-elements(forms|buttons|lists|etc)
-ALL-existing-tests
-ALL-detected-risks|gaps(UNIFIED-model)
-coverage-achieved-per-category
-DO-NOT-include-proposed-scenarios-in-report
-report-must-be-extensive-without-limitations

### 1.1 Report-Update

1.**MANDATORY**:At-end-of-each-engineer-work-session,update-**initial-report**-with-new-added-tests.
Process-must-be-done-BEFORE-closing-session+include:
  -add-new-implemented-scenarios-in-"EXISTING-TESTS"-with-appropriate-subsections-per-category
  -update-coverage-percentages-showing-comparison"Previous-Coverage"vs"Current-Coverage"
  -update-global-coverage-showing-progression(ex:**47%**→**52%**)
  -mark-as-"MITIGATED-GAP"or"PARTIAL-COVERAGE"-detected-risks-that-were-resolved|improved
  -update-prioritization
  -**initial-report**-MUST-NOT-have-"next-steps"-section-NOR-update-dates=>this-info-must-stay-in-**changelog**-to-avoid-overloading-report-with-temporal-info-that-may-hinder-long-term-readability+comprehension

2.Additionally-per-new-page/component/feature-worked,generate-another-Markdown-file-as-**changelog**-where-changes-made,tests-added,risks-detected|mitigated,coverage-percentages-achieved-are-recorded.
Objective:maintain-detailed-history-of-test-suite-evolution-over-time-without-**initial-report**-growing-uncontrollably.
This-changelog-must-be-clear,organized,without-too-much-verbose.
Update-this-changelog-at-each-important-decision-during-session,such-as:
  -new-test-scenario-implementation
  -new-risk|gap-identification
  -existing-risk-mitigation
  -significant-coverage-percentage-update

3.**Verification**:Before-ending-session,confirm:
  -**initial-report**-reflects-ALL-tests-implemented-in-session
  -coverage-percentages-updated
  -mitigated-gaps-correctly-marked
  -prioritization-reflects-current-state
  -**changelog**-synced-with-**initial-report**

## 1.2 Report-Generation-Update-Rules

-Before-generating-anything,check-if-report-already-exists-for-that-page/component=>if-yes:update-instead-of-create-new
-**initial-report**-must-NOT-maintain-change-history=>this-history-must-be-kept-in-**changelog**-files,clearly-indicating-which-tests-were-added-in-each-engineer-work-session
-**initial-report**-must-be-clear+organized,facilitating-understanding-of-test-suite-evolution-over-time
-**CRITICAL**:Must-update-"Detected-risks"-section-in-each-session,reflecting-any-new-risk-identified|mitigated-with-added-tests+coverage-percentages-achieved-with-new-implemented-tests
-**IMPORTANT**:POISED-coverage-table-must-show:
  -"Previous-Coverage"-column-with-initial-percentage
  -"Current-Coverage"-column-with-percentage-after-implementations
  -improvement-indicators(+X%)-in-descriptions
  -global-coverage-with-format:**X%**→**Y%**(+Z-percentage-points)
-"Gaps-prioritization"-section-must:
  -strike-through-~~text~~-fully-implemented-items
  -mark-with-✅-before-struck-item
  -mark-with-⚠️-partially-implemented-items
  -include-reference-to-scenario-number-in-parentheses(Scenario-X)
-Must-NOT-exist-"Next-steps"-section-in-**initial-report**=>this-info-must-stay-in-**changelog**-to-avoid-overloading-report-with-temporal-info-that-may-hinder-long-term-readability+comprehension
-If-**changelog**-becomes-too-extensive,consider-organizing-it-in-sections|subsections-to-maintain-clarity
-If-changing-page/component/feature,generate-new-specific-**initial-report**,maintaining-same-format+structure-as-previous-report+new-**changelog**-for-that-page/component/feature
-changelog-file-name:"bitacora_[page_component_name].md"(ex:bitacora_login.md)

## 1.3 Session-End-Verification

Before-finalizing-work-session,verify-completed-**initial-report**+**changelog**-update.
