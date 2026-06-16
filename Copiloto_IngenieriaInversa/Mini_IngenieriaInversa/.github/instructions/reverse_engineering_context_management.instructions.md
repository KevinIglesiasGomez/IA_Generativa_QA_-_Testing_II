# Context-Management+Compacting-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-how-agent-must-manage-state-persistence+context-recovery-during-reverse-engineering-process,especially-when-conversation-compacted(manual-with-`/compact`-or-automatically-by-context-limit).

---

## 1. STATE-PERSISTENCE-IN-SESSION-MEMORY

### Mandatory-Save-Moments

Agent-MUST-save-analysis-state-in-`/memories/session/reverse_engineering_state.md`-at-these-moments:

1.**On-completing-Phase-0**(approved-discovery)-Save:PROJECT_ROOT,technology,module-map,epic/story-classification,chosen-mode
2.**On-approving-each-story**-Update:story-progress,new-questions,next-step
3.**Before-suggesting-`/compact`**-Save-complete-snapshot-with-all-accumulated-info
4.**On-generating-each-file**-Register:generated-filename,path,approval-status

### State-File-Format

```markdown
# Reverse-Engineering-Analysis-State

## Project
-PROJECT_ROOT:[path]
-App:[name]
-Technology:[framework+version]
-Mode:[Summary/Complete]
-Current-phase:[0/1/2/3]

## Story-Progress
|Story|Status|Generated-file|
|----------|--------|------------------|

## Accumulated-Questions
|#|Area|Question|
|---|------|----------|

## Last-Action
[Last-completed-action-description+next-step]
```

---

## 2. POST-COMPACT-RECOVERY-PROTOCOL

When-agent-detects-conversation-was-compacted(previous-context-is-summary),must:

1.Read-`/memories/session/reverse_engineering_state.md`-to-recover-complete-state
2.If-general-document-already-generated-exists,read-it-to-recover-story-map
3.Confirm-with-user:"Recovered-analysis-state.We-were-at-[phase/story].Continue?"
4.Resume-work-from-exact-point-where-left-off

---

## 3. SUGGESTED-COMPACTING-POINTS

Agent-must-suggest-user-execute-`/compact`-at-these-flow-moments:

1.**After-completing-Phase-0**(approved-discovery)-map-already-saved
2.**After-each-3-4-approved-stories**-in-Complete-Mode-to-maintain-performance
3.**After-generating-general-document**(before-moving-to-detailed-stories)
4.**Before-starting-complex-epic**-free-context-for-deep-analysis
5.**When-agent-detects-slow-responses**-or-extensive-context

---

## 4. USER-SUGGESTION-FORMAT

Agent-MUST-use-following-format-when-suggesting-`/compact`.Important-message-is-clear,visible+reassures-user-about-operation-safety:

```
---
**📦 COMPACTING-SUGGESTION**

[X]-histories/phases-processed-since-last-save-point.
-Session-memory-saved-state:✅
-Current-phase:[phase]
-Next-step:[description]

You-can-execute-`/compact`-to-free-context+maintain-performance.
After-compacting,will-auto-recover-state-from-session-memory.**No-info-will-be-lost.**
---
```

### When-MANDATORY-to-Show-This-Message

1.On-completing-Phase-0(approved-discovery)
2.Each-3-4-approved-stories-in-Complete-Mode
3.On-completing-general-document(before-Step-2)
4.Before-starting-complex-epic
5.When-agent-detects-slow-responses-or-extensive-context

---

## 5. CRITICAL-INFO-TO-PRESERVE

Agent's-`chatSummary`-property-defines-which-info-preserved-during-automatic-compacting.Critical-data:

1.PROJECT_ROOT:analyzed-project-path
2.App-name(`<App>`)+identified-technology
3.Complete-module-map-with-classification(Epic/Story)+status(pending/completed/in-progress)
4.Current-analysis-phase(0-Discovery,1-General,2-Detail,3-Specific-story)
5.Chosen-generation-mode(Summary/Complete)
6.Already-approved-stories+generated-filenames
7.Pending-stories-to-document
8.Questions-table-accumulated-so-far
9.Last-analyzed-story+approval-status
10.User-decisions-about-epic-decomposition
11.Corrections/adjustments-requested-by-user-affecting-future-stories

Session-memory(`/memories/session/`)-acts-as-additional-safety-net:persists-outside-context-window+never-lost-even-if-aggressively-compacted.
