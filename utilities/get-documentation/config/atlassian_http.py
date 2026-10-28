from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import base64
import json
import time
import urllib.error
import urllib.parse
import urllib.request


TIMEOUT_SECONDS = 30
MAX_ATTEMPTS = 3
MAX_RETRY_WAIT_SECONDS = 5


class AtlassianRequestError(RuntimeError):
    pass


def _origin(url: str) -> tuple[str, str, int]:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise AtlassianRequestError("Atlassian requests require a trusted HTTPS URL")
    return parsed.scheme.lower(), parsed.hostname.lower(), parsed.port or 443


class _SameOriginRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self, allowed_origin: tuple[str, str, int]):
        super().__init__()
        self.allowed_origin = allowed_origin
        self.max_redirections = 5

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if _origin(newurl) != self.allowed_origin:
            raise AtlassianRequestError("Atlassian redirected to an untrusted origin")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _retry_delay(headers) -> float:
    value = headers.get("Retry-After") if headers else None
    if value:
        try:
            return min(MAX_RETRY_WAIT_SECONDS, max(0, float(value)))
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(value)
                if retry_at.tzinfo is None:
                    retry_at = retry_at.replace(tzinfo=timezone.utc)
                return min(MAX_RETRY_WAIT_SECONDS, max(0, (retry_at - datetime.now(timezone.utc)).total_seconds()))
            except (TypeError, ValueError, OverflowError):
                pass
    return 1


def request_bytes(
    url: str,
    credentials: tuple[str, str] | None,
    allowed_origin_url: str,
) -> tuple[bytes, str]:
    allowed_origin = _origin(allowed_origin_url)
    if _origin(url) != allowed_origin:
        raise AtlassianRequestError("Refusing to send Atlassian credentials to an untrusted origin")

    headers = {"Accept": "application/json"}
    if credentials is not None:
        token = base64.b64encode(f"{credentials[0]}:{credentials[1]}".encode()).decode()
        headers["Authorization"] = f"Basic {token}"
    request = urllib.request.Request(url, headers=headers)
    opener = urllib.request.build_opener(_SameOriginRedirectHandler(allowed_origin))
    for attempt in range(MAX_ATTEMPTS):
        try:
            with opener.open(request, timeout=TIMEOUT_SECONDS) as response:
                final_url = response.geturl()
                if _origin(final_url) != allowed_origin:
                    raise AtlassianRequestError("Atlassian redirected to an untrusted origin")
                return response.read(), final_url
        except urllib.error.HTTPError as err:
            retryable = err.code == 429 or 500 <= err.code <= 599
            if retryable and attempt < MAX_ATTEMPTS - 1:
                retry_delay = _retry_delay(err.headers)
                err.close()
                time.sleep(retry_delay)
                continue
            err.close()
            raise AtlassianRequestError(f"Atlassian request failed with HTTP {err.code}") from None
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            if attempt < MAX_ATTEMPTS - 1:
                time.sleep(1)
                continue
            reason = getattr(err, "reason", None)
            if isinstance(reason, TimeoutError) or isinstance(err, TimeoutError):
                raise AtlassianRequestError("Atlassian request timed out after bounded retries") from None
            raise AtlassianRequestError("Atlassian request failed after bounded retries") from None
    raise AtlassianRequestError("Atlassian request failed after bounded retries")


def request_json(url: str, credentials: tuple[str, str], allowed_origin_url: str) -> dict | list:
    payload, _ = request_bytes(url, credentials, allowed_origin_url)
    try:
        return json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise AtlassianRequestError("Atlassian returned an invalid JSON response") from None