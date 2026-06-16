# Mini_AnalisisPruebasAPI - Reduced Verbose Copilot

This is a token-optimized version of the Demo_AnalisisPruebasAPI copilot.

## Changes Applied

- **Verbose Reduction**: All content has been compressed to consume minimal tokens while preserving 100% semantic information
- **Translation**: All content translated from Spanish to English
- **Format**: Follows the compact format pattern using hyphens and minimal formatting
- **YAML Front Matter**: Preserved intact as required for GitHub Copilot functionality

## Structure

```
.github/
├── agents/
│   └── api_test_analizer.agent.md
├── instructions/
│   ├── api_test_analizer_interactive_flow.instructions.md
│   ├── api_test_analizer_main.instructions.md
│   └── api_test_analizer_report.instructions.md
└── prompts/
    ├── api_test_analizer_step1.prompt.md
    └── api_test_analizer_step2.prompt.md
```

## Files Reduced

- 1 agent file
- 3 instruction files
- 2 prompt files

**Total: 6 files**

## Benefits

- Significantly reduced token consumption for reading copilot instructions
- Faster processing by AI models
- Maintained 100% of original functionality and semantic information
- English language for broader accessibility
- Compact format optimized for POISED model (Parameters, Outputs, Interoperability, Security, Errors, Data)

## Original Source

Original copilot located at: `Demo_AnalisisPruebasAPI/.github/`

## Key Features

This copilot analyzes API testing projects (Karate DSL and Postman collections) to:
- Identify testing gaps using the POISED model
- Propose incremental improvements with engineer approval
- Generate detailed reports with risk assessment
- Maintain changelog for test suite evolution
