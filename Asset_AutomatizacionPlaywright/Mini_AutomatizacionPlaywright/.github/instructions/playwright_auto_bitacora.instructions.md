---
description: Instrucciones para generar la bitacora de automatización de pruebas en Playwright
applyTo: "**/automation_bitacora.md"
---

# Automation Log Instructions for Agent: Playwright Automation

GENERAL-INSTRUCTIONS:
-automation-log=living-doc(update=per-automated-scenario)
-per-scenario:record-challenges/problems+implemented-solutions
-MAINTAIN-record(per-automated-scenario):automated-steps,modified-files,changes-in-business-logic/web-element-locators
-ensure:log-updated+clearly-documented(critical=traceability+future-reference,for=adjustments/corrections)
-log-entries:BRIEF+sufficiently-detailed(any-engineer=understand-process,changes,decisions-made,during=feature=>Playwright-framework-automation)
TODO:skip-non-automated-scenarios(BUT-record-omission-reason-in-log)

LOG-FORMAT:
-format:Markdown
-new-dir:automation_logs/
-single-file(all-work-sessions):automation_logs/automation_bitacora.md(if-not-exists=create,if-exists=update-per-automated-scenario)
-structured-format(clear-sections-per-automated-scenario):
  *Scenario-name:as-in-.feature-file
  *Automation-date:when-scenario-was-automated
  *Challenges-found:brief,any-challenge/problem(during-scenario-automation)
  *Implemented-solutions:brief,solutions/adjustments(to-resolve-challenges)
  *Modified-files:brief,list-of-modified-files(during-scenario-automation:step-definitions,Page-Objects,related-locators)
