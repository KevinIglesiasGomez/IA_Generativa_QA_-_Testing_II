---
agent: "ui_mapper"
tools: ["search", "read/readFile", "web/fetch"]
description: "Step 2: Analisis profundo de una pantalla individual para identificar y catalogar todos los elementos interactivos (botones, campos, links, tabs) con sus atributos disponibles (id, class, data-*, name, role, text)"
model: "Claude Sonnet 4.6"
---

# Step 2: Mapeo de Elementos UI por Pantalla

## 0. ARQUITECTURA COGNITIVA INTERNA

### ROL A: Lector de Componente
**Objetivo:** Extraer informacion estructural del template HTML/JSX/Vue/Dart.
- Leer template del componente | Identificar estructura jerarquica | Localizar elementos interactivos

### ROL B: Catalogador de Atributos
**Objetivo:** Extraer todos los atributos relevantes por elemento.
- Tipo de elemento | Etiqueta HTML | Atributos: id, name, class, type, aria-*, data-* | Texto visible y label asociado

### ROL C: Detector de Contextos
**Objetivo:** Identificar contextos funcionales que agrupan elementos.
- Formularios y campos | Secciones colapsables | Modales y triggers | Listas/tablas y acciones

### ROL D: Verificador de Completitud
**Objetivo:** Garantizar que no ha quedado ningun elemento interactivo sin catalogar.
- Recorrer template arriba-abajo | Verificar elementos condicionales | Documentar estados de visibilidad

---

## 1. PREREQUISITOS

El Step 1 debe estar completado con:
- Arbol de pantallas aprobado
- Pantalla actual seleccionada para procesar
- Modo de operacion definido

---

## 2. INSTRUCCIONES DEL STEP

Este step se ejecuta para UNA SOLA PANTALLA por iteracion. Al finalizar, el usuario confirma y se repite para la siguiente pantalla.

### Fase 1 - Localizacion del fichero de componente

**Si es modo Estatico**:
- A partir del ID de la pantalla del Step 1, localizar el fichero del componente
- Para Angular: buscar `[nombre].component.html` y `[nombre].component.ts`
- Para React/Next.js: buscar `[Nombre].jsx`, `[Nombre].tsx`, `[Nombre]/index.tsx`
- Para Vue: buscar `[Nombre].vue`
- Para Flutter: buscar el fichero `.dart` que contiene el widget de la pantalla
- Si el componente importa sub-componentes relevantes: leerlos tambien

**Si es modo Dinamico**:
- Capturar el DOM completo de la pantalla activa
- Si la pantalla requiere autenticacion previa:
  - Si `auth_required: true` fue registrado en Step 0: incluir el flujo de login en el script de captura usando las credenciales proporcionadas (en memoria, nunca embebidas en el fichero del script como literales en texto plano; usar variables de entorno o parametros de ejecucion)
  - Si `auth_required: false` o no se proporcionaron credenciales: solicitar al usuario que navegue manualmente a la pantalla autenticada y proporcione el DOM o una captura de pantalla

### Fase 2 - Identificacion de la estructura de la pantalla

Antes de catalogar elementos, documentar la estructura de alto nivel:
- Titulo o nombre visible de la pantalla
- Secciones principales que componen la pantalla
- Si hay formulario: nombre del formulario y su accion
- Si hay tabla o lista: tipo de items de la lista
- Si hay tabs: nombres de los tabs y cuales tienen elementos interactivos propios

### Fase 3 - Catalogacion de elementos

Para CADA elemento interactivo identificado, completar la siguiente ficha:

```
ID provisional:      [nombre-pantalla]-[tipo]-[descripcion-en-kebab-case]
Tipo:                [segun taxonomia de instrucciones principales]
Etiqueta HTML:       [input | button | a | select | textarea | etc.]
Texto visible:       [texto que muestra el elemento, si lo tiene]
Label asociado:      [texto del label si existe]
Contexto:            [formulario, seccion, tabla, modal, etc. donde esta]
Atributos:           [lista completa: id, name, class, type, placeholder, aria-*, data-*]
Visible siempre:     [Si | No - condicion: descripcion de cuando aparece]
Estado inicial:      [enabled | disabled | hidden]
Condicion enable:    [null si siempre activo | descripcion de la condicion de habilitacion]
Estado requerido:    [Si es visible en estado de carga, error, vacio, etc.]
```

### Fase 4 - Documentacion de elementos condicionales

Los elementos que solo son visibles bajo ciertas condiciones deben tener anotado:
- La condicion bajo la que aparecen (ej: "solo cuando el usuario tiene rol Admin")
- El estado de la aplicacion requerido (ej: "solo cuando la lista esta vacia")
- Si el elemento es el mismo en todos los estados o cambia (ej: boton "Guardar" vs "Actualizar")

