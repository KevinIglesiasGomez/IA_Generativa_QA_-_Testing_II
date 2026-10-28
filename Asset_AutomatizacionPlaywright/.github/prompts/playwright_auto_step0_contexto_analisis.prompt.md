---
agent: "Playwright Automation"
tools:
  [
    "edit/editFiles",
    "search",
    "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection",
    "search/usages",
  ]
description: "Step 0 — Contexto"
model: "Claude Haiku 4.5"
---

# Step 0: Analizar el framework Playwright existente y el escenario BDD a implementar

## INSTRUCCIONES DE CONTEXTO PARA ESTE STEP

**CARGAR obligatoriamente:**
- `playwright_auto_framework.instructions.md` — arquitectura y estructura del framework existente
- `playwright_auto_buenas_practicas.instructions.md` — patrones JavaScript/Playwright obligatorios

**NO cargar en este step:**
- `playwright_auto_calidad_verificacion.instructions.md`
- `playwright_auto_bitacora.instructions.md`

---

## 1. VARIABLES DE ENTRADA

- **`${input:feature_name}`**: Nombre del archivo `.feature` BDD a implementar.
- **`${input:project_bdd}`**: Carpeta raíz del proyecto BDD que contiene los archivos `.feature`.
- **`${input:playwright_folder}`**: Carpeta raíz del framework Playwright existente.
- **`${input:code_folder}`** (OPCIONAL): Carpeta con páginas HTML/JSP o código fuente relevante de la aplicación. Si no está disponible, se usará inspección dinámica del DOM. Si contiene un README, léelo completamente para entender la navegación inicial.

---

## 2. CONTEXTO DEL PROYECTO

Tu tarea es generar **pruebas automatizadas en Playwright (JavaScript)** basadas en el escenario de característica BDD **`${input:feature_name}`** ubicado en `${input:project_bdd}`.

- Lee y analiza **únicamente** el archivo de característica **`${input:feature_name}`** en su totalidad.
- Todos los pasos Gherkin deben implementarse como archivos JavaScript de pasos (`*.steps.js`) dentro del framework existente en **`${input:playwright_folder}`**.
- El framework usa **JavaScript + Playwright + Cucumber JS + npm**.

---

## 3. RESTRICCIONES CRÍTICAS

- Usar la estructura y archivos de configuración **existentes** en `${input:playwright_folder}`
- **OBLIGATORIO** analizar los Steps existentes (`src/steps/*.js`), Page Objects existentes (`src/pages/*.js`), localizadores (`src/pages/pagesLocators/*.js`) y utilidades (`src/utils/*.js`, `src/support/*.js`) para identificar código reutilizable antes de crear clases o métodos nuevos. Evitar duplicar lo que ya existe.
- **SOLO `common.steps.js` gestiona el ciclo de vida del navegador** (Before/After)
- **NUNCA crear instancias de navegador en archivos Steps que no sean `common.steps.js`**
- **NUNCA crear instancias de navegador en Page Objects** — los Page Objects reciben la página por constructor
- La página se comparte entre Steps vía el contexto compartido `this.page`

---

