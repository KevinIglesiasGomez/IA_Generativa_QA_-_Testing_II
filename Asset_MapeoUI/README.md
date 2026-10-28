# Demo_MapeoUI - Copiloto de Mapeo de Interfaz para Automatizacion de Pruebas

## Objetivo General

Este copiloto proporciona asistencia experta para **identificar, extraer y estructurar los elementos de interfaz de usuario** necesarios para construir frameworks de pruebas automatizadas. Opera en dos modalidades de analisis: estatico (sobre codigo fuente) y dinamico (sobre aplicaciones en ejecucion). Es agnóstico al framework de frontend y al framework de testing destino.

El copiloto guia al equipo QA a traves de un flujo secuencial de 6 pasos que transforma cualquier aplicacion web o movil en un catalogo estructurado de selectores, listo para ser consumido directamente por Playwright, Cypress, Appium u otros frameworks de automatizacion.

---

## Estructura del Copiloto

```
Demo_MapeoUI/
├── .github/
│   ├── agents/
│   │   └── ui_mapper.agent.md
│   ├── instructions/
│   │   ├── ui_mapper_main.instructions.md
│   │   ├── ui_mapper_selectors.instructions.md
│   │   ├── ui_mapper_artifacts.instructions.md
│   │   └── ui_mapper_reference_tables.instructions.md
│   └── prompts/
│       ├── ui_mapper_step0_discovery.prompt.md
│       ├── ui_mapper_step1_screens.prompt.md
│       ├── ui_mapper_step2_elements.prompt.md
│       ├── ui_mapper_step3_selectors.prompt.md
│       ├── ui_mapper_step4_normalize.prompt.md
│       └── ui_mapper_step5_artifacts.prompt.md
├── Demo_MapeoUI.code-workspace
└── README.md
```

---

## Descripcion de Cada Fichero

### Agentes (.github/agents/)

| Fichero | Descripcion |
|---------|-------------|
| `ui_mapper.agent.md` | **UI Automation Architect** (Claude Sonnet 4.6). Agente principal del copiloto. Especializado en analisis de interfaces de usuario y extraccion de selectores robustos para automatizacion de pruebas. Conoce React, Angular, Vue, React Native, Flutter, Ionic y sus patrones DOM/UI tree. Opera en dos modos: analisis estatico de codigo fuente y analisis dinamico de DOM en runtime. |

### Instrucciones (.github/instructions/)

| Fichero | Descripcion |
|---------|-------------|
| `ui_mapper_main.instructions.md` | Fuente tecnica de verdad para el comportamiento general del copiloto. Define los dos modos de operacion (estatico y dinamico), los criterios de clasificacion de pantallas, los tipos de elementos interactivos reconocidos, las reglas de flujo entre steps y el manejo de casos excepcionales con mensajes estandarizados. |
| `ui_mapper_selectors.instructions.md` | Fuente tecnica de verdad para la evaluacion y priorizacion de selectores. Define la jerarquia de robustez de identificadores (data-testid > id > name > aria-label > role > CSS semantico > XPath contextual > XPath absoluto), los criterios de fragilidad y las estrategias de fallback por framework. Incluye §2 de validacion semantica (tabla de patrones de IDs genericos/ofuscados, criterios Android/Appium para resource-id, deteccion temprana de duplicados en Step 3), selector de contexto para IDs duplicados y campo `enabled_state` en locators. |
| `ui_mapper_artifacts.instructions.md` | Fuente tecnica de verdad para la generacion de artefactos de testing. Define las plantillas de Page Object para Playwright y Cypress, el formato de locator files para Appium, la estructura del mapa JSON de UI y el formato del informe de recomendaciones. La plantilla JSON de Appium (§5) incluye campos `initial_state`, `enabled_condition` y `absolute_fallback` con coordenadas normalizadas (x_ratio/y_ratio) como ultimo recurso. |
| `ui_mapper_reference_tables.instructions.md` | Fichero consolidado con todas las tablas de referencia compartidas entre steps. Incluye: (1) Deteccion de frameworks, (2) Atributos de testing por framework, (3) Convencion de nomenclatura, (4) Sintaxis de selectores, (5) Patrones fragiles, (6) Clasificacion de complejidad, (7) Taxonomia de elementos, (8) Respuestas estandar para casos excepcionales — incluido `ERROR_WRONG_PACKAGE` para capturas con package incorrecto, (9) Tabla de landmarks de deteccion de pantalla activa en modo dinamico movil con procedimiento de verificacion y ejemplo Appium. |

### Prompts (.github/prompts/)

