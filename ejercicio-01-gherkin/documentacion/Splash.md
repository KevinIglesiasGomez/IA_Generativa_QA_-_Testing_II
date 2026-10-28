# Splash - Definición de historias de usuario

| Objetivos |
|---|
| **Definir la vista de splash de la app de Pruebas Seguros nativa, junto con todos los procedimientos internos que deben lanzarse en este punto de acceso.** |

1. Información
1. JIRA
1. Diseños
1. Historias de usuario
1. Historia 1: Splash APROBADA
1. Información anexa
1. Flujo de comprobaciones del splash
1. Detección de dispositivo inseguro
1. Forzado
# Información

## JIRA

## Diseños

# Historias de usuario

Historia 1: Splash 
![image](Splash_images/image_rId6.tmp)

## Historia 1: Splash APROBADA

|  | Estado | Dado | Cuando | Entonces |
|---|---|---|---|---|
| 1 | APROBADO | Un usuario | Acceda a la app | Se muestra la vista SPLASH. Esta vista mostrará una imagen fija. En esta vista se obtendrá la información necesaria para poder continuar con la ejecución de la app. El flujo concreto a seguir está descrito en la sección Información anexa. Diseño: ![image](Splash_images/image_rId8.tmp) |
| 2 | APROBADO | Un usuario | Termine de cargar el splash sin detectar ningún tipo de impedimento | Va a la vista de login que corresponda (historias 1, 2 y 3 de la ) o pasa el proceso de autologado si ya estaba logado. |
| 3 | APROBADO | Un usuario | Se detecte que el dispositivo es inseguro | Se muestra un diálogo nativo que indica que el dispositivo es inseguro, sobre la vista LOGIN. Se impide el acceso total a la app. El diálogo tendrá los siguientes elementos: 1. Título: "Lo sentimos". 1. Descripción: "Hemos detectado que se ha modificado la configuración de fábrica del sistema operativo de este dispositivo. Por ello, no podrás utilizar la App de Pruebas Seguros y se cerrará al pulsar en Aceptar." 1. Botón primario: "Aceptar". 1. Sin botón secundario. Al pulsar en cualquier zona externa al diálogo, no debe ejecutar ninguna acción (ni siquiera cerrar el diálogo). |
| 4 | APROBADO | Un usuario | Pulse en el botón ACEPTAR del diálogo de dispositivo inseguro | Se cierra la app completamente. |
| 5 | APROBADO | Un usuario | Se detecte que hay que mostrar la vista de actualización | Se muestra un diálogo que indica que hay una actualización forzada de la app, sobre la vista LOGIN. El diálogo tendrá los siguientes elementos: 1. Título: updateDialog.title 1. Descripción: updateDialog.body 1. Botón primario: updateDialog.okButtonLabel 1. Botón secundario: updateDialog.koButtonLabel Al pulsar en cualquier zona externa al diálogo, no debe ejecutar ninguna acción (ni siquiera cerrar el diálogo). Importante: La forma de pintar esos diálogos está definida en la sección Servicios y procesos dentro de Información anexa. Diseño: ![image](Splash_images/image_rId11.tmp) |
| 6 | APROBADO | Un usuario | Pulse en un botón del diálogo de actualización Y su acción correspondiente sea update | Se abre la ficha de la app en la store correspondiente. Importante: La acción que ejecuta este criterio está definida en la sección Servicios y procesos. |
| 7 | APROBADO | Un usuario | Pulse en un botón del diálogo de actualización Y su acción correspondiente sea exit | Se cierra la app completamente. |
| 8 | APROBADO | Un usuario | Pulse en un botón del diálogo de actualización Y su acción correspondiente sea cancel | Se cierra el diálogo y va a la vista de login que corresponda (historias 1, 2 y 3 de la ) o pasa el proceso de autologado si ya estaba logado. |
| 9 | APROBADO | Un usuario | Se detecte que hay que mostrar la vista de "no hay conexión" | Se muestra un diálogo personalizado que indica que no hay conexión a internet, sobre la vista LOGIN. El diálogo tendrá los siguientes elementos: 1. Título: "Revisa tu conexión". 1. Descripción: "No parece haber conexión. Por favor, asegura que estás conectado a la red correcta o no podrás hacer uso de la app de Pruebas Seguros.". 1. Botón primario: "Reintentar". 1. Botón secundario: "Salir". Al pulsar en cualquier zona externa al diálogo, no debe ejecutar ninguna acción (ni siquiera cerrar el diálogo). Diseño: ![image](Splash_images/image_rId11.tmp) |
| 10 | APROBADO | Un usuario | Pulse en el botón REINTENTAR del diálogo de "no hay conexión" | Se reintenta el flujo desde el principio. |
| 11 | APROBADO | Un usuario | Pulse en el botón SALIR del diálogo de "no hay conexión" | Se cierra la app completamente. |

