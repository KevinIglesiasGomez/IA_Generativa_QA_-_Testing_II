# 📋 Plantillas Estándar para Agents, Prompts e Instructions

Este directorio contiene plantillas estandarizadas que equilibran **completitud y simplicidad** para la creación de agents, prompts e instructions, facilitando que todo el equipo trabaje con el mismo formato.

## 🎯 Objetivo

Estandarizar de forma **completa pero ágil** la estructura, formato y contenido de:
- **Agents**: Definición de agentes de IA con su rol y comportamiento
- **Prompts**: Instrucciones que guían el comportamiento de los agentes
- **Instructions**: Reglas específicas y criterios de calidad

## 📁 Estructura de Plantillas

```
templates/
├── agent.template.md          # Plantilla para definir agentes
├── prompt.template.md         # Plantilla para diseñar prompts
├── instructions.template.md   # Plantilla para instrucciones y reglas
└── README.md                  # Esta guía de uso
```

## 🚀 Cómo Usar las Plantillas

### Paso 1: Selecciona la Plantilla Apropiada

- **agent.template.md**: Cuando necesites definir un nuevo agente de IA
- **prompt.template.md**: Cuando necesites diseñar el comportamiento detallado de un agente
- **instructions.template.md**: Cuando necesites definir reglas, criterios o estándares específicos

### Paso 2: Copia la Plantilla

```bash
# Ejemplo para crear un nuevo agent
cp templates/agent.template.md .github/agents/MiNuevoAgente.agent.md

# Ejemplo para crear un nuevo prompt
cp templates/prompt.template.md .github/prompts/prompt_MiNuevoAgente.prompt.md

# Ejemplo para crear nuevas instrucciones
cp templates/instructions.template.md .github/instructions/main_MiNuevoAgente.instructions.md
```

### Paso 3: Completa los Placeholders

Las plantillas incluyen:
- **Placeholders simples entre corchetes** `[descripción]`
- **Comentarios mínimos** solo en secciones opcionales `<!-- OPCIONAL: ... -->`

**Proceso**: 
1. Busca `[` para encontrar placeholders
2. Reemplaza cada `[placeholder]` con tu contenido
3. Elimina secciones marcadas como `<!-- OPCIONAL -->` si no las necesitas

### Paso 4: Verifica y Finaliza

Antes de usar tu plantilla:
- ✅ Todos los placeholders `[corchetes]` reemplazados
- ✅ Secciones opcionales no utilizadas eliminadas
- ✅ Contenido específico y claro
- ✅ Estructura consistente

### 🤖 agent.template.md

Define la **identidad y comportamiento general** de un agente de IA.

**Secciones clave:**
- **Metadatos**: Descripción, herramientas, modelo
-  📖 Descripción de Cada Plantilla

### 🤖 agent.template.md

Define la **identidad y comportamiento general** de un agente de IA.

**Secciones principales:**
- **Metadatos**: Descripción, herramientas, modelo
- **Arquitectura Cognitiva** (opcional): Si usa roles estructurados
- **Rol y Función**: Qué es y qué hace
- **Público objetivo**: Quién lo usa
- **Objetivo principal**: Qué debe lograr
- **Enfoque metodológico**: Principios que sigue
- **Tono y Estilo**: Cómo se comunica
- **Restricciones y Reglas**: Qué debe/no debe hacer

**Cuándo usar**: Al crear un nuevo agente de IA.

### 📝 prompt.template.md

Define el **comportamiento detallado y proceso de trabajo** del agente.

**Secciones principales:**
- **Arquitectura Interna** (opcional): Roles cognitivos múltiples
- **Prerequisitos y Contexto**: Archivos e información necesaria
- **Proceso Obligatorio**: Confirmación, análisis y propuesta
- **Flujo de Trabajo**: Resumen de pasos
- **Flujo Interactivo** (opcional): Patrón de aprobación
- **Formato de Salida**: Estructura de resultados
- **Órdenes Interactivas** (opcional): Comandos del usuario
- **Reglas de Calidad**: Estándares a respetar
- **Principio Fundamental**: Filosofía guía

**Cuándo usar**: Al diseñar cómo trabaja un agente.

### 📚 instructions.template.md

Define **reglas específicas, criterios de calidad y estándares técnicos**.

**Secciones principales:**
- **Objetivo**: Qué cubre este archivo
- **Categorías de instrucciones**: Organizadas por tema
- **Validaciones obligatorias**: Criterios mínimos
- **Modelo/Framework** (opcional): Metodologías estructuradas
- **Buenas Prácticas**: Con ✅ y ❌
- **Aspectos Transversales** (opcional): Consideraciones generales
- **Restricciones**: Limitaciones claras
- **Formato de Salida** (opcional): Artefactos a generar
- **Instrucciones Específicas de Framework** (opcional): Por tecnología

**Cuándo usar**: Al definir criterios de calidad
MiAgente/
├── MiAgente.agent.md                      # Definición del agente
├── prompt_MiAgente.prompt.md              # Comportamiento principal
└── instructions/
    ├── main_MiAgente.instructions.md      # Instrucciones generales
    ├── framework1_MiAgente.instructions.md # Instrucciones específicas framework 1
    └── framework2_MiAgente.instructions.md # Instrucciones específicas framework 2
