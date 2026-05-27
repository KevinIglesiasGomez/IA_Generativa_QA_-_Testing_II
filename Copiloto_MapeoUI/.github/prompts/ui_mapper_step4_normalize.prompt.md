---
agent: "ui_mapper"
tools: ["edit/editFiles", "read/readFile", "search"]
description: "Step 4: Normalizacion de identificadores segun convencion de nombres (camelCase/SCREAMING_SNAKE_CASE), validacion de consistencia semantica cross-pantalla, resolucion de colisiones y generacion del registro normalizado final de selectores"
model: "Claude Sonnet 4.6"
---

# Step 4: Normalizacion de Identificadores

## 0. ARQUITECTURA COGNITIVA INTERNA

### ROL A: Auditor de Convenciones
**Objetivo:** Verificar que todos los IDs y constantes siguen la convencion acordada.
- Aplicar formato kebab-case y UPPER_SNAKE_CASE (referencia: `ui_mapper_reference_tables.instructions.md` seccion 3) | Detectar inconsistencias | Corregir IDs provisionales

### ROL B: Detector de Duplicados y Validador de Consistencia Semantica
**Objetivo:** Garantizar que no hay IDs repetidos ni inconsistencias semanticas entre pantallas.
- Comparar con registro global acumulado | Detectar colisiones de nombres | Detectar elementos equivalentes con nomenclatura divergente | Proponer unificacion

### ROL C: Verificador de Completitud
**Objetivo:** Confirmar que el registro esta completo y sin huecos.
- Verificar todos los elementos tienen selector | Verificar selectores fragiles tienen recomendacion | Verificar elementos condicionales tienen condicion anotada

### ROL D: Acumulador de Registro Global
**Objetivo:** Incorporar el registro al acumulativo de la sesion.
- Fusionar con registro global | Actualizar estadisticas de cobertura | Actualizar contador de fragiles | Verificar pantallas pendientes

---

## 1. PREREQUISITOS

El Step 3 debe estar completado con:
- Matriz de selectores aprobada por el usuario
- Todos los elementos con selector primario y fallbacks definidos
- Selectores fragiles documentados

---

## 2. INSTRUCCIONES DEL STEP

### Fase 1 - Aplicacion de convencion de nombres

Para cada elemento, verificar y corregir si necesario:

**Nombre del identificador (ID del elemento)**:
- Formato: `[nombre-pantalla]-[tipo]-[descripcion]`
- `nombre-pantalla`: nombre corto en kebab-case de la pantalla (ej: `login`, `user-profile`, `product-list`)
- `tipo`: segun la tabla de tipos abreviados del Step 2
- `descripcion`: descripcion funcional breve en kebab-case

Tabla de abreviaturas de tipo:
| Tipo completo | Abreviatura |
|---------------|-------------|
| Input texto | `input` |
| Input password | `input` |
| Button / Boton | `btn` |
| Link / Enlace | `link` |
| Select / Dropdown | `select` |
| Checkbox | `chk` |
| Radio button | `radio` |
| Toggle / Switch | `toggle` |
| Textarea | `textarea` |
| Mensaje de estado | `label` |
| Contenedor de lista | `container` |
| Item de lista (patron) | `item` |
| Modal trigger | `btn` (el que lo abre) |

**Nombre de la constante (para el locator file JavaScript)**:
- Formato: `[PANTALLA]_[TIPO]_[DESCRIPCION]`
- Mismo contenido que el ID del elemento pero en UPPER_SNAKE_CASE
- Ejemplo: `login-btn-submit` â†’ `LOGIN_BTN_SUBMIT`

### Fase 2 - Validacion de consistencia semantica entre pantallas

**Nota:** La deteccion de duplicados literales (colisiones de resource-id/id identicos) se realiza en el Step 3 (Fase 0) antes de generar la matriz de selectores. En este Step 4 solo se ejecuta la validacion de consistencia semantica.

**Validacion de consistencia semantica (Paso 2b):**

Detectar elementos equivalentes con nomenclatura divergente entre pantallas:

- **Caso 1: Mismo elemento funcional, nombres diferentes**
  - Ejemplo detectado: `login-btn-submit` (pantalla Login) vs `auth-button-login` (pantalla Register)
  - Accion: Proponer unificacion a `[pantalla]-btn-submit` en ambas pantallas

- **Caso 2: Elementos de navegacion con patrones inconsistentes**
  - Ejemplo: `home-link-profile` vs `settings-profile-link` (orden invertido)
  - Accion: Proponer patron consistente `[pantalla]-link-[destino]`

- **Caso 3: Abreviaturas inconsistentes**
  - Ejemplo: `user-btn-delete` vs `products-button-remove` (btn vs button)
  - Accion: Unificar a la abreviatura acordada en seccion 3 de reference tables

