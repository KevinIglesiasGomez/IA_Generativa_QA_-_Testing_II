# language: es
@web @polizas
Característica: Consulta de pólizas en Pruebas Seguros
  Como cliente o agente de Pruebas Seguros
  Quiero consultar mis pólizas
  Para conocer su estado y su detalle

  @smoke @polizas
  Escenario: El cliente ve únicamente sus pólizas
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Entonces la tabla contiene 3 pólizas
    Y se muestra la póliza "P-1001"
    Y no se muestra la póliza "P-2001"

  @regression @polizas
  Escenario: El agente ve todas las pólizas
    Dado que el usuario "agente1" ha iniciado sesión con la contraseña "Agente#24"
    Entonces la tabla contiene 5 pólizas

  @regression @polizas
  Escenario: Filtrar pólizas por tipo
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando filtra las pólizas por el tipo "Hogar"
    Entonces la tabla contiene 1 pólizas
    Y se muestra la póliza "P-1002"

  @regression @polizas
  Escenario: Una póliza anulada se muestra con su estado
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando filtra las pólizas por el tipo "Vida"
    Entonces se muestra la póliza "P-1003"
    Y la póliza "P-1003" tiene el estado "Anulada"

  @regression @polizas
  Esquema del escenario: Consultar el detalle de una póliza
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando abre el detalle de la póliza "<poliza>"
    Entonces el detalle muestra el tipo "<tipo>"
    Y el detalle muestra el estado "<estado>"
    Y el detalle muestra la prima "<prima>"

    Ejemplos:
      | poliza | tipo  | estado  | prima    |
      | P-1001 | auto  | Vigente | 412,50 € |
      | P-1002 | hogar | Vigente | 238,00 € |
      | P-1003 | vida  | Anulada | 120,00 € |

  @regression @polizas @seguridad
  Escenario: El cliente no accede al detalle de una póliza ajena
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Cuando accede directamente al detalle de la póliza "P-2001"
    Entonces se muestra el mensaje "La póliza solicitada no existe o no tienes acceso."

  @regression @polizas
  Escenario: Volver a Mis pólizas desde el detalle
    Dado que el usuario "cliente1" ha iniciado sesión con la contraseña "Cliente#24"
    Y abre el detalle de la póliza "P-1001"
    Cuando pulsa el botón Volver a Mis pólizas
    Entonces se muestra la página de Mis pólizas
