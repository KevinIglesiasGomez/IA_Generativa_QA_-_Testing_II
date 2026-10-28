import re
import json
from html.parser import HTMLParser


def extract_storage_html(page: dict) -> str:
    return page.get("body", {}).get("storage", {}).get("value", "")


class _TextExtractor(HTMLParser):
    _BLOCK_TAGS = {"p", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self):
        super().__init__()
        self._parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self._BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data):
        self._parts.append(data)

    def get_text(self) -> str:
        text = "".join(self._parts)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def to_text(page: dict) -> str:
    parser = _TextExtractor()
    parser.feed(extract_storage_html(page))
    return parser.get_text()


class _MarkdownExtractor(HTMLParser):
    _HEADINGS = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "h5": "##### ", "h6": "###### "}

    def __init__(self):
        super().__init__()
        self._parts = []
        self._list_stack = []
        self._just_opened_li = False
        self._tables = []  # pila de tablas, soporta anidación aunque Confluence no suele anidarlas
        self._cell_buffer = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self._tables.append({"rows": [], "current_row": None, "is_header": False})
            return
        if self._tables:
            self._handle_table_starttag(tag)
            return

        if tag in self._HEADINGS:
            self._parts.append("\n" + self._HEADINGS[tag])
        elif tag == "p":
            if not self._just_opened_li:
                self._parts.append("\n")
        elif tag in ("strong", "b"):
            self._parts.append("**")
        elif tag in ("em", "i"):
            self._parts.append("_")
        elif tag in ("ul", "ol"):
            self._list_stack.append(tag)
        elif tag == "li":
            prefix = "- " if (self._list_stack and self._list_stack[-1] == "ul") else "1. "
            self._parts.append("\n" + prefix)

        self._just_opened_li = tag == "li"

    def _handle_table_starttag(self, tag):
        table = self._tables[-1]
        if tag == "tr":
            table["current_row"] = []
            table["is_header"] = False
        elif tag in ("th", "td"):
            self._cell_buffer = []
            if tag == "th":
                table["is_header"] = True
        elif tag == "p" and self._cell_buffer:
            self._cell_buffer.append(" ")
        elif tag == "br" and self._cell_buffer is not None:
            self._cell_buffer.append(" ")
        elif tag in ("strong", "b") and self._cell_buffer is not None:
            self._cell_buffer.append("**")
        elif tag in ("em", "i") and self._cell_buffer is not None:
            self._cell_buffer.append("_")

    def handle_endtag(self, tag):
        if tag == "table" and self._tables:
            table = self._tables.pop()
            markdown_table = self._render_table(table["rows"])
            if self._tables:
                # tabla anidada: se inserta como texto plano en la celda contenedora
                if self._cell_buffer is not None:
                    self._cell_buffer.append(markdown_table)
            else:
                self._parts.append("\n" + markdown_table + "\n")
            return
        if self._tables:
            self._handle_table_endtag(tag)
            return

        if tag in self._HEADINGS:
            self._parts.append("\n")
        elif tag in ("strong", "b"):
            self._parts.append("**")
        elif tag in ("em", "i"):
            self._parts.append("_")
        elif tag in ("ul", "ol") and self._list_stack:
            self._list_stack.pop()

    def _handle_table_endtag(self, tag):
        table = self._tables[-1]
        if tag == "tr" and table["current_row"] is not None:
            table["rows"].append({"cells": table["current_row"], "is_header": table["is_header"]})
            table["current_row"] = None
        elif tag in ("th", "td") and self._cell_buffer is not None:
            text = "".join(self._cell_buffer).strip()
            text = re.sub(r"\s+", " ", text).replace("|", "\\|")
            table["current_row"].append(text)
            self._cell_buffer = None
        elif tag in ("strong", "b") and self._cell_buffer is not None:
            self._cell_buffer.append("**")
        elif tag in ("em", "i") and self._cell_buffer is not None:
            self._cell_buffer.append("_")

    @staticmethod
    def _render_table(rows: list) -> str:
        if not rows:
            return ""
        has_header = rows[0]["is_header"]
        header_cells = rows[0]["cells"] if has_header else [""] * len(rows[0]["cells"])
        body_rows = rows[1:] if has_header else rows

        lines = [
            "| " + " | ".join(header_cells) + " |",
            "| " + " | ".join("---" for _ in header_cells) + " |",
        ]
        lines.extend("| " + " | ".join(row["cells"]) + " |" for row in body_rows)
        return "\n".join(lines)

    def handle_data(self, data):
        if self._tables:
            if self._cell_buffer is not None:
                self._cell_buffer.append(data)
            return
        self._parts.append(data)

    def get_markdown(self) -> str:
        text = "".join(self._parts)
        return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def to_markdown(page: dict) -> str:
    parser = _MarkdownExtractor()
    parser.feed(extract_storage_html(page))
    return parser.get_markdown()


