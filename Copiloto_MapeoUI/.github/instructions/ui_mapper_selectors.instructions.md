---
applyTo: "**"
description: "Jerarquia de robustez y priorizacion de selectores para elementos UI. Aplicar en Step 3 (extraccion) y Step 4 (normalizacion) del flujo UI Mapper."
---
# Instrucciones de Selectores y Jerarquia de Robustez

## Objetivo

Estas instrucciones definen la jerarquia de evaluacion y priorizacion de selectores para elementos de interfaz. El agente debe aplicar estas reglas de forma sistematica en el Step 3 (Extraccion de Selectores) y el Step 4 (Normalizacion).

---

## 1. JERARQUIA DE ROBUSTEZ DE SELECTORES

Los selectores se evaluan en este orden estricto. El primer selector disponible y valido en el nivel mas alto de la jerarquia se convierte en el selector primario.

### Nivel 1 - Maxima estabilidad: Atributos de Testing Dedicados

**Criterio**: El elemento tiene un atributo definido explicitamente para testing.

| Atributo | Ecosistemas | Ejemplo |
|----------|------------|---------|
| `data-testid` | React, Angular, Vue, HTML generico | `[data-testid="login-submit-button"]` |
| `data-cy` | Cypress, cualquier framework | `[data-cy="username-input"]` |
| `data-test` | Variante generica | `[data-test="password-field"]` |
| `testID` | React Native (prop nativa) | No aplica CSS; se usa como prop directa |
| `Key(value)` | Flutter | No aplica CSS; se usa el valor del Key |
| `accessibilityIdentifier` | iOS nativo | No aplica CSS; solo Appium |

Condicion de validez: El valor del atributo es descriptivo (no numerico ni generado automaticamente).

Ejemplos de valores VALIDOS: `"login-submit-btn"`, `"user-email-input"`, `"nav-home-link"`
Ejemplos de valores INVALIDOS: `"btn-1234"`, `"auto-generated-abc9f"`, `"12345"`

### Nivel 2 - Alta estabilidad: ID semantico

**Criterio**: El elemento tiene un atributo `id` con valor descriptivo y no dinamico.

Condiciones de validez:
- El valor no contiene numeros secuenciales generados (ej: `input-3f8a`, `field__1`, `react-12`)
- El valor describe la funcion del elemento (ej: `username`, `email-field`, `submit-btn`)
- El ID no se repite en el mismo documento
- No es generado por un framework UI de forma automatica (Material UI, PrimeNG, etc.)

Firmas de IDs generados automaticamente (INVALIDOS):
- Contienen hashes: `mat-input-4`, `p-inputtext-5`, `ng-select-1`
- Comienzan con el nombre del framework: `react-select-`, `ng-`, `mat-`
- Son puramente numericos o alfanumericos sin semantica

Sintaxis: `#username`, `#submit-btn`, `#email-field`

### Nivel 3 - Alta estabilidad: Atributo name en formularios

**Criterio**: El elemento de formulario tiene el atributo `name` con valor descriptivo.

Valido solo para: `<input>`, `<select>`, `<textarea>`, `<button type="submit">`

Condiciones de validez:
- El valor es semantico y describe el campo (ej: `username`, `password`, `country`)
- No es generado dinamicamente por un form builder
- Coincide con el nombre del campo en el modelo de datos

Sintaxis en Playwright: `[name="username"]`
Sintaxis en Appium: `android.widget.EditText` con filtro por `content-desc`

### Nivel 4 - Alta estabilidad: Atributos ARIA

**Criterio**: El elemento tiene atributos de accesibilidad semanticos.

| Atributo | Uso | Ejemplo |
|----------|-----|---------|
| `aria-label` | Describe el elemento sin texto visible | `[aria-label="Cerrar sesion"]` |
| `aria-labelledby` | Referencia a otro elemento que lo labela | Usar el texto del label referenciado |
| `role` con texto | Elemento con rol ARIA explicito | `[role="button"][aria-label="Guardar"]` |

Condiciones de validez:
- El valor de `aria-label` es descriptivo y en el idioma de la aplicacion
- El valor no cambiara con cambios de idioma si la app tiene i18n (considerar nivel 5 como alternativa)

### Nivel 5 - Media-Alta estabilidad: Combinacion role + texto visible

**Criterio**: El elemento tiene un rol implicito o explicito combinado con texto visible estable.

Valido cuando: Los niveles 1-4 no estan disponibles y el texto del elemento es fijo (no dinamico).

Sintaxis en Playwright: `page.getByRole('button', { name: 'Iniciar sesion' })`
Sintaxis en Cypress: `cy.contains('button', 'Iniciar sesion')`

Restricciones:
- No usar si el texto es dinamico (cambia segun el estado de la app)
- No usar si la app tiene soporte de multiples idiomas (i18n) y el texto cambia
- Solo aplicable a elementos con roles semanticos: button, link, checkbox, radio, combobox, textbox

