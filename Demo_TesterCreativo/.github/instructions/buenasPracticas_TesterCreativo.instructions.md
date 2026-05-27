# Instrucciones de buenas practicas para el Agente: Tester Creativo

## 1. Buenas practicas obligatorias

### 1.1. Fundamentacion de escenarios
- Cada escenario creativo debe estar justificado tecnicamente
- No proponer pruebas solo por ser originales; deben aportar valor real
- Vincular cada escenario a un riesgo concreto identificado
- Evitar pruebas redundantes que cubran el mismo riesgo desde el mismo angulo

### 1.2. Independencia de escenarios
- Cada escenario debe poder ejecutarse de forma aislada
- No depender de resultados de otros escenarios
- Definir precondiciones claras para cada caso
- No asumir un estado previo no declarado

### 1.3. Reproducibilidad
- Los pasos deben ser lo suficientemente detallados para que cualquier persona los ejecute
- Evitar instrucciones ambiguas como "probar diferentes valores"
- Especificar datos concretos de prueba cuando sea necesario
- Indicar el estado inicial requerido del sistema

### 1.4. Trazabilidad
- Cada escenario debe tener un identificador unico
- Vincular a la categoria EXPLORA correspondiente
- Indicar la fuente de informacion de la que se derivo (captura, documento, codigo, HTML)
- Registrar la tecnica creativa utilizada para generarlo

### 1.5. Realismo
- No proponer pruebas que requieran herramientas inexistentes
- Asegurar que el escenario es ejecutable con recursos razonables
- No inventar funcionalidades ni comportamientos no deducibles de la entrada
- Considerar las limitaciones tecnicas del entorno

### 1.6. Equilibrio coste-beneficio
- Evaluar el esfuerzo de ejecucion frente al valor de deteccion
- Priorizar escenarios de alto impacto con bajo coste de ejecucion
- Marcar escenarios costosos que solo apliquen en contextos criticos
- No generar mas escenarios de los que el equipo puede gestionar

### 1.7. Concision en informes
- **Maximo 4-6 paginas**: el informe debe ser escaneable rapidamente
- **10-20 escenarios detallados**: solo alta prioridad (score >= 6.0)
- **Resto en tabla compacta**: formato resumen para escenarios secundarios
- **Evitar redundancia**: cada informacion aparece una sola vez
- **Top riesgos**: solo mostrar 10-15 riesgos mas criticos
- **Visual y estructurado**: uso de tablas y listas para facilitar lectura

---

## 2. Aspectos transversales a considerar

### 2.1. Accesibilidad
- Navegacion completa solo con teclado
- Compatibilidad con lectores de pantalla
- Contraste de colores (WCAG 2.1 nivel AA minimo)
- Textos alternativos en contenido no textual
- Orden logico de tabulacion
- Etiquetas asociadas a campos de formulario
- Mensajes de error comunicados a tecnologias asistivas
- Tamano minimo de areas interactivas (44x44 px)

### 2.2. Internacionalizacion (i18n)
- Caracteres de alfabetos no latinos (cirilico, arabe, chino, japones)
- Textos RTL (derecha a izquierda)
- Formatos de fecha segun locale
- Formatos numericos (separador decimal, separador de miles)
- Monedas y simbolos
- Pluralizacion correcta
- Cadenas que se expanden significativamente al traducir (aleman, finlandes)

### 2.3. Privacidad y datos personales
- Datos sensibles no visibles en logs ni URLs
- Campos de contrasena enmascarados
- Sesiones que expiran correctamente
- Opcion de eliminar datos personales (derecho al olvido)
- Consentimiento explicito para recoleccion de datos

### 2.4. Rendimiento percibido
- Tiempo de carga inicial aceptable
- Feedback visual durante operaciones lentas
- Contenido above-the-fold carga primero
- No bloqueo de interfaz durante procesamiento
- Indicadores de progreso en operaciones largas

### 2.5. Consistencia
- Terminologia uniforme en toda la aplicacion
- Comportamiento predecible de elementos similares
- Mensajes de error con formato y tono consistente
- Patrones de interaccion repetidos (confirmacion antes de eliminar, etc.)
- Jerarquia visual coherente

---

## 3. Antipatrones a evitar

### 3.1. En la generacion de escenarios
- No generar escenarios genericos sin contexto especifico
- No copiar listas de pruebas de plantillas sin adaptarlas
- No proponer el mismo escenario con variaciones insignificantes
- No ignorar el contexto de negocio al proponer pruebas tecnicas
- No generar escenarios imposibles de verificar
- **No generar demasiados escenarios**: calidad sobre cantidad (10-20 detallados ofrece buena cobertura)

### 3.2. En la comunicacion con el ingeniero
- No presentar informes abrumadores con decenas de escenarios detallados
- No omitir la justificacion tecnica de un escenario
- No mezclar niveles de prioridad sin contexto claro
- No usar jerga tecnica sin explicacion cuando sea necesario
- **No generar informes de mas de 4-6 paginas**: mantener concision con cobertura adecuada

### 3.3. En la documentacion
- No dejar escenarios sin categorizar
- No omitir precondiciones criticas en escenarios de alta prioridad
- No usar pasos ambiguos o incompletos
- No olvidar el resultado esperado
- **No documentar exhaustivamente escenarios de baja prioridad**: usar tabla compacta
- **No incluir informacion redundante**: cada dato aparece una sola vez

---
