# Generador de Escenarios Gherkin

## Version
2.4.0

## Prefijo

gherkin-generator

## Palabras clave

gherkin, bdd, cucumber, qa-automation, testing, escenarios, feature, behavior-driven-development, historias-usuario, jira, xray

## Repositorio

https://github.com/xxxrepositories/ghb-cop-gherkin-generator.git

## Capacidades

- Analizar documentación funcional de cualquier tipo (manuales de usuario, requisitos de negocio, especificaciones funcionales, historias de usuario en CSV, etc.) y extraer casos de uso relevantes para pruebas.
- Generar archivos `.feature` en formato Cucumber BDD escritos en español, con más de 15 escenarios por característica que cubran flujos positivos, negativos, casos límite y validaciones de negocio.
- Aplicar una estrategia de etiquetado consistente con etiquetas primarias (`@smoke`, `@regression`) y etiquetas secundarias por área funcional y entorno, y, cuando aplica, una etiqueta de relación con la historia de usuario en formato `@related:<ID>`).
- Integrar datos de sistemas de gestión externos (Azure DevOps, Jira/Confluence, SharePoint) mediante MCP para enriquecer el análisis con historias de usuario, épicas y criterios de aceptación.
- Explorar aplicaciones web de forma automatizada mediante MCP Playwright para identificar flujos de navegación, formularios y comportamientos de la interfaz de usuario.
- Identificar y clasificar automáticamente el tipo de documento de entrada para adaptar la estrategia de generación de escenarios.
- Generar un archivo `README.md` comprensivo con el análisis realizado, glosario de dominio, estadísticas de cobertura y descripción de cada característica generada.
- Verificar la calidad de cada archivo `.feature` antes de entregarlo, comprobando criterios obligatorios de Cucumber: estructura Given-When-Then, independencia de escenarios, uso de lenguaje declarativo y ausencia de datos sensibles hardcodeados.
- Asignar etiquetas con identificadores de Jira (`@related:ID-1234`) cuando la documentación de entrada son historias de usuario con referencia a un sistema de gestión de proyectos.
- Maximizar la reutilización de steps entre todas las características generadas mediante parametrización de pasos (placeholders) y una revisión semántica final que unifica pasos equivalentes redactados de forma distinta entre features.
- Sincronizar, bajo demanda, los archivos `.feature` generados (y los resultados de su ejecución) con Xray Cloud / Jira Cloud mediante la skill `xray-integration`, incluyendo el vínculo automático con la Historia de Usuario a través de la etiqueta `@related:<ID>`.

## Entornos soportados

Visual Studio Code con GitHub Copilot, GitHub Copilot Workspace

## MCP Servers

| Nombre          | Tipo   | Descripcion                                                                                                                                                                     |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mcp-playwright  | local  | Exploracion automatizada de aplicaciones web: navegacion, interaccion con formularios, capturas de pantalla y analisis del DOM para enriquecer la generacion de escenarios BDD. |
| azure-devops    | remoto | Conexion a organizaciones de Azure DevOps para recuperar elementos de trabajo, historias de usuario, epicas, tableros y documentacion de proyecto.                              |
| jira-confluence | remoto | Acceso a proyectos Jira e instancias Confluence para obtener issues, historias de usuario, criterios de aceptacion y paginas de documentacion funcional.                        |
| sharepoint      | remoto | Acceso a bibliotecas de documentos y listas de SharePoint como fuente de documentacion funcional y tecnica.                                                                     |

## Dependencias

- https://github.com/xxrepositories/ghb-cop-gherkin-generator.git

## Requisitos adicionales

- Visual Studio Code 1.96 o superior con la extension GitHub Copilot instalada y activa.
- Cuenta con acceso a GitHub Copilot y permisos para usar el modelo Claude Sonnet 4.6.
- Para integraciones con MCP Playwright: Node.js 18 o superior y el servidor MCP de Playwright instalado localmente.
- Para integraciones con sistemas externos (Azure DevOps, Jira, SharePoint): credenciales de acceso validas al servicio correspondiente y el servidor MCP remoto accesible desde el entorno de trabajo.
- La documentacion de entrada debe estar disponible de forma local en el workspace o accesible a traves de uno de los servidores MCP configurados.

---

## Descripcion de ficheros

### Agente

**`.github/agents/generate_gherkin.agent.md`**

Define el agente principal del copiloto. Establece el nombre, descripcion, modelo de IA (Claude Sonnet 4.6), herramientas disponibles y el rol del agente como QA Automation Architect experto en BDD. Describe el publico objetivo (QA Engineers, Product Owners, desarrolladores BDD), el idioma de trabajo (espanol neutro), el tono de comunicacion y las restricciones tecnicas. Orquesta el flujo de trabajo completo en cinco pasos secuenciales referenciando cada prompt correspondiente.

### Prompts

**`.github/prompts/generate_gherkin_step0.prompt.md`** — Contexto y Proyecto (obligatorio)

