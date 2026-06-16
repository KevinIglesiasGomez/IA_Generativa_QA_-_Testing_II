---
description: Flujo interactivo obligatorio para el agente Playwright Automation
applyTo: "**"
---

# Mandatory Interactive Flow for Agent: Playwright Automation

MANDATORY-INTERACTIVE-FLOW:

Agent-MUST-ALWAYS-follow-this-pattern:
0.analyze-framework(complete+in-depth:structure,design-patterns,code-conventions,current-test-coverage)
1.analyze-existing-tests(for-current-page/component/feature)
2.analyze-Gherkin-scenario(to-automate:identify-steps-not-yet-covered,required-data,endpoints-to-consume,any-risk|technical-challenge.Propose-concrete-improvements-to-address-risks|challenges:framework-changes,new-utilities,design-patterns-to-facilitate-implementation)
3.propose-INDIVIDUAL-scenario+code
4.ask:"Approve scenario 1(yes/no)?"
5.ONLY-continue-when-engineer-approves
6.if-engineer-rejects-implementation=>offer-critical-questions(engineer-indicates-rejection-reason+suggests-concrete-improvements-to-proposed-automation)
NEVER-generate-multiple-scenarios-without-individual-approval.Process=incremental+step-by-step-validated.
7.once-approved+implemented=>ASK-BEFORE-EXECUTING:"Implementation ready. Execute test now?(yes/no)"
8.ONLY-after-confirmation=>execute-test(visible-mode,no-headless):
   npx cucumber-js --config cucumber.config.js src/features/Login.feature --tags "@<scenario_tag>"
   OR-equivalent-npm-script-from-project
9.WAIT-FOR-COMPLETE-EXECUTION-FINISH-before-continuing
10.after-execution=>ASK-MANDATORILY:"Test worked correctly?(yes/no/error)"
   -user-responds"yes":update-log+continue-to-next-scenario
   -user-responds"no"|"error":request-error-details|screenshot
   -NEVER-assume-execution-result,ALWAYS-wait-for-user-response
11.if-error-reported-by-user=>follow-failure-protocol(section-4)
12.update-change-log-ONLY-after-success-confirmation

---

INTERACTIVE-OUTPUT-FORMAT:

ALWAYS-structure-as:
-Feature:<name>
-Scenario:<name>
-Current-state:
-Detected-risks:
-Proposed-code:
-Approval-question:

MUST-ALWAYS-show-proposed-test-code(not-just-description)

---

ENGINEER-INTERACTIVE-COMMANDS-SUMMARY:

APPROVAL-COMMANDS:
-"yes"/"approve":approves-proposed-action
-"no"/"reject":rejects-proposed-action
-"error":indicates-execution-error

FLOW-COMMANDS:
-"Approve scenario N(yes/no)":approves|rejects-each-proposed-scenario
-"Reconsider scenario N":requests-improvements-to-proposed-implementation
-"Execute":confirms-test-execution-can-proceed
-"Retry":confirms-re-execution-after-correction
-"Continue":advance-to-next-scenario-after-success
-"stop":stops-current-flow

SESSION-COMMANDS:
-"End work session":closes-session+updates-log
-"Restart work session":resumes-from-last-registered-point
-"Change page/component/feature":shifts-work-focus

IMPORTANT:copilot-MUST-WAIT-for-these-confirmations-before-proceeding.NEVER-assume-user-response.

---

FAILURE+BLOCKER-PROTOCOL:

STRICT-RETRY-PROTOCOL(MANDATORY):

When-scenario-fails-on-execution:

FIRST-FAILURE(Attempt-1):
1.show-exact-error-to-user
2.analyze-root-cause
3.ASK-MANDATORILY:
  "Detected error:[description]
  Identified cause:[cause]
  Correction proposal:[solution]
  Apply this correction?(yes/no)"
4.WAIT-for-user-response
5.ONLY-if-user-approves=>apply-correction
6.ASK-before-re-executing:"Execute test again?(yes/no)"

SECOND-FAILURE(Attempt-2):
1.show-new-error-to-user
2.analyze-if-same-error|different
3.ASK-MANDATORILY:
  "Previous correction did not resolve problem.
  New error:[description]
  Alternative proposal:[solution]
  Apply this alternative correction?(yes/no)"
4.WAIT-for-user-response
5.ONLY-if-user-approves=>apply-correction
6.ASK-before-re-executing:"Execute test again?(yes/no)"

THIRD-FAILURE(Attempt-3):
1.IMMEDIATELY-STOP-any-automatic-attempt
2.present-structured-diagnosis-to-user:
  -exact-observed-error
  -history-of-attempted-corrections
  -probable-root-cause
  -solution-options-with-implications
3.ASK:"How do you want to proceed?"
  -Option-A:try-another-specific-correction
  -Option-B:mark-as-@pendiente+continue
  -Option-C:manual-investigation-needed
4.DO-NOT-apply-any-change-without-explicit-approval

CRITICAL-RULES:
-NEVER-execute-more-than-once-without-asking
-NEVER-assume-correction-will-work
-NEVER-apply-multiple-sequential-corrections(without-confirmation)
-ALWAYS-wait-for-user-response-before-each-action
-ALWAYS-ask-before-re-executing

ESCALATION-PROTOCOL-FOR-BLOCKERS:

Escalate-to-engineer-immediately(without-consuming-attempts)when:
-syntax-error-points-to-module|class-not-existing-in-real-framework
-locator-cannot-be-obtained-from-source-code-available-in-${input:code_folder}
-scenario-requires-access-to-endpoint|data-not-documented-nor-accessible

In-these-cases=>present:
1.blocker-description
2.minimum-info-needed-to-unblock
3.question:"Can you provide this info or how do you want to continue?"

DO-NOT-mark-scenario-as-@pendiente-without-first-informing-engineer-of-reason
