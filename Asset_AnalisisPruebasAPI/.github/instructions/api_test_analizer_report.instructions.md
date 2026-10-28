# Instrucciones: Generación de Informes - API Test Analyzer

## 1. Estructura de Archivos

**Ubicación:** `informes/` (raíz del workspace)  
**Nomenclatura:** `informe_[nombre].md` | `bitacora_[nombre].md`

### Informe (estado actual)
Contiene snapshot del estado de pruebas. Verificar existencia antes de crear.

**Contenido obligatorio:**
- Descripción funcional | Elementos identificados | Todas las pruebas existentes | Riesgos/gaps (modelo UNIFIED) | Cobertura por categoría
- **Excluir:** Escenarios propuestos, siguientes pasos, fechas

### Bitácora (historial)
Registro conciso de evolución. Actualizar en decisiones clave: implementación escenario, detección/mitigación gap, cambios cobertura.

## 2. Directrices de Eficiencia (Generación de Contenido)

**Objetivo:** Máxima información con mínimos tokens.

### Estilo de Redacción
- **Formato telegráfico:** Eliminar artículos/conectores innecesarios
- **Listas compactas:** Bullet points con datos clave, sin párrafos
- **Tablas:** Preferir sobre texto narrativo para datos estructurados
- **Descripciones:** Max 1-2 líneas por ítem. Evitar redundancias

### Secciones del Informe

**Descripción funcional:**
```
API: [nombre] | Versión: [X] | Endpoint: [ruta]
Operaciones: GET/POST/PUT/DELETE [recursos]
Parámetros: [lista separada por |]
```

**Elementos identificados:**
Tabla compacta: Elemento | Tipo | Validaciones

**Pruebas existentes:**
```
### [Categoría]
- E1: [Descripción breve] → Status [código] | Validaciones [X items]
- E2: [Descripción breve] → Status [código] | Validaciones [X items]
```

**Riesgos/Gaps:**
```
- [ID]: [Gap conciso] | Impacto: [A/M/B] | Categoría: [POISED]
```

**Cobertura:**
Tabla única POISED sin explicaciones extra.

### Bitácora
```
## [Fecha]
✅ Implementado: E[X], E[Y] | +5pp cobertura
⚠️ Gap detectado: [descripción 1 línea]
```

### Prohibido
- Párrafos explicativos extensos
- Repetir información ya presente
- Introducciones/conclusiones genéricas
- Texto motivacional o relleno
- Explicar lo obvio

## 3. Actualización Post-Sesión (OBLIGATORIO)

**Informe:**
1. Añadir escenarios nuevos en "PRUEBAS EXISTENTES" (subsección por categoría)
2. Actualizar tabla cobertura: cols "Anterior" | "Actual" | indicadores (+X%)
3. Cobertura global: **X%** → **Y%** (+Z pp)
4. Marcar gaps: "GAP MITIGADO" | "COBERTURA PARCIAL"
5. Actualizar priorización

**Bitácora:**
Registrar pruebas añadidas, riesgos detectados/mitigados, progresión cobertura.

## 4. Reglas de Formato

**Tabla POISED:** Cols: Cobertura Anterior | Cobertura Actual | Mejora (+X%)

**Priorización gaps:**
- ✅ ~~Item completo~~ (Escenario X)
- ⚠️ Item parcial (Escenario X)
- Item pendiente

**Separación responsabilidades:**
- Informe = estado sin histórico
- Bitácora = evolución temporal

## 5. Checklist Pre-Cierre

- [ ] Informe refleja todas pruebas implementadas
- [ ] Coberturas actualizadas
- [ ] Gaps marcados correctamente
- [ ] Priorización actualizada
- [ ] Bitácora sincronizada