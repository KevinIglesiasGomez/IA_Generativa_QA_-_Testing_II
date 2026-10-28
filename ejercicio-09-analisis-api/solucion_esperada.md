# Solución esperada - Ejercicio 09

Uso exclusivo del instructor.

## Gaps de cobertura (POISED)

| Categoría | Gap en las suites actuales |
|---|---|
| Parameters | Sin pruebas de `page`, `size` ni `tipo` inválidos, nulos o límite (0, 1, 50, 51); sin caracteres especiales ni parámetros omitidos |
| Codes | Solo se verifican 200 y 201; ningún 400, 401, 403, 404 ni 409 |
| Outputs | Sin validación de schema (`schemas/poliza.json` existe pero no se usa); sin comprobar campos extra ni tipos |
| Interoperability | No se comprueba que un siniestro creado aparezca en el listado por póliza ni en el detalle |
| Security | Sin pruebas sin token, con token inválido, ni de acceso a pólizas de otro cliente |
| Errors | No se valida el formato del error (`error.codigo`, `error.mensaje`) |
| Data | Datos fijos (`P-1001`, fecha `2026-10-20`) que dejan siniestros duplicados al repetir la ejecución |

Observaciones de arquitectura:

- Postman: el token se guarda en una variable de colección sin `Pre-request`; los tests de las requests son mínimos.
- Karate: `callonce` en `polizas.feature` reutiliza el login; no hay features de siniestros; `baseUrl` solo tiene entornos `local` y `test`.
- Karate: el assert `response.total == 3` depende de los datos de la semilla.

## Defectos sembrados en `mock-api/server.js`

| # | Endpoint | Entrada | Resultado actual | Resultado esperado según el contrato |
|---|---|---|---|---|
| 1 | `POST /siniestros` | `descripcion` null o ausente | 500 con el mensaje interno de la excepción | 400 con mensaje de validación (y nunca 500) |
| 2 | `GET /polizas/{id}` | `P-2001` con `cliente1` | 200 con datos de otro cliente | 403 |
| 3 | `POST /siniestros` | `polizaId` = `P-1003` (ANULADA) | 201 | 409 |
| 4 | `POST /siniestros` | `polizaId` = `P-2001` con `cliente1` | 201 | 403 |
| 5 | `GET /siniestros` | Sin `polizaId` | Devuelve los siniestros de todos los usuarios | Solo los del usuario |
| 6 | `GET /siniestros/{id}` | Siniestro de otro usuario | 200 | 403 o 404 |
| 7 | `POST /auth/login` | Intentos repetidos con contraseña incorrecta | Siempre 401, sin límite | Bloqueo o limitación de intentos |
| 8 | `GET /polizas` | Cualquier petición válida | Sin `Cache-Control: no-store` | Cabecera de no cacheo para datos personales |
| 9 | `POST /siniestros` | `descripcion` con 19 o 501 caracteres | 400 | Correcto, comprobar límites 20 y 500 |
| 10 | `POST /siniestros` | Fecha futura | 400 | Correcto |

Los puntos 9 y 10 son comportamientos correctos que el agente debe confirmar sin marcarlos como defecto.

## Escenarios que deberían proponerse en las primeras iteraciones

1. `GET /polizas` sin token devuelve 401 con cuerpo de error estándar.
2. `GET /polizas?page=0`, `size=51` y `tipo=OTRO` devuelven 400.
3. `GET /polizas/P-2001` con `cliente1` devuelve 403 (falla: defecto 2).
4. `POST /siniestros` con `descripcion` null devuelve 400 (falla: defecto 1).
5. `POST /siniestros` duplicado devuelve 409.
6. Validación de schema de póliza y de siniestro.
