---
description: Instrucciones de verificación de calidad para automatización de pruebas Playwright
applyTo: "**/*.steps.js,**/*Page.js,**/cucumber.config.js"
---

# Instrucciones de Verificación de Calidad para Automatización de Pruebas Playwright

## 1. CRITERIOS DE CALIDAD

### 1.1 Validación de Sintaxis y Estructura

**Checklist de Validaciones Críticas:**

- [ ] **Sintaxis limpia**: `npm run test:dry-run` se ejecuta sin errores ni warnings
- [ ] **Patrón Browser Factory aplicado correctamente**: Solo `common.steps.js` crea y cierra el navegador
- [ ] **Sin instancias de navegador en Page Objects**: Los Page Objects reciben `this.page` del contexto compartido
- [ ] **Sin hooks Before/After duplicados**: Solo `common.steps.js` define estos hooks de Cucumber
- [ ] **Contexto compartido correcto**: Los Steps usan `this.page`, `this.baseUrl`, `this.config` del contexto compartido
- [ ] **Sin `page.waitForTimeout()` con valores fijos**: Usar siempre esperas con condiciones de estado
- [ ] **Localizadores en archivos separados**: Los selectores deben estar en `*PageLocators.js`, no inline en Page Objects ni Steps
- [ ] **Lógica de negocio en Page Objects**: Los Steps solo orquestan, la lógica de interacción va en el Page Object
- [ ] **Tags correctos en escenarios**: Usar `@smoke`, `@regression`, `@critical`, `@pendiente` según corresponda
- [ ] **Escenarios pendientes etiquetados individualmente**: `@pendiente` en cada escenario, nunca solo a nivel de Feature
- [ ] **Sin datos sensibles en código**: URLs, credenciales y configuración de entorno cargados desde `env.*.js` o `process.env`
- [ ] **Cumplimiento de estilo**: Sin emojis, iconos ni caracteres decorativos en archivos de código ni logs

### 1.2 Validación de Ejecución

- [ ] **El escenario se ejecuta correctamente**: `npx cucumber-js --config cucumber.config.js --tags "@<tag>"` pasa sin errores
- [ ] **El navegador se cierra correctamente**: Sin procesos de Playwright huérfanos tras la ejecución
- [ ] **Los reportes se generan**: `reports/json/` y `reports/html/` se crean tras la ejecución
- [ ] **Modo no-headless activo**: El navegador es visible durante la ejecución (HEADLESS=false salvo en CI)
- [ ] **Sin pasos UNDEFINED en el reporte**: Todos los pasos Gherkin del `.feature` tienen implementación

---

## 2. CHECKLIST DE VALIDACIONES FINALES

- [ ] El framework ejecuta en modo dry-run: `npm run test:dry-run`
- [ ] Solo `common.steps.js` gestiona el ciclo de vida del navegador (Before/After)
- [ ] Todos los demás Steps reciben el navegador vía `this.page` del contexto compartido
- [ ] Los Page Objects reciben la instancia de página por constructor, nunca la crean
- [ ] Las definiciones de pasos usan el contexto compartido, no crean su propio navegador
- [ ] No hay datos sensibles codificados: URLs y credenciales en archivos de entorno o `process.env`
- [ ] Los escenarios no implementados están marcados con `@pendiente` individualmente
- [ ] Cada escenario se ejecuta y valida antes de pasar al siguiente
- [ ] La bitácora de automatización está actualizada con los cambios de la sesión

---

## 3. PATRONES PROHIBIDOS

Ver ejemplos completos en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:patron-antipatron]`

Resumen rápido:
- `const { chromium } = require('playwright'); await chromium.launch()` fuera de `browserFactory.js`
- `page.waitForTimeout(3000)` con valores fijos
- Localizadores CSS/XPath inline en Steps o Page Objects (extraer a `*PageLocators.js`)
- Hooks `Before`/`After` en archivos de steps que no sean `common.steps.js`
- URLs o credenciales hardcodeadas: `baseUrl = 'https://app.example.com'`

---

## 4. OBJETIVO DE CALIDAD FINAL

Producir tests de Playwright de alta calidad y mantenibles que:

- Implementen todos los escenarios Gherkin del archivo `.feature` analizado
- Se adhieran al patrón de diseño Page Object Model en JavaScript
- Se integren correctamente con la estructura del framework Playwright existente
- Automaticen la navegación e interacciones usando localizadores precisos obtenidos del análisis de la aplicación
- No contengan datos sensibles codificados (URLs, credenciales, entornos)
- Incluyan captura de evidencias en fallo (screenshots) correctamente configurada
- Sigan la arquitectura de gestión de navegador establecida (Browser Factory Pattern) para evitar conflictos e instancias duplicadas
