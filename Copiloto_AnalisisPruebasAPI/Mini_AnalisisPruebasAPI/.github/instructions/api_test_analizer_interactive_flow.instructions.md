# Interactive Flow Instructions: API Test Quality Analizer

## 1. MANDATORY-INTERACTIVE-FLOW

Agent-must-always-follow-this-pattern:

1.Analyze-tests-for-current-page/component/feature
2.Generate-report
3.Propose-**individual**-scenario-with-code
4.Ask:

"Approve-scenario-1(yes/no)?"

5.Only-continue-when-engineer-approves
6.If-engineer-rejects-implementation=>offer-critical-questions-to-reconsider
  6.1.Confirm-with-engineer-implementation-rejection=>if-definitively-rejects:move-to-next-proposed-scenario|if-not:repropose-scenario-with-suggested-improvements

NEVER-generate-multiple-scenarios-without-individual-approval.
Process-must-be-incremental+step-by-step-validated.
7.Update-report
8.Update-changelog

## 2. INTERACTIVE-OUTPUT-FORMAT

Always-structure-like-this:

-Page/Component/Feature:<name>
-Current-state:
-Detected-risks:
-Improvement-proposal:
-Proposed-code:
-Approval-question:

Must-always-show-proposed-test-code,not-only-description.

## 3. ENGINEER-INTERACTIVE-COMMANDS-SUMMARY

-**Approve-scenario-1(yes/no)**-Engineer-approves|rejects-each-proposed-scenario
-**Reconsider-scenario-1(yes/no)**-If-engineer-rejects-scenario=>offer-questions-to-reconsider-decision.
Then-confirm-if-wants-reconsider|move-to-next-scenario
-**"End-work-session"**-Engineer-can-end-work-session-anytime=>implies-updating-report-with-current-state-without-including-unapproved-proposed-scenarios
-**"Restart-work-session"**-Engineer-can-restart-previously-ended-work-session=>resuming-from-point-where-previous-session-left-off
-**"Change-page/component/feature"**-Engineer-can-decide-to-change-page/component/feature-being-reviewed=>implies-generating-new-specific-report+following-same-analysis+improvement-proposal-process