_URL_PATTERN = re.compile(r"https?://[^\s<>\"']+", re.IGNORECASE)


def extract_urls(value) -> list[str]:
    found = []

    def visit(item):
        if isinstance(item, str):
            found.extend(match.rstrip(".,;:!?)]}") for match in _URL_PATTERN.findall(item))
        elif isinstance(item, list):
            for child in item:
                visit(child)
        elif isinstance(item, dict):
            attrs = item.get("attrs", {})
            for key in ("url", "href"):
                if isinstance(attrs.get(key), str):
                    found.append(attrs[key])
            for mark in item.get("marks", []):
                if isinstance(mark, dict):
                    href = mark.get("attrs", {}).get("href")
                    if isinstance(href, str):
                        found.append(href)
            for child in item.values():
                visit(child)

    visit(value)
    return list(dict.fromkeys(found))


class _ADFRenderer:
    def __init__(self):
        self.unsupported_nodes = []

    def render_value(self, value) -> str:
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            return "\n".join(filter(None, (self.render_value(item) for item in value)))
        if not isinstance(value, dict):
            return str(value)
        if "type" not in value:
            return json.dumps(value, ensure_ascii=False, sort_keys=True)
        return self.node(value)

    def node(self, node: dict) -> str:
        node_type = node.get("type", "unknown")
        if node_type in ("bulletList", "orderedList"):
            items = []
            for index, item in enumerate(node.get("content", []), start=1):
                if not isinstance(item, dict) or item.get("type") != "listItem":
                    continue
                body_parts = []
                for child in item.get("content", []):
                    if isinstance(child, dict):
                        rendered = self.node(child).strip()
                        if rendered:
                            body_parts.append(rendered)
                body = " ".join(body_parts)
                marker = f"{index}." if node_type == "orderedList" else "-"
                items.append(f"{marker} {body}")
            return "\n".join(items) + "\n\n"
        children = [self.node(child) for child in node.get("content", []) if isinstance(child, dict)]
        text = node.get("text", "")
        if node_type in ("doc", "paragraph"):
            rendered = "".join(children)
            return rendered + ("\n\n" if node_type == "paragraph" and rendered else "")
        if node_type == "text":
            rendered = str(text)
            for mark in node.get("marks", []):
                mark_type = mark.get("type") if isinstance(mark, dict) else None
                if mark_type == "strong":
                    rendered = f"**{rendered}**"
                elif mark_type == "em":
                    rendered = f"_{rendered}_"
                elif mark_type == "code":
                    rendered = f"`{rendered}`"
                elif mark_type == "link":
                    href = mark.get("attrs", {}).get("href", "")
                    if href:
                        rendered = f"[{rendered}]({href})"
            return rendered
        if node_type in ("heading",):
            level = max(1, min(6, int(node.get("attrs", {}).get("level", 1))))
            return f"{'#' * level} {''.join(children).strip()}\n\n"
        if node_type == "listItem":
            body = " ".join(part.strip() for part in children if part.strip())
            return f"- {body}"
        if node_type in ("hardBreak",):
            return "\n"
        if node_type == "rule":
            return "\n---\n\n"
        if node_type in ("table", "tableRow", "tableCell", "tableHeader"):
            if node_type == "tableRow":
                return "| " + " | ".join(part.replace("\n", " ").strip() for part in children) + " |\n"
            if node_type == "table":
                rows = [part for part in children if part.strip()]
                if not rows:
                    return ""
                first = rows[0]
                cells = first.count("|") - 1
                separator = "| " + " | ".join("---" for _ in range(max(0, cells))) + " |\n"
                return first + separator + "".join(rows[1:]) + "\n"
            return " ".join(children).strip()
        if node_type in ("inlineCard", "blockCard"):
            url = node.get("attrs", {}).get("url", "")
            return f"[{url}]({url})" if url else ""

        self.unsupported_nodes.append(node_type)
        suffix = "".join(children)
        raw_text = str(text) if text else ""
        return f"[Contenido Jira no compatible: {node_type}] {raw_text}{suffix}"


def jira_to_markdown(fields: dict, field_names: dict | None = None) -> tuple[str, list[str]]:
    renderer = _ADFRenderer()
    field_names = field_names or {}
    lines = []
    summary = fields.get("summary")
    if summary:
        lines.extend([f"# {summary}", ""])
    for field_id, value in fields.items():
        if field_id == "summary" or value is None or value == "":
            continue
        title = field_names.get(field_id, field_id)
        rendered = renderer.render_value(value).strip()
        if rendered:
            lines.extend([f"## {title}", "", rendered, ""])
    return "\n".join(lines).rstrip() + "\n", list(dict.fromkeys(renderer.unsupported_nodes))
