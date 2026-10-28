# Home - Definición de historias de usuario

| Objetivos |
|---|
| Implementar las bases de la home de la app, incluyendo la tabbar principal, así como procedimientos que se replican por igual como la gestión de errores. |

1. Información previa
1. JIRA
1. Diseño
1. Historias de usuario
1. Historia 1: Home para usuarios con rol de perito APROBADA
1. Información anexa
1. Imágenes
1. Opción por defecto
1. Historia 2: Home para usuarios con rol de taller PENDIENTE UX
1. Información anexa
1. Imágenes
1. Opción por defecto
1. Historia 3: Comprobación de sesión in-app APROBADA
1. Historia 4: Comprobación de sesión in-app para usuarios con biometría activa APROBADA
1. Historia 5: Comprobación de sesión in-app para usuarios sin biometría activa APROBADA
1. Historia 6: Cierre de sesión PENDIENTE UX
# Información previa

## JIRA

Historia 1:  - Obteniendo datos de incidencia... ESTADO

Historia 2:  - Obteniendo datos de incidencia... ESTADO

Historias 3, 4 y 5:  - Obteniendo datos de incidencia... ESTADO

Historia 6: Pendiente

## Diseño

# Historias de usuario

Historia 1: Home para usuarios con rol de perito 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 1: Home para usuarios con rol de perito APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario logado | Logue correctamente Y es un usuario con rol de perito Y no tiene permiso de lectura de tasaciones Y el perito es inspector o asesor | Se muestra la HOME, en la cual aparecerá una tabbar con las siguientes opciones: 1. TAREAS 1. INSPECCIÓN 1. TASACIÓN 1. BUSCAR Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId11.tmp)
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId12.tmp)
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId13.tmp) |
| 2 | APROBADO | Un usuario logado | Logue correctamente Y es un usuario con rol de perito Y no tiene permiso de lectura de tasaciones Y el perito no es inspector y no es asesor | Se muestra la HOME, en la cual aparecerá una tabbar con las siguientes opciones: 1. TAREAS 1. AUDITORÍA 1. TASACIÓN 1. BUSCAR |
| 3 | APROBADO | Un usuario logado | Logue correctamente Y es un usuario con rol de perito Y tiene permiso de lectura de tasaciones | Se muestra la HOME, en la cual no aparecerá la tabbar. |

### Información anexa

Los datos a revisar para cada casuística son:

1. El usuario tiene rol de perito si viene definido peritos en el servicio de obtener proveedores (se puede verificar también mirando el perito almacenado en memoria tras este servicio) .
1. El usuario perito tiene permiso de lectura de tasaciones si viene definido LECTURA_TASACIONES en el servicio de obtener permisos.
1. El usuario perito es inspector o asesor si perito.esTipoInspector o si esTipoInspector son true en el perito almacenado en memoria después de obtener el servicio de obtener proveedores.
#### Imágenes

Importante: La opción de IMÁGENES la quitamos de la tabbar por indicación de negocio.

#### Opción por defecto

Al entrar desde el login, se debe ver una opción por defecto seleccionada en la tabbar.

##### Usuario perito

Va a la vista de Trabajo pendiente seleccionada en la tabbar.

Historia 2: Home para usuarios con rol de taller 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 2: Home para usuarios con rol de taller PENDIENTE UX

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | PENDIENTE UX | Un usuario logado | Logue correctamente Y es un usuario con rol de taller Con todos los permisos necesarios dados | Se muestra la HOME, en la cual aparecerá una tabbar con las siguientes opciones: 1. SEGUIMIENTO 1. AGENDA 1. TASACIÓN 1. PERITO |
| 2 | PENDIENTE UX | Un usuario logado | Logue correctamente Y es un usuario con rol de taller Sin permiso de reparación | Se muestra la HOME, en la cual aparecerá la misma tabbar del criterio 4, pero ocultando la opción de SEGUIMIENTO. |
| 3 | PENDIENTE UX | Un usuario logado | Logue correctamente Y es un usuario con rol de taller Sin permiso de agenda | Se muestra la HOME, en la cual aparecerá la misma tabbar del criterio 4, pero ocultando la opción de AGENDA. |
| 4 | PENDIENTE UX | Un usuario logado | Logue correctamente Y es un usuario con rol de taller Sin permiso de tasación | Se muestra la HOME, en la cual aparecerá la misma tabbar del criterio 4, pero ocultando la opción de TASACIÓN. |
| 5 | PENDIENTE UX | Un usuario logado | Logue correctamente Y es un usuario con rol de taller Sin permiso de solicitud a perito | Se muestra la HOME, en la cual aparecerá la misma tabbar del criterio 4, pero ocultando la opción de PERITO. |

### Información anexa

Los datos a revisar para cada casuística son:

1. El usuario tiene rol de taller si viene definido instalacion en el servicio de obtener proveedores.
1. El usuario taller tiene permiso de reparación si viene definido TALLER_REPARA en el servicio de obtener permisos.
1. El usuario taller tiene permiso de agenda si viene definido MENU_AGENDA en el servicio de obtener permisos e instalacion.agenda es “SI” en el servicio de obtener proveedores (se puede verificar también mirando la instalacion almacenada en memoria tras este servicio).
1. El usuario taller tiene permiso de tasación si viene definido TALLER_TASA en el servicio de obtener permisos.
1. El usuario taller tiene permiso de solicitud a perito si viene definido instalacion.solicitudPerito e instalacion.tipoConcierto es 1 o 4 en el servicio de obtener proveedores.
#### Imágenes

Importante: La opción de IMÁGENES la quitamos de la tabbar por indicación de negocio.

#### Opción por defecto

Al entrar desde el login, se debe ver una opción por defecto seleccionada en la tabbar.

##### Usuario taller

1. Si en permisos viene TALLER_TASA -> va a la vista de Tasación seleccionada en la tabbar.
1. Si no, si en permisos viene TALLER_REPARA -> va a la vista de Reparaciones seleccionada en la tabbar.
1. Si no, si cumple la siguientes condiciones -> va a la vista de Perito seleccionada en la tabbar.
Las condiciones para este caso son:
1. El usuario tiene el rol de taller, es decir, viene definido instalacion en el servicio de obtener proveedores
1. instalacion > solicitudPerito es true
1. instalacion > tipoConcierto es 1 o 4
1. Si no cumple ninguna de las anteriores -> va a la vista de Usuario seleccionada en la tabbar.
Historia 3: Comprobación de sesión in-app 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 3: Comprobación de sesión in-app APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario | Se realice cualquier petición durante el uso de la app | Se comprueba si el token actual sigue siendo válido. |
| 2 | APROBADO | Un usuario | Se realice cualquier petición durante el uso de la app Y el token sigue siendo válido | Se continúa con la petición que se iba a ejecutar. |
| 3 | APROBADO | Un usuario | Se realice cualquier petición durante el uso de la app Y el token NO sigue siendo válido | Se llama al servicio de refresco de token sin mostrar otra vista de carga (ya debería haber una mostrándose). |
| 4 | APROBADO | Un usuario | Se realice cualquier petición durante el uso de la app Y el token NO sigue siendo válido Y el servicio de refresco de token responde correctamente | Se realizan las siguientes acciones: 1. Se actualiza el token en local (para poder utilizarlo en el resto de peticiones a partir de ahora). 1. Se oculta el spinner de carga. 1. Se continúa con la petición que se iba a ejecutar. |
| 5 | APROBADO | Un usuario | Se realice cualquier petición durante el uso de la app Y el token NO sigue siendo válido Y el servicio de refresco de token falla | Se comprueba si hay biometría disponible y activa. Continúa el proceso en la historia 3 u 4, según corresponda. |

Historia 4: Comprobación de sesión in-app para usuarios con biometría activa 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 4: Comprobación de sesión in-app para usuarios con biometría activa APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario con la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y la biometría está disponible y activa | Se solicita al usuario que valide la biometría, mediante el procedimiento nativo. |
| 2 | APROBADO | Un usuario con la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y el usuario valida la biometría correctamente | Se realizan las siguientes acciones: 1. Se muestra una vista de carga: 1. Título: "Refrescando la sesión…". 1. Descripción: "Por favor, espere…". 1. Se llama al servicio de login con las credenciales guardadas en almacenamiento seguro. Nota: Esto implica llamar únicamente al servicio de login para obtener un nuevo token, no al resto de servicios que se lanzan tras el procedimiento de login normal. Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId15.tmp) |
| 3 | APROBADO | Un usuario con la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y el usuario NO valida la biometría correctamente | Se oculta la animación de carga y se debe mostrar la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA. Esta vista tendrá los siguientes elementos, todos centrados horizontalmente: 1. Título: "Tu sesión ha caducado". 1. Texto: "Inicia sesión de nuevo para continuar.". 1. Botón "Acceso con biometría", con el icono de biometría a la izquierda. Botón con estilo primario. 1. Enlace "Ir al Inicio de sesión". Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId17.tmp) |
| 4 | APROBADO | Un usuario con la biometría activada | Pulse sobre la sección de biometría de la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA | Se sigue viendo la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA, mientras se solicita al usuario que valide la biometría, mediante el procedimiento nativo. |
| 5 | APROBADO | Un usuario con la biometría activada | Pulse sobre la sección de biometría de la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA Y el usuario valida la biometría correctamente | Se realizan las siguientes acciones: 1. Se muestra una vista de carga: 1. Título: "Refrescando la sesión…". 1. Descripción: "Por favor, espere…". 1. Se llama al servicio de login con las credenciales guardadas en almacenamiento seguro. Nota: Esto implica llamar únicamente al servicio de login para obtener un nuevo token, no al resto de servicios que se lanzan tras el procedimiento de login normal. Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId15.tmp) |
| 6 | APROBADO | Un usuario con la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y el usuario introduce correctamente su biometría en cualquier intento (ya sea mostrándose la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA o no) Y el servicio de login funciona correctamente | Se realizan las siguientes acciones: 1. Si se está mostrando, se oculta la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA. 1. Se actualiza la sesión en local (para poder utilizarlo en el resto de peticiones a partir de ahora). 1. Se ejecuta el procedimiento que intentara lanzar el usuario en el criterio 1. |
| 7 | APROBADO | Un usuario con la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y el usuario introduce correctamente su biometría en cualquier intento Y el servicio de login falla | Se realizan las siguientes acciones: 1. Se oculta el spinner de carga. 1. Se muestra un aviso de error: 1. Título: "Lo sentimos" 1. Descripción: "¡Algo ha fallado! Por favor, inténtalo de nuevo en unos minutos.". Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId20.tmp) |
| 8 | APROBADO | Un usuario no logado | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar Y el usuario introduce correctamente su biometría en cualquier intento Y no hay conexión a internet | Se realizan las siguientes acciones: 1. Se oculta el spinner de carga. 1. Se muestra un aviso de error: 1. Título: "Lo sentimos" 1. Descripción: "Parece que no tienes conexión a Internet. Por favor, comprueba tu red y vuelve a intentarlo para seguir usando Pruebas Seguros.". Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId20.tmp) |
| 9 | APROBADO | Un usuario logado | Pulse en el botón IR A INICIO DE SESIÓN en la vista EXTENSIÓN DE SESIÓN CON BIOMETRÍA | Va a la vista de LOGIN de la historia 1, 2 o 3, según corresponda. |

