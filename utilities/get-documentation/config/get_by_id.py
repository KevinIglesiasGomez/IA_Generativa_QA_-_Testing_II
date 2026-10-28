import json
import os
import config
from confluence_client import fetch_page_by_id
from formatters import extract_storage_html, to_markdown, to_text

FORMATOS = ("json", "html", "md", "txt")


def run(page_id: str, fmt: str = "json") -> dict:
    page = fetch_page_by_id(page_id)
    _guardar(page, fmt)
    return page


def _guardar(page: dict, fmt: str) -> None:
    if fmt not in FORMATOS:
        raise ValueError(f"Formato no soportado: {fmt}")

    if fmt == "json":
        contenido = json.dumps(page, ensure_ascii=False, indent=2)
    elif fmt == "html":
        contenido = extract_storage_html(page)
    elif fmt == "md":
        contenido = to_markdown(page)
    else:
        contenido = to_text(page)

    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(config.OUTPUT_DIR, f"{page['id']}.{fmt}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"Guardado: {file_path}")
