# Solución esperada - Ejercicio 05

Uso exclusivo del instructor.

## Módulos

| Módulo | Rutas | Guards | Perfiles |
|---|---|---|---|
| Login | `/login` | `noAuthGuard` | Público |
| Home | `/home` | `authGuard` | CLIENTE, AGENTE |
| Pólizas | `/polizas`, `/polizas/:idPoliza` | `authGuard` | CLIENTE, AGENTE |
| Siniestros | `/siniestros/declarar`, `/siniestros/:idSiniestro` | `authGuard` | CLIENTE, AGENTE |
| Tasación | `/tasacion` | `authGuard`, `perfilGuard` | Solo AGENTE |

## Endpoints

| Método | URL | Origen |
|---|---|---|
| POST | `/auth/login` | `auth.service.ts` |
| GET | `/polizas?page&size&tipo` | `polizas.service.ts` |
| GET | `/polizas/{idPoliza}` | `polizas.service.ts` |
| POST | `/siniestros` | `siniestros.service.ts` |
| GET | `/siniestros?polizaId=` | `siniestros.service.ts` |
| GET | `/siniestros/{idSiniestro}` | `siniestros.service.ts` |
| POST | `/tasacion/preseleccion` | `tasacion.service.ts` |

## Reglas de negocio

| Regla | Origen |
|---|---|
| Usuario `^[A-Za-z0-9]{1,8}$`; contraseña solo obligatoria | `login.page.ts` |
| 5 intentos fallidos (401) bloquean el login 15 minutos en local | `auth.service.ts` |
| La sesión caduca según `expiresIn`; el guard la elimina | `auth.guard.ts` |
| El último usuario se precarga en el login | `auth.service.ts`, `login.page.ts` |
| Con sesión vigente, `/login` redirige a `/home` | `no-auth.guard.ts` |
| Sin perfil AGENTE se redirige a `/home?error=sin-permiso` | `perfil.guard.ts` |
| Solo pólizas VIGENTE permiten declarar siniestro | `siniestro-declarar.page.ts`, `poliza-detalle.page.ts` |
| Plazo de declaración: AUTO 30 días, HOGAR 7, VIDA 90 | `siniestro-declarar.page.ts` |
| Descripción de 20 a 500 caracteres; fecha no futura | `siniestro-declarar.page.ts` |
| Un 409 al declarar indica siniestro duplicado | `siniestro-declarar.page.ts` |
| Matrícula `^\d{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$`; km de 0 a 300000 | `tasacion-preseleccion.page.ts` |
| Antigüedad > 15 años: rechazo local, sin llamada a la API | `tasacion-preseleccion.page.ts` |
| Antigüedad > 10 años con resultado ACEPTADA pasa a REVISION_MANUAL | `tasacion-preseleccion.page.ts` |

## Hallazgos de calidad del código (intencionados)

- `siniestros/:idSiniestro` es alcanzable por ruta, pero ninguna pantalla enlaza a ella. El listado de siniestros en el detalle de póliza no es navegable.
- El perfil solo se comprueba en cliente (`perfilGuard`); no hay evidencia de control equivalente en backend en el código.
- El bloqueo por intentos fallidos se guarda en `localStorage` y se elude borrando el almacenamiento.
- `validarFecha` de siniestros depende de `polizasVigentes`, que puede estar vacío al evaluar el validador por primera vez.
- El campo de usuario del login tiene `maxlength="20"` mientras la regex admite 8 caracteres.