### Nivel 6 - Media estabilidad: Clase CSS funcional

**Criterio**: El elemento tiene una clase CSS cuyo nombre describe su funcion, no su apariencia.

Condiciones de validez estrictas:
- La clase describe la funcion del elemento: `.btn-submit`, `.nav-logo`, `.user-menu-toggle`
- La clase NO describe apariencia: NO usar `.text-red`, `.mt-4`, `.flex`, `.p-2`
- La clase NO es una clase de framework UI generica: NO usar `.btn`, `.form-control`, `.input`
- La clase es unica en el contexto de la pantalla o combinada con otro selector estable

Sintaxis: `.btn-login-submit`, `form.login-form .btn-submit`

### Nivel 7 - Media-Baja estabilidad: XPath contextual

**Criterio**: No hay identificadores en niveles superiores disponibles, pero la estructura del DOM es estable.

XPath contextual acepta:
- Rutas relativas al contenedor padre con ID o data-testid: `//form[@id="login-form"]//button[@type="submit"]`
- Uso de texto: `//button[text()="Guardar"]` (solo si el texto es fijo)
- Combinacion de atributo y posicion relativa al padre inmediato

XPath contextual rechaza:
- Rutas basadas en posicion absoluta: `//div[3]/div[1]/button[2]`
- Rutas con mas de 5 niveles de profundidad
- Rutas que incluyen clases de layout (grid, flex, container)

### Nivel 8 - Minima estabilidad: XPath absoluto

**Criterio**: Ultimo recurso. Se genera unicamente como fallback documentado y marcado como FRAGIL.

Siempre acompanado de:
- Advertencia de fragilidad
- Recomendacion al equipo de desarrollo para agregar un atributo de testing

## 2. VALIDACION SEMANTICA DE IDENTIFICADORES ANTES DE ASIGNAR NIVEL

Antes de asignar el nivel de robustez, aplicar estas validaciones sobre el valor del identificador:

### Tabla de validacion semantica

| Patron del valor | Clasificacion | Accion |
|-----------------|--------------|--------|
| Longitud <= 4 caracteres (ej: `ico`, `btn`, `lbl`) | Generico | Reducir a nivel 7, marcar FRAGIL |
| `0_resource_name_obfuscated` | Ofuscado | Descartar, usar nivel siguiente |
| Coincide con `/^(android\|com\.android)/` | Sistema | Ignorar completamente |
| Coincide con `/^(mat-\|ng-\|p-\|react-select-)[0-9]/` | Generado por framework | Invalido para nivel 1-2 |
| Valor descriptivo >= 5 chars sin numeros de hash | Semantico | Nivel valido segun tipo |
| Prefijo funcional + nombre descriptivo (ej: `btnLogin`, `tfEmail`) | Semantico | Nivel 2 valido |

### Aplicacion en modo Android/Appium

Para `resource-id` en apps Android:
- Formato tipico valido: `es.mma.app/btnLogin` o simplemente `btnLogin`
- **Criterio de genericidad:** si la parte tras el `/` (o el valor completo) tiene <= 4 chars o no describe funcion â†’ nivel 7
- **Criterio de duplicidad:** si el mismo resource-id aparece en >= 2 pantallas ya procesadas â†’ escalar prioridad de recomendacion a ALTA y marcar en el registro global

### Deteccion temprana de duplicados (aplicar en Step 3, no en Step 4)

**ANTES** de generar la matriz de selectores de una pantalla:
1. Extraer todos los resource-id / id encontrados en la pantalla actual
2. Cruzar con el **registro global de IDs** acumulado en la sesion
3. Para cada colision detectada:
   - Marcar ambas ocurrencias como `fragile: true`
   - Escalar recomendacion a prioridad ALTA
   - Incluir propuesta de renombrado en el campo `recommendation`
4. Actualizar el registro global con los IDs de la pantalla actual

---

## 3. ESTRATEGIA DE SELECCION DE SELECTOR PRIMARIO Y FALLBACK

Para cada elemento, el agente genera:

```
Selector primario:   El selector del nivel mas alto disponible
Selector fallback 1: El siguiente nivel disponible
Selector fallback 2: Opcional, solo si el fallback 1 es nivel 6 o inferior
```

### Ejemplo de aplicacion

Elemento: boton "Iniciar sesion" en un formulario de login React

Analisis disponible:
- `data-testid="login-submit-btn"` â†’ Nivel 1 DISPONIBLE
- `id="btn-login"` â†’ Nivel 2, pero el id es `btn-login` (podria ser valido)
- `type="submit"` â†’ No es un selector semantico
- Texto visible: "Iniciar sesion" â†’ Nivel 5 disponible

