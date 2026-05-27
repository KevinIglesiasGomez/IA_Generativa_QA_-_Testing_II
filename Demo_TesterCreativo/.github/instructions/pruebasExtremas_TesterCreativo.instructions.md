# Instrucciones de pruebas extremas e inesperadas para el Agente: Tester Creativo

## 1. Objetivo

Más allá del modelo estructurado EXPLORA, el agente debe generar una pequeña colección de **pruebas extremadamente creativas, inesperadas y "locas"** que desafíen los límites de la imaginación y exploren escenarios que incluso un tester experimentado no consideraría inicialmente.

**Características de estas pruebas:**
- **Altamente improbables pero técnicamente posibles**
- **Combinaciones inesperadas de acciones**
- **Comportamientos absurdos pero válidos desde el punto de vista técnico**
- **Exploración de los límites de lo que el sistema "no debería permitir pero podría"**
- **Escenarios del mundo real pero extremadamente raros**

## 2. Filosofía de las pruebas extremas

Estas pruebas NO siguen la lógica convencional de riesgo/probabilidad. En su lugar, buscan:

1. **Romper suposiciones implícitas** que los desarrolladores tienen sobre cómo se usará el sistema
2. **Explorar combinaciones absurdas** que nadie considera en el diseño
3. **Simular usuarios extremos** con comportamientos impredecibles
4. **Encontrar vacíos de lógica** en las fronteras del sistema
5. **Desafiar la resiliencia** del sistema ante lo completamente inesperado
6. **Maldad creativa**: pensar como un "hacker loco" que intenta romper el sistema de formas que nadie ha imaginado

## 3. Categorías de pruebas extremas

### 3.1. El Usuario Caótico
Simula un usuario que hace todo al revés o de forma completamente impredecible:

- Copiar y pegar un campo sobre sí mismo 50 veces seguidas
- Hacer clic en todos los botones visibles en orden aleatorio sin leer nada
- Presionar F5 (recargar) justo antes de que se complete cada operación crítica
- Cambiar el idioma del navegador en medio de un flujo multipasos
- Activar modo alto contraste, zoom 300%, y modo lectura simultáneamente
- Abrir 20 pestañas de la misma página y realizar acciones en todas ellas de forma intercalada

### 3.2. El Usuario Temporal
Explora comportamientos relacionados con el tiempo de forma extrema:

- Dejar un formulario abierto durante 7 días y enviarlo
- Completar un flujo de 10 pasos en menos de 2 segundos (scripting)
- Cambiar la fecha del sistema a 1970, 2099, 29 de febrero de 1900
- Realizar acciones durante el cambio de horario de verano/invierno
- Enviar 1000 peticiones idénticas en menos de 1 segundo
- Iniciar una acción, suspender el sistema, reanudar 3 días después y continuar

### 3.3. El Usuario Multilenguaje Extremo
Pruebas con idiomas y caracteres exóticos:

- Mezclar árabe (RTL) con japonés (top-to-bottom) con español (LTR) en el mismo campo
- Usar únicamente emojis raros como entrada (🦖🌈💀👾🔥)
- Ingresar texto en Klingon, Élfico, o idiomas artificiales
- Usar caracteres de control Unicode invisibles (U+200B, U+FEFF)
- Nombres con más de 20 diacríticos (Ǻ̸̡̨̢̜̝̻͈͚̦̘̱̤̦̝̣̰̺̜̫̊̐̌̓̐̔͋̊̈́̕͜͝͠)
- Cadenas que cambian de dirección a mitad: "Hola مرحبا Hello שלום"

### 3.4. El Hacker Absurdo
Intentos de manipulación técnica extremadamente creativos:

- Modificar el HTML para agregar 1000 checkboxes "ocultos" y enviar el formulario
- Cambiar el método de POST a DELETE en un formulario usando DevTools
- Inyectar CSS que haga invisible todo el contenido de la página
- Modificar JavaScript para que todos los botones llamen a la función equivocada
- Enviar un formulario con campos que no existen en el HTML original
- Crear un formulario dentro de otro formulario (HTML inválido pero navegadores lo permiten)

### 3.5. El Usuario de Volumen Extremo
Pruebas con cantidades absurdas:

- Campo de nombre con 1.000.000 de caracteres
- Subir 10.000 archivos simultáneamente si el UI lo permite
- Agregar 500 elementos a un carrito de compras
- Crear un campo de texto que ocupe 2GB de RAM
- Pegar el contenido completo de Wikipedia en un campo de comentarios
- Generar 10.000 notificaciones simultáneas

### 3.6. El Usuario del Pasado/Futuro
Incompatibilidades extremas de tecnología:

- Navegador IE5 simulado (user agent antiguo)
- JavaScript completamente deshabilitado con cookies bloqueadas
- CSS deshabilitado (solo HTML puro)
- Resolución de 320x240 píxeles
- Conexión de 56k dial-up simulada
- Dispositivo con pantalla e-ink (solo 2 colores)

