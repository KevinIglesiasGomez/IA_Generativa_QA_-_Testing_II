---
description: Patrones de configuración, ejecución e integración del framework Playwright existente
applyTo: "**/*.js,**/package.json,**/cucumber.config.js"
---

# Patrones de Configuración y Ejecución del Framework Playwright

## 1. TECNOLOGÍA Y LENGUAJE

- **Lenguaje**: JavaScript / Node.js (NO Java, NO TypeScript)
- **Motor de automatización**: Playwright 1.41.2
- **Framework BDD**: Cucumber JS 10.3.1
- **Gestor de paquetes**: npm
- **Gestión de navegador**: Browser Factory Pattern centralizado en `src/support/browserFactory.js`

**TODA ejecución de pruebas fluye a través de comandos de npm/cucumber-js, NUNCA mediante comandos playwright directamente.**

## 2. COMANDOS DE EJECUCIÓN CON NPM

```bash
# Ejecutar todos los tests
npm run test

# Ejecutar con tag específico
npm run test:smoke
npm run test:regression

# Ejecutar en modo dry-run (validación sin ejecutar)
npm run test:dry-run

# Ejecutar por entorno
npm run test:local
npm run test:test

# Ejecutar por navegador
npm run test:chrome
npm run test:firefox
npm run test:webkit

# Ejecutar modo visible (no headless)
npm run test:headed

# Ejecutar una feature específica
npx cucumber-js --config cucumber.config.js src/features/Login.feature

# Ejecutar con tag específico inline
npx cucumber-js --config cucumber.config.js --tags "@smoke"

# Generar reporte HTML
npm run report
```

## 3. CONFIGURACIÓN PRINCIPAL DE CUCUMBER (cucumber.config.js)

```javascript
module.exports = {
  default: {
    features: ['src/features/*.feature'],
    require: [
      'src/steps/**/*.js',
      'src/support/**/*.js'
    ],
    format: [
      'progress-bar',
      `json:reports/json/${reportName}.json`,
      `html:reports/html/${reportName}.html`
    ],
    worldParameters: {
      environment: config.environment || 'local',
      config: config,
      browser: process.env.BROWSER || config.browser || 'chromium',
      headless: config.headless,
      baseUrl: config.baseUrl,
      screenshotOnFailure: true,
      videoOnFailure: false,
      timeout: config.timeout || 30000,
      slowMo: config.slowMo || 100
    },
    formatOptions: { snippetInterface: 'async-await' },
    parallel: config.workers || 1,
    retry: config.retries || 0
  }
};
```

## 4. PATRON BROWSER FACTORY (OBLIGATORIO)

Ver ejemplos en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:browser-factory]` y `[snippet:common-steps]`

**Regla clave**: Solo `common.steps.js` gestiona el ciclo de vida del navegador (Before/After). El resto de archivos de pasos reciben la página vía contexto compartido `this.page`.

## 5. GESTIÓN DE PÁGINA (Page Objects)

Ver ejemplo en `.github/snippets/playwright_auto_code_snippets.md`: `[snippet:page-object-basico]`

**NUNCA** crear instancias de Playwright browser/page dentro de Page Objects ni en Steps que no sean `common.steps.js`.

## 6. CONFIGURACIÓN MULTI-ENTORNO (env.local.js / env.test.js)

Archivos de configuración por entorno en la raíz del proyecto:

```javascript
// env.local.js
module.exports = {
  environment: 'local',
  baseUrl: process.env.BASE_URL || "http://localhost:3000",
  username: process.env.APP_USERNAME || "usuario_por_defecto",
  password: process.env.APP_PASSWORD || "password_por_defecto",
  browser: process.env.BROWSER || "chromium",
  headless: process.env.HEADLESS === "true" || false,
  timeout: parseInt(process.env.TIMEOUT) || 30000,
  slowMo: parseInt(process.env.SLOW_MO) || 100
};
```

Acceso en código (vía worldParameters):

```javascript
// En Steps: this.config y this.baseUrl disponibles desde common.steps.js
const username = this.config.username || process.env.APP_USERNAME;
const password = this.config.password || process.env.APP_PASSWORD;
```

**NUNCA** codificar URLs, credenciales ni datos de entorno directamente en el código fuente.

## 7. GESTIÓN DE ESCENARIOS PENDIENTES

- Etiquetar escenarios no implementados con `@pendiente` a nivel **individual** de cada escenario.
- **NUNCA** usar `@pendiente` solo a nivel de Feature.

```gherkin
@smoke @login @pendiente
Escenario: Login con usuario con cuenta bloqueada
  Dado que el usuario tiene la cuenta bloqueada
  Cuando intenta iniciar sesión
  Entonces el sistema muestra mensaje de cuenta bloqueada
```

## 8. REPORTES

Generados automáticamente en `reports/` tras cada ejecución:
- `reports/json/cucumber-report-[timestamp].json` — Informe JSON de Cucumber
- `reports/html/cucumber-report-[timestamp].html` — Informe HTML navegable
- `reports/screenshots/` — Capturas de pantalla en fallos
- `reports/videos/` — Videos de ejecución (si está habilitado)

## 9. TAGS DE EJECUCIÓN

| Tag | Uso |
|---|---|
| `@smoke` | Tests de humo, validación básica |
| `@regression` | Suite de regresión completa |
| `@critical` | Tests críticos de negocio |
| `@pendiente` | Escenarios no implementados aún |
| `@debug` | Escenarios con logging adicional |

## 10. REQUISITOS DE SEGURIDAD

- **NUNCA codificar** URLs, credenciales ni contraseñas en código fuente ni en control de versiones.
- **Siempre usar** archivos de entorno (`env.local.js`, `env.test.js`) con `process.env`.
- **Selección de entorno** vía `process.env.ENV` o `cross-env ENV=local`.
- **NUNCA incluir** archivos `.env` con datos reales en commits. Usar plantillas vacías o ficheros de ejemplo.

## 11. CONVENCIONES DE CÓDIGO

- Documentación, comentarios y mensajes de log: **en español**
- Nombres de clases (Page Objects): `PascalCase` en inglés (ej. `LoginPage`, `MenuPage`)
- Nombres de métodos y variables: `camelCase` en inglés (ej. `fillUsername()`, `loginButton`)
- Constantes y localizadores: `UPPER_SNAKE_CASE` en inglés definidos en archivos `*Locators.js` (ej. `LOGIN_BUTTON = '#loginBtn'`)
- Archivos de Steps: `{funcionalidad}.steps.js`
- Archivos de Page Objects: `{Funcionalidad}Page.js`
- Archivos de Localizadores: `{Funcionalidad}PageLocators.js`
- Archivos de Datos: `{Funcionalidad}Data.js`
