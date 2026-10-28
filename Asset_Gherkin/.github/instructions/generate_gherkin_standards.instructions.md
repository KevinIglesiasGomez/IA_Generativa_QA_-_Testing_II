### Objetivo

Definir estándares y mejores prácticas para generar escenarios BDD con Cucumber.

---

### Estándares Obligatorios de Cucumber

**REQUISITOS OBLIGATORIOS:**
- Todos los escenarios DEBEN ser **ejecutables** y **comprobables**
- Usar **lenguaje declarativo** (QUÉ, no CÓMO)
- Seguir estrictamente la estructura **Given-When-Then** (Dado-Cuando-Entonces)
- Asegurar **reutilización de pasos** entre características
- Aplicar **principios SOLID** al diseño de escenarios
- Incluir **pruebas basadas en datos** donde sea apropiado
- Implementar escenarios de **manejo adecuado de errores**
  - **PROHIBIDO**: Pasos que comienzan con "O", "Pero", "E", "*", o cualquier otra palabra
  - **CORRECTO**: Usar "Y" para concatenar múltiples aserciones o condiciones alternativas

**Requisitos Técnicos de Validación:**
- Cada escenario DEBE tener **criterios de aceptación** claros
- Incluir escenarios de **pruebas de valores límite**
- Asegurar **independencia de datos de prueba** entre escenarios

---

### Reutilización Sistemática de Steps

**OBJETIVO**: Maximizar la reutilización de pasos entre TODAS las características generadas en una misma ejecución, para minimizar el código de automatización Playwright necesario al implementar los step definitions.

**REGLAS OBLIGATORIAS:**
- Antes de redactar un paso nuevo, **comprobar si ya existe un paso semánticamente equivalente** en alguna de las features generadas previamente en la misma ejecución (y en los `.feature` ya existentes en `e2e_repo/features/` si los hay).
- Si existe un paso equivalente, **reutilizarlo tal cual** (mismo texto) en vez de crear uno nuevo con redacción distinta.
- Si el paso existente difiere solo en un valor concreto (un usuario, una opción de menú, un campo, un mensaje, etc.), **parametrizarlo** sustituyendo el valor literal por un placeholder entre `< >`, y reutilizar esa forma parametrizada en todas las features donde aplique.
- Los placeholders deben nombrarse en snake_case, en español, describiendo el dato que representan: `<usuario>`, `<menu_option>`, `<campo>`, `<mensaje_error>`, `<rol>`, etc.
- Mantener un **inventario mental de los steps ya creados** durante toda la ejecución (todas las features generadas en la tarea actual) y consultarlo antes de escribir cada paso nuevo.
- No fragmentar un mismo comportamiento en pasos redactados de formas distintas solo por pertenecer a features diferentes (por ejemplo, "hace click en la opción Contacto" y "pulsa sobre el enlace Contacto" deben unificarse en un único paso reutilizable).

**Ejemplo:**
```gherkin
# En lugar de generar pasos distintos por feature:
Entonces Alberto hace click en la opción Contacto
Entonces María hace click en la opción Perfil

# Unificar en un único paso parametrizado y reutilizarlo en todas las features:
Entonces <usuario> hace click en la opción <menu_option>
```

---

### Estrategia Avanzada de Etiquetado BDD

**Etiquetas Primarias:**
- `@smoke` - Funcionalidad esencial que debe funcionar (típicamente 1-2 escenarios por característica)
- `@regression` - Escenarios importantes incluyendo validaciones, manejo de errores, casos límite

**Etiquetas Secundarias:**
- Tipo de entorno: `@web`, `@mobile`, `@api`
- Áreas funcionales (ejemplos): `@authentication`, `@users`, `@products`, `@orders`, `@payments`, `@administration`, `@reports`, etc.

**Etiqueta de Relación con Historia de Usuario:**
- Formato: `@related:<ID>` (ejemplos: `@related:HU-2451`, `@related:PROJ-123`)
- Se usa cuando la documentación incluye un identificador de historia de usuario (por ejemplo, un ID de Jira), para marcar los escenarios que la relacionan, típicamente como "tested by" esa historia
- El prefijo `related:` es intencional: reserva el namespace para IDs de relación, distinguiéndolos de otros posibles prefijos de etiqueta que se incorporen más adelante
- No usar el ID a secas como etiqueta (por ejemplo `@HU-2451`); debe ir siempre precedido de `related:`


**Ejemplo de Etiquetado:**
```gherkin
@smoke @authentication
Escenario: Login exitoso al sistema

@regression @authentication  
Escenario: Login fallido por credenciales incorrectas

@smoke @expedientes @related:HU-2451
Escenario: Consultar expediente existente

@regression @facturas @related:HU-2452
Escenario: Validar campos obligatorios en factura
```

---

### Estructura de Archivos Requerida

```
${output_directory}/
├── INFORME_<fecha_hora>.md    # Comprehensive documentation (ROOT LEVEL)
└── features/    # BDD feature files directory
    ├── authentication.feature
    ├── expediente-management.feature
    ├── turbo-alta-facturas.feature
    └── ...
```

**Importante:**
- **Los archivos .feature** van SOLO en el subdirectorio `features/`
- **INFORME_<fecha_hora>.md** se debe ubicar en la raíz de `${output_directory}/` (NO en directorio `features/`), con el nombre incluyendo la fecha y hora de creación (formato `YYYY-MM-DD_HH-mm-ss`)

---

### Estructura de Escenarios y Mejores Prácticas

**Estructura de Escenarios:**
```gherkin
# language: es
Característica: [Descriptive functionality name]
  Como [user type]
  Quiero [perform an action]
  Para [obtain a benefit]

  @smoke @[functional_area]
  Escenario: [Success scenario description]
    Dado que [initial condition]
    Y [additional condition if necessary]
    Cuando [user action]
    Entonces [expected result]
    Y [additional validation if necessary]

  @regression @[functional_area] @validaciones
  Escenario: [Validation scenario description]
    Dado que [initial condition]
    Cuando [action that causes error]
    Entonces [expected error result]
    Y [specific error validation]
```

**Principios de Escritura:**
1. **Lenguaje Natural**: Usar terminología del dominio de negocio
2. **Declarativo vs Imperativo**: Describir QUÉ no CÓMO
3. **Independencia**: Cada escenario debe ser independiente
4. **Reutilización**: Usar pasos parametrizados que puedan ser reutilizados entre features, según la sección "Reutilización Sistemática de Steps"
5. **Granularidad**: Un escenario por comportamiento específico

---

### Convenciones de Nomenclatura

**Archivos de Características:**
- Usar kebab-case para nombres de archivos
- Nombres descriptivos del área funcional
- Ejemplos: `user-authentication.feature`, `invoice-management.feature`

**Nombres de Escenarios:**
- Descriptivos y concisos
- Ejemplos: "Crear nueva factura con datos válidos", "Validar campos obligatorios"

**Etiquetas:**
- Usar minúsculas
- Separar palabras con guiones bajos si es necesario
- Ejemplos: `@smoke`, `@regression`, `@user_management`

---

### Patrones de Datos de Prueba

**Esquemas de Escenario para Datos Múltiples:**
```gherkin
@regression @validaciones
Esquema del escenario: Validate [field] format
  Dado que estoy en la página "[page]"
  Cuando ingreso "<value>" en el campo "[field]"
  Entonces debería ver el mensaje "<error_message>"

  Ejemplos:
    | value          | error_message                    |
    | invalid_email  | Incorrect email format          |
    | empty_text     | This field is mandatory         |
    | long_text      | Maximum 50 characters allowed   |
```

