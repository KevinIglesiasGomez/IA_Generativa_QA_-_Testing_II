---
agent: "Generador de Datos Sinteticos"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Sonnet 4.6"
description: "Analizar requisitos de datos y crear/validar esquema"
---

# Prompt: Step 1 - Análisis de Requisitos de Datos

## ROL COGNITIVO

Actúa como un **analista de negocio y arqueólogo de información**. Tu capacidad principal en este paso es leer documentación funcional heterogénea (manuales, especificaciones, requisitos) y extraer de ella un modelo de datos estructurado y coherente. Razona sobre las intenciones del negocio, no solo sobre los datos explícitos. Haz referencias cruzadas entre fuentes, detecta inconsistencias y solicita aclaraciones cuando la información sea ambigua o incompleta. En los flujos B y C, actúa como entrevistador experto que guía al usuario para definir su esquema con precisión.

## OBJETIVO

Definir o validar el esquema de datos completo, incluyendo entidades, campos, tipos, restricciones y relaciones según las necesidades específicas del cliente.

---

## 1. CONTEXTO

Este paso tiene cuatro flujos posibles:

**FLUJO A** DOCUMENTACION: Basar la completitud de la plantilla de instrucciones y la generación de datos **a partir de la comprensión profunda y análisis de la documentación funcional** del proyecto. Requisitos funcionales, manuales de usuario, diagramas de entidad-relación, o cualquier documentación que describa el dominio de negocio y las necesidades de datos.

**FLUJO B** INSTRUCCIONES EXISTENTES: Usuario **YA TIENE** archivo de instrucciones del cliente
- Leer y analizar el archivo existente
- Validar que contiene toda la información necesaria
- Solicitar aclaraciones o información faltante al usuario
- Extraer esquema de datos
- Pasar a Step 2

**FLUJO C** CREACIÓN INTERACTIVA: Usuario **NO TIENE** archivo de instrucciones ni documentación detallada del proyecto.
- Crear el archivo mediante conversación interactiva
- Definir esquema de datos colaborativamente
- Generar archivo de instrucciones del cliente
- Pasar a Step 2

**FLUJO D** ESCENARIOS BDD + YAML BD: Usuario proporciona un **fichero de mapeo escenarios-tablas** y un **directorio con ficheros YAML** que describen la estructura de las tablas de BD.
- Leer el fichero de escenarios-tablas para identificar qué tablas necesita cada escenario
- Leer los ficheros YAML del directorio de tablas para obtener columnas, tipos y constraints
- Cruzar la información para generar un esquema de datos alineado con los escenarios BDD
- Pasar a Step 2

---

### Determinación del flujo activo

**PRIORITARIO**: Si en el Step 0 se proporcionaron valores válidos (diferentes de "no") para `${input:escenarios_tablas_file}` Y `${input:tablas_yaml_dir}`, activar directamente el **FLUJO D**.

Si solo se proporcionó `${input:escenarios_tablas_file}` sin YAMLs, activar FLUJO D en modo parcial (sin columnas detalladas).

En cualquier otro caso, seguir el orden: FLUJO B → FLUJO A → FLUJO C.

---

## 2. FLUJO A - Análisis de Documentación Funcional
### 2.1 Análisis de Documentación

Antes de proceder con cualquier análisis, debes:
 
1. **Leer TODA la documentación funcional disponible** en el directorio `documentation` - Esta es la fuente principal para generación de datos funcionales. Debes extraer toda la información relevante sobre entidades, campos, tipos de datos, relaciones y reglas de negocio. Esta documentación describe el dominio de negocio y las necesidades de datos para pruebas funcionales.
2. **Leer la documentación técnica disponible** en el directorio `documentation` (si existe en el proyecto) - **SOLO COMO CONTEXTO**: La documentación técnica proporciona comprensión del sistema pero NO debe usarse para generar datos. Los casos funcionales deben derivarse únicamente de la documentación funcional/negocio.
3. **Revisar el json con la API** si está disponible en el workspace - 
4. **Hacer referencias cruzadas de información** entre diferentes documentos funcionales para asegurar una comprensión completa

### 2.2. Identificación de Tipo de Documento

Después de completar la revisión completa de documentación, analiza el contenido de los documentos ubicados en `documentation`

Basado en su estructura, contenido e idioma, determina el tipo de documento más apropiado entre los siguientes:

- `user_manual`
- `business_requirements`
- `functional_specification`
- `technical_specification`
- `test_plan`
- `process_documentation`
- `system_manual`
- `tutorial`
- _(o sugiere una nueva etiqueta más apropiada si es necesario)_

Establece este valor como `${input:document_type}`.

## 3. FLUJO B - Análisis de Archivo Existente

### 3.1 Validación de Contenido

El archivo DEBE contener mínimamente:

**Información Obligatoria:**
- [ ] Descripción del dominio de negocio
- [ ] Lista de entidades/tablas a generar
- [ ] Definición de campos por entidad
- [ ] Tipos de datos por campo
- [ ] Campos requeridos vs opcionales
- [ ] Campos únicos (PK, unique constraints)
- [ ] Restricciones (min/max, patterns, valores permitidos)
- [ ] Relaciones entre entidades (FK, cardinalidad)
- [ ] Reglas de negocio específicas

### 3.2 Análisis y Extracción

Extraer del archivo:
1. Lista de entidades
2. Esquema completo de cada entidad
3. Relaciones e integridad referencial
4. Reglas de validación específicas
5. Casos especiales o excepciones

### 3.3 Confirmación con Usuario

Presentar resumen y solicitar confirmación:

```markdown
## Análisis del Archivo de Instrucciones

### Entidades Identificadas:
1. [Entidad 1] - [N campos] - [Descripción]
2. [Entidad 2] - [N campos] - [Descripción]
...

### Relaciones:
- [Entidad1] → [Entidad2] (1:N) via [campo_fk]
...

### Casos Especiales:
- [Regla 1]
- [Regla 2]
...

¿Es correcto este análisis? ¿Falta algo por incluir? (s/n)
```

---

## 4. FLUJO C - Creación Interactiva del Esquema

### 4.1 Introducción

**Mensaje al usuario:**
```No se ha proporcionado un archivo de instrucciones del cliente.
Vamos a crear el esquema de datos juntos mediante una conversación guiada.

```

### 4.2 Definición de Entidades

**Pregunta al usuario:**
```
Paso 1: Definir Entidades

¿Qué entidades (tablas/objetos) necesita tu dataset?

Ejemplos según dominio:
- E-commerce: productos, clientes, pedidos, pagos
- Banca: clientes, cuentas, transacciones, tarjetas
- Salud: pacientes, citas, diagnósticos, tratamientos
- Educación: estudiantes, cursos, matriculas, calificaciones

Por favor, lista las entidades principales necesarias (separadas por comas):
${input:entities}

¿Cuál es la entidad principal o más importante? (primera que se debe generar)
${input:main_entity}
```

### 4.3 Definición de Campos por Entidad

**Para cada entidad, preguntar:**

```
Entidad: ${entity_name}

Vamos a definir los campos de ${entity_name}.

Te preguntaré por cada campo:
1. Nombre del campo
2. Tipo de dato
3. Si es obligatorio (required)
4. Si es único (unique)
5. Restricciones (min/max, pattern, etc.)
6. Descripción

¿Cuántos campos tiene ${entity_name}? (aproximadamente)
${input:num_fields}

Comenzamos:

--- Campo 1 ---
Nombre del campo: ${input:field_name}

Tipo de dato (elige uno):
1. string - Texto
2. integer - Número entero
3. float/decimal - Número decimal
4. boolean - Verdadero/Falso
5. date - Fecha
6. datetime - Fecha y hora
7. uuid - Identificador único
8. email - Email
9. phone - Teléfono
10. url - URL
11. Otro (especificar)

Tipo: ${input:field_type}

¿Es obligatorio este campo? (s/n): ${input:is_required}

¿Es único (no puede haber duplicados)? (s/n): ${input:is_unique}

¿Es la clave primaria (primary key)? (s/n): ${input:is_primary_key}

Restricciones adicionales:
- Para strings: ¿longitud mínima/máxima? ${input:min_length} / ${input:max_length}
- Para números: ¿valor mínimo/máximo? ${input:min_value} / ${input:max_value}
- Para strings: ¿patrón/formato específico? ${input:pattern}
- ¿Valores permitidos (enum)? ${input:allowed_values}

Descripción breve del campo: ${input:field_description}

¿Alguna instrucción especial para generar este campo?
Ejemplo: "Debe ser un email corporativo", "Fechas solo de lunes a viernes", etc.
${input:special_instructions}
```
**Importante**: Repetir para cada campo de la entidad.

### 4.4 Definición de Relaciones

**Después de definir todas las entidades:**

