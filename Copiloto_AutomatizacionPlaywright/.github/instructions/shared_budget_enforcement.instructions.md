---
description: Control de presupuesto y consumo de tokens reutilizable para agentes personalizados con telemetría OpenTelemetry-compatible
applyTo: "**"
priority: 100
version: 2.1.0
---

# Budget Enforcement - Control de Presupuesto de Tokens y Telemetría

## Enfoque de Telemetría

Este módulo implementa un sistema de **telemetría genérica de tokens** compatible con estándares de observabilidad como OpenTelemetry. Los reportes generados son:

- ✅ **Genéricos**: Sin referencias específicas a proyectos
- ✅ **Estructurados**: Formato JSON exportable
- ✅ **Estándares-compliant**: Siguiendo convenciones OpenTelemetry GenAI
- ✅ **Reutilizables**: Aplicables a cualquier agente personalizado
- ✅ **Observables**: Métricas, spans y traces capturados
- ✅ **Unificados**: Un solo archivo de reporte con historial completo y análisis de costes

### Compatibilidad con OpenTelemetry

Aunque este módulo no implementa directamente el SDK de OpenTelemetry (requiere extensiones programáticas), los conceptos y métricas capturadas siguen las [convenciones semánticas GenAI de OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/):

- **Spans**: Cada operación de herramienta se registra como un "span" conceptual
- **Traces**: Las sesiones se rastrean como traces distribuidos
- **Métricas**: Consumo de tokens, latencia, eficiencia
- **Context Propagation**: Estados de sesión y checkpoints

**Preparado para integración futura**: Si GitHub Copilot expone APIs de telemetría, los reportes JSON pueden exportarse a endpoints OTLP HTTP.

## 1. LÍMITES DE PRESUPUESTO

### Presupuesto por sesión
- **Límite máximo**: 200,000 tokens
- **Umbral de advertencia**: 150,000 tokens (75%)
- **Umbral crítico**: 180,000 tokens (90%)

### Presupuesto por tarea
- **Tarea simple** (explicación, búsqueda): max 20,000 tokens
- **Tarea media** (implementación 1-3 escenarios): max 50,000 tokens
- **Tarea compleja** (refactorización completa): max 100,000 tokens

## 2. MONITOREO OBLIGATORIO

### Al inicio de cada respuesta
1. Evaluar complejidad de la tarea solicitada
2. Estimar tokens requeridos para completarla
3. Verificar tokens disponibles en el presupuesto
4. Si el consumo proyectado superará el 75%, **PREGUNTAR AL USUARIO**:

```
⚠️ Advertencia de presupuesto:
- Tokens consumidos: X / 200,000 (Y%)
- Tokens estimados para esta tarea: Z
- Tokens restantes tras completar: W

¿Continuar con esta operación? (sí/no/simplificar)
```

### Durante operaciones extensas
- Cada 50,000 tokens consumidos, informar progreso del presupuesto:

```
📊 Progreso de presupuesto: X tokens consumidos (Y% del límite)
```

### Al alcanzar umbral crítico (90%)
- **DETENER INMEDIATAMENTE** operaciones no esenciales
- **PREGUNTAR OBLIGATORIAMENTE**:

```
🚨 Presupuesto crítico:
- Solo quedan Z tokens disponibles (10% restante)
- Operaciones pendientes: [lista]

Opciones:
1. Completar solo tarea actual y finalizar sesión
2. Priorizar operaciones críticas únicamente
3. Dividir tarea en múltiples sesiones
4. Guardar estado y continuar en nueva sesión

¿Cómo deseas proceder?
```

### Al agotar presupuesto (100%)
- **DETENER AUTOMÁTICAMENTE** todas las operaciones
- **EJECUTAR PROTOCOLO DE CIERRE**:

```
🛑 Presupuesto agotado:
- Tokens consumidos: 200,000 / 200,000 (100%)

GUARDANDO ESTADO ACTUAL:
- [x] Bitácora actualizada
- [x] Memoria de sesión guardada
- [x] Contexto preservado

Para continuar:
1. Inicia una nueva sesión
2. Revisa: automation_logs/budget_reports/checkpoints/[nombre_tarea]_checkpoint_[porcentaje].md
3. El agente retomará desde el último punto registrado
```

## 3. OPTIMIZACIÓN DE CONSUMO

