---
agent: "Playwright Automation"
tools:
  [
    "edit/editFiles",
    "search",
    "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection",
    "search/usages",
  ]
description: "Step 0 — Analizar el framework Playwright existente y el escenario BDD a automatizar"
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
- Analizar los Steps existentes (`src/steps/*.js`) y Page Objects existentes (`src/pages/*.js`) para código reutilizable antes de crear clases nuevas
- **SOLO `common.steps.js` gestiona el ciclo de vida del navegador** (Before/After)
- **NUNCA crear instancias de navegador en archivos Steps que no sean `common.steps.js`**
- **NUNCA crear instancias de navegador en Page Objects** — los Page Objects reciben la página por constructor
- La página se comparte entre Steps vía el contexto compartido `this.page`

---

## 4. ORDEN DE ANÁLISIS

1. **Analizar el framework existente en `${input:playwright_folder}`**:
   - Leer `src/support/browserFactory.js` para entender la gestión centralizada del navegador
   - Leer `src/steps/common.steps.js` para entender el patrón de ciclo de vida del navegador
   - Revisar las clases Data (ej. `LoginData.js`, `UsuarioData.js`) para entender el almacenamiento de datos del escenario
   - Revisar `src/support/environmentLoader.js` para entender cómo se carga la configuración de entorno
   - Identificar qué Page Objects y Steps existentes son reutilizables para el feature a implementar

2. **Analizar el archivo de característica `${input:feature_name}`** en `${input:project_bdd}`:
   - Identificar todos los pasos Gherkin a implementar
   - Detectar pasos ya implementados en Steps existentes (reutilizar)
   - Detectar pasos nuevos que requieren creación de código
   - Identificar datos de prueba necesarios y si requieren consultas a BBDD vía `AtDBConnector.js`

3. **Obtener localizadores de elementos de la aplicación** (dos enfoques):

   **Enfoque A: Análisis de código fuente estático** (si `${input:code_folder}` está disponible):
   - Revisar páginas HTML o código fuente en `${input:code_folder}` para obtener localizadores precisos de los elementos interactivos
   - Leer el README si existe para entender la navegación inicial
   - Identificar elementos interactivos relevantes para cada paso Gherkin

   **Enfoque B: Inspección dinámica del DOM** (sin `${input:code_folder}` o para aplicaciones legacy/framesets):
   - Crear scripts temporales de inspección (`inspect_*.js`) en la raíz del proyecto Playwright
   - Ejecutar el navegador para analizar la estructura DOM real renderizada
   - Detectar frames, elementos dinámicos, funciones JavaScript
   - Extraer selectores precisos del HTML final
   - **Ejemplo de script**: Ver `[snippet:inspeccion-dinamica]`

---

## 5. PATRÓN DE ARQUITECTURA (OBLIGATORIO)

Ver ejemplos completos en: `.github/snippets/playwright_auto_code_snippets.md`

**Patrones obligatorios:**
- Page Object recibe `this.page` por constructor y define localizadores en archivo separado (`[snippet:page-object-basico]`)
- Steps usan `this.page` del contexto compartido, nunca crean navegador (`[snippet:steps-playwright]`)
- Solo `common.steps.js` gestiona Before/After y el ciclo de vida del navegador (`[snippet:common-steps]`)

---

## 6. OBJETIVOS DEL ANÁLISIS

Al finalizar este step, debes haber producido:

1. **Inventario de pasos Gherkin** del feature `${input:feature_name}`:
   - Pasos ya implementados (con referencia al archivo Steps existente)
   - Pasos nuevos a implementar (con descripción de qué Page Object y lógica necesitan)

2. **Lista de Page Objects** a crear o extender, con los localizadores identificados mediante análisis estático del código fuente o inspección dinámica del DOM

3. **Riesgos técnicos detectados** y propuesta de solución concreta

4. **Propuesta de implementación** para el primer escenario, lista para presentar al ingeniero antes de escribir código

---

## 7. SEGURIDAD

- **NUNCA codificar** URLs, credenciales ni datos de entorno en el código fuente
- Toda configuración sensible se carga desde archivos de entorno (`env.*.js`) o `process.env`
- Los datos de prueba que requieran BBDD se obtienen con `AtDBConnector.js` usando la configuración del entorno activo
- Las queries SQL se mantienen en `src/utils/QueryDeposit.js`, nunca inline