```
Ahora definamos las relaciones entre entidades:

¿Existe relación entre [Entidad A] y [Entidad B]?

Tipo de relación:
1. Uno a Uno (1:1) - Un A tiene un B
2. Uno a Muchos (1:N) - Un A tiene muchos B
3. Muchos a Muchos (N:M) - Muchos A tienen muchos B

Campo de foreign key: ${input:fk_field}
Referencia a: ${input:referenced_entity}.${input:referenced_field}

¿Todas las referencias deben ser válidas? (s/n - integridad referencial)
${input:enforce_integrity}
```

### 4.5 Reglas de Negocio Específicas

```
¿Hay reglas de negocio específicas que debamos considerar?

Ejemplos:
- "La fecha de fin debe ser posterior a la fecha de inicio"
- "El total debe ser igual a subtotal + IVA"
- "Si el estado es 'ENVIADO', debe existir fecha_envio"
- "El email debe ser del dominio de la empresa"

Lista de reglas (separadas por punto y coma):
${input:business_rules}
```

### 4.6 Casos Especiales y Excepciones

```
¿Hay casos especiales que debamos generar?

Ejemplos:
- Registros con valores en el límite (edad=18, edad=100)
- Registros con campos opcionales vacíos
- Registros con estados específicos
- Porcentaje de registros con ciertas características

Describe los casos especiales necesarios:
${input:special_cases}
```

---

## 5. FLUJO D - Escenarios BDD + Esquema YAML de BD

Este flujo se activa cuando el usuario proporcionó en el Step 0:
- `${input:escenarios_tablas_file}` — ruta al fichero de mapeo escenarios → tablas
- `${input:tablas_yaml_dir}` — ruta al directorio con los ficheros YAML de estructura de tablas

### 5.1 Lectura del Fichero de Escenarios-Tablas

Lee el fichero `${input:escenarios_tablas_file}`. Este fichero tiene formato Markdown con secciones por `.feature` y subsecciones por escenario (`@tag`). Cada subsección contiene:
- La lista de tablas necesarias para ese escenario (entre backticks o en tabla Markdown)
- Una tabla de motivos (por qué se necesita cada tabla)

**Extracción requerida:**
1. Para cada feature identificada, extraer la lista de etiquetas de escenario (`@tag`)
2. Para cada etiqueta, extraer el conjunto de tablas necesarias (unión de todas las mencionadas)
3. Construir un **mapa escenario → tablas** en formato:
   ```
   @tag-escenario: [TABLA1, TABLA2, TABLA3, ...]
   ```
4. Construir también una **lista global de tablas únicas** (unión de todas las tablas de todos los escenarios)

**Pregunta al usuario:**
```
He leído el fichero de mapeo escenarios-tablas.

He identificado los siguientes features y escenarios:
[Listar features con sus escenarios y tablas]

¿Deseas generar datos para TODOS los escenarios o para un subconjunto?
1. Todos los escenarios
2. Solo un feature específico (indicar cuál)
3. Solo escenarios con una etiqueta específica (indicar cuál)

${input:escenarios_seleccionados}
```

### 5.2 Lectura de los Ficheros YAML de Tablas

Lee todos los ficheros `.yaml` del directorio `${input:tablas_yaml_dir}`.

Cada fichero YAML tiene la siguiente estructura (puede variar según la convención del proyecto):
```yaml
dominio: <nombre_dominio>       # Opcional: agrupación lógica de tablas
tablas:
  NOMBRE_TABLA:
    pk: CAMPO_PK
    columnas:
      - nombre: CAMPO_NOMBRE
        tipo: <tipo_nativo_del_motor>   # Ej: VARCHAR, INTEGER, DATE, BOOLEAN...
        size: <numero>                  # Opcional: longitud máxima
        nullable: true|false
    relaciones:  # Opcional
      - campo: CAMPO_FK
        tabla_ref: TABLA_REFERENCIADA
        campo_ref: CAMPO_PK_REF
```

> **NOTA**: El formato exacto puede variar. Si el fichero tiene una estructura diferente (ej: JSON Schema, Liquibase, Flyway, OpenAPI, etc.), adaptá la lectura a la estructura real del fichero proporcionado.

**Extracción requerida:**
Para cada tabla presente en la lista global del paso 5.1:
1. Localizar el fichero YAML que la contiene (buscar en todos los ficheros del directorio)
2. Extraer:
   - Nombre de la tabla
   - Campo PK
   - Todos los campos (nombre, tipo, size, nullable)
   - Relaciones FK si las hay
