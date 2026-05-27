# Copiloto de Generación de Datos Sintéticos

## Descripción

Este copiloto de GitHub Copilot genera datos sintéticos de alta calidad para pruebas de software. Es completamente independiente de la aplicación y adaptable a cualquier dominio de negocio.

## Características Principales

- **Análisis de documentación funcional**: Lee y analiza automáticamente documentación del proyecto (FLUJO A)
- **Independiente de aplicación y datos**: Configurable para cualquier dominio
- **3 flujos de trabajo**: Documentación funcional, archivo de instrucciones, o creación interactiva
- **Interactivo y guiado**: Conversación paso a paso con validaciones y confirmaciones
- **Alta calidad**: Validaciones exhaustivas en 6 dimensiones de calidad
- **Múltiples formatos**: CSV, JSON, JSONL, SQL, Excel, Parquet
- **Gobernanza completa**: Metadatos, linaje, trazabilidad y documentación automática
- **Cumplimiento GDPR**: Datos completamente ficticios y seguros
- **Reproducible**: Uso de semillas para generación determinística
- **Plantilla para clientes**: Plantilla de datos cliente reducida en ~40% para facilitar su uso
- **Documentación automática**: Generación de README completo para cada dataset usando template específico

---

## Arquitectura del Copiloto

```
.github/
├── agents/
│   └── generate_synthetic.agent.md                              # Agente principal (modo "Generador de Datos Sinteticos")
├── instructions/
│   ├── generate_synthetic_estandares_buenas_practicas.instructions.md  # Estándares de calidad y tipos
│   ├── generate_synthetic_gobernanza.instructions.md                   # Gobernanza, formatos y trazabilidad
│   ├── generate_synthetic_calidad_verificacion.instructions.md         # Validaciones y dimensiones de calidad
│   └── generate_synthetic_readme.instructions.md                       # Template para README de datasets
├── prompts/
│   ├── generate_synthetic_data_step0.prompt.md  # Configuración y contexto
│   ├── generate_synthetic_data_step1.prompt.md  # Análisis de requisitos (3 flujos)
│   ├── generate_synthetic_data_step2.prompt.md  # Definición del esquema y estrategias
│   ├── generate_synthetic_data_step3.prompt.md  # Generación de datos sintéticos
│   └── generate_synthetic_data_step4.prompt.md  # Validación y documentación
├── scripts/
│   ├── generate_synthetic_data_generador.example.py  # Ejemplo de generador Python (596 líneas)
│   └── generate_synthetic_data_validador.example.py  # Ejemplo de validador Python (349 líneas)
└── templates/
    ├── generate_synthetic_data_template.instructions.md  # Plantilla de instrucciones para clientes
    └── diccionarios/                                     # Diccionarios de datos predefinidos
        ├── nombres_es.json
        ├── apellidos_es.json
        ├── calles_es.json
        ├── ciudades_provincias_es.json
        ├── descripciones_seguros.json
        └── accidentes.json
```

### Roles Cognitivos por Step

Cada prompt activa un perfil cognitivo específico adaptado a la naturaleza de la tarea:

| Step | Rol cognitivo | Capacidad principal |
|------|--------------|---------------------|
| Step 0 | Consultor especialista en datos | Escucha activa, orientación al cliente, captura de requisitos |
| Step 1 | Analista de negocio / arqueólogo de información | Lectura cruzada de documentación, inferencia de modelos de datos |
| Step 2 | Arquitecto de datos | Diseño sistémico, optimización de estrategias, modelado de dependencias |
| Step 3 | Ingeniero de datos | Ejecución fiable, procesamiento por lotes, exportación multi-formato |
| Step 4 | Auditor de calidad de datos | Certificación de calidad, diagnóstico de problemas, documentación final |

El agente mantiene como identidad base el perfil de **Data Quality Engineer**, y cada prompt refina ese rol para el contexto concreto de cada fase.

### Control de Deuda Cognitiva y Sesgos

El agente principal supervisa activamente los riesgos de sesgo que introduce cada rol especializado:

