#language: es
@login
Característica: Login

  @Paralelizable
  Escenario: Login con un usuario y contraseña correctos
    Dado un usuario en la página de login
    Cuando el usuario hace login con credenciales "correctas"
    Entonces puede visualizar su foto de perfil correctamente
    Y puede navegar a la aplicación "Mis Datos"