### Información anexa

#### Flujo de comprobaciones del splash

1. Comprobación de conexión a internet:
1. Si el dispositivo tiene conexión a internet, se realiza la comprobación de la seguridad del dispositivo:
1. Si el dispositivo es seguro, conectar con Firebase Remote Config para revisar si hay una actualización de la app.
1. Si hay una actualización forzada de la app, va al criterio 2, mostrando el diálogo del criterio 5 por encima.
1. Si hay una actualización opcional de la app, va al criterio 2, mostrando el diálogo del criterio 6 por encima.
1. Si no hay una actualización, se debe comprobar si se ha abierto un universal link:
1. Si se ha abierto un universal link, debe ir al criterio 2, luego al criterio 1 de la Historia 1 de la funcionalidad Login y, una vez logado el usuario, debe ejecutar la acción implicada.
1. Si no se ha abierto un universal link, debe ir al criterio 2.
1. Si el dispositivo es inseguro, debe ir al criterio 2, mostrando el diálogo del criterio 3 por encima.
1. Si el dispositivo no tiene conexión a internet, va al criterio 2, mostrando el diálogo del criterio 10 por encima.
#### Detección de dispositivo inseguro

Para detectar si un dispositivo es inseguro, seguimos lo indicado en la página .

#### Forzado

En la app híbrida, el forzado se obtiene de un servicio, pero nosotros lo implementaremos utilizando Firebase Remote Config.

El JSON de Remote Config debe tener la siguiente estructura base:

[{

"name": "Config_Min_Android",

"minBuildNumber": "0",

"maxBuildNumber": "0",

"repeatDialog": "always",

"updateDialog": {

"okButtonAction": "update",

"okButtonLabel": "Actualizar",

"koButtonAction": "exit",

"koButtonLabel": "Salir",

"title": "¡Actualiza tu app Pruebas Seguros!",

"body": "Para poder disfrutar de todas las ventajas de Pruebas Seguros, actualiza la app."

}

}]

##### Datos de la configuración

1. minBuildNumber: Número mínimo de build desde el cual debe activarse el diálogo de forzado.
1. maxBuildNumber: Número máximo de build hasta el cual debe activarse el diálogo de forzado.
1. repeatDialog: puede tomar los valores:
1. always: El diálogo debe mostrarse siempre que las condiciones previas se den.
1. oneTime: El diálogo solo debe mostrarse una única vez. Se debe guardar en las preferencias de la app si ya se ha visibilizado este diálogo para la versión actual (build actual) para no visibilizarlo más hasta que no se ejecute otra versión distinta de la app.
1. updateDialog > title: Título del diálogo.
1. updateDialog > body: Descripción del diálogo.
1. updateDialog > okButtonLabel: Texto del botón de acción.
1. updateDialog > okButtonAction: Acción del botón de acción. Puede tomar los valores:
1. exit: Se cierra la app.
1. cancel: Se cierra el diálogo.
1. update: Lleva a la Play Store (para Android) o a la Apple Store (para iOS). Si se vuelve a la app después de haberse pulsado en este acceso, debe mantenerse visible el diálogo.
1. updateDialog > okButtonUrl: URL a abrir cuando se pulsa en el botón de acción y la acción es update.
1. updateDialog > koButtonLabel: Texto del botón de error.
1. updateDialog > koButtonAction: Acción del botón de error. Puede tomar los mismos valores que para el botón de acción.
##### Consideraciones

1. Al pulsar en cualquier zona externa al diálogo, no debe cerrarse el diálogo.
1. Los estilos están pendientes de cerrarse.
