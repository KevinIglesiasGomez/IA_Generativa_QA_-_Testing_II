# Requisitos de datos - Cartera de seguros Pruebas Seguros

Documentación funcional para el Flujo A del Step 1 (análisis de documentación).

## 1. Contexto

Pruebas Seguros es la plataforma de gestión de seguros de una aseguradora española. Se necesita un conjunto de datos sintéticos para probar las pantallas de Mis pólizas, Declaración de siniestros y los procesos de consulta de la cartera. Los datos no deben contener información real.

## 2. Clientes

Cada cliente es una persona física residente en España.

- Se identifica por un identificador único interno y por su DNI.
- DNI: 8 dígitos y una letra de control calculada con el resto de dividir el número entre 23 (tabla `TRWAGMYFPDXBNJZSQVHLCKE`). No se admiten duplicados.
- Nombre y dos apellidos con nombres habituales en España, incluyendo acentos y la letra ñ.
- Email único. Teléfono móvil español que empieza por 6 o 7 con prefijo +34.
- Fecha de nacimiento: el cliente debe tener entre 18 y 90 años en la fecha de alta.
- Dirección postal: calle, número, ciudad, provincia y código postal de 5 dígitos coherente con la provincia (los dos primeros dígitos son el código de provincia).
- Fecha de alta en los últimos 5 años.

## 3. Pólizas

Un cliente puede tener entre 1 y 4 pólizas.

- Número de póliza con formato `P-` seguido de 6 dígitos, único.
- Tipos: AUTO, HOGAR y VIDA. Estados: VIGENTE, SUSPENDIDA y ANULADA.
- La vigencia es siempre de un año: la fecha de fin es la fecha de inicio más un año menos un día.
- Una póliza ANULADA tiene fecha de inicio anterior a hace 12 meses.
- Prima anual en euros con dos decimales: AUTO de 250 a 1.200, HOGAR de 120 a 600, VIDA de 80 a 900.
- Las pólizas AUTO incluyen matrícula (4 dígitos y 3 consonantes, sin vocales, Ñ ni Q). Las HOGAR incluyen dirección del riesgo. Las VIDA no incluyen ninguno de los dos.
- El 60% de las pólizas son AUTO o HOGAR; el 15% son VIDA; el resto se reparte.

## 4. Siniestros

Solo se declaran siniestros sobre pólizas AUTO o HOGAR.

- Referencia con formato `SIN-AAAA-NNNN`, única.
- Tipos para AUTO: COLISION, ROBO. Tipos para HOGAR: INCENDIO, AGUA, ROBO.
- La fecha del siniestro está dentro de la vigencia de la póliza y no es futura.
- La fecha de declaración es igual o posterior a la del siniestro; el plazo máximo es 30 días para AUTO y 7 para HOGAR.
- Una póliza ANULADA solo admite siniestros ocurridos antes de su anulación.
- Descripción de 20 a 500 caracteres en español, coherente con el tipo de siniestro.
- Estados: ABIERTO, EN_PERITACION, RESUELTO y RECHAZADO. El importe estimado es obligatorio salvo en ABIERTO y no puede superar 20.000 €.
- Aproximadamente el 35% de las pólizas AUTO o HOGAR tienen algún siniestro; ninguna tiene más de 3.

## 5. Volumen y condiciones de la generación

- Aproximadamente 200 clientes, 350 pólizas y 120 siniestros.
- Datos en español de España (`es_ES`), reproducibles con semilla.
- Casos habituales, casos límite (primas en el mínimo o máximo, clientes de 18 y 90 años, siniestro en el último día del plazo) y casos excepcionales (apellidos compuestos, direcciones con caracteres especiales).
- Formatos de entrega: CSV y JSON.