### Estrategias obligatorias
El agente **DEBE** aplicar estas técnicas para maximizar eficiencia:

#### 3.1 Búsquedas y lecturas eficientes
- ✅ **Búsquedas paralelas**: Agrupar lecturas independientes en un solo bloque de `function_calls`
- ✅ **Pre-filtrado**: Usar `grep_search` antes de `read_file` completo para localizar secciones relevantes
- ✅ **Lecturas selectivas**: Leer solo rangos de líneas necesarios, no archivos completos
- ✅ **Caché de contexto**: No releer archivos ya procesados en la misma sesión
- ❌ **Evitar**: Búsquedas amplias sin filtros, lecturas exploratorias innecesarias

#### 3.2 Respuestas concisas
- ✅ **Directo al punto**: Omitir introducciones y conclusiones innecesarias
- ✅ **Código sin explicaciones redundantes**: Si el código es autoexplicativo, no agregar texto adicional
- ✅ **Confirmaciones breves**: "Completado" en lugar de "He completado exitosamente la tarea solicitada"
- ❌ **Evitar**: Repetir información ya conocida, explicaciones paso a paso cuando no se solicitan

#### 3.3 Ejecución inteligente
- ✅ **Operaciones agrupadas**: Usar `multi_replace_string_in_file` en lugar de múltiples `replace_string_in_file`
- ✅ **Comandos combinados**: Ejecutar múltiples comandos en un solo `run_in_terminal` cuando sea posible
- ✅ **Validación anticipada**: Verificar prerequisitos antes de operaciones costosas
- ❌ **Evitar**: Operaciones secuenciales que pueden paralelizarse

### 3.4 Priorización de recursos

**ALTA PRIORIDAD** (permitir siempre):
- Lectura de archivos de configuración críticos (.instructions.md, .agent.md)
- Ejecución de pruebas automatizadas solicitadas explícitamente
- Actualización de bitácora de cambios
- Aplicación de correcciones tras fallos

**MEDIA PRIORIDAD** (evaluar necesidad según presupuesto):
- Búsquedas semánticas amplias del workspace
- Lecturas exploratorias de código fuente
- Generación de reportes detallados

**BAJA PRIORIDAD** (posponer si presupuesto < 30%):
- Análisis exhaustivo de dependencias
- Generación de documentación extensa no solicitada
- Exploraciones "por si acaso"
- Verificaciones redundantes

## 4. PROTOCOLO DE CHECKPOINTS

### Creación automática de checkpoints
Cuando el consumo alcance **50%, 75% y 90%**, el agente **DEBE**:

1. **Guardar checkpoint en archivo físico del proyecto**:
   
   Archivo: `automation_logs/budget_reports/checkpoints/checkpoint_[porcentaje].md`

```markdown
## Checkpoint - [Timestamp] - [Porcentaje]%

### Estado de Sesión (OpenTelemetry Context)
- **Session ID**: session-[timestamp]
- **Trace ID**: [UUID]
- Tokens consumidos: X / 200,000 (Y%)
- Timestamp: [ISO 8601]

### Contexto de Trabajo
- Tarea en proceso: [descripción genérica]
- Paso actual: [descripción]
- Archivos impactados: [lista]

### Progreso Completado
- ✅ Operaciones exitosas: [lista]
- ✅ Archivos creados/modificados: [lista]

### Tareas Pendientes
- ⏸️ Operaciones sin completar: [lista]
- ⏸️ Correcciones pendientes: [lista]
- ⏸️ Validaciones pendientes: [lista]

### Metadata OpenTelemetry
```json
{
  "traceparent": "00-[trace-id]-[span-id]-01",
  "tracestate": "checkpoint=Y%",
  "baggage": {
    "files_created": N,
    "files_modified": M,
    "operations_completed": X
  }
}
```

### Contexto para Retomar
- Datos necesarios: [lista]
- Dependencias: [lista]
- Notas técnicas: [observaciones]
```

2. **Informar al usuario**:

```
💾 Checkpoint automático guardado (Y% del presupuesto consumido)
Estado preservado en: automation_logs/budget_reports/checkpoints/checkpoint_[porcentaje].md
Trace ID: [UUID]
```

### Recuperación desde checkpoint
Al iniciar una nueva sesión, el agente puede retomar desde el último checkpoint:

1. Leer `automation_logs/budget_reports/checkpoints/` para identificar checkpoints recientes
2. Cargar el checkpoint más reciente del feature correspondiente
3. Informar al usuario del estado recuperado
4. Continuar desde el último paso registrado

## 5. INTEGRACIÓN CON FLUJO INTERACTIVO

### Preguntas combinadas con advertencias de presupuesto
Cuando el agente deba realizar preguntas interactivas según su flujo normal, puede combinarlas con información de presupuesto:

```
[Pregunta del flujo interactivo del agente]

---
💡 Información de presupuesto: Esta operación consumirá aproximadamente X tokens (quedarán Y disponibles - Z%)
```

### Comandos de usuario relacionados con presupuesto
El usuario puede usar estos comandos en cualquier momento:

- **"estado presupuesto"** → Mostrar consumo actual detallado
- **"optimizar"** → Activar modo de consumo mínimo para operaciones restantes
- **"dividir tarea"** → Sugerir puntos de división óptimos para múltiples sesiones
- **"checkpoint"** → Crear checkpoint manual inmediato
- **"estimar tarea"** → Estimar consumo de tokens antes de ejecutar

## 6. MÉTRICAS DE SESIÓN

### Ubicación de reportes y checkpoints

#### Archivos físicos generados en el proyecto
El agente **DEBE** crear estos archivos físicos en el proyecto:

1. **Reporte unificado de telemetría**: `automation_logs/budget_reports/telemetry_report.md`
   - Resumen ejecutivo con estado actual
   - Análisis de costes estimados (referencia)
   - Historial completo de todas las sesiones
   - Métricas de eficiencia y optimizaciones
   - Estadísticas acumuladas del proyecto
   - Proyecciones y recomendaciones
   - Formato JSON exportable OpenTelemetry
   - **SE ACTUALIZA** tras cada sesión (no se crean múltiples archivos)

2. **Checkpoints de recuperación**: `automation_logs/budget_reports/checkpoints/[feature]_checkpoint_[porcentaje].md`
   - Estado completo del progreso
   - Contexto para retomar sesiones
   - Archivos modificados
   - Escenarios pendientes

#### Estructura de carpetas
```
automation_logs/
├── automation_bitacora.md          # Bitácora principal del proyecto (opcional, específico del agente)
└── budget_reports/                  # Reportes de telemetría de tokens (OBLIGATORIO)
    ├── README.md                    # Documentación de reportes
    ├── telemetry_report.md          # Reporte unificado (ÚNICO ARCHIVO, se actualiza)
    └── checkpoints/                 # Checkpoints de recuperación
        ├── checkpoint_50.md
        ├── checkpoint_75.md
        └── checkpoint_90.md
```

#### Memoria interna de VS Code Copilot (temporal)
Adicionalmente, el agente usa la memoria interna de Copilot como respaldo:
- `/memories/session/` → Checkpoints temporales (se pierden al cerrar VS Code)
- `/memories/repo/` → Contexto del repositorio (opcional, persistente)

**Recomendación**: El archivo físico `automation_logs/budget_reports/telemetry_report.md` es la fuente de verdad persistente y debe consultarse para recuperación de sesiones.

### Al finalizar cada sesión (OBLIGATORIO)
El agente **DEBE** actualizar el archivo físico: `automation_logs/budget_reports/telemetry_report.md`

**Formato: Reporte Unificado de Telemetría (OpenTelemetry-compatible)**

