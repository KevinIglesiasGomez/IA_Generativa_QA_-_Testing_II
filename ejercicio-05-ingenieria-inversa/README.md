# Ejercicio 05 - Ingeniería inversa funcional

Asset: `Asset_IngenieriaInversa` (agente `reverse_engineering_analyst`).

## Objetivo

Extraer documentación funcional (épicas, historias, casos funcionales, endpoints, reglas de negocio y guards) a partir del código fuente de una app Ionic + Angular.

## Datos

`pseg-app/` contiene el código fuente de la app móvil Pruebas Seguros (Angular 17 standalone + Ionic 7). No hace falta instalar dependencias: el análisis es estático.

| Capa | Ubicación |
|---|---|
| Routing | `src/app/app.routes.ts`, `features/*/*.routes.ts` |
| Guards | `src/app/core/guards/` |
| Enums y modelos | `src/app/core/enums/`, `src/app/core/models/` |
| Servicios (API) | `src/app/core/services/` |
| Páginas | `src/app/features/{login,home,polizas,siniestros,tasacion}/` |
| Entorno | `src/environments/environment.ts` |

## Cómo ejecutarlo

1. Abrir el workspace `Asset_IngenieriaInversa`.
2. Lanzar `reverse_engineering_step0_discovery` y responder a la pregunta de ruta con `ejercicio-05-ingenieria-inversa/pseg-app`.
3. Confirmar el mapa de módulos, guards y perfiles.
4. Lanzar `reverse_engineering_step1_general` para el documento general.
5. Lanzar `reverse_engineering_step2_detail` por cada historia o épica aprobada (por ejemplo, Declaración de siniestros y Tasación).

Salida sugerida: `ejercicio-05-ingenieria-inversa/salida/`.

## Qué se debe descubrir

- 5 módulos funcionales, 3 guards y 2 perfiles (resumen en `solucion_esperada.md`).
- Los endpoints consumidos y sus parámetros.
- Reglas de negocio embebidas en el código (plazos, límites, bloqueos).
- Funcionalidad no alcanzable desde la UI (debe documentarse como tal, sin inferir comportamiento).

## Criterios de evaluación

- Solo se documenta lo verificable en el código.
- Cada regla de negocio cita el fichero de origen.
- Las rutas se reconstruyen con el path completo (`/polizas/:idPoliza`).
- Se detecta que `siniestros/:idSiniestro` no tiene ningún enlace de entrada.
