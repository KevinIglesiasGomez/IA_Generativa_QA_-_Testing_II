# Generación de INFORME_<fecha_hora>.md

Es obligatorio generar un archivo INFORME_<fecha_hora>.md comprensivo en la raíz de **e2e_repo/** siguiendo TODOS los requisitos de documentación en las instrucciones para cada conjunto de características BDD generadas. El nombre del fichero debe incluir la fecha y hora de creación en formato `YYYY-MM-DD_HH-mm-ss` (ejemplo: `INFORME_2026-10-02_14-30-55.md`). Este INFORME_<fecha_hora>.md debe incluir obligatoriamente las siguientes secciones detalladas utilizando el mínimo de tokens posible, pero sin omitir información relevante:

---

### Documentación Requerida en INFORME_<fecha_hora>.md

**Secciones Obligatorias:**
1. **Análisis de Documentación Realizado**
   - Documentos analizados
   - Tipo de documento identificado
   - Metodología de análisis

2. **Descripción de Archivos de Características**
   - Lista de características generadas
   - Propósito de cada característica
   - Escenarios clave incluidos

3. **Etiquetas BDD Utilizadas**
   - Explicación de la estrategia de etiquetado
   - Definición de cada etiqueta utilizada
   - Criterios para asignación de etiquetas

4. **Terminología Específica del Dominio**
   - Glosario de términos de negocio
   - Mapeo a funcionalidades del sistema
   - Contexto de uso

5. **Estructura de Archivos y Estadísticas**
   - Número total de archivos .feature
   - Número total de escenarios
   - Número total de etiquetas usadas
   - Cobertura y distribución por funcionalidades del sistema

6. **Reutilización de Steps**
   - Listado de steps parametrizados reutilizados entre varias features
   - Features que comparten cada step reutilizado
   - Steps unificados durante la revisión semántica final (Step 5)

### Fuentes Jira/Confluence y discrepancias

Cuando la fuente sea Jira/Confluence, añade además:

- Inventario de fuentes: clave/ID, título, URL, fecha de edición original y normalizada, versión Confluence cuando aplique, fecha de descarga y estado de completitud.
- Tabla de discrepancias con requisito, afirmaciones en conflicto, citas de fuente, fechas, interpretación seleccionada y motivo (más reciente o fallback Jira). Indica los escenarios afectados y la cobertura omitida.
- Errores, enlaces no resueltos y páginas no descargadas. En resultados parciales, limita los escenarios a requisitos respaldados por contenido legible y declara la cobertura faltante.
- Si no queda contenido funcional utilizable, no generes features: informa el bloqueo de recuperación o requisitos.
- Aclara que la fecha es de documento completo y no prueba cuándo cambió una afirmación específica.

---