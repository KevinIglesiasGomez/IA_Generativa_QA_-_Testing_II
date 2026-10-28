# Solución esperada - Ejercicio 02

Uso exclusivo del instructor. Resultado de referencia del análisis semántico.

## Duplicados reales (10)

| Gherkin | Jira | Motivo |
|---|---|---|
| G-001 | PSEG-101 | Login válido hasta la home |
| G-002 | PSEG-102 | Usuario vacío con mensaje de error |
| G-003 | PSEG-103 | Contraseña vacía |
| G-004 | PSEG-104 | Usuario precargado tras login previo |
| G-005 | PSEG-107 | Aceptar en diálogo inseguro cierra la app |
| G-006 | PSEG-108 | Diálogo sin conexión al arrancar |
| G-010 | PSEG-111 | Tasación con matrícula válida |
| G-011 | PSEG-112 | Tasación con matrícula inválida |
| G-014 | PSEG-113 | Cierre de sesión desde menú |
| G-015 | PSEG-105 | Enlace de recuperación de contraseña |

## Falsos positivos (se deben conservar, 5)

| Gherkin | Caso Jira parecido | Por qué NO es duplicado |
|---|---|---|
| G-007 | PSEG-102 | Valida formato (9 caracteres), no el campo vacío |
| G-008 | PSEG-108 | Cubre la acción Reintentar, no la visualización del diálogo |
| G-009 | PSEG-115 | Token caducado, el caso Jira cubre token vigente |
| G-012 | PSEG-109 | Revelar la contraseña, el caso Jira cubre el estado por defecto |
| G-013 | PSEG-101 | Bloqueo de pantalla durante la carga, no el acceso a la home |

## Casos Jira sin equivalente en Gherkin

PSEG-106, PSEG-109, PSEG-110, PSEG-114 y PSEG-115. No generan duplicado.

## CSV limpio esperado

5 filas: G-007, G-008, G-009, G-012 y G-013.