```

**Ventajas**:
- Separación de responsabilidades
- Reutilización de instrucciones específicas
- Mantenimiento más sencillo
- Escalabilidad

## ✨ Ejemplo de Uso Completo

### Ejemplo: Crear un "Code Review Agent"

#### 1. Agent (CodeReviewer.agent.md)
```markdown
---
description: "Analiza código para detectar problemas de calidad y sugerir mejoras"
tools: ['edit/editFiles', 'search', 'runCommands']
model: "Claude Sonnet 4.6"
---

# Code Review Agent

## Rol
Eres un **experto en revisión de código** y calidad de software.
[... resto del contenido ...]
```

#### 2. Prompt (prompt_CodeReviewer.prompt.md)
```markdown
---
agent: "CodeReviewer"
tools: ["edit/editFiles", "search", "runCommands"]
description: "Revisar código y proponer mejoras de calidad"
model: "Claude Sonnet 4.6"
---

# Prompt: Code Review Agent

## 1. PREREQUISITOS Y CONTEXTO
[... definición del proceso ...]
```

#### 3. Instructions (main_CodeReviewer.instructions.md)
```markdown
# Instrucciones de análisis para el Agente: Code Reviewer

## Objetivo
Estas instrucciones definen los criterios de calidad que el agente debe seguir...
[... criterios específicos ...]
```

#### 4. Instructions específicas (python_CodeReviewer.instructions.md)
```markdown
# Instrucciones específicas de Python para el Agente: Code Reviewer

## 1. Convenciones de Código
### PEP 8
- Usar snake_case para funciones y variables
[... instrucciones específicas de Python ...]
```

## 🎨 Convenciones de Formato

### Placeholders
- Formato: `[descripción breve]`
- Ejemplo: `[Nombre del agente]` → `Code Review Agent`
- Sin prefijos como `REEMPLAZAR:` para mantenerlo limpio

### Secciones Opcionales
Las secciones opcionales tienen un comentario HTML al inicio:
```markdown
<!-- OPCIONAL: Elimina esta sección si no aplica -->
```

### Ejemplos de Código
Usa bloques de código cuando sea apropiado:
````markdown
```javascript
// ✅ USAR: Patrón correcto
const result = await fetchData()

// ❌ EVITAR: Patrón incorrecto
const result = fetchDataSync()
```
````

### Listas de Buenas Prácticas
- ✅ Indica lo que SÍ se debe hacer
- ❌ Indica lo que NO se debe hacer

## ✅ Checklist de Calidad

Antes de considerar completada una plantilla:

- [ ] He reemplazado todos los placeholders `[entre corchetes]`
- [ ] He eliminado las secciones marcadas `<!-- OPCIONAL -->` que no uso
- [ ] El contenido es específico y claro
- [ ] La estructura es consistente
- [ ] He incluido ejemplos donde son útiles (especialmente en instructions)
Consulta los archivos existentes como referencia:
- [FrontendTestAnalizer.agent.md](../.github/agents/FrontendTestAnalizer.agent.md)
- [prompt_FrontendTestAnalizer.prompt.md](../.github/prompts/prompt_FrontendTestAnalizer.prompt.md)
## 📚 Recursos Adicionales

### Ejemplos Reales
Consulta los archivos existentes como referencia:
- [FrontendTestAnalizer.agent.md](../agents/FrontendTestAnalizer.agent.md)
- [prompt_FrontendTestAnalizer.prompt.md](../prompts/prompt_FrontendTestAnalizer.prompt.md)
- [main_FrontendTestAnalizer.instructions.md](../instructions/main_FrontendTestAnalizer.instructions.md)

### Preguntas Frecuentes

**P: ¿Debo usar todas las secciones de cada plantilla?**  
R: No necesariamente. Las secciones marcadas como `<!-- OPCIONAL -->` puedes eliminarlas si no aplican a tu caso.

**P: ¿Puedo añadir nuevas secciones?**  
R: Sí, pero mantén la coherencia con el formato y estructura existente.

**P: ¿Qué hago si mi agente necesita instrucciones para múltiples frameworks?**  
R: Crea un archivo `main_[AgentName].instructions.md` con instrucciones generales y archivos separados por framework: `[framework]_[AgentName].instructions.md`.

**P: ¿Los placeholders `[corchetes]` deben permanecer?**  
R: NO. Debes reemplazarlos todos con tu contenido específico.

**P: ¿Los comentarios `<!-- OPCIONAL -->` deben permanecer?**  
R: NO. Si decides usar la sección, elimina el comentario. Si no la usas, elimina la sección completa.
🤝 Contribución

Si encuentras mejoras para las plantillas:
1. Propón cambios manteniendo el equilibrio entre completitud y simplicidad
2. Documenta claramente el propósito de nuevas secciones
3. Usa placeholders simples `[descripción]` sin prefijos
4. Marca secciones opcionales con `<!-- OPCIONAL: ... -->`
5. Valida que no rompas la compatibilidad con plantillas existentes

---

**Última actualización**: Febrero 2026  
**Versión de plantillas**: 2.0.0 (Equilibradas: Completas pero Amigables)
