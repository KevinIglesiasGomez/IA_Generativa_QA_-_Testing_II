---
agent: "Gherkin-Scenario-Generator"
description: "Analyze-documentation+generate-BDD-use-cases"
---

### Step-2:External-Tools-Integration(Optional)

**MCP-Service-Validation:**
First,verify-if-MCP(Model-Context-Protocol)-service-active+configured-for-external-integrations.

If-MCP-available+configured,collect-additional-project-context-from-external-tools-using-variables:

-**${input:project_reference}**:Unique-project-identifier
-**${input:mcp_service}**:Specific-MCP-service-to-use

**Auto-Detection-Logic:**
Based-on-provided-`${input:project_reference}`+using-specified-`${input:mcp_service}`,auto-detect-type+perform-appropriate-queries:

1.**Azure-DevOps-Pattern-Detection:**
   -Format:`https://dev.azure.com/{organization}/{project}`-or-`{organization}/{project}`
   -Auto-query:Work-items,repositories,boards+documentation

2.**Jira/Confluence-Pattern-Detection:**
   -Format:`https://{domain}.atlassian.net/browse/{project-key}`-or-`{project-key}`
   -Auto-query:Issues,epics,stories+Confluence-pages

3.**SharePoint-Pattern-Detection:**
   -Format:`https://{tenant}.sharepoint.com/sites/{site}`-or-direct-URL
   -Auto-query:Document-libraries+lists

4.**Generic-URL-Pattern-Detection:**
   -Format:Any-valid-URL-containing-project/workspace-identifiers
   -Auto-query:Available-endpoints+documentation-sources

**Automated-Data-Collection:**

-**Work-Items+Issues**:Auto-retrieve-user-stories,requirements,tasks,epics+tickets
-**Documentation-Sources**:Auto-discover+analyze-functional-specs,technical-docs+knowledge-articles
-**Swagger+APIs**:Auto-extract-endpoint-details,parameters+API-responses
-**Code-Repositories**:Auto-detect+cross-reference-code-structure+documentation
-**Project-Metadata**:Extract-organization,workspace+project-details-from-reference

**Integration-Guidelines:**

-**Validate-MCP-Service**:Verify-MCP-service-active-before-attempting-external-integrations
-**Auto-Detect-Platform**:Analyze-`${input:project_reference}`-pattern-to-identify-external-system-type
-**Intelligent-Discovery**:Auto-discover-available-endpoints+data-sources-based-on-detected-platform
-**Adaptive-Query**:Perform-platform-specific-queries-to-collect-relevant-project-information
-Use-external-data-to-**complement**-local-documentation-analysis
-**Cross-validate**-requirements-between-local-docs+external-systems
-**Prioritize**-use-cases-based-on-external-work-item-priorities
-**Align**-BDD-scenarios-with-external-acceptance-criteria-when-available
-If-MCP-not-active,platform-detection-fails,or-external-tools-unavailable,proceed-with-local-documentation-only

### **MCP-Playwright(if-available):**
Application-Exploration-Flow: 

#### Application-Access:

1.Navigate-to-web-app-URL:`${input:URL}`.
2.Ensure-application-loads-successfully.
3.Analyze-HTML-structure+identify-key-elements.
4.Click-each-link+button-to-explore-navigation-flow.
5.Interact-with-forms,dropdowns,modals+other-UI-components-to-understand-behavior.
6.Use-browser-dev-tools-to-inspect-elements,network-requests+console-logs-for-deeper-functionality-insight.

Note:If-any-application-access-issues,report-immediately.
Note:Application-may-be-legacy-with-quirks,be-patient+thorough-in-exploration.

#### Application-Exploration:

1.Login-with-credentials-if-needed:
   -User:`${input:username}`
   -Password:`${input:password}`
2.Familiarize-with-main-features+navigation-structure.Read-HTML-code-to-identify-elements,iframes,javascript-actions,etc.
3.Application-may-have-multiple-sections/modules;note-any-specific-workflows/functionalities-that-stand-out.
4.Take-screenshots/record-navigation-if-needed-for-reference.
5.Capture-element-locators-relevant-for-BDD-scenarios.
6.Ask-any-questions-about-application-to-clarify-understanding.
