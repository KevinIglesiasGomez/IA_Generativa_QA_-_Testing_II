# Instrucciones de tecnicas creativas para el Agente: Tester Creativo

## 1. Tecnicas de testing creativo

El agente debe dominar y aplicar las siguientes tecnicas segun el contexto de la informacion analizada. No todas las tecnicas aplican en todos los casos; el agente debe seleccionar las mas relevantes.

### 1.1. Analisis de valores limite (Boundary Value Analysis)
- Identificar todos los limites explicitos e implicitos
- Probar el valor exacto en el limite
- Probar un valor inmediatamente por debajo
- Probar un valor inmediatamente por encima
- Aplicar a: longitudes de texto, rangos numericos, fechas, cantidades, dimensiones de archivos

### 1.2. Particion de equivalencia (Equivalence Partitioning)
- Dividir el dominio de entrada en clases validas e invalidas
- Seleccionar al menos un representante de cada clase
- Identificar clases no obvias (valores especiales, formatos mixtos)
- Aplicar a: campos de formulario, parametros de API, opciones de configuracion

### 1.3. Tabla de decision (Decision Table Testing)
- Identificar todas las condiciones que afectan el comportamiento
- Mapear combinaciones de condiciones con acciones esperadas
- Detectar combinaciones no cubiertas o ambiguas
- Aplicar a: reglas de negocio complejas, permisos, flujos condicionales

### 1.4. Transicion de estados (State Transition Testing)
- Mapear todos los estados posibles del sistema
- Identificar transiciones validas e invalidas
- Probar secuencias de transiciones
- Detectar estados huerfanos o inalcanzables
- Aplicar a: flujos de pedido, estados de usuario, ciclos de vida de recursos

### 1.5. Testing exploratorio con heuristicas
Aplicar las siguientes heuristicas sistematicamente:

**Heuristica SFDPOT:**
- Structure: estructura y composicion del producto
- Function: que hace el producto
- Data: que datos procesa
- Platform: en que entorno opera
- Operations: como se usa en la practica
- Time: como se comporta respecto al tiempo

**Heuristica FEW HICCUPPS:**
- Familiar: comparar con productos similares conocidos
- Explainability: se puede explicar el comportamiento observado
- World: es consistente con el mundo real
- History: es consistente con versiones anteriores
- Image: es consistente con la imagen de la empresa
- Comparable: es consistente con productos comparables
- Claims: es consistente con lo que se promete
- User expectations: cumple las expectativas del usuario
- Product: es consistente consigo mismo
- Purpose: cumple su proposito
- Standards: cumple estandares aplicables

### 1.6. Testing por mutacion conceptual
- Invertir una regla de negocio y verificar que el sistema la rechaza
- Cambiar el orden de los pasos y verificar que el flujo lo detecta
- Omitir un paso obligatorio y verificar el comportamiento
- Duplicar una accion y verificar que se maneja correctamente
- Sustituir un valor valido por uno de otro tipo

### 1.7. Testing combinatorio (Pairwise)
- Identificar variables independientes con multiples valores
- Generar combinaciones minimas que cubran todos los pares
- Detectar interacciones inesperadas entre parametros
- Aplicar a: formularios con multiples campos, configuraciones, filtros

### 1.8. Inyeccion de fallos (Fault Injection)
- Simular corte de red durante operacion critica
- Simular respuesta lenta del servidor
- Simular respuesta con datos corruptos
- Simular falta de espacio en disco (upload)
- Simular sesion expirada en medio de flujo

---

## 2. Heuristicas de pensamiento lateral

### 2.1. Inversion
- Si el usuario deberia hacer X, que pasa si hace lo contrario
- Si el sistema espera datos en formato A, que pasa si recibe formato B
- Si el flujo es A entonces B entonces C, que pasa si es C entonces B entonces A

### 2.2. Analogia
- Comparar la funcionalidad con un proceso del mundo real
- Identificar que podria salir mal en el proceso analogico
- Trasladar esos fallos al contexto del software

### 2.3. Personificacion de usuarios extremos
- El usuario novato que no lee instrucciones
- El usuario impaciente que hace click multiples veces
- El usuario malintencionado que busca vulnerabilidades
- El usuario con discapacidad visual que usa lector de pantalla
- El usuario con conexion intermitente
- El usuario que usa un dispositivo no convencional
- El usuario que deja la sesion abierta durante horas
- El usuario que trabaja con multiples pestanas simultaneamente

### 2.4. WWWWWH (What, Who, Where, When, Why, How)
Para cada funcionalidad preguntar:
- What: que puede salir mal
- Who: a quien afecta
- Where: en que contexto falla
- When: en que momento temporal falla
- Why: por que podria fallar
- How: como se manifiesta el fallo

---

## 3. Priorizacion de escenarios creativos

Cada escenario creativo debe evaluarse con estos criterios:

### 3.1. Matriz de priorizacion

| Criterio | Peso | Escala |
|---|---|---|
| Probabilidad de ocurrencia | 30% | 1-10 |
| Impacto en el usuario | 25% | 1-10 |
| Impacto en el negocio | 25% | 1-10 |
| Dificultad de deteccion por otros medios | 20% | 1-10 |

**Score = (Probabilidad x 0.30) + (Impacto usuario x 0.25) + (Impacto negocio x 0.25) + (Dificultad deteccion x 0.20)**

### 3.2. Clasificacion por score
- **Alta prioridad:** Score >= 7.0
- **Media prioridad:** Score entre 4.0 y 6.9
- **Baja prioridad:** Score < 4.0

### 3.3. Orden de propuesta
Los escenarios deben proponerse al ingeniero en orden descendente de score, comenzando siempre por los de mayor prioridad.

---

## 4. Cuando usar cada tecnica

| Tipo de entrada | Tecnicas recomendadas |
|---|---|
| Captura de pantalla | Testing exploratorio, personificacion de usuarios, inversion, analisis de limites visuales |
| Documentacion | Tabla de decision, transicion de estados, particion de equivalencia, WWWWWH |
| Codigo fuente | Analisis de limites, mutacion conceptual, inyeccion de fallos, testing combinatorio |
| HTML/Markup | Analisis de limites (atributos), testing exploratorio, accesibilidad, inversion |

---
