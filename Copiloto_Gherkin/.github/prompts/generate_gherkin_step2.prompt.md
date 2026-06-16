---
agent: "Generador de escenarios Gherkin"
description: "Analizar documentación y generar casos de uso BDD"
---

### Paso 2: Integración de Herramientas Externas (Opcional)

**Validación de Servicio MCP:**
Primero, verifica si el servicio MCP (Model Context Protocol) está activo y configurado para integraciones externas.

Si MCP está disponible y configurado, recopila contexto adicional del proyecto desde herramientas externas usando las variables:

- **${input:project_reference}**: Identificador único del proyecto
- **${input:mcp_service}**: Servicio MCP específico a usar

**Lógica de Auto-Detección:**
Basado en el `${input:project_reference}` proporcionado y usando el `${input:mcp_service}` especificado, detecta automáticamente el tipo y realiza consultas apropiadas:

1. **Detección de Patrón Azure DevOps:**
   - Formato: `https://dev.azure.com/{organization}/{project}` o `{organization}/{project}`
   - Auto-consulta: Elementos de trabajo, repositorios, tableros y documentación

2. **Detección de Patrón Jira/Confluence:**
   - Formato: `https://{domain}.atlassian.net/browse/{project-key}` o `{project-key}`
   - Auto-consulta: Issues, épicas, historias y páginas de Confluence

3. **Detección de Patrón SharePoint:**
   - Formato: `https://{tenant}.sharepoint.com/sites/{site}` o URL directa
   - Auto-consulta: Bibliotecas de documentos y listas

4. **Detección de Patrón URL Genérico:**
   - Formato: Cualquier URL válida conteniendo identificadores de proyecto/workspace
   - Auto-consulta: Endpoints disponibles y fuentes de documentación

**Recopilación Automatizada de Datos:**

- **Elementos de Trabajo e Issues**: Recuperar automáticamente historias de usuario, requisitos, tareas, épicas y tickets
- **Fuentes de Documentación**: Auto-descubrir y analizar especificaciones funcionales, documentación técnica y artículos de base de conocimiento
- **Swagger y APIs**: Extraer automáticamente detalles de endpoints, parámetros y respuestas de APIs documentadas
- **Repositorios de Código**: Auto-detectar y hacer referencias cruzadas de estructura de código y documentación
- **Metadatos del Proyecto**: Extraer detalles de organización, workspace y proyecto de la referencia

**Guías de Integración:**

- **Validar Servicio MCP**: Verificar si el servicio MCP está activo antes de intentar integraciones externas
- **Auto-Detectar Plataforma**: Analizar patrón de `${input:project_reference}` para identificar el tipo de sistema externo
- **Descubrimiento Inteligente**: Descubrir automáticamente endpoints disponibles y fuentes de datos basados en plataforma detectada
- **Consulta Adaptativa**: Realizar consultas específicas de plataforma para recopilar información relevante del proyecto
- Usar datos externos para **complementar** el análisis de documentación local
- **Validar cruzadamente** requisitos entre documentos locales y sistemas externos
- **Priorizar** casos de uso basados en prioridades de elementos de trabajo externos
- **Alinear** escenarios BDD con criterios de aceptación externos cuando estén disponibles
- Si MCP no está activo, la detección de plataforma falla, o las herramientas externas no están disponibles, proceder solo con documentación local

### **MCP Playwright (si está disponible):**
Flujo de Exploración de la aplicación: 

#### Acceso a la aplicación:

1. Navega a la URL de la aplicación web: `${input:URL}`.
2. Asegúrate de que la aplicación se cargue exitosamente.
3. Analiza la estructura HTML e identifica elementos clave.
4. Haz clic en cada enlace y botón para explorar el flujo de navegación.
5. Interactúa con formularios, desplegables, modales y otros componentes de UI para entender su comportamiento.
6. Usa las herramientas de desarrollador del navegador para inspeccionar elementos, solicitudes de red y logs de consola para obtener información más profunda sobre la funcionalidad de la aplicación.

Nota: Si encuentras algún problema al acceder a la aplicación, por favor infórmame inmediatamente.
Nota: La aplicación es antigua y puede tener algunas peculiaridades, así que sé paciente y minucioso en tu exploración.

#### Exploración de la aplicación:

1. Inicia sesión con las siguientes credenciales si es necesario:
   - Usuario: `${input:username}`
   - Contraseña: `${input:password}`
2. Familiarízate con las características principales y la estructura de navegación de la aplicación. Lee el código HTML para identificar elementos, iframes, acciones de javascript, etc.
3. La aplicación puede tener múltiples secciones o módulos; toma nota de cualquier flujo de trabajo o funcionalidad específica que destaque.
4. Toma capturas de pantalla o graba tu navegación si es necesario para referencia.
5. Toma localizadores de elementos que sean relevantes para los escenarios BDD.
6. Hazme cualquier pregunta que tengas sobre la aplicación para aclarar tu comprensión.