| Fichero | Descripcion | Mejoras v2.0 | Mejoras v2.1 |
|---------|-------------|-------------|-------------|
| `ui_mapper_step0_discovery.prompt.md` | **Step 0: Descubrimiento**. Detecta el proyecto o aplicacion objetivo, identifica el framework, el modo de operacion (estatico/dinamico) y genera el inventario inicial de modulos o pantallas. | Roles cognitivos simplificados, mensajes de error estandarizados | **Fase 1b**: lista de verificacion pre-flight de 6 items para modo dinamico movil (adb, Appium, AVD, overlays), plantilla de capabilities Appium con `newCommandTimeout: 180`, regla de sesion unica |
| `ui_mapper_step1_screens.prompt.md` | **Step 1: Deteccion de Pantallas**. Construye el arbol completo de vistas, rutas y componentes. Establece la jerarquia de navegacion y el contexto de cada pantalla. | Roles cognitivos simplificados, referencias a tablas consolidadas | **Modo Dinamico Movil**: rama especifica para Appium/Compose/RN/Flutter: construccion de tabla de landmarks de pantalla activa y deteccion del mecanismo de navegacion |
| `ui_mapper_step2_elements.prompt.md` | **Step 2: Mapeo de Elementos UI**. Para cada pantalla seleccionada, identifica y cataloga todos los elementos interactivos con sus atributos, tipo y contexto funcional. | Few-shot example completo con codigo JSX de 40 lineas | Ficha de elemento ampliada con campos **`Estado inicial`** (enabled/disabled/hidden) y **`Condicion enable`** para elementos con estado condicional |
| `ui_mapper_step3_selectors.prompt.md` | **Step 3: Extraccion de Selectores**. Evalua los identificadores disponibles por elemento, los clasifica segun la jerarquia de robustez y genera la matriz de selectores primarios y de fallback. | Few-shot example con matriz completa y selectores fragiles | **Fase 0 obligatoria**: cruce con registro global de IDs ANTES de generar selectores, criterio de colision, escalado a ALTA, actualizacion del registro global |
| `ui_mapper_step4_normalize.prompt.md` | **Step 4: Normalizacion de Identificadores**. Aplica convenciones de nomenclatura y genera el registro normalizado con recomendaciones de mejora. | Validacion cruzada de nomenclatura entre pantallas, few-shot example | Fase 2 simplificada: **deteccion de duplicados literales relocada a Step 3**; Step 4 solo ejecuta validacion de consistencia semantica (patrones inconsistentes entre pantallas) |
| `ui_mapper_step5_artifacts.prompt.md` | **Step 5: Generacion de Artefactos**. Produce los ficheros finales: Page Objects para Playwright/Cypress, locator files para Appium, mapa UI en JSON y el informe de recomendaciones de identificadores. | Confirmacion explicita, priorizacion de recomendaciones, checklist integracion | Fase 3 actualizada: locators JSON de Appium incluyen **`initial_state`**, **`enabled_condition`** y **`absolute_fallback`** (coordenadas normalizadas) |

---

## Flujo de Trabajo

```
Step 0: Descubrimiento
   |
   +--> Modo Estatico (codigo fuente)
   |         |
   +--> Modo Dinamico (app en ejecucion)
             |
        Step 1: Deteccion de Pantallas
             |
        Step 2: Mapeo de Elementos UI
             |
        Step 3: Extraccion de Selectores
             |
        Step 4: Normalizacion de Identificadores
             |
        Step 5: Generacion de Artefactos
```

### Modos de Operacion

| Modo | Cuando Usarlo | Fuente de Datos |
|------|---------------|-----------------|
| **Estatico** | Tienes acceso al codigo fuente | Ficheros JSX/TSX/HTML/Vue/Dart del proyecto |
| **Dinamico** | Solo tienes la app en ejecucion | DOM via DevTools, Accessibility Tree, capturas de pantalla |

---

## Jerarquia de Robustez de Selectores

El copiloto prioriza los selectores segun esta escala de mayor a menor estabilidad:

| Nivel | Tipo de Selector | Estabilidad | Notas |
|-------|-----------------|-------------|-------|
| 1 | `data-testid` / `data-cy` / `data-test` | Maxima | Especifico para testing, no cambia con refactors |
| 2 | `id` semantico (no generado) | Alta | Estable si no es generado dinamicamente |
| 3 | `name` en formularios | Alta | Semantico y raramente cambia |
| 4 | `aria-label` / `aria-labelledby` | Alta | Semantico y beneficioso para accesibilidad |
| 5 | `role` con texto visible | Media-Alta | Combination robusta para elementos interactivos |
| 6 | CSS semantico (clase funcional) | Media | Solo clases funcionales, no de estilo |
| 7 | XPath contextual | Media-Baja | Acepta si el contexto es estable |
| 8 | XPath absoluto | Minima | Evitar; se rompe en cualquier cambio estructural |

---

## Compatibilidad de Frameworks

### Frontend Soportado (Modo Estatico)

