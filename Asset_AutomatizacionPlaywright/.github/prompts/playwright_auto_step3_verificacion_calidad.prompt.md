---
agent: "Playwright Automation"
tools:
  [
    "edit/editFiles",
    "search",
    "execute/getTerminalOutput", "execute/runInTerminal", "read/terminalLastCommand", "read/terminalSelection",
    "search/usages",
  ]
description: "Step 3 — Verificación de calidad del test Playwright automatizado e integración en framework existente"
model: "GPT-5.3-Codex"
---

# Step 2: Verificación de Calidad del Test Playwright Automatizado

## INSTRUCCIONES DE CONTEXTO PARA ESTE STEP

**CARGAR obligatoriamente:**
- `playwright_auto_calidad_verificacion.instructions.md` — checklist de calidad para Playwright
- `playwright_auto_buenas_practicas.instructions.md` — patrones JavaScript/Playwright obligatorios
- `playwright_auto_bitacora.instructions.md` — instrucciones para actualizar la bitácora

**NO cargar en este step:**
- `playwright_auto_framework.instructions.md` (arquitectura ya conocida del step anterior)
- `playwright_auto_interactive_flow.instructions.md`

---

## 1. VALIDACIÓN DE CALIDAD

### 1.1 Verificaciones de Sintaxis y Estructura

- [ ] **Sintaxis limpia**: `npm run test:dry-run` ejecuta sin errores
- [ ] **Patrón Browser Factory aplicado**: solo `common.steps.js` crea y cierra el navegador
- [ ] **Página gestionada correctamente**: todos los demás Steps usan `this.page` del contexto compartido
- [ ] **Sin instancias de navegador duplicadas**: un único navegador activo por escenario
- [ ] **Sin `page.waitForTimeout()` con valores fijos**: solo esperas con condiciones de estado
- [ ] **Localizadores en archivos separados**: definidos en `*PageLocators.js` como constantes `UPPER_SNAKE_CASE`
- [ ] **Lógica en Page Objects**: los Steps solo llaman métodos del Page Object, no interactúan directamente con `page`
- [ ] **Sin datos sensibles**: no hay URLs, credenciales ni contraseñas codificadas en el código fuente
- [ ] **`@pendiente` individual**: los escenarios no implementados tienen el tag en el escenario concreto, no en la Feature completa
- [ ] **Sin emojis ni caracteres decorativos** en código fuente ni en mensajes de log

### 1.2 Verificación de Ejecución

- [ ] **El escenario pasa**: `npx cucumber-js --config cucumber.config.js --tags "@<tag>"` sin errores
- [ ] **El navegador se cierra correctamente**: sin procesos de Playwright huérfanos tras la ejecución
- [ ] **Reportes generados**: `reports/json/` y `reports/html/` se crean correctamente
- [ ] **Navegador visible**: modo no-headless activo (el ingeniero puede observar la ejecución)
- [ ] **Sin pasos UNDEFINED** en el reporte: todos los pasos Gherkin del `.feature` tienen implementación

---

## 2. VERIFICACIÓN DE INTEGRACIÓN CON EL FRAMEWORK

- [ ] Los nuevos archivos no rompen la ejecución de features existentes: `npm run test` pasa globalmente
- [ ] Los nuevos Steps son cargados correctamente por cucumber.config.js (carga automática `src/steps/**/*.js`)
- [ ] Los nuevos Page Objects siguen las convenciones de nomenclatura del framework (`{Funcionalidad}Page.js`)
- [ ] Los nuevos Steps siguen las convenciones de nomenclatura (`{funcionalidad}.steps.js`)
- [ ] Los nuevos archivos de localizadores siguen la nomenclatura (`{Funcionalidad}PageLocators.js`)
- [ ] No se ha duplicado código ya existente en otros Steps o Page Objects

---

## 3. PATRONES PROHIBIDOS — VERIFICAR AUSENCIA

```javascript
// Nunca debe aparecer en el codigo generado
await page.waitForTimeout(3000);                                     // espera fija

const { chromium } = require('playwright');                          // fuera de browserFactory.js
const browser = await chromium.launch();                             // fuera de browserFactory.js

Before(async function() { this.page = ... });                        // hooks en steps que no sean common.steps.js

const baseUrl = 'https://app.example.com';                           // URL hardcodeada
const password = 'micontrasenia123';                                 // credencial hardcodeada

// Localizador inline en Steps (debe estar en *PageLocators.js)
await this.page.click('#loginButton');                               // acceso directo a page en Step
```

---

## 4. ACTUALIZACIÓN DE BITÁCORA

Una vez validados todos los puntos anteriores, actualizar `automation_logs/automation_bitacora.md` siguiendo las instrucciones de `playwright_auto_bitacora.instructions.md`:

- Registrar cada escenario automatizado con fecha, archivos modificados y retos encontrados
- El registro debe ser breve pero suficientemente claro para cualquier ingeniero del equipo

---

## 5. OBJETIVO DE CALIDAD FINAL

Los tests Playwright generados deben:

- Implementar correctamente todos los escenarios Gherkin de **`${input:feature_name}`**
- Integrarse en `${input:playwright_folder}` sin romper la suite existente
- Seguir el patrón Page Object Model en JavaScript con localizadores separados
- No contener datos sensibles codificados; toda configuración vía archivos de entorno o `process.env`
- Ser ejecutables con `npm run test` y producir reportes en `reports/`
