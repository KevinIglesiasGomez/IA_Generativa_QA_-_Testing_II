# Login nativo - Definición de historias de usuario

| Objetivos |
|---|
| **Reimplementar el procedimiento de login en nativo.** |

1. Información previa
1. JIRA
1. Diseño
1. Historias de usuario
1. Historia 1: Login nativo sin credenciales previas APROBADA
1. Información anexa
1. Servicios
1. Validación de campos
1. Login
1. Proceso de recuperación de contraseña
1. Historia 2: Login nativo con biometría APROBADA
1. Información anexa
1. Cómo detectar si el usuario no tiene biometría configurada a nivel de dispositivo
1. Historia 3: Comprobación de sesión al arrancar la app (autologado) APROBADA
1. Historia 4: Finalización del flujo de login APROBADO
1. Historia 5: Gestión de errores del flujo de login APROBADA
# Información previa

## JIRA

- Obteniendo datos de incidencia... ESTADO

## Diseño

# Historias de usuario

Historia 1: Login nativo sin credenciales previas 
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 1: Login nativo sin credenciales previas APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario no logado Y sin ningún registro de token ni credenciales previos | Termine de cargar el splash | Se muestra la vista LOGIN. Esta vista tendrá los siguientes elementos: 1. Título: "¡Bienvenido a Pruebas Seguros!". 1. Texto: "Accede con tus credenciales corporativas". 1. Campo de texto del usuario: 1. Por defecto, su valor es "". 1. El placeholder debe ser "Usuario". Cuando se introduzca texto en el campo, este placeholder transicionará hacia arriba para convertirse en el nombre del campo. Así se comportarán todos los campos de texto de la app. 1. Tiene un icono de usuario alineado a la izquierda. 1. Campo de texto de contraseña: 1. Por defecto, su valor es "". 1. El texto debe estar por defecto ofuscado (cuando se escriba texto no deben visualizarse los caracteres) y el icono del ojito debe aparecer tachado. 1. El placeholder debe ser "Contraseña", con el mismo comportamiento que el campo de usuario. 1. Tiene un icono de llave alineado a la izquierda. 1. Botón de inicio de sesión en estado normal. Con el texto "Iniciar sesión". Botón con estilo primario. Deshabilitado por defecto. 1. Enlace "¿Olvidaste tu contraseña?". Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId9.tmp) |
| 2 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente | Termine de cargar el splash | Se muestra la vista LOGIN, en la cual aparecerá relleno el campo de texto del usuario. Nota: El usuario debe estar almacenado en el almacenamiento seguro desde el último login exitoso. |
| 3 | APROBADO | Un usuario no logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y el campo de texto del usuario está vacío | Se sigue viendo la vista LOGIN, en la cual se resalta el campo de texto de usuario con error (el icono se sustituyen por el icono de aviso y todo se tiñe rojo) y se muestra un error debajo de él: "El usuario está vacío. Introduce tus datos e inténtalo de nuevo." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId11.tmp) |
| 4 | APROBADO | Un usuario no logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y el campo de texto de la contraseña está vacío | Se sigue viendo la vista LOGIN, en la cual se resalta el campo de texto de contraseña con error (el icono se sustituyen por el icono de aviso y todo se tiñe rojo) y se muestra un error debajo de él: "La contraseña está vacía. Introduce tus datos e inténtalo de nuevo." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId11.tmp) |
| 5 | APROBADO | Un usuario no logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y el campo de texto del usuario está vacío | Se sigue viendo la vista LOGIN, en la cual se resalta el campo de texto de usuario con error (el icono se sustituyen por el icono de aviso y todo se tiñe rojo) y se muestra un error debajo de él: "El formato del usuario es incorrecto. Revisa tus datos e inténtalo de nuevo." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId14.tmp) |
| 6 | APROBADO | Un usuario no logado | Ponga el foco (por cualquier método) en el campo de texto de usuario | Se sigue viendo la vista LOGIN, en la cual se cambia el campo de texto de usuario al estado focused. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId16.tmp) |
| 7 | APROBADO | Un usuario no logado | Ponga el foco (por cualquier método) en el campo de texto de contraseña | Se sigue viendo la vista LOGIN, en la cual se cambia el campo de texto de contraseña al estado focused. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId16.tmp) |
| 8 | APROBADO | Un usuario no logado | Introduzca texto en el campo de texto de usuario | Se sigue viendo la vista LOGIN, en la cual se cambia el campo de texto de usuario al estado typing. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId19.tmp) |
| 9 | APROBADO | Un usuario no logado | Introduzca texto en el campo de texto de contraseña | Se sigue viendo la vista LOGIN, en la cual se cambia el campo de texto de contraseña al estado typing. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId19.tmp) |
| 10 | APROBADO | Un usuario no logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y todos los campos están rellenos y son válidos | Se sigue viendo la vista LOGIN, en la cual: 1. Si se está visualizando algún banner rojo de la historia 5, se debe ocultar. 1. En el botón de inicio de sesión aparece la animación de carga a la izquierda del texto y cambia su texto por “Iniciando sesión…”. Además, se bloquea la interacción con toda la pantalla. 1. Se llama al servicio de login con los datos: 1. usuario: siendo este el contenido del campo usuario de la vista LOGIN. 1. password: siendo este el contenido del campo contraseña de la vista LOGIN. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId22.tmp) |
| 11 | APROBADO | Un usuario  logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y el servicio de login funcione correctamente | Se sigue viendo la vista LOGIN, con la animación de carga, y se ejecutan los siguientes pasos: 1. Se recupera el token de sesión del usuario recién logado del servicio de login. 1. Se guarda la sesión y las credenciales del usuario en almacenamiento seguro (por si el usuario tiene activa o va a querer activar la biometría en algún momento). 1. Llamada a los servicios de obtener datos necesarios para la carga de la app. Estos servicios pueden variar en función del usuario logado. |
| 12 | APROBADO | Un usuario no logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y haya algún problema con algún servicio posterior al login | Se realizan las acciones indicadas en la historia 5. |
| 13 | APROBADO | Un usuario logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y ningún servicio posterior al login falle | Se realizan las acciones indicadas en la historia 4. |
| 14 | APROBADO | Un usuario no logado | Pulse en el enlace ¿OLVIDASTE TU CONTRASEÑA? de la vista LOGIN | Abre la URL del proceso de recuperación de contraseña de RHSSO en un navegador externo. La URL se encuentra definida en la sección Información anexa. |

