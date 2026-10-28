# language: es
@web @authentication
Característica: Inicio de sesión en Pruebas Seguros
  Como cliente de Pruebas Seguros
  Quiero iniciar sesión con mis credenciales
  Para consultar mis pólizas

  @smoke @authentication
  Escenario: Login exitoso con credenciales válidas
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente1" y la contraseña "Cliente#24"
    Y pulsa el botón Iniciar sesión
    Entonces se muestra la página de Mis pólizas
    Y el saludo muestra "Hola, Lucía Fernández"

  @regression @authentication @validaciones
  Escenario: Error al iniciar sesión con el usuario vacío
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "" y la contraseña "Cliente#24"
    Y pulsa el botón Iniciar sesión
    Entonces se muestra el error de usuario "El usuario está vacío. Introduce tus datos e inténtalo de nuevo."

  @regression @authentication @validaciones
  Escenario: Error al iniciar sesión con la contraseña vacía
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente1" y la contraseña ""
    Y pulsa el botón Iniciar sesión
    Entonces se muestra el error de contraseña "La contraseña está vacía. Introduce tus datos e inténtalo de nuevo."

  @regression @authentication @validaciones @limite
  Escenario: Error por formato de usuario superior a 8 caracteres
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente123" y la contraseña "Cliente#24"
    Y pulsa el botón Iniciar sesión
    Entonces se muestra el error de usuario "El formato del usuario es incorrecto. Revisa tus datos e inténtalo de nuevo."

  @regression @authentication
  Escenario: Error al iniciar sesión con credenciales incorrectas
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente1" y la contraseña "ClaveErronea1"
    Y pulsa el botón Iniciar sesión
    Entonces se muestra el banner de error "Usuario o contraseña incorrectos. Inténtalo de nuevo."

  @regression @authentication
  Escenario: La contraseña está ofuscada por defecto
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente1" y la contraseña "Cliente#24"
    Entonces el campo contraseña está ofuscado

  @regression @authentication
  Escenario: Mostrar la contraseña al pulsar Ver
    Dado que el usuario accede a la página de login
    Cuando introduce el usuario "cliente1" y la contraseña "Cliente#24"
    Y pulsa el botón Ver contraseña
    Entonces el campo contraseña se muestra en texto claro

  @regression @authentication
  Escenario: Cerrar sesión desde Mis pólizas
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando pulsa el botón Cerrar sesión
    Entonces se muestra la página de login

  @regression @authentication
  Escenario: Acceso directo a Mis pólizas sin sesión redirige al login
    Dado que el usuario no ha iniciado sesión
    Cuando accede directamente a la página de Mis pólizas
    Entonces se muestra la página de login

  @regression @authentication
  Escenario: Abrir la recuperación de contraseña desde el login
    Dado que el usuario accede a la página de login
    Cuando pulsa el enlace ¿Olvidaste tu contraseña?
    Entonces se muestra la página de Recuperar contraseña
