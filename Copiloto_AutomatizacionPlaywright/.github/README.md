# Playwright Automation Copilot

Copiloto de GitHub Copilot especializado en la generación de pruebas automatizadas en Playwright para el framework BDD existente basado en Cucumber JS y Node.js.

---

## Características y Capacidades

- Generación interactiva de tests automatizados en Playwright siguiendo el patrón Page Object Model en JavaScript
- Análisis del framework Playwright existente antes de proponer cualquier implementación
- Flujo de aprobación escenario por escenario: nunca genera múltiples implementaciones sin validación previa del ingeniero
- Adaptado completamente al framework Playwright del proyecto: Browser Factory Pattern, contexto compartido `this.page`, localizadores en archivos separados `*PageLocators.js`
- Soporte multi-navegador: chromium, firefox, webkit
- Ejecución de pruebas desde terminal con `npm run test` en modo visible (no-headless) para revisión del ingeniero
- Actualización automática de bitácora de automatización tras cada sesión
- Protocolo estructurado ante fallos: máximo 2 reintentos autónomos, diagnóstico al ingeniero en el tercero

---

## Ficheros que Componen el Copiloto

### Agente Principal

| Fichero | Descripción |
|---|---|
| `agents/playwright_auto_generation.agent.md` | Definición del agente: rol, modelo, herramientas permitidas, tono y restricciones |

### Instrucciones

| Fichero | Descripción | Aplica a |
|---|---|---|
| `instructions/playwright_auto_framework.instructions.md` | Estructura completa del framework Playwright: carpetas, dependencias, patrones de arquitectura, configuración multi-entorno | `**/*.js`, `**/package.json`, `**/*.feature` |
| `instructions/playwright_auto_main.instructions.md` | Patrones de configuración y ejecución: comandos npm, Browser Factory, gestión de entornos, convenciones de código | `**/*.js`, `**/package.json`, `**/cucumber.config.js` |
| `instructions/playwright_auto_buenas_practicas.instructions.md` | Selectores recomendados, esperas explícitas, organización de Steps, manejo de errores en Page Objects | `**/*.js`, `**/*.feature` |
| `instructions/playwright_auto_calidad_verificacion.instructions.md` | Checklist de calidad para validar cada test antes de aprobarlo, patrones prohibidos | `**/*.steps.js`, `**/*Page.js`, `**/cucumber.config.js` |
| `instructions/playwright_auto_bitacora.instructions.md` | Formato y reglas de la bitácora de automatización en `automation_logs/automation_bitacora.md` | `**/automation_bitacora.md` |
| `instructions/playwright_auto_interactive_flow.instructions.md` | Flujo interactivo obligatorio: pasos del proceso, órdenes del ingeniero, protocolo ante fallos | `**` |

### Prompts

| Fichero | Descripción |
|---|---|
| `prompts/playwright_auto_step0_contexto_analisis.prompt.md` | Análisis del framework y del escenario BDD a implementar. Produce el inventario de pasos, Page Objects necesarios y riesgos detectados |
| `prompts/playwright_auto_step1_flujo_implementacion.prompt.md` | Implementación interactiva escenario por escenario siguiendo el flujo de aprobación |
| `prompts/playwright_auto_step2_verificacion_calidad.prompt.md` | Verificación de calidad final, validación de integración y actualización de bitácora |

### Snippets

| Fichero | Descripción |
|---|---|
| `snippets/playwright_auto_code_snippets.md` | Biblioteca de snippets JavaScript reutilizables: Page Object, Steps, Browser Factory, localizadores, esperas, datos y patrones prohibidos |

---

## Uso del Copiloto

### Origen de los casos de prueba

El copiloto no genera ni inventa casos de prueba. Los casos a automatizar los define siempre el ingeniero de QA en archivos `.feature` escritos en Gherkin. El copiloto lee esos archivos y los convierte en código Playwright ejecutable.

El archivo `.feature` debe existir antes de iniciar una sesión de trabajo. El copiloto analiza sus escenarios, identifica los pasos ya implementados en el framework y propone la implementación de los nuevos, uno a la vez y con aprobación explícita del ingeniero.