```markdown
# Reporte Unificado de Telemetría y Presupuesto

**Proyecto:** [Nombre del Proyecto]
**Agente:** [Nombre del Agente]
**Fecha Inicio:** [fecha]
**Última Actualización:** [fecha]

---

## 📊 RESUMEN EJECUTIVO

### Estado Actual del Presupuesto
```json
{
  "tokens_consumed": X,
  "budget_limit": 200000,
  "percentage_used": Y,
  "tokens_remaining": Z,
  "status": "SALUDABLE/ADVERTENCIA/CRÍTICO",
  "sessions_completed": N
}
```

### 💰 Análisis de Costes (Estimado)

> **Nota:** GitHub Copilot no cobra por tokens individualmente. Las estimaciones siguientes son referencias basadas en precios de modelos similares (Claude Sonnet 4.5) para contexto.

```json
{
  "estimated_cost_per_session": {
    "input_tokens": X,
    "input_cost_usd": X * 3.00 / 1000000,
    "output_tokens": Y,
    "output_cost_usd": Y * 15.00 / 1000000,
    "total_session_cost_usd": "suma"
  },
  "projected_total_project_cost": {
    "estimated_total_tokens": 200000,
    "estimated_sessions": N,
    "estimated_total_cost_usd": "estimación"
  },
  "cost_efficiency": {
    "cost_per_scenario_implemented": "coste/escenarios",
    "cost_savings_from_optimizations": "ahorro",
    "optimization_percentage": Y
  }
}
```

**Referencia de Precios (Claude Sonnet 4.5):**
- Input: $3.00 / 1M tokens
- Output: $15.00 / 1M tokens

---

## 📈 HISTORIAL DE SESIONES

### Sesión N - [Nombre] ([Fecha])

**Trace ID:** `[UUID]`
**Duración:** X minutos
**Tokens:** X / 200,000 (Y%)
**Coste Estimado:** $X.XX USD

#### Logros
- [Lista de logros]

#### Métricas de Operaciones
```json
{
  "operations_breakdown": {
    "read_file": {"calls": X, "tokens": Y, "percentage": Z},
    "create_file": {"calls": X, "tokens": Y, "percentage": Z}
  }
}
```

---

## 🎯 EFICIENCIA Y OPTIMIZACIONES

[Detalles de optimizaciones aplicadas]

---

## 📊 ANÁLISIS ACUMULADO DEL PROYECTO

[Progreso general, features completadas, cobertura]

---

## 📉 PROYECCIONES Y ANÁLISIS PREDICTIVO

[Proyecciones de consumo futuro]

---

## 💰 ANÁLISIS DE COSTE-BENEFICIO

### Métricas de Valor
```json
{
  "cost_per_scenario": X,
  "estimated_manual_cost_equivalent": {
    "hours_saved": Y,
    "hourly_rate_usd": 50,
    "manual_cost_usd": Y * 50,
    "automation_cost_usd": X,
    "savings_percentage": ((manual - automation) / manual) * 100
  }
}
```

---

## 📊 Métricas de Consumo de la Última Sesión

### Consumo Total
```json
{
  "tokens_consumed": 42000,
  "budget_limit": 200000,
  "percentage_used": 21.0,
  "tokens_remaining": 158000,
  "tokens_per_minute": 1400
}
```

### Umbrales de Presupuesto
```json
{
  "threshold_critical_reached": false,
  "threshold_warning_reached": false,
  "current_threshold_percentage": 21.0
}
```

---

## 🔧 Telemetría de Operaciones (OpenTelemetry Spans)

### Operaciones de Lectura
```json
{
  "total_read_operations": 12,
  "read_file_calls": 10,
  "grep_search_calls": 1,
  "file_search_calls": 1,
  "semantic_search_calls": 0,
  "list_dir_calls": 4,
  "total_lines_read": 1500,
  "tokens_estimated": 18000
}
```

### Operaciones de Escritura
```json
{
  "total_write_operations": 3,
  "create_file_calls": 3,
  "replace_string_calls": 0,
  "multi_replace_calls": 0,
  "tokens_estimated": 8000
}
```

### Operaciones de Terminal
```json
{
  "total_terminal_operations": 0,
  "run_in_terminal_calls": 0,
  "get_terminal_output_calls": 0,
  "tokens_estimated": 0
}
```

### Operaciones Paralelas
```json
{
  "parallel_batches_executed": 3,
  "average_operations_per_batch": 3.3,
  "efficiency_gain": "Alta"
}
```

---

## 📈 Desglose de Consumo por Tipo de Operación

| Tipo de Operación | Llamadas | Tokens Estimados | % del Total | Latencia Promedio |
|-------------------|----------|------------------|-------------|-------------------|
| read_file | 10 | 15,000 | 35.7% | ~2.5s |
| create_file | 3 | 8,000 | 19.0% | ~3.0s |
| Agent responses | N/A | 15,500 | 36.9% | ~5.0s |
| grep_search | 1 | 2,000 | 4.8% | ~1.5s |
| file_search | 1 | 1,000 | 2.4% | ~1.0s |
| list_dir | 4 | 500 | 1.2% | ~0.5s |
| **TOTAL** | **19** | **42,000** | **100%** | - |

---

## 🎯 Optimizaciones de Eficiencia Aplicadas

```json
{
  "parallel_reads": true,
  "parallel_reads_count": 3,
  "targeted_searches": true,
  "selective_line_reading": true,
  "context_caching": false,
  "response_conciseness": true,
  "proactive_batching": true
}
```

### Impacto de Optimizaciones
```
Sin optimizaciones estimado: ~65,000 tokens
Con optimizaciones real: 42,000 tokens
Ahorro estimado: 23,000 tokens (35.4% de reducción)
```

---

## 📉 Análisis de Patrones de Consumo

### Distribución Temporal
```json
{
  "0-5_min": {"tokens": 8400, "percentage": 20},
  "5-10_min": {"tokens": 10500, "percentage": 25},
  "10-20_min": {"tokens": 12600, "percentage": 30},
  "20-30_min": {"tokens": 10500, "percentage": 25}
}
```

### Picos de Consumo
```
Pico máximo: ~2,100 tokens/minuto
Pico mínimo: ~1,050 tokens/minuto
Promedio: ~1,400 tokens/minuto
```

---

## 📋 Historial de Warnings del Sistema

```json
[
  {"timestamp": "T1", "tokens": 24076, "percentage": 12.0},
  {"timestamp": "T2", "tokens": 26495, "percentage": 13.2},
  {"timestamp": "T3", "tokens": 30196, "percentage": 15.1},
  {"timestamp": "T4", "tokens": 37798, "percentage": 18.9},
  {"timestamp": "T5", "tokens": 44805, "percentage": 22.4}
]
```

---

## 📊 Resumen Estadístico Final (OpenTelemetry-compatible JSON)

```json
{
  "session_id": "session-2026-04-27-inicial",
  "trace_id": "00-abc123...-01",
  "total_tokens_consumed": 42000,
  "total_tokens_budget": 200000,
  "percentage_used": 21.0,
  "tokens_remaining": 158000,
  "efficiency_classification": "ALTA",
  "parallel_batches": 3,
  "tool_calls_total": 19,
  "files_read": 12,
  "files_created": 3,
  "terminal_executions": 0,
  "optimization_savings": 23000,
  "optimization_percentage": 35.4,
  "session_duration_minutes": 30,
  "tokens_per_minute": 1400,
  "estimated_remaining_time_minutes": 113,
  "spans": [
    {"operation": "read_file", "count": 10, "tokens": 15000},
    {"operation": "create_file", "count": 3, "tokens": 8000}
  ]
}
```

---

---

## 📊 MÉTRICAS OPENTELEMETRY (JSON EXPORTABLE)

```json
{
  "telemetry_version": "2.0.0",
  "opentelemetry_compatible": true,
  "project": {
    "name": "[nombre_proyecto]",
    "agent": "[nombre_agente]",
    "start_date": "[ISO 8601]"
  },
  "sessions": [
    {
      "session_id": "session-[timestamp]",
      "trace_id": "00-[uuid]-01",
      "gen_ai.usage.input_tokens": X,
      "gen_ai.usage.output_tokens": Y,
      "custom.cost_usd": Z,
      "custom.scenarios_implemented": N
    }
  ],
  "aggregated_metrics": {
    "total_tokens": X,
    "total_cost_usd": Y,
    "total_scenarios": N
  }
}
```

**Reporte generado automáticamente**  
**Versión:** Token Telemetry Reporter v2.0.0  
**Formato:** OpenTelemetry-Compatible JSON  
**Timestamp:** [ISO 8601]
```

