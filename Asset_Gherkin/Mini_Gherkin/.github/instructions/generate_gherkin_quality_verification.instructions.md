# Quality+Verification:Mandatory-Checks+Review-Criteria-for-Cucumber-Features

Mandatory-that-each-generated-Cucumber-feature-meets-following-quality+verification-criteria-to-ensure-effectiveness+maintainability:

### Quality-Assurance-Criteria

**MANDATORY-CHECKS:**
- [ ] All-scenarios-**executable**+**testable**
- [ ] Each-feature-has-at-least-1-`@smoke`-scenario(critical-path)
- [ ] Boundary-value-tests-included-for-numeric-inputs
- [ ] Steps-use-**declarative-language**(avoid-implementation-details)
- [ ] Test-data-**independent**-between-scenarios
- [ ] Features-**cohesive**+**well-organized**
- [ ] Tagging-strategy-**consistent**-across-all-features
- [ ] Documentation-**complete**+**actionable**
- [ ] If-features-generated-from-**User-Stories**-with-Jira-ID,each-scenario-has-corresponding-tag-`@ID-1234`

---

### Validation+Review

**Review-Checklist:**
- [ ] All-scenarios-follow-Given-When-Then-pattern
- [ ] **Mandatory**-In-each-feature:NO-unnecessary-line-breaks-between-steps
- [ ] **Mandatory**-In-each-feature:NO-steps-starting-with-non-standard-keywords,ONLY-"Dado","Cuando","Entonces","Y"
  -**FORBIDDEN**:Steps-starting-with-"O","Pero","E","*",any-other-word
  -**CORRECT**:Use-"Y"-to-concatenate-multiple-assertions/alternative-conditions
  -**VALIDATION**:Execute-regex-search-`^    O `-in-all-.feature-files-before-finalizing
- [ ] Tags-correctly-assigned
- [ ] Language-declarative+free-of-implementation-details
- [ ] Scenarios-independent-from-each-other
- [ ] Both-success+error-cases-included
- [ ] Documentation-complete+updated
- [ ] File-names-follow-conventions
- [ ] Step-reusability-principles-applied
