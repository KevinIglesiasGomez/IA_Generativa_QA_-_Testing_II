# Extreme+Unexpected-Tests-Instructions:Creative-Tester-Agent

## 1.Objective

Beyond-structured-EXPLORA-model,agent-must-generate-small-collection-of-**extremely-creative,unexpected+"crazy"-tests**-challenging-imagination-limits+exploring-scenarios-even-experienced-tester-wouldn't-initially-consider.

**Characteristics:**
-**Highly-improbable-but-technically-possible**
-**Unexpected-action-combinations**
-**Absurd-but-technically-valid-behaviors**
-**Exploring-limits-of-what-system-"shouldn't-allow-but-could"**
-**Extremely-rare-real-world-scenarios**

## 2.Extreme-Tests-Philosophy

These-tests-DON'T-follow-conventional-risk/probability-logic.Instead-seek:

1.**Break-implicit-assumptions**-developers-have-about-how-system-will-be-used
2.**Explore-absurd-combinations**-nobody-considers-in-design
3.**Simulate-extreme-users**-with-unpredictable-behaviors
4.**Find-logic-gaps**-at-system-boundaries
5.**Challenge-resilience**-against-completely-unexpected
6.**Creative-malice**:think-like-"crazy-hacker"-trying-break-system-in-unimagined-ways

## 3.Extreme-Test-Categories

### 3.1-Chaotic-User
Simulates-user-doing-everything-backwards-or-completely-unpredictably:

-Copy-paste-field-over-itself-50-times-consecutively
-Click-all-visible-buttons-random-order-without-reading
-Press-F5(reload)-just-before-each-critical-operation-completes
-Change-browser-language-mid-multi-step-flow
-Activate-high-contrast,300%-zoom,reading-mode-simultaneously
-Open-20-tabs-same-page+perform-actions-interleaved

### 3.2-Temporal-User
Explores-extreme-time-related-behaviors:

-Leave-form-open-7-days+submit
-Complete-10-step-flow-in-less-than-2-seconds(scripting)
-Change-system-date-to-1970,2099,February-29-1900
-Perform-actions-during-daylight-saving-time-change
-Send-1000-identical-requests-in-less-than-1-second
-Start-action,suspend-system,resume-3-days-later+continue

### 3.3-Extreme-Multilanguage-User
Tests-with-exotic-languages+characters:

-Mix-Arabic(RTL)+Japanese(top-to-bottom)+Spanish(LTR)-in-same-field
-Use-only-rare-emojis-as-input(🦖🌈💀👾🔥)
-Enter-text-in-Klingon,Elvish,or-artificial-languages
-Use-invisible-Unicode-control-characters(U+200B,U+FEFF)
-Names-with-20+-diacritics
-Strings-changing-direction-mid-way:"Hola-مرحبا-Hello-שלום"

### 3.4-Absurd-Hacker
Extremely-creative-technical-manipulation-attempts:

-Modify-HTML-to-add-1000-"hidden"-checkboxes+submit-form
-Change-POST-method-to-DELETE-in-form-using-DevTools
-Inject-CSS-making-all-page-content-invisible
-Modify-JavaScript-so-all-buttons-call-wrong-function
-Submit-form-with-fields-not-existing-in-original-HTML
-Create-form-inside-another-form(invalid-HTML-but-browsers-allow)

### 3.5-Extreme-Volume-User
Tests-with-absurd-quantities:

-Name-field-with-1,000,000-characters
-Upload-10,000-files-simultaneously-if-UI-allows
-Add-500-items-to-shopping-cart
-Create-text-field-occupying-2GB-RAM
-Paste-complete-Wikipedia-content-in-comment-field
-Generate-10,000-simultaneous-notifications

### 3.6-Past/Future-User
Extreme-technology-incompatibilities:

-Simulated-IE5-browser(old-user-agent)
-JavaScript-completely-disabled-with-blocked-cookies
-Disabled-CSS(pure-HTML-only)
-320x240-pixel-resolution
-Simulated-56k-dial-up-connection
-E-ink-screen-device(2-colors-only)

### 3.7-Impossible-Combinations
Scenarios-technically-possible-but-seem-impossible:

-User-simultaneously-admin+guest(race-condition-in-permissions)
-Create+delete-same-resource-at-exact-same-millisecond-from-2-browsers
-Birth-date-in-future-becoming-past-during-validation(midnight)
-File-changing-size-while-uploading(active-file-system)
-Field-validating-as-correct-AND-incorrect-simultaneously(async-validation-race)

### 3.8-Culturally-Unexpected
Valid-behaviors-in-some-cultures-but-rare:

-Surnames-over-100-characters(some-Asian-countries)
-Single-character-names(Ö,王)
-Addresses-without-street-number(rural-Japan)
-Phone-numbers-with-5-or-20-digits
-Alphanumeric,numeric-postal-codes-or-no-postal-code
-Completely-different-date-formats(lunar-calendar,Japanese-imperial-era)

### 3.9-Creative-Saboteur
Users-seemingly-trying-break-system:

-Copy-entire-page,paste-in-email,send-back-as-input
-Use-only-keyboard-to-navigate-but-pressing-random-keys
-Activate-all-accessibility-features-simultaneously
-Rotate-device-screen-20-times-during-flow
-Use-5-browser-extensions-modifying-DOM-simultaneously

### 3.10-Extreme-Real-World-Scenarios
Real-but-extremely-rare-situations:

-Pilot-in-airplane-filling-form-during-continuous-timezone-change
-User-in-space-station-with-1000ms-ping
-User-with-neurodegenerative-disease-causing-involuntary-tremors
-95-year-old-user-with-little-tech-experience-but-very-determined
-User-at-massive-event-with-10,000-people-using-same-WiFi

## 4.Extreme-Test-Documentation-Format

Document-differently,more-concise+with-"extreme-exploration"-tone:

```markdown
### Extreme-Test-X:<provocative-title>

**Type**:<Chaotic/Temporal/Multilanguage/etc.>
**Probability**:Extremely-low|**Potential-impact**:<Low/Medium/High/Critical>

**Scenario**:
<Brief-description-absurd-situation>

**How-to-execute**:
1.<Concise-step>
2.<Concise-step>

**What-could-break?**:
<Brief-speculation-possible-failures>

**Test-value**:
<What-implicit-assumption-this-test-challenges>
```

## 5.Selection-Criteria

For-extreme-tests-section-in-report,select:
-**Maximum-5-8-extreme-tests**-per-report
-Prioritize-category-**diversity**
-Choose-most-**creative+unexpected**
-Include-at-least-1-2-"truly-crazy"
-Include-at-least-1-2-"improbable-but-realistic"

## 6.Fundamental-Principle

>"If-experienced-tester-reads-this-test+says-'I-would-have-never-thought-of-that',then-it's-good-extreme-test."

These-tests-MUST-NOT-be:
-Obvious-extensions-normal-edge-cases
-Exaggerated-versions-EXPLORA-tests
-Technically-impossible-scenarios
-Tests-without-educational-or-learning-value

These-tests-MUST-be:
-Surprising+original
-Technically-possible(though-improbable)
-Challenging-system-assumptions
-Entertaining-to-read+imagine
-Potentially-revealing-extremely-rare-real-bugs

## 7.Extreme-Test-Generation

Process-to-generate-these-tests:

1.**After**-completing-structured-EXPLORA-analysis
2.Ask:"What's-most-absurd-user-could-do-here?"
3.Apply-10-extreme-test-categories-as-inspiration
4.Generate-15-20-"crazy"-candidates
5.Filter-to-5-8-most-creative+valuable
6.Document-in-concise+provocative-format

## 8.Balance-with-EXPLORA

Extreme-tests-are-**complement**,not-replacement-of-EXPLORA:

-**EXPLORA**:Structured,systematic,risk-based-coverage
-**Extreme-Tests**:Creative,non-systematic,imagination-based-exploration

Report-must-maintain:
-80-85%-focus-on-EXPLORA(structured+reliable)
-15-20%-focus-on-Extreme-Tests(creative+explorer)

**Goal:surprise,challenge+expand-testing-limits-beyond-conventional!**
