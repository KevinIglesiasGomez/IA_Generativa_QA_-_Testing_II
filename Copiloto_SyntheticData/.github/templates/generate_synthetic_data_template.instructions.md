# Plantilla de Datos Cliente

> Completa las secciones necesarias. Las marcadas con * son obligatorias.

---

## 1. Información Básica *

- **Proyecto**: [Nombre del proyecto]
- **Dominio**: [e-commerce, banca, salud, educación, etc.]
- **Propósito**: [testing funcional, rendimiento, demo, desarrollo]
- **Registros**: [cantidad aproximada total]

---

## 2. Descripción del Dominio *

¿Qué representa este dataset y para qué se usará?

```
[Escribe aquí una breve descripción del contexto de negocio]
```

---

## 3. Entidades y Campos *

### [Nombre_Entidad_1]

> [Breve descripción de qué representa esta entidad]

**Campos:**

| Campo | Tipo | Req | Único | PK | Restricciones | Ejemplo |
|-------|------|-----|-------|----|--------------| --------|
| id | uuid | ✓ | ✓ | ✓ | - | 550e8400-e29b-41d4... |
| nombre | string | ✓ | ✗ | ✗ | min: 2, max: 100 | Juan García |
| email | email | ✓ | ✓ | ✗ | formato email | user@example.com |
| fecha | date | ✓ | ✗ | ✗ | 1920-01-01 a hoy | 1985-03-15 |
| status | string | ✓ | ✗ | ✗ | [ACTIVE, INACTIVE] | ACTIVE |

**Relaciones:**
- Sin relaciones (entidad independiente)

**Reglas de negocio:**
- [Lista las reglas específicas para esta entidad]

---

### [Nombre_Entidad_2]

> [Breve descripción]

**Campos:**

| Campo | Tipo | Req | Único | PK | Restricciones | Ejemplo |
|-------|------|-----|-------|----|--------------| --------|
| id | uuid | ✓ | ✓ | ✓ | - | 650e8400-e29b-41d4... |
| entidad1_id | uuid | ✓ | ✗ | ✗ | FK a entidad1.id | 550e8400-e29b-41d4... |
| [otros campos] | ... | ... | ... | ... | ... | ... |

**Relaciones:**
- `entidad1_id` → `entidad1.id` (N:1)

**Reglas de negocio:**
- [Lista las reglas específicas]

---

_Repetir para cada entidad adicional_

---

#### Dataset de Ejemplo (Opcional pero recomendado)
**IMPORTANTE:** También se puede proporcionar un dataset de ejemplo con 5-10 registros por entidad para ilustrar el formato y las relaciones. Indicando claramente en este instruction que la generación final debe seguir las mismas reglas y estructura que el dataset de ejemplo.

## 4. Mapa de Relaciones

```
[Entidad1] 1 → N [Entidad2]
           ↓
           1 → N [Entidad3]
```

---

## 5. Validaciones Críticas *

Reglas que DEBEN cumplirse obligatoriamente:

1. [Ej: El email debe ser único en toda la base de datos]
2. [Ej: fecha_fin debe ser mayor que fecha_inicio]
3. [Ej: Los Foreign Keys deben apuntar a registros existentes]

---

## 6. Distribución de Datos (Opcional)

Si necesitas proporciones específicas, especifícalas aquí:

- **Casos normales (70%)**: [Describe los casos típicos]
- **Casos límite (20%)**: [Describe casos extremos válidos]
- **Casos excepcionales (10%)**: [Describe casos especiales]

---

## 7. Requisitos Especiales (Opcional)

Cualquier requisito adicional:

- [Ej: Incluir 20% de registros con múltiples relaciones]
- [Ej: Generar nombres que suenen naturales en español]
- [Ej: Usar códigos postales españoles]
- [Ej: Incluir caracteres especiales (ñ, acentos)]

---

## 8. Configuración (Opcional)

```yaml
locale: es_ES                    # Idioma/región para generación
seed: 42                         # Semilla para reproducibilidad
formatos: [CSV, JSON, SQL]       # Formatos de salida deseados
encoding: UTF-8                  # Codificación de caracteres
```

---

## Notas Adicionales

[Cualquier otra información relevante que no encaje en las secciones anteriores]

---

## Tipos de Datos Disponibles

- **Primitivos**: string, integer, decimal, boolean, date, datetime, uuid
- **Especializados**: email, phone, url, ip_address, postal_code, iban
- **Compuestos**: address, person, company, geolocation

## Restricciones Comunes

- `min` / `max`: Longitud (strings) o valor (números)
- `pattern`: Expresión regular
- `values`: Lista de valores permitidos [A, B, C]
- `range`: Rango de fechas o números

