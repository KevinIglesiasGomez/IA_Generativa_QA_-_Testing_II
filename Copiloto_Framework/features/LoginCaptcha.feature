# language: es
@loginCaptcha
Característica: Login con captcha

  Escenario: [Login Captcha] [Intenta hacer login sin captcha y falla]
    Dado un usuario en la página de login
    Cuando el usuario de rol "Producción" hace login sin completar el captcha
    Entonces comprueba que no puede hacer login

  Escenario: [Login Captcha] [Intenta hacer login con un código incorrecto]
    Dado un usuario en la página de login
    Cuando el usuario de rol "Producción" hace login con un código incorrecto
    Entonces comprueba que no puede hacer login

  Escenario: [Login Captcha] [Usuario solicita cambio de contraseña y recibe un mail]
    Dado un usuario que intenta recuperar la contraseña del rol "Producción"
    Entonces abre el correo para ver si los correos correspondientes al proceso "Recuperar contraseña" son enviados

  Escenario: [Login Captcha] [Usuario recupera la contraseña]
    Dado un usuario que intenta recuperar la contraseña del rol "Producción"
    Y accede mediante el link con href "password" del correo de asunto "Cambio de contraseña corporativa" - Borrar correo: "Si"
    Y cambia la contraseña por una nueva
    Entonces el usuario comprueba que puede loguearse con la nueva contraseña
