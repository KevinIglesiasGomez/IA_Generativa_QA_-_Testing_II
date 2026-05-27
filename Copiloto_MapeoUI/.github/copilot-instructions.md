# Instrucciones Globales - Demo_MapeoUI

## Proposito del Workspace

Este workspace contiene el copiloto **UI Mapper**: un agente de IA que analiza interfaces de usuario (web o movil) y genera los artefactos necesarios para automatizacion de pruebas - Page Objects, locator files y mapas UI JSON.

## Flujo de Trabajo (6 Steps)

| Step | Prompt | Descripcion |
|------|--------|-------------|
| 0 | `/ui_mapper_step0_discovery` | Descubrimiento del proyecto y deteccion de framework |
| 1 | `/ui_mapper_step1_screens` | Arbol de pantallas y navegacion |
| 2 | `/ui_mapper_step2_elements` | Mapeo de elementos UI por pantalla |
| 3 | `/ui_mapper_step3_selectors` | Extraccion y priorizacion de selectores |
| 4 | `/ui_mapper_step4_normalize` | Normalizacion de identificadores |
| 5 | `/ui_mapper_step5_artifacts` | Generacion de artefactos de testing |

## Convenciones de Nombres

- **Locator files:** `<pantalla>.locators.json` en `ui-map/<app>/locators/`
- **Page Objects:** `<Pantalla>Page.<ext>` en `ui-map/<app>/pages/`
- **Selectores:** preferir `data-testid` > ARIA roles > ID > CSS semantico

## Frameworks Soportados

- **Automatizacion destino:** Playwright, Cypress, Selenium, Appium
- **Plataformas:** Web (SPA/SSR), Android (Appium), iOS (Appium/XCUITest)

## Agente Principal

Usar el agente **@ui_mapper** para ejecutar el flujo completo. No se debe usar el chat general para tareas de mapeo UI.
