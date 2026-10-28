# Descarga de documentación de Confluence

Herramienta en Python puro (sin dependencias externas) para buscar y descargar el
contenido de páginas de Confluence Cloud, identificándolas de varias formas distintas,
y exportarlo en varios formatos.

## Uso

Un único ejecutable, `download.py`, admite varios modos (excluyentes entre sí):

```bash
python download.py --id 123456                          # por ID de pagina (recomendado)
python download.py --title "Nombre de la pagina" ESPACIO # por titulo + clave de espacio
python download.py --issue PROJ-123                      # por issue de Jira enlazado
python download.py --issue-context PROJ-123              # issue Jira y páginas Confluence directamente enlazadas
python download.py --search "texto"                      # busca paginas por texto libre
python download.py --batch ejemplo.json                  # descarga varios items de una vez
```

Por defecto el contenido se guarda como JSON. Para elegir otro formato se usa `--format`:

```bash
python download.py --id 123456 --format md     # Markdown (tablas, listas, negrita/cursiva)
python download.py --id 123456 --format html   # HTML "storage" tal cual lo devuelve Confluence
python download.py --id 123456 --format txt    # texto plano sin etiquetas
python download.py --id 123456 --format json   # respuesta cruda de la API (por defecto)
```

El archivo se guarda en `output/<pageId>.<formato>`.

### Contexto completo de un issue Jira

`--issue-context` es independiente del modo histórico `--issue`: recupera el issue y sus campos de requisito, además de todas las páginas Confluence enlazadas directamente desde remote links o URLs de descripción/campos custom textuales.

```bash
python download.py --issue-context PROJ-123
python download.py --issue-context https://tuempresa.atlassian.net/browse/PROJ-123
```

El modo siempre genera `manifest.json`, `jira.json`, `jira.md` y, por cada página, `confluence-<id>.json` y `.md` bajo `output/<ISSUE>/<run-id>/`. Imprime la ruta absoluta del manifest. El manifest enumera fuentes, timestamps de edición, versiones, errores y enlaces omitidos. Cada ejecución usa un directorio exclusivo; analiza únicamente los archivos listados en su manifest. Si hay un error de página/enlaces, el bundle se guarda como parcial y el estado se determina por el manifest, no por el código de salida. Fallos de configuración, issue o persistencia son fatales. `--issue-context` admite formato predeterminado/JSON; no admite `--format html`, `md` o `txt`.

Se descargan páginas Confluence directas, sin rastrear sus enlaces. Las URLs deben ser del sitio Atlassian HTTPS configurado; enlaces de otro sitio o no compatibles se reportan. Los short links se resuelven sin autenticación y con redirecciones acotadas al mismo origen; las credenciales solo se envían a endpoints API fijos del sitio configurado. Los errores no incluyen cuerpos de respuesta ni credenciales.

### ¿Cuándo usar cada modo de identificación?

- **`--id`**: la forma más fiable, el ID no cambia aunque la página se renombre o mueva.
- **`--title`**: cuando no se conoce el ID pero sí el título exacto y el espacio.
- **`--issue`**: cuando se parte de un ticket de Jira que tiene una página de Confluence
  enlazada como remote link. Requiere que el enlace exista; si el issue no tiene ninguna
  página enlazada, falla con un error explícito.
- **`--search`**: cuando no se conoce ni el ID ni el título exacto. Lista candidatos
  (`id`, `título`, `url`) sin descargarlos; el ID obtenido se usa después con `--id`.
- **`--batch`**: cuando hay que descargar varios items (mezclando los tres modos
  anteriores) en una sola ejecución.

### Búsqueda por texto libre (`--search`)

```bash
python download.py --search "texto"                   # busca en todo el sitio
python download.py --search "texto" --space ESPACIO   # acota a un espacio
python download.py --search "texto" --limit 20         # cambia el numero de resultados (por defecto 10)
```

No descarga nada: imprime una lista `id`, `título`, `url` por cada página candidata usando
búsqueda CQL (`text ~ "..."`), y al final indica cuántos resultados se muestran sobre el
total real (`totalSize` de la API), avisando si hay más disponibles que el `--limit` usado.

### Descarga por lotes (`--batch`)

```bash
python download.py --batch ejemplo.json
python download.py --batch ejemplo.json --format md   # formato por defecto si el item no indica el suyo
```

El fichero JSON es una lista de items; cada uno usa uno de los tres identificadores
(`id`, `issue`, o `title`+`space`) y opcionalmente su propio `format`:

```json
[
  { "id": "2710765570" },
  { "id": "2526511146", "format": "md" },
  { "issue": "OTT-766" },
  { "title": "Nombre de la pagina", "space": "ESPACIO" }
]
```

Ver [ejemplo.json](ejemplo.json). Cada item se procesa de forma independiente: si uno
falla, se registra el error y continúa con el resto, mostrando al final un resumen de
cuántos items salieron bien y cuáles fallaron.

## Configuración

Copia `.env.example` a `.env` y rellena las credenciales:

```
ATLASSIAN_USER_EMAIL=tu-email@empresa.com
ATLASSIAN_API_TOKEN=xxxxx

# Subdominio de tu sitio Atlassian: si tu URL es https://tuempresa.atlassian.net, pon "tuempresa"
ATLASSIAN_SITE=tuempresa

OUTPUT_DIR=./output

# Opcional: IDs de campos custom Jira que contienen requisitos, separados por coma.
JIRA_REQUIREMENT_FIELD_IDS=customfield_10001,customfield_10002
```

El token se genera en [id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
Confluence y Jira Cloud comparten el mismo sistema de tokens por cuenta y el mismo
subdominio (`ATLASSIAN_SITE`); las URL completas (`https://<site>.atlassian.net` para
Jira, `https://<site>.atlassian.net/wiki` para Confluence) se construyen automáticamente.

El `.env` nunca debe subirse al repositorio (ya está excluido en `.gitignore`).

## Requisitos

- Python 3.10 o superior instalado y disponible en el PATH (`python3`).
- No requiere instalar ningún paquete: usa solo librería estándar (`urllib`, `json`,
  `base64`, `re`, `html.parser`).

## Estructura

```
download.py                 # unico ejecutable: parsea argumentos y despacha al modo elegido
example_batch.json          # ejemplo de fichero de entrada para --batch
.env / .env.example         # credenciales (el .env real nunca se versiona)
config/
  config.py                 # carga de .env y construccion de URLs (ATLASSIAN_SITE)
  confluence_client.py      # llamadas HTTP a la API de Confluence (id / titulo+espacio / busqueda)
  jira_client.py             # resuelve el pageId a partir de un issue de Jira
  atlassian_http.py          # HTTPS mismo origen, timeout y reintentos acotados
  get_issue_context.py      # bundle versionado de Jira y Confluence directo
  formatters.py              # conversion del storage format de Confluence a md/txt
  get_by_id.py               # modo --id (y guardado comun al resto de modos)
  get_by_title_and_space.py  # modo --title
  get_by_jira_issue.py       # modo --issue
  search.py                  # modo --search (busqueda por texto libre, no descarga)
  batch.py                   # modo --batch (procesa una lista de items desde un JSON)
output/                      # resultado de las descargas (se crea al vuelo)
```

(La carpeta raíz se puede renombrar libremente: todas las rutas se calculan de forma
relativa a `download.py`.)

Los scripts dentro de `config/` contienen toda la lógica y son reutilizados directamente
por `download.py` (no hay lógica duplicada entre modos).
