# Onboarding - Definición de historias de usuario

| Objetivos |
|---|
| **Reimplementar el procedimiento de login en nativo.** |

1. Información previa
1. JIRA
1. Diseño
1. Historias de usuario
1. Historia 1: Onboarding APROBADA
1. Información anexa
1. Permisos de cámara + Fotos/Galería
1. Historia 2: Confirmación de uso de biometría APROBADA
1. Información anexa
# Información previa

## JIRA

- Obteniendo datos de incidencia... ESTADO

## Diseño

# Historias de usuario

Historia 1: Onboarding 
![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 1: Onboarding APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Termine de cargar el proceso post-login (antes de ir a la home) | Se muestra la vista PERMISO DE NOTIFICACIONES. Esta vista contiene los siguientes elementos: 1. Título: "Pruebas Seguros evoluciona contigo". 1. Imagen informativa. 1. Descripción: "Te damos la bienvenida a Pruebas Seguros, tu aplicación móvil renovada por completo y con novedades: 1. Login nativo 1. Nuevo diseño 1. ¡Y mucho más!" 1. Botón: "Continuar". Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId9.tmp) |
| 2 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding |  | Se muestra la vista PERMISO DE NOTIFICACIONES. Esta vista contiene los siguientes elementos: 1. Título: "No te pierdas nada". 1. Imagen informativa. 1. Descripción: "Ten el control de tu día a día: cambios en tu ruta, nuevas asignaciones y más. Configura tus preferencias en Ajustes.". Parte del texto está resaltado. 1. Botón: "Activar notificaciones". 1. Enlace: "En otro momento". Este enlace no está en el diseño de esta pantalla. El diseño debe ser igual que en el criterio 1 de la historia 2. Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId11.tmp) |
| 3 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Pulse en el botón ACTIVAR NOTIFICACIONES en la vista PERMISO DE NOTIFICACIONES | Se muestra el diálogo nativo que solicita al usuario que active el permiso de notificaciones. Nota sobre los textos de permisos: 1. El diálogo nativo de solicitud de permiso de notificaciones en iOS debe mostrar el siguiente texto: “Recibirás avisos con todo lo relevante de tu actividad diaria.” ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId12.tmp) |
| 4 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Seleccione cualquier opción en el diálogo que le solicita el permiso de notificaciones O pulse en EN OTRO MOMENTO en la vista PERMISO DE NOTIFICACIONES | Se muestra la vista PERMISO DE UBICACIÓN. Esta vista contiene los siguientes elementos: 1. Título: "Tu ruta, más eficiente". 1. Imagen informativa. 1. Descripción: "Usamos la ubicación para mostrarte los talleres en tu ruta diaria y hacerte todo más fácil.". Parte del texto está resaltado. 1. Botón: "Activar ubicación". 1. Enlace: "En otro momento". Este enlace no está en el diseño de esta pantalla. El diseño debe ser igual que en el criterio 1 de la historia 2. Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId14.tmp) |
| 5 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Pulse en el botón ACTIVAR UBICACIÓN en la vista PERMISO DE UBICACIÓN | Se muestra el diálogo nativo que solicita al usuario que active el permiso de ubicación. Nota sobre los textos de permisos: 1. El diálogo nativo de solicitud de permiso de ubicación en iOS debe mostrar el siguiente texto: “Con tu ubicación, te guiaremos a los talleres de tu ruta diaria de forma rápida y sencilla.” ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId15.tmp) |
| 6 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Seleccione cualquier opción en el diálogo que le solicita el permiso de ubicación O pulse en EN OTRO MOMENTO en la vista PERMISO DE UBICACIÓN | Se muestra la vista PERMISO DE CÁMARA. Esta vista contiene los siguientes elementos: 1. Título: "Da vida a cada tasación". 1. Imagen informativa. 1. Descripción: "Activa la cámara y agiliza tus tasaciones capturando imágenes al instante.". Parte del texto está resaltado. 1. Botón: "Activar cámara". 1. Enlace: "En otro momento". Este enlace no está en el diseño de esta pantalla. El diseño debe ser igual que en el criterio 1 de la historia 2. Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId17.tmp) |
| 7 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Pulse en el botón ACTIVAR CÁMARA en la vista PERMISO DE CÁMARA | Se muestra el diálogo nativo que solicita al usuario que active el permiso de cámara y el permiso de Fotos/Galería. Nota sobre los textos de permisos: 1. El diálogo nativo de solicitud de permiso de ubicación en iOS debe mostrar el siguiente texto: “Permite el acceso a la cámara para capturar imágenes en las tasaciones de forma sencilla.” 1. El diálogo nativo de solicitud de permiso de ubicación en iOS debe mostrar el siguiente texto: “Permite el acceso a tus imágenes para adjuntar imágenes en las tasaciones de forma sencilla.” ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId18.tmp) |
| 8 | APROBADO | Un usuario logado en un dispositivo en el que nunca ha visualizado el onboarding | Seleccione cualquier opción en el diálogo que le solicita el último permiso de cámara/fotos O pulse en PREFIERO ACTIVARLO MÁS TARDE en la vista PERMISO DE CÁMARA | Se deben realizar las siguientes acciones: 1. Guardar que ya se ha visualizado el onboarding en las preferencias de la app (sin distinguir el usuario que lo ha visto). 1. Ir a a la vista HOME (funcionalidad Home). |

### Información anexa

#### Permisos de cámara + Fotos/Galería

