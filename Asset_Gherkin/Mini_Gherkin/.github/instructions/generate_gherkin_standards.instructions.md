### Objective

Define-standards+best-practices-for-generating-BDD-scenarios-with-Cucumber.

---

### Mandatory-Cucumber-Standards

**MANDATORY-REQUIREMENTS:**
-All-scenarios-MUST-be-**executable**+**testable**
-Use-**declarative-language**(WHAT,not-HOW)
-Strictly-follow-**Given-When-Then**-structure
-Ensure-**step-reusability**-across-features
-Apply-**SOLID-principles**-to-scenario-design
-Include-**data-driven-tests**-where-appropriate
-Implement-proper-**error-handling**-scenarios
  -**FORBIDDEN**:Steps-starting-with-"O","Pero","E","*",any-other-word
  -**CORRECT**:Use-"Y"-to-concatenate-multiple-assertions/alternative-conditions

**Technical-Validation-Requirements:**
-Each-scenario-MUST-have-clear-**acceptance-criteria**
-Include-**boundary-value-testing**-scenarios
-Ensure-**test-data-independence**-between-scenarios

---

### Advanced-BDD-Tagging-Strategy

**Primary-Tags:**
-`@smoke`-Essential-functionality-that-must-work(typically-1-2-scenarios-per-feature)
-`@regression`-Important-scenarios-including-validations,error-handling,edge-cases

**Secondary-Tags:**
-Environment-type:`@web`,`@mobile`,`@api`
-Functional-areas(examples):`@authentication`,`@users`,`@products`,`@orders`,`@payments`,`@administration`,`@reports`,etc.
-If-documentation-User-Stories-with-Jira-ID,add-tag-with-ID:`@ID-1234`

**Tagging-Example:**
```gherkin
@smoke @authentication
Escenario: Successful-system-login

@regression @authentication  
Escenario: Failed-login-incorrect-credentials

@smoke @expedientes
Escenario: Query-existing-record

@regression @facturas
Escenario: Validate-mandatory-invoice-fields
```

---

### Required-File-Structure

```
${output_directory}/
├── INFORME_<fecha_hora>.md    # Comprehensive documentation (ROOT LEVEL)
└── features/    # BDD feature files directory
    ├── authentication.feature
    ├── expediente-management.feature
    ├── turbo-alta-facturas.feature
    └── ...
```

**Important:**
-**.feature-files**-go-ONLY-in-`features/`-subdirectory
-**INFORME_<fecha_hora>.md**-located-in-root-of-`${output_directory}/`(NOT-in-`features/`-directory),filename-must-include-creation-date+time(format-`YYYY-MM-DD_HH-mm-ss`)

---

### Scenario-Structure+Best-Practices

**Scenario-Structure:**
```gherkin
# language: es
Característica: [Descriptive functionality name]
  Como [user type]
  Quiero [perform an action]
  Para [obtain a benefit]

  @smoke @[functional_area]
  Escenario: [Success scenario description]
    Dado que [initial condition]
    Y [additional condition if necessary]
    Cuando [user action]
    Entonces [expected result]
    Y [additional validation if necessary]

  @regression @[functional_area] @validaciones
  Escenario: [Validation scenario description]
    Dado que [initial condition]
    Cuando [action that causes error]
    Entonces [expected error result]
    Y [specific error validation]
```

**Writing-Principles:**
1.**Natural-Language**:Use-business-domain-terminology
2.**Declarative-vs-Imperative**:Describe-WHAT-not-HOW
3.**Independence**:Each-scenario-must-be-independent
4.**Reusability**:Use-steps-that-can-be-reused
5.**Granularity**:One-scenario-per-specific-behavior

---

### Naming-Conventions

**Feature-Files:**
-Use-kebab-case-for-file-names
-Descriptive-functional-area-names
-Examples:`user-authentication.feature`,`invoice-management.feature`

**Scenario-Names:**
-Descriptive+concise
-Examples:"Create-new-invoice-with-valid-data","Validate-mandatory-fields"

**Tags:**
-Use-lowercase
-Separate-words-with-underscores-if-needed
-Examples:`@smoke`,`@regression`,`@user_management`

---

### Test-Data-Patterns

**Scenario-Outlines-for-Multiple-Data:**
```gherkin
@regression @validaciones
Esquema del escenario: Validate [field] format
  Dado que estoy en la página "[page]"
  Cuando ingreso "<value>" en el campo "[field]"
  Entonces debería ver el mensaje "<error_message>"

  Ejemplos:
    | value          | error_message                    |
    | invalid_email  | Incorrect email format          |
    | empty_text     | This field is mandatory         |
    | long_text      | Maximum 50 characters allowed   |
```