### Actualización del reporte unificado (OBLIGATORIO)
**IMPORTANTE:** Al finalizar cada sesión, el agente **DEBE ACTUALIZAR** (no crear nuevo) el archivo `automation_logs/budget_reports/telemetry_report.md`:

**Acciones a realizar:**
1. Leer el archivo existente `telemetry_report.md` (si existe)
2. Actualizar la sección "RESUMEN EJECUTIVO" con los datos actuales
3. Actualizar la sección "💰 Análisis de Costes" con totales acumulados
4. **AGREGAR** una nueva entrada en "HISTORIAL DE SESIONES" (no reemplazar)
5. Actualizar "ANÁLISIS ACUMULADO DEL PROYECTO" con progreso total
6. Actualizar "PROYECCIONES" basadas en el consumo acumulado
7. Actualizar "MÉTRICAS OPENTELEMETRY" agregando la nueva sesión al array

**NO CREAR archivos separados por sesión.** Todo debe estar en un único archivo unificado.

Ver el formato completo en la sección anterior "REPORTE UNIFICADO DE TELEMETRÍA Y PRESUPUESTO" que incluye:
- Resumen Ejecutivo con estado actual
- Análisis de Costes (con precios de referencia)
- Historial completo de todas las sesiones
- Eficiencia y Optimizaciones
- Análisis Acumulado del Proyecto
- Proyecciones y Análisis Predictivo
- Análisis de Coste-Beneficio
- Métricas OpenTelemetry exportables

