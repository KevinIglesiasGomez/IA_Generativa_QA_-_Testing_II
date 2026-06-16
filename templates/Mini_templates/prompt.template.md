---
agent: "AgentName"
tools: ["edit/editFiles", "search", "runCommands"]
description: "Prompt-purpose"
model: "Claude Sonnet 4.5"
---

# Prompt:Prompt-Name

## 0.AGENT-INTERNAL-ARCHITECTURE
<!-- OPTIONAL:Remove-complete-section-if-agent-doesn't-require-structured-cognitive-roles -->

Before-[main-action],agent-must-execute-internally-following-phases.Skipping-phases-not-allowed.

### 0.1-Internal-Cognitive-Roles

#### ROLE-A:[Role-Name]
Objective:[role-objective]

-[Analysis-1]:
-[Analysis-2]:
-[Analysis-3]:

[Important-restriction]

#### ROLE-B:[Role-Name]
Objective:[role-objective]

Per-each-[unit]:
-[Metric-1]:
-[Metric-2]:

[Expected-action]

#### ROLE-C:[Role-Name]
Objective:[role-objective]

-[Critical-question-1]
-[Critical-question-2]

[Acceptance-condition]

#### ROLE-D:[Role-Name]
Objective:[role-objective]

-[Impact-1]:
-[Impact-2]:
-[Classification-system]:
   Level-A→[Description]
   Level-B→[Description]
   Level-C→[Description]
   Level-D→[Description]

## 1.PREREQUISITES+CONTEXT

### 1.1-Required-Instruction-Files

**[standards-type]-SOURCE**:This-prompt-requires-following-ALL-instructions-defined-in-instruction-files,containing-[brief-description].

### 1.2-Project-Context

You-act-as-[agent-role].

Will-provide-[project-type]-in-one-formats:
-[Format-1]
-[Format-2]
-[Format-3]

Your-task:
1.[Task-1]
2.[Task-2]
3.[Task-3]

## 2.MANDATORY-[PROCESS-NAME]-PROCESS

### 2.1-Mandatory-First-Step:Initial-Confirmation

Before-[main-action],must-ask:
1.[Question-1]
2.[Question-2]
3.[Question-3]

Once-confirmed,proceed-to-detailed-analysis.Don't-propose-changes-without-prior-analysis.

### 2.2-Deep-Project-Analysis

When-confirmed,must:
-[Aspect-to-analyze-1]
-[Aspect-to-analyze-2]
-[Aspect-to-analyze-3]
-[Aspect-to-analyze-4]
-[Aspect-to-analyze-5]

### 2.3-Validated-Proposal

Proposal-format:

### [Work-unit]:<name>

Current-state:
-[What-to-describe]

Detected-risks/gaps:
-[What-to-describe]

Proposal:
-[Metric-1]:
-[Metric-2]:
-[Metric-3]:

Proposed-code/artifact:
```
[code-or-structure]
```

Approval:
[Approval-question]

## 3.WORKFLOW-SUMMARY

1.[Step-1]
2.[Step-2]
3.[Step-3]
4.[Step-4]
5.[Step-5]
   5.1.[Optional-sub-step-1]
   5.2.[Optional-sub-step-2]

**IMPORTANT**:[Note-on-deviation-handling]

## 4.INTERACTIVE-FLOW
<!-- OPTIONAL:Remove-if-agent-doesn't-require-step-by-step-approval -->

Agent-must-always-follow-this-pattern:
1.[Step-1]
2.[Step-2]
3.Propose-individual-scenario
4.Ask:"[approval-question]"
5.Continue-only-if-approves
6.If-rejects:[rejection-handling]

Never-generate-multiple-proposals-without-individual-approval.

## 5.OUTPUT-FORMAT

Always-structure:
-[Section-1]
-[Section-2]
-[Section-3]

SHOW-proposed-[code/artifact],not-just-description.

## 6.USER-INTERACTIVE-COMMANDS
<!-- OPTIONAL:Remove-if-no-specific-commands -->

-**[Command-1]**-[Description]
-**[Command-2]**-[Description]
-**[Command-3]**-[Description]

## 7.QUALITY-RULES

-[Rule-1]
-[Rule-2]
-[Rule-3]
-[Rule-4]

## 8.FUNDAMENTAL-PRINCIPLE

[Statement-NOT-desired-objective]

[Statement-YES-desired-objective]

Each-proposal-must-balance:
-[Factor-1]
-[Factor-2]
-[Factor-3]
