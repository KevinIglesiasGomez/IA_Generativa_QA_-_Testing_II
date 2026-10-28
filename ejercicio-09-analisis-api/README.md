# Ejercicio 09 - Análisis de calidad de pruebas API

Asset: `Asset_AnalisisPruebasAPI` (agente `API Test Analizer`, modelo POISED).

## Objetivo

Analizar una suite de pruebas API existente, detectar gaps de cobertura endpoint por endpoint y proponer, con aprobación individual, las pruebas que faltan.

## Datos

| Ruta | Contenido |
|---|---|
| `mock-api/` | API de demostración de Pruebas Seguros (Node.js sin dependencias) para ejecutar las pruebas |
| `postman/` | Colección Postman de humo y entorno local |
| `karate/` | Proyecto Karate (Maven) con `karate-config.js`, helper de login y 2 features |
| `openapi/pseg-api.yaml` | Contrato de la API, fuente de verdad para detectar desviaciones |
| `solucion_esperada.md` | Gaps y defectos sembrados (no abrir antes de ejecutar) |

Credenciales: `cliente1` / `Cliente#24` (CLIENTE) y `agente1` / `Agente#24` (AGENTE). El cliente solo debe ver sus pólizas P-1001, P-1002 y P-1003.

## Preparación

```bash
cd ejercicio-09-analisis-api/mock-api
npm start
```

La API queda en `http://localhost:3000/api/v1`. Los datos viven en memoria y se reinician al parar el proceso.

Para ejecutar las suites actuales:

- Postman: importar `postman/PSEG_API.postman_collection.json` y `postman/PSEG_Local.postman_environment.json`, y lanzar el Collection Runner.
- Karate (requiere Java 17 y Maven): `cd karate` y `mvn test`.

## Cómo ejecutarlo

1. Abrir el workspace `Asset_AnalisisPruebasAPI`.
2. Lanzar `api_test_analizer_step1` con el agente `API Test Analizer`.
3. Indicar el tipo de proyecto (Karate o Postman) y la suite a revisar. Se recomienda hacer ambos por separado y comparar.
4. Revisar el informe POISED y aprobar o rechazar cada escenario propuesto.
5. Lanzar `api_test_analizer_step2` para continuar con la implementación y actualizar la bitácora.

## Criterios de evaluación

- El análisis de arquitectura identifica `karate-config.js`, `callonce` y el uso de variables de colección en Postman.
- El informe prioriza los gaps por riesgo e impacto, y los propuestos no inventan endpoints.
- Se detectan los defectos reales al ejecutar los escenarios aprobados (ver `solucion_esperada.md`).
- Los escenarios propuestos son incrementales, justificados y sin sobre-testing.
- La bitácora refleja los escenarios añadidos y los rechazados con su motivo.