3. Si una tabla no está en ningún YAML (ej: tablas de sistemas externos, de identidad o de auditoría que el proyecto no documenta en los YAMLs), anotarla como "tabla externa / no documentada" y no incluirla en el esquema generado, pero mencionarla al usuario

### 5.3 Mapeo de Tipos Nativos a Tipos del Generador

Analiza los tipos de datos presentes en los ficheros YAML e infiere la estrategia de generación. La tabla siguiente muestra ejemplos comunes, pero **debe adaptarse a los tipos reales encontrados en los ficheros del proyecto**:

| Tipo nativo (ejemplos) | Tipo generador | Estrategia de generación |
|------------------------|---------------|---------------------------|
| INT, INTEGER, NUMBER (PK) | integer | Secuencia incremental |
| INT, NUMBER (FK) | integer | Referencia a PK de tabla relacionada |
| INT, NUMBER, BIGINT | integer | Random en rango según tamaño |
| VARCHAR, VARCHAR2, TEXT, STRING | string | Random alfanumérico, respetando max length |
| CHAR | string | Random de longitud fija |
| DATE | date | Fecha aleatoria en rango configurado |
| DATETIME, TIMESTAMP | datetime | Fecha y hora aleatoria |
| BOOLEAN, BIT | boolean | Random true/false |
| DECIMAL, FLOAT, NUMERIC | float | Random decimal en rango |
| CLOB, BLOB, TEXT largo | string | Texto largo aleatorio |

Si el proyecto usa tipos personalizados o enums, inferir los valores posibles del contexto del fichero.

### 5.4 Selección de Tablas por Escenario

A partir de los escenarios seleccionados en 5.1 y los campos extraídos en 5.2:

**Pregunta al usuario:**
```
He cruzado los escenarios con la estructura de las tablas.

Tablas encontradas en los YAML: [N tablas]
Tablas referenciadas en escenarios pero NO en YAML (externas): [lista]

Para los datos sintéticos, ¿qué volumen necesitas por tabla?
- Opción A: El mismo número de registros para todas las tablas (${input:num_records} registros)
- Opción B: Volumen proporcional (tablas maestras = 20-50 registros, tablas transaccionales = ${input:num_records})
- Opción C: Indicar manualmente el volumen por tabla

${input:volume_strategy}
```

### 5.5 Generación del Esquema desde YAML

Con la información recopilada, construir el esquema de datos en el formato estándar del agente:

Para **cada tabla** seleccionada:

```markdown
### [NOMBRE_TABLA]

> Dominio: [nombre_dominio del YAML o "sin dominio"] | Feature(s): [features que la usan]
> Escenarios que la requieren: @tag1, @tag2, ...

**Campos:**

| Campo | Tipo nativo | Tipo generador | Req | PK | FK | Restricciones |
|-------|------------|---------------|-----|----|----|---------------|
| id_campo | INTEGER | integer | ✓ | ✓ | - | Secuencial |
| id_referencia | INTEGER | integer | ✓ | - | OTRA_TABLA.id | - |
| campo_texto | VARCHAR(100) | string | [nullable] | - | - | max=100 |
| campo_fecha | DATE | date | [nullable] | - | - | rango configurable |

**Relaciones detectadas:**
- [CAMPO_FK] → [TABLA_REFERENCIADA].[CAMPO_PK_REF]

**Notas de generación:**
- [Observaciones extraídas del fichero de escenarios-tablas o del YAML]
```

### 5.6 Confirmación del Esquema con el Usuario

Presentar el esquema completo al usuario:

```markdown
## Esquema Extraído desde Escenarios BDD + YAML de BD

### Tablas incluidas en el dataset: [N tablas]
[Lista de tablas con nº de campos y dominio]

### Tablas externas (no generadas): [N tablas]
[Tablas referenciadas en los escenarios pero no encontradas en los YAMLs del proyecto]

### Mapa de escenarios → tablas generadas:
| Escenario | Tablas del dataset |
|-----------|-------------------|
| @tag1 | TABLA_A, TABLA_B |
| @tag2 | TABLA_A, TABLA_C |
...

### Relaciones detectadas entre tablas: [N relaciones]
[Lista de FK detectados]

¿Es correcto este esquema? ¿Hay alguna tabla que excluir o algún campo que ajustar? (s/n)
```

