# Solución esperada - Ejercicio 06

Uso exclusivo del instructor.

## Inventario de elementos esperado

| Pantalla | Elemento | Mejor selector actual | Valoración |
|---|---|---|---|
| Login | Usuario | `[data-testid="login-usuario"]` | Robusto |
| Login | Contraseña | `[data-testid="login-password"]` | Robusto |
| Login | Mostrar contraseña | `[data-testid="login-ver-password"]` | Robusto |
| Login | Iniciar sesión | `[data-testid="login-submit"]` | Robusto |
| Login | Enlace recuperar | `[data-testid="login-recuperar"]` | Robusto |
| Pólizas | Título | `[data-testid="polizas-titulo"]` | Robusto |
| Pólizas | Cerrar sesión | `#btn1` | Frágil: id genérico |
| Pólizas | Filtro de tipo | `#select2` | Frágil: id genérico |
| Pólizas | Filas de la tabla | `tr.fila` | Frágil: sin identificador por póliza |
| Pólizas | Ver detalle | `getByRole('button', { name: 'Ver detalle' })` | Ambiguo: 3 coincidencias |
| Pólizas | Declarar siniestro | `[data-testid="polizas-nuevo-siniestro"]` | Robusto |
| Siniestro | Tipo | `.css-4f5g6h` | Muy frágil: clase ofuscada; `#field` duplicado |
| Siniestro | Fecha | `.css-7a8b9c` | Muy frágil; `#field` duplicado |
| Siniestro | Descripción | `.css-2d3e4f` | Muy frágil |
| Siniestro | Aceptar condiciones | `input[type="checkbox"]` | Sin identificador |
| Siniestro | Enviar | `getByRole('button', { name: 'Enviar' })` | Aceptable; estado inicial disabled |
| Siniestro | Cancelar | `getByRole('button', { name: 'Cancelar' })` | Aceptable |
| Siniestro | Mensaje de confirmación | `.css-1x2y3z` | Muy frágil |
| Siniestro | Mensaje de error | `.css-9k8j7h` | Muy frágil |

## Hallazgos clave

1. `id="field"` aparece dos veces en la misma pantalla (tipo y fecha): el selector `#field` es ambiguo.
2. Las clases `css-*` no son estables y no deben usarse como selector.
3. Los textos de error del login están disponibles con `data-testid`, no así los de Siniestro.
4. El botón Enviar depende del checkbox de condiciones (`enabled_condition`).
5. La navegación exige sesión en memoria; el acceso directo a `/polizas` redirige a `/login`.

## Artefactos esperados

- `LoginPage`, `PolizasPage` y `SiniestroPage` en `ui-map/<app>/pages/`.
- Locators JSON por pantalla en `ui-map/<app>/locators/`.
- Mapa UI JSON y informe de recomendaciones con prioridad ALTA para `SiniestroPage`.
