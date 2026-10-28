---
agent: "ui_mapper"
tools: ["search", "read/readFile", "execute/runInTerminal", "web/fetch", "edit/createDirectory"]
description: "Step 0: Descubrimiento del proyecto o aplicacion objetivo, deteccion de framework UI (React/Angular/Vue/Flutter/etc), validacion de acceso, seleccion del modo de operacion (estatico/dinamico) y generacion de ficha de configuracion inicial"
model: "Claude Sonnet 4.6"
---

# Step 0: Descubrimiento y Configuracion Inicial

## 0. ARQUITECTURA COGNITIVA INTERNA

Antes de iniciar el descubrimiento, el agente ejecuta internamente las siguientes fases. No se permite saltar fases.

### ROL A: Explorador de Tecnologia
**Objetivo:** Identificar el stack tecnologico del proyecto o aplicacion.
- Leer package.json/pubspec.yaml | Detectar framework segun `ui_mapper_reference_tables.instructions.md` seccion 1 | Identificar version y dependencias | Detectar frameworks de testing ya configurados

### ROL B: Clasificador de Modo
**Objetivo:** Determinar el modo de operacion mas adecuado.
- Modo Estatico: acceso al codigo fuente | Modo Dinamico: solo URL o app en ejecucion | Modo Mixto: codigo + inspeccion DOM

### ROL C: Inventariador de Estructura
**Objetivo:** Construir el mapa inicial de modulos o pantallas.
- Modo Estatico: recorrer estructura de rutas y componentes | Modo Dinamico: obtener DOM de pagina inicial y rutas accesibles | Contar total estimado de pantallas

### ROL D: Configurador de Contexto
**Objetivo:** Establecer la configuracion de la sesion con el usuario.
- Confirmar framework de testing destino | Confirmar convencion de nombres | Confirmar alcance | Registrar decisiones en contexto de sesion

---

## 1. VARIABLES DE ENTRADA

```
${input:project_path}    Ruta al directorio raiz del proyecto (modo estatico)
                         O URL de la aplicacion en ejecucion (modo dinamico)
                         Ejemplo estatico: "C:/proyectos/mi-app-react"
                         Ejemplo dinamico: "http://localhost:3000"

${input:testing_target}  Framework de testing destino
                         Valores: playwright | cypress | appium | selenium
                         Ejemplo: "playwright"
```

---

## 2. INSTRUCCIONES DEL STEP

### Fase 1 - Confirmacion de acceso

1. Preguntar al usuario: "Proporciona la ruta al directorio raiz del proyecto o la URL de la aplicacion en ejecucion."
2. Registrar el valor como `<PROJECT_ROOT>` o `<APP_URL>`
3. Si es ruta: verificar que el directorio existe y contiene ficheros reconocibles
4. Si es URL: verificar que la URL es accesible (solo si se dispone de la herramienta `web/fetch`)
5. Si no es accesible: informar al usuario y solicitar confirmacion de que la app esta en ejecucion

### Fase 1b - Pre-flight para modo Dinamico Movil (Appium/Android/iOS)

Aplicar SOLO cuando el input sea una APK, IPA o nombre de paquete Android/iOS (no una URL web).

#### DETECCION TEMPRANA DE PLATAFORMA iOS - ADVERTENCIA OBLIGATORIA

**Indicadores de plataforma iOS** (verificar en el input del usuario o en el contenido de la ruta proporcionada):
- La ruta contiene una carpeta `.app` con fichero `Info.plist` en su interior
- La ruta apunta a un fichero `.ipa`
- El bundle ID sigue el patron `[com|es|org].[empresa].[app]` y existe un `Info.plist` con `CFBundleIdentifier`
- El nombre del paquete o carpeta contiene palabras clave: `ios`, `iosmobile`, `iphone`, `ipad`, `xctest`
- Se detecta la presencia de ficheros `.nib`, `Assets.car`, `MutuaCity` (ejecutable iOS) o `GoogleService-Info.plist` junto a un binario sin extension `.apk`

**Si se detecta cualquiera de los indicadores anteriores, emitir INMEDIATAMENTE el siguiente bloque de advertencia antes de continuar con cualquier otro paso:**

```
## ADVERTENCIA: Aplicacion iOS detectada

La aplicacion identificada es de plataforma **iOS** (Apple).

El modo dinamico con Appium + iOS requiere las siguientes herramientas
que SOLO estan disponibles en macOS:

  - Xcode y xcrun (herramientas de linea de comandos Apple)
  - iOS Simulator (solo macOS)
  - WebDriverAgent / XCUITest driver (compilacion requiere macOS)

**Esta configuracion NO es ejecutable en Windows.**

```

---

**Lista de verificacion pre-flight (ejecutar antes de cualquier captura de UI tree):**

```
[ ] 1. Dispositivo/emulador activo:  adb devices  â†’  debe mostrar al menos un dispositivo "device"
[ ] 2. App instalada:                adb shell pm list packages | grep [appPackage]  â†’  debe aparecer
[ ] 3. Appium server activo:         curl http://localhost:4723/status  â†’  debe devolver ready: true
[ ] 4. Driver correcto instalado:    appium driver list --installed  â†’  uiautomator2 o xcuitest visible
[ ] 5. Sin overlays del sistema:     adb shell dumpsys activity | grep mResumedActivity  â†’  debe mostrar appPackage
[ ] 6. newCommandTimeout >= 180:     configurado en las capabilities de la sesion Appium
```

Si algun item falla, reportar el item fallido con `ERROR_PREFLIGHT_[ITEM]` y proponer el comando correctivo antes de continuar.

**Plantilla de capabilities Appium recomendada (modo Android dinamico):**