### 5.7 Generación del Fichero de Instrucciones desde YAML

Una vez confirmado el esquema, generar el fichero de instrucciones del cliente usando la información extraída de los YAML:

**Ruta:** `${input:output_directory}/instructions/bdd_schema.instructions.md`

Este fichero debe incluir:
1. Cabecera con metadatos (proyecto, dominio, fuentes usadas, fecha)
2. Mapa de escenarios → tablas (para trazabilidad)
3. Definición completa de cada tabla con todos sus campos (usando la plantilla `generate_synthetic_data_template.instructions.md`)
4. Mapa de relaciones entre tablas
5. Notas sobre tablas externas no generadas (si las hubiera)

---

## 6. GENERACIÓN DEL ARCHIVO DE INSTRUCCIONES

Una vez recopilada toda la información (Flujo A, B, C o D), generar el archivo:

**Ruta:** `${input:output_directory}/instructions/client_specific_data.instructions.md`

**Contenido:**

Utilizar la plantilla de instrucciones del cliente (data_template.instructions.md) para estructurar el archivo, llenando cada sección con la información recopilada.

---

## 7. GENERACIÓN DEL ESQUEMA JSON

Paralelamente, generar el esquema formal en JSON:

**Ruta:** `${input:output_directory}/schemas/schema.json`

```json
{
  "schema_version": "1.0.0",
  "entities": [
    {
      "name": "${entity_name}",
      "description": "${entity_description}",
      "fields": [
        {
          "name": "${field_name}",
          "type": "${field_type}",
          "description": "${field_description}",
          "required": true,
          "unique": false,
          "primary_key": false,
          "foreign_key": {
            "entity": "${referenced_entity}",
            "field": "${referenced_field}"
          },
          "constraints": {
            "min_length": 3,
            "max_length": 50,
            "min_value": 0,
            "max_value": 100,
            "pattern": "^[A-Z]{3}-[0-9]{4}$",
            "values": ["value1", "value2"]
          },
          "generation_strategy": "pattern|random|dictionary|rule",
          "special_instructions": "${special_instructions}",
          "example": "${example_value}"
        }
      ],
      "business_rules": [
        {
          "rule": "${rule_name}",
          "description": "${rule_description}",
          "logic": "${rule_logic}"
        }
      ]
    }
  ],
  "relationships": [
    {
      "from_entity": "${entity_a}",
      "to_entity": "${entity_b}",
      "type": "one_to_many",
      "foreign_key": "${fk_field}",
      "referenced_field": "${pk_field}",
      "enforce_integrity": true
    }
  ]
}
```

---

## 8. VALIDACIÓN DEL ESQUEMA

Validar que el esquema cumple con requisitos mínimos:

- Cada entidad tiene al menos un campo PK
- Los FK referencian entidades existentes
- Campos requeridos no son nullable
- Campos únicos tienen estrategia apropiada
- Las reglas de negocio son coherentes
- No hay contradicciones entre campos o relaciones  

---

## 9. RESULTADO DEL PASO

Al finalizar este paso, debes tener:

1. Archivo de instrucciones del cliente creado/validado (o `bdd_schema.instructions.md` si se usó FLUJO D)
2. Esquema JSON formal generado
3. Validación del esquema completada
4. Confirmación del usuario

**Mensaje al usuario:**
```
Esquema de datos definido correctamente.

Archivos generados:
- ${input:output_directory}/instructions/client_specific_data.instructions.md
- ${input:output_directory}/schemas/schema.json

Resumen:
- Entidades: ${num_entities}
- Total de campos: ${num_fields}
- Relaciones: ${num_relationships}
- Reglas de negocio: ${num_rules}

Siguiente paso: Procederemos a Step 2 para definir estrategias de generación

¿Continuamos? (s/n)
```

---

## 10. MEJORES PRÁCTICAS

**Creación Interactiva:**
- Ser paciente y guiar al usuario
- Ofrecer ejemplos específicos del dominio
- Proporcionar valores por defecto razonables
- Permitir correcciones y refinamientos
- Confirmar información crítica
- No permitir que el usuario se salga del contexto

**Documentación:**
- Ser exhaustivo pero claro
- Incluir ejemplos en cada campo
- Documentar motivo de cada regla
- Mantener consistencia en nomenclatura

**Validación:**
- Verificar coherencia entre entidades
- Detectar posibles problemas de integridad
- Sugerir mejoras cuando sea apropiado
- Alertar sobre complejidades innecesarias
