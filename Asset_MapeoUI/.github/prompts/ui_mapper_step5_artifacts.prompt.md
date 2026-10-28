---
agent: "ui_mapper"
tools: ["edit/editFiles", "edit/createDirectory", "read/readFile"]
description: "Step 5: Generacion masiva de artefactos finales de testing en ui-map/: Page Objects con metodos tipados, locator files (.locators.json), mapa UI JSON consolidado con jerarquia completa e informe de recomendaciones priorizadas"
model: "Claude Sonnet 4.6"
---

# Step 5: Generacion de Artefactos para Testing

## 0. ARQUITECTURA COGNITIVA INTERNA

### ROL A: Generador de Page Objects
**Objetivo:** Crear ficheros Page Object para el framework de testing destino.
- Generar Page Object por pantalla segun plantilla de `ui_mapper_artifacts.instructions.md` | Incluir getters, acciones y verificaciones

### ROL B: Generador de Locator Constants
**Objetivo:** Crear ficheros de constantes de selectores.
- Generar locator file por pantalla | Incluir selectores primarios como constantes | Anotar nivel y fallback | Marcar fragiles

### ROL C: Generador de Mapa UI JSON y Calculo de Metricas
**Objetivo:** Compilar registro global en ui-map.json y calcular puntuacion de testability.
- Incluir datos app, pantallas y elementos | Calcular metricas de resumen | Calcular puntuacion de testability

### ROL D: Generador de Informe de Recomendaciones Priorizado
**Objetivo:** Compilar recomendaciones acumuladas con priorizacion por impacto.
- Recopilar recomendaciones de Steps 3-4 | Calcular prioridad (pantalla critica + nivel fragil + frecuencia uso) | Organizar por prioridad | Incluir checklist integracion

---

## 1. PREREQUISITOS

El registro global debe estar completo con:
- Todas las pantallas aprobadas en estado "Completado"
- Todos los registros normalizados validados
- Framework de testing destino confirmado desde Step 0

---

## 2. INSTRUCCIONES DEL STEP

### Fase 0 - Confirmacion explicita antes de generacion masiva de ficheros (NUEVO)

Antes de generar los artefactos, presentar al usuario el resumen de lo que se va a crear:

```
## Resumen de Artefactos a Generar - Confirmacion Requerida

**Pantallas procesadas**: [numero]
**Total de ficheros a crear**: [numero] ([X] Page Objects + [X] Locator files + 2 ficheros globales)

**Ubicacion de destino**: `ui-map/[nombre-app]/`

**Ficheros que se crearan:**
- [X] Page Objects en `/pages/`
- [X] Locator files en `/locators/`
- 1 Mapa UI JSON: `ui-map.json`
- 1 Informe de recomendaciones: `recommendations.md`

**Estimacion de contenido:**
- Lines totales aproximadas: [estimacion]
- Pantallas con selectores fragiles: [numero]
- Recomendaciones prioritarias: [numero]

**IMPORTANTE:** Esta operacion creara multiples ficheros en el sistema de archivos.

Â¿Confirmas la generacion de los artefactos? (Responde "Si" para continuar o "Revisar" para ajustar la configuracion)
```

Esperar confirmacion del usuario antes de continuar a Fase 1.

### Fase 1 - Creacion de la estructura de carpetas de salida

Crear la siguiente estructura en la carpeta de trabajo:

```
ui-map/
|-- [nombre-app]/
    |-- pages/
    |-- locators/
    |-- ui-map.json
    |-- recommendations.md
```

Confirmar al usuario donde se van a generar los ficheros antes de crearlos.

### Fase 2 - Generacion de Page Objects

Para CADA pantalla del registro global:
1. Determinar el nombre del fichero siguiendo la convencion: `[NombrePantalla]Page.[extension]`
2. Aplicar la plantilla de Page Object de `ui_mapper_artifacts.instructions.md` para el framework destino
3. Incluir un getter por cada elemento del registro de la pantalla
4. Incluir metodos de accion:
   - Un metodo por cada accion atomica (rellenar campo, hacer click)
   - Un metodo compuesto para los flujos principales de la pantalla (ej: `iniciarSesion(usuario, password)`)
5. Incluir metodos de verificacion para elementos condicionales (mensajes de error, estados vacios)
6. Guardar el fichero en `ui-map/[nombre-app]/pages/`

### Fase 3 - Generacion de Locator Constants

