import urllib.parse
from atlassian_http import AtlassianRequestError, request_json
import config


def _get(url: str) -> dict:
    return request_json(
        url,
        (config.CONFLUENCE["user_email"], config.CONFLUENCE["api_token"]),
        config.CONFLUENCE["base_url"],
    )


# Identificador primario: no cambia aunque se renombre o mueva la página
def fetch_page_by_id(page_id: str) -> dict:
    url = f"{config.CONFLUENCE['base_url']}/api/v2/pages/{page_id}?body-format=storage&include-version=true"
    try:
        return _get(url)
    except RuntimeError as err:
        if "404" not in str(err):
            raise
        tipo = _detectar_tipo_contenido(page_id)
        if tipo and tipo != "page":
            raise RuntimeError(
                f"El ID {page_id} corresponde a un contenido de tipo '{tipo}', no a una pagina "
                f"(ej. blogpost, attachment, folder o whiteboard). Esta herramienta solo descarga paginas."
            ) from err
        raise


# La API v2 solo admite tipo "page"; se usa v1 para diagnosticar otros tipos de contenido (blogpost, attachment...)
def _detectar_tipo_contenido(content_id: str) -> str | None:
    url = f"{config.CONFLUENCE['base_url']}/rest/api/content/{content_id}"
    try:
        return _get(url).get("type")
    except RuntimeError:
        return None


# La API v2 no admite filtrar por título+espacio, se usa CQL vía v1
def search_page_by_title_and_space(title: str, space_key: str) -> str:
    cql = f'title="{title}" and space="{space_key}"'
    query = urllib.parse.urlencode({"cql": cql})
    url = f"{config.CONFLUENCE['base_url']}/rest/api/content/search?{query}"
    results = _get(url).get("results", [])
    if not results:
        raise ValueError(f'No se encontró página "{title}" en el espacio "{space_key}"')
    return results[0]["id"]


# Busqueda libre por texto (CQL "text ~"), opcionalmente acotada a un espacio
# Se usa /rest/api/search (no /content/search) porque es el unico que devuelve totalSize
def search_pages(text: str, space_key: str | None = None, limit: int = 10) -> dict:
    cql = f'text ~ "{text}" and type = page'
    if space_key:
        cql += f' and space = "{space_key}"'
    params = urllib.parse.urlencode({"cql": cql, "limit": limit})
    url = f"{config.CONFLUENCE['base_url']}/rest/api/search?{params}"
    data = _get(url)
    base = data.get("_links", {}).get("base", config.CONFLUENCE["base_url"])
    resultados = [
        {
            "id": item["content"]["id"],
            "title": item.get("title", ""),
            "url": base + item.get("url", ""),
        }
        for item in data.get("results", [])
    ]
    return {
        "results": resultados,
        "total": data.get("totalSize", len(resultados)),
    }
