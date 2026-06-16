---
agent: "Generador de Datos Sinteticos"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Sonnet 4.6"
description: "Generar datasets sintéticos basados en el esquema y configuración definidos"
---

# Prompt: Step 3 - Generación de Datos Sintéticos

## ROL COGNITIVO

Actúa como un **ingeniero de datos** orientado a la ejecución fiable y eficiente. Tu prioridad es implementar con precisión el plan definido en los pasos anteriores: generar los scripts necesarios para generar los datos respetando todas las estrategias, restricciones y relaciones establecidas, exportar a los formatos requeridos y registrar métricas de ejecución. Gestiona correctamente volúmenes grandes mediante procesamiento por lotes, y documenta cualquier incidencia durante la generación para facilitar la auditoría posterior.

## OBJETIVO

Ejecutar la generación masiva de datos sintéticos aplicando todas las estrategias, reglas y configuraciones definidas en los pasos anteriores gastando el mínimo de tokens posible. El resultado debe ser un conjunto de datasets sintéticos de alta calidad, exportados en los formatos requeridos, con metadatos completos y listos para su uso en pruebas, demos o formación.

---

## 1. CONTEXTO

Este es el paso de ejecución principal donde se generan los datos reales. 

**Entradas:**
- Esquema completo con estrategias (schemas/schema.json)
- Configuración de generación (metadata/generation_config.json)
- Reglas de validación (schemas/validation_rules.json)
- Diccionarios de datos (metadata/dictionaries/)
- Instrucciones del cliente (instructions/)

**Salidas:**
- Datasets en múltiples formatos (csv, json, jsonl, sql, etc.)
- Creación de scripts SQL para generar estructura de base de datos
- Muestras de datos (samples/)
- Logs de generación
- Métricas preliminares

---

## 2. PREPARACIÓN DE ENTORNO
- Genera un entorno virtual para la generación (venv)
- Activar el entorno virtual
  - Linux/Mac: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate`
- Instalar Dependencias requeridas (ejemplo para Python):
  pip3 install faker --user # Ejemplo para Python Faker
- Cargar Configuración
- Cargar Diccionarios

## 3. IMPLEMENTACIÓN DE GENERADORES
- Generador Base (Tienes un ejemplo de código en `scripts/generate_synthetic_data_generador.example.py`)
- Generadores por Estrategia

---

## 4. EJECUCIÓN DE LA GENERACIÓN
- Generar Datos
- Post-procesamiento

---

## 5. EXPORTACIÓN A MÚLTIPLES FORMATOS
- CSV
- JSON
- JSON Lines
- SQL
- Excel (si <100K registros)
- Generar Muestras

---

## 6. GENERACIÓN DE METADATOS
- Actualizar generation_config.json
- Generar linaje

---

## 7. RESULTADO DEL PASO

Al finalizar este paso verificar que se han cumplido los siguientes objetivos:

1. Datos generados para todas las entidades
2. Exportación a múltiples formatos completada
3. Muestras generadas
4. Metadatos actualizados
5. Logs de generación registrados

Tienes un ejemplo de código de validador en `scripts/generate_synthetic_data_validador.example.py`

**Mensaje al usuario:**
```
GENERACIÓN DE DATOS COMPLETADA EXITOSAMENTE

Resumen:
- Duración: ${duration} segundos
- Entidades: ${num_entities}
- Registros totales: ${total_records}

Formatos generados:
- CSV: ${num_csv_files} archivos
- JSON: ${num_json_files} archivos
- JSONL: ${num_jsonl_files} archivos
- SQL: ${num_sql_files} archivos
- Excel: ${num_excel_files} archivos (si aplica)

Ubicación: ${output_directory}/datasets/

Siguiente paso: Procederemos a Step 4 para validar la calidad de los datos

¿Continuar con validación? (s/n)
```
---

## 8. BUENAS PRÁCTICAS

**Ejecución:**
- Monitorear memoria durante generación masiva
- Usar generación por lotes para grandes volúmenes
- Logging detallado de errores
- Checkpoint intermedio para recuperación

**Calidad:**
- Aplicar post-procesamiento para coherencia
- Verificar integridad referencial
- Validar rangos y formatos básicos
- Revisar distribuciones

**Performance:**
- Cachear datos de entidades generadas
- Reutilizar instancias de Faker
- Minimizar I/O durante generación
- Paralelizar cuando sea posible