| Step | Riesgo de sesgo | Control aplicado |
|------|----------------|------------------|
| Step 0 | Complacencia: aceptar requisitos vagos | Validar precisión antes de avanzar |
| Step 1 | Interpretación: añadir supuestos no documentados | Distinguir hechos de inferencias y confirmar estas últimas |
| Step 2 | Sobreingeniería: complejidad innecesaria | Justificar cada decisión en un requisito concreto |
| Step 3 | Ejecución ciega: implementar sin verificar | Revisar consistencia del esquema antes de generar |
| Step 4 | Confirmación: buscar éxito en lugar de fallos | Postura crítica activa orientada a detectar problemas |

En cada transición de step, el agente verifica: ausencia de deuda cognitiva acumulada (ambigüedades sin resolver), consistencia de la información con steps anteriores, y puntos ciegos que el nuevo rol puede detectar respecto al anterior.

---

### Archivos de Instrucciones

El copiloto utiliza 4 archivos de instrucciones en `.github/instructions/`:

1. **generate_synthetic_estandares_buenas_practicas.instructions.md** (210 líneas)
   - Tipos de datos soportados (primitivos, especializados, compuestos)
   - Estrategias de generación (aleatoria, plantillas, diccionarios, reglas)
   - Distribución de datos (60% válidos normales, 20% límite, 20% excepcionales/negativos)
   - Validaciones obligatorias pre y post-generación

2. **generate_synthetic_gobernanza.instructions.md** (325 líneas)
   - Formatos de salida estándar (CSV, JSON, JSONL, Parquet, SQL, Excel)
   - Principios de trazabilidad y reutilización
   - Estructura de metadatos y linaje
   - Cumplimiento normativo (GDPR, LOPD)

3. **generate_synthetic_calidad_verificacion.instructions.md** (309 líneas)
   - 6 dimensiones de calidad con umbrales específicos
   - Métricas y validaciones por dimensión
   - Sistema de scoring global
   - Criterios de aprobación/rechazo

4. **generate_synthetic_readme.instructions.md** (83 líneas)
   - Template para generar README de datasets
   - Estructura con métricas de calidad
   - Información de privacidad y cumplimiento
   - Ejemplos de uso y configuración

### Plantilla para Clientes

En `.github/templates/` se encuentra la plantilla que los clientes completan para definir su esquema:

- **generate_synthetic_data_template.instructions.md** (144 líneas)
   - 8 secciones: información básica, descripción del dominio, entidades y campos, mapa de relaciones, validaciones críticas, distribución de datos, requisitos especiales y configuración
   - Campos obligatorios marcados con `*`
   - Formato tabla compacto para definición de campos
   - Quick reference de tipos de datos y restricciones comunes

### Diccionarios Predefinidos

En `.github/templates/diccionarios/` hay 6 diccionarios en español listos para usar:

| Archivo | Dominio |
|---------|---------|
| `nombres_es.json` | Nombres de persona en español |
| `apellidos_es.json` | Apellidos en español |
| `calles_es.json` | Nombres de calles españolas |
| `ciudades_provincias_es.json` | Ciudades y provincias de España |
| `descripciones_seguros.json` | Descripciones del sector seguros |
| `accidentes.json` | Tipos de accidentes y siniestros |

El copiloto prioriza estos diccionarios cuando el dominio del cliente es compatible. Para otros dominios genera nuevos diccionarios usando la librería Faker.

### Scripts de Ejemplo

En `.github/scripts/` hay dos scripts Python de referencia:

- **generate_synthetic_data_generador.example.py** (596 líneas): Implementación de referencia para generación masiva de datos con todas las estrategias soportadas, exportación a múltiples formatos y gestión de semillas.
- **generate_synthetic_data_validador.example.py** (349 líneas): Implementación de referencia para validación de las 6 dimensiones de calidad y generación de reportes.

---

## Flujo de Trabajo

### Step 0: Configuración y Contexto
- Recopila información del proyecto
- Establece parámetros de generación
- Crea estructura de directorios
- Configura formatos de salida

### Step 1: Análisis de Requisitos
El copiloto soporta **3 flujos diferentes** según tu punto de partida:

- **FLUJO A**: **Análisis de documentación funcional** - Lee y analiza automáticamente la documentación funcional del proyecto (manuales de usuario, requisitos, especificaciones) del directorio `documentation/` para extraer entidades, campos y reglas de negocio
- **FLUJO B**: **Con archivo de instrucciones existente** - Analiza archivo de instrucciones del cliente previamente definido y solicita aclaraciones si falta información
- **FLUJO C**: **Creación interactiva desde cero** - Crea esquema mediante conversación guiada paso a paso cuando no hay documentación ni archivo de instrucciones

