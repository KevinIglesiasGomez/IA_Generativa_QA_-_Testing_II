---
agent: "ui_mapper"
tools: ["search", "read/readFile"]
description: "Step 3: Evaluacion de identificadores disponibles por elemento, aplicacion de jerarquia de robustez (data-testid > ARIA > ID > class), construccion de matriz de selectores con fallbacks y deteccion de duplicados cross-pantalla"
model: "Claude Sonnet 4.6"
---

# Step 3: Extraccion y Priorizacion de Selectores

## 0. ARQUITECTURA COGNITIVA INTERNA

### ROL A: Evaluador de Disponibilidad
**Objetivo:** Detectar todos los identificadores disponibles por elemento.
- Revisar atributos del catalogo Step 2 | Determinar cuales son utilizables como selectores | Distinguir estaticos vs dinamicos

### ROL B: Clasificador de Robustez
**Objetivo:** Aplicar jerarquia de 8 niveles de `ui_mapper_selectors.instructions.md`.
- Evaluar cada atributo segun criterios de validez | Asignar nivel de robustez | Construir ranking de selectores

### ROL C: Generador de Selectores
**Objetivo:** Construir sintaxis exacta para el framework de testing destino.
- Generar sintaxis correcta (referencia: `ui_mapper_reference_tables.instructions.md` seccion 4) | Selector primario + fallbacks

### ROL D: Detector de Fragilidad
**Objetivo:** Identificar y documentar selectores problematicos.
- Aplicar patrones fragiles (seccion 5 de reference tables) | Marcar flag fragile | Generar recomendaciones

---

## 1. PREREQUISITOS

El Step 2 debe estar completado con:
- Catalogo de elementos aprobado por el usuario
- Todos los atributos disponibles registrados por elemento

---

## 2. INSTRUCCIONES DEL STEP

Este step se ejecuta para la misma pantalla que el Step 2 acabado de completar.

### Fase 0 - Cruce con Registro Global de IDs (ejecutar ANTES de la evaluacion de atributos)

**Obligatorio antes de generar cualquier selector:**

1. Extraer todos los identificadores (resource-id, id, data-testid, accessibilityLabel) encontrados en el catalogo del Step 2 para la pantalla actual
2. Comparar con el **registro global de IDs** acumulado en sesion (elemento 11 del contexto preservado)
3. Para cada colision detectada:
   - Marcar el elemento como `fragile: true` en la matriz de selectores
   - Escalar recomendacion a prioridad ALTA
   - Incluir en el campo `recommendation` una propuesta de renombrado con prefijo de pantalla
   - Ejemplo: `tfEmail` (duplicado en Login y RecoverPassword) â†’ proponer `tfLoginEmail` y `tfRecoverEmail`
4. Actualizar el registro global con los IDs de la pantalla actual (incluso si no hay colisiones)
5. Si se detectan >= 3 colisiones en una misma pantalla: emitir `ERROR_DUPLICATE_IDS` del catalogo de mensajes

**Criterio de colision:** Mismo valor de identificador en >= 2 pantallas distintas ya procesadas O en la pantalla actual vs. cualquier pantalla anterior.

### Fase 1 - Evaluacion de atributos por elemento

Para cada elemento del catalogo, evaluar en orden los siguientes atributos:

**Verificacion de Nivel 1** (data-testid, data-cy, data-test, testID, Key):
- Existe alguno de estos atributos?
- El valor es descriptivo (no numerico, no hash, no generado)?
- Si Si y Si: selector primario Nivel 1

**Verificacion de Nivel 2** (id):
- Existe atributo `id`?
- El valor NO coincide con patrones de IDs generados?
- El valor describe la funcion del elemento?
- El ID es unico en el documento?

**Verificacion de Nivel 3** (name - solo para formularios):
- El elemento es un input, select, textarea o button submit?
- Existe atributo `name`?
- El valor es semantico y no generado?

**Verificacion de Nivel 4** (aria-label, aria-labelledby):
- Existe `aria-label` con valor descriptivo?
- O existe `aria-labelledby` que referencia a un elemento con texto claro?

**Verificacion de Nivel 5** (role + texto visible):
- El elemento tiene un role semantico (button, link, checkbox, combobox, etc.)?
- El texto visible es estable (no dinamico, no dependiente de i18n)?

