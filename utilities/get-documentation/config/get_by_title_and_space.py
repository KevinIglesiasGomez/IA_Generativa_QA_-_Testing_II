from confluence_client import search_page_by_title_and_space
import get_by_id


def run(title: str, space_key: str, fmt: str = "json") -> dict:
    page_id = search_page_by_title_and_space(title, space_key)
    return get_by_id.run(page_id, fmt)
