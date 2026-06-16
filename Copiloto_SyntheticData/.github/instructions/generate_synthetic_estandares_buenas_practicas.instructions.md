### Objetivo

Definir estándares y mejores prácticas para generar datos sintéticos de alta calidad para pruebas de software.

---

### Principios Fundamentales de Datos Sintéticos

**REQUISITOS OBLIGATORIOS:**
- Los datos DEBEN ser **realistas** y coherentes con el dominio de negocio
- Los datos DEBEN mantener **integridad referencial** entre entidades relacionadas
- Los datos NO DEBEN contener **información sensible real**
- Los datos DEBEN ser **reproducibles** (semilla controlada)
- Los datasets DEBEN incluir **metadatos completos**
- Los datos DEBEN cubrir **casos normales, límite y excepcionales**
- Los datos DEBEN cumplir con **GDPR** y normativas de protección de datos

**Principios de Calidad:**
- **Exactitud**: Los datos respetan el formato y tipo de dato definido
- **Completitud**: No hay valores nulos donde no deberían existir
- **Consistencia**: Los datos son coherentes entre campos relacionados
- **Validez**: Los datos cumplen reglas de negocio y validaciones
- **Unicidad**: Los campos únicos no tienen duplicados
- **Actualidad**: Las fechas y timestamps son lógicos y coherentes

---

### Tipos de Datos Soportados

**Tipos Primitivos:**
- `string` - Cadenas de texto
- `integer` - Números enteros
- `float`/`decimal` - Números con decimales
- `boolean` - Verdadero/Falso
- `date` - Fecha (YYYY-MM-DD)
- `datetime` - Fecha y hora (ISO 8601)
- `timestamp` - Unix timestamp
- `uuid` - Identificador único universal

**Tipos Especializados:**
- `email` - Dirección de correo electrónico. Los emails para happy path no deben contener caracteres especiales como tildes, eñes o caracteres no ASCII. Para los casos negativos, se pueden incluir caracteres especiales para probar validaciones.
- `phone` - Número de teléfono
- `url` - URL válida
- `ip_address` - Dirección IP (v4 o v6)
- `credit_card` - Número de tarjeta (enmascarado)
- `iban` - Código IBAN bancario
- `dni`/`nif` - Documento de identidad con letra correspondiente (España)
- `cif` - Código de identificación fiscal para empresas (España)
- `nie` - Número de identidad de extranjero (España)
- `postal_code` - Código postal
- `country_code` - Código ISO de país
- `currency_code` - Código ISO de moneda

**Tipos Compuestos:**
- `address` - Dirección completa (calle, ciudad, código postal, país)
- `person` - Datos personales (nombre, apellidos, fecha nacimiento)
- `company` - Datos empresariales (nombre, CIF, dirección)
- `geolocation` - Coordenadas geográficas (lat, lon)

---

### Estrategias de Generación

**1. Generación Aleatoria Controlada:**

- Crear scripts que generen datos aleatorios pero controlados por parámetros
- Todos los scripts deben quedar guardades en el área de trabajo para su reutilización
- Usar semilla (seed) para reproducibilidad
- Aplicar distribuciones apropiadas 
  - normal: valores alrededor de una media
  - uniforme: valores distribuidos equitativamente
  - exponencial: para tiempos de espera o eventos raros
  - poisson: para conteos de eventos (numero de pedidos por día, visitas a un sitio, etc.)
- Respetar rangos y límites definidos

**2. Generación Basada en Plantillas:**

- Usar patrones predefinidos (ej: "PROD-{number:5}")
- Aplicar máscaras de formato
- Combinar elementos fijos y variables

**3. Generación Basada en Diccionarios:**

- Usa los diccionarios ya existentes en 'templates/diccionarios' si son relevantes para el dominio
- Usar listas curadas de valores reales (nombres, ciudades, etc.)
- Combinar elementos de múltiples diccionarios
- Mantener coherencia cultural y geográfica
- Si se generan diccionarios nuevos deben quedar guardados en el área de trabajo para su reutilización

**4. Generación Basada en Reglas:**

- Aplicar lógica de negocio
- Mantener relaciones entre campos
- Calcular campos derivados

---

### Distribución de Datos

**Escenarios de Prueba:**
- **60%** - Casos válidos normales (happy path)
- **20%** - Casos de valores límite (boundary)
- **20%** - Casos excepcionales/inválidos (para pruebas negativas)

**Variedad de Datos:**
- Incluir diferentes longitudes de texto (corto, medio, largo)
- Incluir caracteres especiales y unicode cuando sea apropiado
- Incluir valores en diferentes idiomas si aplica
- Incluir fechas recientes, pasadas y futuras según contexto

---

### Formato de Esquema de Datos

**Definición de Campo:**
```json
{
  "field_name": {
    "type": "string",
    "description": "Descripción del campo",
    "required": true,
    "unique": false,
    "constraints": {
      "min_length": 3,
      "max_length": 50,
      "pattern": "^[A-Z]{3}-[0-9]{4}$",
      "values": ["option1", "option2", "option3"]
    },
    "generation_strategy": "pattern",
    "example": "ABC-1234"
  }
}
```

**Restricciones Comunes:**
- `min_length` / `max_length` - Para strings
- `min_value` / `max_value` - Para números
- `pattern` - Expresión regular
- `values` - Lista de valores permitidos (enum)
- `foreign_key` - Referencia a otra entidad
- `default` - Valor por defecto
- `nullable` - Permite valores nulos

---

### Mejores Prácticas

**Correcto:**
- Usar nombres de campo descriptivos y consistentes 
- Documentar cada campo con descripción clara
- Incluir ejemplos representativos
- Mantener relaciones entre entidades
- Validar datos generados contra el esquema
- Incluir metadatos de generación (fecha, versión, semilla)
- Usar identificadores que no colisionen con datos reales

**Incorrecto:**
- Usar datos personales reales
- Generar IBANs, tarjetas de crédito o DNIs reales
- Incluir información confidencial en ejemplos
- Crear relaciones inconsistentes entre entidades
- Ignorar restricciones de negocio
- Generar datos sin validación
- Omitir documentación

---

### Validaciones Obligatorias

**Pre-generación:**
- [ ] El esquema está completamente definido
- [ ] Las restricciones son coherentes
- [ ] Las relaciones entre entidades están mapeadas
- [ ] Los tipos de datos son apropiados
- [ ] Las estrategias de generación están definidas

**Post-generación:**
- [ ] Todos los campos requeridos tienen valores
- [ ] Los tipos de datos son correctos
- [ ] Las restricciones se cumplen (rangos, patrones, etc.)
- [ ] Los campos únicos no tienen duplicados
- [ ] Las relaciones referenciales son válidas
- [ ] Los datos pasan validaciones de negocio
- [ ] El tamaño del dataset es correcto

---

### Casos de Uso Típicos

**Testing Funcional:**
- Datos válidos para happy path
- Datos que cubren todas las funcionalidades
- Volumen moderado (10-1000 registros)

**Testing de Rendimiento:**
- Gran volumen de datos (1M+ registros)
- Datos realistas que simulan producción
- Distribución representativa

**Testing de Seguridad:**
- Datos con intentos de inyección SQL
- Datos con XSS y scripts maliciosos
- Datos con caracteres especiales problemáticos

**Testing de Integración:**
- Datos que respetan interfaces entre sistemas
- Datos con todas las relaciones necesarias
- Datos sincronizados entre entidades

**Demos y Formación:**
- Datos realistas pero ficticios
- Datos que ilustran todas las características
- Volumen moderado y fácil de entender
```