Primer paso del flujo. Define las variables de entrada requeridas: ruta de la documentacion a analizar (`document_location`), ruta del repositorio de salida (`e2e_repo`) y variables opcionales para integraciones externas (`project_reference`, `mcp_service`, `URL`, `username`, `password`). Establece el rol del agente como Analista de Negocio especializado en BDD y referencia todos los criterios de calidad obligatorios.

**`.github/prompts/generate_gherkin_step1.prompt.md`** — Analisis Completo de Documentacion (obligatorio)

Segundo paso. Instruye al agente para leer exhaustivamente toda la documentacion funcional del directorio de entrada como fuente primaria de casos de prueba, revisar la documentacion tecnica unicamente como contexto arquitectonico y cruzar referencias entre documentos para garantizar una comprension completa. Los escenarios BDD deben derivarse exclusivamente de la documentacion funcional.

**`.github/prompts/generate_gherkin_step2.prompt.md`** — Integracion de Herramientas Externas (opcional)

Tercer paso, ejecutado unicamente si se solicita trabajar con MCP. Detalla la logica de auto-deteccion del tipo de servicio externo a partir del patron de la referencia de proyecto, los flujos de consulta especificos para Azure DevOps, Jira/Confluence, SharePoint y URLs genericas, y el flujo completo de exploracion automatizada de aplicaciones web mediante MCP Playwright. Si ningun servicio MCP esta disponible, el agente continua solo con documentacion local.

**`.github/prompts/generate_gherkin_step3.prompt.md`** — Identificacion de Tipo de Documento (obligatorio)

Cuarto paso. Clasifica el documento de entrada en una de las categorias predefinidas (manual de usuario, requisitos de negocio, especificacion funcional, especificacion tecnica, plan de pruebas, documentacion de proceso, manual de sistema, tutorial, historias de usuario, u otra categoria propuesta). Establece la variable `document_type` que condicionara la estrategia de generacion en el paso siguiente.

**`.github/prompts/generate_gherkin_step4.prompt.md`** — Extraccion de Casos de Uso y Generacion de Caracteristicas BDD (obligatorio)

Genera los archivos `.feature` en Cucumber/Gherkin en espanol a partir del analisis completo. Exige un minimo de 15 escenarios por archivo cubriendo flujos positivos y negativos, casos limite, validaciones de negocio e interacciones de usuario. Para historias de usuario, requiere al menos 3 escenarios por historia con los criterios de aceptacion definidos. Prohibe datos sensibles hardcodeados. Antes de redactar cada paso, exige comprobar el inventario de steps ya generados y reutilizarlos o parametrizarlos en vez de crear redacciones nuevas equivalentes. Crea el `README.md` comprensivo en la raiz del repositorio de salida y aplica todos los criterios de calidad antes de finalizar cada archivo.

**`.github/prompts/generate_gherkin_step5.prompt.md`** — Revision Semantica de Reutilizacion de Steps (obligatorio)

Sexto y ultimo paso, ejecutado tras generar y validar individualmente todas las features. Repasa todos los `.feature` de la ejecucion, detecta pasos semanticamente equivalentes redactados de forma distinta y los unifica en una unica forma parametrizada aplicada de manera consistente en todas las features afectadas. Documenta en el `INFORME_<fecha_hora>.md` los steps unificados.

### Instrucciones

**`.github/instructions/generate_gherkin_standards.instructions.md`**

Define los estandares obligatorios de Cucumber y las mejores practicas de escritura BDD. Incluye la estrategia completa de etiquetado (etiquetas primarias `@smoke` y `@regression`, etiquetas secundarias por entorno y area funcional, etiquetas de identificador Jira en formato `@related:<ID>`), la estructura de escenarios con patron Given-When-Then en espanol, los principios de escritura declarativa, las convenciones de nomenclatura y organizacion de archivos, y las reglas de reutilizacion sistematica de steps (parametrizacion con placeholders y consulta del inventario de pasos existentes antes de crear uno nuevo).

**`.github/instructions/generate_gherkin_quality_verification.instructions.md`**

Establece los criterios obligatorios de aseguramiento de calidad y la lista de verificacion de revision que debe superarse antes de entregar cada archivo `.feature`. Contempla criterios como: todos los escenarios son ejecutables, existencia de al menos un escenario `@smoke` por caracteristica, independencia de datos de prueba, uso de lenguaje declarativo, ausencia de saltos de linea innecesarios entre pasos, prohibicion de palabras clave no estandar al inicio de los pasos (solo se permiten "Dado", "Cuando", "Entonces" e "Y") y verificacion de que cada paso nuevo se contrasta contra el inventario de steps existentes antes de darse por valido.

**`.github/instructions/generate_gherkin_readme.instructions.md`**

Especifica la estructura y el contenido obligatorio del archivo `README.md` que debe generarse en la raiz del repositorio de salida. Define seis secciones obligatorias: analisis de documentacion realizado, descripcion de archivos de caracteristicas generados, etiquetas BDD utilizadas, terminologia especifica del dominio, estadisticas de cobertura (numero de features, escenarios y etiquetas) y reutilizacion de steps entre features.

### Skills

**`.github/skills/xray-integration/SKILL.md`**