En todos los flujos se definen entidades, campos, tipos de datos, restricciones, relaciones y reglas de negocio específicas

### Step 2: Definición del Esquema y Estrategias de Generación
- Asigna estrategias de generación óptimas por campo (UUID, Faker, Dictionary, Pattern, etc.)
- **Prioriza diccionarios existentes del workspace** (`templates/diccionarios/`) si cumplen con el dominio
- Genera nuevos diccionarios con Faker solo si es necesario
- Determina orden de generación por dependencias (análisis de grafo)
- Configura distribuciones de escenarios (normal/límite/excepcional)
- Genera esquema JSON formal con estrategias

### Step 3: Generación de Datos
- Ejecuta generación masiva de datos en lotes
- Aplica todas las estrategias definidas por campo
- Mantiene integridad referencial entre entidades
- Exporta simultáneamente a múltiples formatos (CSV, JSON, SQL, etc.)
- Genera muestras de 10 registros por entidad

### Step 4: Validación y Documentación
- Ejecuta validaciones exhaustivas en 6 dimensiones de calidad
- Genera reportes detallados de calidad con métricas
- **Genera automáticamente README.md** del dataset usando template formal definido en `readme.instructions.md`
- Actualiza metadatos con métricas finales y linaje completo

---

## Cómo Usar el Copiloto

El copiloto soporta **3 flujos de trabajo** diferentes según tu punto de partida:

---

### FLUJO A: Con Documentación Funcional del Proyecto

**Caso de uso**: Tienes documentación funcional (manuales, requisitos, especificaciones) pero no un archivo de instrucciones estructurado

1. **Organiza tu documentación** en un directorio `documentation/` en tu workspace:
   - Manuales de usuario
   - Requisitos funcionales
   - Especificaciones funcionales
   - Diagramas de entidad-relación
   - Cualquier documento que describa el dominio de negocio

2. **Invoca el agente** desde Copilot Chat:
   - Abre Copilot Chat en VS Code
   - Selecciona el modo **"Generador de Datos Sinteticos"** en el selector de agente
   - Escribe como primer mensaje:
   ```
   Tengo documentación funcional en el directorio documentation/
   ```

3. **El agente automáticamente**:
   - Lee **toda la documentación funcional** disponible
   - Hace **referencias cruzadas** entre documentos
   - Identifica el **tipo de documento** (manual, especificación, etc.)
   - Extrae entidades, campos, tipos y reglas de negocio
   - **Solicita aclaraciones** si falta información crítica
   - Genera el archivo de instrucciones estructurado
   - Procede con la generación de datos

4. **Ventajas**:
   - Aprovecha documentación existente sin reescribir
   - Análisis inteligente de múltiples fuentes
   - Reduce tiempo de configuración manual
   - Mantiene trazabilidad con documentación original
---

### FLUJO B: Con Archivo de Instrucciones del Cliente Existente

**Caso de uso**: Ya tienes un archivo de instrucciones estructurado o quieres regenerar datos

1. **Prepara tu archivo de instrucciones** usando la plantilla disponible en:
   ```
   .github/templates/generate_synthetic_data_template.instructions.md
   ```
   La plantilla está optimizada (~40% más corta) con 8 secciones bien definidas para facilitar su uso.

2. **Invoca el agente** desde Copilot Chat:
   - Abre Copilot Chat en VS Code
   - Selecciona el modo **"Generador de Datos Sinteticos"** en el selector de agente
   - Escribe como primer mensaje:
   ```
   Archivo de instrucciones: ./config/my_client_data.instructions.md
   ```

3. **El agente**:
   - Analiza el archivo de instrucciones
   - Valida completitud de la información
   - **Solicita aclaraciones** si falta información crítica
   - Confirma el análisis contigo antes de proceder
   - Genera los datos según especificaciones
   - Ejecuta validaciones de calidad automáticas
   - Crea documentación README completa del dataset

---

### FLUJO C: Creación Interactiva desde Cero

**Caso de uso**: Primera vez generando datos, sin documentación ni archivo de instrucciones

1. **Abre el agente** en GitHub Copilot Chat:
   - Abre Copilot Chat en VS Code
   - Selecciona el modo **"Generador de Datos Sinteticos"** en el selector de agente

