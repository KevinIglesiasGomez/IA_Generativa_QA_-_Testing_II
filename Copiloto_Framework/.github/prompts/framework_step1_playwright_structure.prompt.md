---
agent: 'qa_framework-setup'
tools: ['edit/createDirectory', "edit/editFiles", "runCommands", "search", "search/searchResults", "usages", edit/createFile]
description: "Generar Estructura de Playwright"
---

# Prompt: Generar Estructura de Playwright

## 1. PREREQUISITOS Y CONTEXTO

### 1.1 Archivos de Instrucciones Requeridos
**FUENTE TÉCNICA DE VERDAD**: Este prompt requiere seguir TODAS las instrucciones definidas en:
- **`playwright_structure.instructions.md`**: Contiene TODA la documentación técnica, patrones arquitectónicos, requisitos de seguridad y guías de implementación.

**CRÍTICO**: El archivo `playwright_structure.instructions.md` es la ÚNICA fuente de verdad para:
- Estructura de carpetas y archivos
- Patrones de arquitectura (Browser Factory, Page Object Model)
- Configuración de Cucumber y Playwright
- Requisitos de seguridad
- Plantillas de código
- Mejores prácticas

**RESTRICCIÓN DE ALCANCE**: Este prompt genera SOLO la estructura del framework, NO implementaciones BDD reales.

### 1.2 Variables de Entrada
- **${input:playwright_folder}**: Nombre de la carpeta del proyecto
- **${input:project_bdd}**: Carpeta que contiene archivos .feature existentes
- **${input:environment_url}**: URL base para entorno de pruebas
- **${input:username}**: Nombre(s) de usuario para configuración de ejemplo (puede ser un solo usuario o múltiples usuarios separados por coma)
- **${input:password}**: Contraseña(s) para configuración de ejemplo (puede ser una sola contraseña o múltiples contraseñas separadas por coma, correspondientes a los nombres de usuario)
- **${input:role}**: Rol(es) para usuarios (opcional - puede ser un solo rol, múltiples roles separados por coma, o vacío si no se requieren roles)

### 1.3 Contexto del Proyecto
Lee este prompt completo antes de las instrucciones. Tu tarea es generar **SOLO la estructura base del framework automatizado de Playwright**.

**IMPORTANTE**: Este framework usa **Cucumber como el ÚNICO ejecutor de pruebas**. 

**Jerarquía de Flujo de Ejecución:**
1. El usuario ejecuta comando npm: Llama a cucumber-js (NUNCA playwright directamente)
2. Cucumber lee archivos .feature: Analiza escenarios Gherkin  
3. Cucumber ejecuta definiciones de pasos: Traduce Gherkin a acciones JavaScript
4. Las definiciones de pasos usan Page Objects: Pasan el contexto compartido `this.page`
5. Los Page Objects llaman a Playwright: Realizan automatización del navegador internamente
6. Browser Factory gestiona el ciclo de vida: Creación/limpieza centralizada del navegador
7. Cucumber genera reportes: Reportes JSON/HTML (NO reportes de Playwright)

**CRÍTICO**: Playwright se usa SOLO internamente por Page Objects, NUNCA llamado directamente por usuarios o scripts npm.

## 2. OBJETIVOS Y RESTRICCIONES CRÍTICAS

### 2.1 Objetivo Principal
Generar **SOLO la estructura base del framework automatizado de Playwright**. NO crear pruebas reales, escenarios o implementaciones específicas de aplicación.

### 2.2 Prohibiciones Explícitas
Consultar `playwright_structure.instructions.md` sección 2 para restricciones completas. Resumen:

- **SOLO archivos de ejemplo únicos**: NO crear pruebas reales o código específico de aplicación
- **SOLO copiar archivos .feature**: NO leer, analizar o crear implementaciones basadas en ellos
- **NO páginas específicas**: NO crear LoginPage.js, HomePage.js, o clases de página específicas
- **NO pasos específicos**: NO crear LoginSteps.js, HomeSteps.js, o archivos de definición de pasos específicos

### 2.3 Requisitos Críticos de Arquitectura
**Patrón Browser Factory (OBLIGATORIO)**:
- Implementar `src/support/browserFactory.js` para gestión centralizada del navegador
- Solo UN archivo (`common.steps.js`) gestiona el ciclo de vida del navegador con hooks Before/After
- Todos los archivos de pasos usan `this.page` del contexto compartido
- Soporte multi-navegador: chromium, firefox, webkit

**Configuración de Cucumber (MEJORADA)**:
- Carga escalable de pasos: patrón `'src/steps/**/*.js'`
- Generación única de reportes: nomenclatura basada en timestamp
- Creación automática de directorios: screenshots, videos, JSON, HTML
- Retroalimentación post-ejecución: manejador con ubicaciones de reportes

