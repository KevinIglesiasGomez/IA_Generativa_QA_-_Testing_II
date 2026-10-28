# Solución esperada - Ejercicio 08

Uso exclusivo del instructor. Defectos sembrados en `entrada/validaciones.js` y `entrada/formulario_presupuesto.html`.

| # | Defecto | Dónde | Entrada que lo revela | Resultado actual | Resultado esperado |
|---|---|---|---|---|---|
| 1 | La edad solo compara años | `calcularEdad` | Nacimiento hace 17 años y 11 meses | Se acepta como mayor de edad | Error "Debes ser mayor de edad." |
| 2 | Recargo por menor de 25 con la misma edad errónea | `calcularEdad` y `calcularPrima` | Nacimiento hace 24 años y 11 meses (cumple 25 en semanas) | Recargo aplicado o no según el año natural | Edad real |
| 3 | La matrícula admite vocales, Ñ y Q | `validarMatricula` | `1234AEI`, `1234QQQ` | Se acepta | Error de matrícula |
| 4 | El código postal admite provincias inexistentes | `validarCodigoPostal` | `00000`, `53000`, `99999` | Se acepta | Error: 01 a 52 |
| 5 | Kilómetros: el límite superior es exclusivo | `validarKilometros` | `60000` | Error | Se acepta (límite inclusivo) |
| 6 | Kilómetros: `parseInt` admite texto y decimales | `validarKilometros` | `12abc`, `1e3`, `3.9`, `0x10` | Se acepta como 12, 1, 3 y 0 | Error de formato |
| 7 | El email solo exige `algo@algo` | `validarEmail` | `a@b`, `@@`, `a b@c d` | Se acepta | Error de email |
| 8 | Fecha de carné futura permitida | `validarFechaCarnet` | Carné en 2050 | Se acepta | Error: no puede ser futura |
| 9 | Carné anterior a los 18 años por comparar solo años | `validarFechaCarnet` | Nacimiento 15/06/2000 y carné 01/01/2018 | Se acepta | Error: antes del cumpleaños 18 |
| 10 | Cupón sensible a mayúsculas | `aplicarCupon` | `sol10`, `Sol10` | "El cupón indicado no es válido." | Descuento del 10% |
| 11 | Conductores adicionales decimales | Formulario | `1.5` | Se cobra 60 € | Error: entero de 0 a 3 |
| 12 | Valor de franquicia manipulado en el DOM | `calcularPrima` | Cambiar la opción a `999` desde DevTools | `NaN €` | Rechazo de la petición |
| 13 | Inyección de HTML en el resultado | Formulario (`innerHTML`) | Email `<img src=x onerror=alert(1)>@a.com` | Se ejecuta el script | Texto escapado |
| 14 | No se evitan envíos repetidos | Formulario | Doble clic o Enter repetido en Calcular | Varios cálculos y mensajes | Botón deshabilitado durante el proceso |
| 15 | Fechas interpretadas en UTC | Varias | Nacimiento el día de hoy hace 18 años, cerca de medianoche | Resultado distinto según zona horaria | Cálculo con fecha local |

## Comportamientos correctos que deben confirmarse

- La prima mínima de 90 euros se respeta aunque el descuento sea alto.
- Un cupón desconocido no bloquea el cálculo y se informa.
- Con `adicionales` de 0 a 3 la suma es de 40 euros por conductor.

## Referencia para evaluar la creatividad

El informe debe incluir al menos 4 de estas técnicas: partición por valores límite, entradas hostiles (inyección, Unicode, emojis, espacios), manipulación del DOM, entradas de zona horaria o cambio de fecha, combinaciones de campos (edad, carné y fecha de nacimiento), automatización de doble envío y pruebas de accesibilidad con teclado.
