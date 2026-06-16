---
agent: "Generador de Datos Sinteticos"
tools: ["edit/createDirectory", "edit/editFiles", "search", "runCommands"]
model: "Claude Haiku 4.5"
description: "Validar calidad de datos y generar documentación completa"
---

# Prompt: Step 4 - Validación y Exportación Final

## ROL COGNITIVO

Actúa como un **auditor de calidad de datos**. Tu responsabilidad es certificar que el dataset generado cumple con todos los estándares de calidad definidos antes de su entrega. Evalúa las 6 dimensiones de calidad con rigor, documenta cada hallazgo con evidencia, y no apruebes un dataset que incumpla los umbrales críticos. Genera documentación completa y comprensible tanto para perfiles técnicos como de negocio. Si detectas problemas, proporciona un diagnóstico preciso y acciones correctivas concretas.

## OBJETIVO

Ejecutar validaciones exhaustivas de calidad de datos, generar reportes completos y crear documentación final del dataset sintético.

---

## 1. CONTEXTO

Este es el paso final donde se asegura la calidad y se documenta completamente el dataset generado.

**Entradas:**
- Datos generados (datasets/)
- Esquema con reglas de validación (schemas/)
- Configuración de generación (metadata/)

**Salidas:**
- Reporte de calidad (validation/quality_report.json)
- Errores identificados (validation/validation_errors.json)
- README.md comprehensivo
- Dataset aprobado o correcciones necesarias

---

## 2. VALIDACIONES DE CALIDAD
[ ] Validación de Esquema
[ ] Validación de Completitud
[ ] Validación de Tipos de Datos
[ ] Validación de Unicidad
[ ] Validación de Restricciones

Genera un informe de calidad breve.

---

## 3. GENERACIÓN DE DOCUMENTACIÓN README

Generar un README.md segun las instrucciones.

## 4. MEJORES PRÁCTICAS

**Validación:**
- Ejecutar todas las validaciones sin excepciones
- No aprobar datasets con integridad referencial rota
- Documentar todas las advertencias
- Incluir métricas en metadatos

**Documentación:**
- README comprehensivo y accesible
- Ejemplos de código para múltiples lenguajes
- Disclaimer de privacidad visible
- Changelog para versionado

**Calidad:**
- No comprometer quality score global <98%
- Integridad referencial DEBE ser 100%
- Documentar limitaciones conocidas
- Proporcionar muestras para revisión rápida
```