**Verificacion de Nivel 6** (clase CSS funcional):
- Existe al menos una clase CSS cuyo nombre describe la funcion del elemento?
- La clase NO es una clase de utilidad (Tailwind, Bootstrap genericas)?
- La clase permite identificar univocamente el elemento en el contexto de la pantalla?

**Verificacion de Nivel 7** (XPath contextual):
- Existe algun atributo estable en un antecesor directo que permita anclar el XPath?
- El XPath relativo tiene menos de 5 niveles de profundidad?

**Verificacion de Nivel 8** (XPath absoluto):
- Generado siempre como ultimo fallback
- Marcado automaticamente como FRAGIL

### Fase 2 - Construccion de la matriz de selectores

Para cada elemento, generar:

```
Selector primario:    [selector del nivel mas alto disponible y valido]
Nivel primario:       [1-8]
Selector fallback 1:  [siguiente nivel disponible]
Nivel fallback 1:     [1-8]
Selector fallback 2:  [solo si fallback 1 es nivel 6 o inferior]
Fragil:               [true/false]
```

### Fase 3 - Generacion de sintaxis por framework de testing

Aplicar la sintaxis segun el framework destino confirmado en Step 0.

**Referencia:** `ui_mapper_reference_tables.instructions.md` seccion 4 (Sintaxis de selectores por framework)

---

## 3. SALIDA ESPERADA

### EJEMPLO COMPLETO (continuacion de pantalla Login del Step 2 - framework Playwright)

**Entrada:** Catalogo de elementos del Step 2 con 6 elementos (login-input-username, login-input-password, etc.)

**Salida del Step 3:**

```
## Matriz de Selectores - Login

**Framework de testing destino**: Playwright

| # | Elemento | Selector Primario | Nivel | Selector Fallback 1 | Nivel F1 | Fragil | Observacion |
|---|----------|------------------|-------|---------------------|----------|--------|-------------|
| 1 | login-input-username | [data-testid="login-input-username"] | 1 | [name="username"] | 3 | No | |
| 2 | login-input-password | [data-testid="login-input-password"] | 1 | [name="password"] | 3 | No | |
| 3 | login-btn-submit | [data-testid="login-btn-submit"] | 1 | button[type="submit"] | 6 | No | |
| 4 | login-link-forgot | a[href="/forgot-password"] | 6 | //a[text()="Olvidaste tu contrasena?"] | 7 | Si | Sin data-testid. Ver recomendacion #1 |
| 5 | login-label-error | .login-error | 6 | [role="alert"] | 4 | Si | Ver recomendacion #2 |
| 6 | login-chk-remember | #remember-me | 2 | [name="rememberMe"] | 3 | No | ID semantico valido |

### Selectores fragiles detectados

| # | Elemento | Motivo | Recomendacion |
|---|---------|--------|---------------|
| 1 | login-link-forgot | Solo disponible via href o texto visible. El texto puede cambiar. | Agregar `data-testid="login-link-forgot-password"` |
| 2 | login-label-error | Clase CSS es fragil ante refactors de estilos. | Agregar `data-testid="login-label-error"` |

### Resumen de cobertura por nivel

| Nivel | Elementos | % |
|-------|-----------|---|
| Nivel 1 (data-testid) | 3 | 50% |
| Nivel 2 (id semantico) | 1 | 17% |
| Nivel 3 (name) | 0 | 0% |
| Nivel 4 (aria) | 0 | 0% |
| Nivel 6 (CSS funcional) | 2 | 33% |
| **Total fragiles** | **2** | **33%** |

---

Confirma si la matriz de selectores es correcta para avanzar al Step 4: Normalizacion.
```

### FORMATO PARA TU PANTALLA ACTUAL

```
## Matriz de Selectores - [Nombre de la Pantalla]

**Framework de testing destino**: [playwright | cypress | appium | selenium]

| # | Elemento | Selector Primario | Nivel | Selector Fallback 1 | Nivel F1 | Fragil | Observacion |
|---|----------|------------------|-------|---------------------|----------|--------|-------------|

---

## 4. PREREQUISITOS PARA AVANZAR AL STEP 4

- La matriz de selectores esta aprobada por el usuario
- Todos los elementos tienen al menos un selector (aunque sea Nivel 8)
- Los selectores fragiles estan documentados con sus recomendaciones
- El usuario conoce los elementos sin identificadores estables