---
    {"id": 1, "tokens": 87400, "percentage": 43.7},
    {"id": 2, "tokens": 152300, "percentage": 76.2},
    {"id": 3, "tokens": 134200, "percentage": 67.1}
  ],
  "average_tokens": 124633,
  "trend": "FLUCTUANTE"
}
```

### Distribución por Tipo de Operación (Acumulado)
| Tipo | Llamadas | % Total | Tokens | % Tokens |
|------|----------|---------|--------|----------|
| read_file | 87 | 52.4% | 125,000 | 39.7% |
| create_file | 15 | 9.0% | 35,000 | 11.1% |
| Agent responses | N/A | N/A | 110,000 | 34.9% |
| terminal | 8 | 4.8% | 25,000 | 7.9% |
| searches | 56 | 33.7% | 20,000 | 6.3% |

---

## 🎯 Patrones de Optimización Identificados

```json
{
  "parallel_reading": {
    "usage": "Alta",
    "impact": "Alto",
    "savings_per_batch": 2500,
    "recommendation": "Continuar aplicando"
  },
  "selective_line_reading": {
    "usage": "Alta",
    "impact": "Medio-Alto",
    "savings_per_operation": 700,
    "recommendation": "Continuar aplicando"
  },
  "context_caching": {
    "usage": "No implementado",
    "potential_savings": "10-15%",
    "recommendation": "Implementar"
  }
}
```

---

## 🔍 Proyecciones y Análisis Predictivo

```json
{
  "sessions_until_75_percent": 0,
  "sessions_until_90_percent": 0,
  "sessions_until_budget_exhaustion": 0.6,
  "recommended_checkpoint_interval": "Cada 50,000 tokens",
  "estimated_capacity_remaining": "1-2 sesiones más"
}
```

---

## 📊 KPIs de Rendimiento

```json
{
  "efficiency_score": 8.7,
  "optimization_ratio": 28.2,
  "parallel_effectiveness": "Alta",
  "cost_benefit_ratio": "Excelente",
  "budget_health": "Moderado"
}
```

---

**Reporte generado automáticamente**  
**Módulo**: Token Telemetry Consolidator v2.0.0  
**OpenTelemetry Compatible**: Si (convenciones GenAI)  
**Timestamp**: [ISO 8601]  
**Frecuencia de actualización**: Tras cada sesión
```

## 7. MODO ECONÓMICO

### Activación automática
Cuando quedan menos del 25% de tokens (< 50,000):

```
🔋 Modo económico activado automáticamente

Restricciones activas:
- Búsquedas: Solo targeted grep_search
- Lecturas: Máximo 100 líneas por archivo
- Respuestas: Formato conciso obligatorio
- Validaciones: Solo críticas

Esto maximizará el aprovechamiento del presupuesto restante.
```

### Comportamiento en modo económico
- ❌ **Deshabilitado**: semantic_search, exploraciones amplias
- ⚠️ **Limitado**: read_file (max 100 líneas), grep_search (includePattern obligatorio)
- ✅ **Permitido**: Operaciones de escritura, ejecución de comandos, preguntas al usuario

## 8. CASOS ESPECIALES

### 8.1 Operaciones costosas conocidas
Estas operaciones consumen muchos tokens, el agente debe **advertir antes de ejecutar**:

- `semantic_search` sin query específico: ~10,000-30,000 tokens
- Lectura completa de workspace grande: ~50,000-100,000 tokens
- Ejecución con output extenso: ~5,000-20,000 tokens
- Análisis profundo de errores: ~10,000-25,000 tokens

