---
agent: "Playwright Automation"
tools:
  [
    "edit/editFiles",
    "search",
    "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection",
    "search/usages",
  ]
description: "Step 1 — Implementar pruebas Playwright siguiendo el flujo interactivo, Browser Factory Pattern en JavaScript y buenas prácticas de seguridad"
---

# Step 1: Flujo de Implementación de Pruebas Playwright

## INSTRUCCIONES DE CONTEXTO PARA ESTE STEP

**CARGAR obligatoriamente:**
- `playwright_auto_main.instructions.md` — patrones de configuración y ejecución del framework
- `playwright_auto_buenas_practicas.instructions.md` — patrones JavaScript/Playwright obligatorios
- `playwright_auto_interactive_flow.instructions.md` — flujo interactivo de aprobación con el ingeniero

**NO cargar en este step:**
- `playwright_auto_calidad_verificacion.instructions.md` (se usará en Step 2)
- `playwright_auto_bitacora.instructions.md` (se usará al finalizar el Step 1)

---

## 1. ORDEN DE IMPLEMENTACIÓN

1. **Revisar los archivos de pasos existentes** en `${input:playwright_folder}/src/steps/` para reutilizar pasos ya implementados y entender los patrones en uso.
2. **Identificar el patrón de contexto compartido**: cómo la página se comparte entre Steps vía `this.page` definido en `common.steps.js`.
3. Analizar completamente el archivo de característica **`${input:feature_name}`** en `${input:project_bdd}` para determinar el alcance total de implementación.
4. **Obtener localizadores precisos de los elementos** mediante uno de estos enfoques:
   - **Si `${input:code_folder}` disponible**: Revisar páginas estáticas o código relevante para extraer selectores
   - **Si no hay acceso al código fuente**: Crear scripts de inspección dinámica (`inspect_*.js`) que ejecuten el navegador y analicen el DOM real renderizado. Ver `[snippet:inspeccion-dinamica]` para el patrón.
5. **Crear o extender Page Objects** que reciban la instancia de página por constructor. Nunca instanciar Playwright browser/page dentro de Page Objects.
6. **Crear o extender archivos de Steps** usando `this.page` del contexto compartido. Los archivos de Steps nunca crean instancias de navegador propias.
7. **Trabajar estrictamente un escenario a la vez** siguiendo el flujo interactivo de `playwright_auto_interactive_flow.instructions.md`.
8. **FLUJO INTERACTIVO OBLIGATORIO** tras implementar cada escenario:
   a. Implementar el código del escenario
   b. **PREGUNTAR**: "¿Ejecutar la prueba ahora? (sí/no)"
   c. **ESPERAR confirmación** del usuario
   d. Solo tras confirmación, ejecutar con npm
   e. **ESPERAR** a que la ejecución termine completamente
   f. **PREGUNTAR**: "¿La prueba funcionó correctamente? (sí/no/error)"
   g. **ESPERAR respuesta** del usuario - NUNCA asumir el resultado
   h. Si hay error, **PREGUNTAR antes de cada corrección y reintento**
9. **Protocolo de fallos**: 
   - Máximo 3 intentos de corrección
   - **PREGUNTAR antes de cada corrección**: "¿Aplicar esta corrección? (sí/no)"
   - **PREGUNTAR antes de cada reintento**: "¿Ejecutar nuevamente? (sí/no)"
   - NUNCA ejecutar múltiples veces sin confirmación
10. Repetir para cada escenario restante hasta que todos estén implementados y validados.

---

## 2. OBJETIVOS

- Implementar **todos los pasos** Gherkin del `.feature` como archivos JavaScript (`*.steps.js`)
- Seguir estrictamente el patrón **Page Object Model en JavaScript** con localizadores en archivos separados
- **Solo `common.steps.js` gestiona el navegador**: setup con `Before` y teardown con `After`
- Asegurar cobertura completa de todas las funcionalidades BDD descritas en el feature
- Implementar **esperas explícitas con condiciones** — nunca `page.waitForTimeout()` con valores fijos
- **Sin datos sensibles en código**: URLs y credenciales vía archivos de entorno o `process.env`
- Usar `console.log` con mensajes descriptivos para facilitar el debugging

---

## 3. REGLAS DE IMPLEMENTACIÓN

1. **Todo el código nuevo** se genera dentro de `${input:playwright_folder}`
2. **Localizadores como constantes** en archivos `*PageLocators.js` separados, en `UPPER_SNAKE_CASE`
3. **Lógica de negocio en Page Objects**; los Steps solo orquestan llamadas a métodos del Page Object
4. **Documentación, comentarios y mensajes de log**: en español
5. **SEGURIDAD**: nunca codificar URLs, contraseñas ni datos de entorno; usar archivos de entorno o `process.env`
6. **Marcar con `@pendiente`** los escenarios que no puedan implementarse completamente, a nivel individual
7. El archivo `.feature` **no se modifica** salvo para añadir tags `@pendiente`
8. **Las queries SQL** deben estar en `src/utils/QueryDeposit.js`, nunca inline en Steps ni Page Objects

---

## 4. VALIDACIÓN ANTES DE APROBAR CADA ESCENARIO

- Sin instancias de navegador duplicadas (solo una por escenario, gestionada en `common.steps.js`)
- Sin hooks `Before`/`After` en archivos de Steps que no sean `common.steps.js`
- Los Page Objects reciben la instancia de página por constructor, no la instancian
- Sin `page.waitForTimeout()` con valores fijos — usar esperas con condiciones de estado
- Sin datos sensibles codificados
- El escenario ejecuta correctamente con npm y el navegador es visible (HEADLESS=false)

---

## 5. OBJETIVO DE CALIDAD FINAL

Producir tests Playwright en JavaScript de alta calidad que:

- Implementen todos los escenarios Gherkin de **`${input:feature_name}`**
- Se adhieran al patrón Page Object Model en JavaScript
- Se integren correctamente en `${input:playwright_folder}` sin romper tests existentes
- Usen localizadores precisos obtenidos del análisis de `${input:code_folder}`
- No contengan datos sensibles codificados
- Sean ejecutables con `npm run test` y produzcan reportes en `reports/`
