from jira_client import find_confluence_page_id_from_issue
import get_by_id


def run(issue_key: str, fmt: str = "json") -> dict:
    page_id = find_confluence_page_id_from_issue(issue_key)
    return get_by_id.run(page_id, fmt)
