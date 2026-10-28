### Objetivo

## Analizar y comparar dos CSVs de casos de prueba para identificar duplicados funcionales y generar un informe detallado que permita al ingeniero de pruebas tomar decisiones sobre qué casos eliminar antes de la importación a Jira.

### Contexto de los CSVs

El proceso de detección de duplicados trabaja con dos tipos de archivos CSV:

1. **CSV exportado de Jira**: Contiene casos de prueba sin estructura concreta, descriptivos y ya existentes en el sistema Jira.
   - Campos relevantes: Clave de incidencia, ID de la incidencia, Resumen
   - Los casos están descritos en lenguaje natural sin seguir estructura Gherkin
   - Representa los casos de prueba actuales en el sistema

2. **CSV con casos Gherkin**: Contiene casos de prueba estructurados en formato Gherkin, generados por el copiloto gherkin_csv_import_XRAY.
   - Campos relevantes: Issue Id, Test Summary, Description, Gherkin definition, Links
   - Los casos siguen estructura BDD con Given-When-Then
   - Estos casos están listos para ser importados a Jira

### Criterios de Detección de Duplicados

La detección de duplicados NO debe basarse únicamente en similitud textual, sino en **análisis semántico profundo** del objetivo y funcionalidad de cada caso de prueba.

**CRITERIOS OBLIGATORIOS PARA CONSIDERAR UN DUPLICADO:**

- [ ] **Mismo objetivo funcional**: Ambos casos de prueba validan la misma funcionalidad o comportamiento del sistema
- [ ] **Mismo contexto de ejecución**: Los casos se ejecutan sobre el mismo módulo/componente/feature
- [ ] **Mismas precondiciones**: Requieren el mismo estado inicial del sistema
- [ ] **Mismas acciones principales**: Las acciones que se realizan son funcionalmente equivalentes (aunque estén redactadas diferente)
- [ ] **Mismos resultados esperados**: Verifican los mismos criterios de éxito

**IMPORTANTE**: Dos casos pueden estar redactados de forma completamente diferente y aún así ser duplicados. Por ejemplo:
- Caso Jira: "Verificar que el sistema no permite guardar sin completar campos obligatorios"
- Caso Gherkin: "Escenario: El sistema impide guardar cuando faltan datos requeridos"

Estos son duplicados porque tienen el mismo objetivo funcional, aunque la redacción sea diferente.

---

### Análisis Profundo Requerido

Para cada caso de prueba en el CSV de Gherkin, debes realizar un análisis exhaustivo:

1. **Extracción de intención**: Identificar el objetivo principal del caso de prueba
   - ¿Qué funcionalidad se está probando?
   - ¿Cuál es el comportamiento esperado del sistema?
   - ¿Qué regla de negocio se está validando?

2. **Identificación de componentes**: Determinar a qué módulo/componente pertenece
   - Revisar el campo Component en el CSV Gherkin
   - Revisar las etiquetas y Links del caso
   - Analizar el contexto del escenario

3. **Mapeo de acciones**: Traducir los pasos Gherkin a acciones funcionales
   - Dado (Given) = Precondiciones
   - Cuando (When) = Acciones del usuario
   - Entonces (Then) = Resultados esperados

4. **Comparación semántica**: Comparar con todos los casos del CSV de Jira
   - Buscar coincidencias conceptuales, no literales
   - Considerar sinónimos y formas alternativas de expresar la misma idea
   - Evaluar si prueban el mismo flujo funcional

---

### Estructura del Informe de Duplicados

El informe generado DEBE ser un archivo Markdown (.md) con la siguiente estructura:

```markdown
# Informe de Detección de Duplicados

**Fecha de análisis**: [FECHA]  
**CSV Jira analizado**: [RUTA]  
**CSV Gherkin analizado**: [RUTA]  
**Total casos en CSV Jira**: [NÚMERO]  
**Total casos en CSV Gherkin**: [NÚMERO]  
**Duplicados detectados**: [NÚMERO]  

---

## Resumen Ejecutivo

[Breve descripción de los hallazgos principales]

---

## Duplicados Detectados

### Duplicado 1

**CSV Jira (Original)**
- **Clave**: [Clave de incidencia]
- **ID**: [ID de la incidencia]
- **Línea en CSV**: [Número de línea]
- **Título**: [Resumen del caso]

**CSV Gherkin (Nuevo - A importar)**
- **Issue Id**: [Issue Id]
- **Línea en CSV**: [Número de línea]
- **Título**: [Test Summary]
- **Componente**: [Component]
- **Links**: [Links si existen]

**Análisis de similitud**:
[Explicación detallada de por qué se consideran duplicados, analizando:
- Objetivo funcional común
- Acciones equivalentes
- Resultados esperados similares
- Cualquier otro criterio relevante]

**Recomendación**: [¿Se recomienda eliminar el caso del CSV Gherkin? ¿Por qué?]

---

### Duplicado 2

[Repetir estructura para cada duplicado detectado]

---

## Casos sin Duplicados

**Total de casos únicos en CSV Gherkin**: [NÚMERO]

[Opcional: Lista de casos que no tienen duplicados y están listos para importar]

---

## Recomendaciones Finales

[Recomendaciones generales sobre el proceso de importación]
```