Para CADA pantalla del registro global:
1. Determinar el nombre del fichero: `[nombre-pantalla].locators.[extension]`
2. Aplicar la plantilla de locator constants de `ui_mapper_artifacts.instructions.md`
3. Incluir una constante por cada elemento con el selector primario
4. Agregar en comentarios: nivel de robustez, tipo de atributo y selector fallback
5. Marcar con comentario de advertencia `ADVERTENCIA: Fragil` los selectores de Nivel 6 o superior
6. Para modo Appium (JSON): incluir los campos `initial_state`, `enabled_condition` y `absolute_fallback` segun la plantilla de la seccion 5 de `ui_mapper_artifacts.instructions.md`
7. Guardar el fichero en `ui-map/[nombre-app]/locators/`

### Fase 4 - Generacion del Mapa UI JSON

Compilar `ui-map.json` con el registro global completo:
1. Seccion `app`: datos del proyecto detectados en Step 0
2. Seccion `screens`: array con todas las pantallas y sus elementos
3. Para cada elemento: ID, descripcion, tipo, selector primario, nivel, fallback, fragil
4. Seccion `summary`: metricas calculadas a partir del registro global
5. Guardar en `ui-map/[nombre-app]/ui-map.json`

### Fase 5 - Generacion del Informe de Recomendaciones con Priorizacion (MEJORADO)

Compilar `recommendations.md` con el siguiente contenido en orden:

**1. Resumen ejecutivo:** puntuacion de testability del proyecto

**2. Selectores fragiles priorizados por impacto:**

Calcular la prioridad de cada recomendacion segun la formula:

```
Prioridad = (Criticidad_Pantalla * 0.4) + (Nivel_Fragilidad * 0.3) + (Frecuencia_Uso * 0.3)

Donde:
- Criticidad_Pantalla:
  * Alta (1.0): Login, Checkout, Payment, Auth, Register
  * Media (0.6): Home, Dashboard, Profile, Settings
  * Baja (0.3): About, Help, Terms, Privacy

- Nivel_Fragilidad:
  * Nivel 8 (XPath absoluto): 1.0
  * Nivel 7 (XPath contextual): 0.85
  * Nivel 6 (CSS funcional): 0.7
  * Nivel 5 (role + texto): 0.5
  * Nivel 4 o inferior: 0.3

- Frecuencia_Uso (estimada por tipo de elemento):
  * Botones de accion primaria: 1.0
  * Inputs de formulario: 0.9
  * Enlaces de navegacion: 0.7
  * Botones secundarios: 0.5
  * Elementos de solo lectura: 0.3
```

Clasificacion final:
- Prioridad >= 0.75: **ALTA** (implementar inmediatamente)
- Prioridad 0.50-0.74: **MEDIA** (implementar en siguiente sprint)
- Prioridad < 0.50: **BAJA** (backlog de mejora continua)

Organizar las recomendaciones por prioridad descendente.

**3. Guia de implementacion** adaptada al framework del proyecto

**4. Metricas de cobertura** por nivel de robustez

**5. Convencion de nombres adoptada** durante el analisis

**6. Checklist de Integracion Post-Implementacion (NUEVO):**

```markdown
## Checklist de Integracion

### Paso 1: Importar artefactos en el proyecto de testing

- [ ] Copiar carpeta `ui-map/[app]/pages/` a `[tu-proyecto]/tests/pages/`
- [ ] Copiar carpeta `ui-map/[app]/locators/` a `[tu-proyecto]/tests/locators/`
- [ ] Verificar que las rutas de importacion son correctas

### Paso 2: Verificar compatibilidad de versiones

- [ ] Verificar version de [Playwright/Cypress/Selenium/Appium] es compatible
- [ ] Instalar dependencias si es necesario: `npm install` o equivalente
- [ ] Verificar que los imports de Page Objects funcionan sin errores

### Paso 3: Ejecutar test de smoke inicial

- [ ] Crear un test basico que importe 1 Page Object
- [ ] Ejecutar el test contra la aplicacion en desarrollo
- [ ] Verificar que los selectores encuentran los elementos correctamente
- [ ] Si falla: revisar que la aplicacion esta en la version analizada

### Paso 4: Implementar recomendaciones prioritarias (ALTA)

- [ ] Compartir `recommendations.md` con el equipo de desarrollo
- [ ] Crear issues/tareas para las [X] recomendaciones de prioridad ALTA
- [ ] Asignar propietario a cada tarea
- [ ] Estimar esfuerzo de implementacion

### Paso 5: Re-analizar para medir mejora

- [ ] Tras implementar las recomendaciones ALTA, re-ejecutar UI Mapper en el mismo proyecto
- [ ] Comparar puntuacion de testability anterior vs nueva
- [ ] Objetivo: pasar de [X]% a 85%+ de testability
- [ ] Documentar la mejora en el backlog del equipo

### Paso 6: Crear tests funcionales usando Page Objects

- [ ] Identificar los 3-5 flujos criticos de la aplicacion
- [ ] Crear tests end-to-end usando los Page Objects generados
- [ ] Integrar tests en pipeline de CI/CD
- [ ] Establecer umbral de cobertura minimo
```

