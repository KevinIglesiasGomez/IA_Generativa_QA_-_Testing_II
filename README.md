# Ejercicios prácticos del curso

Cada carpeta contiene los datos de entrada para ejecutar un asset de forma práctica, con un README que indica cómo lanzarlo y cómo evaluarlo. Todos comparten el mismo dominio: Pruebas Seguros, plataforma de seguros con clientes, pólizas y siniestros.

| Ejercicio | Asset | Entrada |
|---|---|---|
| [ejercicio-01-gherkin](ejercicio-01-gherkin/README.md) | `Asset_Gherkin` | Documentación funcional en Markdown |
| [ejercicio-02-casos-duplicados](ejercicio-02-casos-duplicados/README.md) | `Asset_CasosDuplicadosDetector` | Dos CSV (Jira y Gherkin) con duplicados conocidos |
| [ejercicio-03-framework](ejercicio-03-framework/README.md) | `Asset_Framework` | Aplicación web estática y feature de login |
| [ejercicio-04-automatizacion-playwright](ejercicio-04-automatizacion-playwright/README.md) | `Asset_AutomatizacionPlaywright` | Features de pólizas y siniestros sobre el framework del ejercicio 03 |
| [ejercicio-05-ingenieria-inversa](ejercicio-05-ingenieria-inversa/README.md) | `Asset_IngenieriaInversa` | Código fuente Ionic + Angular |
| [ejercicio-06-mapeo-ui](ejercicio-06-mapeo-ui/README.md) | `Asset_MapeoUI` | App React con selectores de calidad desigual |
| [ejercicio-07-datos-sinteticos](ejercicio-07-datos-sinteticos/README.md) | `Asset_SyntheticData` | Requisitos de datos y esquema de cliente |
| [ejercicio-08-tester-creativo](ejercicio-08-tester-creativo/README.md) | `Asset_TesterCreativo` | Especificación, HTML y código con defectos sembrados |
| [ejercicio-09-analisis-api](ejercicio-09-analisis-api/README.md) | `Asset_AnalisisPruebasAPI` | API de demostración, colección Postman y proyecto Karate |

## Orden recomendado

1. Ejercicio 01, 02 y 07: generación y gestión de casos y datos.
2. Ejercicio 05 y 06: análisis del código y la interfaz.
3. Ejercicio 03 y 04: framework y automatización (el 04 depende del 03).
4. Ejercicio 08 y 09: pruebas creativas y análisis de la calidad de las pruebas API.

## Notas

- Los ficheros `solucion_esperada.md` son para el instructor; no deben abrirse antes de ejecutar el asset.
- Los usuarios y contraseñas son ficticios y solo válidos para estas aplicaciones de demostración: `cliente1` / `Cliente#24` y `agente1` / `Agente#24`.
- El ejercicio 02 no tiene aplicación; el 03, 04 y 09 requieren arrancar un servidor local (ver su README).
