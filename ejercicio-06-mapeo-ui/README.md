# Ejercicio 06 - Mapeo de interfaz de usuario

Asset: `Asset_MapeoUI` (agente `ui_mapper`).

## Objetivo

Descubrir las pantallas de una app React, extraer y priorizar selectores, normalizar identificadores y generar Page Objects, locator files y el mapa UI en JSON.

## Datos

`pseg-react/` es una app React 18 + Vite + React Router con tres pantallas y calidad de selectores deliberadamente desigual.

| Pantalla | Ruta | Calidad de selectores |
|---|---|---|
| `LoginPage.jsx` | `/login` | Alta: `data-testid`, `id`, `label` asociado |
| `PolizasPage.jsx` | `/polizas` | Media: ids genéricos (`btn1`, `div1`, `select2`), filas sin identificar |
| `SiniestroPage.jsx` | `/siniestro/nuevo` | Baja: clases ofuscadas (`css-xxxx`), `id="field"` duplicado, botones sin identificar |

Credenciales de la app: `cliente1` / `Cliente#24` y `agente1` / `Agente#24`.

## Cómo ejecutarlo

Modo estático (código fuente), sin arrancar la app:

| Variable | Valor |
|---|---|
| `project_path` | `ejercicio-06-mapeo-ui/pseg-react` |
| `testing_target` | `playwright` |

Modo dinámico (opcional):

```bash
cd ejercicio-06-mapeo-ui/pseg-react
npm install
npm run dev
```

Con la app en marcha usar `http://localhost:5173` como `project_path`. La sesión vive en memoria: tras recargar hay que volver a iniciar sesión.

Después seguir los prompts `ui_mapper_step1_screens` a `ui_mapper_step5_artifacts` y confirmar cada paso. Salida sugerida: `ejercicio-06-mapeo-ui/ui-map/`.

## Criterios de evaluación

- Se detectan 3 pantallas y el flujo Login -> Pólizas -> Siniestro.
- Los selectores de `LoginPage` se priorizan por `data-testid`.
- Se marcan como frágiles los ids genéricos y las clases `css-xxxx`.
- Se detecta la colisión del `id="field"` en `SiniestroPage` y se propone un selector de contexto.
- Se registra el estado inicial del botón Enviar (deshabilitado hasta aceptar condiciones).
- Las recomendaciones piden añadir `data-testid` en las pantallas Pólizas y Siniestro.