Historia 5: Comprobación de sesión in-app para usuarios sin biometría activa 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 5: Comprobación de sesión in-app para usuarios sin biometría activa APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario SIN la biometría activada | Se realice cualquier petición durante el uso de la app Y el token NO se ha podido refrescar | Se oculta la animación de carga y se debe mostrar la vista CIERRE DE SESIÓN. Esta vista tendrá los siguientes elementos, todos centrados horizontalmente: 1. Título: "Tu sesión ha caducado". 1. Texto: "Tu sesión se ha cerrado automáticamente por seguridad. Vuelve a iniciar sesión para seguir navegando por la aplicación.". 1. Botón "Ir a Inicio de sesión", con el diseño del botón de "Acceso con biometría", pero sin el icono de biometría a la izquierda. Botón con estilo primario. Nota: No hay un diseño específico para esta vista, así que reutilizaremos el de la vista equivalente de biometría, mostrando solo un botón y sin el icono de biometría. Diseño: ![image](Home+-+Definición+de+historias+de+usuario_images/image_rId17.tmp) |
| 2 | APROBADO | Un usuario SIN la biometría activada | Pulse en el botón IR A INICIO DE SESIÓN en la vista CIERRE DE SESIÓN | Va a la vista de LOGIN. |

Historia 6: Cierre de sesión en Perfil 
![image](Home+-+Definición+de+historias+de+usuario_images/image_rId9.tmp)

## Historia 6: Cierre de sesión PENDIENTE UX

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | PENDIENTE | Un usuario logado | Pulse en la opción CERRAR SESIÓN de la vista MI INFORMACIÓN | Se muestra un diálogo nativo para preguntar al usuario si realmente quiere cerrar sesión. El fondo debe estar emborronado. El diálogo tendrá los siguientes elementos: 1. Título: "¿Seguro que quieres cerrar la sesión?". 1. Descripción: "¡Te vamos a echar de menos! Ten en cuenta que si cierras la sesión tendrás que volver a iniciarla para entrar en Pruebas Seguros.". 1. Botón azul: "Cerrar sesión". 1. Botón gris: "Cancelar". |
| 2 | PENDIENTE | Un usuario logado | Pulsa en CERRAR SESIÓN en el diálogo personalizado de CERRAR SESIÓN | Se ejecutan las siguientes acciones: 1. Se cierra el diálogo de CERRAR SESIÓN. 1. Se muestra un spinner de carga. 1. Se llama al servicio de cerrar sesión. Importante: En este caso no aplica la comprobación de token de la historia 6. Si el token ya está caducado, no hay sesión que cerrar. Duda: ¿Cómo es la vista de carga dentro de la app? |
| 3 | PENDIENTE | Un usuario logado | Pulsa en CANCELAR en el diálogo personalizado de CERRAR SESIÓN | Se cierra el diálogo de CERRAR SESIÓN, visualizando la vista tal cual estaba previamente. |
| 4 | PENDIENTE | Un usuario logado | Pulsa en CERRAR SESIÓN en el diálogo personalizado de CERRAR SESIÓN y el servicio responde (es irrelevante si con éxito o error) | Se ejecutan las siguientes acciones: 1. Se oculta el spinner de carga. 1. Se borra la sesión actual almacenada en el almacenamiento seguro. 1. Va a la vista de LOGIN. |

