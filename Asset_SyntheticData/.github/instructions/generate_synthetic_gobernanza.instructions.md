<!--
SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
SPDX-License-Identifier: GPL-3.0-only
-->

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

| Formato | Contrato mínimo | Uso principal |
|---------|-----------------|---------------|
| CSV | RFC 4180, UTF-8, cabecera, fechas ISO 8601 | Intercambio y Excel/DB |
| JSON | ECMA-404, UTF-8, array por colección | APIs y datos jerárquicos |
| JSONL | Un objeto JSON por línea | Lotes y grandes volúmenes |
| Parquet | Columnar, esquema embebido, compresión | Analítica y data lakes |
| SQL | `CREATE TABLE` e `INSERT`, transacción opcional | Carga en RDBMS |
| XLSX | Hojas por entidad y metadatos separados; máximo práctico 100K registros | Revisión manual |

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

| Archivo | Contenido obligatorio |
|---------|-----------------------|
| `metadata/generation_config.json` | Identidad, versión, propósito, proyecto, fecha UTC; seed, volumen, locale, rango, distribución y formatos; métricas de calidad |
| `metadata/data_dictionary.json` | Por entidad y campo: nombre, tipo, descripción, obligatoriedad, unicidad, PK/FK, restricciones, reglas y ejemplo |
| `metadata/lineage.json` | Generador y versión, esquema e instrucciones de origen, transformaciones con fecha UTC y dependencias |

Los tres archivos deben ser JSON válido y usar `instructions/client_specific_data.instructions.md` como ruta de instrucciones generadas.

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

Generar el README según `generate_synthetic_readme.instructions.md`, fuente única para sus secciones y contenido.

---

### Exportación Multi-formato

Generar solo los formatos confirmados por el usuario. Recomendar Parquet para más de 10K registros y XLSX solo por debajo de 100K.

**Validación Cruzada:**

Todos los formatos deben contener exactamente los mismos datos
Ejecutar checksums MD5/SHA256 para verificar integridad

### Historial de Cambios:
- Mantener registro de todas las versiones
- Documentar qué cambió entre versiones
- Identificar responsable de cambios
- Fecha y hora de cada modificación
