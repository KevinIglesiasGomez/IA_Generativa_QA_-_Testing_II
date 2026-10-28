import os


# Carga manual del .env para no depender de python-dotenv
def _load_env_file(path: str = ".env") -> None:
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


_load_env_file()

ATLASSIAN_SITE = os.getenv("ATLASSIAN_SITE")
_SITE_URL = f"https://{ATLASSIAN_SITE}.atlassian.net" if ATLASSIAN_SITE else None

CONFLUENCE = {
    "base_url": f"{_SITE_URL}/wiki" if _SITE_URL else None,
    "user_email": os.getenv("ATLASSIAN_USER_EMAIL"),
    "api_token": os.getenv("ATLASSIAN_API_TOKEN"),
}

JIRA_REQUIREMENT_FIELD_IDS = tuple(
    field_id.strip()
    for field_id in os.getenv("JIRA_REQUIREMENT_FIELD_IDS", "").split(",")
    if field_id.strip()
)

JIRA = {
    "base_url": _SITE_URL,
    "user_email": os.getenv("ATLASSIAN_USER_EMAIL"),
    "api_token": os.getenv("ATLASSIAN_API_TOKEN"),
}

OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output")