Guardar en `ui-map/[nombre-app]/recommendations.md`

---

## 3. CALCULO DE PUNTUACION DE TESTABILITY

La puntuacion de testability es un indicador del porcentaje de elementos con selectores estables.

Formula:
```
Puntuacion = ((N1 * 1.0) + (N2 * 0.9) + (N3 * 0.85) + (N4 * 0.8) + (N5 * 0.6) + (N6 * 0.4) + (N7 * 0.2) + (N8 * 0.0)) / Total_Elementos * 100
```

Donde N1...N8 = numero de elementos cuyo selector primario es de ese nivel.

Interpretacion:
| Puntuacion | Nivel de Testability | Descripcion |
|------------|---------------------|-------------|
| 85-100% | Excelente | La mayoria de elementos tienen atributos de testing dedicados |
| 70-84% | Buena | Pocos selectores fragiles, mantenimiento bajo |
| 50-69% | Aceptable | Riesgo moderado de rotura de tests en refactors |
| 30-49% | Deficiente | Alta fragilidad, se recomienda mejora urgente |
| 0-29% | Critica | La aplicacion no es testable sin intervencion del equipo de desarrollo |

---

## 4. SALIDA ESPERADA

```
## Artefactos Generados - Step 5 Completado

**Aplicacion**: [nombre]
**Framework de testing**: [playwright | cypress | appium | selenium]

### Ficheros generados

| Fichero | Tipo | Pantalla |
|---------|------|----------|
| ui-map/[app]/pages/LoginPage.js | Page Object Playwright | Login |
| ui-map/[app]/pages/HomePage.js | Page Object Playwright | Home |
| ui-map/[app]/locators/login.locators.js | Locator Constants | Login |
| ui-map/[app]/locators/home.locators.js | Locator Constants | Home |
| ui-map/[app]/ui-map.json | Mapa UI JSON | Todas |
| ui-map/[app]/recommendations.md | Informe de recomendaciones | Todas |

### Resumen de la sesion

**Pantallas procesadas**: [numero]
**Total de elementos mapeados**: [numero]
**Puntuacion de testability**: [X]% ([nivel])
**Selectores fragiles**: [numero] ([X]% del total)
**Recomendaciones para el equipo de desarrollo**: [numero]

### Proximos pasos recomendados

1. Compartir `recommendations.md` con el equipo de desarrollo para agregar los atributos de testing sugeridos
2. Importar los Page Objects y locator files en el framework de testing de destino
3. Crear los tests usando los Page Objects generados
4. Re-ejecutar el analisis tras la implementacion de las recomendaciones para verificar la mejora de testability

---

Analisis completado. Todos los artefactos han sido generados en `ui-map/[nombre-app]/`.
```

---

## 5. NOTAS DE INTEGRACION CON FRAMEWORKS DE TESTING

### Para Playwright

Los Page Objects se importan en los tests de la siguiente forma:
```javascript
const { LoginPage } = require('./ui-map/[app]/pages/LoginPage');

test('deberia iniciar sesion correctamente', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await loginPage.iniciarSesion('usuario@test.com', 'password123');
});
```

### Para Cypress

Los Page Objects se usan como objetos de comando en los tests:
```javascript
import { LoginPage } from './ui-map/[app]/pages/LoginPage.cy';

describe('Login', () => {
  it('deberia iniciar sesion correctamente', () => {
    LoginPage.visitar();
    LoginPage.introducirUsuario('usuario@test.com');
    LoginPage.introducirPassword('password123');
    LoginPage.clickSubmit();
  });
});
```

### Para Appium

Los locator files JSON se leen desde el test runner para inicializar los locators:
```java
JSONObject locators = new JSONObject(new String(Files.readAllBytes(Paths.get("ui-map/[app]/locators/login.locators.json"))));
```

