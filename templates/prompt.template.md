---
agent: "NombreDelAgente"
tools: ["edit/editFiles", "search", "runCommands"]
description: "Propósito del prompt"
model: "Claude Sonnet 4.6"
---

# Prompt: Nombre del Prompt

## 0. ARQUITECTURA INTERNA DEL AGENTE
<!-- OPCIONAL: Elimina esta sección completa si tu agente no requiere roles cognitivos estructurados -->

Antes de [acción principal], el agente debe ejecutar internamente las siguientes fases. No se permite saltar fases.

### 0.1 Roles Cognitivos Internos

#### ROL A: [Nombre del Rol]
Objetivo: [objetivo del rol]

- [Análisis 1]:
- [Análisis 2]:
- [Análisis 3]:

[Restricción importante]

#### ROL B: [Nombre del Rol]
Objetivo: [objetivo del rol]

Por cada [unidad]:
- [Métrica 1]:
- [Métrica 2]:

[Acción esperada]

#### ROL C: [Nombre del Rol]
Objetivo: [objetivo del rol]

- [Pregunta crítica 1]
- [Pregunta crítica 2]

[Condición de aceptación]

#### ROL D: [Nombre del Rol]
Objetivo: [objetivo del rol]

- [Impacto 1]:
- [Impacto 2]:
- [Sistema de clasificación]:
   Nivel A → [Descripción]  
   Nivel B → [Descripción]  
   Nivel C → [Descripción]  
   Nivel D → [Descripción]

---

## 1. PREREQUISITOS Y CONTEXTO

### 1.1 Archivos de Instrucciones Requeridos

**FUENTE DE [tipo de estándares]**: Este prompt requiere seguir TODAS las instrucciones definidas en los ficheros de instrucciones, que contienen [descripción breve].

### 1.2 Contexto del Proyecto

Actúas como un [rol del agente].

Voy a proporcionarte un [tipo de proyecto] en uno de estos formatos:
- [Formato 1]
- [Formato 2]
- [Formato 3]

Tu tarea es:
1. [Tarea 1]
2. [Tarea 2]
3. [Tarea 3]

---

## 2. PROCESO OBLIGATORIO DE [NOMBRE DEL PROCESO]

### 2.1 Primer paso obligatorio: Confirmación inicial

Antes de [acción principal], debes preguntarme:
1. [Pregunta 1]
2. [Pregunta 2]
3. [Pregunta 3]

Una vez confirmado, procederás al análisis detallado. No proponer cambios sin análisis previo.

### 2.2 Análisis profundo del proyecto

Cuando esté confirmado, debes:
- [Aspecto a analizar 1]
- [Aspecto a analizar 2]
- [Aspecto a analizar 3]
- [Aspecto a analizar 4]
- [Aspecto a analizar 5]

### 2.3 Propuesta validada

Formato de propuesta:

### [Unidad de trabajo]: <nombre>

Estado actual:
- [Qué describir]

Riesgos/Gaps detectados:
- [Qué describir]

Propuesta:
- [Métrica 1]:
- [Métrica 2]:
- [Métrica 3]:

Código/Artefacto propuesto:
```
[código o estructura]
```

Aprobación:
[Pregunta de aprobación]

---

## 3. RESUMEN DE FLUJO DE TRABAJO

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. [Paso 4]
5. [Paso 5]
   5.1. [Sub-paso opcional 1]
   5.2. [Sub-paso opcional 2]

**IMPORTANTE**: [Nota sobre manejo de desvíos]

---

## 4. FLUJO INTERACTIVO
<!-- OPCIONAL: Elimina si tu agente no requiere aprobación paso a paso -->

El agente debe seguir siempre este patrón:
1. [Paso 1]
2. [Paso 2]
3. Proponer escenario individual
4. Preguntar: "[pregunta de aprobación]"
5. Continuar solo si aprueba
6. Si rechaza: [manejo de rechazo]

Nunca generar múltiples propuestas sin aprobación individual.

---

## 5. FORMATO DE SALIDA

Estructura siempre:
- [Sección 1]
- [Sección 2]
- [Sección 3]

MOSTRAR [código/artefacto] propuesto, no solo descripción.

---

## 6. ÓRDENES INTERACTIVAS DEL USUARIO
<!-- OPCIONAL: Elimina si no hay comandos específicos -->

- **[Comando 1]** - [Descripción]
- **[Comando 2]** - [Descripción]
- **[Comando 3]** - [Descripción]

---

## 7. REGLAS DE CALIDAD

- [Regla 1]
- [Regla 2]
- [Regla 3]
- [Regla 4]

---

## 8. PRINCIPIO FUNDAMENTAL

[Declaración del objetivo NO deseado]

[Declaración del objetivo SÍ deseado]

Cada propuesta debe equilibrar:
- [Factor 1]  
- [Factor 2]  
- [Factor 3]  