2. **El agente te guiará interactivamente** preguntando:
   - Nombre del proyecto y dominio de negocio
   - Propósito de los datos (testing, demo, desarrollo)
   - Cantidad de registros necesarios
   - Locale e idioma preferido
   - Formatos de salida deseados (CSV, JSON, SQL, etc.)
   - Directorio de salida
   - Configuración avanzada (opcional): seed, distribuciones, rango de fechas

3. **Definirás el esquema colaborativamente** campo por campo:
   - Entidades necesarias y su prioridad
   - Campos de cada entidad con tipos específicos
   - Restricciones detalladas (min/max, patterns, enums)
   - Si cada campo es requerido, único o primary key
   - Relaciones y foreign keys entre entidades
   - Reglas de negocio específicas del dominio

4. **El agente generará automáticamente**:
   - Archivo de instrucciones del cliente (estructurado)
   - Esquema JSON formal con estrategias de generación
   - Diccionarios de datos necesarios
   - Datos en todos los formatos solicitados
   - Validaciones exhaustivas con reportes
   - README completo del dataset generado
   - Metadatos de linaje y trazabilidad

---

## Estructura de Salida

```
output_directory/
├── README.md                          # Documentación completa del dataset generado y especificaciones de cliente
├── schemas/
│   ├── schema.json                   # Esquema formal con estrategias de generación
│   └── validation_rules.json         # Reglas de validación definidas
├── metadata/
│   ├── generation_config.json        # Configuración completa de generación
│   ├── data_dictionary.json          # Diccionario de datos por entidad
│   ├── lineage.json                  # Linaje y trazabilidad del dataset
│   └── dictionaries/                 # Diccionarios utilizados en generación
│       ├── first_names.json
│       ├── last_names.json
│       └── ...
├── datasets/
│   ├── csv/                          # Formato CSV (RFC 4180, UTF-8)
│   ├── json/                         # Formato JSON (pretty print)
│   ├── jsonl/                        # Formato JSON Lines (streaming)
│   ├── sql/                          # Scripts SQL INSERT + CREATE TABLE
│   ├── excel/                        # Archivos Excel XLSX (si <100K registros)
│   └── parquet/                      # Formato Parquet (si >10K registros)
├── samples/                           # Muestras de 10 registros por entidad
│   ├── entity1_sample_10.csv
│   └── entity2_sample_10.csv
└── validation/
    ├── quality_report.json           # Reporte completo de calidad (6 dimensiones)
    └── validation_errors.json        # Errores identificados (si los hay)
```

---

## Dimensiones de Calidad

El copiloto valida automáticamente 6 dimensiones de calidad:

| Dimensión | Qué Valida | Umbral |
|-----------|------------|--------|
| **Completitud** | Campos requeridos llenos | ≥99% |
| **Validez** | Tipos y formatos correctos | ≥99% |
| **Unicidad** | PKs y campos unique sin duplicados | 100% |
| **Consistencia** | Coherencia entre campos | ≥95% |
| **Integridad Referencial** | FKs válidos | 100% |
| **Exactitud** | Realismo y lógica de negocio | Cualitativa |

**Quality Score Global**: Promedio de todas las dimensiones

- **≥98%**: Dataset APROBADO
- **95-98%**: Dataset APROBADO con advertencias
- **<95%**: Dataset RECHAZADO - requiere corrección

---

## Estrategias de Generación

El copiloto soporta 10 estrategias de generación:

1. **UUID**: Identificadores únicos universales
2. **SEQUENTIAL**: Secuencias autoincrementales
3. **FAKER**: Datos realistas mediante librería Faker
4. **DICTIONARY**: Valores desde diccionarios curados
5. **PATTERN**: Basado en plantillas (ej: PROD-{year}-{number})
6. **ENUM**: Listas cerradas de valores
7. **DATE_RANGE**: Fechas en rango con distribución
8. **RANDOM**: Valores aleatorios controlados
9. **RELATED**: Foreign keys a entidades relacionadas
10. **CALCULATED**: Valores derivados de otros campos

---

## Formatos de Salida

### CSV
- **Uso**: Universal, Excel, pandas
- **Encoding**: UTF-8 con BOM
- **Estándar**: RFC 4180