Creo que en iOS sería estos permisos los que hay que pedir:

1. NSCameraUsageDescription
1. NSPhotoLibraryUsageDescription
Y en Android: android.permission.CAMERA, READ_MEDIA_IMAGES

Historia 2: Confirmación de uso de biometría 
![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId7.tmp)

## Historia 2: Confirmación de uso de biometría APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Llegue a la home | Se muestra la modal ACTIVAR BIOMETRÍA sobre la vista HOME (que mostrará la funcionalidad que corresponda según el tipo de usuario). Esta vista contiene los siguientes elementos: 1. Título: "Accede al instante, sin esfuerzo". 1. Imagen informativa. 1. Descripción: "Utiliza el acceso con biometría de tu dispositivo y evita introducir el usuario y contraseña a mano.". 1. Botón: "Activar biometría". 1. Enlace: "En otro momento". Nota: La modal no debe cerrarse por ningún método no especificado (ni pulsando fuera de la vista ni haciendo swipe). Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId20.tmp) |
| 2 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA en un dispositivo iOS | Pulse en el botón ACTIVAR BIOMETRÍA en la vista ACTIVAR BIOMETRÍA | Se muestra el diálogo nativo que le pide que active el permiso de biometría. Nota sobre los textos de permisos: 1. El diálogo nativo de solicitud de permiso de Face ID/Touch ID en iOS debe mostrar el siguiente texto: “Haz tu inicio de sesión más rápido cada vez que entras a la app.” |
| 3 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA en un dispositivo Android | Pulse en el botón ACTIVAR BIOMETRÍA en la vista ACTIVAR BIOMETRÍA | Se solicita al usuario que se autentique biométricamente. |
| 4 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Pulse en el enlace EN OTRO MOMENTO en la vista ACTIVAR BIOMETRÍA | Se ejecutan las siguientes acciones: 1. Guardar que ya ha visualizado la vista ACTIVAR BIOMETRÍA en las preferencias de la app (sin distinción de usuario). 1. Cierra la modal ACTIVAR BIOMETRÍA. |
| 5 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA en un dispositivo iOS | Active el permiso en el diálogo nativo que aparece tras pulsar en el botón CONFIGURAR ACCESO CON BIOMETRÍA en la vista ACTIVAR BIOMETRÍA | Se solicita al usuario que se autentique biométricamente. |
| 6 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Valide la verificación biométrica tras pulsar en el botón CONFIGURAR ACCESO CON BIOMETRÍA en la vista PERMISOS NOTIFICACIONES | Se muestra la modal BIOMETRÍA ACTIVA sobre la vista HOME (que mostrará la funcionalidad que corresponda según el tipo de usuario). Esta vista contiene los siguientes elementos: 1. Título: "Acceso con biometría activado". 1. Imagen informativa. 1. Descripción: "Ahora puedes iniciar sesión usando tu identificación biométrica.". 1. Botón: "Continuar". Nota: La modal no debe cerrarse por ningún método no especificado (ni pulsando fuera de la vista ni haciendo swipe). Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId22.tmp) |
| 7 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Pulse en el botón CONTINUAR de la vista BIOMETRÍA ACTIVA | Se ejecutan las siguientes acciones: 1. Guardar que el usuario ya ha visualizado la vista ACTIVAR BIOMETRÍA en las preferencias de la app. 1. Cierra la modal BIOMETRÍA ACTIVA. |
| 8 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | No valide la verificación biométrica tras pulsar en el botón CONFIGURAR ACCESO CON BIOMETRÍA en la vista ACTIVAR BIOMETRÍA O no active el permiso en el diálogo nativo que aparece tras pulsar en el botón CONFIGURAR ACCESO CON BIOMETRÍA en la vista PERMISOS NOTIFICACIONES (en dispositivos iOS) O haya algún tipo de error en el proceso | Se muestra la modal BIOMETRÍA ERROR sobre la vista HOME (que mostrará la funcionalidad que corresponda según el tipo de usuario). Esta vista contiene los siguientes elementos: 1. Título: "Algo ha fallado…". 1. Descripción: "No hemos podido activar el acceso con biometría. Vuelve a intentarlo o configúralo más tarde desde Ajustes.". 1. Botón: "Reintentar". 1. Enlace: "En otro momento". Nota: La modal no debe cerrarse por ningún método no especificado (ni pulsando fuera de la vista ni haciendo swipe). Diseño: ![image](Onboarding+-+Definición+de+historias+de+usuario_images/image_rId24.tmp) |
| 9 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Pulse en el botón REINTENTAR de la vista BIOMETRÍA ERROR | Vuelve a iniciar el proceso como si hubiera pulsado en ACTIVAR BIOMETRÍA en la vista ACTIVAR BIOMETRÍA. |
| 10 | APROBADO | Un usuario logado cuyo dispositivo disponga de biometría en el que nunca se ha visualizado la vista de ACTIVAR BIOMETRÍA | Pulse en el botón EN OTRO MOMENTO de la vista PERMISO DE BIOMETRÍA ERROR | Se ejecutan las siguientes acciones: 1. Guardar que el usuario ya ha visualizado la vista ACTIVAR BIOMETRÍA en las preferencias de la app. 1. Cierra la modal BIOMETRÍA ERROR. |

### Información anexa

En iOS hay que separar el paso de la solicitud del permiso y la autenticación biométrica, mientras que en android solo se solicita la autenticación. Por eso se separan ciertos criterios en función de la plataforma.

