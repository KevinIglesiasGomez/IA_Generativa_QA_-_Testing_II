---
agent: "agent"
tools:
  [
    "edit/editFiles",
    "search",
    "microsoft/playwright-mcp/*",
    "runCommands",
    "usages",
  ]
description: "Generar Pruebas de Playwright"
---

# Prompt: Generar Pruebas de Playwright

## 1. PREREQUISITOS Y CONTEXTO

### 1.1 Archivos de Instrucciones Requeridos

**FUENTE TÉCNICA DE VERDAD**: Este prompt requiere seguir TODAS las instrucciones definidas en:

- **`playwright_tests.instructions.md`**: Contiene TODOS los patrones de prueba, arquitectura de gestión de navegador, requisitos de seguridad y guías de implementación.

**CRÍTICO**: El archivo `playwright_tests.instructions.md` es la ÚNICA fuente de verdad para:

- Patrón Browser Factory (uso obligatorio)
- Arquitectura de gestión de navegador
- Page Object Model (POM) sin herencia
- Requisitos de seguridad
- Mejores prácticas de pruebas
- Patrones de contexto compartido

### 1.2 Variables de Entrada

- **${input:feature_name}**: Nombre del archivo de característica BDD a implementar
- **${input:project_bdd}**: Carpeta que contiene los archivos .feature existentes
- **${input:playwright_folder}**: Carpeta del framework de Playwright existente
- **${input:JSP_folder}**: Carpeta que contiene páginas JSP o HTML estáticas para referencia

### 1.3 Contexto del Proyecto

Lee este prompt completo antes de las instrucciones. Tu tarea es generar **pruebas automatizadas de Playwright** basadas en el **escenario de característica BDD** llamado **${input:feature_name}** ubicado en la carpeta: **${input:project_bdd}**, lee y analiza SOLO este archivo de característica completamente. Todos los pasos descritos en la característica Gherkin BDD **${input:feature_name}** deben implementarse como archivos .js dentro de la carpeta src/pages con src/steps correspondientes.

**IMPORTANTE**: Este framework usa **Cucumber como el ejecutor principal de pruebas**. Toda ejecución de pruebas se realiza a través de comandos de Cucumber (cucumber-js), no comandos de Playwright directamente. Playwright se usa internamente por las definiciones de pasos para automatización del navegador.

## 2. RESTRICCIONES CRÍTICAS

- Usar la estructura del framework de Playwright y archivos de configuración existentes en **${input:playwright_folder}**
- Analizar Pages previas (src/pages) y definiciones de pasos previas (src/steps) para código reutilizable
- **OBLIGATORIO: Usar el Patrón Browser Factory existente** - Nunca crear instancias de navegador directas
- **NUNCA crear inicialización de navegador duplicada** - Usar el contexto de navegador existente de `this.page`
- **NO agregar hooks Before/After** para gestión de navegador en archivos de pasos específicos de características
- **Los archivos de pasos de características deben SOLO usar `this.page`** del contexto compartido, nunca inicializar navegadores
- **Aprovechar browserFactory.js existente** para patrones de gestión de navegador consistentes

## 3. CONFIGURACIÓN DEL PROYECTO

### 3.1 Recursos de Desarrollo

- Revisar las **páginas JSP o HTML estáticas** disponibles en **${input:JSP_folder}** para obtener información sobre la estructura y comportamiento de la aplicación. Si en este directorio hay un **README**, leelo completamente para conocer detalles de la navegación inicial.
- El framework de pruebas debe seguir estrictamente el diseño **Page Object Model (POM)**
- La ejecución de pruebas se realiza vía comandos de Cucumber (cucumber-js), con Playwright usado internamente para automatización del navegador
- Revisar los archivos existentes en la carpeta **${input:playwright_folder}** para entender cómo funcionan las páginas (src/pages) y pasos (src/steps)
- Aplicar TODOS los requisitos de seguridad de `playwright_tests.instructions.md` para configuración de variables de entorno

## 4. PATRÓN DE ARQUITECTURA DE GESTIÓN DE NAVEGADOR

**REGLAS CRÍTICAS**:

1. **Patrón Browser Factory**: Siempre usar browserFactory.js existente para gestión de navegador - Nunca crear instancias directas
2. **Instancia Única de Navegador**: Solo UN archivo de pasos (típicamente `autenticacion.steps.js`) debe inicializar y gestionar el ciclo de vida del navegador usando Browser Factory
3. **Contexto Compartido**: Todos los archivos de pasos específicos de características deben usar `this.page` del contexto compartido de Cucumber
4. **Patrón Page Object**:

   ```javascript
   // ✅ CORRECT - Feature step file
   const BrowserFactory = require("../support/browserFactory"); // Reference existing factory
   let myPage;
   Given("some step", async function () {
     if (!myPage) {
       myPage = new MyPage(this.page); // Use shared context
     }
   });

   // ❌ WRONG - Never do this in feature step files
   Before(async function () {
     browser = await chromium.launch(); // Creates duplicate browser
   });

   // ❌ WRONG - Direct browser creation
   const browser = await chromium.launch();

   // ✅ CORRECT - Use Browser Factory (only in main step file)
   const browser = await BrowserFactory.createBrowser();
   ```

5. **No Hooks Duplicados**: Los archivos de pasos específicos de características NO deben tener hooks Before/After para gestión de navegador
6. **Patrón de Inicialización**: Inicializar Page Objects dentro de definiciones de pasos usando parámetro `this.page` solamente
7. **Soporte Multi-Navegador**: Aprovechar Browser Factory existente para capacidades de pruebas cross-browser