Si se detectan inconsistencias semanticas:
1. Listar las divergencias encontradas
2. Proponer renombrado para unificar patron
3. Solicitar confirmacion del usuario antes de aplicar cambios al registro global

### Fase 3 - Generacion del registro normalizado de la pantalla

El registro normalizado es la version definitiva que se usara en el Step 5 para generar los artefactos.

Estructura del registro:
```
Registro normalizado: [nombre-pantalla]

  [id-elemento]
    ID:              [nombre-pantalla]-[tipo]-[descripcion]
    Constante:       [PANTALLA_TIPO_DESCRIPCION]
    Tipo:            [tipo completo]
    Descripcion:     [descripcion funcional en espanol]
    Selector primary: [selector exacto]
    Nivel primary:    [1-8]
    Selector fallback: [selector de fallback]
    Nivel fallback:    [1-8]
    Fragil:            [true | false]
    Condicion:         [null | descripcion de cuando es visible]
    Recomendacion:     [null | texto de recomendacion para el equipo de desarrollo]
```

### Fase 4 - Actualizacion del registro global y decision de continuacion

Tras incorporar la pantalla al registro global:
1. Mostrar el resumen del estado global (pantallas procesadas vs. pendientes)
2. Si hay pantallas pendientes: proponer la siguiente pantalla para el ciclo Step 2-3-4
3. Si todas las pantallas del alcance estan procesadas: proponer avanzar al Step 5

---

## 3. SALIDA ESPERADA

### EJEMPLO COMPLETO (continuacion de pantalla Login del Step 3)

**Entrada:** Matriz de selectores del Step 3 con 6 elementos validados

**Salida del Step 4:**

```
## Registro Normalizado - Login

| ID Elemento | Constante | Tipo | Selector Primario | Nivel | Selector Fallback | Fragil | Condicion |
|-------------|-----------|------|------------------|-------|------------------|--------|-----------|
| login-input-username | LOGIN_INPUT_USERNAME | Input texto | [data-testid="login-input-username"] | 1 | [name="username"] | No | - |
| login-input-password | LOGIN_INPUT_PASSWORD | Input password | [data-testid="login-input-password"] | 1 | [name="password"] | No | - |
| login-btn-submit | LOGIN_BTN_SUBMIT | Boton primario | [data-testid="login-btn-submit"] | 1 | button[type="submit"] | No | - |
| login-link-forgot-password | LOGIN_LINK_FORGOT_PASSWORD | Enlace de accion | a[href="/forgot-password"] | 6 | //a[text()="Olvidaste..."] | Si | - |
| login-label-error | LOGIN_LABEL_ERROR | Mensaje de error | .login-error | 6 | [role="alert"] | Si | Solo si hay error de autenticacion |
| login-chk-remember | LOGIN_CHK_REMEMBER | Checkbox | #remember-me | 2 | [name="rememberMe"] | No | - |

### Recomendaciones para el equipo de desarrollo

| # | Elemento | Accion recomendada | Codigo sugerido |
|---|---------|-------------------|----------------|
| 1 | login-link-forgot-password | Agregar data-testid | `<a data-testid="login-link-forgot-password" ...>` |
| 2 | login-label-error | Agregar data-testid | `<div data-testid="login-label-error" ...>` |

### Validacion de consistencia semantica

**Comparacion con pantallas previas del registro global:** (no aplica, es la primera pantalla procesada)

### Estado del registro global

| Pantalla | Estado |
|----------|--------|
| login | Completado |
| home | Pendiente |
| users-list | Pendiente |
| users-detail | Pendiente |
| users-edit | Pendiente |

**Pantallas completadas**: 1 de 5
**Selectores fragiles acumulados**: 2

---

Confirma el registro normalizado.
Siguiente pantalla a procesar: **Home** (volver al Step 2 con esta pantalla).
O escribe "Step 5" si deseas generar los artefactos con las pantallas procesadas hasta ahora.
```

### FORMATO PARA TU PANTALLA ACTUAL

```
## Registro Normalizado - [Nombre de la Pantalla]

| ID Elemento | Constante | Tipo | Selector Primario | Nivel | Selector Fallback | Fragil | Condicion |
|-------------|-----------|------|------------------|-------|------------------|--------|-----------|

---

## 4. PREREQUISITOS PARA AVANZAR AL STEP 5

- Todas las pantallas del alcance estan en estado "Completado" en el registro global
- O el usuario ha decidido generar artefactos parciales con las pantallas ya procesadas
- El registro global no tiene IDs duplicados
- Todos los registros normalizados estan aprobados