---

## 3. SALIDA ESPERADA

### EJEMPLO COMPLETO (pantalla Login, aplicacion React)

**Codigo fuente del componente LoginPage.jsx analizado:**
```jsx
function LoginPage() {
  return (
    <div className="login-container">
      <h1>Iniciar Sesion</h1>
      <form id="login-form" onSubmit={handleSubmit}>
        <label htmlFor="username">Usuario</label>
        <input 
          type="text" 
          id="username" 
          name="username" 
          data-testid="login-input-username"
          placeholder="Introduce tu usuario" 
        />
        <label htmlFor="password">Contrasena</label>
        <input 
          type="password" 
          id="password" 
          name="password" 
          data-testid="login-input-password"
        />
        <div className="remember-section">
          <input 
            type="checkbox" 
            id="remember-me" 
            name="rememberMe" 
          />
          <label htmlFor="remember-me">Recuerdame</label>
        </div>
        <button 
          type="submit" 
          className="btn btn-primary login-btn"
          data-testid="login-btn-submit"
        >
          Iniciar sesion
        </button>
      </form>
      <a href="/forgot-password" className="forgot-link">
        Olvidaste tu contrasena?
      </a>
      {error && (
        <div className="error-message login-error" role="alert">
          {error}
        </div>
      )}
    </div>
  );
}
```

**Salida del Step 2 para este ejemplo:**

```
## Catalogo de Elementos - Login

**Pantalla**: Login
**Ruta**: /login
**Componente**: LoginPage.jsx

### Estructura de la pantalla

La pantalla contiene:
- 1 formulario de autenticacion (id="login-form")
- 2 campos de entrada (usuario y contrasena)
- 1 checkbox de recordar sesion
- 1 boton de submit
- 1 enlace a recuperacion de contrasena
- 1 mensaje de error condicional

### Catalogo de elementos interactivos

| # | ID Provisional | Tipo | Etiqueta | Texto / Label | Atributos relevantes | Contexto | Visible |
|---|----------------|------|----------|---------------|---------------------|----------|---------|
| 1 | login-input-username | Input texto | input | "Usuario" | type="text", name="username", id="username", data-testid="login-input-username", placeholder="Introduce tu usuario" | Formulario de login | Siempre |
| 2 | login-input-password | Input password | input | "Contrasena" | type="password", name="password", id="password", data-testid="login-input-password" | Formulario de login | Siempre |
| 3 | login-btn-submit | Boton primario | button | "Iniciar sesion" | type="submit", class="btn btn-primary login-btn", data-testid="login-btn-submit" | Formulario de login | Siempre |
| 4 | login-link-forgot | Enlace de accion | a | "Olvidaste tu contrasena?" | href="/forgot-password", class="forgot-link" | Debajo del formulario | Siempre |
| 5 | login-label-error | Mensaje de error | div | (dinamico) | class="error-message login-error", role="alert" | Encima del boton | Solo si hay error |
| 6 | login-chk-remember | Checkbox | input | "Recuerdame" | type="checkbox", name="rememberMe", id="remember-me" | Formulario de login | Siempre |

### Elementos condicionales

| # | Elemento | Condicion de Visibilidad |
|---|----------|--------------------------|
| 5 | login-label-error | Visible cuando el servidor devuelve un error de autenticacion |

### Resumen

**Total de elementos catalogados**: 6
**Elementos condicionales**: 1
**Formularios identificados**: 1 (login-form)
**Modales en esta pantalla**: 0

---

Confirma si el catalogo es correcto y completo para avanzar al Step 3 con esta pantalla.
```

### FORMATO PARA TU PANTALLA ACTUAL

```
## Catalogo de Elementos - [Nombre de la Pantalla]

**Pantalla**: [nombre]
**Ruta**: [ruta]
**Componente**: [nombre del fichero del componente]

### Estructura de la pantalla

[Descripcion de la estructura de alto nivel]

### Catalogo de elementos interactivos

| # | ID Provisional | Tipo | Etiqueta | Texto / Label | Atributos relevantes | Contexto | Visible |
|---|----------------|------|----------|---------------|---------------------|----------|---------|

---

## 4. PREREQUISITOS PARA AVANZAR AL STEP 3

- El catalogo de elementos esta aprobado por el usuario
- Todos los elementos interactivos de la pantalla estan catalogados
- Los elementos condicionales estan documentados con su condicion
- El usuario ha confirmado que no falta ningun elemento relevante

