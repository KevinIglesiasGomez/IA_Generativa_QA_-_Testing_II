# Global-Instructions-Demo_MapeoUI

## Workspace-Purpose

This-workspace-contains-**UI-Mapper**-copilot:AI-agent-analyzing-user-interfaces(web-or-mobile)+generating-artifacts-needed-for-test-automation-Page-Objects,locator-files+JSON-UI-maps.

## Workflow(6-Steps)

|Step|Prompt|Description|
|------|--------|-------------|
|0|`/ui_mapper_step0_discovery`|Project-discovery+framework-detection|
|1|`/ui_mapper_step1_screens`|Screens-tree+navigation|
|2|`/ui_mapper_step2_elements`|UI-elements-mapping-per-screen|
|3|`/ui_mapper_step3_selectors`|Selectors-extraction+prioritization|
|4|`/ui_mapper_step4_normalize`|Identifiers-normalization|
|5|`/ui_mapper_step5_artifacts`|Testing-artifacts-generation|

## Naming-Conventions

-**Locator-files:**`<screen>.locators.json`-in-`ui-map/<app>/locators/`
-**Page-Objects:**`<Screen>Page.<ext>`-in-`ui-map/<app>/pages/`
-**Selectors:**prefer-`data-testid`>ARIA-roles>ID>semantic-CSS

## Supported-Frameworks

-**Target-automation:**Playwright,Cypress,Selenium,Appium
-**Platforms:**Web(SPA/SSR),Android(Appium),iOS(Appium/XCUITest)

## Main-Agent

Use-agent-**@ui_mapper**-to-execute-complete-flow.Don't-use-general-chat-for-UI-mapping-tasks.
