# Pruebas Seguros Web - Aplicación de demostración

Aplicación estática (HTML + JavaScript) que simula la web de Pruebas Seguros. No requiere backend ni base de datos; la sesión se guarda en `sessionStorage`.

## Arranque

```bash
npx http-server ejercicio-03-framework/app-web -p 8080
```

URL inicial: `http://localhost:8080/login.html`

## Usuarios de prueba

| Usuario | Contraseña | Rol | Pólizas visibles |
|---|---|---|---|
| `cliente1` | `Cliente#24` | cliente | P-1001, P-1002, P-1003 |
| `agente1` | `Agente#24` | agente | Todas (P-1001 a P-2002) |

El usuario debe cumplir `^[A-Za-z0-9]{1,8}$`; la contraseña solo se valida como no vacía.

## Navegación

| Página | Acceso | Descripción |
|---|---|---|
| `login.html` | Directo | Formulario de login con validaciones y botón Ver contraseña |
| `recuperar.html` | Enlace "¿Olvidaste tu contraseña?" | Página simulada de recuperación |
| `home.html` | Tras el login | Tabla "Mis pólizas" con filtro por tipo |
| `poliza.html?id=P-1001` | Botón "Ver detalle" | Ficha de la póliza |
| `siniestro.html` | Botón "Declarar siniestro" | Formulario con validaciones; solo pólizas vigentes |

Los elementos exponen `data-testid` (por ejemplo `login-usuario`, `login-submit`, `home-tabla-polizas`) y `id` en los campos del login.

## Pólizas

| Id | Tipo | Titular | Estado |
|---|---|---|---|
| P-1001 | auto | cliente1 | Vigente |
| P-1002 | hogar | cliente1 | Vigente |
| P-1003 | vida | cliente1 | Anulada |
| P-2001 | auto | cliente2 | Vigente |
| P-2002 | hogar | cliente2 | Vigente |
