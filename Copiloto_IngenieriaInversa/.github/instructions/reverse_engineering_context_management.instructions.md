# Instrucciones de Gestión de Contexto y Compactado para el Agente: Reverse Engineering Functional Analyst

## Objetivo

Estas instrucciones definen cómo el agente debe gestionar la persistencia de estado y la recuperación de contexto durante el proceso de ingeniería inversa, especialmente cuando la conversación se compacta (manual con `/compact` o automáticamente por límite de contexto).

---

## 1. PERSISTENCIA DE ESTADO EN MEMORIA DE SESIÓN

### Momentos obligatorios de guardado

El agente DEBE guardar el estado del análisis en `/memories/session/reverse_engineering_state.md` en estos momentos:

1. **Al completar la Fase 0** (descubrimiento aprobado) — Guardar: PROJECT_ROOT, tecnología, mapa de módulos, clasificación épica/historia, modo elegido
2. **Al aprobar cada historia** — Actualizar: progreso de historias, dudas nuevas, siguiente paso
3. **Antes de sugerir `/compact`** — Guardar snapshot completo con toda la información acumulada
4. **Al generar cada fichero** — Registrar: nombre del fichero generado, ruta, estado de aprobación

### Formato del fichero de estado

```markdown
# Estado del Análisis de Ingeniería Inversa

## Proyecto
- PROJECT_ROOT: [ruta]
- App: [nombre]
- Tecnología: [framework + versión]
- Modo: [Resumen/Completo]
- Fase actual: [0/1/2/3]

## Progreso de historias
| Historia | Estado | Fichero generado |
|----------|--------|------------------|

## Dudas acumuladas
| # | Área | Pregunta |
|---|------|----------|

## Última acción
[Descripción de la última acción completada y siguiente paso]
```

---

## 2. PROTOCOLO DE RECUPERACIÓN POST-COMPACTADO

Cuando el agente detecte que la conversación fue compactada (el contexto anterior es un resumen), debe:

1. Leer `/memories/session/reverse_engineering_state.md` para recuperar el estado completo
2. Si existe un documento general ya generado, leerlo para recuperar el mapa de historias
3. Confirmar con el usuario: "He recuperado el estado del análisis. Estábamos en [fase/historia]. ¿Continuamos?"
4. Retomar el trabajo desde el punto exacto donde se quedó

---

## 3. PUNTOS DE COMPACTADO SUGERIDOS

El agente debe sugerir al usuario ejecutar `/compact` en estos momentos del flujo:

1. **Después de completar la Fase 0** (descubrimiento aprobado) — el mapa ya está guardado
2. **Después de cada 3-4 historias aprobadas** en Modo Completo — para mantener rendimiento
3. **Después de generar el documento general** (antes de pasar a historias detalladas)
4. **Antes de iniciar una épica compleja** — liberar contexto para el análisis profundo
5. **Cuando el agente detecte respuestas lentas** o contexto extenso

---

## 4. FORMATO DE SUGERENCIA AL USUARIO

El agente DEBE usar el siguiente formato al sugerir `/compact`. Es importante que el mensaje sea claro, visible y tranquilice al usuario sobre la seguridad de la operación:

```
---
**📦 SUGERENCIA DE COMPACTADO**

Se han procesado [X] historias/fases desde el último punto de guardado.
- Estado guardado en memoria de sesión: ✅
- Fase actual: [fase]
- Siguiente paso: [descripción]

Puedes ejecutar `/compact` para liberar contexto y mantener el rendimiento.
Tras el compactado, recuperaré automáticamente el estado desde la memoria de sesión. **No se perderá ninguna información.**
---
```

### Cuándo es OBLIGATORIO mostrar este mensaje

1. Al completar la Fase 0 (descubrimiento aprobado)
2. Cada 3-4 historias aprobadas en Modo Completo
3. Al completar el documento general (antes de Step 2)
4. Antes de iniciar una épica compleja
5. Cuando el agente detecte respuestas lentas o contexto extenso

---

## 5. INFORMACIÓN CRÍTICA A PRESERVAR

La propiedad `chatSummary` del agente define qué información se preserva durante el compactado automático. Los datos críticos son:

1. PROJECT_ROOT: ruta del proyecto analizado
2. Nombre de la aplicación (`<App>`) y tecnología identificada
3. Mapa completo de módulos con clasificación (Épica/Historia) y estado (pendiente/completado/en curso)
4. Fase actual del análisis (0-Descubrimiento, 1-General, 2-Detalle, 3-Historia específica)
5. Modo de generación elegido (Resumen/Completo)
6. Historias ya aprobadas y sus nombres de fichero generados
7. Historias pendientes de documentar
8. Tabla de dudas acumulada hasta el momento
9. Última historia analizada y su estado de aprobación
10. Decisiones del usuario sobre descomposición de épicas
11. Correcciones o ajustes solicitados por el usuario que afecten a historias futuras

La memoria de sesión (`/memories/session/`) actúa como red de seguridad adicional: persiste fuera de la ventana de contexto y nunca se pierde aunque se compacte agresivamente.