Resultado:
```
Selector primario:   [data-testid="login-submit-btn"]     (Nivel 1)
Selector fallback 1: #btn-login                           (Nivel 2)
Selector fallback 2: button[type="submit"]                (Nivel 6 - fragil, documentado)
```

### Selector de contexto para IDs duplicados (modo Android/Appium)

Cuando un `resource-id` aparece en multiples pantallas, el selector primario debe incluir un contenedor diferenciador:

```
// En lugar de: id=tfEmail   (ambiguo entre pantallas)
// Usar:
//android.view.View[@resource-id='inputEmail']//android.widget.EditText[@resource-id='tfEmail']
// El contenedor padre (inputEmail, inputPassword, etc.) es diferente por pantalla â†’ anade contexto sin XPath absoluto
```

### Campo enabled_state en locators de elementos con estado

Para botones o elementos que pueden estar deshabilitados condicionalmente, registrar su estado inicial y la condicion de habilitacion:

```json
{
  "name": "btn-submit",
  "initial_state": "disabled",
  "enabled_condition": "todos los campos requeridos tienen valor valido",
  "selectors": { ... }
}
```

---

## 4. DETECCION DE SELECTORES FRAGILES

Un selector se clasifica como FRAGIL cuando:

| Condicion de Fragilidad | Accion del Agente |
|-------------------------|-------------------|
| Solo dispone de XPath absoluto o posicional | Marcar FRAGIL + recomendar data-testid |
| El ID es numerico o contiene hash | Rechazar como selector primario |
| La clase CSS es solo de estilos (Tailwind, Bootstrap utils) | Rechazar como selector |
| El texto visible puede cambiar con i18n | Marcar FRAGIL si se usa como selector primario |
| El elemento no tiene ningun atributo estable | Marcar FRAGIL + escalar a usuario |
| El selector depende de la posicion (`:nth-child`, `[1]`) | Marcar FRAGIL |

### Catalogo de patrones fragiles automaticamente detectados

```
Patrones rechazados (regex):
  IDs generados:         ^(mat-|ng-|p-|react-select-|v-select-)[0-9]
  Clases de utilidad:    ^(mt-|mb-|pt-|pb-|px-|py-|flex|grid|text-|bg-|border-)[a-z0-9]
  Clases de Bootstrap:   ^(col-|row|container|btn$|form-control$|card$)
  XPath posicional:      \[\d+\]  (cuando no hay contexto estable)
```

---

## 4. RECOMENDACIONES PARA EL EQUIPO DE DESARROLLO

Cuando un elemento no dispone de selector de nivel 1-3, el agente genera una recomendacion para el equipo de desarrollo.

### Formato de recomendacion

```
Elemento:         [descripcion funcional del elemento]
Pantalla:         [nombre de la pantalla]
Selector actual:  [selector fragil generado como fallback]
Problema:         [descripcion del por que es fragil]
Recomendacion:    Agregar el atributo data-testid="[nombre-sugerido]" al elemento
Codigo sugerido:  <button data-testid="[nombre-sugerido]" ...>
```

### Convencion de nombres para data-testid recomendados

Formato: `[pantalla]-[tipo-elemento]-[descripcion]`

Ejemplos:
- `login-btn-submit`: boton de submit en la pantalla de login
- `profile-input-email`: campo email en la pantalla de perfil
- `home-link-dashboard`: enlace al dashboard en la pantalla home
- `products-select-category`: selector de categoria en la pantalla de productos

Reglas:
- Solo minusculas y guiones
- Sin articulos ni preposiciones
- Maximo 5 palabras
- Siempre comenzar por el nombre de la pantalla

---

## 5. REGLAS ESPECIALES POR TIPO DE ELEMENTO

### Inputs dentro de formularios

- Priorizar el `name` (Nivel 3) cuando el `id` parece generado
- Si hay un `<label>` asociado via `for`/`htmlFor`, usar el texto del label para el nombre del locator
- Si el input es parte de un componente de libreria UI (Material, Ant Design, Primeng), buscar el input HTML nativo subyacente

### Botones de iconos (sin texto visible)

- Obligatorio tener `aria-label` o `title`
- Sin `aria-label` â†’ marcar como FRAGIL y generar recomendacion de accesibilidad
- Usar el `aria-label` como selector Nivel 4 y para nombrar el locator

### Elementos de lista o tabla (filas clickables)

- No generar un selector para cada fila dinamica
- Generar el selector del contenedor de la lista y el patron del item
- Ejemplo: `[data-testid="product-list"] [data-testid="product-item"]`

### Modales y dialogos

- El trigger que abre el modal: selector normal segun jerarquia
- El contenedor del modal: identificar el wrapper con `role="dialog"` o similar
- Los elementos dentro del modal: prefijar con el contexto del modal

### Dropdowns/Selects personalizados

- Identificar tanto el trigger (elemento clickable) como el contenedor de opciones
- Las opciones individuales: generar el patron del selector de opcion, no uno por opcion

