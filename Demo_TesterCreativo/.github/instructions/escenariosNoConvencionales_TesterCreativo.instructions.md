# Instrucciones de catalogo de escenarios no convencionales para el Agente: Tester Creativo

## 1. Escenarios no convencionales por tipo de aplicacion

El agente debe considerar estos escenarios segun el tipo de aplicacion detectada. No todos aplican en todos los casos; seleccionar los relevantes segun la informacion proporcionada.

### 1.1. Aplicaciones con formularios

**Manipulacion de datos:**
- Pegar texto con formato enriquecido (HTML, RTF) en campos de texto plano
- Pegar contenido de una hoja de calculo en un campo de texto
- Usar autocompletado del navegador con datos antiguos o incorrectos
- Ingresar datos via extension de gestor de contrasenas
- Completar campos con dictado por voz
- Arrastrar texto desde otra aplicacion al campo

**Comportamiento temporal:**
- Dejar el formulario abierto durante horas y luego enviarlo
- Completar un formulario, cerrar la pestana sin enviar, y volver
- Llenar un formulario mientras la sesion de autenticacion expira
- Enviar un formulario justo cuando el servidor esta en mantenimiento
- Cambiar la hora del sistema durante un flujo con validacion temporal

**Interacciones inesperadas:**
- Llenar un campo, borrarlo completamente, y enviar
- Usar el autocomplete del navegador para rellenar todos los campos
- Presionar Enter en un campo que no es el ultimo del formulario
- Usar Tab para navegar y activar validaciones en cascada
- Hacer click en enviar sin haber interactuado con ningun campo

### 1.2. Aplicaciones con listados y tablas

**Volumenes:**
- Lista con exactamente 0 elementos
- Lista con exactamente 1 elemento
- Lista con el numero exacto del tamano de pagina (ej: exactamente 10, 25, 50)
- Lista con un elemento mas que el tamano de pagina
- Lista con miles de elementos

**Operaciones sobre datos:**
- Ordenar por una columna y luego filtrar: se mantiene el orden
- Filtrar, paginar, y luego quitar el filtro: se restaura correctamente
- Seleccionar elementos, cambiar de pagina, volver: seleccion se mantiene
- Eliminar el ultimo elemento de una pagina: paginacion se actualiza
- Editar un elemento y verificar que la fila se actualiza sin recargar

**Contenido problematico:**
- Celdas con contenido extremadamente largo (sin truncar)
- Celdas con caracteres especiales que rompen el layout
- Columnas con valores nulos o indefinidos mezclados con datos validos
- Filas con datos en formatos inconsistentes

### 1.3. Aplicaciones con autenticacion

**Sesiones:**
- Iniciar sesion en dos navegadores diferentes simultaneamente
- Cerrar sesion en un navegador y verificar el otro
- Cambiar la contrasena y verificar que las sesiones activas se invalidan
- Mantener una sesion abierta mas alla del tiempo de expiracion
- Acceder a una URL protegida directamente sin autenticacion

**Credenciales:**
- Login con mayusculas/minusculas diferentes en usuario
- Login con espacios antes o despues del usuario
- Login con contrasena copiada que incluye espacio al final
- Login con caracter de salto de linea en la contrasena
- Intentar multiples logins fallidos y verificar bloqueo

### 1.4. Aplicaciones con carga de archivos

**Archivos problematicos:**
- Archivo con extension cambiada (renombrar .exe a .jpg)
- Archivo con doble extension (foto.jpg.exe)
- Archivo de 0 bytes
- Archivo que excede el tamano permitido por 1 byte
- Archivo con nombre extremadamente largo
- Archivo con caracteres especiales en el nombre (espacios, acentos, simbolos)
- Archivo con nombre duplicado al de uno ya cargado

**Proceso de carga:**
- Cancelar la carga a mitad de proceso
- Perder conexion durante la carga
- Subir el mismo archivo dos veces seguidas
- Arrastrar multiples archivos cuando solo se permite uno
- Pegar desde el portapapeles (Ctrl+V) en zona de carga

### 1.5. Aplicaciones con busqueda

**Consultas no convencionales:**
- Buscar con un solo caracter
- Buscar con espacios solamente
- Buscar con operadores especiales (AND, OR, NOT, *, ?)
- Buscar con expresiones regulares literales
- Buscar con emojis
- Buscar texto que existe en metadatos pero no en contenido visible
- Buscar con acentos vs sin acentos (cafe vs cafe)

**Comportamiento:**
- Escribir y borrar rapidamente (debounce)
- Buscar, obtener resultados, y buscar de nuevo sin limpiar
- Buscar desde URL con parametro de query directamente
- Buscar en un idioma diferente al contenido

---

## 2. Escenarios de interaccion entre funcionalidades

### 2.1. Efectos cruzados
- Crear un recurso desde la pagina A, verificar que aparece en la pagina B
- Eliminar un recurso referenciado por otro recurso
- Modificar un dato compartido entre varias vistas
- Cambiar permisos de un usuario mientras tiene sesion activa
- Modificar la configuracion de idioma y verificar que afecta a todas las paginas

### 2.2. Secuencias de acciones
- Realizar la misma accion 10 veces seguidas (crear, eliminar, crear, eliminar...)
- Ejecutar acciones en un orden inverso al esperado
- Preocuparse del "camino de vuelta": despues de completar un flujo, el estado queda limpio
- Verificar que despues de un error, el sistema permite volver a intentar

---

## 3. Escenarios de entorno y contexto

### 3.1. Condiciones del entorno
- Zona horaria diferente a la del servidor
- Idioma del navegador diferente al de la aplicacion
- Modo oscuro del sistema operativo
- Alto contraste del sistema operativo
- Tamano de fuente grande configurado en el navegador
- Bloqueador de anuncios activo
- VPN activa (posible latencia adicional)

### 3.2. Dispositivos y configuraciones
- Pantalla de alta densidad (Retina, 4K)
- Pantalla de baja resolucion
- Dispositivo tactil (sin hover)
- Dispositivo con solo teclado (sin raton)
- Navegador antiguo (funcionalidad degradada)
- Modo incognito/privado del navegador

---
