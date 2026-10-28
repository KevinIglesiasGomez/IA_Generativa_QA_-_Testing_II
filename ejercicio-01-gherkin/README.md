# Ejercicio 01 - Generación de escenarios Gherkin

Asset: `Asset_Gherkin` (agente `Generador de escenarios Gherkin`).

## Objetivo

Generar archivos `.feature` y un informe de cobertura a partir de documentación funcional de una app móvil de seguros (Splash, Onboarding, Login nativo, Home y Entrada de tasación).

## Datos

| Fichero | Contenido |
|---|---|
| `documentacion/Splash.md` | Arranque de la app, dispositivo inseguro, actualización forzada y sin conexión |
| `documentacion/Onboarding+-+Definición+de+historias+de+usuario.md` | Historias de onboarding |
| `documentacion/Login+nativo+-+Definición+de+historias+de+usuario.md` | Login, biometría, autologado y gestión de errores |
| `documentacion/Home+-+Definición+de+historias+de+usuario.md` | Pantalla principal |
| `documentacion/Entrada+-+tasacion+-+preseleccion.md` | Entrada al flujo de tasación |

## Cómo ejecutarlo

1. Abrir el workspace `Asset_Gherkin`.
2. Lanzar `generate_gherkin_step0` con estas variables:

| Variable | Valor |
|---|---|
| `document_location` | `ejercicio-01-gherkin/documentacion` |
| `e2e_repo` | `ejercicio-01-gherkin/salida` |

3. Continuar con los prompts `step1` a `step5`. El `step2` (MCP) es opcional y no es necesario para este ejercicio; la sincronización con Xray es una skill aparte y tampoco se usa aquí.

## Criterios de evaluación

- Un `.feature` por área funcional en `salida/features/` y un informe `INFORME_<fecha_hora>.md` en la raíz de `salida/`.
- Más de 15 escenarios por característica, con flujos positivos, negativos y valores límite (por ejemplo, la regex de usuario `^[A-Za-z0-9]{1,8}$`).
- Etiquetas `@smoke` y `@regression`, y áreas funcionales.
- Pasos reutilizados y parametrizados entre features.
- Sin datos sensibles escritos en los escenarios.

## Continuación

Los casos resultantes alimentan el ejercicio 02 (detección de duplicados) y los escenarios de login se automatizan en los ejercicios 03 y 04.