### 8.2 Tareas que pueden fragmentarse
Si una tarea grande amenaza con agotar el presupuesto, **sugerir fragmentación**:

```
⚠️ Tarea detectada como fragmentable:
- Automatizar 20 escenarios BDD
- Consumo estimado: ~150,000 tokens (75% del presupuesto)

Sugerencia de fragmentación:
- Sesión 1: Escenarios 1-7 (login y autenticación) - ~50,000 tokens
- Sesión 2: Escenarios 8-14 (gestión de datos) - ~50,000 tokens  
- Sesión 3: Escenarios 15-20 (reportes y validaciones) - ~50,000 tokens

¿Proceder con fragmentación o continuar con todo en esta sesión?
```

## 9. EXCEPCIONES AL CONTROL DE PRESUPUESTO

### Operaciones que NO deben bloquearse nunca
Incluso con presupuesto agotado, **siempre permitir**:

1. ✅ **Actualización de bitácora**: Guardar progreso completado en `automation_logs/automation_bitacora.md`
2. ✅ **Creación de checkpoint**: Preservar estado en `automation_logs/budget_reports/checkpoints/`
3. ✅ **Reporte de telemetría**: Actualizar métricas en `automation_logs/budget_reports/telemetry_report.md`
4. ✅ **Respuesta a preguntas del usuario**: Comunicación básica
5. ✅ **Guardado de archivos pendientes**: Evitar pérdida de trabajo

### Protocolo cuando se alcanza el límite absoluto
```
🛑 Presupuesto totalmente agotado

ACCIONES FINALES EJECUTADAS:
1. ✅ Bitácora actualizada (si aplica al agente)
2. ✅ Checkpoint final creado: automation_logs/budget_reports/checkpoints/checkpoint_final.md
3. ✅ Reporte de telemetría actualizado: automation_logs/budget_reports/telemetry_report.md
4. ✅ Archivos pendientes guardados

ESTADO FINAL:
- Operaciones completadas: X/Y
- Archivos modificados: [lista]
- Tokens consumidos: 200,000 / 200,000 (100%)

REPORTES DISPONIBLES:
- Reporte unificado de telemetría: automation_logs/budget_reports/telemetry_report.md
- Último checkpoint: automation_logs/budget_reports/checkpoints/checkpoint_final.md

PARA CONTINUAR:
Inicia nueva sesión y solicita: "Retomar desde último checkpoint"
```

## 10. PREGUNTAS DE ESTIMACIÓN PREVIA

### Antes de operaciones costosas
Antes de comenzar tareas que consumirán significativos tokens, el agente puede **preguntar para estimar**:

```
📋 Estimación de presupuesto necesaria:

Operación solicitada: [descripción]
Complejidad estimada: [simple/media/compleja]
Tokens estimados: ~X tokens
Presupuesto actual disponible: Y tokens (Z%)

¿Cómo deseas proceder?
1. Continuar con la operación completa
2. Simplificar la operación
3. Dividir en múltiples sesiones
4. Cancelar operación
```

---

## 11. INTEGRACIÓN CON OPENTELEMETRY (PREPARACIÓN FUTURA)

### Conceptos OpenTelemetry Aplicados

