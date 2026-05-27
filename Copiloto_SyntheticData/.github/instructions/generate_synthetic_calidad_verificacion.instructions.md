# Verificación de Calidad: Validaciones obligatorias para datasets sintéticos

Es obligatorio que cada dataset sintético generado cumpla con los siguientes criterios de calidad y verificación para asegurar su utilidad y fiabilidad.

---

### Dimensiones de Calidad de Datos

**1. COMPLETITUD (Completeness)**

Definición: Porcentaje de valores presentes vs esperados

Métricas:
- % campos requeridos con valores
- % registros completos
- Conteo de valores nulos/vacíos

Umbrales:
- Crítico: >99% para campos obligatorios
- Aceptable: >95% para campos opcionales
- Inaceptable: <90%


**2. VALIDEZ (Validity)**

Definición: Conformidad con reglas de negocio y restricciones

Validaciones:
- Tipos de datos correctos
- Formatos válidos (email, teléfono, etc.)
- Valores dentro de rangos permitidos
- Cumplimiento de expresiones regulares
- Valores en listas permitidas (enums)

Umbrales:
- Crítico: >99.9%
- Aceptable: >98%
- Inaceptable: <95%


**3. UNICIDAD (Uniqueness)**

Definición: Ausencia de duplicados en campos únicos

Validaciones:
- Primary keys sin duplicados (100%)
- Campos unique sin duplicados
- Combinaciones únicas donde aplique

Umbrales:
- Crítico: 100% para PKs
- Aceptable: >99% para campos unique
- Inaceptable: <98%


**4. CONSISTENCIA (Consistency)**

Definición: Coherencia entre campos relacionados

Validaciones:
- Fechas lógicas (fecha_fin > fecha_inicio)
- Relaciones matemáticas (subtotal + IVA = total)
- Estados coherentes (estado=ENVIADO → fecha_envio no nula)
- Formatos consistentes

Umbrales:
- Crítico: >99%
- Aceptable: >95%
- Inaceptable: <90%


**5. INTEGRIDAD REFERENCIAL (Referential Integrity)**

Definición: Validez de relaciones entre entidades

Validaciones:
- Foreign keys apuntan a registros existentes
- Relaciones bidireccionales coherentes
- Cardinalidades respetadas (1:1, 1:N, N:M)

Umbrales:
- Crítico: 100%
- Aceptable: >99.5%
- Inaceptable: <98%


**6. EXACTITUD (Accuracy)**

Definición: Realismo y coherencia con el dominio

Validaciones:
- Valores realistas para el contexto
- Distribuciones apropiadas
- Coherencia cultural/geográfica
- Lógica de negocio aplicada

Evaluación: Cualitativa + muestreo manual


---

### Validaciones Obligatorias Pre-Generación

**CHECKLIST PRE-GENERACIÓN:**
- [ ] El esquema está completamente definido en schemas/schema.json
- [ ] Todos los campos tienen tipo de dato especificado
- [ ] Los campos requeridos están marcados como required: true
- [ ] Los campos únicos están marcados como unique: true
- [ ] Las restricciones (min, max, pattern) están definidas
- [ ] Las relaciones entre entidades están mapeadas
- [ ] Las estrategias de generación están asignadas
- [ ] Los diccionarios de datos están disponibles si se necesitan
- [ ] La configuración de generación (semilla, cantidad) está definida
- [ ] El propósito del dataset está documentado

---

### Validaciones Obligatorias Post-Generación

**1. VALIDACIÓN DE ESQUEMA:**

- Todos los campos del esquema existen en los datos
- No hay campos extra no definidos en el esquema
- Nombres de campos coinciden exactamente

**2. VALIDACIÓN DE TIPOS:**

- Integer: valores numéricos enteros
- Float: valores numéricos con decimales
- String: cadenas de texto
- Boolean: true/false
- Date: formato YYYY-MM-DD
- DateTime: formato ISO 8601
- UUID: formato UUID v4
- Email: formato válido de email
- Teléfono: formato válido de teléfono
- Enum: valores dentro de la lista permitida

**3. VALIDACIÓN DE RESTRICCIONES:**

- Min/max length para strings
- Min/max value para números
- Pattern regex para formatos
- Enum values para listas cerradas
- Not null para campos requeridos

**4. VALIDACIÓN DE UNICIDAD:**

- Primary keys únicos (100%)
- Campos unique sin duplicados
- Combinaciones únicas donde aplique
- Reporte de duplicados encontrados


**5. VALIDACIÓN DE INTEGRIDAD REFERENCIAL:**

- Foreign keys válidos
- Referencias a registros existentes
- Navegabilidad bidireccional


