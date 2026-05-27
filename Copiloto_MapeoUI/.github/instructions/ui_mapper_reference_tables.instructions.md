---
applyTo: "**"
description: "Tablas de deteccion de frameworks, compatibilidad de herramientas de testing, convenciones de nomenclatura y mapeos tecnicos. Esencial para Step 0 (discovery) y Step 1 (screens)."
---
# Tablas de Referencia Consolidadas - UI Mapper

## Objetivo

Este fichero centraliza todas las tablas de compatibilidad de frameworks, convenciones de nomenclatura y mapeos tecnicos reutilizados en multiples steps del copiloto UI Mapper. Los prompts y otros ficheros de instrucciones referencian este documento para evitar duplicacion.

---

## 1. TABLA DE DETECCION DE FRAMEWORKS

### Modo Estatico (analisis de codigo fuente)

| Dependencia encontrada en package.json/pubspec.yaml | Framework detectado | Extensiones de ficheros | Donde buscar rutas |
|-----------------------------------------------------|---------------------|------------------------|-------------------|
| `react`, `react-dom` | React | `.jsx`, `.tsx` | `App.jsx`, routers, `Route` |
| `next` | Next.js (React) | `.jsx`, `.tsx` | `/pages/`, `/app/`, `createBrowserRouter` |
| `@angular/core` | Angular | `.html` (template) + `.ts` | `app-routing.module.ts`, `Routes[]` |
| `vue` | Vue.js | `.vue` (SFC) | `router/index.js`, `routes[]` |
| `@ionic/angular` o `@ionic/react` | Ionic | `.html` + `.ts` o `.jsx` | `app-routing.module.ts` |
| `react-native` | React Native | `.tsx` con componentes RN | `navigation/`, `Stack.Screen` |
| (pubspec.yaml con `flutter`) | Flutter | `.dart` | `GoRouter`, `MaterialApp routes` |
| `nuxt` | Nuxt.js (Vue) | `.vue` | `/pages/`, `router/index.js` |

### Modo Dinamico (inferencia desde DOM)

| Patron detectado en DOM | Framework inferido |
|-------------------------|-------------------|
| Atributos `ng-`, `data-ng-` | Angular |
| Script `__NEXT_DATA__` | Next.js |
| Atributo `data-reactroot` | React |
| Atributo `data-v-` | Vue |
| Sin patrones reconocibles | HTML generico |

---

## 2. ATRIBUTOS DE TESTING POR FRAMEWORK

| Framework | Atributo de testing recomendado | Sintaxis en codigo | Alternativa |
|-----------|---------------------------------|-------------------|-------------|
| React | `data-testid` | `<button data-testid="login-btn-submit">` | `data-cy`, `data-test` |
| Angular | `data-testid` | `<button data-testid="login-btn-submit">` | `id`, `#templateRef` |
| Vue | `data-testid` | `<button data-testid="login-btn-submit">` | `data-cy` |
| React Native | `testID` (prop nativa) | `<Button testID="login-btn-submit" />` | `accessibilityLabel` |
| Flutter | `Key(value)` | `Button(key: Key('login-btn-submit'))` | `Semantics(label:)` |
| Ionic | `data-testid` | `<ion-button data-testid="login-btn-submit">` | `id`, atributos ion-* |

---

## 3. CONVENCION DE NOMENCLATURA DE IDENTIFICADORES

### Formato de IDs de elementos (kebab-case)

**Formato:** `[pantalla]-[tipo]-[descripcion]`

**Ejemplos:**
- `login-btn-submit`: boton de submit en la pantalla de login
- `profile-input-email`: campo email en la pantalla de perfil
- `home-link-dashboard`: enlace al dashboard en la pantalla home
- `products-select-category`: selector de categoria en la pantalla de productos

**Reglas:**
- Solo minusculas y guiones
- Sin articulos ni preposiciones
- Maximo 5 palabras
- Siempre comenzar por el nombre de la pantalla

### Formato de constantes de locators (UPPER_SNAKE_CASE)

**Formato:** `[PANTALLA]_[TIPO]_[DESCRIPCION]`

**Ejemplos:**
- `LOGIN_BTN_SUBMIT`
- `PROFILE_INPUT_EMAIL`
- `HOME_LINK_DASHBOARD`

### Tabla de abreviaturas de tipo

