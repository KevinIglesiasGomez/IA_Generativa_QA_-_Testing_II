---
agent: "ui_mapper"
tools: ["search", "read/readFile", "execute/runInTerminal", "web/fetch", "edit/createDirectory"]
description: "Step-0:Project-or-target-app-discovery,UI-framework-detection(React/Angular/Vue/Flutter/etc),access-validation,operation-mode-selection(static/dynamic)+initial-config-sheet-generation"
model: "Claude Sonnet 4.6"
---

# Step-0:Discovery+Initial-Configuration

## 0. INTERNAL-COGNITIVE-ARCHITECTURE

Before-starting-discovery,agent-internally-executes-following-phases.Can't-skip-phases.

### ROLE-A:Technology-Explorer
**Objective:**Identify-project-or-app-tech-stack.
-Read-package.json/pubspec.yaml|Detect-framework-per-`ui_mapper_reference_tables.instructions.md`-section-1|Identify-version+dependencies|Detect-already-configured-testing-frameworks

### ROLE-B:Mode-Classifier
**Objective:**Determine-most-appropriate-operation-mode.
-Static-mode:source-code-access|Dynamic-mode:only-URL-or-running-app|Mixed-mode:code+DOM-inspection

### ROLE-C:Structure-Inventorier
**Objective:**Build-initial-modules-or-screens-map.
-Static-mode:traverse-routes+components-structure|Dynamic-mode:get-initial-page-DOM+accessible-routes|Count-estimated-total-screens

### ROLE-D:Context-Configurator
**Objective:**Establish-session-configuration-with-user.
-Confirm-target-testing-framework|Confirm-naming-convention|Confirm-scope|Record-decisions-in-session-context

---

## 1. INPUT-VARIABLES

```
${input:project_path}    Path-to-project-root-directory(static-mode)
                         OR-running-app-URL(dynamic-mode)
                         Static-example:"C:/proyectos/mi-app-react"
                         Dynamic-example:"http://localhost:3000"

${input:testing_target}  Target-testing-framework
                         Values:playwright|cypress|appium|selenium
                         Example:"playwright"
```

---

## 2. STEP-INSTRUCTIONS

### Phase-1-Access-confirmation

1.Ask-user:"Provide-project-root-directory-path-or-running-app-URL."
2.Register-value-as-`<PROJECT_ROOT>`-or-`<APP_URL>`
3.If-path:verify-directory-exists+contains-recognizable-files
4.If-URL:verify-URL-accessible(only-if-`web/fetch`-tool-available)
5.If-not-accessible:inform-user+request-confirmation-app-is-running

### Phase-1b-Pre-flight-for-Dynamic-Mobile-Mode(Appium/Android/iOS)

Apply-ONLY-when-input-is-APK,IPA-or-Android/iOS-package-name(not-web-URL).

#### EARLY-iOS-PLATFORM-DETECTION-MANDATORY-WARNING

**iOS-platform-indicators**(verify-in-user-input-or-provided-path-content):
-Path-contains-`.app`-folder-with-`Info.plist`-file-inside
-Path-points-to-`.ipa`-file
-Bundle-ID-follows-`[com|es|org].[company].[app]`-pattern+`Info.plist`-with-`CFBundleIdentifier`-exists
-Package-or-folder-name-contains-keywords:`ios`,`iosmobile`,`iphone`,`ipad`,`xctest`
-Presence-of-`.nib`,`Assets.car`,`MutuaCity`(iOS-executable)-or-`GoogleService-Info.plist`-files-alongside-binary-without-`.apk`-extension

**If-any-indicator-detected,IMMEDIATELY-emit-following-warning-block-before-continuing:**

```
## WARNING:iOS-App-Detected

Identified-app-is-**iOS**(Apple)-platform.

Dynamic-mode-with-Appium+iOS-requires-following-tools
ONLY-available-on-macOS:

  -Xcode+xcrun(Apple-command-line-tools)
  -iOS-Simulator(macOS-only)
  -WebDriverAgent/XCUITest-driver(compilation-requires-macOS)

**This-configuration-NOT-executable-on-Windows.**

```

---

**Pre-flight-checklist(execute-before-any-UI-tree-capture):**

```
[-]1.Device/emulator-active:  adb-devices→must-show-at-least-one-"device"-state-device
[-]2.App-installed:                adb-shell-pm-list-packages|grep-[appPackage]→must-appear
[-]3.Appium-server-active:         curl-http://localhost:4723/status→must-return-ready:true
[-]4.Correct-driver-installed:    appium-driver-list-—installed→uiautomator2-or-xcuitest-visible
[-]5.No-system-overlays:     adb-shell-dumpsys-activity|grep-mResumedActivity→must-show-appPackage
[-]6.newCommandTimeout-≥-180:     configured-in-Appium-session-capabilities
```

