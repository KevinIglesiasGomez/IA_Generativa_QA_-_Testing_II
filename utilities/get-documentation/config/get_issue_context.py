from datetime import datetime, timezone
import json
from pathlib import Path
import re
import urllib.parse
import uuid

import config
import confluence_client
import jira_client
from atlassian_http import AtlassianRequestError, request_bytes
from formatters import extract_urls, jira_to_markdown, to_markdown


_ISSUE_KEY = re.compile(r"^[A-Za-z][A-Za-z0-9_]*-\d+$")
_BROWSE_KEY = re.compile(r"/browse/([A-Za-z][A-Za-z0-9_]*-\d+)(?:/|$)", re.IGNORECASE)
_PAGE_ID = re.compile(r"/pages/(\d+)(?:/|$)")
_NON_REQUIREMENT_FIELD = re.compile(
    r"story\s*points?|sprint|rank|epic\s*link|estimate|remaining\s*time|time\s*tracking|"
    r"reporter|assignee|creator|watcher|votes|security\s*level|resolution|status\s*category",
    re.IGNORECASE,
)


def _same_origin(left: str, right: str) -> bool:
    try:
        left_url = urllib.parse.urlsplit(left)
        right_url = urllib.parse.urlsplit(right)
        left_port = left_url.port or 443
        right_port = right_url.port or 443
    except ValueError:
        return False
    return (
        left_url.scheme.lower() == right_url.scheme.lower() == "https"
        and (left_url.hostname or "").lower() == (right_url.hostname or "").lower()
        and left_port == right_port
    )


def _configured() -> None:
    values = (
        config.JIRA.get("base_url"),
        config.JIRA.get("user_email"),
        config.JIRA.get("api_token"),
        config.CONFLUENCE.get("base_url"),
    )
    if not all(values):
        raise ValueError("Falta configurar ATLASSIAN_SITE, ATLASSIAN_USER_EMAIL y ATLASSIAN_API_TOKEN en .env")
    jira_origin = urllib.parse.urlsplit(config.JIRA["base_url"])
    confluence_origin = urllib.parse.urlsplit(config.CONFLUENCE["base_url"])
    if (
        jira_origin.scheme != "https"
        or confluence_origin.scheme != "https"
        or jira_origin.hostname.lower() != confluence_origin.hostname.lower()
    ):
        raise ValueError("La configuración Atlassian debe usar el mismo sitio HTTPS para Jira y Confluence")


def _issue_key(reference: str) -> str:
    value = reference.strip()
    if value.lower().startswith(("https://", "http://")):
        parsed = urllib.parse.urlsplit(value)
        if parsed.username or parsed.password or not _same_origin(value, config.JIRA["base_url"]):
            raise ValueError("La URL del issue debe pertenecer al sitio Atlassian configurado y usar HTTPS")
        match = _BROWSE_KEY.search(parsed.path)
        if not match:
            raise ValueError("La URL no contiene una ruta Jira /browse/ISSUE-123 válida")
        value = match.group(1)
    if not _ISSUE_KEY.fullmatch(value):
        raise ValueError("Clave Jira no válida; usa un formato como PROJ-123")
    return value.upper()


def _normalized_timestamp(value) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        timestamp = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if timestamp.tzinfo is None:
        return None
    return timestamp.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _nonempty(value) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def _custom_requirement_fields(fields: dict, names: dict, schema: dict) -> dict:
    selected = {}
    overrides = set(config.JIRA_REQUIREMENT_FIELD_IDS)
    for field_id, value in fields.items():
        if not field_id.startswith("customfield_") or not _nonempty(value):
            continue
        if overrides:
            if field_id in overrides:
                selected[field_id] = value
            continue
        field_name = names.get(field_id, "")
        if _NON_REQUIREMENT_FIELD.search(field_name):
            continue
        field_schema = schema.get(field_id, {})
        if not isinstance(field_schema, dict):
            field_schema = {}
        schema_type = str(field_schema.get("type", "")).lower()
        custom_type = str(field_schema.get("custom", "")).lower()
        is_adf = isinstance(value, dict) and value.get("type") == "doc"
        is_text = isinstance(value, str) and (schema_type in ("string", "text") or "textarea" in custom_type)
        if is_adf or is_text:
            selected[field_id] = value
    return selected