| Tipo completo | Abreviatura para ID | Sufijo para constante |
|---------------|---------------------|----------------------|
| Input texto | `input` | `INPUT` |
| Input password | `input` | `INPUT` |
| Input email | `input` | `INPUT` |
| Input numero | `input` | `INPUT` |
| Button / Boton | `btn` | `BTN` |
| Link / Enlace | `link` | `LINK` |
| Select / Dropdown | `select` | `SELECT` |
| Checkbox | `chk` | `CHK` |
| Radio button | `radio` | `RADIO` |
| Toggle / Switch | `toggle` | `TOGGLE` |
| Textarea | `textarea` | `TEXTAREA` |
| Mensaje de estado | `label` | `LABEL` |
| Contenedor de lista | `container` | `CONTAINER` |
| Item de lista (patron) | `item` | `ITEM` |
| Modal trigger | `btn` | `BTN` |

---

## 4. SINTAXIS DE SELECTORES POR FRAMEWORK DE TESTING

### Playwright (JavaScript/TypeScript)

| Nivel | Tipo de selector | Sintaxis |
|-------|-----------------|----------|
| 1 | data-testid | `page.locator('[data-testid="login-btn-submit"]')` |
| 2 | id | `page.locator('#username')` |
| 3 | name | `page.locator('[name="username"]')` |
| 4 | aria-label | `page.locator('[aria-label="Cerrar sesion"]')` |
| 5 | role + texto | `page.getByRole('button', { name: 'Iniciar sesion' })` |
| 6 | CSS funcional | `page.locator('.btn-login-submit')` |
| 7 | XPath contextual | `page.locator('//form[@id="login"]//button')` |

### Cypress (JavaScript)

| Nivel | Tipo de selector | Sintaxis |
|-------|-----------------|----------|
| 1 | data-testid | `cy.get('[data-testid="login-btn-submit"]')` |
| 2 | id | `cy.get('#username')` |
| 3 | name | `cy.get('[name="username"]')` |
| 4 | aria-label | `cy.get('[aria-label="Cerrar sesion"]')` |
| 5 | role + texto | `cy.contains('button', 'Iniciar sesion')` |
| 6 | CSS funcional | `cy.get('.btn-login-submit')` |
| 7 | XPath contextual | `cy.xpath('//form[@id="login"]//button')` |

### Appium (Android - UiSelector)

| Nivel | Tipo de selector | Sintaxis |
|-------|-----------------|----------|
| 1 | testID (content-desc) | `new UiSelector().description("login-btn-submit")` |
| 2 | resource-id | `new UiSelector().resourceId("com.app:id/username")` |
| 3 | content-desc semantico | `new UiSelector().description("Campo de usuario")` |
| 5 | texto visible | `new UiSelector().text("Iniciar sesion")` |

### Selenium (Java)

| Nivel | Tipo de selector | Sintaxis |
|-------|-----------------|----------|
| 1 | data-testid | `By.cssSelector("[data-testid='login-btn-submit']")` |
| 2 | id | `By.id("username")` |
| 3 | name | `By.name("username")` |
| 4 | aria-label | `By.cssSelector("[aria-label='Cerrar sesion']")` |
| 6 | CSS funcional | `By.className("btn-login-submit")` |
| 7 | XPath | `By.xpath("//form[@id='login']//button")` |

---

## 5. PATRONES FRAGILES AUTOMATICAMENTE DETECTADOS (REGEX)

```regex
# IDs generados automaticamente (rechazar como Nivel 2)
^(mat-|ng-|p-|react-select-|v-select-)[0-9]

# Clases de utilidad (rechazar como Nivel 6)
^(mt-|mb-|pt-|pb-|px-|py-|flex|grid|text-|bg-|border-)[a-z0-9]

# Clases de Bootstrap genericas (rechazar como Nivel 6)
^(col-|row|container|btn$|form-control$|card$)

# XPath posicional (marcar como fragil en Nivel 7-8)
\[\d+\]
```

---

## 6. CLASIFICACION DE COMPLEJIDAD DE PANTALLAS

| Clasificacion | Criterio | Impacto en el Flujo |
|---------------|----------|---------------------|
| **Simple** | Menos de 10 elementos interactivos, sin formularios complejos | Procesada en un unico ciclo Steps 2-3-4 |
| **Compleja** | 10-30 elementos interactivos, formularios con validaciones | Puede requerir subdivision por secciones |
| **Modulo** | Mas de 30 elementos o multiples sub-vistas dentro de la misma ruta | Se divide en sub-pantallas antes de procesar |