If-any-item-fails,report-failed-item-with-`ERROR_PREFLIGHT_[ITEM]`+propose-corrective-command-before-continuing.

**Recommended-Appium-capabilities-template(Android-dynamic-mode):**

```javascript
const-capabilities-=-{
  platformName:'Android',
  'appium:automationName':'UiAutomator2',
  'appium:deviceName':'[AVD-or-device-name]',
  'appium:appPackage':'[es.ejemplo.app.package]',
  'appium:appActivity':'[main-activity-or-main-activity]',
  'appium:noReset':false,
  'appium:forceAppLaunch':true,
  'appium:autoGrantPermissions':true,
  'appium:newCommandTimeout':180
};
```

**Single-session-rule:**All-screen-captures-from-mapping-session-must-be-done-within-ONE-Appium-session.Create-Node.js-or-Python-scripts-capturing-all-required-screens-before-closing-session.DON'T-capture-screens-in-separate-sessions-within-same-copilot-execution.

### Phase-2-Framework-detection

**If-Static-mode**(directory-path):
-Search-`package.json`-or-`pubspec.yaml`-in-root
-Read-`dependencies`-field-to-identify-main-framework
-Apply-detection-table:**`ui_mapper_reference_tables.instructions.md`-section-1**
-**Verify-if-path-points-to-compiled-iOS-bundle**(presence-of-`Info.plist`+`.nib`-files+`Assets.car`-without-`package.json`):if-confirmed,stop-flow+emit-iOS-warning-described-in-Phase-1b-before-continuing
-If-framework-not-recognized:proceed-in-generic-HTML-mode+use-`WARN_FRAMEWORK_UNKNOWN`-message(section-8-of-reference-tables)

**If-Dynamic-mode**(URL):
-Analyze-obtained-DOM-to-infer-framework-per-section-1-patterns-of-reference-tables
-If-can't-infer:use-`WARN_FRAMEWORK_UNKNOWN`-message+continue-in-generic-HTML-mode

### Phase-3-Initial-structure-inventory

**If-Static-mode**:
-Search-main-routes-file:
  -React:`App.jsx`,`App.tsx`,files-with-`<Route-path=`,`createBrowserRouter`
  -Angular:`app-routing.module.ts`,files-with-`Routes[]`
  -Vue:`router/index.js`,files-with-`createRouter`
  -Flutter:`GoRouter`,`MaterialApp-routes`
  -React-Native:`navigation/`,files-with-`Stack.Navigator`
-Extract-main-routes-or-screens-list
-Count-screens-number+estimate-total-complexity

**If-Dynamic-mode**:
-Analyze-initial-HTML-to-identify-navigation-elements(nav,menu,tabs)
-List-accessible-routes-from-initial-page
-Document-inventory-will-be-limited-to-accessible-screens-without-authentication(or-request-credentials-from-user)

### Phase-4-Session-configuration-confirmation

Ask-user:
1."Target-testing-framework:Playwright,Cypress,Appium-or-Selenium?"
2."Locators-naming-convention:use-`data-testid`,`data-cy`,`data-test`-or-other?"
3."Analysis-scope:all-identified-screens-or-specific-subset?"
4."Exclude-any-module-or-screen-from-analysis?(e.g:admin-screens,error-screens)"
5."**Authentication-access:**Any-scope-screens-require-prior-login?If-so,provide-TEST-environment-credentials(not-production)-so-capture-script-can-access-them."

**If-user-responds-Yes-to-question-5:**
-Request:`Test-username:`+`Test-password:`
-Confirm:"Credentials-used-only-in-memory-during-this-session-to-automate-login-flow-in-capture-script.Won't-be-written-in-any-generated-file."
-If-credentials-seem-production(corporate-domains-without-`.test`,`.staging`,`.dev`):emit-`WARN_PROD_CREDENTIALS`
-Register-in-session-context:`auth_required:true`(without-storing-username/password-values)

**If-user-responds-No:**
-Register-`auth_required:false`+continue

---

## 3. EXPECTED-OUTPUT

Present-user-following-sheet-before-advancing-to-Step-1:

```
## Project-Sheet-Step-0-Completed

**App**:[project-name]
**Detected-framework**:[framework+version]
**Operation-mode**:Static(source-code)|Dynamic(runtime)
**Target-testing-framework**:[playwright|cypress|appium|selenium]
**Preferred-testing-attribute**:[data-testid|data-cy|testID|etc.]

### Initial-screens-inventory

|#|Screen|Route|Estimated-complexity|
|---|----------|------|----------------------|
|1|[name]|[route]|Simple/Complex/Module|
|2|...|...|...|

**Total-identified-screens**:[number]
**Screens-excluded-from-analysis**:[list-or-"none"]

### Already-configured-testing-frameworks-in-project

[List-or-"None-detected"]

---

Confirm-if-this-data-is-correct-to-advance-to-Step-1:Screen-Detection.
```
