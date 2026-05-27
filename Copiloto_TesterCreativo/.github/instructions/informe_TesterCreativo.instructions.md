# Instrucciones para generar el informe para el Agente: Tester Creativo

## 1. Informe

Después de realizar el análisis completo y generar todos los escenarios creativos, debes generar un informe **conciso y accionable** por cada página/componente/funcionalidad analizada.

- Formato Markdown
- Directorio nuevo "informes/" en **la raíz del área de trabajo**.
- Nombre del fichero: `informe_<nombre_pagina_componente>.md`
- **Extensión máxima recomendada**: 4-6 páginas en formato impreso
- Priorizar calidad sobre cantidad: enfoque en los escenarios de mayor valor
- Formato visual y escaneable: uso de tablas, listas y estructura clara
- Solo detalles completos para escenarios de alta prioridad (score >= 6.0)
- Escenarios de prioridad media/baja en formato tabla compacta

### 1.1. Estructura del informe (simplificada)

```markdown
# Informe de Testing Creativo: <nombre>

**Fuente**: <captura/documentación/código/HTML> | **Fecha**: <fecha> | **Complejidad**: <baja/media/alta>

## 1. Descripción y elementos clave
<Breve descripción funcional (2-3 párrafos) + elementos principales identificados>

## 2. Resumen de cobertura EXPLORA

| Categoría | Riesgos | Escenarios | Prioridad |
|---|:---:|:---:|---|
| E - Extremos y Límites | X | Y | Alta/Media/Baja |
| X - Cross-cutting | X | Y | Alta/Media/Baja |
| P - Percepción usuario | X | Y | Alta/Media/Baja |
| L - Lógica de negocio | X | Y | Alta/Media/Baja |
| O - Operaciones concurrentes | X | Y | Alta/Media/Baja |
| R - Resiliencia | X | Y | Alta/Media/Baja |
| A - Adversarial | X | Y | Alta/Media/Baja |
| **TOTAL** | **X** | **Y** | - |

## 3. Top 10-15 Riesgos Principales
<Solo los riesgos más críticos con score >= 6.0, ordenados de mayor a menor>

## 4. Escenarios Creativos (solo alta prioridad)

### Escenario X: <título>
**Categoría**: <E/X/P/L/O/R/A> | **Prioridad**: <score> | **Confianza**: <X%>

**Qué probar**: <descripción breve en 1-2 líneas>

**Pasos**:
1. <paso conciso>
2. <paso conciso>
3. ...

**Resultado esperado**: <breve descripción>
**Riesgo que mitiga**: <descripción breve>

---

## 5. Escenarios Adicionales (media/baja prioridad)

<Listado compacto en formato tabla>

| # | Título | Categoría | Prioridad | Descripción breve |
|---|---|---|---|---|
| X | ... | E | 5.2 | ... |
| Y | ... | P | 4.8 | ... |

## 6. 🚀 Pruebas Extremas e Inesperadas (5-8 escenarios)

<Escenarios creativos "muy locos" que desafían suposiciones y exploran lo improbable>

### 🚀 Prueba Extrema X: <título provocativo>
**Tipo**: <Usuario Caótico/Temporal/Multilenguaje/Hacker Absurdo/etc.>
**Probabilidad**: Extremadamente baja | **Impacto**: <Bajo/Medio/Alto/Crítico>

**Escenario**: <Descripción breve de la situación absurda>

**Cómo ejecutar**:
1. <Paso conciso>
2. <Paso conciso>

**¿Qué podría romperse?**: <Breve especulación>
**Valor**: <Qué suposición desafía>

---

## 7. Recomendaciones
- <Top 3-5 recomendaciones concisas>
```

### 1.2. Actualización del informe

1. El informe se genera una única vez de forma completa y concisa con los escenarios priorizados.

2. Si en el futuro se requieren actualizaciones o se desea agregar nuevos escenarios, se puede generar un fichero de **bitácora** adicional donde se registren los cambios incrementales.
   - Nombre del fichero: `bitacora_<nombre_pagina_componente>.md`
   - Este archivo es opcional y solo se crea si hay actualizaciones posteriores al informe inicial.

3. El **informe inicial** debe ser conciso, accionable y enfocado en escenarios de alta prioridad.

## 1.3. Reglas para la generación del informe

- **Priorizar calidad sobre cantidad**: Enfocarse en los escenarios de mayor valor (prioridad >= 6.0)
- **Solo detalles completos para alta prioridad**: Escenarios con score >= 6.0 deben tener todos los pasos detallados
- **Escenarios de media/baja prioridad**: Formato compacto en tabla resumen
- **Límite recomendado**: 10-20 escenarios con detalle completo + tabla resumen con el resto
- **Riesgos**: Solo mostrar top 10-15 riesgos más críticos, no todos los detectados
- El informe debe ser claro, conciso y accionable
- Evitar repetición: no detallar la misma información en múltiples secciones
- Usar formato visual (tablas, listas) para facilitar lectura rápida
- Antes de generar, verificar si ya existe un informe para esa página/componente
- Si se cambia de página/componente/funcionalidad, se debe generar un nuevo informe específico

## 1.4. Principios de concisión

- **Brevedad**: Descripción funcional en 2-3 párrafos máximo
- **Enfoque**: Priorizar escenarios creativos sobre documentación exhaustiva
- **Cobertura balanceada**: 10-20 escenarios detallados para cobertura adecuada sin ser exhaustivo
- **Legibilidad**: Usar formato que permita escaneo rápido (tablas, bullets, títulos claros)
- **Accionabilidad**: Cada escenario debe ser claro y ejecutable sin ambigüedades
- **Eliminación de ruido**: No incluir información que no aporte valor directo a las pruebas

## 1.5. Verificación antes de entregar el informe

Antes de entregar el informe al ingeniero, verifica que:
- ✅ Longitud razonable: el informe no debe exceder 4-6 páginas en formato impreso
- ✅ Top escenarios destacados: los 10-20 escenarios de mayor prioridad tienen detalle completo
- ✅ Scores calculados: prioridades asignadas correctamente (>=6.0 para alta)
- ✅ Formato consistente y visual: usa tablas y listas para facilitar lectura rápida
- ✅ Sin información redundante: cada dato aparece solo una vez
- ✅ Accionable: cualquier persona puede ejecutar los escenarios sin ambigüedades

---
