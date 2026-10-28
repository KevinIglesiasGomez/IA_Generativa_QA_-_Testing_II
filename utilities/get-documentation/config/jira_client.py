import re
import urllib.parse
from atlassian_http import request_json
import config


def _get(url: str) -> dict:
    return request_json(
        url,
        (config.JIRA["user_email"], config.JIRA["api_token"]),
        config.JIRA["base_url"],
    )


def get_issue_details(issue_key: str) -> dict:
    if not config.JIRA["base_url"] or not config.JIRA["user_email"] or not config.JIRA["api_token"]:
        raise ValueError("Falta configurar el acceso a Jira en el archivo .env")
    fields = (
        "*all,-comment,-worklog,-attachment,-assignee,-reporter,-creator,-watches,-votes,"
        "-issuelinks,-subtasks,-project,-components,-fixVersions,-versions,-timetracking,-environment"
    )
    query = urllib.parse.urlencode({"fields": fields, "expand": "names,schema"})
    encoded_key = urllib.parse.quote(issue_key, safe="-_")
    return _get(f"{config.JIRA['base_url']}/rest/api/3/issue/{encoded_key}?{query}")


def get_remote_links_for_issue(issue_key: str) -> list:
    encoded_key = urllib.parse.quote(issue_key, safe="-_")
    result = _get(f"{config.JIRA['base_url']}/rest/api/2/issue/{encoded_key}/remotelink")
    if not isinstance(result, list):
        raise ValueError("Jira devolvió un formato de enlaces remotos no válido")
    return result


# Un issue no contiene páginas directamente: se resuelve vía remote links
def find_confluence_page_id_from_issue(issue_key: str) -> str:
    url = f"{config.JIRA['base_url']}/rest/api/2/issue/{issue_key}/remotelink"
    links = _get(url)

    confluence_link = next(
        (link for link in links if "/wiki/" in link.get("object", {}).get("url", "")),
        None,
    )
    if not confluence_link:
        raise ValueError(f"El issue {issue_key} no tiene ninguna página de Confluence enlazada")

    # soporta tanto /pages/<id>/... (formato nuevo) como viewpage.action?pageId=<id> (formato antiguo)
    match = re.search(r"/pages/(\d+)|[?&]pageId=(\d+)", confluence_link["object"]["url"])
    if not match:
        raise ValueError(f"No se pudo extraer el pageId de la URL: {confluence_link['object']['url']}")

    return match.group(1) or match.group(2)