---

### Modo Interactivo

Una vez generado el informe, el copiloto DEBE entrar en **modo interactivo** con el ingeniero de pruebas.

**PROCESO INTERACTIVO OBLIGATORIO:**

1. **Presentar el informe**: Mostrar el resumen ejecutivo y estadísticas
2. **Iterar caso por caso**: Para cada duplicado detectado:
   - Mostrar la información del duplicado (ambos casos)
   - Mostrar el análisis de similitud
   - Preguntar al ingeniero: "¿Deseas eliminar este caso del CSV Gherkin que se va a importar? (sí/no/saltar)"
   - Esperar respuesta del usuario
   - Si responde "sí": Marcar el caso para eliminación
   - Si responde "no": Mantener el caso y justificar en el informe final
   - Si responde "saltar": Pasar al siguiente caso sin tomar acción
3. **Generar CSV limpio**: Una vez revisados todos los duplicados, generar un nuevo CSV Gherkin sin los casos marcados para eliminación
4. **Generar informe final**: Actualizar el informe con las decisiones tomadas y estadísticas finales

**FORMATO DE INTERACCIÓN:**

```
[COPILOTO]
══════════════════════════════════════════════════════════════
🔍 DUPLICADO DETECTADO #1 de 5
══════════════════════════════════════════════════════════════

📋 CASO EXISTENTE EN JIRA
   Clave: INTA0001-556
   ID: 10748
   Línea: 2
   Título: La validación integral detecta elementos incompletos e impide la validación

📋 CASO NUEVO (GHERKIN)
   Issue Id: TEST-042
   Línea: 43
   Título: El sistema no permite validar cuando existen elementos sin completar
   Componente: planificacion-prueba-fuego

💡 ANÁLISIS
   Ambos casos verifican que el sistema impide la validación cuando hay
   datos incompletos. Aunque la redacción es diferente, el objetivo
   funcional es idéntico: validar que la validación integral detecta
   elementos incompletos y bloquea el proceso.

❓ ¿Deseas ELIMINAR el caso nuevo (TEST-042) del CSV a importar?
   Responde: si / no / saltar

[USUARIO]
[Espera respuesta del usuario]
```

---

### Criterios de Aseguramiento de Calidad

**COMPROBACIONES OBLIGATORIAS:**

- [ ] Se han analizado TODOS los casos de ambos CSVs
- [ ] El análisis es semántico, no solo textual
- [ ] Cada duplicado tiene una justificación clara y fundamentada
- [ ] El informe incluye número de línea para cada caso en ambos CSVs
- [ ] El informe incluye todos los IDs disponibles (Clave, Issue Id, etc.)
- [ ] Se muestran los títulos completos de ambos casos
- [ ] El modo interactivo permite revisar caso por caso
- [ ] El CSV final generado excluye correctamente los casos eliminados
- [ ] Se genera un informe final con las decisiones tomadas
- [ ] No se han modificado casos que el usuario decidió mantener
- [ ] La numeración de líneas en el informe es precisa y verificable

**VALIDACIONES TÉCNICAS:**

- [ ] El CSV limpio mantiene la estructura y formato original
- [ ] No hay errores de encoding al procesar los CSVs
- [ ] El separador de columnas se detecta correctamente
- [ ] Los campos con comillas y saltos de línea se manejan correctamente
- [ ] El informe está en formato Markdown válido
- [ ] El CSV generado es importable a XRay sin modificaciones

---

### Detección de Falsos Negativos

El copiloto debe ser **conservador** en la detección de duplicados. Es mejor marcar un caso como posible duplicado y dejar que el ingeniero decida, que omitir un duplicado real.

**CASOS ESPECIALES A CONSIDERAR:**

- Casos con diferente nivel de detalle pero mismo objetivo
- Casos que prueban el mismo flujo con diferentes datos de entrada
- Casos que validan la misma regla de negocio en diferentes contextos
- Casos con diferente prioridad pero misma funcionalidad
- Casos relacionados con el mismo User Story o épica

**CRITERIOS PARA NO MARCAR COMO DUPLICADO:**

- Casos que prueban diferentes flujos (happy path vs. casos de error)
- Casos que validan diferentes aspectos de la misma funcionalidad
- Casos con diferentes precondiciones críticas
- Casos que aunque mencionen el mismo componente, prueban funcionalidades distintas
