|  |
| --- |
| **Requisitos generales** |
| Como un usuario con rol de perito o de taller, desde la pestaña TASACIÓN permite iniciar el flujo de tasación y preseleccionar los datos necesarios para acceder al flujo central. |

# Información previa

### JIRA


### Diseño
<https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=45-1080&m=dev>

# Historias de usuario

## Historia 1: Entrada a Tasación desde la tabbar APROBADA

Esta historia es para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Pulse en la opción TASACIÓN de la tabbar | Se muestra la vista MATRÍCULA.Esta vista contiene los siguientes elementos: - Cabecera:     - Título de opción del tabbar: "Tasación".     - Botón de cambio de método de introducción de matrícula. - Contenido:     - El contenido de la vista se mostrará según se indica en la historia 3.     - Tabbar con la opción TASACIÓN seleccionada. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=6424-188383&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de crear de la sección de **botones flotantes** en la vista VEHÍCULOS DE TALLER | Se muestra la vista MATRÍCULA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón volver.     - Título: "Añadir matrícula".     - Botón de cambio de método de introducción de matrícula. - Contenido:     - El contenido de la vista se mostrará según se indica en la historia 3. **Notas**: - Esto se corresponde con el criterio 17 de la historia 10 de [Trabajo pendiente](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario#Historia-10%3A-Veh%C3%ADculos-de-un-taller-aprobada). - La variación de esta vista con respecto al criterio previo es que la cabecera es distinta y que no tiene tabbar. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=6424-196346&m=dev> |

## Historia 2: Detalle de taller (entrada a tasación desde otros flujos) APROBADAPENDIENTE UX

Esta historia es para usuarios con rol de perito y taller.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | PENDIENTE UX | Un cliente logado con el rol de taller  | Pulse en la opción TASACIÓN en la tabbar de la home | Se muestra la vista VEHÍCULOS DE UN TALLER, tal y como está definida en la Historia 10 de Trabajo pendiente: [Consulta de trabajo pendiente - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario) |
| 2 | APROBADO | Un cliente logado con el rol de taller  | Pulse sobre una agrupación de tasaciones en la vista VEHÍCULOS DE TALLERY todos los **servicios** funcionen correctamente | Va a la historia 9 → Inicio tasación.**Nota**: Esto corresponde al criterio 11 de la historia 10 de Trabajo pendiente: [Consulta de trabajo pendiente - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario) |
| 3 | APROBADO | Un cliente logado con el rol de taller  | Pulse sobre una agrupación de tasaciones en la vista VEHÍCULOS DE TALLERY el **servicio de obtener siniestros por matrícula** falla | Va a la historia 9 → Inicio tasación, pero con los siniestros vacíos.**Nota**: Esto corresponde al criterio 13 de la historia 10 de Trabajo pendiente: [Consulta de trabajo pendiente - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario) |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de crear de la sección de **botones flotantes** en la vista VEHÍCULOS DE TALLER | Se muestra la vista MATRÍCULA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón volver.     - Título: "Añadir matrícula".     - Botón de cambio de método de introducción de matrícula. - Contenido:     - El contenido de la vista se mostrará según se indica en la historia 3. **Nota**: Esto se corresponde con el criterio 17 de la historia 10 de [Trabajo pendiente](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario#Historia-10%3A-Veh%C3%ADculos-de-un-taller-aprobada).**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=6424-196346&m=dev> |

## Historia 3: Introducir matrícula APROBADA

 Esta historia es para usuarios con rol de perito y taller.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado | Entre en la vista MATRÍCULAY los permisos de cámara están activos | Se muestra la vista MATRÍCULA en modo OCR.Esta vista contiene la estructura que corresponda según las historias 1 y 2. Lo que varía es el contenido: - Sección OCR: vista de la cámara para hacer el OCR en esta misma pantalla. Sobre esta vista aparecen:     - Texto informativo: "Escanea una matrícula para continuar".     - Recuadro azul, para ayudar al usuario a encuadrar la matrícula. Este recuadro restringe la zona de reconocimiento de OCR a esta zona de la imagen.     - Botón de flash, alineado arriba a la derecha. Por defecto estará apagado. Además, en la cabecera, el botón de cambio de método de introducción de matrícula muestra como icono un teclado.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=6424-188383&m=dev> |
| 2 | APROBADO | Un cliente logado | Pulse el botón de cambio de método de introducción de matrículaY la vista MATRÍCULA está en modo OCR | La vista cambia al modo INTRODUCCIÓN MANUAL.Esta vista contiene la estructura que corresponda según las historias 1 y 2. Lo que varía es el contenido: - Sección de introducción manual: contiene los siguientes elementos:     - Campo de texto de matrícula con la lupa a la izquierda y el texto "Introduce la matrícula…". Al entrar en la vista se hace foco sobre este campo y aparece el teclado. Además, en la cabecera, el botón de cambio de método de introducción de matrícula muestra como icono una cámara. |
| 3 | APROBADO | Un cliente logado | Pulse el botón de cambio de método de introducción de matrícula Y la vista MATRÍCULA está en modo INTRODUCCIÓN MANUAL | La vista cambia a modo OCR, como en el criterio 1.Si el flash estaba encendido, debe apagarse. |
| 4 | APROBADO | Un cliente logado | Entre en la vista MATRÍCULAY los permisos de cámara no se han solicitado nunca | Se muestra la vista MATRÍCULA en modo INTRODUCCIÓN MANUAL, en la cual debajo del campo de texto de matrícula aparecerá un aviso informativo de color azul: - Icono info. - Título: "Sin acceso a la cámara". - Descripción: "Activa el permiso en ajustes para escanear la matrícula." - Enlace: "Activar permiso". Además, el botón de cambio de método de introducción de matrícula se deshabilita.En este caso, también debe hacer foco en el campo de matrícula nada más entrar en la vista. |
| 5 | APROBADO | Un cliente logado | Entre en la vista MATRÍCULAY los permisos de cámara se han rechazado | Se muestra la vista MATRÍCULA en modo INTRODUCCIÓN MANUAL, en la cual debajo del campo de texto de matrícula aparecerá un aviso informativo de color azul: - Icono info. - Título: "Sin acceso a la cámara". - Descripción: "Activa el permiso en ajustes para escanear la matrícula." - Enlace: "Ir a Ajustes". Además, el botón de cambio de método de introducción de matrícula se deshabilita.En este caso, también debe hacer foco en el campo de matrícula nada más entrar en la vista. |
| 6 | APROBADO | Un cliente logado | Pulse en el botón de flash en la vista MATRÍCULA en modo OCRY el flash está encendido | Se realizan las siguientes acciones: - Se apaga el flash de la cámara. - Se cambia el icono del flash. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=4534-82954&m=dev> **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=4534-82954&m=dev> |
| 7 | APROBADO | Un cliente logado | Pulse en el botón de flash en la vista MATRÍCULA en modo OCRY el flash está apagado | Se realizan las siguientes acciones: - Se enciende el flash de la cámara. - Se cambia el icono del flash. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=4534-82954&m=dev> |
| 8 | APROBADO | Un cliente logado | Pulse en Activar permiso en el aviso de permisos faltantes en la vista MATRÍCULA en modo INTRODUCCIÓN MANUAL | Solicita el permiso de cámara. |
| 9 | APROBADO | Un cliente logado | Pulse en Ir a Ajustes en el aviso de permisos faltantes en la vista MATRÍCULA en modo INTRODUCCIÓN MANUAL | Debe llevar a Ajustes, a la sección más cercana posible al uso del permiso de cámara. |
| 10 | APROBADO | Un cliente logado | Pulse en el botón ENTER del teclado en la vista MATRÍCULA en modo INTRODUCCIÓN MANUAL | Se valida la matrícula. La expresión regular está definida en **Información anexa**. |
| 11 | APROBADO | Un cliente logado | Pulse en el botón ENTER del teclado en la vista MATRÍCULA en modo INTRODUCCIÓN MANUALY el formato de la matrícula es incorrecto | Se muestra un error de formato en el campo de matrícula: "La matrícula debe contener como máximo 9 caracteres. Estos caracteres solo pueden ser letras y números."**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=6566-15912&m=dev> |
| 12 | APROBADO | Un cliente logado | Pulse en el botón ENTER del teclado en la vista MATRÍCULA en modo INTRODUCCIÓN MANUALY el formato de la matrícula es correcto | Se realizan las siguientes acciones: 1. Se muestra la vista de carga:     - Título: "Procesando matrícula…".     - Descripción: "Por favor, espere." 2. Se realiza el procedimiento de captura del color de vehículo sobre la imagen del vehículo del instante en que funcionó el OCR de matrícula. 3. Se llama a los servicios necesarios para continuar el proceso:     1. **Servicio de obtener pólizas por matrícula**     2. **Servicio de búsqueda de siniestros por matrícula**     3. **Servicio de obtener tasaciones abiertas**     4. **Servicio de obtener tipos de siniestro**     5. **Servicio de obtener histórico de las tasaciones** **Notas**: - Este flujo se muestra con más detalle en la página de Servicios de este análisis (sección Flujos completos por historia \> Historia 3 - Al introducir una matrícula): [\[Servicios\] \[Tasación\] Entrada a tasación y preselección](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1502185023/Servicios+Tasaci+n+Entrada+a+tasaci+n+y+preselecci+n) - La captura del color queda pendiente de aclarar con negocio el funcionamiento concreto, porque tal y como funciona la app actual, el valor capturado no tiene efecto. **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 13 | APROBADO | Un cliente logado | Se detecte la matrícula mediante OCR en la vista MATRÍCULA en modo OCR | Se realiza el mismo procedimiento que en el criterio anterior, pero mostrando la carga dentro de la propia vista de OCR: - Al recuadro azul resaltado, se agrega un fondo semitransparente y se muestran dentro:     - *Spinner* de carga la izquierda, en movimiento.     - Matrícula identificada mediante OCR. Además, si el flash estaba encendido, debe apagarse.**Nota**: En este caso no hay validación de formato, ya que no deberíamos devolver una matrícula que no coincida con dicho formato.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=4643-18931&m=dev> |
| 14 | APROBADO | Un cliente logado | Responden los servicios en la vista MATRÍCULAY no hay referencias de póliza, no hay siniestros sin tasación y no hay tasaciones abiertas | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Si la vista está en modo OCR, se limpia el contenido del recuadro azul y empieza a evaluar el OCR de nuevo. - Se muestra un aviso de error:     - Título: "Lo sentimos"     - Descripción:         - Si el servicio que ha fallado ha devuelto un error, mostramos ese texto.         - En caso contrario, mostramos: "Ha ocurrido un error al buscar la póliza". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 15 | APROBADO | Un cliente logado | Responden los servicios en la vista MATRÍCULAY hay referencias de póliza, hay siniestros sin tasación y hay tasaciones abiertasY hay más de una póliza en la respuesta del **servicio de obtener pólizas por matrícula** | Va a la historia 4 → Listado de pólizas. |
| 16 | APROBADO | Un cliente logado | Responden los servicios en la vista MATRÍCULA Y hay referencias de póliza, hay siniestros sin tasación y hay tasaciones abiertasY no hay pólizas en la respuesta del **servicio de obtener pólizas por matrícula** | Va a la historia 9 → Inicio tasación. |
| 17 | APROBADO | Un cliente logado | Responden los servicios en la vista MATRÍCULAY hay referencias de póliza, hay siniestros sin tasación y hay tasaciones abiertasY hay una única póliza en la respuesta del **servicio de obtener pólizas por matrícula** | 1. Se carga el detalle de la póliza:     1. Llama al **servicio de obtener póliza por referencia**.     2. Llama al **servicio de obtener póliza futura por referencia**. 2. Si la póliza del **servicio de obtener póliza por referencia** tiene `codigoNegocio`, se llama al **servicio de obtener comprobaciones de negocio**. 3. Si la póliza futura no coincide con la matrícula introducida:     1. Llama al **servicio de buscar póliza antigua por fecha**. **Nota**: Este flujo se muestra con más detalle en la página de Servicios de este análisis (sección Flujos completos por historia \> Historia 1 - Al introducir una matrícula). |
| 18 | APROBADO | Un cliente logado | Termina de cargar el detalle de la póliza en la vista MATRÍCULAY hay siniestros sin tasación o hay tasaciones abiertas | Se realizan las siguientes acciones: - Se comprueba si la póliza tiene un mensaje de alerta (ver Información anexa \> Definición de mensaje de alerta de la póliza). - Va a la historia 9 → Inicio tasación. |
| 19 | APROBADO | Un cliente logado | Termina de cargar el detalle de la póliza en la vista MATRÍCULAY no hay siniestros sin tasación y no hay tasaciones abiertas | Se realizan las siguientes acciones: - Se comprueba si la póliza tiene un mensaje de alerta  (ver Información anexa \> Definición de mensaje de alerta de la póliza). - Inicia una nueva tasación directamente, es decir, va al flujo central de tasación. **Nota**: Esto se implementará en ese flujo. |

### Información técnica

#### Validación de matrícula

La expresión regular para validar la matrícula, como mínimo, podría ser: `^[A-Z0-9]{1,9}$`

#### Definición de mensaje de alerta de la póliza

Al obtener la póliza actual y la póliza futura se revisan ciertos datos para saber si hay alertas que mostrar en las próximas vistas o en el proceso de tasación. En concreto, si la póliza obtenida del servicio (`polizaServicio`) tiene ciertos datos distintos con respecto a la póliza actual de memoria (`polizaActual`). Las comprobaciones y el cálculo del mensaje de alerta (que será un nuevo campo en el modelo de datos de `poliza`) son:

- Cambio de matrícula:
    - Ocurre si `polizaServicio.vehiculo.matricula` es distinta de `polizaActual.vehiculo.matricula`
    - Definimos `poliza.mensajeAlerta` como "Hasta el día FECHA el vehículo asegurado era MARCA MODELO - MATRICULA", siendo FECHA `polizaActual.fechaUltimoSup`, MARCA `polizaServicio.marcaPeritos.descripcion`, MODELO `polizaServicio.modeloPeritos.descripcion` y MATRICULA `polizaServicio.vehiculo.matricula`.
    - Además, definimos `poliza.cambioVehiculo` = *true*
- Cambio de situación de póliza: 
    - Ocurre si `polizaServicio.situacionPoliza.codigo` es distinto de `polizaActual.situacionPoliza.codigo`
    - Definimos `poliza.mensajeAlerta` como "Hasta el día FECHA la póliza se encontraba a SITUACION", siendo FECHA `polizaActual.fechaUltimoSup` y SITUACION:
        - si `poliza.situacionPoliza.codigo` es 'V': "Vigor"
        - si no, si `poliza.situacionPoliza.codigo` es 'A': "Anulada"
        - si no: "Suspendida"
- Cambio de producto/cobertura: 
    - Ocurre si `polizaServicio.productoSeleccionado.descripcion` es distinto de `polizaActual.productoSeleccionado.descripcion`
    - Definimos `poliza.mensajeAlerta` como "Hasta el día FECHA la cobertura de este vehículo era PRODUCTO", siendo FECHA `polizaActual.fechaUltimoSup` y PRODUCTO `polizaServicio.productoSeleccionado.descripcion`.

#### Detección de matrícula

Para implementar el OCR de matrícula vamos a usar para **iOS Vision/VisionKit** y para **Android, CameraX junto a ML Kit Text Recognition v2**. Ambos pueden funcionar sin conexión de red.

En iOS, Apple te da `VNRecognizeTextRequest` para OCR y `regionOfInterest` para limitar el análisis a una zona concreta. Además, `DataScannerViewController` está presentado por Apple como la forma más sencilla de hacer OCR con cámara en vivo.

En Android, ML Kit Text Recognition v2 está pensado para texto en imagen/vídeo en tiempo real y funciona *on-device*. Además, Google permite elegir entre modelo **bundled** o **unbundled** (detallado más adelante).

##### Prueba de concepto básica

La prueba de concepto que podríamos hacer consistiría en hacer una **captura guiada**:

1. marco visual en pantalla
2. pedir que la matrícula ocupe buena parte de la imagen
3. sacar foto
4. recortar la zona esperada
5. pasar OCR on-device
6. validar el resultado con las reglas de negocio del país/formato

Este enfoque encaja con Vision usando `regionOfInterest` y con ML Kit porque el OCR devuelve estructura de texto y geometría suficiente para trabajar con bounding boxes y líneas.

#### Detección de color del vehículo

Para la detección del color del vehículo no se usará OCR, sino **análisis de imagen sobre la captura final**. Una vez localizada la matrícula y validado su formato, se usará su *bounding box* como referencia para calcular una o varias zonas candidatas de carrocería alrededor de la matrícula. Sobre esas zonas se extraerá el color dominante o medio, se normalizará y se clasificará en un conjunto reducido de colores de negocio: blanco, negro, gris/plata, rojo, azul, verde, amarillo/dorado, naranja, marrón, beige u otro/desconocido.

En iOS, usaríamos la imagen capturada y Core Image o procesamiento directo de píxeles; `CIAreaAverage`, por ejemplo, devuelve una imagen de 1x1 con el color medio de una región concreta.

En Android, CameraX `ImageAnalysis` proporciona una imagen accesible por CPU para visión artificial o ML, y permite recibir *frames* en formatos como YUV o RGBA. ML Kit Text Recognition v2 devuelve bloques, líneas, elementos y símbolos con coordenadas/*bounding boxes*, lo cual se puede usar para localizar la matrícula y reutilizar su geometría.

#### Flujo recomendado

1. Mostrar cámara con marco visual.
2. Pedir que la matrícula ocupe una zona concreta y que se vea parte suficiente del frontal/trasera del coche.
3. Congelar *frame*.
4. Recortar la zona esperada de matrícula.
5. Ejecutar OCR.
6. Validar matrícula con reglas de negocio.
7. Obtener el bounding box final de la matrícula.
8. Calcular zonas candidatas de color alrededor de la matrícula.
9. Extraer color dominante/medio.
10. Clasificar a color de negocio.
11. Devolver:

```
matricula: "1234ABC"
colorVehiculo: "gris/plata"
colorConfidence: 0.74
```

En función de la confianza podríamos trasladar o no el color a la siguiente fase, para procurar no devolver información potencialmente falsa.

#### Listado de colores

- `AMARILLO`
- `AZUL`
- `BLANCO`
- `GRIS`
- `NEGRO`
- `ROJO`
- `VERDE`
- `OTRO`

#### Asociación de colores y valores detectados

La detección devolverá siempre uno de esos valores. Cualquier color que no encaje claramente en las categorías principales se mapeará a **OTRO**.

Para la clasificación inicial se puede trabajar en espacio HSV, ya que permite separar razonablemente bien:

- **tono**: rojo, amarillo, verde, azul
- **saturación**: color intenso frente a blanco/gris/negro
- **brillo**: blanco frente a gris frente a negro

Reglas aproximadas:

```
V < 0.18                      => NEGRO
S < 0.15 && V > 0.82          => BLANCO
S < 0.18                      => GRIS

H 345-360 o 0-15              => ROJO
H 35-65                       => AMARILLO
H 65-170                      => VERDE
H 170-260                     => AZUL

Cualquier otro caso            => OTRO
```

Con esta simplificación:

- **plata** se clasifica como **GRIS**
- **beige**, **dorado**, **marrón**, **naranja**, **morado** y colores poco habituales se clasifican como **OTRO**
- colores oscuros con poca luz pueden caer en **NEGRO**
- colores claros con poca saturación pueden caer en **BLANCO** o **GRIS**

#### Proceso tras la detección

Después de detectar la matrícula, la app realiza más acciones:

- Limpia el estado de tasación previo.
- Prepara una tasación inicial con matrícula y color.
- Busca pólizas asociadas a esa matrícula.
- Busca siniestros sin tasación.
- Busca tasaciones abiertas para esa matrícula.
- Carga tipos de siniestro.
- Si hay varias pólizas, muestra listado de pólizas.
- Si hay siniestros o tasaciones abiertas, va a "Inicio tasación" con agrupaciones.
- Si hay una póliza y no hay siniestros/tasaciones abiertas, puede iniciar una nueva tasación directamente.
- Si inicia una nueva tasación, guarda/abre la tasación, recupera última tasación, valida contra SPTS si hay siniestro seleccionado y navega a datos del siniestro.

## Historia 4: Listado de pólizas APROBADAPENDIENTE UX

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Introduzca una matrículaY los **servicios** respondan correctamenteY haya varias pólizas | Se muestra la vista LISTADO DE PÓLIZAS.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Pólizas".     - Subtítulo: "Vehículo MATRICULA", siendo MATRICULA el campo `referenciasPoliza[0]?.matricula` de la respuesta del **servicio de obtener pólizas para una matrícula**. - Contenido:     - Listado de pólizas, con el listado de pólizas que vienen en `referenciasPoliza` de la respuesta del **servicio de obtener pólizas para una matrícula**. Por cada `referencia` se muestra:         - Línea principal:             - A la izquierda: `referencia.numReferencia` formateado con el formato numérico (puntos para separar los millares).         - Línea secundaria: "SITUACION · DESCRIPCION", siendo SITUACION  `referencia.situacion` y DESCRIPCION `referencia.descripcionProducto`.         - Línea secundaria: `referencia.fechaVencimiento` sumando un día más y formateada como "dd/MM/yyyy".         - Si `referencia.operacion === 'DISCREPANCIA'`: aviso de  Discrepancia con el icono de aviso a la izquierda. No tenemos forma de mostrar el motivo, así que no se agrega. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2047-16178&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver en vista LISTADO DE PÓLIZAS | Vuelve a la vista de INTRODUCIR MATRÍCULA (historias 1 a 3). |
| 3 | PENDIENTE UX | Un cliente logado con el rol de perito  | Haga *swipe* hacia la derecha sobre una póliza en vista LISTADO DE PÓLIZAS | Acción lateral al deslizar: icono de información. |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Haga *swipe* hacia la derecha sobre una póliza en vista LISTADO DE PÓLIZAS y completa la acción | Intenta ir a la Historia 5 -\> Detalle de póliza. |
| 5 | APROBADO | Un cliente logado con el rol de perito  | Pulse en una póliza del listado de la vista LISTADO DE PÓLIZAS | Se realizan las siguientes acciones: 1. Se muestra la vista de carga:     - Título: "Asociando póliza…".     - Descripción: "Por favor, espere." 2. Se llama a los servicios necesarios para continuar el proceso:     1. Se carga el detalle de la póliza:         1. Llama al **servicio de obtener póliza por referencia**.         2. Llama al **servicio de obtener póliza futura por referencia**.     2. Si la póliza del **servicio de obtener póliza por referencia** tiene `codigoNegocio`, se llama al **servicio de obtener comprobaciones de negocio**. **Nota**: En este caso, al buscar la póliza no se envía la matrícula, por lo que no se comprueba si la póliza futura no coincide con la matrícula introducida y, por tanto, no se llama al **servicio de buscar póliza antigua por fecha**.**Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 6 | APROBADO | Un cliente logado con el rol de perito  | Termina de cargar el detalle de la pólizaY el **servicio de obtener póliza por referencia** y el **servicio de obtener póliza futura por referencia** funcionan correctamenteY no hay siniestros sin tasación y no hay tasaciones abiertas | Se realizan las siguientes acciones: - Se comprueba si la póliza tiene un mensaje de alerta (ver Información anexa de la historia 3). - Inicia una nueva tasación directamente (iría a Datos de siniestro). |
| 7 | APROBADO | Un cliente logado con el rol de perito  | Termina de cargar el detalle de la pólizaY el **servicio de obtener póliza por referencia** y el **servicio de obtener póliza futura por referencia** funcionan correctamenteY hay siniestros sin tasación o hay tasaciones abiertas | Se realizan las siguientes acciones: - Se comprueba si la póliza tiene un mensaje de alerta (ver Información anexa de la historia 3). - Va a la historia 9 → Inicio tasación. |
| 8 | APROBADO | Un cliente logado con el rol de perito  | Termina de cargar el detalle de la pólizaY el **servicio de obtener póliza por referencia** o el **servicio de obtener póliza futura por referencia** fallan | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error:     - Título: "Lo sentimos"     - Descripción: "Ha ocurrido un error al obtener el detalle de la póliza". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |

## Historia 5: Detalle de póliza APROBADA

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito | Intente acceder a la vista DETALLE DE PÓLIZAY no tengamos información de la póliza ya cargada | Se muestra la vista DETALLE DE PÓLIZA CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Detalle de póliza". - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama a los servicios: - **Servicio de obtener póliza por referencia**. - **Servicio de obtener daños rechazados**. **Nota**: Si el **servicio de obtener daños rechazados** falla no se bloquea el acceso al DETALLE DE PÓLIZA.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito | Intente acceder a la vista DETALLE DE PÓLIZAY el **servicio de obtener póliza por referencia** falle | Se muestra la vista DETALLE DE PÓLIZA ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Detalle de póliza". - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado con el rol de perito  | Intente acceder a la vista DETALLE DE PÓLIZAY el **servicio de obtener póliza por referencia** funcione correctamente | Se muestra la vista DETALLE DE PÓLIZA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Detalle de póliza". - Contenido:     - Sección: "Datos generales".         - Campo "Matrícula asegurada”, con el texto de `poliza.vehiculo.matricula` o "Sin especificar".         - Campo "Marca”, con el texto de `poliza.marcaPeritos.descripcion` o "Sin especificar".         - Campo "Modelo”, con el texto de `poliza.modeloPeritos.descripcion` o "Sin especificar".         - Campo "Bastidor”, con el texto de `poliza.vehiculo.numBastidor` o "Sin especificar".         - Botón "Verificación de vehículo".         - Botón "Accesorios".     - Sección "Detalle de póliza":         - Campo "Número de póliza”, con el texto de `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares) o "Sin especificar".         - Campo "Fecha de vencimiento”, con el texto de `poliza.fechaVencimiento` sumando un día más y formateada como "dd/MM/yyyy" o "Sin especificar".         - Campo "Producto”, con el texto de `poliza.productoSeleccionado.descripcion` o "Sin especificar".         - Campo "Franquicia”, con el texto de `poliza.productoSeleccionado.franquiciaSeleccionada.codigoFranquicia` o "No aplica".         - Campo "Daños excluidos”, que contendrán:             - si `danosRechazados` está vacío:  texto "No existen daños".             - en caso contrario, se muestra el listado de daños, con el listado de daños que vienen en `danosRechazados`. Por cada `dano` se muestra:                 - Línea principal: `dano.fechaAlta` en formato 'dd/MM/yyyy'.                 - Línea: `dano.causa` (capitalizado).                 - Línea: `dano.observaciones`.         - Botón "Recibos".         - Si la `poliza` del **servicio de obtener póliza por referencia** tiene `codigoNegocio`: botón "Datos de negocio". **Notas**: - Cada elemento `poliza` viene en el campo `referenciasPoliza` de la respuesta del **servicio de obtener pólizas para una matrícula**. El elemento concreto será el que haya seleccionado el usuario en la vista POLIZAS. - Los `danosRechazados` equivalen a la lista de objetos que vienen en la respuesta del **servicio de obtener daños rechazados**. Si el servicio falla, la lista estará vacía por defecto. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Termina de cargar el **servicio de obtener daños rechazados**Y el servicio falla | Se muestra un aviso de error: - Título: "Lo sentimos" - Descripción: "Ha ocurrido un error al cargar los daños rechazados del vehículo". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 5 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista DETALLE DE PÓLIZA | Vuelve a la vista de la que procede (en este caso, al LISTADO DE PÓLIZAS). |
| 6 | APROBADO | Un cliente logado con el rol de perito  | Pulse en Verificación de vehículo en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista VERIFICACIÓN DE VEHÍCULO ERROR | Se muestra la vista VERIFICACIÓN DE VEHÍCULO.**Nota**: Se define en otra historia. |

## Historia 6: Recibos de póliza APROBADA

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón Recibos en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista RECIBOS DE PÓLIZA ERROR | Se muestra la vista RECIBOS DE PÓLIZA CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Recibos".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama al **servicio de obtener de recibos de una póliza**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito | Pulse en el botón Recibos en la vista DETALLE DE PÓLIZAY el **servicio de obtener recibos de una póliza** falle | Se muestra la vista RECIBOS DE PÓLIZA ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Recibos".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón Recibos en la vista DETALLE DE PÓLIZAY el **servicio de obtener recibos de una póliza** funcione correctamenteY no haya recibos | Se muestra la vista RECIBOS DE PÓLIZA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Recibos".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "No hay recibos para esta póliza".     - Sin botones. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2041-31326&m=dev> |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón Recibos en la vista DETALLE DE PÓLIZAY el **servicio de obtener recibos de una póliza** funcione correctamenteY haya algún recibo | Se muestra la vista RECIBOS DE PÓLIZA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Recibos".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Listado de recibos, con el listado de `recibos` que vienen en la respuesta del **servicio de obtener recibos de una póliza**. Por cada `recibo` se muestra:         - Línea principal: `recibo.situacion.descripcion`         - Línea: "Tipo: TIPO (FRECUENCIA)", siendo TIPO `recibo.tipo.descripcion` y FRECUENCIA, `recibo.frecuenciaPagoLiteral`.         - Línea: "Fecha efecto recibo: FECHA", siendo FECHA `recibo.fechaEfecto` en formato `dd/MM/yyyy`. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2041-31326&m=dev> |
| 5 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista RECIBOS DE PÓLIZA | Vuelve a la vista de la que procede (en este caso, al DETALLE DE PÓLIZA). |

## Historia 7: Accesorios de póliza APROBADA

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Pulse en Accesorios en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista ACCESORIOS DE PÓLIZA ERROR | Se muestra la vista ACCESORIOS DE PÓLIZA CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Accesorios".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama a los servicios: - si `poliza.codigoNegocio` y `negocio.idCuentaPrincipal` existen y tienen valor definido: **servicio de obtener reglas para accesorios** - **servicio de obtener accesorios de una póliza**. **Nota**: El elemento `negocio` viene en la respuesta del **servicio de obtener comprobaciones de un negocio**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito | Pulse en Accesorios en la vista DETALLE DE PÓLIZAY el **servicio de obtener accesorios de una póliza** devuelva error | Se muestra la vista ACCESORIOS DE PÓLIZA ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Accesorios".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado con el rol de perito  | Pulse en Accesorios en la vista DETALLE DE PÓLIZAY el **servicio de obtener accesorios de una póliza** funcione correctamenteY no haya accesorios | Se muestra la vista ACCESORIOS DE PÓLIZA VACÍO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Accesorios".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - **Sección de filtros**, en horizontal:         - Botón de buscar (lupa).         - Filtro "Excluido".         - Filtro "De serie".         - Filtro "Opcional".     - Imagen representativa.     - Texto: "No hay accesorios para esta póliza".     - Sin botones. **Diseños**: - <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2205-24399&t=vmHON4tSVKyMmvNh-4> |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en Accesorios en la vista DETALLE DE PÓLIZAY el **servicio de obtener accesorios de una póliza** funcione correctamenteY haya algún accesorio | Se muestra la vista ACCESORIOS DE PÓLIZA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Accesorios".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - **Sección de filtros**, igual que en el criterio 3.     - Lista agrupada por tipo de accesorio obtenida del **servicio de obtener accesorios de una póliza**. Estas agrupaciones solo se muestran si contienen al menos un accesorio. Las agrupaciones son:         - Si `accesorio.tipo` es 'N' -\> "Excluido"         - Si `accesorio.tipo` es 'O' -\> "Opcional"         - Si `accesorio.tipo` es 'S' -\> "De serie"         - Cualquier otro valor de `accesorio.tipo`-\> "Opcional"                    Por cada celda de `accesorio` se muestra:         - Línea principal:              - Si `accesorio.tipo` es 'N': etiqueta roja con el texto de `accesorio.descripcion`.             - En otro caso: texto `accesorio.descripcion`.         - Si `accesorio.tipo` es 'O' y si `accesorio.valor` existe: se agrega un texto a la derecha con "VALOR €", siendo VALOR `accesorio.valor` con 2 decimales. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2205-24399&m=dev> |
| 5 | APROBADO | Un cliente logado con el rol de perito  | Pulse en Accesorios en la vista DETALLE DE PÓLIZAY el **servicio de obtener reglas para accesorios** funcione correctamenteY hay algún mensaje informativo | Se muestra la vista ACCESORIOS DE PÓLIZA.Esta vista contiene los siguientes elementos: - Cabecera, igual al criterio previo. - Contenido, todo será igual al criterio previo, salvo porque se agrega una nueva sección después de la sección de filtros:     - **Listado de avisos**, con el listado de mensajes que vengan en `configPrestacion` del **servicio de obtener reglas para accesorios**. Este listado debe comportarse como si formara parte del listado de accesorios, es decir, deben formar parte del mismo *scroll*. Por cada `mensaje` cuyo `mensaje.nivel` sea ‘INFORMATIVO’, mostraremos:         - Bloque amarillo con el siguiente contenido:             - A la izquierda, icono de aviso.             - Texto `mensaje.descripcion`. No habrá un segundo texto. **Nota**: Si el servicio falla o si funciona, pero no devuelve mensajes, estos avisos no se muestran.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2205-24399&m=dev> |
| 6 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista AVISOS DE PÓLIZA | Vuelve a la vista ACCESORIOS DE PÓLIZA. |
| 7 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista ACCESORIOS DE PÓLIZA | Vuelve a la vista de la que procede (en este caso, al DETALLE DE PÓLIZA). |
| 8 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de buscar en la vista ACCESORIOS DE PÓLIZA | Se realizan las siguientes acciones: - El botón de buscar se selecciona (aparece resaltado). - Aparece el campo de texto de accesorio, debajo de la sección de filtros y encima del contenido. Tendrá el icono de la lupa a la derecha, el aspa de borrado a la derecha y el *placeholder* "Buscar accesorio". **Diseño**: Igual que en la vista VEHÍCULOS DE TALLER. |
| 9 | APROBADO | Un cliente logado con el rol de perito  | Introduzca un carácter en el campo de texto de accesorio de la vista ACCESORIOS DE PÓLIZA | Filtra los elementos del listado para mostrar únicamente los accesorios cuyo `accesorio.descripcion` contenga el texto introducido. |
| 10 | APROBADO | Un cliente logado con el rol de perito  | Pulse uno de los filtros junto al botón Filtros en la vista ACCESORIOS DE PÓLIZA | Se realizan las siguientes acciones: - Se activa o desactiva ese filtro, en función del estado previo. - Se reaplican los filtros sobre el listado de accesorios según apliquen. Si no hay ningún filtro seleccionado, no se filtra por nada (es decir, se muestra la totalidad de los accesorios). |

### Información anexa

#### Filtros 

- Filtro "Excluido": cuando está activo, muestra los accesorios cuyo `tipo` sea 'N'.
- Filtro "De serie": cuando está activo, muestra los accesorios cuyo `tipo` sea 'S'.
- Filtro "Opcional": cuando está activo, muestra los accesorios cuyo `tipo` no sea ‘N' ni 'S'.

Estos filtros se pueden acumular, es decir, si se seleccionan "Excluido" y "De serie" se verán ambos tipos de accesorios.

Si se desmarcan todos los filtros, no aplicará ninguno y, por tanto, se mostrarán todos los accesorios.

## Historia 8: Detalle de negocio APROBADA

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón Datos de negocio en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista DETALLE DE NEGOCIO ERROR | Se muestra la vista DETALLE DE NEGOCIO CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Datos del negocio".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama al **servicio de obtener comprobaciones de negocio**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito | Pulse en el botón Datos de negocio en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista DETALLE DE NEGOCIO ERRORY el **servicio de obtener comprobaciones de negocio** falle | Se muestra la vista DETALLE DE NEGOCIO ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Datos del negocio".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón Datos de negocio en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista DETALLE DE NEGOCIO ERRORY el **servicio de obtener comprobaciones de negocio** funcione correctamente | Se muestra la vista DETALLE DE NEGOCIO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Datos del negocio".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Campo "Negocio", con el texto de  `negocio.nombreNegocio`.     - Campo "Tipo", con el texto de `negocio.nombreTipoNegocio`.     - Campo "Subtipo", con el texto de `negocio.nombreSubtipoNegocio`.     - Campo "Cuenta principal", con el texto "NOMBRE (ID)", siendo NOMBRE `negocio.nombreCuentaPrincipal` e ID, `negocio.idCuentaPrincipal`.     - Si existe algún elemento en `negocio.observacion[]`: Campo "Observaciones". Listado de elementos de `negocio.observacion[]`. Por cada `observacion` se muestra:         - Texto `observacion.descripcionObservacion` **Nota**: El elemento `negocio` viene en la respuesta del **servicio de obtener comprobaciones de un negocio**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2047-35140&m=dev> |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista DETALLE DE NEGOCIO | Vuelve a la vista de la que procede (en este caso, al DETALLE DE PÓLIZA). |

## Historia 9: Inicio de tasación APROBADA

Esta historia es para peritos y talleres.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado | Llegue a Inicio de tasación por cualquier vía posible desde una vista anterior | Se muestra la vista INICIO DE TASACIÓN CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Vehículo MATRICULA", siendo MATRICULA `tasacion.matricula`.     - Botón de información. - Contenido:     - **Sección de datos del vehículo**.     - **Sección de filtro**.     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en la vista, se llama a los servicios: - Si existe `poliza`: **servicio de obtener póliza IDC**. - Si el usuario tiene rol de perito: **servicio de obtener tasaciones cerradas de los últimos 3 días**. **Nota**: En la app híbrida se llama al **servicio de obtener tasaciones cerradas de los últimos 3 días** tanto para peritos como para talleres, pero como este servicio solo sirve para mostrar la categoría de Tasaciones cerradas los últimos 3 días, vemos innecesario llamarlo y así optimizamos la app.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado | Llegue a Inicio de tasación desde una vista posterior (es decir, vuelva atrás)O pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERROR | Se muestra la vista INICIO DE TASACIÓN CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Vehículo MATRICULA", siendo MATRICULA `tasacion.matricula`.     - Botón de información. - Contenido:     - **Sección de datos del vehículo**.     - **Sección de filtro**.     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en la vista, se llama a los servicios: - **Servicio de obtener tasaciones abiertas**. - Si existe `poliza`: **servicio de obtener póliza IDC**. - Si el usuario tiene rol de perito: **servicio de obtener tasaciones cerradas de los últimos 3 días**. **Nota**: En la app híbrida se llama al **servicio de obtener tasaciones cerradas de los últimos 3 días** tanto para peritos como para talleres, pero como este servicio solo sirve para mostrar la categoría de Tasaciones cerradas los últimos 3 días, vemos innecesario llamarlo y así optimizamos la app.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 3 | APROBADO | Un cliente logado con rol de perito | Llegue a Inicio de tasación desde cualquier víaY haya un mensaje de alerta que mostrar | Se muestra el diálogo AVISO MENSAJE ALERTA, con el siguiente contenido:  - Título: "Aviso". - Descripción: Contenido de `poliza.mensajeAlerta`. - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 4 | APROBADO | Un cliente logado | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** falle | Se muestra la vista INICIO DE TASACIÓN ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Vehículo MATRICULA", siendo MATRICULA `tasacion.matricula`.     - Botón de información. - Contenido:     - **Sección de datos del vehículo**.     - **Sección de filtro**.     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 5 | APROBADO | Un cliente logado  | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente | Se muestra la vista INICIO DE TASACIÓN.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Vehículo MATRICULA", siendo MATRICULA `tasacion.matricula`.     - Botón de información. - Contenido:     - **Sección de datos del vehículo**.     - **Sección de filtro**.     - **Listado de tasaciones**.     - Botón "Ver histórico de tasaciones cerradas (últimos 2 años)". Como si fuera una celda más del listado de tasaciones.     - Botón de crear, alineado abajo a la derecha, por encima del listado de tasaciones. Este botón se muestra solo si se cumplen ciertas condiciones (ver **Información anexa**).  **Diseños**: - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-18397&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2154-63073&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2154-63316&m=dev> |
| 6 | APROBADO | Un cliente logado con rol de perito | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente | Se muestra la vista INICIO DE TASACIÓN, en la cual en la **sección de datos del vehículo** se muestra con los siguientes elementos: - Línea principal: "MARCA MODELO", siendo MARCA `poliza.marcaPeritos.descripcion` y MODELO `poliza.modeloPeritos.descripcion`. - Línea secundaria:     - Alineado a la izquierda:         - Si es vehículo no asegurado (ver **Información anexa**): etiqueta "Vehículo no asegurado".         - Si no, si es perjudicado (ver **Información anexa**): etiqueta "Perjudicado".         - En caso contrario: texto "PRODUCTO FRANQUICIA", siendo PRODUCTO `poliza.productoSeleccionado.descripcion` y FRANQUICIA `poliza.productoSeleccionado.franquiciaSeleccionada.codigoFranquicia`.     - Alineado a la derecha:         - Si aplica una etiqueta VIP:             - Si alguna tasación abierta tiene `tasacion.isBansacar` igual a 'S': etiqueta "BSAN".              - Si `tipoPoliza.esPolizaEci` es *true*: etiqueta "ECI" (visualmente, igual a la etiqueta "BSAN", pero con este texto).         - Si `poliza.tomador.segmento` existe: etiqueta de segmento con el texto de `poliza.tomador.segmento`.         - Si aplica una etiqueta de cobertura IDC:             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PM' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "MOVILIDAD".             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PI' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "IMPACTO".             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PT' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "TOP". **Notas**:  - hay datos que no se podrán mostrar hasta que no se carguen las tasaciones, por lo que la vista tendrá que refrescarse cuando esos servicios respondan - `tipoPoliza` es la respuesta del **servicio de obtener comprobaciones de negocio** - `coberturas` es la respuesta del **servicio de obtener póliza IDC** **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2020-27275&m=dev> |
| 7 | APROBADO | Un cliente logado con rol de taller | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente | Se muestra la vista INICIO DE TASACIÓN, en la cual en la **sección de datos del vehículo** se muestra con los siguientes elementos: - Línea principal: "MARCA MODELO", siendo MARCA `poliza.marcaPeritos.descripcion` y MODELO `poliza.modeloPeritos.descripcion`. - Línea secundaria:     - Alineado a la izquierda:         - Si es vehículo no asegurado (ver **Información anexa**): etiqueta "Vehículo no asegurado".         - Si no, si es perjudicado (ver **Información anexa**): etiqueta "Perjudicado".         - En caso contrario: texto "PRODUCTO FRANQUICIA", siendo PRODUCTO `poliza.productoSeleccionado.descripcion` y FRANQUICIA `poliza.productoSeleccionado.franquiciaSeleccionada.codigoFranquicia`.     - Alineado a la derecha:         - Si `tipoPoliza.esPolizaEci` es *true*: etiqueta "ECI" (visualmente, igual a la etiqueta "BSAN", pero con este texto).         - Si aplica una etiqueta de cobertura IDC:             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PM' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "MOVILIDAD".             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PI' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "IMPACTO".             - Si en `coberturas` viene una con el campo `cobertura.tipo` igual a ‘PT' y `cobertura.valor` contiene 'SI’: etiqueta IDC con el texto "TOP". **Notas**:  - hay datos que no se podrán mostrar hasta que no se carguen las tasaciones, por lo que la vista tendrá que refrescarse cuando esos servicios respondan - `tipoPoliza` es la respuesta del **servicio de obtener comprobaciones de negocio** - `coberturas` es la respuesta del **servicio de obtener póliza IDC** **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2020-27275&m=dev> |
| 8 | APROBADO | Un cliente logado con rol de perito | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente | Se muestra la vista INICIO DE TASACIÓN, en la cual en la **sección de filtro** se muestra con los siguientes elementos,  en horizontal: - Botón de lupa: filtro de identificadores. - Botón de filtros. - Filtro "Mías". - Filtro "Otro perito". - Filtro "Taller". |
| 9 | APROBADO | Un cliente logado con rol de taller | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente | Se muestra la vista INICIO DE TASACIÓN, en la cual en la **sección de filtro** se muestra con los siguientes elementos,  en horizontal: - Botón de lupa: filtro de identificadores. **Nota**: El botón de filtros y otros filtros no aplican para usuarios con rol de taller. |
| 10 | APROBADO | Un cliente logado con cualquier tipo de rol | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y no hay tasaciones ni siniestros | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** contiene una vista de estado vacío: - Imagen representativa. - Texto: "No hay tasaciones para esta póliza". - Sin botones. **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2041-31326&m=dev> |
| 11 | APROBADO | Un cliente logado con cualquier tipo de rol | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación | Por cada tasación que se haya obtenido de la lista de tasaciones abiertas, se llama al **servicio de obtener las tareas de una tasación**.Además, por cada tasación en reparto que tenga `tasacion.codigoSiniestro`, se llama al **servicio de obtener detalle del siniestro**.**Nota**: Esto solo ocurre para las celdas de tasación, no para las de siniestro. |
| 12 | APROBADO | Un cliente logado con rol de perito | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación o siniestro | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** contiene el listado de tasaciones o siniestros categorizados en función de las condiciones que cumplan. El listado de posibles categorías para este caso es: - `Tasaciones erróneas` - `Avisos peritación` - `Siniestros sin tasación` - `Tasaciones abiertas pte autorizar` - `Tasaciones abiertas pte validar` - `Tasaciones abiertas pte info` - `Tasaciones abiertas` - `Tasaciones cerradas pte autorizar` - `Tasaciones cerradas pte validar` - `Tasaciones cerradas pte info` - `Tasaciones inacabadas` - `Tasaciones cerradas por taller (últimos 3 días)` |
| 13 | APROBADO | Un cliente logado con rol de taller con nivel de confianza distinto de 9 | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación o siniestro | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** contiene el listado de tasaciones o siniestros categorizados en función de las condiciones que cumplan. El listado de posibles categorías para este caso es: - `Tasaciones erróneas` - `Siniestros sin tasación` - `Tasaciones abiertas pte autorizar` - `Tasaciones abiertas pte info` - `Tasaciones abiertas` - `Tasaciones cerradas pte autorizar` - `Tasaciones inacabadas` - `Tasaciones anuladas` |
| 14 | APROBADO | Un cliente logado con rol de taller con nivel de confianza 9 | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación o siniestro | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** contiene el listado de tasaciones o siniestros categorizados en función de las condiciones que cumplan. El listado de posibles categorías para este caso es: - `Tasaciones erróneas` - `Avisos peritación` - `Siniestros sin tasación` - `Tasaciones abiertas pte autorizar` - `Tasaciones abiertas pte info` - `Tasaciones abiertas` - `Tasaciones cerradas pte autorizar` - `Tasaciones inacabadas` - `Tasaciones anuladas` |
| 15 | APROBADO | Un cliente logado con el rol de perito  | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** muestra por cada celda de `tasacion` los siguientes elementos: - Línea principal:     - A la izquierda:         - Identificador:             - Si `tasacion.codigoSiniestro` existe, se muestra el siniestro con formato `CODIGO/AÑO`, usando `tasacion.codigoSiniestro` y `tasacion.anioSiniestro`.             - Si `tasacion.codigoSiniestro` no existe, se muestra `tasacion.codigoPoliza` formateada con separador de miles.         - Etiqueta con el tipo de siniestro, según el valor de `tasacion.tipoSiniestro`.     - A la derecha:          - Si existe `tasacion.situacionFacturacion` y la tasación está cerrada: etiqueta con el estado del pago:             - si `tasacion.situacionFacturacion` es menor que 90 → etiqueta verde con texto "Disponible"             - si `tasacion.situacionFacturacion` es 97 → etiqueta azul con texto "Pagado"             - si `tasacion.situacionFacturacion` es `98`, `96` o `93` → etiqueta roja con texto "Bloqueo”             - si `tasacion.situacionFacturacion` es `92` → etiqueta gris con texto "Anulado”             - en otro caso → no se muestra esta etiqueta         - Si existe `tasacion.totalPeritado`: texto con `tasacion.totalPeritado` en formato con 2 decimales y moneda €. - Lista de etiquetas, que debe ocupar tantas líneas como necesite para mostrar todas las etiquetas necesarias:     - Si está en proceso el **servicio de obtener las tareas de una tasación** o el **servicio de obtener detalle del siniestro** para la tasación de esta celda, se muestra la etiqueta de carga. Es una etiqueta sin texto con un gradiente que se anima como un skeleton.  **Nota**: Que se muestre esta etiqueta de carga no implica que no se muestren otras si es posible. Es un aviso de que aún no se han terminado de cargar todas las posibles etiquetas.     - Iconos de conversación. Si la tasación tiene conversación abierta asociada a tareas de comunicación: iconos de conversación o mensajería:         - Si hay una conversación con taller visible para perito: icono de conversación gris.         - Si hay un mensaje con perito no asignado al usuario: icono de comentario rojo con puntito.         - Si hay un mensaje con perito asignado al usuario: icono de comentario gris.     - Etiqueta del creador:         - si `tasacion.codigoPerito` es igual al id del usuario logado: no se muestra etiqueta.         - si `tasacion.codigoPerito` tiene tamaño 7: etiqueta con el valor de `tasacion.codigoPerito` e icono de taller a la izquierda.         - en caso contrario: etiqueta con el valor de `tasacion.codigoPerito` e icono de perito a la izquierda.     - Si la póliza seleccionada no coincide con la póliza de la tasación (cuando existe póliza cargada y `poliza.numReferencia !== tasacion.codigoPoliza`): etiqueta "Incidencia póliza".     - Si la tasación está pendiente de consolidar (`tasacion.isPendienteConsolidar` es *true*): etiqueta "Pte. consolidar".     - Si la tasación está en borrador (`tasacion.borrador` es 1): etiqueta "Borrador".     - Si la tasación no procede de Pruebas Seguros o cuando su motor no es STAR (si `tasacion.aplicacionModificacion` no existe o, si existe, no contiene "21"; o `tasacion.motor` no es ‘ST’): etiqueta del motor de valoración con el texto `tasacion.motor` traducido:         - si `tasacion.motor` es AU → el texto es AU         - si `tasacion.motor` es EI → el texto es GT         - si `tasacion.motor` es DT → el texto es DAT     - Si `tasacion.nps` es *true*: etiqueta "NPS". - Líneas con textos descriptivos, en líneas independientes:     - Si la tasación está en reparto y existe `tasacion.danyos`: `tasacion.danyos`.     - Si la tasación está en reparto y existe `tasacion.descripcionAccidente`:  `tasacion.descripcionAccidente`.     - Si la tasación no está en reparto y existe `tasacion.detalleDanyos`: `tasacion.detalleDanyos`.     - Si la tasación está en reparto o anulada y existe `tasacion.comentariosAviso`: `tasacion.comentariosAviso`.   **Nota**: Este texto se pintaba con un icono de info en la app híbrida. Se descarta en la app actual.     - Si la tasación está en reparto: "FECHA AVISO: FECHA\_PERITACION", siendo FECHA\_PERITACION `tasacion.fechaPeritacion`, con formato "dd/MM/yyyy". - Línea secundaria:     - Fecha de tasación, cuyo texto es:         - Si en la vista de filtro está seleccionado el botón "Apertura" en Tipo fecha: `tasacion.fechaCreacion`, formateada como "dd/MM/yyyy HH:mm".         - Si en la vista de filtro está seleccionado el botón "Modificación" en Tipo fecha: `tasacion.fechaModificacion`, con el mismo formato.         - En otro caso:             - Si es reparto o no existe `tasacion.fechaModificacion`: `tasacion.fechaCreacion`, con el mismo formato.             - En otro caso: `tasacion.fechaModificacion`, con el mismo formato.     - Si la tasación la ha hecho un taller y está definido el nivel de confianza (`tasacion.codigoPerito.length` no es 5 y existe `tasacion.nivelConfianzaTasacion)`: etiqueta con `tasacion.nivelConfianzaTasacion`.         - Nota: Cuando esta vista se usa en el flujo de Inspección, la condición es simplemente que exista `tasacion.nivelConfianzaTasacion`. **Diseño**:  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2154-14348&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-18542&m=dev>  Ejemplo de celda de tasación completoEtiqueta de carga |
| 16 | APROBADO | Un cliente logado con el rol de taller  | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay alguna tasación | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** muestra por cada celda de `tasacion` los siguientes elementos: - Línea principal:     - A la izquierda:         - Identificador, igual que para perito.         - Etiqueta con el tipo de siniestro, según el valor de `tasacion.tipoSiniestro`.     - A la derecha:          - Situación de facturación, no se muestra, al contrario que para perito.         - Total peritado, igual que para perito, pero se mostrará únicamente bajo ciertas condiciones (ver **Información anexa**). - Lista de etiquetas, que debe ocupar tantas líneas como necesite para mostrar todas las etiquetas necesarias. Son las mismas etiquetas salvo por estas excepciones:     - Iconos de conversación. Es diferente a la de perito. Si la tasación tiene conversación abierta asociada a tareas de comunicación, iconos de conversación o mensajería:         - Si hay mensaje con taller no asignado al usuario es 1:  icono de comentario rojo con puntito.         - Si hay mensaje con taller asignado al usuario:  icono de comentario gris.     - Etiqueta "Mod." con el icono de MM a la izquierda". Aparece cuando se indica en **Información anexa \> Modificada por MM**.     - El resto de etiquetas se muestran igual que para perito. - Líneas con textos descriptivos, en líneas independientes, igual que para perito. - Línea secundaria:     - Fecha de tasación, igual que para perito.     - El nivel no se muestra, al contrario que para perito. **Diseño**:  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-18542&m=dev>  - Etiqueta Modificada (como en Trabajo pendiente): <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2047-41558&m=dev>  Ejemplo de celda de tasación completo |
| 17 | APROBADO | Un cliente logado con cualquier tipo de rol | Llegue a Inicio de tasación por cualquier vía posibleO pulse en el botón REINTENTAR de la vista INICIO DE TASACIÓN ERRORY el **servicio de obtener tasaciones abiertas** funcione correctamente Y hay algún siniestro | Se muestra la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** muestra por cada celda de `siniestro` los siguientes elementos: - Línea principal:     - A la izquierda:         - Si `siniestro.siniestro` existe, se muestra el siniestro con formato `CODIGO/AÑO`, siendo AÑO los 4 primeros dígitos de `siniestro.siniestro` y el resto, CODIGO.         - Si hay catálogo de tipos de siniestro y hay coincidencia de tipos con el del siniestro (se busca el `tipo.tipoSiniestro === siniestro.codTipoSiniestro` dentro del catálogo de tipos de siniestro): etiqueta de subtipo de siniestro con el valor de `tipo.subtipo`. - Lista de etiquetas, que debe ocupar tantas líneas como necesite para mostrar todas las etiquetas necesarias:     - Si la tasación tiene conversación abierta asociada a tareas de comunicación, iconos de conversación o mensajería:         - Si hay mensaje con taller no asignado al usuario es 1:  icono de comentario rojo con puntito.         - Si hay mensaje con taller asignado al usuario:  icono de comentario gris.     - Etiqueta VTS:         - si `siniestro.bloqueoVts` es 'S': etiqueta "Bloqueo VTS" de color rojo.         - si `siniestro.bloqueoVts` es 'A': etiqueta "Revisión VTS" de color amarillo.         - en otro caso: no se muestra la etiqueta.     - Si `siniestro.bloqueoVts` es distinto de 'S' y `siniestro.concepto` es distinto de 1: etiqueta de compromiso. La etiqueta se muestra:         - si `siniestro.compromisoPago` es 'S': etiqueta "Compromiso" de color verde.         - si `siniestro.compromisoPago` es 'A': etiqueta "Pte. compromiso" de color amarillo.         - si `siniestro.compromisoPago` no es ‘S' ni 'A’: etiqueta "Sin compromiso" de color rojo.     - Si hay póliza seleccionada y no coincide con la póliza del siniestro ( `Number(poliza.numReferencia) !== siniestro.poliza`): etiqueta "Incidencia póliza".     - Si la póliza seleccionada tiene franquicia y `siniestro.concepto` es 1: etiqueta de la franquicia. La etiqueta se muestra:         - si `siniestro.aplicaFranquicia` es 'S': "Aplica fq." de color verde.         - si `siniestro.aplicaFranquicia` es distinto de 'S': "No aplica fq." de color amarillo.     - Si `siniestro.bloqueoLopd` es 'S': etiqueta "LOPD". - Líneas con textos descriptivos, en líneas independientes:     - Si existe `siniestro.danyos`: `siniestro.danyos` de color *tertiary*     - Si existe `siniestro.version`: `siniestro.version` **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-18542&m=dev> Ejemplo de celda de tasación completo |
| 18 | APROBADO | Un cliente logado | Estemos en la vista Inicio de tasación Y responda el **servicio de obtener las tareas de una tasación** lanzando para una celda de tasación | Se realizan las siguientes acciones: - Si no queda otro servicio pendiente de respuesta para esta tasación, se oculta la etiqueta de carga de la celda de la tasación afectada - Se actualiza la siguiente información en la tasación afectada y simultáneamente en la celda de dicha tasación:     - Información de los iconos de conversación. |
| 19 | APROBADO | Un cliente logado | Estemos en la vista Inicio de tasación Y responda el **servicio de obtener detalle del siniestro** lanzando para una celda de tasación | Se realizan las siguientes acciones: - Si no queda otro servicio pendiente de respuesta para esta tasación, se oculta la etiqueta de carga de la celda de la tasación afectada - Se actualiza la siguiente información en la tasación afectada y simultáneamente en la celda de dicha tasación:     - `tasacion.tipoSiniestro`: lo calcula buscando `detalleSiniestro.codTipoSiniestro` en el catálogo de tipos.     - `tasacion.descripcionAccidente`: desde `detalleSiniestro.version`.     - `tasacion.danyos`: desde `detalleSiniestro.danyos`. |
| 20 | APROBADO | Un cliente logado | Llegue a Inicio de tasación por cualquier vía posibleY el **servicio de obtener tasaciones cerradas de los últimos 3 días** falle | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error:     - Título: "Lo sentimos"     - Descripción: "Ha ocurrido un error al cargar las tasaciones cerradas". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 21 | APROBADO | Un cliente logado | Pulse en el botón de volver de la vista INICIO DE TASACIÓN | Vuelve a la vista de la que proceda (INTRODUCIR MATRÍCULA - historias 1 a 3, DETALLE DE TALLER - historia 2 o LISTADO DE PÓLIZAS - historia 4). |
| 22 | APROBADO | Un cliente logado | Pulse en el botón de crear en la vista INICIO DE TASACIÓN | Realiza las siguientes acciones: - Se muestra una vista de carga: "Cargando...". - Limpia datos de tasación manteniendo póliza - Resetea datos de pintura anteriores - Limpia situación de facturación - Se comprueba `origenRepetirTasacion`:     - Si `origenRepetirTasacion`, inicia tasación     - Si no, crea tasación con matrícula, color y taller **Nota**: Esto se definirá mejor en la funcionalidad core de tasación.**Diseños**:<https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 23 | APROBADO | Un cliente logado | Pulse en el botón de lupa (filtro de identificadores) en la vista INICIO DE TASACIÓN | Se realizan las siguientes acciones: - El botón de lupa se selecciona (aparece resaltado). - Aparece el campo de texto de identificadores, debajo de la sección de filtros y encima del contenido. Tendrá el icono de la lupa a la derecha, el aspa de borrado a la derecha y el *placeholder* "Buscar por siniestro o póliza". **Nota**: Visualmente es igual que en el criterio 14 de la historia 10 de Trabajo pendiente: [Consulta de trabajo pendiente - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1433042947/Consulta+de+trabajo+pendiente+-+Definici+n+de+historias+de+usuario)   |
| 24 | APROBADO | Un cliente logado | Escribe texto en el campo de texto de identificadores en la vista INICIO DE TASACIÓN | Se actualizará la vista INICIO DE TASACIÓN, en la cual el **listado de tasaciones** se filtra en tiempo real mostrando únicamente aquellos elementos que contienen el texto introducido. Si no hay coincidencias, se oculta la agrupación correspondiente.**Notas**: - Se debe filtrar por coincidencia del texto introducido en el campo de texto con el identificador de la celda (que podrá ser `tasacion.codigoSiniestro` + `tasacion.anioSiniestro` o  `tasacion.codigoPoliza` para una tasación o  `siniestro.siniestro` para un siniestro, con el formato con que ya se estén mostrando). - Es importante que se pueda filtrar sin necesidad de introducir los puntos de separación. |
| 25 | APROBADO | Un cliente logado con cualquier rol | Borra todo el texto en el buscador de identificadores (a mano o pulsando en el icono de borrado) en la vista INICIO DE TASACIÓN | Se actualizará la vista INICIO DE TASACIÓN, volviendo a mostrar el **listado de tasaciones** completo.  |

### Información anexa

#### Mensaje de alerta

Hay un mensaje de alerta que mostrar si está definido `poliza.mensajeAlerta` (tiene un texto de tamaño mayor que 0).

#### Botón de crear

Este botón se muestra solo si se cumplen estas condiciones:

1. el flujo es tasación, no auditoría
2. Y hay una póliza cargada (porque si la vista está en caso de perjudicado con matrícula distinta, no asigna `this.poliza` y no se muestra)
3. Y la póliza no está suspendida (`poliza.situacionPoliza.codigo` no es 'S')
4. Y, si el usuario tiene rol de perito: si`poliza.cambioVehiculo` no es *true*
5. Y, si el usuario tiene rol de taller, se comprueba que no pertenezca a grupo de taller NNN (si `instalacion.grupoInstalaciones` del **servicio de obtener proveedores** se encuentra en el catálogo de talleres NNN).

**Nota**: El catálogo de talleres NNN se llama en el proceso de login para usuarios con rol de taller.

#### Condiciones

##### Vehículo no asegurado

El vehículo se considera no asegurado cuando:

- `poliza == null` (esto puede ocurrir si es perjudicado, parece ser)
- y no haya siniestros sin tasación, es decir, no haya elementos en la respuesta del **servicio de búsqueda de siniestros por matrícula **(que ya tendríamos cargados desde el paso anterior)
- y haya tasaciones abiertas, es decir, la respuesta del **servicio de obtener tasaciones abiertas** contenga al menos una tasación
- y algún elemento tenga `tasacion.perjudicado` distinto de *true*

##### Perjudicado

Es perjudicado cuando: 

- `tasacion.getTasacionAIniciar().perjudicado === true`
- y `poliza.vehiculo.matricula !== tasacion.getTasacionAIniciar().matricula`

#### Listado de categorías de tasaciones y siniestros

Una misma tasación puede aparecer en varias agrupaciones si cumple las condiciones.

Las condiciones para mostrar una tasación o siniestro en cada agrupación son:

- `Tasaciones erróneas`: si `tasacion.estado` es 14, 15, 16 o 17
- `Avisos peritación`: si `tasacion.estado` es 1
- `Siniestros sin tasación`: listado de siniestros sin tasación (directamente del **servicio de búsqueda de siniestros por matrícula**, que ya tendríamos cargados desde el paso anterior)
- `Tasaciones abiertas pte autorizar`: si `tasacion.estado` es 24 y `tasacion.pendienteInformacionTaller` no es *true*
- `Tasaciones abiertas pte validar`: si `tasacion.estado` es 22 o 26 y `tasacion.pendienteInformacionTaller` no es *true*
- `Tasaciones abiertas pte info`: si `tasacion.pendienteInformacionTaller` es *true* y `tasacion.estado` es 5, 6, 11, 12, 16, 17, 22, 24 o 26
- `Tasaciones abiertas`: en función del rol del usuario logado:
    - si el usuario es taller: si `tasacion.estado` es 11, 12, 16, 17, 22 o 26 y `tasacion.pendienteInformacionTaller` no es *true*
    - si el usuario es perito: si `tasacion.pendienteInformacionTaller` no es *true*, no cerrada, y (`tasacion.estado` es 11, 12, 16 o 17 o `tasacion.borrador` es 1)
- `Tasaciones cerradas pte autorizar`: si `tasacion.estado` es 25 y `tasacion.pendienteInformacionTaller` no es *true*
- `Tasaciones cerradas pte validar`: si `tasacion.estado` es 23 o 27  y `tasacion.pendienteInformacionTaller` no es *true*
- `Tasaciones cerradas pte info`: si `tasacion.pendienteInformacionTaller` es *true* y `tasacion.estado` es 7, 8, 9, 10, 14, 15, 23, 25 o 27
- `Tasaciones inacabadas`: si `tasacion.borrador` es 2, `tasacion.estado` sin definir y `tasacion.codigoPerito` es el id del usuario logado
- `Tasaciones anuladas` (solo para usuario con rol de taller): 
    - si taller es nivel 9: si `tasacion.estado` es 20
    - en caso contrario: si `tasacion.estado` es 20 o 1 (esta condición parece no cuadrar, porque realmente se muestran aquí anuladas y en reparto, pero para este tipo de talleres no aplica la condición de "Avisos peritación", ya que esa categoría no se muestra)
- `Tasaciones cerradas por taller (últimos 3 días)`: salen de un servicio independiente.
- `Tasaciones cerradas (últimos 2 años)`: esta agrupación aparece siempre al entrar en la vista, pero sus tasaciones no se cargan inicialmente. Se llama al servicio para obtenerlas solo si se pulsa en esta agrupación, si no estaban cargadas ya.


#### Estados de la tasación

##### Tasación errónea

La tasación es errónea si `tasacion.estado` está dentro de TASACIONES\_ESTADOS\_ERRONEAS (14, 15, 16, 17).

##### Tasación cerrada

La tasación está cerrada si `tasacion.estado` está dentro de TASACIONES\_ESTADOS\_CERRADAS\_ALL (7, 8, 9, 10, 14, 15, 23 o 25).

##### Tasación en reparto

La tasación está en reparto si `tasacion.estado` es 1.

##### Tasación anulada

La tasación está anulada si `tasacion.estado` es 20.


#### Iconos de conversación

Para saber si hay conversaciones abiertas y de qué tipo, hay que revisar las tareas de tasaciones cuya `tarea.referencia.numeroReferencia` sea igual a `tasacion.id`. Estas tareas son las que se obtienen al llamar a cada **servicio de obtener tareas de la tasación**.

##### Comprobaciones para perito

Hay una conversación con taller visible para perito si alguna tarea del listado tiene `tarea.tipo` igual a 14 (TAREAS\_TIPO\_COMUNICACION\_TALLER).

Hay un mensaje con perito asignado al usuario si alguna tarea del listado tiene:

- `tarea.tipo` igual a 16 (TAREAS\_TIPO\_COMUNICACION\_PERITO\_ZONA)
- y `tarea.usuarioAsignado` es el id del usuario logado

Hay un mensaje con perito no asignado al usuario si:

-  alguna tarea del listado tiene `tarea.tipo` igual a 16 (TAREAS\_TIPO\_COMUNICACION\_PERITO\_ZONA)
- y no hay un mensaje con perito asignado al usuario

##### Comprobaciones para taller

Hay un mensaje con taller asignado al usuario si alguna tarea del listado tiene:

- `tarea.tipo` igual a 14 (TAREAS\_TIPO\_COMUNICACION\_TALLER)
- y `tarea.usuarioAsignado` es el id del usuario logado

Hay un mensaje con taller no asignado al usuario si:

-  alguna tarea del listado tiene `tarea.tipo` igual a 14 (TAREAS\_TIPO\_COMUNICACION\_TALLER)
- y no hay un mensaje con taller asignado al usuario


#### Indicador "Modificada por MM"

Esta etiqueta solo aparece para usuarios con rol de taller cuando se cumple que:

- la tasación no es "especialista N8 sin modificar por taller"
- y `tasacion.usuarioModificacion` existe y tiene longitud 5
- y `tasacion.importeModificadoPerito` es *true*

La tasación no es "especialista N8 sin modificar por taller" cuando falla alguna de las siguientes condiciones:

- el usuario/instalación no es taller N8, es decir, o el usuario no es taller, o si lo es (si existe `instalacion` en el **servicio de obtener proveedores**), `instalacion.nivelConfianza` no es igual a 8
- o `tasacion.tipoTasacionSecundaria !== 'ESPECIALISTA'`
- o `tasacion.usuarioModificacion` existe y su longitud es mayor que `5`
- o `tasacion.pendienteInformacionTaller` no es *true*

#### Total peritado para usuario con rol de taller

Debe ocultarse esta etiqueta si se cumplen todas estas condiciones:

- La instalación del usuario es taller nivel 8.
- La tasación es secundaria especialista: `tasacion.tipoTasacionSecundaria === 'ESPECIALISTA'`.
- La tasación no ha sido modificada por taller: `tasacion.usuarioModificacion` no existe o su longitud no es mayor que 5.
- La tasación tiene `pendienteInformacionTaller` a *true*.

También debe ocultarse si el usuario logado es taller de lunas de nivel 3, es decir, si se cumplen estas condiciones:

- El usuario logado es un taller (existe `instalacion` en el **servicio de obtener proveedores**).
- La instalación es taller de lunas:
    - `instalacion.actividad` es una lista de un único elemento
    - ese único elemento es 4
- `instalacion.nivelConfianza` es 3

## Historia 10: Histórico de tasaciones APROBADA

Esta historia es para peritos.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con rol de perito | Pulse en el botón "Ver histórico de tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓNO pulse en el botón REINTENTAR de la sección "Tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓN | En la misma vista INICIO DE TASACIÓN: - Se oculta el botón "Ver histórico de tasaciones cerradas (últimos 2 años)". - Se muestra la nueva categoría "Tasaciones cerradas (últimos 2 años)". - Skeleton de carga (igual al del resto de vistas ya implementadas, con 3 elementos). Mientras tanto, se llama al **servicio de obtener tasaciones cerradas de los últimos 2 años**.**Diseños**: - <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2172-36496&m=dev> |
| 2 | APROBADO | Un cliente logado con rol de perito | Pulse en el botón "Ver histórico de tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓNO pulse en el botón REINTENTAR de la sección "Tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓNY el **servicio de obtener tasaciones cerradas de los últimos 2 años** falle | En la misma vista INICIO DE TASACIÓN: - Se oculta el skeleton de carga. - Dentro de la nueva categoría "Tasaciones cerradas (últimos 2 años)", se muestra la vista de error:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado  | Pulse en el botón "Ver histórico de tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓNO pulse en el botón REINTENTAR de la sección "Tasaciones cerradas (últimos 2 años)" de la vista INICIO DE TASACIÓNY el **servicio de obtener tasaciones cerradas de los últimos 2 años** funcione correctamenteY no hay tasaciones cerradas | En la misma vista INICIO DE TASACIÓN: - Se oculta el skeleton de carga. - Dentro de la nueva categoría "Tasaciones cerradas (últimos 2 años)", se muestra la vista de estado vacío:     - Imagen representativa.     - Texto: "Sin resultados".     - Texto descriptivo: "No hemos encontrado tasaciones cerradas en los últimos 2 años." **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> **Diseños**: - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-18397&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2154-63073&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2154-63316&m=dev> |
| 4 | APROBADO | Un cliente logado con rol de perito | Pulse en el botón de histórico de la vista INICIO DE TASACIÓNY el **servicio de obtener tasaciones cerradas de los últimos 2 años** funcione correctamente Y hay alguna tasación cerrada | En la misma vista INICIO DE TASACIÓN: - Se oculta el skeleton de carga. - Dentro de la nueva categoría "Tasaciones cerradas (últimos 2 años)", se muestra las tasaciones cerradas. El contenido de cada tasación es igual que en la vista de INICIO DE TASACIÓN (historia 9). |

## Historia 11: Acciones al hacer *swipe* en una celda en Inicio de tasación APROBADA

Creo que esta historia es para peritos y talleres.a

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY se debe mostrar la acción de información para tasación | Acción lateral al deslizar: icono de información.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=10069-58419&m=dev> |
| 2 | APROBADO | Un cliente logado | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY no se debe mostrar la acción de información para tasación | No permite la acción de Información. Ni se muestra la acción. |
| 3 | APROBADO | Un cliente logado con el rol de taller  | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acciónY la tasación está en reparto | Se abre el resumen de la tasación.**Nota**: Esto se implementará en la vista Resumen de la tasación. |
| 4 | APROBADO | Un cliente logado con el rol de perito | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acciónY la tasación está en repartoY hay un siniestro definido | Intentar ir a la Historia 12 → Detalle de siniestro. |
| 5 | APROBADO | Un cliente logado con el rol de perito | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acciónY la tasación está en repartoY no hay un siniestro definido | Intentar ir a la Historia 5 → Detalle de póliza. |
| 6 | APROBADO | Un cliente logado con el rol de taller distinto de nivel N8 | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acciónY la tasación no está en reparto | Se abre el resumen de la tasación.**Nota**: Esto se implementará en la vista Resumen de la tasación. |
| 7 | APROBADO | Un cliente logado con el rol de taller de nivel N8 | Haga *swipe* hacia la derecha sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acciónY la tasación no está en repartoY no es una tasación especialista N8 sin modificar por taller | Se abre el resumen de la tasación.**Nota**: Esto se implementará en la vista Resumen de la tasación. |
| 8 | APROBADO | Un cliente logado con el rol de perito  | Haga *swipe* hacia la derecha sobre una celda de siniestro de la vista INICIO TASACIÓN | Acción lateral al deslizar: icono de información.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=10069-58419&m=dev> |
| 9 | APROBADO | Un cliente logado con el rol de perito  | Haga *swipe* hacia la derecha sobre una celda de siniestro de la vista INICIO TASACIÓNY completa la acciónY el siniestro está bloqueado por LOPD | Se muestra el diálogo AVISO BLOQUEO LOPD, con el siguiente contenido:  - Título: "Póliza bloqueada por LOPD". - Descripción: "No es posible realizar la tasación ni consultar el siniestro o la póliza.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 10 | APROBADO | Un cliente logado con el rol de perito  | Haga *swipe* hacia la derecha sobre una celda de siniestro de la vista INICIO TASACIÓNY completa la acciónY el siniestro no está bloqueado por LOPD | Intenta ir a la Historia 12 → Detalle de siniestro. |
| 11 | APROBADO | Un cliente logado | Haga *swipe* hacia la izquierda sobre una celda de tasación de la vista INICIO TASACIÓNY la tasación no tiene estado o, si lo tiene, es estado Pendiente | Acción lateral al deslizar: icono de eliminar.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=10069-58419&m=dev> |
| 12 | APROBADO | Un cliente logado | Haga *swipe* hacia la izquierda sobre una celda de tasación de la vista INICIO TASACIÓNY la tasación tiene estado y no es estado Pendiente | No permite la acción de Eliminar. Ni se muestra la acción. |
| 13 | APROBADO | Un cliente logado | Haga *swipe* hacia la izquierda sobre una celda de tasación de la vista INICIO TASACIÓNY completa la acción | Se muestra el diálogo CONFIRMACIÓN DE ELIMINAR, con el siguiente contenido:  - Título: "Eliminar tasación". - Descripción: "¿Deseas eliminar la tasación? Esta acción no se puede deshacer." - Botón: "Eliminar tasación". - Botón: "Cancelar". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2875-37479&m=dev> |
| 14 | APROBADO | Un cliente logado | Pulse en Eliminar tasación en el diálogo de CONFIRMACIÓN DE ELIMINAR | Se realizan las siguientes acciones: - Se muestra el diálogo de carga: "Eliminando…". - Se llama al **servicio de eliminación de tasación**. |
| 15 | APROBADO | Un cliente logado | Pulse en Eliminar tasación en el diálogo de CONFIRMACIÓN DE ELIMINARY el servicio funcione correctamente | Se realizan las siguientes acciones: - Refresca los datos de la vista. Para ello llama a los servicios:     - **Servicio de búsqueda de siniestros**     - **Servicio de búsqueda de tasaciones**     - **Servicio de búsqueda de tareas** - Muestra aviso de éxito: "Tasación eliminada correctamente". **Nota**: En este punto, se llama al **servicio de búsqueda de tareas**, pero esa respuesta no se usa para pintar Inicio tasación. Quizás podríamos quitar esta llamada. |
| 16 | APROBADO | Un cliente logado | Pulse en Eliminar tasación en el diálogo de CONFIRMACIÓN DE ELIMINARY el servicio falle | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error: "Ha ocurrido un error al cancelar la tasación". |
| 17 | APROBADO | Un cliente logado con el rol de perito  | Pulsa en el botón  Entendido o Cancelar en cualquier diálogo previo | Cierra el diálogo correspondiente y no continúa. |
| 18 | APROBADO | Un cliente logado | Haga *swipe* hacia la izquierda sobre una celda de siniestro de la vista INICIO TASACIÓN | No permite la acción de Eliminar. Ni se muestra la acción.Nota: Este criterio implica que los siniestros no se pueden borrar. |

### Información extra

#### Comprobaciones

- El siniestro está bloqueado por LOPD si `siniestro.bloqueoLopd` es 'S'.
- La tasación está en reparto si `tasacion.estado` es 1.
- Hay un siniestro definido si `tasacion.codigoSiniestro` existe.
- La tasación no tiene estado o, si lo tiene, es estado Pendiente: `!tasacion.estado` o `tasacion.estado` es `ESTADO_PENDIENTE_INSPECCION`.
- Se debe mostrar la acción de información para una tasación si no se cumplen todas estas condiciones (es decir, si se cumplen todas las condiciones se debe impedir la acción):
    - el usuario logado es un taller de nivel N8
    - la tasación no está en reparto
    - la tasación es una tasación especialista N8 sin modificar por taller

#### Tasación especialista N8 sin modificar por taller

Al hacer *swipe* sobre una celda de tasación, si el usuario logado es taller nivel 8, la app comprueba si esa tasación es una “tasación especialista N8 sin modificar por taller”.

Si lo es, cierra el *swipe* y no hace nada más: no abre resumen, no recupera tasación, no navega.

```
if (
  this.permisos.tienePermisosTalleres() &&
  this.store.getInstalacion().nivelConfianza === 8
) {
  slidingItem.close();

  if (!this.tasacionUtil.esTasacionEspecialistaTallerNivel8SinModificarTaller(this.tasacion)) {
    this.cargarResumenTasacion(this.fromInspeccion);
  }
}
```

esTasacionEspecialistaTallerNivel8SinModificarTaller es *true* si:

- usuario logado es taller nivel 8
- `tasacion.tipoTasacionSecundaria === 'ESPECIALISTA'`
- la tasación no ha sido modificada por taller
- `tasacion.pendienteInformacionTaller` es true

## Historia 12: Acciones al pulsar sobre una celda de siniestro en Inicio de tasación APROBADA

Esta historia es para peritos y talleres.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con rol de taller | Pulse sobre una celda de siniestro sin tasación de la vista INICIO DE TASACIÓNY la póliza existeY la póliza tenga algún mensaje de alerta | Se muestra el diálogo AVISO MENSAJE ALERTA, con el siguiente contenido:  - Título: "Cambios en las condiciones de la póliza". - Descripción: "Debido a cambios en la situación de la póliza, este vehículo deberá ser tasado por el perito de zona.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 2 | APROBADO | Un cliente logado con cualquier rol | Pulse sobre una celda de siniestro sin tasación de la vista INICIO DE TASACIÓNY la póliza no tiene mensaje de alerta (si es usuario con rol de taller)Y hay bloqueo de LOPD | Se muestra el diálogo AVISO BLOQUEO LOPD, con el siguiente contenido:  - Título: "Póliza bloqueada por LOPD". - Descripción: "No es posible realizar la tasación ni consultar el siniestro o la póliza.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 3 | APROBADO | Un cliente logado con cualquier rol | Pulse sobre una celda de siniestro sin tasación de la vista INICIO DE TASACIÓNY la póliza no tiene mensaje de alerta (si es usuario con rol de taller)Y no hay bloqueo de LOPD | Se realizan las siguientes acciones: - Se muestra la vista de carga:     - Título: "Cargando…".     - Descripción: "Por favor, espere." - Llama al **servicio de obtener detalle de siniestro**. **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 4 | APROBADO | Un cliente logado con cualquier rol | Pulse sobre una celda de siniestro sin tasación de la vista INICIO DE TASACIÓNY la póliza no tiene mensaje de alerta (si es usuario con rol de taller)Y no hay bloqueo de LOPDY el **servicio de obtener detalle de siniestro** funcione correctamente | Intenta acceder al flujo de Inicio de tasación con el siniestro obtenido del servicio. - Guarda el detalle de siniestro en `siniestroSeleccionado`. - Va a la edición de la tasación → Historia 1 de procesos comunes a los pasos de la tasación: [\[Tasación\] Procesos comunes a los pasos de la tasación - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1746600170/Tasaci+n+Procesos+comunes+a+los+pasos+de+la+tasaci+n+-+Definici+n+de+historias+de+usuario) |
| 5 | APROBADO | Un cliente logado con cualquier rol | Pulse sobre una celda de siniestro sin tasación de la vista INICIO DE TASACIÓNY la póliza no tiene mensaje de alerta (si es usuario con rol de taller)Y no hay bloqueo de LOPDY el **servicio de obtener detalle de siniestro** falle | Se muestra un aviso de error: - Título: "Algo salió mal" - Descripción: "No hemos podido cargar la información del siniestro. Inténtalo de nuevo más tarde." **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 6 | APROBADO | Un cliente logado con rol de perito | Pulsa en el botón  Entendido o Cancelar en cualquier diálogo previo | Cierra el diálogo correspondiente y no continúa. |

### Información anexa

- La póliza tiene algún mensaje de alerta si está definido `poliza.mensajeAlerta`.
- Hay bloqueo de LOPD si `siniestro.bloqueoLopd === 'S'`.

## Historia 13: Acciones al pulsar sobre una celda de tasación en Inicio de tasación para usuario perito APROBADA

Esta historia es para peritos al inicio. A partir del criterio 4 aplica a peritos y talleres. La siguiente historia especifica el flujo inicial para talleres y a partir de un punto, ambos flujos confluyen en el mismo.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con rol de perito | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es recuperableY la tasación no es Pruebas Seguros | Se muestra el diálogo AVISO NO Pruebas Seguros, con el siguiente contenido:  - Título: "Tasación externa a Pruebas Seguros"  - Descripción: "La tasación no pertenece a la aplicación Pruebas Seguros." - Botón "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 2 | APROBADO | Un cliente logado con rol de perito | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es recuperableY el motor no es Stars | Se muestra el diálogo AVISO MOTOR EXTERNO, con el siguiente contenido:  - Título: "Tasación de motor externo". - Descripción: "Esta tasación se creó con un motor externo. Para acceder a ella, utiliza Pruebas Seguros en escritorio.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 3 | APROBADO | Un cliente logado con rol de perito | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es recuperableY hay mano de obra de atención comercial | Se muestra el diálogo AVISO ATENCIÓN COMERCIAL, con el siguiente contenido:  - Título: "Tasación con atención comercial". - Descripción: "Esta tasación cuenta con atención comercial.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 4 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY es una tasación en reparto y tiene siniestro | Se realizan las siguientes acciones: - Si hubiera algún diálogo mostrándose, se cierra. - Si no se está mostrando una vista de carga, se muestra:     - Título: "Cargando…".     - Descripción: "Por favor, espere." - Se llama al **servicio de obtener el total de tasaciones**. **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 5 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY es una tasación en reparto y tiene siniestroY el **servicio de obtener el total de tasaciones** responde correctamenteY no existe otra tasación para el expediente | Continúa con las siguientes comprobaciones: se revisa si la tasación es editable (tope de reparación, tasación pagada). |
| 6 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY es una tasación en reparto y tiene siniestroY el **servicio de obtener el total de tasaciones** responde correctamenteY ya existe otra tasación para el expediente | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra el diálogo CONFIRMACIÓN NUEVA TASACIÓN, con el siguiente contenido:      - Título: "Tasación existente".     - Descripción: "En este expediente ya existe una tasación para el vehículo MATRICULA. Al continuar se creará una nueva tasación.", siendo MATRICULA el campo `tasacion.matricula`"     - Botón: "Continuar".     - Botón: "Cancelar". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2875-37479&m=dev> |
| 7 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY es una tasación en reparto y tiene siniestroY el **servicio de obtener el total de tasaciones** falle | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error:     - Título: "Algo salió mal"     - Descripción: "No hemos podido cargar la información. Inténtalo de nuevo más tarde." **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 8 | APROBADO | Un cliente logado | Pulse en Continuar en CONFIRMACIÓN NUEVA TASACIÓN | Continúa con las siguientes comprobaciones: se revisa si la tasación es editable (tope de reparación, tasación pagada). |
| 9 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY es una tasación no está en reparto o no tiene siniestro | Continúa con las siguientes comprobaciones: se revisa si la tasación es editable (tope de reparación, tasación pagada). |
| 10 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY existe tope de reparación | Se muestra el diálogo AVISO DE TOPE DE REPARACIÓN, con el siguiente contenido:  - Título: "Tasación con límite de reparación". - Descripción: "Esta tasación no se puede modificar desde la aplicación Pruebas Seguros por tener registrado un tope de reparación.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 11 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY no existe tope de reparaciónY la tasación está pagada | Se muestra el diálogo CONFIRMACIÓN DE TASACIÓN PAGADA, con el siguiente contenido:  - Título: "Tasación pagada". - Descripción: "Esta tasación ya ha sido abonada, pero puedes continuar para ampliar la tasación.". - Botón: "Continuar". - Botón: "Cancelar". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2875-37479&m=dev> |
| 12 | APROBADO | Un cliente logado | Pulsa en el botón Continuar en el diálogo CONFIRMACIÓN DE TASACIÓN PAGADA | Se realizan las siguientes acciones: - Si hubiera algún diálogo mostrándose, se cierra. - Si no se está mostrando una vista de carga, se muestra:     - Título: "Cargando…".     - Descripción: "Por favor, espere." - Se llama al **servicio de obtener siniestro**. **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 13 | APROBADO | Un cliente logado | Pulsa en el botón Continuar en el diálogo CONFIRMACIÓN DE TASACIÓN PAGADAY el **servicio de obtener siniestro** responde correctamente | Se realizan las siguientes acciones: - Se clona la tasación con el siniestro devuelto.  - Va a la edición de la tasación → Historia 1 de procesos comunes a los pasos de la tasación: [\[Tasación\] Procesos comunes a los pasos de la tasación - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1746600170/Tasaci+n+Procesos+comunes+a+los+pasos+de+la+tasaci+n+-+Definici+n+de+historias+de+usuario) |
| 14 | APROBADO | Un cliente logado | Pulsa en el botón Continuar en el diálogo CONFIRMACIÓN DE TASACIÓN PAGADAY el **servicio de obtener siniestro** falle | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error:     - Título: "Algo salió mal"     - Descripción: "No hemos podido cargar la información del siniestro. Inténtalo de nuevo más tarde." **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 15 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY no existe tope de reparaciónY tiene bloqueo de facturación | Se muestra el diálogo CONFIRMACIÓN DE BLOQUEO DE FACTURACIÓN, con el siguiente contenido:  - Título: "Pago bloqueado". - Descripción: "El pago de la factura está bloqueado, pero puedes continuar para modificar la tasación.". - Botón: "Continuar". - Botón: "Cancelar". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2875-37479&m=dev> |
| 16 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY no existe tope de reparaciónY la facturación de la tasación es editable y no está bloqueadaO pulse en el botón Continuar en CONFIRMACIÓN DE BLOQUEO DE FACTURACIÓN | Se realizan las siguientes acciones: - Si hubiera algún diálogo mostrándose, se cierra. - Si no se está mostrando una vista de carga, se muestra:     - Título: "Cargando…".     - Descripción: "Por favor, espere." - Se llama al **servicio de obtener desgloses**. **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2443-5099&m=dev> |
| 17 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY el servicio de **obtener desgloses** falle | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra un aviso de error:     - Título: "Algo salió mal"     - Descripción: "No hemos podido recuperar la tasación. Inténtalo de nuevo más tarde." **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 18 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY el servicio de **obtener desgloses** funcione correctamenteY hay desgloses con deducciones | Se realizan las siguientes acciones: - Se oculta la vista de carga. - Se muestra el diálogo AVISO DE DEPRECIACIONES, con el siguiente contenido:      - Título: "Tasación con depreciaciones".     - Descripción: "Esta tasación no se puede modificar desde la aplicación Pruebas Seguros por tener registradas depreciaciones.".     - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 19 | APROBADO | Un cliente logado | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY, tras las comprobaciones necesarias, se llama a los **servicios** de desgloses, siniestro, etcY los servicios funcionen correctamenteY no hay desgloses con deducciones | Va a la edición de la tasación → Historia 1 de procesos comunes a los pasos de la tasación: [\[Tasación\] Procesos comunes a los pasos de la tasación - Definición de historias de usuario](https://mutuamad.atlassian.net/wiki/spaces/EX/pages/1746600170/Tasaci+n+Procesos+comunes+a+los+pasos+de+la+tasaci+n+-+Definici+n+de+historias+de+usuario) |
| 20 | APROBADO | Un cliente logado | Pulsa en el botón  Entendido o Cancelar en cualquier diálogo previo | Cierra el diálogo correspondiente y no continúa. |

### Información anexa

- La tasación es recuperable si:
    - La tasación es Pruebas Seguros.
    - El motor es Stars.
    - No hay mano de obra de atención comercial.
- La tasación es Pruebas Seguros si `tasacion.aplicacionModificacion` contiene "Pruebas Seguros".
- El motor es Stars si `tasacion.motor` es "ST".
- La tasación está en reparto si `tasacion.estado` es 1.
- La tasación está bloqueada si `tasacion.bloqueado` es *true*. El bloqueo local no viene ni se envía a ningún servicio; solo evita doble pulsación mientras responden los servicios.
- Desmarcar el bloqueo de tasación consiste en definir `tasacion.bloqueado` como *false*.
- No hay mano de obra de atención comercial si `tasacion.manoObraAC` no existe, es 0 o no es mayor que 0.
- Existe tope de reparación si `tasacion.topeReparacion` tiene valor.
- La facturación de la tasación puede:
    - Ser no editable (es decir, estar pagada) si `situacionFacturacion <= 90` o `situacionFacturacion` es 92.
    - Estar bloqueada (bloqueo de facturación) si `situacionFacturacion` es 93, 96 o 98 y `tasacion.estado` es un estado cerrado (TASACIONES\_ESTADOS\_CERRADAS → 7, 8, 9, 10, 14, 15).
    - Ser editable y no estar bloqueada en cualquier otro caso.
- Hay desgloses con deducciones si algún desglose del **servicio de obtener desgloses de la tasación** tiene `desglose.tipoReparación` igual a "S" (DEDUCCIÓN MUTUALISTA) o igual a "D" (DEDUCCIÓN TALLER).
- No existe otra tasación del expediente cuando el total de tasaciones para el expediente de esa tarea devuelve 0. Ese total es el tamaño del array que devuelve el **servicio de obtener total de tasaciones**.

## Historia 14: Acciones al pulsar sobre una celda de tasación en Inicio de tasación para usuario taller APROBADA

Esta historia es para talleres.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con rol de taller | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es recuperableY la tasación no es Pruebas Seguros | Se muestra el diálogo AVISO NO Pruebas Seguros, con el siguiente contenido:  - Título: "Tasación externa a Pruebas Seguros". - Descripción: "La tasación no pertenece a la aplicación Pruebas Seguros.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 2 | APROBADO | Un cliente logado con rol de taller | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es recuperableY la tasación está anulada | Se muestra el diálogo AVISO TASACIÓN ANULADA, con el siguiente contenido:  - Título: "Tasación anulada". - Descripción: "La tasación está anulada.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 3 | APROBADO | Un cliente logado con rol de taller | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es cerrada y propia del taller | Se muestra el diálogo AVISO TASACIÓN CERRADA, con el siguiente contenido:  - Título: "Tasación cerrada". - Descripción: "La tasación está cerrada y solo permite realizar modificaciones rápidas.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 4 | APROBADO | Un cliente logado con rol de taller N9 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación tenga total peritado | Deriva al flujo de Resumen de tasación.**Nota**: El detalle queda fuera de esta historia. |
| 5 | APROBADO | Un cliente logado con rol de taller N9 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY no tenga total peritado | Intenta recuperar la tasación → Criterio 10. |
| 6 | APROBADO | Un cliente logado con rol de taller N8 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación no es secundaria especialistaY la tasación tenga total peritado | Deriva al flujo de Resumen de tasación.**Nota**: El detalle queda fuera de esta historia. |
| 7 | APROBADO | Un cliente logado con rol de taller N8 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es secundaria especialista o la tasación no tenga total peritado | Intenta recuperar la tasación → Criterio 10. |
| 8 | APROBADO | Un cliente logado con rol de taller distinto de N8 y N9 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY está en reparto | Se muestra el diálogo AVISO TASACIÓN EN REPARTO, con el siguiente contenido:  - Título: "Tasación derivada a perito". - Descripción: "La tasación fue derivada a un perito.". - Botón: "Entendido". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2315-38474&m=dev> |
| 9 | APROBADO | Un cliente logado con rol de taller distinto de N8 y N9 | Pulse sobre una celda de tasación de la vista INICIO DE TASACIÓNY la tasación es recuperableY la tasación no está en repartoY la tasación no es cerrada y propia del taller | Intenta recuperar la tasación → Criterio 10. |
| 10 | APROBADO | Un cliente logado con rol de taller | Intenta recuperar la tasación | Continúa por el criterio 4 de la historia 13.**Nota**: A partir de aquí el flujo es el mismo que en la historia 13. |

### Información anexa

- La tasación tiene total peritado si `tasacion.totalPeritado > 0`.
- La tasación es secundaria especialista si `tasacion.tipoTasacionSecundaria` es 'ESPECIALISTA'.
- La tasación es recuperable para taller si:
    - La tasación es Pruebas Seguros.
    - La tasación no está anulada.
    - Si está en reparto, el taller debe ser N8 o N9.
    - No es una tasación cerrada propia del taller.
- El taller es N8 si `instalacion.nivelConfianza` del **servicio de obtener proveedores** es 8.
- El taller es N9 si `instalacion.nivelConfianza` del **servicio de obtener proveedores** es 9.
- La tasación es Pruebas Seguros si `tasacion.aplicacionModificacion` contiene "Pruebas Seguros".
- La tasación está en reparto si `tasacion.estado` es 1.
- La tasación está anulada si `tasacion.estado` es 20.

## Historia 15: Filtro de tasaciones APROBADA

Esta historia es únicamente para usuarios con rol de perito, pero también aplica a otros flujos (en concreto, el de auditoría). Esta vista debe comportarse igual que la del filtro de Trabajo pendiente, salvo porque se hace un filtrado sobre tasaciones y no sobre agrupaciones de tasaciones.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado con el rol de perito  | Pulse en botón filtros en la vista INICIO DE TASACIÓN o en la vista HISTÓRICO DE TASACIONES | Sobre la vista actual, se mostrará una modal con la vista FILTROS DE TASACIONES a pantalla completa. Esta vista tendrá los siguientes elementos: - Cabecera:     - Botón cerrar, a la izquierda.     - Título "Filtros". - Contenido:     - Sección "Creador de la tasación". Con los siguientes filtros, por defecto todos deseleccionados:         - Yo         - Otro perito         - Talleres     - Sección "Estado de la tasación". Con los siguientes filtros, por defecto todos deseleccionados:         - Abiertas         - Erróneas         - Avisos         - Cerradas     - Sección "Tipo de tasación". Con los siguientes filtros, por defecto todos deseleccionados:         - Pte. Autorizar         - Pte. Validar         - Pte. Info         - Cerradas por taller     - Sección "Nivel de tasación". Con los siguientes filtros, por defecto todos deseleccionados:         - Nivel 1         - Nivel 2         - Nivel 3         - Nivel 8         - Nivel 9     - Sección "Fechas":         - Botones "Desde" y "Hasta", por separado. Por defecto, sin rango de fechas seleccionado. No se debe permitir seleccionar fechas inconsistentes: si ya hay una fecha "Desde", la fecha "Hasta" no puede ser anterior, y viceversa.         - Selector "Fecha de modificación". Por defecto, seleccionado.****         - Selector "Fecha de apertura".     - Botón "Aplicar filtros".     - Botón "Limpiar filtros". **Nota**: Además de por dificultad técnica, hemos decidido separar el botón "Desde - Hasta" en 2 por motivos funcionales, ya que creemos que tiene lógica permitir al usuario usar un solo filtro (o solo Desde o solo Hasta). Si están en un mismo botón, esto no se puede permitir.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1185-59241&m=dev> |
| 2 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón cerrar de la vista FILTROS DE TASACIONES | Se cierra la vista modal, volviendo a la vista previa (ya sea INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES), sin aplicar ningún filtro y, por tanto, sin modificar nada.  |
| 3 | APROBADO | Un cliente logado con el rol de perito  | Pulse el botón de Limpiar filtros de la vista FILTROS DE TASACIONES | Se realizan las siguientes acciones: - Se resetea el valor de los filtros disponibles a los valores por defecto. Ver **Información anexa**. - Se cierra la modal con la vista FILTROS DE TASACIONES. - Se actualiza la vista previa (INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES), para volver a filtrar con los filtros originales. - Y el icono de filtros de la barra superior de la vista previa (INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES) se pinta de color blanco.  |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en uno de los filtros de las secciones "Creador de la tasación", "Estado de tasación", "Tipo de tasación" o "Nivel de tasación" de la vista FILTROS DE TASACIONES | Se activa el filtro pulsado. |
| 5 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón "Desde" o "Hasta" de la sección "Fechas" de la vista FILTROS DE TASACIONES | Aparece un calendario nativo que permite seleccionar un único día.**Nota**: Si el usuario no modifica nada, se toma por defecto el día de hoy, y será el filtro que tenga efecto. |
| 6 | APROBADO | Un cliente logado con el rol de perito  | Seleccione una fecha en el calendario abierto al pulsar en el botón "Desde" o "Hasta" de la sección "Fechas" de la vista FILTROS DE TASACIONES | Se realizan las siguientes acciones: - Se vuelve a ocultar el calendario del selector de tipo de fecha. - El texto del botón pulsado ("Desde" o "Hasta") se sustituye por la fecha de ese día en formato "dd/MM/yyyy". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1185-59238&m=dev> |
| 7 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el selector "Fechas de modificación" de la sección "Fechas" de la vista FILTROS DE TASACIONES | Se activa el selector "Fechas de modificación" y se desactiva el selector "Fechas de apertura". |
| 8 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el selector "Fechas de apertura" de la sección "Fechas" de la vista FILTROS DE TASACIONES | Se activa el selector "Fechas de apertura" y se desactiva el selector "Fechas de modificación". |
| 9 | APROBADO | Un cliente logado con el rol de perito  | Pulse el botón Aplicar filtros de la vista FILTROS DE TASACIONESY hay al menos un filtro con un valor distinto de los valores por defecto | Se realizan las siguientes acciones: - Se cierra la vista modal FILTRO DE TASACIONES (volviendo a INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES, sin llamar a ningún servicio). - Se aplican los filtros seleccionados sobre el listado de agrupaciones de tasaciones/tareas. Para saber cómo afecta cada filtro al contenido de esta vista, ver la sección **Información anexa**. Si no hay ningún filtro seleccionado, no se filtra por nada (es decir, se muestra la totalidad de las agrupaciones). - El botón de Filtros de la vista previa (INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES) aparece seleccionado y muestra la cantidad de filtros que se hayan seleccionado. - Junto al botón de Filtros aparecen seleccionados los filtros "Mías", "Otro perito" y "Taller", si en la vista FILTRO DE TASACIONES se han activado los filtros equivalentes de la sección "Creador de la tasación" ("Yo", "Otro perito" y "Taller", respectivamente). **Diseño**:    |
| 10 | APROBADO | Un cliente logado con el rol de perito  | Pulse uno de los filtros junto al botón Filtros en la vista INICIO DE TASACIÓN o en la vista de HISTÓRICO DE TASACIONES | Se realizan las siguientes acciones: - Se activa o desactiva ese filtro, en función del estado previo. - Se reaplican los filtros sobre el listado de agrupaciones según apliquen (teniendo en cuenta que estos filtros equivalen a los de la sección "Creador de la tasación" de la vista INICIO DE TASACIÓN y de la vista HISTÓRICO DE TASACIONES). Si no hay ningún filtro seleccionado, no se filtra por nada (es decir, se muestra la totalidad de las tareas). |

### Información anexa

#### Aplicación de filtros

Cuando se pulsa en el botón APLICAR FILTROS, se revisa el estado de todos los filtros para actualizar la vista previa (ya sea INICIO DE TASACIÓN o HISTÓRICO DE TASACIONES) al volver a ella con los datos filtrados según los criterios que apliquen.

**Importante**: Como los filtros aplican únicamente a las tasaciones, en cuanto se seleccione al menos un filtro, se dejarán de mostrar los siniestros. Solo volverán a verse cuando se eliminen todos los filtros.

##### Filtros de creador de la tasación

Al aplicar los filtros, se revisa qué filtros de creador de la tasación están activos y se mostrarán únicamente aquellas tasaciones que cumplan las siguientes condiciones en función del filtro:

- *Yo/Mías*: si `tasacion.codigoPerito` es exactamente igual al `id` del usuario logado
- *Otro perito*: si `tasacion.codigoPerito` no es de tamaño 7 y es distinto del `id` del usuario logado
- *Talleres*: si `tasacion.codigoPerito` es de tamaño 7

##### Filtros de estado de la tasación

Al aplicar los filtros, se revisa qué filtros de estado de la tasación están activos y se mostrarán únicamente aquellas tasaciones que cumplan las siguientes condiciones en función del filtro:

- Abiertas: si `tasacion.estado` es 5, 6, 11, 12, 16, 17, 22 o 24
- Erróneas: si `tasacion.estado` es 14, 15, 16 o 17
- Avisos: si `tasacion.estado` es 1
- Cerradas: si `tasacion.estado` es 7, 8, 9, 10, 14, 15, 23 o 25

###### Listado de estados relevantes

- TASACIONES\_ESTADOS\_ABIERTAS\_ALL → 5, 6, 11, 12, 16, 17, 22, 24
- TASACIONES\_ESTADOS\_ERRONEAS → 14, 15, 16, 17
- TASACION\_ESTADO\_REPARTO → 1 
- TASACIONES\_ESTADOS\_CERRADAS\_ALL → 7, 8, 9, 10, 14, 15, 23, 25

##### Filtros de tipo de la tasación

Al aplicar los filtros, se revisa qué filtros de tipo de la tasación están activos y se mostrarán únicamente aquellas tasaciones que cumplan las siguientes condiciones en función del filtro:

- Pte. Autorizar: si `tasacion.estado` es 24 o 25
- Pte. Validar: si `tasacion.estado` es 22, 23, 26 o 27
- Pte. Info: si `tasacion.pendienteInformacionTaller` es *true*
- Cerradas por taller:
    - si `tasacion.estado` es 7, 8, 9, 10, 14, 15, 23 o 25 
    - y `tasacion.pendienteInformacionTaller` no es *true*
    - y `tasacion.codigoPerito` tiene longitud 7

###### Listado de estados relevantes

- TASACIONES\_ESTADOS\_PTE\_AUTORIZAR
    - 24 → TASACION\_ESTADO\_ABIERTA\_PENDIENTE\_AUTORIZAR 
    - 25 → TASACION\_ESTADO\_CERRADA\_PENDIENTE\_AUTORIZAR 
- TASACIONES\_ESTADOS\_PTE\_VALIDAR
    - 22 → TASACION\_ESTADO\_ABIERTA\_PENDIENTE\_VALIDAR 
    - 23 → TASACION\_ESTADO\_CERRADA\_PENDIENTE\_VALIDAR 
    - 26 → TASACION\_ESTADO\_ABIERTA\_PENDIENTE\_VALIDAR\_ERROR 
    - 27 → TASACION\_ESTADO\_CERRADA\_PENDIENTE\_VALIDAR\_ERROR 
- TASACIONES\_ESTADOS\_CERRADAS\_ALL → 7, 8, 9, 10, 14, 15, 23, 25

##### Filtros de nivel de tasación

Al aplicar los filtros, se revisa qué filtros de nivel de tasación están activos y se mostrarán únicamente aquellas tasaciones que tengan un campo `nivelConfianzaTasacion` igual al de alguno de los niveles de tasación activos.

##### Filtros de fecha

###### Apertura/Modificación

Al aplicar los filtros, si está activo el selector "Fecha de apertura" del selector de tipo de fecha, se mostrará la fecha de apertura en el campo de fecha de la celda de una tasación en el listado de tasaciones.

En cambio, si está activo el botón "Fecha de modificación", se mostrará la fecha de modificación.

La explicación detallada de cómo se muestran estas fechas está en la historia 10.

###### Rango de fechas

Al aplicar los filtros, si se ha definido alguna fecha o rango de fechas en los botones "Desde" y "Hasta" de la sección "Fechas", se mostrarán únicamente aquellas tasaciones cuyo campo FECHA esté dentro del rango de fechas especificado. El valor de FECHA será `tasacion.fechaCreacion` si está seleccionado el selector "Fecha de apertura" o `tasacion.fechaModificacion` si está seleccionado el botón "Fecha de modificación".

## Historia 16: Detalle de siniestro  APROBADA

Esta vista no comprueba nada de modo que no tiene por qué ser únicamente para perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | APROBADO | Un cliente logado | Intente acceder a la vista DETALLE DE SINIESTROO pulse en el botón REINTENTAR de la vista DETALLE DE SINIESTRO ERROR | Se muestra la vista DETALLE DE SINIESTRO CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Siniestro".     - Subtítulo: "Vehículo". - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama al **servicio de obtener detalle de siniestro**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | APROBADO | Un cliente logado | Intente acceder a la vista DETALLE DE SINIESTROY el **servicio de obtener detalle de siniestro** falle | Se muestra la vista DETALLE DE SINIESTRO ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Siniestro".     - Subtítulo: "Vehículo". - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | APROBADO | Un cliente logado | Intente acceder a la vista DETALLE DE SINIESTROY el **servicio de obtener detalle de siniestro **funcione correctamente | Se muestra la vista DETALLE DE SINIESTRO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Siniestro CODIGO/AÑO", siendo AÑO los 4 primeros dígitos de `siniestro.siniestro` y CODIGO el resto de contenido del mismo valor.     - Subtítulo: "Vehículo MATRICULA", siendo MATRICULA `siniestro.matricula`  o "". - Contenido:     - Sección "Datos del siniestro":         - Póliza: `siniestro.poliza` formateado con el formato numérico (puntos para separar los millares).         - Residencia: `siniestro.descripcionResidencia`  o "Sin especificar".         - Matrícula: `siniestro.matricula`  o "Sin especificar".         - Marca/Modelo: “MARCA MODELO”, siendo MARCA `descripcionMarca` y MODELO `descripcionModelo`.         - Garantías: `siniestro.garantias`  o "Sin especificar".         - Si debemos mostrar la franquicia (ver **Información anexa**): Franquicia:             - Si `siniestro.aplicaFranquicia` forzado a mayúsculas es 'S': "Sí"             - En caso contrario: "No"         - Si `siniestro.concepto` es distinto de 1:  Compromiso:              - Si `siniestro.compromisoPago` es ‘S' o 'A’: "Sí"             - En caso contrario: "No"     - Sección "Datos del accidente":         - Situación: `siniestro.situacion`         - Tipo siniestro: Este siniestro debe mostrarse como una etiqueta con el icono del tipo de siniestro que aplique, en función del dato `siniestro.codTipoSiniestro`, y el texto de `siniestro.descTipoSiniestro`.         - Fecha accidente: `siniestro.fechaAccidente` con formato "dd/MM/yyyy"         - Provincia: `siniestro.descripcionProvincia`         - Daños asegurado: `siniestro.danyosAsegurado` Este texto debe ocupar el espacio que necesite.         - Lesiones: `siniestro.lesiones` Este texto debe ocupar el espacio que necesite.         - Lugar: `siniestro.lugar`         - Act. judiciales: `siniestro.actuacionesJudiciales` Este texto debe ocupar el espacio que necesite.         - Daños vehículo: `siniestro.danyos`. Este texto debe ocupar el espacio que necesite.         - Versión:             - Si no existe `siniestro.version`: en esa misma fila, "Sin especificar".             - Si existe `siniestro.version`: `siniestro.version`, ocupando todas las líneas que necesite.         - Botón "Tasación no viable".         - Botón "Imágenes". **Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=8684-116854&m=dev> |
| 4 | APROBADO | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista DETALLE DE SINIESTRO | Vuelve a la vista de la que procede (probablemente INICIO DE TASACIÓN). |

### Información extra

#### Tipos de siniestro

El siniestro debe mostrarse como una etiqueta con el icono del tipo de siniestro que aplique, en función del dato `siniestro.codTipoSiniestro`, y el texto de `siniestro.descTipoSiniestro`. Para saber qué icono aplica, hay que comparar el valor de `siniestro.codTipoSiniestro` con el del Código de la siguiente tabla. Dejo la correspondencia completa entre Código, Subtipo y Descripción de cada tipo:

| Código | Subtipo | Descripción |
| --- | --- | --- |
| 0 | SC | SIN CONTRARIO |
| 1 | AP | APARCAMIENTO |
| 4 | LU | LUNA |
| 5 | CO | COLISION |
| 6 | CM | COLISION MULTIPLE |
| 7 | AT | ATROPELLO |
| 8 | IN | INCENDIO |
| 11 | RT | ROBO TOTAL |
| 12 | RU | ROBO RUEDAS |
| 13 | RR | ROBO RADIO |
| 14 | RV | ROBO VARIOS |
| 15 | RA | ROBO APARECIDO |
| 21 | IU | INUNDACIONES |
| 22 | TE | MOTIN |
| 23 | PE | PEDRISCO |
| 24 | VI | VIENTO |
| 30 | AV | AVERIA MECANICA |
| 31 | GR | GRAN REPARACION |
| 33 | FR | FINALIZACION RENTING |
| 34 | CB | COLISION ANIMAL |
| 35 | BA | AVERIA BATERIA |

Los iconos están en Figma: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=1749-28079&m=dev> 

#### Cuando mostrar la franquicia

Debemos mostrar el campo franquicia únicamente si:

- `siniestro.concepto` es 1
- Y `poliza.productoSeleccionado.franquiciaSeleccionada` existe

Esto implica que hay que traer la póliza hasta esta vista para poder hacer la comprobación, si venimos de una vista donde ya esté cargada. Si venimos de una vista donde no esté cargada, no se podrá visualizar este campo, porque la segunda condición no se cumpliría.

Código original:

```
siniestro.mostrarFranquicia =
  this.siniestro.concepto === 1 &&
  this.store.poliza.getPoliza().productoSeleccionado.franquiciaSeleccionada
    ? true
    : false;
```

# Historias de usuario sin definir

## Historia 17: Vehículo no tasable PENDIENTE UX

Esta historia es para usuarios con rol de perito y para usuarios con rol de Taller (creo que en Tasaciones de taller).

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | WIP | Un cliente logado  | Completa el movimiento de swipe hacia la derecha sobre una agrupación de tasaciones dentro de un a categoría que no sea “Avisos verificación” que puedan ser no tasables | Se muestra la vista VEHÍCULOS NO TASABLE CARGA.Esta vista tendrá los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: texto "Vehículo no tasable". - **Contenido**:     - Listado con *skeleton*. Mientras se muestra esta vista, se llama al **servicio de obtener catálogo de motivos de rechazo**.**¿Podríamos cachear esta información para el día de hoy la primera vez que entramos?****Pendiente vistas** |
| 2 | WIP | Un cliente logado  | Termina de cargar el servicio de obtener catálogo de motivos de rechazoY el servicio responde correctamente | Se muestra la modal VEHÍCULO NO TASABLE, que tendrá los siguientes elementos:  - **Cabecera** superior en color gris, que contiene la status bar. La cabecera contendrá:      - Botón de aspa de cierre alineado a la izquierda.      - Título centrado: “Veh. no tasable”.  - **Contenido**:      - Selector de motivo, cargado desde el catálogo MOTIVOS\_RECHAZO, mostrado como lista de radios.     - Campo de texto libre “Acciones”, con un máximo de 50 caracteres (no se indica en la vista) y *placeholder* “Introduce acciones acordadas…”.     - Campo de texto libre “Observaciones”, con un máximo de 50 caracteres (no se indica en la vista) y *placeholder* “Introduce observaciones…”.     - **Sección de selector de fecha**:         - A la izquierda, texto “Posponer aviso”.         - A la derecha, texto “Seleccione” con una flecha alineada a la derecha.     - Posible mensaje de error.     - Botón “CONFIRMAR” en color SECONDARY, alineado a la parte inferior de la vista. **Pendiente vistas** |
| 3 | WIP | Un cliente logado  | Termina de cargar el servicio de obtener catálogo de motivos de rechazoY el servicio devuelve error |  |
|  | WIP | Un cliente logado  | Pulse en el botón volver de la vista VEHÍCULO NO TASABLE | Vuelve a la vista anterior (VEHÍCULOS DE TALLER), tal y como estaba, sin refrescar los datos. |
| 4 | WIP | Un cliente logado  | Pulsa sobre un motivo del selector de motivos en la modal VEHÍCULO NO TASABLE | Si había un motivo seleccionado, se deselecciona, y se selecciona el recién pulsado con un check azul a la izquierda del texto del motivo.**Pendiente vistas** |
| 5 | WIP | Un cliente logado  | Pulse sobre la **sección de selector de fecha **de la modal VEHÍCULO NO TASABLE | Aparece un selector de fecha nativo que permite elegir una fecha.**Nota**: Parece haber una restricción que obliga a que la fecha mínima sea el día de hoy.**Pendiente vistas** |
| 6 | WIP | Un cliente logado  | Selecciona una fecha en el selector nativo de la modal VEHÍCULO NO TASABLE | Se muestra la fecha seleccionada en lugar del texto “Seleccione” en la **sección de selector de fecha**. |
| 7 | WIP |  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY no se ha seleccionado ningún motivo | Se muestra un mensaje de error de validación debajo del campo Motivo con el texto “El campo es requerido.” en rojo.**Pendiente vistas** |
| 8 | WIP | Un cliente logado  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY se ha seleccionado un motivoY se ha seleccionado una fecha en fin de semana | Se muestra un aviso rojo: “Error: la fecha de aviso es un sábado o domingo”**Pendiente vistas** |
| 9 | WIP |  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY se ha seleccionado un motivoY se ha seleccionado una fecha anterior a hoy o exactamente hoy | Se muestra un aviso rojo: “Error: la fecha no puede ser igual o inferior a la actual”**Pendiente vistas** |
| 10 | WIP | Un cliente logado  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY se ha seleccionado un motivoY se ha seleccionado una fecha posterior a hoy y que no cae en fin de semana | Realizar las siguientes acciones: 1. En paralelo, guarda una observación de “tasación fallida” por cada tasación del modal llamando al **servicio de crear observación**. 2. Marca cada tasación como “no tasable” (ver sección Información anexa). |
| 11 | WIP | Un cliente logado  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY todas las validaciones son correctasY el servicio responde correctamente | Se muestra un aviso de éxito: - Título: "Correcto" - Descripción: "La observación se ha creado". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |
| 12 | WIP | Un cliente logado  | Pulsa en el botón CONFIRMAR en la modal VEHÍCULO NO TASABLEY todas las validaciones son correctasY el servicio devuelve error | Se muestra un aviso de error: - Título: "Lo sentimos" - Descripción: "Error al crear la observación". **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2176-805&p=f&m=dev> |

### Información anexa

#### Acción al confirmar

1. Guarda una observación de “tasación fallida” por cada tasación del modal llamando al **servicio de crear observación**.
    1. Se llama a este servicio tantas veces como tasaciones haya en la agrupación.
2. Marca cada tasación como “no tasable”:
    1. Antes de guardar, para cada tasación modifica:
        1. `tasacion.obserVisitaFallida` se define como el valor del motivo seleccionado
        2. `tasacion.estado` se define como `0`
    2. Luego guarda o actualiza la tasación:
        1. Si existe `tasacion.id`, la tasación ya existe, por lo que se llama al **servicio de modificar tasación**.
        2. Si no existe, se llama al **servicio de crear una tasación**.

## Historia 18: Verificación de vehículo PENDIENTE UXFUNCIONALIDAD IMÁGENES

Esta historia es únicamente para usuarios con rol de perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | WIP | Un cliente logado con el rol de perito  | Pulse en Verificación de vehículo en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista VERIFICACIÓN DE VEHÍCULO ERROR | Se muestra la vista VERIFICACIÓN DE VEHÍCULO CARGA.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Verificación de vehículo".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Listado con *skeleton*: 3 elementos, siempre con el mismo formato. Cuando se entra en esta vista, se llama al **servicio de obtener documentos de verificación del vehículo**.**Diseño**: <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2191-31114&m=dev> |
| 2 | WIP | Un cliente logado con el rol de perito | Pulse en Verificación de vehículo en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista VERIFICACIÓN DE VEHÍCULO ERRORY el **servicio de obtener documentos de verificación del vehículo** devuelva error | Se muestra la vista VERIFICACIÓN DE VEHÍCULO ERROR.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Verificación de vehículo".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "Algo no ha salido como esperábamos".     - Texto descriptivo: "Inténtalo de nuevo en unos segundos."     - Botón: "Reintentar" **Diseño**: <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev> |
| 3 | WIP | Un cliente logado con el rol de perito  | Pulse en Verificación de vehículo en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista VERIFICACIÓN DE VEHÍCULO ERRORY el **servicio de obtener documentos de verificación del vehículo** funcione correctamenteY no haya documentos | Se muestra la vista VERIFICACIÓN DE VEHÍCULO VACÍO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Verificación de vehículo".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Imagen representativa.     - Texto: "No hay documentos para esta póliza".     - Sin botones. **Diseños**: - <https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=2318-13599&m=dev>  - <https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=2205-24399&t=vmHON4tSVKyMmvNh-4> |
| 4 | WIP | Un cliente logado con el rol de perito  | Pulse en Verificación de vehículo en la vista DETALLE DE PÓLIZAO pulse en el botón REINTENTAR de la vista VERIFICACIÓN DE VEHÍCULO ERRORY el **servicio de obtener documentos de verificación del vehículo** funcione correctamenteY haya documentos | Se muestra la vista VERIFICACIÓN VEHÍCULO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Verificación de vehículo".     - Subtítulo: "Póliza POLIZA", siendo POLIZA  `poliza.numReferencia` formateado con el formato numérico (puntos para separar los millares). - Contenido:     - Sección: "Documentos".     - Listado de `documentos` procedentes de la respuesta del **servicio de obtener documentos de verificación del vehículo**. Por cada `documento`:         - A la izquierda:             - Si `documento.thumbnail` existe: thumbnail             - En caso contrario, icono de archivo         - A la derecha, una fila de 4 iconos fijos:             - `car-crash-solid.svg`             - `clipboard`             - `user-shield-solid.svg`             - `folder-open`            El color cambia según `documento.tipo`:             - Los 3 primeros van en `TERTIARY` (gris) si `documento.tipo` está definido; en caso contrario, van en color `MEDIUM`             - `folder-open` va en `TERTIARY`(gris) si `documento.tipo` no está definido; en caso contrario, va en color `MEDIUM`         - Etiqueta fija: "Sin clasificación"         - Si `documento.error` está definido, además muestra el texto `documento.mensajeError` en rojo. |
| 5 | POR REFINAR | Un cliente logado con el rol de perito  | Pulse en el botón de volver de la vista VERIFICACIÓN DE VEHíCULO | Vuelve a la vista de la que procede (en este caso, al DETALLE DE PÓLIZA). |
| 6 | WIP | Un cliente logado con el rol de perito  | Pulse en el *thumbnail* o icono del archivo del documento en la vista VERIFICACIÓN VEHÍCULO | Se realizan las siguientes acciones: - En la misma vista, se muestra una vista de carga: "Cargando documento…". - Se llama al **servicio de obtener documento**. |
| 7 | WIP | Un cliente logado con el rol de perito  | Pulse en el *thumbnail* o icono del archivo del documento en la vista VERIFICACIÓN VEHÍCULOY el servicio funciona correctamente | Se previsualiza el documento. |
| 8 | WIP | Un cliente logado con el rol de perito  | Pulse en el *thumbnail* o icono del archivo del documento en la vista VERIFICACIÓN VEHÍCULOY el servicio falla | Muestra un error: "Error al descargar el archivo". |

## Historia 19: Imágenes de siniestro  PENDIENTE UXFUNCIONALIDAD IMÁGENES

Esta vista no comprueba nada de modo que no tiene porqué ser únicamente para perito.

|  | Estado | Dado | Cuando | Entonces |
| --- | --- | --- | --- | --- |
| 1 | WIP | Un cliente logado | Pulse en Imágenes en la vista DETALLE DE SINIESTRO | Se realizan las siguientes acciones: - Se muestra un *spinner* de carga. - Se llama a los servicios:     - si no está ya en memoria el catálogo de tipos de documentos de tasación: **servicio de obtener catálogo de tipos de documentos de tasación**     - **servicio de obtener documentos del siniestro** |
| 2 | WIP | Un cliente logado | Pulse en Imágenes en la vista DETALLE DE SINIESTROY terminen de cargar los servicios | Se muestra la vista IMÁGENES DE SINIESTRO.Esta vista contiene los siguientes elementos: - Cabecera:     - Botón de volver.     - Título: "Siniestro CODIGO/AÑO", siendo AÑO los 4 primeros dígitos de `siniestro.siniestro` y CODIGO el resto de contenido del mismo valor. - Contenido:     - Sección: "Imágenes".     - Estado vacío:         - Imagen de carpeta.         - Texto: "No se ha registrado aún ninguna imagen.". **Nota**: Esta vista no se va a profundizar en estos criterios porque es equivalente al resto de vistas de subidas de imágenes o documentos en el flujo de tasación. |

# Dudas

|  | **Duda** | **Informador** | **Responsable** | **Estado** | **Respuesta** |
| --- | --- | --- | --- | --- | --- |
| 1 | **General**En vistas como Detalle de póliza (historia 5), Recibos de póliza (historia 6), Daños excluidos (historia 6), Accesorios de póliza (historia 7), Detalle de negocio (historia 8), Verificación del vehículo (historia 18), Inicio de tasación (historia 9) o Detalle de siniestro (historia 16), en la app híbrida, se lanzan las peticiones desde la vista previa. Si funciona, navega, si no funciona, se queda donde está y muestra error. ¿Se quiere mantener este comportamiento así o se prefiere navegar primero y mostrar la vista de error si aplica? ¿O se quiere que varíe dependiendo de la vista? | @Noelia Sales Montes | UX | RESUELTA | Siempre procuraremos navegar y en la pantalla final mostrar: - Error - Empty state - O pantalla correcta. |
| 2 | **Historia 3: Introducir matrícula (entrada a Tasación para peritos)**En la app híbrida, para validar la matrícula simplemente se verifica que el número de caracteres de la matrícula sea menor o igual que 9. ¿No se quiere especificar más esta validación? | @Noelia Sales Montes | Negocio | PENDIENTE |  |
| 3 | **Historia 4: Listado de pólizas**Cuando haga *swipe* hacia la derecha sobre una póliza en vista LISTADO DE PÓLIZAS, aparece la acción de información (con el icono *readme-brands.svg*, que parece un libro abierto). ¿Eso se mantiene? ¿Cuál es la vista o el icono? | @Noelia Sales Montes | UX | RESUELTA | Tendremos la misma acción al hacer *swipe* a la derecha con el icono de info. |
| 4 | **Historia 5: Detalle de póliza**Cuando se entra en esta vista, se llama a los servicios: - **Servicio de obtener documentos de verificación del vehículo** → Se usa para saber si hay que mostrar Verificación vehículo. - **Servicio de obtener daños rechazados** → Se usa para mostrar los daños excluidos. - **Servicio de obtener de recibos de una póliza** → Se usa para mostrar el estado de los recibos. - **Servicio de obtener reglas para accesorios** ¿Debemos llamar a estos servicios para mostrar u ocultar los botones o pintamos todos y se llama a los servicios al acceder a cada vista? Si llamamos en este momento, ¿cómo reaccionaría la vista? ¿Alargamos la carga inicial con estos servicios - criterio 1 - o no mostramos ninguna carga y actualizamos después? | @Noelia Sales Montes | UX | RESUELTA | Mostramos siempre los botones sin llamar a los servicios. Los servicios se llamarán una vez que pulsemos en un botón y vayamos a su detalle. |
| 5 | **Historia 5: Detalle de póliza**En la app híbrida, Daños excluidos se muestran en su propia pantalla, porque son una lista. ¿Tendremos esa pantalla o mostraremos la lista directamente en la vista de Detalle de póliza? | @Noelia Sales Montes | UX | RESUELTA | Llamamos al servicio de obtener daños al entrar en Detalle de póliza y mostramos la lista directamente. |
| 6 | **Historia 7: Accesorios de póliza**En esta vista, ¿cómo debe funcionar el icono de filtro? Entiendo que en esta vista no tiene mucha utilidad abrir otra pantalla de filtro más y con los filtros de la derecha es más que suficiente. ¿Quizás sirve solo para llevar el conteo de los filtros de la derecha? | @Noelia Sales Montes | UX | RESUELTA | Ese icono no aplica. |
| 7 | **Historia 9: Inicio de tasación**En el bloque superior de contexto con datos del vehículo/póliza, en la app híbrida se muestran posibles etiquetas: 1. `PERJUDICADO` 2. `BLOQUEADA LOPD` 3. `VEH. NO ASEGURADO` O también: - Etiqueta ECI. - Etiquetas de coberturas IDC:     - MOVILIDAD     - IMPACTO     - TOP ¿Ya no se muestran o el diseño está en otro sitio? | @Noelia Sales Montes | UX | PENDIENTE | - ECI lo pintamos como BSAN (ambos son VIP). - "Perjudicado" y "Vehículo no asegurado" los pintamos a nivel de datos de vehículo/póliza. - "Bloqueada LOPD" lo pintamos a nivel de tasación. - Las etiquetas de coberturas IDC las pintamos a nivel de datos de vehículo/póliza. |
| 8 | **Historia 9: Inicio de tasación**En una celda de tasación, en la app híbrida se muestran posibles etiquetas: - Etiqueta VTS. ¿Ya no se muestran o el diseño está en otro sitio? | @Noelia Sales Montes | UX | PENDIENTE | - R ALT no aplica. - Perjudicado en duda. - Errónea lo quitamos. - Las etiquetas de motor se unifican con la etiqueta "Externa". - VTS en duda. |
| 9 | **Historia 9: Inicio de tasación**Al cargar la vista, en la app híbrida, se llama a estos servicios: - Se llama al **servicio de obtener tasaciones abiertas**. - Si existe `poliza`: llama al **servicio de obtener póliza IDC**. - Se llama al **servicio de obtener zonas**. - Se llama al **servicio de obtener tasaciones cerradas de los últimos 3 días**. ¿Para qué se usa el servicio de obtener zonas en esta vista? | @Noelia Sales Montes | Equipo técnico | RESUELTA | El servicio de obtener zonas no sirve para nada en esta vista. Sirve para vistas posteriores (tasacion-pieza, tasacion-total o tasacion-datos-siniestros). Por tanto, lo eliminamos de esta carga. |
| 10 | **Historia 9: Inicio de tasación**En la app híbrida, las agrupaciones de tasaciones eran desplegables: conforme se pulsa en una en una agrupación cerrada, se llama a los siguientes servicios por cada tasación: - **Servicio de obtener las tareas de una tasación**. - Si la tasación es de reparto y tiene `tasacion.codigoSiniestro`: **servicio de obtener detalle de siniestro**. Ahora que no va a haber plegado o desplegado, ¿cómo hacemos esto? ¿Al inicio de la vista cargamos todo? ¿Cargamos lo que tengamos y conforme respondan los servicios actualizamos la vista? ¿Cómo informamos al usuario de que no está todo cargado? Es decir, puede que no salga cierta información porque todavía no haya respondido el servicio, no porque no se de ese caso. ¿Y si el servicio falla?En la app actual, si alguno de estos servicios falla, no se hace nada. En concreto, si falla el **servicio de obtener las tareas de una tasación** simplemente afecta a que no se actualizan los iconos de conversación. | @Noelia Sales Montes | Equipo técnico | RESUELTA | Cargamos lo que tengamos y conforme respondan los servicios actualizamos la vista. Mientras no está todo cargado, mostramos una etiqueta de carga para informar de que falta información por mostrar en ciertas celdas. |
| 11 | **Historia 11: Acciones al hacer *****swipe***** en una celda en Inicio de tasación**Las acciones en la app híbrida son: - *Swipe* hacia la derecha en celda de tasación: icono información (detalle de póliza, detalle de siniestro o resumen de tasación) - *Swipe* hacia la derecha en celda de siniestro: icono información (detalle de siniestro) - *Swipe* hacia la izquierda en cualquier celda: acción eliminar ¿Van a ser iguales ahora? ¿Tenemos los iconos? | @Noelia Sales Montes | Equipo técnico | PENDIENTE |  |
| 12 | **Historia 17: Vehículo no tasable**¿Tenemos la vista? | @Noelia Sales Montes | Equipo técnico | PENDIENTE | Pendiente de la vista. Se definirá cuando esté definido. |
| 13 | **Historia 12: Acciones al pulsar sobre una celda de siniestro en Inicio de tasación**Respecto a los nuevos diálogos que nos han trasladado desde negocio: - Diálogo "CONFIRMACIÓN" con el texto "Atención: este vehículo presenta un rechazo general" y botones "CANCELAR" y "ACEPTAR". - Diálogo "AVISO" con el texto "Este vehículo debe ser tasado por un perito" y botón "ACEPTAR". El segundo diálogo diría que es el del criterio 1 de la historia 14, que muestra el texto: "Debido a cambios en la situación de la póliza este vehículo deberá ser tasado por el perito de zona" y no permite continuar.El primer diálogo no lo he visto exactamente, pero creo que sería el diálogo de CONFIRMACIÓN con botones "Cancelar" / "Aceptar" (referencia: *util.service.ts, línea 313*). En este caso, el texto del diálogo llega a través del parámetro `mensaje`, cuyo posible origen es dinámico: `mensajeErrorValidacion` (referencia: *tasacion-datos-siniestros.page.ts, línea 669*). | @Noelia Sales Montes | Equipo técnico | PENDIENTE |  |
| 14 | **Historias 12, 13 y 14: Acciones al pulsar…**En estas 3 historias aparecen: - Avisos tipo toast de color naranja, que no permiten continuar. - Avisos tipo toast de color rojo (errores), que no permiten continuar. - Diálogos con título "Aviso", que no permiten continuar. - Diálogos con título "Confirmación", que permiten continuar si se pulsa en el botón "Continuar". - Diálogos con título "Confirmación", que tienen 2 botones (Aceptar y Cancelar), pero no permiten continuar y ambos botones son equivalentes. ¿Cuál sería la equivalencia en diálogos o avisos? | @Noelia Sales Montes | Equipo técnico | RESUELTA | Todos van a ser el mismo diálogo con 3 diferencias: - Diálogo con un solo botón "Entendido". - Diálogo con 2 botones: "Acción prioritaria" y "Acción secundaria". - Diálogo con 2 botones (igual que el anterior), pero con una ilustración, para darles más énfasis. |
