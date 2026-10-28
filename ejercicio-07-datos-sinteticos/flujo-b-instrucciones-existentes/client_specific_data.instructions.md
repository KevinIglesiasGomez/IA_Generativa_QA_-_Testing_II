<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

# Datos Cliente - Cartera de seguros Pruebas Seguros

---

## 1. Información Básica *

- **Proyecto**: Pruebas Seguros - Cartera de Seguros
- **Dominio**: seguros
- **Propósito**: testing funcional
- **Registros**: 670 aproximados (200 clientes, 350 pólizas, 120 siniestros)

---

## 2. Descripción del Dominio *

```
Cartera de una aseguradora española con clientes, pólizas de auto, hogar y vida, y siniestros declarados sobre pólizas de auto y hogar. Se usará para probar las pantallas de consulta de pólizas y declaración de siniestros de la plataforma Pruebas Seguros.
```

---

## 3. Entidades y Campos *

### clientes

> Persona física residente en España titular de una o varias pólizas.

**Campos:**

| Campo | Tipo | Req | Único | PK | Restricciones | Ejemplo |
|-------|------|-----|-------|----|---------------|---------|
| id_cliente | uuid | ✓ | ✓ | ✓ | - | 550e8400-e29b-41d4-a716-446655440001 |
| dni | string | ✓ | ✓ | ✗ | 8 dígitos + letra de control (mod 23) | 12345678Z |
| nombre | string | ✓ | ✗ | ✗ | min: 2, max: 40 | Lucía |
| apellido1 | string | ✓ | ✗ | ✗ | min: 2, max: 40 | Fernández |
| apellido2 | string | ✗ | ✗ | ✗ | max: 40 | Ruiz |
| email | email | ✓ | ✓ | ✗ | formato email | lucia.fernandez@example.com |
| telefono | string | ✓ | ✗ | ✗ | +34 seguido de 9 dígitos que empiezan por 6 o 7 | +34612345678 |
| fecha_nacimiento | date | ✓ | ✗ | ✗ | edad entre 18 y 90 años en fecha_alta | 1985-03-15 |
| direccion | string | ✓ | ✗ | ✗ | calle y número | Calle Alcalá 45 |
| ciudad | string | ✓ | ✗ | ✗ | catálogo ciudades_provincias_es | Madrid |
| provincia | string | ✓ | ✗ | ✗ | catálogo ciudades_provincias_es | Madrid |
| codigo_postal | string | ✓ | ✗ | ✗ | 5 dígitos; 2 primeros = código de provincia | 28014 |
| fecha_alta | date | ✓ | ✗ | ✗ | últimos 5 años | 2023-06-10 |

**Relaciones:**
- Entidad independiente (1:N con polizas)

**Reglas de negocio:**
- El DNI no se repite entre clientes y su letra se calcula con `TRWAGMYFPDXBNJZSQVHLCKE`.
- El email no se repite.

---

### polizas

> Contrato de seguro de un cliente.

**Campos:**

| Campo | Tipo | Req | Único | PK | Restricciones | Ejemplo |
|-------|------|-----|-------|----|---------------|---------|
| numero_poliza | string | ✓ | ✓ | ✓ | formato P-NNNNNN | P-100245 |
| id_cliente | uuid | ✓ | ✗ | ✗ | FK a clientes.id_cliente | 550e8400-e29b-41d4-a716-446655440001 |
| tipo | string | ✓ | ✗ | ✗ | [AUTO, HOGAR, VIDA] | AUTO |
| estado | string | ✓ | ✗ | ✗ | [VIGENTE, SUSPENDIDA, ANULADA] | VIGENTE |
| fecha_inicio | date | ✓ | ✗ | ✗ | últimos 5 años | 2026-01-01 |
| fecha_fin | date | ✓ | ✗ | ✗ | fecha_inicio + 1 año - 1 día | 2026-12-31 |
| prima_anual | decimal | ✓ | ✗ | ✗ | 2 decimales; AUTO 250-1200, HOGAR 120-600, VIDA 80-900 | 412.50 |
| matricula | string | ✗ | ✗ | ✗ | obligatoria solo en AUTO; 4 dígitos + 3 consonantes | 1234BCD |
| direccion_riesgo | string | ✗ | ✗ | ✗ | obligatoria solo en HOGAR | Calle Mayor 12, Valencia |

