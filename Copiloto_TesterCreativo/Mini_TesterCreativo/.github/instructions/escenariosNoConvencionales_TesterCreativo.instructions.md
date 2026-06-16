# Unconventional-Scenarios-Catalog:Creative-Tester-Agent

## 1.Unconventional-Scenarios-by-Application-Type

Agent-must-consider-these-scenarios-according-detected-application-type.Not-all-apply-in-all-cases;select-relevant-ones-according-provided-info.

### 1.1-Form-Applications

**Data-manipulation:**
-Paste-rich-formatted-text(HTML,RTF)-in-plaintext-fields
-Paste-spreadsheet-content-in-text-field
-Use-browser-autocomplete-with-old-or-incorrect-data
-Enter-data-via-password-manager-extension
-Fill-fields-with-voice-dictation
-Drag-text-from-another-app-to-field

**Temporal-behavior:**
-Leave-form-open-for-hours+then-submit
-Fill-form,close-tab-without-submitting,return
-Fill-form-while-auth-session-expires
-Submit-form-just-when-server-in-maintenance
-Change-system-time-during-temporal-validation-flow

**Unexpected-interactions:**
-Fill-field,completely-erase,submit
-Use-browser-autocomplete-to-fill-all-fields
-Press-Enter-in-non-last-form-field
-Use-Tab-to-navigate+activate-cascade-validations
-Click-submit-without-interacting-with-any-field

### 1.2-List+Table-Applications

**Volumes:**
-List-with-exactly-0-elements
-List-with-exactly-1-element
-List-with-exact-page-size-number(e.g:exactly-10,25,50)
-List-with-one-more-element-than-page-size
-List-with-thousands-elements

**Data-operations:**
-Sort-by-column+then-filter:order-maintained
-Filter,paginate,remove-filter:correctly-restored
-Select-elements,change-page,return:selection-maintained
-Delete-last-page-element:pagination-updates
-Edit-element+verify-row-updates-without-reload

**Problematic-content:**
-Cells-with-extremely-long-content(without-truncate)
-Cells-with-special-chars-breaking-layout
-Columns-with-null-or-undefined-values-mixed-with-valid-data
-Rows-with-inconsistent-format-data

### 1.3-Authentication-Applications

**Sessions:**
-Login-in-two-different-browsers-simultaneously
-Logout-in-one-browser+verify-other
-Change-password+verify-active-sessions-invalidate
-Maintain-session-open-beyond-expiration-time
-Access-protected-URL-directly-without-authentication

**Credentials:**
-Login-with-different-uppercase/lowercase-in-username
-Login-with-spaces-before-or-after-username
-Login-with-copied-password-including-trailing-space
-Login-with-newline-character-in-password
-Attempt-multiple-failed-logins+verify-lockout

### 1.4-File-Upload-Applications

**Problematic-files:**
-File-with-changed-extension(rename-.exe-to-.jpg)
-File-with-double-extension(photo.jpg.exe)
-0-byte-file
-File-exceeding-allowed-size-by-1-byte
-File-with-extremely-long-name
-File-with-special-chars-in-name(spaces,accents,symbols)
-File-with-duplicate-name-to-already-uploaded

**Upload-process:**
-Cancel-mid-process-upload
-Lose-connection-during-upload
-Upload-same-file-twice-consecutively
-Drag-multiple-files-when-only-one-allowed
-Paste-from-clipboard(Ctrl+V)-in-upload-zone

### 1.5-Search-Applications

**Unconventional-queries:**
-Search-with-single-character
-Search-with-only-spaces
-Search-with-special-operators(AND,OR,NOT,*,?)
-Search-with-literal-regex-expressions
-Search-with-emojis
-Search-text-existing-in-metadata-but-not-visible-content
-Search-with-accents-vs-without(café-vs-cafe)

**Behavior:**
-Write+erase-quickly(debounce)
-Search,get-results,search-again-without-clearing
-Search-from-URL-with-query-parameter-directly
-Search-in-different-language-than-content

## 2.Inter-Functionality-Interaction-Scenarios

### 2.1-Cross-Effects
-Create-resource-from-page-A,verify-appears-in-page-B
-Delete-resource-referenced-by-another-resource
-Modify-shared-data-between-multiple-views
-Change-user-permissions-while-active-session
-Modify-language-config+verify-affects-all-pages

### 2.2-Action-Sequences
-Perform-same-action-10-times-consecutively(create,delete,create,delete...)
-Execute-actions-in-reverse-expected-order
-Worry-about-"return-path":after-completing-flow,state-remains-clean
-Verify-after-error,system-allows-retry

## 3.Environment+Context-Scenarios

### 3.1-Environment-Conditions
-Timezone-different-from-server
-Browser-language-different-from-application
-OS-dark-mode
-OS-high-contrast
-Large-font-size-configured-in-browser
-Active-ad-blocker
-Active-VPN(possible-additional-latency)

### 3.2-Devices+Configurations
-High-density-screen(Retina,4K)
-Low-resolution-screen
-Touch-device(no-hover)
-Keyboard-only-device(no-mouse)
-Old-browser(degraded-functionality)
-Browser-incognito/private-mode
