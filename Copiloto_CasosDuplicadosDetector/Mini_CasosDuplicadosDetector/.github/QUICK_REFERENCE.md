# Quick Reference: CSV Duplicate Detector

## QUICK-INVOCATION

```
@csv_duplicate_detector

CSV Jira: CSV_example/Jira.csv
CSV Gherkin: CSV/scenarios_all_final.csv
Report: informes/duplicados.md
Clean CSV: CSV/clean.csv
```

---

## INTERACTIVE-MODE-RESPONSES

| Command      | Action                                      |
| ------------ | ------------------------------------------- |
| `yes`\|`sí`  | ✅ Delete case from CSV to import            |
| `no`         | ⛔ Keep case in CSV to import                |
| `skip`       | ⏭️ Decide later (not included in clean CSV) |
| `info`       | ℹ️ See more case details                     |
| `gherkin`    | 📄 Show complete Gherkin scenario            |
| `previous`   | ⬅️ Go back to previous duplicate             |

---

## DUPLICATE-CRITERIA

Case=duplicate-when-meets-AT-LEAST-4-of-5:

1. ✅ same-functional-objective
2. ✅ same-context/component
3. ✅ equivalent-preconditions
4. ✅ similar-main-actions
5. ✅ identical-expected-results

---

## GENERATED-OUTPUTS

1. **MD-Report**: detailed-analysis+decisions
2. **Clean-CSV**: no-duplicates,ready-for-Jira/XRay
3. **Statistics**: process-summary

---

## COPILOT-FILES

```
.github/
├── agents/csv_duplicate_detector.agent.md
├── instructions/csv_duplicate_detection.instructions.md
└── prompts/csv_duplicate_detection.prompt.md
```

---

## DUPLICATE-EXAMPLE

**Jira**: "Validation detects incomplete elements"  
**Gherkin**: "Cannot validate with incomplete data"  
**Duplicates?** ✅ YES - same-functional-objective

---

## COMPLETE-FLOW

```
1. Export Jira cases → Jira CSV
2. Generate Gherkin cases → Gherkin CSV
3. @csv_duplicate_detector → Analysis + Report
4. Interactive mode → Decisions
5. Clean CSV → Import to Jira ✓
```

---

**🎯 OBJECTIVE**: avoid-duplicates-in-Jira+maintain-complete-test-coverage