**Separación de Configuración (CRÍTICO)**:
- `playwright.config.js` NO USADO: Existe SOLO para prevenir errores de dependencias
- `browserFactory.js` GESTIONA NAVEGADORES: Toda la lógica de creación y opciones de lanzamiento
- `environmentLoader.js` REQUERIDO`: Carga centralizada de configuración de entorno

## 3. CONFIGURACIÓN DEL PROYECTO

### 3.1 Información de Entorno
- Seguir TODAS las guías de contexto y recursos definidas en `playwright_structure.instructions.md`
- La URL base del proyecto en Entorno de Pruebas es **${input:environment_url}**
- Puedes usar esta URL para verificar el comportamiento y estructura de la aplicación
- Puedes usar esta URL para verificar localizadores y acciones en la aplicación

### 3.2 Credenciales y URLs
Puede haber una o múltiples credenciales de roles de usuario para la aplicación:
- **Nombre(s) de usuario**: **${input:username}** (configurar vía variables de entorno - puede ser un solo usuario o múltiples usuarios)
- **Contraseña(s)**: **${input:password}** (configurar vía variables de entorno - contraseñas correspondientes para cada nombre de usuario)
- **Rol(es)**: **${input:role}** (opcional - configurar vía variables de entorno - puede ser un solo rol, múltiples roles, o sin roles)

**Nota**: Cuando se proporcionan múltiples usuarios, deben estar separados por coma en las variables de entrada, y el framework debe configurarse para manejar múltiples conjuntos de credenciales para diferentes escenarios de prueba. Los roles son opcionales y pueden o no ser requeridos dependiendo del sistema de autenticación de la aplicación.

### 3.3 Configuración de Seguridad
- **CRÍTICO**: Aplicar TODOS los requisitos de seguridad de `playwright_structure.instructions.md` para configuración de variables de entorno
- **Implementar mejores prácticas de seguridad** usando variables de entorno para toda la configuración

### 3.4 Objetivos del Framework
- Seguir el patrón **Page Object Model (POM)** estrictamente con SOLO UN archivo de ejemplo
- Crear estructura base del framework con archivos de ejemplo únicos para desarrollo futuro de pruebas
- **Implementar Patrón Browser Factory** para gestión multi-navegador centralizada
- **Documentar el patrón de contexto compartido** claramente para uso de `this.page` en archivos de pasos

## 4. REGLAS DE IMPLEMENTACIÓN

### 4.1 Estructura de Carpetas
1. Crear una nueva carpeta en el directorio raíz del workspace llamada **${input:playwright_folder}**
2. Usar las **instrucciones de estructura de Playwright** para configurar la estructura del framework en esta carpeta
3. Implementar todo el código generado exclusivamente dentro de esta nueva carpeta
4. Almacenar **todas las salidas y archivos generados** en esta carpeta

### 4.2 Requisitos de Scripts NPM y Configuración
**CRÍTICO**: Implementar scripts npm mejorados y configuración de cucumber como se define en `playwright_structure.instructions.md`:

**Requisitos Clave:**
- **TODOS los scripts DEBEN usar `--config cucumber.config.js`**: Asegura que la configuración mejorada se cargue
- **cucumber.config.js mejorado**: Usar plantilla validada del archivo de instrucciones
- **Soporte cross-browser**: Variables de entorno para selección de navegador
- **Soporte multi-entorno**: Variables ENV para diferentes entornos de prueba
- **Carga escalable de pasos**: Carga automática de todos los archivos de definición de pasos
- **Generación única de reportes**: Nomenclatura de reportes basada en timestamp
- **Estructura de directorios mejorada**: Auto-creación de todos los directorios necesarios

### 4.3 Requisitos de Idioma, Estilo y Licencia
- **Toda documentación, archivos README, comentarios y texto orientado al usuario debe estar escrito en español**
- **Los comentarios de código deben ser naturales y comprensibles, evitando lenguaje robótico o excesivamente técnico**
- **Los logs y mensajes de error (console.log, console.error, etc.) deben ser claros, amigables y en español, SIN ICONOS NI EMOJIS**
- **PROHIBICIÓN: No deben aparecer iconos o emojis en NINGÚN archivo de código (.js, .json, archivos .config), solo permitidos en README.md**
- **Todos los archivos de código deben estar completamente libres de símbolos visuales, iconos, emojis o caracteres decorativos**
- **La licencia del proyecto debe ser GPLv3 y el campo author en package.json debe ser "Knowmadmood"**
- **Agregar `.env` a `.gitignore`** e incluir documentación de seguridad apropiada en README

### 4.4 Validaciones Finales
- Asegurar que el framework funciona end-to-end con scripts npm apropiados
- Validar que la implementación de Browser Factory previene múltiples instancias de navegador
- Verificar que la configuración mejorada de Cucumber funciona correctamente con ejecución dry-run
- **Validar carga automática de pasos**: Verificar que el patrón `src/steps/**/*.js` carga todos los archivos de pasos
- **Probar generación única de reportes**: Confirmar que los nombres de reportes basados en timestamp previenen sobrescrituras
- **Validar creación completa de directorios**: Asegurar que todos los directorios de reportes se crean automáticamente
- **Verificar retroalimentación post-ejecución**: Confirmar que el manejador process.on('exit') proporciona ubicaciones de reportes
- **Validar que playwright.config.js existe pero NO SE USA**: Debe existir para prevenir errores de dependencias pero no ejecutado por el framework
- **Confirmar responsabilidad de browserFactory.js**: Toda la lógica de gestión de navegador centralizada, completamente aislada de playwright.config.js
- **Probar separación de configuración**: Creación de navegador vía browserFactory SOLO, playwright.config.js NO sirve propósito funcional

## 5. CRITERIOS DE CALIDAD

### 5.1 Estándares Técnicos
Producir una estructura de framework Playwright de alta calidad y mantenible que:

**Requisitos del Framework:**
- Estructura base completa del framework con solo archivos de ejemplo únicos
- Se adhiere al patrón de diseño Page Object Model **SIN clases base o herencia**
- **Incluye browserFactory.js en src/support/** y **common.steps.js** para gestión centralizada del navegador
- **Incluye environmentLoader.js en src/support/** para gestión centralizada de configuración de entorno
- Usa variables de entorno para toda configuración sensible
- Incluye scripts npm multi-navegador (chromium, firefox, webkit) usando variables de entorno

### 5.2 Documentación Requerida y Estilo
- Toda documentación, archivos README, comentarios deben estar escritos en español
- Los comentarios de código deben usar tono natural y conversacional - evitar lenguaje robótico
- Los logs de consola y mensajes de error deben ser amigables y comprensibles
- **PROHIBICIÓN: No iconos o emojis en NINGÚN archivo de código (.js, .json, archivos .config) - solo permitidos en archivos README.md**
- **Todos los archivos de código deben estar completamente libres de símbolos visuales, iconos, emojis o caracteres decorativos**
- Configuración de licencia GPLv3 con "Knowmadmood" como autor en package.json
- Documentación clara para configuración segura de entorno
- Documentar el patrón de contexto compartido para uso de `this.page` en archivos de pasos
- Documentación de mejores prácticas de seguridad para manejo de credenciales

### 5.3 Validación de Funcionalidad

**Validaciones Críticas:**
- **Cucumber dry-run pasa**: `npx cucumber-js --config cucumber.config.js --dry-run` se ejecuta sin errores
- **Carga mejorada de pasos funciona**: Verificar que el patrón `'src/steps/**/*.js'` carga automáticamente TODOS los archivos de definición de pasos
- **Integración de archivos de soporte**: Confirmar que el patrón `'src/support/**/*.js'` incluye todos los archivos de soporte automáticamente
- **Generación única de reportes**: Validar que la nomenclatura de reportes basada en timestamp previene sobrescribir reportes anteriores
- **Creación completa de directorios**: Asegurar creación automática de directorios de screenshots, videos, JSON y HTML
- **Retroalimentación post-ejecución**: Verificar que el manejador process.on('exit') proporciona información clara de ubicación de reportes
- **Gestor único de ciclo de vida del navegador**: Solo common.steps.js contiene hooks Before/After
- **Patrón de contexto compartido funciona**: Los archivos de pasos usan `this.page`, nunca crean navegadores directamente
- **Ejecución multi-navegador**: Los scripts funcionan con la variable de entorno BROWSER usando `--config cucumber.config.js`
- **worldParameters mejorados**: Verificar compartición de objeto de configuración comprensivo con definiciones de pasos
- **Validación end-to-end**: `npm install && npm run test:dry-run` tiene éxito
- **Validación de escalabilidad**: Agregar nuevos archivos de pasos NO requiere cambios de configuración
- **playwright.config.js NO USADO por el framework**: Existe solo para prevenir errores de dependencias, NO contiene configuración funcional
- **Patrón Browser Factory enforced**: TODA gestión de navegador a través de browserFactory.js EXCLUSIVAMENTE
- **Validación de environmentLoader.js**: Carga centralizada de configuración de entorno funciona correctamente
- **Separación de configuración**: playwright.config.js NO sirve propósito funcional, browserFactory.js maneja TODAS las operaciones del navegador
- **Validación de retroalimentación visual**: Confirmar salida de consola clara y amigable durante inicialización del framework
- **Validación de manejo de errores**: Verificar que los bloques try-catch proporcionan mensajes de error significativos
- **Cumplimiento de estilo de código**: TODOS los archivos de código completamente libres de iconos, emojis o caracteres decorativos
- **Todas las RESTRICCIONES CRÍTICAS seguidas**: Sin violaciones de alcance del framework, creación de archivos o requisitos de arquitectura