### JSON
- **Uso**: APIs, web apps
- **Pretty print**: Sí (indentado)
- **Arrays**: Para colecciones

### JSON Lines
- **Uso**: Big data, batch processing
- **Stream-friendly**: Sí
- **Un objeto por línea**: Sí

### SQL
- **Uso**: Carga directa en DB
- **Incluye**: CREATE TABLE + INSERTs
- **Compatible**: MySQL, PostgreSQL, etc.

### Excel
- **Uso**: Revisión manual, reports
- **Límite**: <100K registros
- **Múltiples hojas**: Sí

### Parquet
- **Uso**: Data lakes, analytics
- **Compresión**: Snappy
- **Columnar**: Sí

---

## Ejemplos de Uso

### Ejemplo 1: E-commerce (FLUJO A - Con Documentación)

```
Documentación: Manual de usuario + Especificaciones funcionales en documentation/
Dominio: E-commerce
Flujo: Análisis automático de documentación
Resultado: Extracción automática de entidades (customers, products, orders, order_items)
```

### Ejemplo 2: Banking (FLUJO B - Con Archivo)

```
Dominio: Banking
Archivo: banking_data_specs.instructions.md
Entidades: clients, accounts, transactions, cards
Registros: 5000 clients, 10000 accounts, 100000 transactions
Formatos: CSV, JSON Lines, Parquet
Propósito: Testing de rendimiento
```

### Ejemplo 3: Healthcare (FLUJO C - Interactivo)

```
Dominio: Healthcare
Creación: Interactiva desde cero
Entidades: patients, appointments, diagnoses, treatments
Registros: 2000 patients, 5000 appointments
Formatos: CSV, JSON, Excel
Propósito: Demo/Presentación
```

---

## Cumplimiento y Privacidad

### GDPR Compliance

- Todos los datos son **completamente ficticios**
- No se usan datos personales reales
- DNI/NIE/CIF generados son **inválidos**
- Emails en dominios ficticios (example.com)
- Teléfonos en rangos ficticios (555-xxxx)
- Direcciones ficticias o anonimizadas

### Disclaimer Obligatorio

Todos los datasets incluyen un aviso claro:

> **AVISO**: Este dataset contiene datos sintéticos generados artificialmente
> para propósitos de testing y desarrollo. Ningún dato corresponde a
> personas, organizaciones o eventos reales.

---

## Preguntas Frecuentes

### ¿Cómo funciona el análisis de documentación funcional (FLUJO A)?

El copiloto lee automáticamente todos los documentos del directorio `documentation/`, identifica su tipo (manual, requisitos, especificaciones), hace referencias cruzadas entre ellos y extrae entidades, campos, tipos y reglas de negocio. Genera un archivo de instrucciones estructurado sin intervención manual.

### ¿Qué tipo de documentación puede analizar el FLUJO A?

Manuales de usuario, requisitos funcionales, especificaciones funcionales, diagramas ER, documentación de procesos, planes de prueba y cualquier documento que describa el dominio de negocio y necesidades de datos.

### ¿Puedo regenerar los mismos datos?

Sí. Usa la misma **semilla (seed)** en la configuración. Los datos serán idénticos.

### ¿Qué pasa si necesito más campos después?

1. Edita el archivo de instrucciones del cliente
2. Añade los nuevos campos
3. Re-ejecuta el agente
4. Versiona el dataset (v1.1.0)

### ¿Cómo añado reglas de negocio personalizadas?

Especifícalas en el archivo de instrucciones del cliente en la sección "Reglas de Negocio". El copiloto las aplicará durante la generación.

### ¿Puedo usar mis propios diccionarios?

Sí. Colócalos en `metadata/dictionaries/` en formato JSON y referéncialos en las estrategias de generación. El copiloto priorizará diccionarios existentes del workspace si son relevantes para el dominio.

### ¿Qué hago si la validación falla?

1. Revisa `validation/quality_report.json`
2. Identifica los errores
3. Ajusta el esquema o instrucciones
4. Regenera los datos

---

## Novedades y Mejoras