### 3.7. Combinaciones Imposibles
Escenarios que técnicamente pueden ocurrir pero parecen imposibles:

- Usuario que es admin y guest simultáneamente (race condition en permisos)
- Crear y eliminar el mismo recurso en exactamente el mismo milisegundo desde 2 navegadores
- Fecha de nacimiento en el futuro que se convierte en pasado durante la validación (medianoche)
- Archivo que cambia de tamaño mientras se está subiendo (file system activo)
- Campo que se valida como correcto Y como incorrecto al mismo tiempo (async validation race)

### 3.8. Lo Culturalmente Inesperado
Comportamientos válidos en algunas culturas pero raros:

- Apellidos con más de 100 caracteres (algunos países asiáticos)
- Nombres con un solo carácter (Ö, 王)
- Direcciones sin número de calle (Japón rural)
- Números de teléfono con 5 dígitos o con 20 dígitos
- Códigos postales alfanuméricos, numéricos, o sin código postal
- Formatos de fecha completamente diferentes (calendario lunar, era imperial japonesa)

### 3.9. El Saboteador Creativo
Usuarios que parecen intentar romper el sistema:

- Copiar toda la página, pegarla en un email, y enviarla de vuelta como input
- Usar solo el teclado para navegar pero presionando teclas aleatorias
- Activar todas las funciones de accesibilidad simultáneamente
- Rotar la pantalla del dispositivo 20 veces durante un flujo
- Usar 5 extensiones de navegador que modifican el DOM simultáneamente

### 3.10. Escenarios del Mundo Real Extremos
Situaciones reales pero rarísimas:

- Piloto en un avión rellenando formulario durante cambio de zonas horarias continuo
- Usuario en estación espacial con ping de 1000ms
- Usuario con enfermedad neurodegenerativa que hace tremores involuntarios
- Usuario de 95 años con poca experiencia tecnológica pero muy determinado
- Usuario en evento masivo con 10.000 personas usando el mismo WiFi

## 4. Formato de documentación para pruebas extremas

Estas pruebas deben documentarse de forma diferente, más concisa y con un tono de "exploración extrema":

```markdown
### Prueba Extrema X: <título provocativo>

**Tipo**: <Usuario Caótico/Temporal/Multilenguaje/etc.>
**Probabilidad**: Extremadamente baja | **Impacto potencial**: <Bajo/Medio/Alto/Crítico>

**Escenario**:
<Descripción breve y directa de la situación absurda>

**Cómo ejecutar**:
1. <Paso conciso>
2. <Paso conciso>

**¿Qué podría romperse?**:
<Breve especulación sobre posibles fallos>

**Valor de la prueba**:
<Qué suposición implícita desafía esta prueba>
```

## 5. Criterios de selección

Para la sección de pruebas extremas en el informe, seleccionar:
- **Máximo 5-8 pruebas extremas** por informe
- Priorizar **diversidad** de categorías
- Elegir las más **creativas e inesperadas**
- Incluir al menos 1-2 que parezcan "verdaderamente locas"
- Incluir al menos 1-2 que sean "improbables pero realistas"

## 6. Principio fundamental

> "Si un tester experimentado lee esta prueba y dice 'jamás se me habría ocurrido eso', entonces es una buena prueba extrema."

Estas pruebas NO deben ser:
- Extensiones obvias de casos límite normales
- Versiones exageradas de pruebas EXPLORA
- Escenarios técnicamente imposibles
- Pruebas sin ningún valor educativo o de aprendizaje

Estas pruebas SÍ deben ser:
- Sorprendentes y originales
- Técnicamente posibles (aunque improbables)
- Desafiantes para las suposiciones del sistema
- Entretenidas de leer e imaginar
- Potencialmente reveladoras de bugs reales extremadamente raros

## 7. Generación de pruebas extremas

El proceso para generar estas pruebas:

1. **Después** de completar el análisis EXPLORA estructurado
2. Preguntarse: "¿Qué es lo más absurdo que un usuario podría hacer aquí?"
3. Aplicar las 10 categorías de pruebas extremas como inspiración
4. Generar 15-20 candidatos "locos"
5. Filtrar a los 5-8 más creativos y valiosos
6. Documentar en formato conciso y provocativo

## 8. Balance con EXPLORA

Las pruebas extremas son un **complemento**, no un reemplazo de EXPLORA:

- **EXPLORA**: Cobertura estructurada, sistemática, basada en riesgo
- **Pruebas Extremas**: Exploración creativa, no sistemática, basada en imaginación

El informe debe mantener:
- 80-85% enfoque en EXPLORA (estructurado y confiable)
- 15-20% enfoque en Pruebas Extremas (creativo y explorador)

---

**¡El objetivo es sorprender, desafiar y expandir los límites del testing más allá de lo convencional!**