Skill opcional, invocada solo cuando se pide sincronizar los `.feature` generados (o sus resultados de ejecución) con Xray Cloud / Jira Cloud. Etiqueta cada escenario con la clave del Test Issue (`@PROYECTO-n`), crea o reutiliza Test Issues, propaga nombre/etiquetas/pasos, vincula Historias de Usuario mediante la etiqueta `@related:<ID>` (la misma que genera el flujo principal) y publica los resultados de ejecución como Test Execution en Jira. No incluye copia del código ni ninguna URL fija: su primer paso, obligatorio, es preguntar por el repositorio de herramientas del que descargar `utilities/XRAY`, para poder reutilizarse sin cambios en otros copilotos y en instalaciones de clientes externas. Documentación ampliada en la carpeta `references/` de la propia skill.

### Configuracion MCP

**`.github/mcp/gherkin-generator-mcp-config.json`**

Archivo de configuracion del servidor MCP que describe de forma estructurada las capacidades, el flujo de trabajo de cinco pasos, los esquemas de las variables de entrada, las integraciones con servicios externos soportados y las especificaciones de los archivos de salida. Actua como contrato formal del servicio MCP entre el agente y los consumidores externos que deseen integrarse con este copiloto mediante el protocolo MCP.

---

## Roles

| Rol                                 | Descripcion                                                                                                                                                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QA Engineer / Automation Tester     | Principal beneficiario. Utiliza el copiloto para generar rapidamente una bateria inicial de escenarios BDD ejecutables a partir de documentacion existente, reduciendo el tiempo de creacion manual de features. |
| Product Owner / Analista de Negocio | Valida que los escenarios generados reflejan correctamente los requisitos y criterios de aceptacion definidos en las historias de usuario.                                                                       |
| Desarrollador BDD                   | Consume los archivos `.feature` generados para implementar los step definitions correspondientes en el framework de automatizacion del proyecto.                                                                 |
| QA Lead / Arquitecto de Calidad     | Supervisa la estrategia de etiquetado, la cobertura de escenarios y la adherencia a los estandares Cucumber definidos en las instrucciones.                                                                      |

## Flujo de uso

1. El usuario invoca al agente `Generador de escenarios Gherkin` en GitHub Copilot.
2. El agente solicita las variables de entrada obligatorias: ruta de la documentacion y ruta del repositorio de salida.
3. Opcionalmente, el usuario proporciona una referencia a un proyecto externo (Azure DevOps, Jira) o una URL de aplicacion para exploracion con Playwright.
4. El agente ejecuta el flujo de seis pasos: contexto, analisis, integracion opcional, clasificacion del documento, generacion de features y revision semantica final de reutilizacion de steps.
5. El resultado son uno o varios archivos `.feature` en el directorio `features/` del repositorio de salida, con steps reutilizados/parametrizados entre features, y un `README.md` comprensivo en la raiz.
6. Opcionalmente, si se solicita, el agente invoca la skill `xray-integration` para etiquetar esos `.feature` y sincronizarlos con Xray Cloud / Jira Cloud.

### Generar desde Jira/Confluence

Cuando se soliciten requisitos desde una clave Jira o una URL `/browse/CLAVE-123`, el agente ejecuta el skill `.github/skills/retrieve-atlassian-context` antes del análisis. No se solicita una ruta local en esta modalidad. La recuperación incluye campos Jira (descripción y campos de requisito textuales) y todas las páginas Confluence directamente enlazadas desde remote links o URLs de campos de requisito; no sigue enlaces dentro de las páginas.

La utilidad compartida está en `../utilities/get-documentation`. Mantén esa carpeta disponible en el workspace. Requiere Python 3.10+ y configuración local de `.env` a partir de su `.env.example`; nunca incluyas tokens en argumentos, chat, informes o capturas. `JIRA_REQUIREMENT_FIELD_IDS` permite indicar IDs de campos custom de requisito separados por comas; sin esa opción se incluyen campos textuales no identificados como metadatos y se evalúa su relevancia funcional durante el análisis.

La ejecución `--issue-context` crea un directorio único por issue con `manifest.json`, `jira.json`, `jira.md` y los JSON/Markdown de cada página. El manifest enumera solo las fuentes de esa ejecución, sus URLs, IDs, timestamps y versiones. Una descarga parcial se marca explícitamente; no se reutilizan bundles anteriores. `--issue` conserva el comportamiento anterior de descargar una sola página enlazada y no incluye los campos del ticket.

La utilidad solo resuelve páginas del mismo sitio Atlassian y los short links se consultan sin autenticación; las credenciales se envían únicamente a endpoints API del sitio configurado.

Para contradicciones entre fuentes, prevalece la edición válida más reciente. En empate o fechas ausentes/inválidas/no comparables entre Jira y Confluence, se usa Jira y se informa el fallback. Las fechas son del documento completo, no prueban cuándo cambió un requisito concreto. El informe debe citar fuentes, explicar las discrepancias y declarar cobertura faltante; si no hay requisitos funcionales utilizables, no se generan features.