### FLUJO A - Análisis de Documentación Funcional
Nueva capacidad para **analizar automáticamente documentación funcional** del proyecto:
- Lee múltiples documentos del directorio `documentation/`
- Identifica automáticamente tipo de documento (manual, requisitos, especificaciones)
- Hace referencias cruzadas entre diferentes fuentes
- Extrae entidades, campos, tipos y reglas de negocio
- Genera archivo de instrucciones estructurado automáticamente
- **Prioriza documentación funcional sobre técnica** para casos de prueba
- Reduce significativamente el tiempo de configuración manual

### Plantilla Simplificada para Clientes
El archivo `templates/generate_synthetic_data_template.instructions.md` ha sido **optimizado y reducido en ~40%** respecto a versiones anteriores, eliminando secciones redundantes y simplificando la estructura. Cuenta con 8 secciones bien delimitadas para facilitar su cumplimentación.

### Documentación Automática de Datasets
La instrucción `generate_synthetic_readme.instructions.md` genera automáticamente un **README completo** para cada dataset generado, incluyendo:
- Información del proyecto y métricas de calidad
- Estructura de datos y formatos disponibles
- Ejemplos de uso en múltiples lenguajes
- Configuración de generación y privacidad
- Changelog y soporte

### Interacción Mejorada
- **Step 0**: Validación preventiva de prerequisitos y confirmación de configuración antes de proceder
- **Step 1**: **FLUJO A** para análisis de documentación + Solicitud de aclaraciones automática si falta información
- **Step 2**: Prioriza diccionarios existentes del workspace + Análisis de dependencias con grafo de relaciones
- **Step 4**: Generación de README usando template formal específico con métricas y documentación completa

### Estrategias de Generación Expandidas
10 estrategias diferentes disponibles con configuración detallada:
- UUID, Sequential, Faker, Dictionary, Pattern, Enum, Date Range, Random, Related, Calculated

### Validación Robusta
Control de contexto para evitar que el usuario se desvíe durante la configuración interactiva, asegurando que toda la información necesaria sea recopilada.

---

## Mejores Prácticas

### Durante la Definición del Esquema

- Sé específico con restricciones (min/max, pattern)
- Define campos únicos explícitamente
- Documenta reglas de negocio claramente
- Incluye ejemplos representativos
- Piensa en casos límite y excepcionales

### Durante la Generación

- Usa semillas diferentes para variabilidad
- Genera por lotes si son muchos registros
- Monitorea la memoria en volúmenes grandes
- Valida integridad referencial siempre

### Después de la Generación

- Revisa el quality report completo
- Inspecciona muestras manualmente
- Verifica distribuciones estadísticas
- Prueba cargar datos en tu aplicación
- Versiona el dataset correctamente

---

## Soporte y Contribuciones

### Reportar Problemas

Si encuentras bugs o problemas:
1. Revisa la documentación completa
2. Verifica los logs de generación
3. Consulta el quality report
4. Contacta al equipo de QA

### Mejoras y Sugerencias

Para proponer mejoras al copiloto:
- Nuevas estrategias de generación
- Tipos de datos adicionales
- Validaciones extra
- Formatos de salida adicionales

---

## Changelog

### v1.2.0 (2026-03-09)
- Análisis automático de documentación funcional (FLUJO A)
- Lectura e interpretación de múltiples documentos del proyecto
- Referencias cruzadas entre documentos funcionales
- Identificación automática de tipo de documento
- Extracción automática de entidades, campos y reglas de negocio
- Priorización de documentación funcional sobre técnica
- Reestructuración de flujos: A (documentación), B (archivo), C (interactivo)
- Step 2: Prioriza diccionarios existentes del workspace
- Documentación actualizada con los 3 flujos claramente diferenciados

### v1.1.0 (2026-03-06)
- Archivo `generate_synthetic_readme.instructions.md` para generación automática de README de datasets
- Template `data_template.instructions.md` simplificado (~40% más corto)
- Step 0: Validación preventiva de prerequisitos y confirmación explícita
- Step 1: Solicitud automática de aclaraciones si falta información
- Step 2: Análisis de grafo de dependencias para optimizar generación
- Step 4: Generación automática de documentación usando template específico
- Control de contexto mejorado en interacciones
- Documentación expandida de estrategias de generación

### v1.0.0 (2026-03-06)
- Release inicial del copiloto
- 10 estrategias de generación
- 6 formatos de salida
- 6 dimensiones de calidad
- Modo interactivo completo
- Documentación comprehensiva

---

## Licencia

Uso interno para testing y desarrollo.