**6. VALIDACIÓN DE REGLAS DE NEGOCIO:**

- Fechas lógicas (orden temporal)
- Cálculos correctos (totales)
- Estados coherentes
- Dependencias condicionales

---

### Reporte de Calidad

Genera un reporte para lectura humana y análisis automático con las siguientes secciones: 
- Resumen ejecutivo con métricas clave
- Detalles de validación 
- Checklist de aceptación

---

### Criterios de Aceptación

**DATASET APROBADO:**

- Completitud: ≥99%
- Validez: ≥99%
- Unicidad: 100% para PKs, ≥99% para unique fields
- Consistencia: ≥95%
- Integridad referencial: 100%
- Quality Score Global: ≥98%

**DATASET CON ADVERTENCIAS:**

- Completitud: 95-99%
- Validez: 95-99%
- Unicidad: ≥98%
- Consistencia: 90-95%
- Integridad referencial: 98-100%
- Quality Score Global: 95-98%

Acción: Revisar advertencias y documentar excepciones

**DATASET RECHAZADO:**

- Cualquier dimensión <90%
- Integridad referencial <98%
- Quality Score Global <95%

Acción: Regenerar dataset corrigiendo errores

### Muestreo Manual por experto humano

**Proceso:**
1. Seleccionar muestra aleatoria de 50-100 registros
2. Revisión manual por experto del dominio
3. Verificar realismo y coherencia
4. Documentar hallazgos cualitativos

**Checklist Muestreo:**
- [ ] Los nombres suenan realistas
- [ ] Las direcciones son coherentes geográficamente
- [ ] Las fechas tienen sentido lógico
- [ ] Los importes son razonables
- [ ] Los estados/flujos son lógicos
- [ ] No hay patrones obvios artificiales

---

### Validación de Seguridad y Privacidad

**CHECKLIST OBLIGATORIO:**
- [ ] No hay datos personales reales
- [ ] No hay DNI/NIE/NIF reales válidos
- [ ] No hay IBAN reales válidos
- [ ] No hay tarjetas de crédito reales
- [ ] Emails en dominios ficticios (example.com, test.com)
- [ ] Teléfonos en rangos ficticios (555-xxxx)
- [ ] Direcciones ficticias o anonimizadas
- [ ] No hay información confidencial empresarial real
- [ ] Disclaimer de datos sintéticos incluido
- [ ] Documentación GDPR compliance incluida

---

### Validación de Formatos de Salida

**Para cada formato generado:**

CSV:
- [ ] Encoding UTF-8 con BOM
- [ ] Primera línea con headers
- [ ] Delimitador consistente
- [ ] Entrecomillado correcto
- [ ] No líneas vacías al final

JSON:
- [ ] JSON válido (parseable)
- [ ] Encoding UTF-8
- [ ] Pretty print (indentado)
- [ ] Estructura consistente

SQL:
- [ ] Sintaxis SQL válida
- [ ] CREATE TABLE incluido
- [ ] INSERTS bien formados
- [ ] Escapado correcto de comillas

Excel:
- [ ] Headers en primera fila
- [ ] Tipos de datos preservados
- [ ] Formato de fechas coherente
- [ ] No excede límites (1M filas)

---

### Validación Cruzada Multi-formato

**Consistencia entre formatos:**

- Mismo número de registros en todos los formatos
- Mismos valores en todos los formatos
- Checksum MD5/SHA256 de contenido coincide
- No pérdida de precisión en conversiones

---

### Acciones Correctivas

**Si la validación falla:**
1. Revisar errores
2. Analizar si el error es sistemático o aleatorio
3. Corregir esquema según necesidad
4. Regenerar dataset solo si es necesario
5. Re-ejecutar validaciones
6. Repetir hasta alcanzar criterios de aceptación

**No debes:**
- Ignorar errores o advertencias
- Modificar datos manualmente sin regenerar
- Omitir validaciones para "ahorrar tiempo"
- Aprobar datasets con integridad referencial rota

### Ejemplo texto de disclaimer en README.md

```markdown
Aunque todos los datos han sido generados algorítmicamente sin referencia a personas reales, existe una probabilidad estadística extremadamente remota de que alguna combinación de datos (nombre, dirección, fecha de nacimiento, etc.) pueda coincidir fortuitamente con información de una persona real. Cualquier similitud es puramente casual y no intencionada. La generación sintética no implica ni garantiza la inexistencia de tales coincidencias aleatorias en el mundo real.

Exclusión de Responsabilidad

Este dataset es exclusivamente para propósitos de testing, desarrollo y formación. No debe utilizarse para tomar decisiones sobre personas reales ni para ningún propósito que requiera datos auténticos verificados.
```