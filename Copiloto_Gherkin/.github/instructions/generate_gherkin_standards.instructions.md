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

### Estrategia Avanzada de Etiquetado BDD

**Etiquetas Primarias:**
- `@smoke` - Funcionalidad esencial que debe funcionar (típicamente 1-2 escenarios por característica)
- `@regression` - Escenarios importantes incluyendo validaciones, manejo de errores, casos límite

**Etiquetas Secundarias:**
- Tipo de entorno: `@web`, `@mobile`, `@api`
- Áreas funcionales (ejemplos): `@authentication`, `@users`, `@products`, `@orders`, `@payments`, `@administration`, `@reports`, etc.
- Si la documentación son Historias de Usuario con ID de Jira, añadir etiqueta con el ID: `@ID-1234`

**Ejemplo de Etiquetado:**
```gherkin
@smoke @authentication
Escenario: Login exitoso al sistema

@regression @authentication  
Escenario: Login fallido por credenciales incorrectas

@smoke @expedientes
Escenario: Consultar expediente existente

@regression @facturas
Escenario: Validar campos obligatorios en factura
```

---

### Estructura de Archivos Requerida

```
${output_directory}/
├── INFORME.md    # Comprehensive documentation (ROOT LEVEL)
└── features/    # BDD feature files directory
    ├── authentication.feature
    ├── expediente-management.feature
    ├── turbo-alta-facturas.feature
    └── ...
```

**Importante:**
- **Los archivos .feature** van SOLO en el subdirectorio `features/`
- **INFORME.md** se debe ubicar en la raíz de `${output_directory}/` (NO en directorio `features/`)

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
4. **Reutilización**: Usar pasos que puedan ser reutilizados
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

