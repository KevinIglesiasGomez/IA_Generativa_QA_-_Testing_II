# 🚀 Quick Reference: Detector de Duplicados CSV

## Invocación Rápida

```
@csv_duplicate_detector

CSV Jira: CSV_example/Jira.csv
CSV Gherkin: CSV/scenarios_all_final.csv
Informe: informes/duplicados.md
CSV Limpio: CSV/clean.csv
```

---

## Respuestas en Modo Interactivo

| Comando     | Acción                                          |
| ----------- | ----------------------------------------------- |
| `si` o `sí` | ✅ Eliminar el caso del CSV a importar           |
| `no`        | ⛔ Mantener el caso en el CSV a importar         |
| `saltar`    | ⏭️ Decidir después (no se incluye en CSV limpio) |
| `info`      | ℹ️ Ver más detalles del caso                     |
| `gherkin`   | 📄 Mostrar escenario Gherkin completo            |
| `anterior`  | ⬅️ Volver al duplicado anterior                  |

---

## Criterios de Duplicado

Un caso es duplicado cuando cumple **al menos 4 de 5**:

1. ✅ Mismo objetivo funcional
2. ✅ Mismo contexto/componente
3. ✅ Precondiciones equivalentes
4. ✅ Acciones principales similares
5. ✅ Resultados esperados idénticos

---

## Salidas Generadas

1. **Informe MD**: Análisis detallado + decisiones
2. **CSV Limpio**: Sin duplicados, listo para Jira/XRay
3. **Estadísticas**: Resumen del proceso

---

## Archivos del Copiloto

```
.github/
├── agents/csv_duplicate_detector.agent.md
├── instructions/csv_duplicate_detection.instructions.md
└── prompts/csv_duplicate_detection.prompt.md
```

---

## Documentación Completa

- **Guía detallada**: [EJEMPLO_USO_DETECTOR_DUPLICADOS.md](.github/EJEMPLO_USO_DETECTOR_DUPLICADOS.md)
- **README general**: [.github/README.md](.github/README.md)
- **Resumen completo**: [RESUMEN_COPILOTO_CREADO.md](RESUMEN_COPILOTO_CREADO.md)

---

## Ejemplo de Duplicado

**Jira**: "La validación detecta elementos incompletos"  
**Gherkin**: "No es posible validar con datos incompletos"  
**¿Duplicados?** ✅ SÍ - Mismo objetivo funcional

---

## Flujo Completo

```
1. Exportar casos de Jira → CSV Jira
2. Generar casos Gherkin → CSV Gherkin
3. @csv_duplicate_detector → Análisis + Informe
4. Modo interactivo → Decisiones
5. CSV Limpio → Importar a Jira ✓
```

---

**🎯 Objetivo**: Evitar duplicados en Jira manteniendo cobertura completa de pruebas