**Relaciones:**
- `id_cliente` → `clientes.id_cliente` (N:1)

**Reglas de negocio:**
- Cada cliente tiene entre 1 y 4 pólizas.
- Una póliza ANULADA tiene fecha_inicio anterior a hace 12 meses.
- VIDA no lleva matrícula ni dirección de riesgo.

---

### siniestros

> Siniestro declarado sobre una póliza AUTO o HOGAR.

**Campos:**

| Campo | Tipo | Req | Único | PK | Restricciones | Ejemplo |
|-------|------|-----|-------|----|---------------|---------|
| id_siniestro | uuid | ✓ | ✓ | ✓ | - | 750e8400-e29b-41d4-a716-446655440010 |
| referencia | string | ✓ | ✓ | ✗ | formato SIN-AAAA-NNNN | SIN-2026-1042 |
| numero_poliza | string | ✓ | ✗ | ✗ | FK a polizas.numero_poliza, tipo AUTO o HOGAR | P-100245 |
| tipo | string | ✓ | ✗ | ✗ | AUTO [COLISION, ROBO]; HOGAR [INCENDIO, AGUA, ROBO] | COLISION |
| fecha_siniestro | date | ✓ | ✗ | ✗ | dentro de la vigencia y no futura | 2026-03-10 |
| fecha_declaracion | date | ✓ | ✗ | ✗ | >= fecha_siniestro; máx. 30 días AUTO, 7 HOGAR | 2026-03-12 |
| descripcion | string | ✓ | ✗ | ✗ | min: 20, max: 500; coherente con el tipo | Colisión trasera en un semáforo con daños en el paragolpes |
| estado | string | ✓ | ✗ | ✗ | [ABIERTO, EN_PERITACION, RESUELTO, RECHAZADO] | EN_PERITACION |
| importe_estimado | decimal | ✗ | ✗ | ✗ | obligatorio salvo ABIERTO; máx. 20000 | 1850.00 |

**Relaciones:**
- `numero_poliza` → `polizas.numero_poliza` (N:1)

**Reglas de negocio:**
- Una póliza ANULADA solo admite siniestros ocurridos antes de su anulación.
- Ninguna póliza tiene más de 3 siniestros; el 35% de las AUTO y HOGAR tienen al menos uno.

---

#### Dataset de Ejemplo

La generación final debe seguir las mismas reglas y estructura que este dataset.

**clientes**

| id_cliente | dni | nombre | apellido1 | apellido2 | email | telefono | fecha_nacimiento | direccion | ciudad | provincia | codigo_postal | fecha_alta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 550e8400-e29b-41d4-a716-446655440001 | 12345678Z | Lucía | Fernández | Ruiz | lucia.fernandez@example.com | +34612345678 | 1985-03-15 | Calle Alcalá 45 | Madrid | Madrid | 28014 | 2023-06-10 |
| 550e8400-e29b-41d4-a716-446655440002 | 87654321X | Marcos | Ortega | Gil | marcos.ortega@example.com | +34698765432 | 1972-11-02 | Avenida del Puerto 8 | Valencia | Valencia | 46023 | 2022-01-20 |
| 550e8400-e29b-41d4-a716-446655440003 | 11223344B | Núria | Puig | Casals | nuria.puig@example.com | +34711223344 | 1996-07-28 | Carrer de Mallorca 210 | Barcelona | Barcelona | 08036 | 2024-09-05 |
| 550e8400-e29b-41d4-a716-446655440004 | 23456789D | José Ángel | Muñoz | | joseangel.munoz@example.com | +34623456789 | 1950-01-30 | Calle Larga 3 | Sevilla | Sevilla | 41003 | 2022-03-14 |
| 550e8400-e29b-41d4-a716-446655440005 | 34567890V | Irene | Vázquez | Lago | irene.vazquez@example.com | +34734567890 | 2007-12-01 | Rúa Nova 17 | Vigo | Pontevedra | 36201 | 2025-12-02 |

