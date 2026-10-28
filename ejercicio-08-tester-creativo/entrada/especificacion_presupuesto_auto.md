# Especificación - Presupuesto de seguro de auto (Pruebas Seguros)

## 1. Descripción

Formulario público que calcula una prima anual orientativa de seguro de auto. No requiere login. El resultado se muestra en pantalla y se anuncia que se enviará una copia al email indicado.

## 2. Campos y reglas

| Campo | Obligatorio | Regla |
|---|---|---|
| Matrícula | Sí | 4 dígitos y 3 consonantes (sin vocales, Ñ ni Q). Se admite minúscula y se normaliza a mayúscula |
| Fecha de nacimiento | Sí | El conductor debe tener 18 años cumplidos a fecha de hoy |
| Fecha del carné | Sí | No puede ser futura ni anterior al cumpleaños 18 del conductor |
| Código postal | Sí | 5 dígitos; los dos primeros entre 01 y 52 |
| Kilómetros anuales | Sí | Entero de 0 a 60000, ambos incluidos |
| Franquicia | Sí | 0, 150, 300 o 500 euros |
| Conductores adicionales | Sí | Entero de 0 a 3 |
| Cupón | No | Sin distinguir mayúsculas. `SOL10` aplica un 10% de descuento; `BIENVENIDA50` resta 50 euros |
| Email | Sí | Formato válido de correo electrónico |

## 3. Cálculo de la prima

1. Base: 150 euros si los kilómetros son inferiores a 5000; 300 euros en el resto de casos.
2. Recargo del 30% si el conductor tiene menos de 25 años.
3. Ajuste por franquicia: 0 euros de franquicia +15%; 150 sin cambio; 300 -5%; 500 -10%.
4. Se suman 40 euros por cada conductor adicional.
5. Se aplica el cupón si es válido.
6. La prima nunca puede ser inferior a 90 euros.
7. El resultado se redondea a dos decimales.

## 4. Comportamiento de la pantalla

- Los errores se muestran junto a cada campo y no se calcula la prima mientras haya errores.
- Al calcular correctamente se muestra "Prima anual estimada: X €" y "Hemos enviado una copia a <email>".
- Un cupón desconocido no bloquea el cálculo, pero se informa de que no es válido.
- El botón Calcular no debe permitir envíos repetidos mientras se procesa la petición.
