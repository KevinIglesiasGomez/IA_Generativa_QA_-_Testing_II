# 📋-Standard-Templates-for-Agents,Prompts+Instructions

This-directory-contains-standardized-templates-balancing-**completeness+simplicity**-for-creating-agents,prompts+instructions,facilitating-whole-team-works-with-same-format.

## 🎯-Objective

Standardize-in-**complete-but-agile**-way-structure,format+content-of:
-**Agents**:AI-agent-definition-with-role+behavior
-**Prompts**:Instructions-guiding-agent-behavior
-**Instructions**:Specific-rules+quality-criteria

## 📁-Template-Structure

```
templates/
├──agent.template.md          #Agent-definition-template
├──prompt.template.md         #Prompt-design-template
├──instructions.template.md   #Instructions+rules-template
└──README.md                  #This-usage-guide
```

## 🚀-How-to-Use-Templates

### Step-1:Select-Appropriate-Template

-**agent.template.md**:When-need-define-new-AI-agent
-**prompt.template.md**:When-need-design-detailed-agent-behavior
-**instructions.template.md**:When-need-define-rules,criteria-or-specific-standards

### Step-2:Copy-Template

```bash
#Example-create-new-agent
cp-templates/agent.template.md-.github/agents/MyNewAgent.agent.md

#Example-create-new-prompt
cp-templates/prompt.template.md-.github/prompts/prompt_MyNewAgent.prompt.md

#Example-create-new-instructions
cp-templates/instructions.template.md-.github/instructions/main_MyNewAgent.instructions.md
```

### Step-3:Complete-Placeholders

Templates-include:
-**Simple-placeholders-in-brackets**`[description]`
-**Minimal-comments**-only-in-optional-sections`<!-- OPTIONAL:... -->`

**Process**:
1.Search-`[`-to-find-placeholders
2.Replace-each-`[placeholder]`-with-your-content
3.Remove-sections-marked-as-`<!-- OPTIONAL -->`-if-don't-need-them

### Step-4:Verify+Finalize

Before-using-template:
-✅All-placeholders-`[brackets]`-replaced
-✅Unused-optional-sections-removed
-✅Specific+clear-content
-✅Consistent-structure

## 📖-Each-Template-Description

### 🤖-agent.template.md

Defines-AI-agent-**identity+general-behavior**.

**Main-sections:**
-**Metadata**:Description,tools,model
-**Cognitive-Architecture**(optional):If-uses-structured-roles
-**Role+Function**:What-is+what-does
-**Target-audience**:Who-uses-it
-**Main-objective**:What-must-achieve
-**Methodological-approach**:Principles-follows
-**Tone+Style**:How-communicates
-**Constraints+Rules**:What-must/mustn't-do

**When-to-use**:Creating-new-AI-agent.

### 📝-prompt.template.md

Defines-agent's-**detailed-behavior+work-process**.

**Main-sections:**
-**Internal-Architecture**(optional):Multiple-cognitive-roles
-**Prerequisites+Context**:Necessary-files+info
-**Mandatory-Process**:Confirmation,analysis+proposal
-**Workflow**:Step-summary
-**Interactive-Flow**(optional):Approval-pattern
-**Output-Format**:Results-structure
-**Interactive-Commands**(optional):User-commands
-**Quality-Rules**:Standards-to-respect
-**Fundamental-Principle**:Guiding-philosophy

**When-to-use**:Designing-how-agent-works.

### 📚-instructions.template.md

Defines-**specific-rules,quality-criteria+technical-standards**.

**Main-sections:**
-**Objective**:What-this-file-covers
-**Instruction-categories**:Organized-by-topic
-**Mandatory-validations**:Minimum-criteria
-**Model/Framework**(optional):Structured-methodologies
-**Best-Practices**:With-✅+❌
-**Cross-cutting-Aspects**(optional):General-considerations
-**Constraints**:Clear-limitations
-**Output-Format**(optional):Artifacts-to-generate
-**Framework-Specific-Instructions**(optional):Per-technology

**When-to-use**:Defining-quality-criteria+specific-standards.

## 📂-Recommended-Organization

```
MyAgent/
├──MyAgent.agent.md                      #Agent-definition
├──prompt_MyAgent.prompt.md              #Main-behavior
└──instructions/
    ├──main_MyAgent.instructions.md      #General-instructions
    ├──framework1_MyAgent.instructions.md #Framework-1-specific-instructions
    └──framework2_MyAgent.instructions.md #Framework-2-specific-instructions
```

**Advantages**:
-Separation-of-responsibilities
-Specific-instruction-reuse
-Simpler-maintenance
-Scalability

## ✨-Complete-Usage-Example

### Example:Create-"Code-Review-Agent"

#### 1.Agent(CodeReviewer.agent.md)
```markdown
---
description: "Analyzes-code-to-detect-quality-issues+suggest-improvements"
tools: ['edit/editFiles', 'search', 'runCommands']
model: "Claude Sonnet 4.5"
---

# Code-Review-Agent

## Role
You-are-**code-review+software-quality-expert**.
[...rest-of-content...]
```

#### 2.Prompt(prompt_CodeReviewer.prompt.md)
```markdown
---
agent: "CodeReviewer"
tools: ["edit/editFiles", "search", "runCommands"]
description: "Review-code+propose-quality-improvements"
model: "Claude Sonnet 4.5"
---

# Prompt:Code-Review-Agent

## 1.PREREQUISITES+CONTEXT
[...process-definition...]
```

#### 3.Instructions(main_CodeReviewer.instructions.md)
```markdown
# Analysis-Instructions:Agent-Code-Reviewer

## Objective
These-instructions-define-quality-criteria-agent-must-follow...
[...specific-criteria...]
```

#### 4.Specific-Instructions(python_CodeReviewer.instructions.md)
```markdown
# Python-Specific-Instructions:Agent-Code-Reviewer

## 1.Code-Conventions
### PEP-8
-Use-snake_case-for-functions+variables
[...Python-specific-instructions...]
```

## 🎨-Format-Conventions

### Placeholders
-Format:`[brief-description]`
-Example:`[Agent-name]`→`Code-Review-Agent`
-No-prefixes-like-`REPLACE:`-to-keep-clean

### Optional-Sections
Optional-sections-have-HTML-comment-at-start:
```markdown
<!-- OPTIONAL:Remove-this-section-if-doesn't-apply -->
```

### Code-Examples
Use-fenced-code-blocks-with-language:
```markdown
```python
def-example():
    pass
\`\`\`
```

### Lists
-Use-`-`-for-unordered-lists
-Use-`1.`-for-ordered-lists
-Keep-consistent-format

## 🔄-Template-Updates

Templates-maintained-centrally.If-detect-improvement:
1.Propose-change-in-templates-repository
2.Team-reviews+approves
3.Update-all-templates
4.Communicate-to-team

## 📋-Checklist-Before-Using-Template

-☐Copied-template-to-correct-location
-☐Replaced-all-`[placeholders]`
-☐Removed-unused-optional-sections
-☐Verified-YAML-frontmatter-correct
-☐Content-specific+clear
-☐Structure-follows-template
-☐Ready-to-use

## 🤝-Support

For-questions-or-suggestions-about-templates:
-Open-issue-in-repository
-Contact-QA-team
-Review-existing-examples-in-`.github/`-directories