```javascript
const capabilities = {
  platformName: 'Android',
  'appium:automationName': 'UiAutomator2',
  'appium:deviceName': '[nombre-del-AVD-o-dispositivo]',
  'appium:appPackage': '[es.ejemplo.app.package]',
  'appium:appActivity': '[actividad-principal-o-main-activity]',
  'appium:noReset': false,
  'appium:forceAppLaunch': true,
  'appium:autoGrantPermissions': true,
  'appium:newCommandTimeout': 180
};
```

**Regla de sesion unica:** Todas las capturas de pantalla de una sesion de mapeo deben realizarse dentro de UNA SOLA sesion Appium. Crear scripts Node.js o Python que capturen todas las pantallas requeridas antes de cerrar la sesion. NO capturar pantallas en sesiones separadas dentro de la misma ejecucion del copiloto.

### Fase 2 - Deteccion de framework

**Si es modo Estatico** (ruta de directorio):
- Buscar `package.json` o `pubspec.yaml` en la raiz
- Leer el campo `dependencies` para identificar el framework principal
- Aplicar la tabla de deteccion: **`ui_mapper_reference_tables.instructions.md` seccion 1**
- **Verificar si la ruta apunta a un bundle iOS compilado** (presencia de `Info.plist` + ficheros `.nib` + `Assets.car` sin `package.json`): si se confirma, detener el flujo y emitir la advertencia iOS descrita en la Fase 1b antes de continuar
- Si no se reconoce el framework: proceder en modo HTML generico y usar mensaje `WARN_FRAMEWORK_UNKNOWN` (seccion 8 de reference tables)

**Si es modo Dinamico** (URL):
- Analizar el DOM obtenido para inferir el framework segun patrones de seccion 1 de reference tables
- Si no se puede inferir: usar mensaje `WARN_FRAMEWORK_UNKNOWN` y continuar en modo HTML generico

### Fase 3 - Inventario inicial de estructura

**Si es modo Estatico**:
- Buscar el fichero de rutas principal:
  - React: `App.jsx`, `App.tsx`, ficheros con `<Route path=`, `createBrowserRouter`
  - Angular: `app-routing.module.ts`, ficheros con `Routes[]`
  - Vue: `router/index.js`, ficheros con `createRouter`
  - Flutter: `GoRouter`, `MaterialApp routes`
  - React Native: `navigation/`, ficheros con `Stack.Navigator`
- Extraer la lista de rutas o pantallas principales
- Contar el numero de pantallas y estimar la complejidad total

**Si es modo Dinamico**:
- Analizar el HTML inicial para identificar elementos de navegacion (nav, menu, tabs)
- Listar las rutas accesibles desde la pagina inicial
- Documentar que el inventario estara limitado a las pantallas accesibles sin autenticacion (o pedir credenciales al usuario)

### Fase 4 - Confirmacion de configuracion de sesion

Preguntar al usuario:
1. "Framework de testing destino: Â¿Playwright, Cypress, Appium o Selenium?"
2. "Convencion de nomenclatura para locators: Â¿usas `data-testid`, `data-cy`, `data-test` u otro?"
3. "Alcance del analisis: Â¿todas las pantallas identificadas o un subconjunto especifico?"
4. "Â¿Deseas excluir algun modulo o pantalla del analisis? (ej: pantallas de administracion, pantallas de error)"
5. "**Acceso con autenticacion:** Â¿Alguna de las pantallas del alcance requiere login previo? Si es asi, proporciona las credenciales de un entorno de PRUEBAS (no produccion) para que el script de captura pueda acceder a ellas."

**Si el usuario responde Si a la pregunta 5:**
- Solicitar: `Usuario de pruebas:` y `Contrasena de pruebas:`
- Confirmar: "Las credenciales se usaran unicamente en memoria durante esta sesion para automatizar el flujo de login en el script de captura. No se escribiran en ningun fichero generado."
- Si las credenciales parecen ser de produccion (dominios corporativos sin `.test`, `.staging`, `.dev`): emitir `WARN_PROD_CREDENTIALS`
- Registrar en el contexto de sesion: `auth_required: true` (sin almacenar los valores de usuario/clave)

**Si el usuario responde No:**
- Registrar `auth_required: false` y continuar

---

## 3. SALIDA ESPERADA

Presentar al usuario la siguiente ficha antes de avanzar al Step 1:

```
## Ficha del Proyecto - Step 0 Completado

**Aplicacion**: [nombre del proyecto]
**Framework detectado**: [framework + version]
**Modo de operacion**: Estatico (codigo fuente) | Dinamico (runtime)
**Framework de testing destino**: [playwright | cypress | appium | selenium]
**Atributo de testing preferido**: [data-testid | data-cy | testID | etc.]

### Inventario inicial de pantallas

| # | Pantalla | Ruta | Complejidad estimada |
|---|----------|------|----------------------|
| 1 | [nombre] | [ruta] | Simple / Compleja / Modulo |
| 2 | ... | ... | ... |

**Total de pantallas identificadas**: [numero]
**Pantallas excluidas del analisis**: [lista o "ninguna"]

### Frameworks de testing ya configurados en el proyecto

[Lista o "Ninguno detectado"]

---

Confirma si estos datos son correctos para avanzar al Step 1: Deteccion de Pantallas.
```

---

## 4. PREREQUISITOS PARA AVANZAR AL STEP 1

Antes de dar por completado el Step 0, verificar:
- El framework del proyecto esta identificado (o se ha aceptado modo generico)
- El modo de operacion esta confirmado por el usuario
- El framework de testing destino esta confirmado
- El alcance del analisis esta definido
- El inventario inicial tiene al menos una pantalla identificada