### Información anexa

#### Servicios

La definición completa de los servicios y el flujo de login y post-login, así como la diferencia entre los servicios obligatorios y opcionales, están descritos en la .

#### Validación de campos

El campo de texto de usuario debe validar la siguiente expresión regular: ^[A-Za-z0-9]{1,8}$

En Kotlin:

val regex = Regex("^[A-Za-z0-9]{1,8}$")

En Swift:

let pattern = "^[A-Za-z0-9]{1,8}$"

El campo de texto de contraseña solo debe validar si está vacío. No hay expresión regular a validar para contraseña.

#### Login

##### Implementación base

###### Android

1. Implementación: data > src > main > kotlin > es > mma > inmobiliaria > mutuacity > data > datasources > remote > api > apiAuth > *
###### iOS

1. Implementación: MutuaCity > Data > DataSources > Remote > AuthRemoteDataSource.swift - método doLogin
##### Descripción de datos para este proyecto

De momento solo tenemos el entorno de showroom que usaremos desde nuestros entornos PRE y STAGE.

Descriptor de OIDC:

Hay que sustituir:

1. Reino (va en el path de la URL): el anterior era mutuacityshowroom y el nuevo es solmobileshowroom
##### Ejemplo de peticiones

Se pueden ver en:

#### Proceso de recuperación de contraseña

URL:

Historia 2: Login nativo con biometría   
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 2: Login nativo con biometría  APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Termine de cargar el splash | Se sigue viendo la vista SPLASH, mientras se solicita de forma nativa la validación mediante biometría. Nota para iOS: 1. Se deben permitir 3 reintentos y, si ninguno de ellos es exitoso, utilizar el código. Nota sobre los textos de biometría: 1. El diálogo nativo de solicitud de permisos de biometría en iOS debe mostrar el siguiente texto: "Haz tu inicio de sesión más rápido cada vez que entras a la app." 1. El texto del prompt de validación por biometría (solo válido para Android y para Touch ID en iOS) debe ser: "Por favor, verifica tu identidad para continuar." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId27.tmp)
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId28.tmp)
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId29.tmp) |
| 2 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría en la vista SPLASH | Se sigue viendo la vista SPLASH, en la cual se llama al servicio de login con los datos: 1. usuario: siendo este el usuario almacenado en el almacenamiento securizado. 1. password: siendo esta la contraseña almacenada en el almacenamiento securizado. |
| 3 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría en la vista SPLASH Y el servicio de login funcione correctamente | Se sigue viendo la vista SPLASH y se ejecutan los siguientes pasos: 1. Se recupera el token de sesión del usuario recién logado del servicio de login. 1. Se guardan la sesión y las credenciales del usuario en almacenamiento seguro (por si el usuario tiene activa o va a querer activar la biometría en algún momento). 1. Llamada a los servicios de obtener datos necesarios para la carga de la app. Estos servicios pueden variar en función del usuario logado. |
| 4 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Termine de cargar el splash Y la biometría no se valida correctamente O haya algún problema con el servicio de login o con algún servicio posterior al login | Se muestra la vista LOGIN, en la cual aparecerá un nuevo botón. Este nuevo botón aparecerá justo debajo del botón de inicio de sesión y encima del enlace de “¿Olvidaste tu contraseña?”. Este botón será: 1. Botón "Acceso con biometría", con el icono de biometría a la izquierda. Botón con estilo secundario. Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId31.tmp) |
| 5 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Pulse en el botón de ACCESO CON BIOMETRÍA en la vista LOGIN | Se sigue viendo la vista LOGIN, mientras se solicita de forma nativa la validación mediante biometría. |
| 6 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría en la vista LOGIN | Se sigue viendo la vista LOGIN, en la cual: 1. Si se está visualizando el banner rojo del criterio 10, 11 o 12, se debe ocultar. 1. El botón de inicio de sesión cambia a estado de carga: 1. aparece la animación de carga a la izquierda del texto 1. cambia su texto por “Iniciando sesión…” 1. se bloquea la interacción en toda la pantalla 1. Se llama al servicio de login con los datos: 1. usuario: siendo este el usuario almacenado en el almacenamiento securizado. 1. password: siendo esta la contraseña almacenada en el almacenamiento securizado. |
| 7 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría (ya sea en LOGIN o en SPLASH) Y el servicio de login funcione correctamente | Se sigue viendo la vista actual (ya sea SPLASH o LOGIN) y se ejecutan los siguientes pasos: 1. Se recupera el token de sesión del usuario recién logado del servicio de login. 1. Se guardan la sesión y las credenciales del usuario en almacenamiento seguro (por si el usuario tiene activa o va a querer activar la biometría en algún momento). 1. Llamada a los servicios de obtener datos necesarios para la carga de la app. Estos servicios pueden variar en función del usuario logado. |
| 8 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría en la vista LOGIN Y haya algún problema con algún servicio posterior al login | Se realizan las acciones indicadas en la historia 5. |
| 9 | APROBADO | Un usuario no logado Y con registro de usuario logado previamente Y con biometría activa | Se valida correctamente la biometría en la vista LOGIN Y ningún servicio posterior al login falle | Se realizan las acciones indicadas en la historia 4. |

### Información anexa

#### Cómo detectar si el usuario no tiene biometría configurada a nivel de dispositivo

##### Android

Comprobando si el manager de biometría devuelve el error "BIOMETRIC_ERROR_NONE_ENROLLED".

##### iOS

Llamando a canEvaluate con la política "deviceOwnerAuthenticationWithBiometrics" y comprobando si devuelva el error "biometryNotEnrolled":

