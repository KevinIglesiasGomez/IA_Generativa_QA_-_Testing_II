# Ejercicio 03 - Creación del framework de automatización

Assets: `Asset_Framework` (agentes `framework_setup` y `framework_test_generation`).

## Objetivo

Generar un framework Playwright + Cucumber (POM + Browser Factory) y automatizar el primer feature de login sobre una aplicación web de demostración.

## Datos

| Ruta | Contenido |
|---|---|
| `app-web/` | Aplicación Pruebas Seguros Web estática (ver `app-web/README.md`) |
| `features/Login.feature` | 10 escenarios BDD de login (entrada de ambos prompts) |
| `playwright-demo/` | Carpeta de destino del framework (se crea en la fase 1) |

## Preparación

```bash
npx http-server ejercicio-03-framework/app-web -p 8080
```

Dejar el servidor en una terminal aparte durante todo el ejercicio.

## Fase 1 - Estructura (`framework_step1_playwright_structure`)

| Variable | Valor |
|---|---|
| `playwright_folder` | `ejercicio-03-framework/playwright-demo` |
| `project_bdd` | `ejercicio-03-framework/features` |
| `environment_url` | `http://localhost:8080/login.html` |
| `username` | `cliente1,agente1` |
| `password` | `Cliente#24,Agente#24` |
| `role` | `cliente,agente` |

Resultado esperado: estructura `src/` con Browser Factory, environment loader, Cucumber como único ejecutor, sin pages ni steps específicos.

## Fase 2 - Pruebas (`framework_step2_playwright_tests`)

| Variable | Valor |
|---|---|
| `feature_name` | `Login.feature` |
| `project_bdd` | `ejercicio-03-framework/features` |
| `playwright_folder` | `ejercicio-03-framework/playwright-demo` |
| `JSP_folder` | `ejercicio-03-framework/app-web` |

Resultado esperado: `LoginPage.js`, locators, `login.steps.js` y ejecución de los 10 escenarios en modo no headless.

## Criterios de evaluación

- El framework no contiene datos específicos de la aplicación tras la fase 1.
- Solo `common.steps.js` gestiona el ciclo de vida del navegador.
- Los locators usan `data-testid` o `id`, nunca XPath absoluto.
- Los 10 escenarios pasan y se genera reporte JSON y HTML.
- Las credenciales se leen de variables de entorno, no del código.

## Continuación

El framework generado se usa como base en el ejercicio 04 (`Asset_AutomatizacionPlaywright`).
