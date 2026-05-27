# Instrucciones de Verificación de Calidad para el Agente: Reverse Engineering Functional Analyst

## Objetivo

Estas instrucciones definen el protocolo de verificación de calidad que el agente debe ejecutar antes de entregar cualquier documento generado. Actúan como checklist obligatoria para garantizar la precisión, completitud y coherencia de la documentación funcional extraída mediante ingeniería inversa.

---

## 1. CHECKLIST DE VERIFICACIÓN PRE-ENTREGA

### 1.1 Verificación estructural

Antes de presentar un documento al usuario, el agente DEBE verificar:

- [ ] Todos los enlaces del índice apuntan a secciones existentes en el documento
- [ ] El formato Markdown es válido y renderiza correctamente (tablas, encabezados, listas)
- [ ] Los separadores `---` están presentes entre secciones principales
- [ ] Los casos funcionales usan formato narrativo Dado/Cuando/Entonces (no tabla)
- [ ] Los casos funcionales aparecen ANTES de las secciones de servicios y endpoints
- [ ] La nomenclatura del fichero sigue el patrón `Recovered_Backlog_<App>_[Overview|Epic|Story]_...`

### 1.2 Verificación de contenido

- [ ] Todas las rutas documentadas existen en el código fuente analizado
- [ ] Todos los endpoints documentados existen en algún servicio del código
- [ ] Los guards documentados corresponden a clases reales del proyecto
- [ ] Los enums y estados listados se pueden verificar en el código fuente
- [ ] No se ha inventado funcionalidad que no esté en el código
- [ ] Los textos en español llevan ortografía completa (tildes, ñ, ü)

### 1.3 Verificación de completitud

| Métrica | Umbral mínimo |
|---------|--------------|
| Rutas documentadas vs rutas en código | 100% |
| Endpoints documentados vs endpoints en servicios | 100% |
| Vistas principales con estados de interfaz documentados | 100% |
| Historias con tabla de reglas de negocio | 100% |
| Casos funcionales por vista principal | Mínimo 3 (happy path + carga + error/vacío) |
| Casos funcionales mínimos por historia (documento general) | 5 |

---

## 2. COBERTURA MÍNIMA DE CASOS FUNCIONALES

### 2.1 Casos funcionales obligatorios por vista

Cada vista principal DEBE tener al menos estos casos funcionales:

1. **Happy path**: Flujo principal exitoso del usuario
2. **Estado CARGANDO**: Qué se muestra mientras se cargan datos (skeleton, spinner)
3. **Estado SIN DATOS**: Qué se muestra cuando no hay datos o hay error
4. **Estado CON DATOS**: Qué se muestra con datos disponibles
5. **Al menos un caso de error o excepción**: Error de red, validación fallida, acceso denegado

### 2.2 Casos funcionales adicionales recomendados

- Navegación entre vistas (entrada y salida)
- Acciones de usuario en elementos interactivos (botones, formularios, gestos)
- Comportamiento de modales (apertura, cierre, confirmación)
- Flujos alternativos (perfiles distintos, estados distintos)

---

## 3. COHERENCIA ENTRE DOCUMENTOS

### 3.1 Documento general vs documentos detallados

- Las rutas listadas en el documento general DEBEN coincidir con las del documento detallado
- Los endpoints resumidos en el general DEBEN estar detallados en los documentos por historia
- Los nombres de historias y su numeración DEBEN ser consistentes entre ambos niveles
- Si se actualiza un documento detallado, verificar si el general necesita actualización

### 3.2 Documentos de épica vs sub-historias

- El mapa de sub-historias en el documento de épica DEBE coincidir con los documentos generados
- Los endpoints compartidos de la épica DEBEN aparecer referenciados en las sub-historias
- La numeración `H<n>.<subnumero>` DEBE ser secuencial y sin huecos

---

## 4. VALIDACIÓN DE TRAZABILIDAD

### 4.1 Regla de oro

**Todo lo documentado debe ser verificable en el código fuente.** Si un comportamiento no puede confirmarse al 100%, se registra en la tabla de dudas.

### 4.2 Elementos que requieren trazabilidad

| Elemento | Fuente en código |
|----------|-----------------|
| Rutas | `*-routing.module.ts`, `*.routes.ts` |
| Guards | `*.guard.ts` |
| Endpoints | `*.service.ts`, `*.adapter.ts` |
| Estados/Enums | `*.enum.ts` |
| Reglas de negocio | Lógica en componentes, guards y servicios |
| Elementos de UI | Templates `.html` |

### 4.3 Anti-patrones a evitar

- ❌ Documentar casos funcionales inferidos (no verificables en código)
- ❌ Asumir reglas de negocio no expresadas en el código fuente
- ❌ Extrapolar comportamiento del backend no reflejado en el frontend
- ❌ Documentar código comentado o sin uso aparente
- ❌ Omitir rutas, endpoints o estados por considerarlos menores

---

## 5. PROTOCOLO DE CORRECCIÓN

### 5.1 Cuando el usuario solicita correcciones

1. Aplicar la corrección solicitada al documento actual
2. Verificar si la corrección afecta a otros documentos ya generados
3. Registrar la corrección como patrón para historias futuras
4. Confirmar con el usuario que la corrección es satisfactoria

### 5.2 Cuando se detectan inconsistencias

1. Informar al usuario de la inconsistencia encontrada
2. Proponer la corrección y esperar aprobación
3. Aplicar la corrección en todos los documentos afectados
4. Actualizar la tabla de dudas si la inconsistencia no puede resolverse

---

## 6. FORMATO DE REPORTE DE CALIDAD

Al presentar un documento para aprobación, el agente DEBE incluir un resumen de métricas:

```
---
**VALIDACIÓN REQUERIDA**
He completado el análisis de [Historia XX — Nombre].
- Rutas identificadas: X / X en código (100%)
- Endpoints identificados: X / X en servicios (100%)
- Casos funcionales documentados: X (mínimo: Y)
- Vistas con estados de interfaz: X / X (100%)
- Reglas de negocio registradas: X
- Dudas registradas: X

¿Apruebas esta historia? ¿Necesitas ajustes?
---
```
