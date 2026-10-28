# Ejercicio 04 - Automatización de escenarios con Playwright

Asset: `Asset_AutomatizacionPlaywright` (agente `Playwright Automation`).

## Objetivo

Automatizar, escenario a escenario y con aprobación del ingeniero, features BDD sobre un framework Playwright + Cucumber ya existente.

## Requisitos previos

1. Haber completado el ejercicio 03: el framework debe estar en `ejercicio-03-framework/playwright-demo` con el login automatizado (`LoginPage`, `login.steps.js`, `common.steps.js`).
2. Servidor de la aplicación en marcha:

```bash
npx http-server ejercicio-03-framework/app-web -p 8080
```

Si no se dispone del framework, ejecutar antes la fase 1 del ejercicio 03.

## Datos

| Fichero | Contenido |
|---|---|
| `features/Polizas.feature` | 7 escenarios, uno con tabla de ejemplos (3 casos) |
| `features/Siniestros.feature` | 6 escenarios, dos con tabla de ejemplos (8 casos) |

Ambos features reutilizan el paso `Dado que el usuario "<usuario>" ha iniciado sesión con la contraseña "<contraseña>"`, que se implementa una sola vez a partir del login del ejercicio 03.

## Cómo ejecutarlo

Copiar los `.feature` a `ejercicio-03-framework/playwright-demo/src/features/` y lanzar los prompts por orden (`playwright_auto_step0_contexto_analisis`, `step1_analisis`, `step2_flujo_implementacion`, `step3_verificacion_calidad`) con:

| Variable | Valor |
|---|---|
| `feature_name` | `Polizas.feature` y después `Siniestros.feature` |
| `project_bdd` | `ejercicio-03-framework/playwright-demo/src/features` |
| `playwright_folder` | `ejercicio-03-framework/playwright-demo` |
| `code_folder` | `ejercicio-03-framework/app-web` |

El agente propone un escenario cada vez y espera la aprobación antes de implementarlo y ejecutarlo.

## Puntos a observar

- Reutilización de steps y pages existentes antes de crear código nuevo.
- Manejo de fechas relativas ("hace 2 días", "dentro de 3 días") sin valores fijos.
- Escenario de seguridad: acceso directo a `poliza.html?id=P-2001` con `cliente1`.
- Esquemas con valores límite (19, 20, 500 y 501 caracteres).
- Bitácora de automatización actualizada tras cada escenario confirmado.

## Criterios de evaluación

- Los 13 escenarios pasan con ejecución visible.
- Ningún step crea instancias de navegador fuera de `common.steps.js`.
- Sin `waitForTimeout` fijos; se usan esperas de Playwright sobre locators.
- Locators separados en `pagesLocators` con `data-testid`.