Este módulo implementa conceptos de observabilidad compatibles con [OpenTelemetry](https://opentelemetry.io/):

#### Traces y Spans
- **Trace**: Cada sesión de trabajo representa un trace distribuido
- **Span**: Cada operación de herramienta (read_file, create_file, etc.) se registra como un span conceptual
- **Trace ID**: Generado para cada sesión (UUID) para correlación
- **Parent-Child Relationships**: Operaciones paralelas comparten el mismo parent span

#### Métricas Capturadas (Convenciones GenAI)

Siguiendo [OpenTelemetry Semantic Conventions for GenAI](https://opentelemetry.io/docs/specs/semconv/gen-ai/):

```json
{
  "gen_ai.operation.name": "copilot.session",
  "gen_ai.request.model": "claude-sonnet-4.5",
  "gen_ai.usage.input_tokens": 42000,
  "gen_ai.usage.output_tokens": 15500,
  "gen_ai.response.finish_reasons": ["completed", "budget_limit"],
  "gen_ai.system": "github.copilot",
  "telemetry.sdk.name": "budget-enforcement",
  "telemetry.sdk.version": "2.0.0"
}
```

#### Context Propagation

Los checkpoints implementan propagación de contexto similar a OpenTelemetry:
- **traceparent**: Session ID + Checkpoint percentage
- **tracestate**: Estado de progreso serializado
- **baggage**: Metadata adicional (archivos, tokens, estado)

### Exportación de Datos

Los reportes JSON embebidos pueden exportarse a:

1. **Consola/Logs** (actual) → Archivos markdown con bloques JSON
2. **OTLP HTTP Endpoint** (futuro) → POST a collector OpenTelemetry
3. **File Exporter** (futuro) → JSON Lines format
4. **Prometheus** (futuro) → Métricas en formato Prometheus

#### Ejemplo de Integración Futura

Si GitHub Copilot expone capacidades de telemetría programáticas:

```typescript
// Ejemplo conceptual - NO IMPLEMENTADO AÚN
import { CopilotClient } from "@github/copilot-sdk";

const client = new CopilotClient({
  telemetry: {
    otlpEndpoint: "http://localhost:4318",
    captureContent: false,
    sourceName: "budget-enforcement"
  },
  onGetTraceContext: () => {
    const carrier: Record<string, string> = {};
    propagation.inject(context.active(), carrier);
    return carrier;
  }
});
```

### Visualización y Análisis

Los datos JSON pueden consumirse por herramientas de observabilidad:

- **Jaeger**: Visualizar traces distribuidos de sesiones
- **Grafana**: Dashboards de consumo de tokens
- **Prometheus**: Alertas basadas en umbrales
- **Datadog/New Relic**: Monitoreo APM

### Roadmap de Telemetría

**v2.0 (Actual)**
- ✅ Reportes JSON estructurados
- ✅ Conceptos de spans y traces
- ✅ Métricas según convenciones GenAI
- ✅ Checkpoints como context propagation

**v2.1 (Futuro)**
- 🔄 Exportador OTLP HTTP
- 🔄 Integración con GitHub Copilot SDK telemetry
- 🔄 Real-time metrics streaming

**v2.2 (Futuro)**
- 🔄 Dashboard web integrado
- 🔄 Alertas proactivas vía webhooks
- 🔄 Machine learning para predicción de consumo

### Referencias

- [OpenTelemetry GenAI Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [GitHub Copilot SDK Observability](https://docs.github.com/es/copilot/how-tos/copilot-sdk/observability/opentelemetry)
- [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/)
- [Trace Context W3C](https://www.w3.org/TR/trace-context/)

---

## CHANGELOG

### v2.1.0 (27 de abril de 2026)
**Simplificación y Mejoras:**
- ✅ **Reporte unificado**: Ahora se genera un solo archivo `telemetry_report.md` en lugar de múltiples archivos separados
- ✅ **Análisis de costes**: Incluye estimaciones de coste basadas en precios de referencia de Claude Sonnet 4.5
- ✅ **ROI visible**: Comparación automática con coste de desarrollo manual
- ✅ **Mantenimiento simplificado**: Actualización en un solo lugar en lugar de gestionar múltiples archivos
- ✅ **Historial completo**: Todas las sesiones en orden cronológico en un único documento
- ⚠️ **Breaking change**: Eliminados `budget_session_[timestamp].md` y `budget_summary.md` - ahora todo está en `telemetry_report.md`

### v2.0.0 (Anterior)
- Telemetría OpenTelemetry-compatible
- Reportes genéricos reutilizables
- Múltiples archivos por sesión

---

## RESUMEN DE REGLAS CRÍTICAS

1. ✅ **Monitorear en todo momento** el consumo de tokens
2. ✅ **Advertir proactivamente** cuando se alcancen umbrales (75%, 90%)
3. ✅ **Optimizar automáticamente** usando estrategias de eficiencia
4. ✅ **Crear checkpoints** en hitos clave (50%, 75%, 90%)
5. ✅ **Modo económico** automático al llegar a 25% restante
6. ✅ **Protocolo de cierre** estructurado al agotar presupuesto
7. ✅ **Nunca perder trabajo**: Guardar estado antes de detenerse
8. ✅ **Transparencia total**: Usuario siempre informado del estado del presupuesto
9. ✅ **Telemetría genérica**: Reportes sin referencias específicas a proyectos
10. ✅ **OpenTelemetry-compatible**: Formato JSON exportable según estándares