Historia 3: Comprobación de sesión al arrancar la app 
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 3: Comprobación de sesión al arrancar la app (autologado) APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario | Arranque la app desde 0 | Se muestra la vista SPLASH. Se comprueba si existe un token previo almacenado. **Nota**: Las comprobaciones obligatorias de la app deben hacerse antes de este proceso (tal como estaba definido en la ). Esto incluye: 1. Comprobación de conexión a internet. 1. Comprobación de seguridad del dispositivo. 1. Comprobación de diálogo de forzado. |
| 2 | APROBADO | Un usuario | Arranque la app desde 0 Y existe un *token* previo almacenado | Mientras se sigue mostrando la vista SPLASH, se comprueba si el token previo almacenado sigue siendo válido. |
| 3 | APROBADO | Un usuario | Arranque la app desde 0 Y el *token* sigue siendo válido | Mientras se sigue mostrando la vista SPLASH, se realizan las acciones indicadas en la historia 4. |
| 4 | APROBADO | Un usuario no logado | Arranque la app desde 0 Y sin ningún registro de *token* ni credenciales previos | Va a la vista LOGIN de la historia 1. |
| 5 | APROBADO | Un usuario no logado | Arranque la app desde 0 Y existe un *token* previo almacenado pero ya no es válido | Va a la vista LOGIN de la historia 1 o de la historia 2, en función de si tiene biometría activa o no. |
| 6 | APROBADO | Un usuario no logado | Arranque la app desde 0 Realiza las llamadas a los servicios obligatorios que se llaman tras el login normal Y alguno de los servicios obligatorios requeridos falla | Va a la vista LOGIN de la historia 1 o de la historia 2, en función de si tiene biometría activa o no. |

Historia 4: Finalización del flujo de login 
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 4: Finalización del flujo de login APROBADO

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario logado | Se inicie sesión en cualquier vista afectada (Historia 1, 2 o 3) Y ningún servicio obligatorio falle Y hay un único perito o un taller | Llama a todos los servicios necesarios, mientras continúa mostrándose la vista actual en el mismo estado. |
| 2 | APROBADO | Un usuario logado | Pulse en el botón INICIAR SESIÓN de la vista LOGIN Y ningún servicio obligatorio falle Y hay varios peritos | Realiza las siguientes acciones: 1. Llama a todos los servicios necesarios hasta donde se pueda, mientras continúa mostrándose la vista actual en el mismo estado. 1. Se muestra la modal SELECCIÓN DE PERITO sobre la vista actual, para elegir con qué perito se desea continuar el proceso. No debe permitirse ocultar esta modal por ningún método.

En esta vista se visualiza: 1. Título: “Selecciona un perfil” 1. Listado de peritos. Por defecto, está seleccionado el primer perito. El listado de peritos se obtiene del array peritos del servicio de obtener proveedores.