### Condiciones automaticas de subdivision

Una pantalla se subdivide automaticamente si:
- Contiene pestanas (tabs) con contenidos independientes (cada tab = sub-pantalla)
- Contiene un wizard / stepper multi-paso (cada paso = sub-pantalla)
- Contiene secciones colapsables con mas de 5 elementos cada una (cada seccion = sub-pantalla)

---

## 7. TAXONOMIA DE ELEMENTOS INTERACTIVOS

### Elementos de Formulario

| Tipo | Identificadores comunes | Notas |
|------|------------------------|-------|
| Input texto | `<input type="text">`, `TextField`, `TextInput` | Incluir placeholders y labels asociados |
| Input password | `<input type="password">`, `PasswordField` | Anotar si tiene toggle de visibilidad |
| Input email | `<input type="email">` | |
| Input numero | `<input type="number">`, `NumberInput` | |
| Textarea | `<textarea>`, `TextArea` | |
| Select / Dropdown | `<select>`, `Dropdown`, `Picker` | Catalogar opciones si son estaticas |
| Checkbox | `<input type="checkbox">`, `Checkbox` | |
| Radio button | `<input type="radio">`, `RadioButton` | |
| Toggle / Switch | `<input type="checkbox" role="switch">`, `Switch` | |

### Elementos de Accion

| Tipo | Identificadores comunes | Notas |
|------|------------------------|-------|
| Boton primario | `<button>`, `Button`, `ElevatedButton` | Accion principal de la pantalla |
| Boton secundario | `<button type="button">`, `OutlinedButton` | |
| Boton icono | `<button>` con solo icono | Anotar el aria-label o tooltip |
| Enlace de navegacion | `<a>`, `Link`, `RouterLink` | |
| FAB (Floating Action Button) | `FloatingActionButton`, `<button class="fab">` | |

### Elementos de Navegacion

| Tipo | Notas |
|------|-------|
| Tab bar / Navigation tabs | Cada tab es un elemento independiente |
| Menu lateral (drawer) | Cada item del menu es un elemento independiente |
| Breadcrumb | Cada nivel es un elemento independiente si es clickable |

---

## 8. RESPUESTAS ESTANDAR PARA CASOS EXCEPCIONALES

| Escenario excepcional | Codigo de mensaje | Respuesta estandar del agente |
|-----------------------|-------------------|------------------------------|
| Framework no reconocido en package.json | `WARN_FRAMEWORK_UNKNOWN` | "ADVERTENCIA: No he podido detectar el framework de forma automatica. Procedere en modo HTML generico. Esto puede limitar la precision de los selectores. Â¿Puedes confirmar manualmente el framework (React/Angular/Vue/Flutter/React Native/Otro)?" |
| URL inaccesible en modo dinamico | `ERROR_URL_UNREACHABLE` | "ERROR: La URL proporcionada no responde o no es accesible. Verifica que: 1) La aplicacion esta en ejecucion, 2) La URL es correcta, 3) No hay restricciones de CORS o red. Â¿Deseas reintentar o cambiar a modo Estatico (codigo fuente)?" |
| Codigo ofuscado/minificado | `WARN_CODE_OBFUSCATED` | "ADVERTENCIA: Detectado codigo ofuscado o minificado. Los selectores generados seran mayoritariamente Nivel 7-8 (fragiles). RECOMENDACIÃ“N: Solicita el codigo fuente original del proyecto para obtener selectores estables. Â¿Deseas continuar con el codigo ofuscado o tienes acceso al codigo fuente?" |
| Pantalla sin elementos interactivos | `WARN_NO_INTERACTIVE_ELEMENTS` | "ADVERTENCIA: No se han detectado elementos interactivos en esta pantalla. Verifica que: 1) La pantalla esta completamente cargada, 2) No requiere autenticacion previa, 3) No es una pantalla de solo lectura. Â¿Deseas continuar con la siguiente pantalla?" |
| Conflicto de IDs duplicados entre pantallas | `ERROR_DUPLICATE_IDS` | "ERROR: Detectado conflicto de IDs. El identificador '[ID]' ya existe en la pantalla '[pantalla-previa]'. Opciones: 1) Renombrar a '[ID-propuesta-1]', 2) Renombrar a '[ID-propuesta-2]', 3) Especificar manualmente." |
| Todos los selectores de un elemento son Nivel 7-8 | `WARN_ALL_SELECTORS_FRAGILE` | "ADVERTENCIA: El elemento '[elemento]' solo dispone de selectores fragiles (Nivel 7-8). RECOMENDACIÃ“N PRIORITARIA: Agregar data-testid='[propuesta]' al elemento en el codigo fuente. Â¿Deseas documentar esta recomendacion como prioritaria?" |
| UI tree capturado pertenece a package incorrecto | `ERROR_WRONG_PACKAGE` | "ERROR: El UI tree capturado pertenece al package '[package-capturado]', no al package objetivo '[package-esperado]'. Verifica que: 1) La app esta en primer plano (foreground) antes de capturar, 2) No hay overlays del sistema (Play Store, notificaciones, launchers) cubriendo la pantalla. Accion correctiva: ejecutar `adb shell am force-stop [package-overlay]` y reintentar la captura." |
| Credenciales de produccion detectadas | `WARN_PROD_CREDENTIALS` | "ADVERTENCIA: Las credenciales proporcionadas parecen pertenecer a un entorno de produccion. Por seguridad, el copiloto solo debe operar con credenciales de entornos de pruebas (staging, dev, QA). Por favor, proporciona credenciales de un entorno de pruebas dedicado. Si no dispones de ellas, las pantallas que requieran autenticacion se marcaran como 'pendiente - requiere autenticacion'." |