## 5. ORDEN DE IMPLEMENTACIÓN

1. **PRIMERO: Revisar archivos de pasos existentes** para entender el patrón de gestión de navegador (típicamente en autenticacion.steps.js)
2. **IDENTIFICAR el patrón de contexto compartido** - Cómo `this.page` se proporciona a las definiciones de pasos
3. Analizar el archivo de características proporcionado **${input:feature_name}** para comprender completamente los requisitos y alcance de las pruebas
4. Revisar **SOLO las páginas JSP o HTML estáticas relevantes** ubicadas en **${input:JSP_folder}** para recopilar información sobre la estructura de la aplicación, localizadores de elementos y comportamiento. Leer cualquier README disponible en esta carpeta para obtener detalles de navegación inicial.
5. **Crear Page Objects que acepten el parámetro `this.page`** - Nunca inicializar navegadores dentro de Page Objects
6. **Crear definiciones de pasos usando contexto compartido** - Inicializar Page Objects con `this.page` solamente
7. **Trabajar estrictamente un escenario a la vez**. 
8. Crear un solo escenario, ejecutarlo y **confirmar que funciona correctamente antes de proceder**. No debes crear o pasar al siguiente escenario hasta que este esté completamente funcional. 
9. Para ejecutar un escenario específico, asegurate que estas en el directorio correcto y usa el comando de cucumber: 
`cucumber-js --config cucumber.config.js src/features/Login.feature`
10. Repetir este proceso para cada escenario restante en el archivo de características hasta que todos estén implementados y validados exitosamente

## 6. OBJETIVOS

- Implementar **todos los pasos** de escenarios BDD usando definiciones de pasos de **Cucumber.js**
- Seguir estrictamente el patrón **Page Object Model (POM)**
- **OBLIGATORIO: Usar el Patrón Browser Factory existente** - Nunca crear instancias de navegador directas
- Asegurar que las pruebas cubran **todas las funcionalidades BDD descritas**
- Crear automatización de pruebas robusta y mantenible
- Implementar **manejo de errores** apropiado y **estrategias de espera**
- **CRÍTICO: Implementar mejores prácticas de seguridad** - NO credenciales codificadas, URLs o datos sensibles
- Usar variables de entorno para toda configuración e información sensible
- **SEGUIR patrones de gestión de navegador establecidos** - Usar solo contexto compartido `this.page`
- **APROVECHAR capacidades multi-navegador** - Las pruebas deben funcionar en chromium, firefox y webkit
- **EVITAR instancias de navegador duplicadas** - Los archivos de pasos de características nunca deben inicializar navegadores
- **MANTENER compatibilidad cross-browser** - Todos los Page Objects deben funcionar con el patrón Browser Factory

## 7. REGLAS DE IMPLEMENTACIÓN

1. Usar las **instrucciones de pruebas de Playwright** para implementar las pruebas en la carpeta existente **${input:playwright_folder}**
2. Implementar todo el código generado exclusivamente dentro de esta carpeta
3. Almacenar **todas las salidas y archivos de prueba generados** en esta carpeta
4. **Toda documentación, archivos README, comentarios y texto orientado al usuario deben estar escritos en español**
5. **REQUISITO DE SEGURIDAD**: **Nunca codificar información sensible** como URLs, nombres de usuario, contraseñas o datos específicos del entorno en ningún archivo de configuración. Siempre usar variables de entorno con `process.env` y proporcionar valores predeterminados sensatos
6. **Incluir documentación de seguridad apropiada** en README explicando cómo configurar variables de entorno de forma segura
7. **REQUISITO DE ETIQUETADO**: **Marcar escenarios no implementados con `@pendiente`** a nivel individual de cada escenario, nunca solo a nivel de Característica

## 8. VALIDACIÓN

### 8.1 Lista de Verificación

- **No instancias de navegador duplicadas**: Solo un navegador debe abrirse durante la ejecución de pruebas
- **No hooks Before/After** en archivos de pasos específicos de características para gestión de navegador
- **Los Page Objects reciben parámetro `this.page`**, nunca inicializan sus propios navegadores
- **Las definiciones de pasos usan contexto compartido**: `this.page` viene del contexto global
- **No datos sensibles codificados**: Todas las URLs, credenciales usan variables de entorno
- **Escenarios no implementados marcados con `@pendiente`**: A nivel individual de cada escenario
- **Ejecución de escenario único**: Probar un escenario completamente antes de pasar al siguiente

### 8.2 Objetivo de Calidad Final

Producir scripts de prueba de Playwright de alta calidad y mantenibles que:

- Implementen los escenarios Gherkin de **${input:feature_name}**
- Se adhieran al patrón de diseño Page Object Model
- Se integren sin problemas con la estructura del framework de Playwright en **${input:playwright_folder}**
- Automaticen correctamente la navegación e interacciones usando las referencias JSP de **${input:JSP_folder}**
- **Usen variables de entorno para toda configuración sensible** (URLs, credenciales, timeouts)
- **Incluyan medidas de seguridad apropiadas** para prevenir información sensible codificada
- **Proporcionen documentación clara** para configuración segura de entorno
- **Sigan la arquitectura de gestión de navegador establecida** para prevenir conflictos e instancias duplicadas