Por cada perito, se muestra: 1. A la izquierda, círculo con la inicial del perito (primera letra del nombre). El color del fondo del círculo debe ser uno de los 3 colores del componente obtenido de forma aleatoria. 1. Arriba, el identificador del perito. Este valor es el parámetro id del perito dentro del array peritos del servicio de obtener proveedores. 1. Abajo, el nombre del perito. Se compondrá con el texto “NOMBRE APELLIDOS”, siendo NOMBRE el parámetro nombrePerito y APELLIDOS, el parámetro apellidosPerito, ambos del perito dentro del array peritos del servicio de obtener proveedores. Si después de componer el texto sobran espacios, deben eliminarse (hacer un trim). 1. Alineado a la derecha del todo, un icono de flecha. Notas: 1. El enlace de “Iniciar sesión con otro perfil” tampoco. 1. Hay que preparar la vista suponiendo que pueden venir n peritos (no únicamente 2). 1. La modal no debe cerrarse por ningún método no especificado (ni pulsando fuera de la vista ni haciendo swipe). Diseño: 1. Vista: https://www.figma.com/design/JAImevUVjtPlEcHQCQcDKB/Pruebas-Seguros-Nativo-%C2%B7-Funcionalidades?node-id=127-5069&m=dev 1. Avatar (librería):https://www.figma.com/design/txM3KJSHgLe0Kl4HP29cJW/Pruebas-Seguros-Nativo-%C2%B7-Librer%C3%ADa?node-id=382-2000&m=dev ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId37.tmp)
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId38.tmp) |
| 3 | APROBADO | Un usuario logado | Pulse en cualquier perito de la modal SELECCIÓN DE PERITO | Realiza las siguientes acciones: 1. Se oculta la modal SELECCIÓN DE PERITO y vuelve a mostrarse la vista previa en el mismo estado en que estaba. 1. Se guarda la información el perito seleccionado en memoria. 1. Llama al resto de servicios necesarios. |
| 4 | APROBADO | Un usuario logado | Al llamar al resto de servicios, no hay impedimentos para continuar con el login | Va a la vista HOME (Historia 1 de la ), según el rol del usuario que corresponda. |
| 5 | APROBADO | Un usuario logado | Al llamar al resto de servicios, se detecta que el usuario no tiene las condiciones legales aprobadas | Se muestra una modal CONDICIONES LEGALES sobre la vista actual, con el siguiente contenido: 1. Título: “Algo ha fallado...”. 1. Descripción: “Para utilizar esta herramienta es necesario que aceptes los términos y condiciones de usuario en la versión de escritorio de Pruebas Seguros.” 1. Botón “Volver a Iniciar sesión”. Nota: La modal no debe cerrarse por ningún método no especificado (ni pulsando fuera de la vista ni haciendo swipe). Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId41.tmp) |
| 6 | APROBADO | Un usuario logado | Pulse en el botón VOLVER A INICIAR SESIÓN en la modal CONDICIONES LEGALES | Vuelve a la vista LOGIN (criterio 1 de la historia 1 o de la historia 2 en función de si tiene activa la biometría o no). |

Historia 5: Gestión de errores del flujo de login 
![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 5: Gestión de errores del flujo de login APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario no logado | Se intente iniciar sesión desde la vista LOGIN Y al llamar a algún servicio obligatorio no hay conexión a internet | Se sigue viendo la vista de login que corresponda, en la cual: 1. el botón de inicio de sesión volverá a su estado normal (criterio 1 de la Historia 1) 1. se resaltan los campos de texto de usuario y email con error (los iconos se sustituyen por el icono de aviso y todo se tiñe rojo) 1. se muestra un texto de error debajo de ambos campos: "Parece que no tienes conexión a Internet. Por favor, comprueba tu red y vuelve a intentarlo para seguir usando Pruebas Seguros." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId43.tmp) |
| 2 | APROBADO | Un usuario no logado | Se intente iniciar sesión desde la vista LOGIN Y algún servicio obligatorio falle con un error 40X | Se sigue viendo la vista de login que corresponda, en la cual: 1. el botón de inicio de sesión volverá a su estado normal (criterio 1 de la Historia 1) 1. se resaltan los campos de texto de usuario y email con error (los iconos se sustituyen por el icono de aviso y todo se tiñe rojo) 1. se muestra un texto de error debajo de ambos campos: "El usuario o la contraseña son incorrectos. Comprueba tus datos e inténtalo de nuevo." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId43.tmp) |
| 3 | APROBADO | Un usuario no logado | Se intente iniciar sesión desde la vista LOGIN Y algún servicio obligatorio falle con un error 50X u otros | Se sigue viendo la vista de login que corresponda, en la cual: 1. el botón de inicio de sesión volverá a su estado normal (criterio 1 de la Historia 1) 1. se resaltan los campos de texto de usuario y email con error (los iconos se sustituyen por el icono de aviso y todo se tiñe rojo) 1. se muestra un texto de error debajo de ambos campos: "¡Algo ha fallado! Por favor, inténtalo de nuevo en unos minutos." Diseño: ![image](Login+nativo+-+Definición+de+historias+de+usuario_images/image_rId43.tmp) |

