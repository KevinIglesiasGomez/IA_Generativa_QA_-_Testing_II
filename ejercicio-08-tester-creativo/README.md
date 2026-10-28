# Ejercicio 08 - Pruebas creativas y exploratorias

Asset: `Asset_TesterCreativo` (agente `Tester Creativo`).

## Objetivo

Encontrar defectos que las pruebas convencionales no detectan en un formulario de presupuesto de seguro de auto, aplicando técnicas creativas, pruebas extremas y el modelo EXPLORA.

## Datos

El agente admite varios tipos de entrada. Se proporcionan tres para elegir o combinar.

| Fichero | Tipo de entrada |
|---|---|
| `entrada/especificacion_presupuesto_auto.md` | Documentación funcional |
| `entrada/formulario_presupuesto.html` | HTML de la pantalla (abrir en el navegador para pruebas manuales) |
| `entrada/validaciones.js` | Código fuente de las validaciones y del cálculo |
| `solucion_esperada.md` | Defectos sembrados (no abrir antes de ejecutar) |

La pantalla funciona sin servidor: abrir `entrada/formulario_presupuesto.html` directamente en el navegador.

## Cómo ejecutarlo

1. Abrir el workspace `Asset_TesterCreativo`.
2. Lanzar el prompt `prompt_TesterCreativo` con el agente `Tester Creativo`.
3. Facilitar como entrada, por este orden, la especificación, el HTML y el código. Para una ejecución reducida usar `prompt_TesterCreativo_reducido` con solo la especificación.
4. Aprobar o rechazar cada escenario propuesto.
5. Ejecutar manualmente en el navegador los escenarios aprobados para confirmar los defectos.

Salida sugerida: `ejercicio-08-tester-creativo/salida/`.

## Criterios de evaluación

- El informe incluye escenarios no obvios con ángulo creativo justificado y puntuación de prioridad.
- Se detectan al menos 8 de los 15 defectos sembrados.
- Cada escenario es ejecutable con los datos disponibles y no inventa funcionalidad.
- Se cubren varias categorías EXPLORA y varias técnicas creativas distintas.
- El agente distingue los comportamientos correctos de los defectuosos.
