# language: es
@web @siniestros
Característica: Declaración de siniestros en Pruebas Seguros
  Como cliente de Pruebas Seguros
  Quiero declarar un siniestro sobre una póliza vigente
  Para iniciar su tramitación

  @smoke @siniestros
  Escenario: Declarar un siniestro con datos válidos
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y accede a la declaración de siniestros
    Cuando declara un siniestro de tipo "Colisión" sobre la póliza "P-1001" con fecha de hace 2 días y la descripción "Colisión trasera en un semáforo con daños en el paragolpes"
    Entonces se muestra la confirmación con una referencia de siniestro

  @regression @siniestros
  Escenario: Solo se ofrecen pólizas vigentes
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando accede a la declaración de siniestros
    Entonces el desplegable de pólizas ofrece "P-1001" y "P-1002"
    Y el desplegable de pólizas no ofrece "P-1003"

  @regression @siniestros @validaciones
  Esquema del escenario: Validación de campos obligatorios
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y accede a la declaración de siniestros
    Cuando envía la declaración sin informar "<campo>"
    Entonces se muestra el error "<mensaje>"

    Ejemplos:
      | campo       | mensaje                                              |
      | póliza      | Selecciona una póliza.                               |
      | tipo        | Selecciona el tipo de siniestro.                     |
      | fecha       | Indica la fecha del siniestro.                       |
      | descripción | La descripción debe tener entre 20 y 500 caracteres. |

  @regression @siniestros @validaciones @limite
  Esquema del escenario: Límites de longitud de la descripción
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y accede a la declaración de siniestros
    Cuando declara un siniestro con una descripción de <longitud> caracteres
    Entonces el resultado de la declaración es "<resultado>"

    Ejemplos:
      | longitud | resultado |
      | 19       | error     |
      | 20       | correcto  |
      | 500      | correcto  |
      | 501      | error     |

  @regression @siniestros @validaciones
  Escenario: No se permite una fecha futura
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y accede a la declaración de siniestros
    Cuando declara un siniestro con fecha de dentro de 3 días
    Entonces se muestra el error "La fecha del siniestro no puede ser futura."

  @regression @siniestros
  Escenario: Cancelar la declaración vuelve a Mis pólizas
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y accede a la declaración de siniestros
    Cuando pulsa el botón Cancelar
    Entonces se muestra la página de Mis pólizas