### Inicio de una sesión de trabajo

1. Abrir el panel de GitHub Copilot Chat en VS Code.
2. Seleccionar el agente **Playwright Automation** en el selector de agentes.
3. Indicarle "Comenzar"

El copiloto puede operar en dos modos según el contexto:

**Modo A: Con acceso al código fuente**
- Solicita las variables: `feature_name`, `project_bdd`, `playwright_folder`, `code_folder`
- Analiza el código fuente estático para extraer localizadores
- Útil para aplicaciones modernas con código accesible

**Modo B: Sin acceso al código fuente** (aplicaciones legacy, framesets)
- Detecta automáticamente el workspace y feature activo
- Crea scripts temporales de inspección (`inspect_*.js`)
- Ejecuta el navegador para analizar el DOM real renderizado
- Extrae selectores del HTML en tiempo de ejecución

4. Revisar el análisis y continuar con el flujo de implementación.

### Métodos de obtención de localizadores

El copiloto soporta dos enfoques complementarios:

#### A. Análisis de código fuente estático (variable `code_folder`)
- **Cuándo usar**: Aplicaciones modernas con código fuente accesible (React, Vue, Angular)
- **Cómo funciona**: Analiza archivos HTML, JSX, templates para extraer selectores
- **Ventajas**: No requiere ejecutar la aplicación, análisis rápido
- **Limitaciones**: No detecta elementos generados dinámicamente por JavaScript

#### B. Inspección dinámica del DOM (sin `code_folder`)
- **Cuándo usar**: Aplicaciones legacy, framesets, sin acceso al código fuente
- **Cómo funciona**: 
  1. Crea scripts temporales que lanzan el navegador
  2. Inspecciona el DOM renderizado en tiempo real
  3. Detecta frames, elementos dinámicos y estructura real
  4. Extrae selectores precisos del HTML final
- **Ventajas**: Selectores 100% precisos del DOM real, detecta arquitecturas complejas
- **Ejemplo**: Aplicaciones con framesets, JSP con renderizado servidor, elementos cargados por AJAX

El copiloto elegirá automáticamente el enfoque más apropiado según el tipo de aplicación.

### Flujo de implementación paso a paso

1. El copiloto analiza el framework y el feature, identifica pasos existentes y nuevos.
2. Propone el primer escenario con código completo.
3. El ingeniero aprueba o rechaza: **"Aprobar escenario 1 (sí/no)"**
4. **Tras la aprobación**, el copiloto pregunta: **"¿Ejecutar la prueba ahora? (sí/no)"**
5. Solo tras confirmación, ejecuta la prueba en modo visible:
   ```bash
   npx cucumber-js --config cucumber.config.js src/features/<feature_name> --tags "@<tag>"
   ```
6. **Espera a que la ejecución termine completamente**.
7. **Pregunta obligatoriamente**: **"¿La prueba funcionó correctamente? (sí/no/error)"**
   - Si responde **"sí"**: Actualiza bitácora y propone siguiente escenario
   - Si responde **"no/error"**: Analiza el error, propone corrección y **pregunta antes de aplicarla**
8. **En caso de fallo**: 
   - **Nunca reintenta sin preguntar**
   - Muestra el error y propone solución
   - Pregunta: **"¿Aplicar esta corrección? (sí/no)"**
   - Si aprueba, pregunta: **"¿Ejecutar nuevamente? (sí/no)"**
   - Máximo 3 intentos con confirmación en cada uno
9. El ciclo se repite para cada escenario.
10. Al finalizar, actualiza la bitácora en `automation_logs/automation_bitacora.md`.

### Comandos disponibles para el ingeniero