---

## 9. TABLA DE LANDMARKS DE DETECCION DE PANTALLA ACTIVA (MODO DINAMICO MOVIL)

En modo dinamico con Appium, usar esta tabla para identificar en que pantalla se encuentra la app ANTES de capturar el UI tree. Verificar la presencia de los resource-ids landmark antes de ejecutar la captura.

### Procedimiento de verificacion de pantalla activa

1. Capturar source XML del dispositivo: `driver.getPageSource()`
2. Comprobar presencia de los resource-ids landmark en orden de precedencia
3. Si no se identifica la pantalla: esperar 2s y reintentar (max 3 intentos)
4. Si tras 3 intentos el package raiz no coincide con el objetivo: emitir `ERROR_WRONG_PACKAGE`

### Formato de la tabla de landmarks por proyecto

El agente construye esta tabla al inicio del Step 1 para cada proyecto analizado en modo dinamico movil, usando los datos descubiertos durante el Step 0:

| Pantalla esperada | Resource-id landmark (presente) | Resource-id landmark (ausente para distinguir) | Condicion adicional |
|------------------|--------------------------------|-----------------------------------------------|---------------------|
| Welcome / Onboarding | `btnRegister` | `tfEmail` | package raiz = appPackage objetivo |
| Login | `tfEmail` Y `tfPassword` | `btnRecoveryPassword` | package raiz = appPackage objetivo |
| RecoverPassword | `btnRecoveryPassword` | `tfPassword` | package raiz = appPackage objetivo |
| [Pantalla N] | [resource-id unico de esa pantalla] | [resource-id que excluye otras pantallas] | package raiz = appPackage objetivo |

**Regla critica:** Si el package raiz del XML capturado NO coincide con el appPackage objetivo â†’ emitir `ERROR_WRONG_PACKAGE` ANTES de analizar cualquier elemento.

### Ejemplo de verificacion pre-captura (pseudocodigo Node.js / Appium)

```javascript
async function verificarPantallaActiva(driver, appPackage, landmarkId, screenName) {
  const source = await driver.getPageSource();
  const rootPackage = extraerPackageRaiz(source);
  if (rootPackage !== appPackage) {
    throw new Error(`ERROR_WRONG_PACKAGE: capturado ${rootPackage}, esperado ${appPackage}`);
  }
  if (!source.includes(`resource-id="${landmarkId}"`)) {
    throw new Error(`Pantalla activa no es ${screenName}. Landmark '${landmarkId}' no encontrado.`);
  }
  return true;
}
```

---

## Uso de este fichero

Los ficheros de instrucciones y prompts deben referenciar estas tablas con el formato:

```
[Aplicar la deteccion de frameworks segun la tabla de referencia: ui_mapper_reference_tables.instructions.md seccion 1]
```

En lugar de duplicar el contenido literal de las tablas.