| Framework | Ficheros Analizados | Particularidades |
|-----------|--------------------|--------------------|
| React / Next.js | `.jsx`, `.tsx` | Props, hooks de estado, data-testid convencional |
| Angular | `.html` (template), `.ts` (componente) | Directivas, reactive forms, Angular Testing Library |
| Vue / Nuxt | `.vue` (SFC) | Template, script setup, v-model |
| React Native | `.tsx` con componentes RN | testID prop, AccessibilityLabel |
| Flutter | `.dart` | Key widget, Semantics widget |
| Ionic | `.html` + `.ts` | ion-* components, capacitor |

### Testing Destino Soportado

| Framework | Artefactos Generados |
|-----------|---------------------|
| Playwright (JS/TS) | Page Object class, locator constants file |
| Cypress | Page Object class, commands.js additions |
| Appium | Locator file (JSON), Page Object Java/JS |
| Selenium | Page Object Java, By locators file |

---

## Caracteristicas Principales

| Caracteristica | Detalle |
|----------------|---------|
| Doble modo | Analisis de codigo fuente y analisis de DOM en runtime |
| Agnostico al framework | Compatible con React, Angular, Vue, React Native, Flutter, Ionic y Android Nativo/Jetpack Compose |
| Jerarquia de estabilidad | Priorizacion automatica de selectores segun fragilidad (8 niveles) |
| Flujo guiado y controlado | 6 steps secuenciales con confirmacion en cada paso |
| Artefactos multi-framework | Page Objects para Playwright, Cypress, Appium y Selenium |
| Deteccion de fragilidad | Identifica y advierte sobre selectores inestables con patrones regex y validacion semantica de IDs |
| Mapa UI estructurado | Genera JSON normalizado reutilizable entre herramientas |
| Recomendaciones priorizadas | Propuestas clasificadas ALTA/MEDIA/BAJA segun criticidad, fragilidad y frecuencia |
| Validacion cruzada | Detecta inconsistencias de nomenclatura entre pantallas |
| Deteccion temprana de duplicados | Cruce con registro global de IDs en Step 3 (antes de generar selectores) |
| Estado de elementos | Campos `initial_state` y `enabled_condition` en locators para elementos con estado condicional |
| Few-shot examples | Ejemplos completos en Steps 2-4 para garantizar formato correcto |
| Manejo de errores | 7 mensajes estandarizados para casos excepcionales, incluido `ERROR_WRONG_PACKAGE` para capturas con package incorrecto |
| Pre-flight movil | Lista de verificacion de 6 items antes de capturar UI trees en modo dinamico movil |
| Landmarks de pantalla | Tabla de resource-ids landmark para identificar pantalla activa ANTES de capturar (evita captures de overlays del sistema) |
| Checklist de integracion | Guia de 6 pasos para adopcion del framework de testing |

---

## Como Usar Este Copiloto

### Inicio Rapido

1. **Abrir workspace:** Abrir `Demo_MapeoUI.code-workspace` en VS Code
2. **Activar agente:** En GitHub Copilot Chat, escribir `@ui_mapper`
3. **Iniciar analisis:** Proporcionar ruta del proyecto o URL de la app en ejecucion
4. **Seguir flujo:** El copiloto guiara a traves de los 6 steps con confirmaciones
5. **Obtener artefactos:** Los ficheros se generan en `ui-map/[nombre-app]/`

### Estructura de Salida

```
ui-map/
└── [nombre-app]/
    ├── pages/
    │   ├── LoginPage.js         (Page Object Playwright)
    │   └── HomePage.js
    ├── locators/
    │   ├── login.locators.js    (Locator constants)
    │   └── home.locators.js
    ├── ui-map.json              (Mapa UI completo)
    └── recommendations.md       (Informe priorizado con checklist)
```

### Casos de Uso Comunes

| Escenario | Modo Recomendado | Framework Testing |
|-----------|-----------------|-------------------|
| Proyecto React/Angular con acceso a codigo | Estatico | Playwright, Cypress |
| Aplicacion legacy sin codigo fuente | Dinamico | Selenium, Appium |
| App movil React Native | Estatico | Appium con testID |
| Proyecto Flutter | Estatico | Flutter Driver con Key |
| Auditoria de testability de app existente | Dinamico | Cualquiera (genera baseline) |

---

## Documentacion Adicional

- **Informe de calidad del copiloto:** Ver `Demo_AnalizaCopilotos/informes/informe_calidad_ui-mapper.md`
- **Tablas de referencia:** Ver `.github/instructions/ui_mapper_reference_tables.instructions.md`
- **Issue tracker:** Para reportar bugs o proponer mejoras

---

## Licencia y Contribuciones

Este copiloto es parte del repositorio de demos de IA para QA de la Comunidad QA CE.

**Mantenido por:** Comunidad QA CE  
**Version:** 2.1 (marzo 2026)  
**Changelog v2.1:** Pre-flight movil, landmarks de pantalla activa, validacion semantica de IDs, deteccion temprana de duplicados en Step 3, campos `initial_state`/`enabled_condition`/`absolute_fallback` en locators Appium, `ERROR_WRONG_PACKAGE`, registro global de IDs en contexto de sesion.  