| Orden | Efecto |
|---|---|
| `Aprobar escenario N (sí/no)` | Aprueba o rechaza la implementación propuesta |
| `Ejecutar` / `sí` | Confirma que se puede ejecutar la prueba |
| `Reintentar` / `sí` | Confirma que se puede volver a ejecutar tras corrección |
| `error` | Indica que hubo un error en la ejecución |
| `para` | Detiene el flujo de reintentos actual |
| `Reconsiderar escenario N` | El copiloto ofrece preguntas para entender el rechazo y mejorar la propuesta |
| `Finalizar sesión de trabajo` | Cierra la sesión y actualiza la bitácora con el estado actual |
| `Reiniciar sesión de trabajo` | Retoma la sesión desde el último punto registrado en la bitácora |
| `Cambiar de página/componente/feature` | Cambia el foco de trabajo, actualiza bitácora y reinicia el análisis |

---

## Salida Esperada

Cada sesión de trabajo produce los siguientes artefactos dentro de `framework-playwright`:

- **Archivos de Steps** (`src/steps/{funcionalidad}.steps.js`): Implementación de pasos Gherkin en JavaScript usando `this.page` del contexto compartido.
- **Page Objects** (`src/pages/{Funcionalidad}Page.js`): Encapsulación de interacciones con el navegador, recibiendo la página por constructor.
- **Localizadores** (`src/pages/pagesLocators/{Funcionalidad}PageLocators.js`): Selectores CSS, ARIA o data-testid centralizados como constantes `UPPER_SNAKE_CASE`.
- **Clases de datos** (`src/datas/{Funcionalidad}Data.js`): Objetos simples para almacenar datos del escenario cuando sea necesario.
- **Actualización de bitácora** (`automation_logs/automation_bitacora.md`): Registro de cada escenario automatizado con fecha, archivos modificados y observaciones.

El código generado es ejecutable directamente con:

```bash
npm run test
npm run test:smoke
npm run test:headed
```

---

## Reglas para la Generación de Código

### Arquitectura obligatoria

1. **Solo `common.steps.js` gestiona el ciclo de vida del navegador.** Ningún otro archivo de Steps define hooks `Before` o `After`.
2. **Los Page Objects reciben `this.page` por constructor.** Nunca instancian el navegador de forma independiente.
3. **Los localizadores residen en archivos `*PageLocators.js` separados.** No se definen inline en Page Objects ni en Steps.
4. **Los Steps usan el contexto compartido** (`this.page`, `this.baseUrl`, `this.config`). No acceden directamente a `page` sin pasar por un Page Object.
5. **Las queries SQL** se centralizan en `src/utils/QueryDeposit.js`. Nunca se escriben inline.

### Esperas y sincronización

6. **Prohibido `page.waitForTimeout()` con valores fijos.** Usar siempre esperas con condiciones de estado: `waitFor({ state: 'visible' })`, `waitForURL()`, `waitForLoadState()`.

### Seguridad

7. **Prohibido codificar URLs, credenciales o datos de entorno** directamente en el código. Usar `process.env` o archivos de entorno (`env.local.js`, `env.test.js`).
8. **Los archivos `.env`** con datos reales no se incluyen en control de versiones.

### Estilo y nomenclatura

9. **Comentarios, documentación y logs en español.**
10. **Nombres de clases en PascalCase en inglés** (ej. `LoginPage`, `MenuPage`).
11. **Métodos y variables en camelCase en inglés** (ej. `fillUsername()`, `loginButton`).
12. **Constantes de localizadores en UPPER_SNAKE_CASE en inglés** (ej. `LOGIN_BUTTON = '#loginBtn'`).
13. **Sin emojis, iconos ni símbolos decorativos** en ningún archivo del proyecto.

### Flujo de trabajo

14. **Un escenario a la vez.** El copiloto no avanza al siguiente sin aprobación explícita del ingeniero.
15. **Ejecución obligatoria tras implementación.** Cada escenario se ejecuta con `npm run test:headed` antes de pasar al siguiente.
16. **Máximo 2 reintentos autónomos** ante fallos de ejecución. En el tercer intento se escala al ingeniero con diagnóstico estructurado.
17. **`@pendiente` a nivel de escenario individual**, nunca a nivel de Feature completa.