**polizas**

| numero_poliza | id_cliente | tipo | estado | fecha_inicio | fecha_fin | prima_anual | matricula | direccion_riesgo |
|---|---|---|---|---|---|---|---|---|
| P-100245 | 550e8400-e29b-41d4-a716-446655440001 | AUTO | VIGENTE | 2026-01-01 | 2026-12-31 | 412.50 | 1234BCD | |
| P-100246 | 550e8400-e29b-41d4-a716-446655440001 | HOGAR | VIGENTE | 2026-02-15 | 2027-02-14 | 238.00 | | Calle Alcalá 45, Madrid |
| P-100301 | 550e8400-e29b-41d4-a716-446655440002 | AUTO | ANULADA | 2023-03-01 | 2024-02-29 | 250.00 | 5678FGH | |
| P-100412 | 550e8400-e29b-41d4-a716-446655440003 | VIDA | VIGENTE | 2025-05-10 | 2026-05-09 | 900.00 | | |
| P-100530 | 550e8400-e29b-41d4-a716-446655440004 | HOGAR | SUSPENDIDA | 2025-09-01 | 2026-08-31 | 600.00 | | Calle Larga 3, Sevilla |

**siniestros**

| id_siniestro | referencia | numero_poliza | tipo | fecha_siniestro | fecha_declaracion | descripcion | estado | importe_estimado |
|---|---|---|---|---|---|---|---|---|
| 750e8400-e29b-41d4-a716-446655440010 | SIN-2026-1042 | P-100245 | COLISION | 2026-03-10 | 2026-03-12 | Colisión trasera en un semáforo con daños en el paragolpes | EN_PERITACION | 1850.00 |
| 750e8400-e29b-41d4-a716-446655440011 | SIN-2026-1043 | P-100246 | AGUA | 2026-03-20 | 2026-03-26 | Rotura de tubería en la cocina con daños en el suelo y la pared | ABIERTO | |
| 750e8400-e29b-41d4-a716-446655440012 | SIN-2023-0877 | P-100301 | ROBO | 2023-10-05 | 2023-10-06 | Robo del vehículo estacionado en la vía pública durante la noche | RESUELTO | 12000.00 |

---

## 4. Mapa de Relaciones

```
clientes 1 → N polizas 1 → N siniestros
```

---

## 5. Validaciones Críticas *

1. DNI y email únicos; letra del DNI correcta.
2. Todas las claves foráneas apuntan a registros existentes.
3. fecha_fin = fecha_inicio + 1 año - 1 día.
4. Prima dentro del rango del tipo de póliza.
5. Matrícula solo en AUTO y dirección de riesgo solo en HOGAR.
6. Siniestros solo sobre pólizas AUTO o HOGAR, dentro de la vigencia, no futuros y dentro del plazo de declaración.
7. importe_estimado obligatorio salvo estado ABIERTO y nunca superior a 20000.

---

## 6. Distribución de Datos

- **Casos normales (70%)**: clientes de 25 a 70 años, primas en el rango central, pólizas vigentes.
- **Casos límite (20%)**: clientes de 18 y 90 años, primas en el mínimo y máximo, siniestro en el último día del plazo, siniestro el día de inicio o fin de vigencia.
- **Casos excepcionales (10%)**: apellidos compuestos o sin segundo apellido, direcciones con caracteres especiales, pólizas SUSPENDIDA o ANULADA con siniestros previos.

---

## 7. Requisitos Especiales

- Nombres y apellidos naturales en español, con acentos y ñ.
- Ciudades, provincias y códigos postales coherentes entre sí.
- Descripciones de siniestro coherentes con el tipo.

---

## 8. Configuración

```yaml
locale: es_ES
seed: 42
formatos: [CSV, JSON]
encoding: UTF-8
```
