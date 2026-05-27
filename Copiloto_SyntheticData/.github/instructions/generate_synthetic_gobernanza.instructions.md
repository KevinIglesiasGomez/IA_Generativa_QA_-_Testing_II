### Objetivo

Establecer directrices de gobernanza, formatos estándar y trazabilidad para datasets sintéticos, garantizando reutilización, cumplimiento normativo y trazabilidad completa.

---

### Principios de Gobernanza de Datos

**FUNDAMENTOS:**
- **Trazabilidad**: Todo dataset debe tener origen, propósito y versión claros
- **Reutilización**: Los datasets deben ser autodescriptivos y reutilizables
- **Cumplimiento**: Adherencia a GDPR, LOPD y normativas sectoriales
- **Calidad**: Metadatos completos y validaciones documentadas
- **Seguridad**: No incluir datos sensibles reales o información clasificada
- **Auditabilidad**: Historia completa de generación y cambios

---

### Formatos de Salida Estándar

**1. CSV**

Características:
- Estándar: RFC 4180
- Encoding: UTF-8
- Delimitador: ,
- Entrecomillado: dobles comillas (") cuando necesario
- Primera línea: nombres de columna
- Fecha: ISO 8601 (YYYY-MM-DD)

Uso: Intercambio universal, importación a Excel/DB
Ventajas: Simple, universal, legible
Limitaciones: No soporta tipos complejos, sin metadatos embebidos

**2. JSON**

Características:
- Estándar: ECMA-404
- Encoding: UTF-8
- Arrays para colecciones

Uso: APIs, aplicaciones web, datos jerárquicos
Ventajas: Estructuras anidadas, tipos de datos, legible
Limitaciones: Tamaño mayor que otros formatos

**3. JSON Lines (JSONL/NDJSON)**

Características:
- Un objeto JSON válido por línea
- Newline (\n) como separador
- Sin comas entre objetos

Uso: Big data, procesamiento por lotes, logs
Ventajas: Procesable línea a línea, eficiente en memoria
Limitaciones: Menos legible para humanos

**4. Parquet**

Características:
- Formato columnar binario
- Compresión eficiente (Snappy, GZIP)
- Esquema embebido
- Tipos de datos tipados

Uso: Data lakes, analytics, big data
Ventajas: Muy eficiente, comprimido, tipado fuerte
Limitaciones: Requiere librerías especializadas, no legible

**5. SQL Script**

Características:
- Sentencias INSERT en SQL estándar
- Compatible con múltiples RDBMS
- Include CREATE TABLE
- Transacciones opcionales

Uso: Población de bases de datos de prueba
Ventajas: Directo a DB, incluye esquema
Limitaciones: Específico de SQL, puede ser grande

**6. Excel (XLSX)**

Características:
- Formato Office Open XML
- Múltiples hojas (sheets)
- Tipos de datos conservados
- Metadatos en hoja separada

Uso: Reporting, análisis visual, documentación
Ventajas: Familiar para usuarios de negocio, visual
Limitaciones: Límite de filas (1M), propietario

---

### Estructura de Directorios

**Organización Estándar:**

synthetic-data/
├── README.md                          # Documentación general
├── schemas/                           # Definiciones de esquemas
│   ├── schema.json                   # Esquema principal
│   └── validation_rules.json         # Reglas de validación
├── metadata/                          # Metadatos y gobernanza
│   ├── generation_config.json        # Configuración de generación
│   ├── data_dictionary.json          # Diccionario de datos
│   └── lineage.json                  # Linaje de datos
├── datasets/                          # Datasets generados
│   ├── csv/                          # Formato CSV
│   ├── json/                         # Formato JSON
│   ├── jsonl/                        # Formato JSON Lines
│   ├── parquet/                      # Formato Parquet
│   ├── sql/                          # Scripts SQL
│   └── excel/                        # Archivos Excel
├── samples/                           # Datasets de muestra (pequeños)
│   └── sample_10_records.csv         # Primeros 10 registros
└── validation/                        # Resultados de validación
    ├── quality_report.json           # Reporte de calidad
    └── validation_errors.json        # Errores detectados


---

### Metadatos Obligatorios

**1. Archivo: metadata/generation_config.json**
```json
{
  "dataset_info": {
    "name": "users_dataset",
    "version": "1.0.0",
    "description": "Dataset sintético de usuarios para testing",
    "domain": "users",
    "purpose": "functional_testing",
    "created_date": "2026-03-06T10:30:00Z",
    "created_by": "synthetic-data-generator",
    "project": "project_name"
  },
  "generation_params": {
    "seed": 42,
    "num_records": 1000,
    "locale": "es_ES",
    "date_range": {
      "start": "2020-01-01",
      "end": "2026-03-06"
    }
  },
  "quality_metrics": {
    "completeness": 100.0,
    "validity": 99.8,
    "uniqueness": 100.0,
    "consistency": 99.5
  }
}
```

**2. Archivo: metadata/data_dictionary.json**
```json
{
  "entity": "User",
  "fields": [
    {
      "name": "user_id",
      "type": "uuid",
      "description": "Identificador único del usuario",
      "required": true,
      "unique": true,
      "primary_key": true,
      "example": "550e8400-e29b-41d4-a716-446655440000"
    },
    {
      "name": "email",
      "type": "email",
      "description": "Correo electrónico del usuario",
      "required": true,
      "unique": true,
      "business_rules": ["must_be_valid_email", "unique_per_user"],
      "example": "juan.perez@example.com"
    }
  ]
}
```

**3. Archivo: metadata/lineage.json**
```json
{
  "source": {
    "type": "synthetic_generation",
    "generator": "qa_synthetic-data-generator",
    "version": "1.0.0",
    "base_schema": "schemas/schema.json",
    "instructions": "instructions/client_specific_data.instructions.md"
  },
  "transformations": [
    {
      "step": 1,
      "operation": "generate_base_data",
      "timestamp": "2026-03-06T10:30:00Z"
    },
    {
      "step": 2,
      "operation": "apply_relationships",
      "timestamp": "2026-03-06T10:31:00Z"
    },
    {
      "step": 3,
      "operation": "validate_data_quality",
      "timestamp": "2026-03-06T10:32:00Z"
    }
  ],
  "dependencies": {
    "related_datasets": ["roles_dataset", "permissions_dataset"]
  }
}
```

---

### Nomenclatura de Archivos

**Convenciones:**

Formato: {entity}_{variant}_{date}_{version}.{extension}

Ejemplos:
- users_base_20260306_v1.csv
- orders_with_items_20260306_v1.json
- customers_large_dataset_20260306_v2.parquet

Componentes:
- entity: nombre de la entidad (singular o plural consistente)
- variant: variante opcional (base, extended, large, etc.)
- date: fecha de creación YYYYMMDD
- version: versión vN
- extension: formato de archivo

---

### Versionado de Datasets

**Esquema de Versiones:**

Semantic Versioning: MAJOR.MINOR.PATCH

- MAJOR: Cambios incompatibles en el esquema
- MINOR: Añadir campos o datos (compatible hacia atrás)
- PATCH: Correcciones de datos sin cambios de esquema

Ejemplos:
- v1.0.0 → v1.1.0: Se añaden 3 campos nuevos
- v1.1.0 → v2.0.0: Se elimina un campo o cambia tipo
- v1.0.0 → v1.0.1: Corrección de datos inválidos

---

### Cumplimiento GDPR y Privacidad

**OBLIGATORIO:**
- Todos los datos personales deben ser **ficticios**
- No usar datos reales de personas identificables
- No generar DNI/NIE/CIF reales 
- No generar IBAN o tarjetas de crédito reales
- Emails con dominios de ejemplo como example.com/test.com
- Teléfonos con prefijos 555 idenficables como ficticios

---

### Documentación README.md

**Secciones Obligatorias:**

# Dataset Sintético: [Nombre]

## Descripción
Breve descripción del propósito y contenido

## Metadatos Clave
- Versión: X.Y.Z
- Fecha de Generación: YYYY-MM-DD
- Número de Registros: N
- Formatos Disponibles: CSV, JSON, etc.

## Estructura de Datos
Tabla con campos, tipos y descripciones

## Uso
Ejemplos de cómo cargar y usar los datos

## Calidad de Datos
Métricas de calidad alcanzadas

## Restricciones y Limitaciones
Qué NO cubre este dataset

## Changelog
Historial de versiones

## Licencia
Términos de uso, disclaimer de datos sintéticos

---

### Exportación Multi-formato

**Generación Simultánea:**

Cuando se genera un dataset, preguntar al usuario si desea exportarlo en múltiples formatos (CSV, JSON, etc.) para maximizar su utilidad y compatibilidad con diferentes herramientas:
- CSV: Para uso general
- JSON: Para APIs y testing web
- JSONL: Para procesamiento batch
- SQL: Para carga en DB de pruebas
- Excel: Para revisión manual (solo si <100K registros)

Nota: Parquet solo para datasets grandes (>10K registros)

**Validación Cruzada:**

Todos los formatos deben contener exactamente los mismos datos
Ejecutar checksums MD5/SHA256 para verificar integridad

### Historial de Cambios:
- Mantener registro de todas las versiones
- Documentar qué cambió entre versiones
- Identificar responsable de cambios
- Fecha y hora de cada modificación