def _safe_url(url: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(url)
        port = parsed.port
    except ValueError:
        return "[URL no compatible]"
    if not parsed.scheme or not parsed.hostname:
        return "[URL no compatible]"
    host = parsed.hostname
    if port:
        host = f"{host}:{port}"
    return urllib.parse.urlunsplit((parsed.scheme, host, parsed.path, "", ""))


def _direct_page_id(url: str, allowed_origin: str) -> str | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.username or parsed.password or not _same_origin(url, allowed_origin):
        return None
    if not parsed.path.startswith("/wiki/"):
        return None
    query_id = urllib.parse.parse_qs(parsed.query).get("pageId", [None])[0]
    if query_id and query_id.isdigit():
        return query_id
    match = _PAGE_ID.search(parsed.path)
    return match.group(1) if match else None


def _resolve_page_id(url: str) -> str:
    base_url = config.CONFLUENCE["base_url"]
    parsed = urllib.parse.urlsplit(url)
    if parsed.username or parsed.password or not _same_origin(url, config.JIRA["base_url"]):
        raise ValueError("Enlace Atlassian de otro sitio o con esquema no compatible")
    if not parsed.path.startswith("/wiki/"):
        raise ValueError("Enlace Atlassian no compatible con una página Confluence")
    page_id = _direct_page_id(url, base_url)
    if page_id:
        return page_id
    _, final_url = request_bytes(url, None, config.JIRA["base_url"])
    page_id = _direct_page_id(final_url, base_url)
    if not page_id:
        raise ValueError("El enlace corto no redirigió a una página Confluence con ID reconocible")
    return page_id


def _new_run_directory(issue_key: str, output_dir: str | None = None) -> Path:
    root = Path(output_dir or config.OUTPUT_DIR).expanduser().resolve() / issue_key
    root.mkdir(parents=True, exist_ok=True)
    for _ in range(5):
        run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + "-" + uuid.uuid4().hex[:8]
        run_dir = root / run_id
        try:
            run_dir.mkdir()
            return run_dir
        except FileExistsError:
            continue
    raise OSError("No se pudo crear un directorio de ejecución exclusivo")


def _write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _record_error(errors: list, source: str, message: str, url: str | None = None) -> None:
    error = {"source": source, "message": message}
    if url:
        error["url"] = _safe_url(url)
    errors.append(error)


def run(issue_reference: str, output_dir: str | None = None) -> str:
    _configured()
    requested_key = _issue_key(issue_reference)
    try:
        issue = jira_client.get_issue_details(requested_key)
    except Exception as err:
        raise RuntimeError(f"No se pudo recuperar el issue Jira {requested_key}: {_public_error(err)}") from None

    if not isinstance(issue, dict) or not isinstance(issue.get("fields"), dict):
        raise RuntimeError("Jira devolvió un issue con estructura no válida")
    fields = issue.get("fields", {})
    issue_key = str(issue.get("key") or requested_key).upper()
    if not _ISSUE_KEY.fullmatch(issue_key):
        raise RuntimeError("Jira devolvió una clave de issue no válida")
    names = issue.get("names", {})
    schemas = issue.get("schema", {})
    names = names if isinstance(names, dict) else {}
    schemas = schemas if isinstance(schemas, dict) else {}
    base_ids = ("summary", "description", "updated", "issuetype", "status", "labels")
    selected_fields = {field_id: fields[field_id] for field_id in base_ids if field_id in fields}
    selected_fields.update(_custom_requirement_fields(fields, names, schemas))
    selected_names = {field_id: names[field_id] for field_id in selected_fields if field_id in names}
    selected_schema = {field_id: schemas[field_id] for field_id in selected_fields if field_id in schemas}
    snapshot = {"key": issue_key, "fields": selected_fields, "names": selected_names, "schema": selected_schema}
    markdown, unsupported_nodes = jira_to_markdown(selected_fields, selected_names)

    run_dir = _new_run_directory(issue_key, output_dir)
    errors = []
    skipped_links = []
    jira_json = run_dir / "jira.json"
    jira_markdown = run_dir / "jira.md"
    try:
        _write_json(jira_json, snapshot)
        jira_markdown.write_text(markdown, encoding="utf-8")
    except OSError:
        raise RuntimeError("No se pudo persistir el snapshot Jira") from None

    original_updated = selected_fields.get("updated")
    jira_url = f"{config.JIRA['base_url']}/browse/{urllib.parse.quote(issue_key, safe='-_')}"
    sources = [{
        "type": "jira",
        "id": issue_key,
        "title": selected_fields.get("summary", ""),
        "url": jira_url,
        "original_updated_at": original_updated,
        "updated_at_utc": _normalized_timestamp(original_updated),
        "timestamp_origin": "Jira fields.updated",
        "paths": {"json": "jira.json", "markdown": "jira.md"},
        "unsupported_adf_nodes": unsupported_nodes,
    }]

    requirement_values = {
        field_id: value
        for field_id, value in selected_fields.items()
        if field_id == "description" or field_id.startswith("customfield_")
    }
    urls = [(url, "Jira requirement field") for url in extract_urls(requirement_values)]
    try:
        for link in jira_client.get_remote_links_for_issue(issue_key):
            url = link.get("object", {}).get("url")
            if isinstance(url, str) and url:
                urls.append((url, "Jira remote link"))
    except Exception as err:
        _record_error(errors, "jira_remote_links", _public_error(err))

    unique_urls = {}
    for url, origin in urls:
        unique_urls.setdefault(url, origin)
    downloaded_ids = set()
    for url, link_source in unique_urls.items():
        try:
            page_id = _resolve_page_id(url)
        except Exception as err:
            reason = _public_error(err)
            if "otro sitio" in reason or "no compatible" in reason:
                skipped_links.append({"source": link_source, "url": _safe_url(url), "reason": reason})
            else:
                _record_error(errors, link_source, reason, url)
            continue
        if page_id in downloaded_ids:
            continue
        downloaded_ids.add(page_id)
        try:
            page = confluence_client.fetch_page_by_id(page_id)
        except Exception as err:
            _record_error(errors, "confluence_page", _public_error(err), url)
            continue
        if not isinstance(page, dict):
            _record_error(errors, "confluence_page", "Confluence devolvió una página con estructura no válida", url)
            continue
        try:
            page_markdown = to_markdown(page)
        except Exception as err:
            _record_error(errors, "confluence_page", _public_error(err), url)
            continue
        try:
            raw_path = f"confluence-{page_id}.json"
            md_path = f"confluence-{page_id}.md"
            _write_json(run_dir / raw_path, page)
            (run_dir / md_path).write_text(page_markdown, encoding="utf-8")
        except OSError:
            raise RuntimeError("No se pudo persistir una página Confluence del bundle") from None
        version = page.get("version", {})
        page_updated = version.get("createdAt")
        sources.append({
            "type": "confluence",
            "id": page_id,
            "title": page.get("title", ""),
            "url": f"{config.CONFLUENCE['base_url']}/pages/{page_id}",
            "original_updated_at": page_updated,
            "updated_at_utc": _normalized_timestamp(page_updated),
            "timestamp_origin": "Confluence version.createdAt",
            "version_number": version.get("number"),
            "paths": {"json": raw_path, "markdown": md_path},
        })

    manifest = {
        "manifest_version": 1,
        "canonical_issue_key": issue_key,
        "site": urllib.parse.urlsplit(config.JIRA["base_url"]).hostname,
        "fetched_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "completeness": "partial" if errors or skipped_links else "complete",
        "sources": sources,
        "errors": errors,
        "skipped_links": skipped_links,
    }
    manifest_path = run_dir / "manifest.json"
    try:
        _write_json(manifest_path, manifest)
    except OSError:
        raise RuntimeError("No se pudo persistir el manifest del bundle") from None
    return str(manifest_path.resolve())


def _public_error(error: Exception) -> str:
    if isinstance(error, AtlassianRequestError):
        return str(error)
    if isinstance(error, ValueError):
        return str(error)
    if isinstance(error, OSError):
        return "Error local de red o escritura"
    return "Error al procesar la respuesta del servicio Atlassian"