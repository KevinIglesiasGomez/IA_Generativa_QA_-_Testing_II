import json
import io
from pathlib import Path
import sys
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

CONFIG_DIR = Path(__file__).resolve().parents[1] / "config"
UTILITY_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CONFIG_DIR))
sys.path.insert(0, str(UTILITY_DIR))

import config
import atlassian_http
import download
from formatters import jira_to_markdown
import get_by_jira_issue
import get_issue_context
import jira_client


class IssueContextTests(unittest.TestCase):
    def setUp(self):
        self.output = tempfile.TemporaryDirectory()
        self.addCleanup(self.output.cleanup)
        config.JIRA.update({
            "base_url": "https://example.atlassian.net",
            "user_email": "test@example.invalid",
            "api_token": "never-print-this-token",
        })
        config.CONFLUENCE.update({
            "base_url": "https://example.atlassian.net/wiki",
            "user_email": "test@example.invalid",
            "api_token": "never-print-this-token",
        })
        self.requirement_fields = config.JIRA_REQUIREMENT_FIELD_IDS
        config.JIRA_REQUIREMENT_FIELD_IDS = ()

    def tearDown(self):
        config.JIRA_REQUIREMENT_FIELD_IDS = self.requirement_fields

    def _issue(self, description=None):
        return {
            "key": "DEMO-12",
            "fields": {
                "summary": "Payment requirements",
                "description": description or {
                    "type": "doc",
                    "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Pay only once."}]}],
                },
                "updated": "2026-10-15T17:30:00+02:00",
                "issuetype": {"name": "Story"},
                "status": {"name": "Open"},
                "labels": ["payments"],
                "customfield_10101": {
                    "type": "doc",
                    "content": [{"type": "paragraph", "content": [{"type": "text", "text": "The confirmation appears."}]}],
                },
                "customfield_10102": "5",
            },
            "names": {"customfield_10101": "Criterios de aceptación", "customfield_10102": "Story Points"},
            "schema": {
                "customfield_10101": {"type": "string", "custom": "textarea"},
                "customfield_10102": {"type": "number", "custom": "number"},
            },
        }

    def _manifest(self, issue=None, remote_links=None, page=None):
        with patch.object(get_issue_context.jira_client, "get_issue_details", return_value=issue or self._issue()), \
             patch.object(get_issue_context.jira_client, "get_remote_links_for_issue", return_value=remote_links or []), \
             patch.object(get_issue_context.confluence_client, "fetch_page_by_id", return_value=page or {}):
            path = get_issue_context.run("DEMO-12", self.output.name)
        return Path(path), json.loads(Path(path).read_text(encoding="utf-8"))

    def test_jira_only_bundle_includes_requirements_and_edit_metadata(self):
        path, manifest = self._manifest()
        self.assertEqual(manifest["completeness"], "complete")
        self.assertEqual([source["type"] for source in manifest["sources"]], ["jira"])
        self.assertEqual(manifest["sources"][0]["updated_at_utc"], "2026-10-15T15:30:00Z")
        self.assertTrue((path.parent / "jira.md").exists())
        snapshot = json.loads((path.parent / "jira.json").read_text(encoding="utf-8"))
        self.assertIn("customfield_10101", snapshot["fields"])
        self.assertNotIn("customfield_10102", snapshot["fields"])
        self.assertIn("Criterios de aceptación", (path.parent / "jira.md").read_text(encoding="utf-8"))

    def test_inline_and_remote_links_are_deduplicated_and_page_version_is_used(self):
        description = {
            "type": "doc",
            "content": [{"type": "inlineCard", "attrs": {"url": "https://example.atlassian.net/wiki/pages/77/detail"}}],
        }
        page = {"id": "77", "title": "Policy", "version": {"number": 4, "createdAt": "2026-10-14T10:00:00Z"}, "body": {"storage": {"value": "<p>Rule</p>"}}}
        path, manifest = self._manifest(
            issue=self._issue(description),
            remote_links=[{"object": {"url": "https://example.atlassian.net/wiki/pages/77/other"}}],
            page=page,
        )
        self.assertEqual(len(manifest["sources"]), 2)
        self.assertEqual(manifest["sources"][1]["updated_at_utc"], "2026-10-14T10:00:00Z")
        self.assertEqual(manifest["sources"][1]["version_number"], 4)
        self.assertTrue((path.parent / "confluence-77.md").exists())

    def test_failed_remote_link_lookup_keeps_partial_jira_bundle(self):
        with patch.object(get_issue_context.jira_client, "get_issue_details", return_value=self._issue()), \
             patch.object(get_issue_context.jira_client, "get_remote_links_for_issue", side_effect=RuntimeError("ignored details")):
            path = Path(get_issue_context.run("DEMO-12", self.output.name))
        manifest = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["completeness"], "partial")
        self.assertEqual(manifest["errors"][0]["source"], "jira_remote_links")
        self.assertNotIn("ignored details", path.read_text(encoding="utf-8"))

    def test_cross_site_links_are_not_fetched_or_sent_credentials(self):
        issue = self._issue({"type": "doc", "content": [{"type": "inlineCard", "attrs": {"url": "https://attacker.invalid/wiki/pages/77"}}]})
        with patch.object(get_issue_context.jira_client, "get_issue_details", return_value=issue), \
             patch.object(get_issue_context.jira_client, "get_remote_links_for_issue", return_value=[]), \
             patch.object(get_issue_context, "request_bytes") as request_bytes:
            path = Path(get_issue_context.run("DEMO-12", self.output.name))
        manifest = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["completeness"], "partial")
        self.assertEqual(request_bytes.call_count, 0)
        self.assertEqual(manifest["skipped_links"][0]["url"], "https://attacker.invalid/wiki/pages/77")

    def test_url_and_issue_key_validation(self):
        with self.assertRaises(ValueError):
            get_issue_context._issue_key("DEMO-12; touch /tmp/nope")
        with self.assertRaises(ValueError):
            get_issue_context._issue_key("https://attacker.invalid/browse/DEMO-12")
        self.assertEqual(
            get_issue_context._issue_key("https://example.atlassian.net:443/browse/demo-12"),
            "DEMO-12",
        )

    def test_legacy_and_query_page_urls_are_supported(self):
        self.assertEqual(
            get_issue_context._direct_page_id("https://example.atlassian.net/wiki/viewpage.action?pageId=81", config.CONFLUENCE["base_url"]),
            "81",
        )
        self.assertEqual(
            get_issue_context._direct_page_id("https://example.atlassian.net:443/wiki/pages/82", config.CONFLUENCE["base_url"]),
            "82",
        )

    def test_invalid_and_naive_timestamps_are_not_used_for_precedence(self):
        self.assertIsNone(get_issue_context._normalized_timestamp("2026-10-15 10:00:00"))
        self.assertIsNone(get_issue_context._normalized_timestamp("not-a-date"))

    def test_repeat_runs_create_isolated_directories(self):
        first_path, _ = self._manifest()
        second_path, _ = self._manifest()
        self.assertNotEqual(first_path.parent, second_path.parent)
        self.assertEqual(len(list(Path(self.output.name, "DEMO-12").iterdir())), 2)

    def test_retry_after_is_bounded_and_retry_count_is_limited(self):
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self):
                return b'{"ok": true}'

            def geturl(self):
                return "https://example.atlassian.net/rest/api"

        class Opener:
            def __init__(self):
                self.calls = 0

            def open(self, request, timeout):
                self.calls += 1
                if self.calls == 1:
                    raise urllib.error.HTTPError("https://example.atlassian.net", 429, "busy", {"Retry-After": "0"}, None)
                return Response()

        opener = Opener()
        with patch.object(atlassian_http.urllib.request, "build_opener", return_value=opener), \
             patch.object(atlassian_http.time, "sleep") as sleep:
            payload, final_url = atlassian_http.request_bytes(
                "https://example.atlassian.net/rest/api",
                ("test@example.invalid", "never-print-this-token"),
                "https://example.atlassian.net",
            )
        self.assertEqual(payload, b'{"ok": true}')
        self.assertEqual(final_url, "https://example.atlassian.net/rest/api")
        self.assertEqual(opener.calls, 2)
        sleep.assert_called_once_with(0)

    def test_transient_server_errors_stop_after_three_attempts(self):
        class Opener:
            def __init__(self):
                self.calls = 0

            def open(self, request, timeout):
                self.calls += 1
                raise urllib.error.HTTPError("https://example.atlassian.net", 503, "busy", {}, None)

        opener = Opener()
        with patch.object(atlassian_http.urllib.request, "build_opener", return_value=opener), \
             patch.object(atlassian_http.time, "sleep") as sleep:
            with self.assertRaisesRegex(atlassian_http.AtlassianRequestError, "HTTP 503"):
                atlassian_http.request_bytes(
                    "https://example.atlassian.net/rest/api",
                    ("test@example.invalid", "never-print-this-token"),
                    "https://example.atlassian.net",
                )
        self.assertEqual(opener.calls, 3)
        self.assertEqual(sleep.call_count, 2)

    def test_untrusted_host_is_rejected_before_opening_request(self):
        with patch.object(atlassian_http.urllib.request, "build_opener") as build_opener:
            with self.assertRaisesRegex(atlassian_http.AtlassianRequestError, "untrusted origin"):
                atlassian_http.request_bytes(
                    "https://attacker.invalid/path",
                    ("test@example.invalid", "never-print-this-token"),
                    "https://example.atlassian.net",
                )
        build_opener.assert_not_called()

    def test_short_link_resolution_uses_same_origin_final_url(self):
        with patch.object(
            get_issue_context,
            "request_bytes",
            return_value=(b"", "https://example.atlassian.net/wiki/pages/77/title"),
        ) as request_bytes:
            self.assertEqual(
                get_issue_context._resolve_page_id("https://example.atlassian.net/wiki/x/short"),
                "77",
            )
        request_bytes.assert_called_once()
        self.assertIsNone(request_bytes.call_args.args[1])

    def test_anonymous_short_link_request_has_no_authorization_header(self):
        class Response:
            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self):
                return b""

            def geturl(self):
                return "https://example.atlassian.net/wiki/x/short"

        class Opener:
            def open(self, request, timeout):
                self.request = request
                return Response()

        opener = Opener()
        with patch.object(atlassian_http.urllib.request, "build_opener", return_value=opener):
            atlassian_http.request_bytes(
                "https://example.atlassian.net/wiki/x/short",
                None,
                "https://example.atlassian.net",
            )
        self.assertIsNone(opener.request.get_header("Authorization"))

    def test_cross_origin_redirect_is_blocked(self):
        handler = atlassian_http._SameOriginRedirectHandler(
            atlassian_http._origin("https://example.atlassian.net")
        )
        request = atlassian_http.urllib.request.Request("https://example.atlassian.net/start")
        with self.assertRaisesRegex(atlassian_http.AtlassianRequestError, "untrusted origin"):
            handler.redirect_request(
                request,
                None,
                302,
                "Found",
                {},
                "https://attacker.invalid/steal",
            )

    def test_cli_preserves_legacy_id_dispatch_and_rejects_incompatible_format(self):
        with patch.object(sys, "argv", ["download.py", "--id", "123"]), \
             patch.object(download.get_by_id, "run") as legacy_run:
            download.main()
        legacy_run.assert_called_once_with("123", "json")

        stderr = io.StringIO()
        with patch.object(sys, "argv", ["download.py", "--issue-context", "DEMO-12", "--format", "md"]), \
             redirect_stderr(stderr), self.assertRaises(SystemExit) as exit_error:
            download.main()
        self.assertEqual(exit_error.exception.code, 2)
        self.assertIn("no admite --format", stderr.getvalue())

    def test_issue_context_cli_prints_only_manifest_path(self):
        stdout = io.StringIO()
        with patch.object(sys, "argv", ["download.py", "--issue-context", "DEMO-12"]), \
             patch.object(download.get_issue_context, "run", return_value="/tmp/manifest.json"), \
             redirect_stdout(stdout):
            download.main()
        self.assertEqual(stdout.getvalue(), "/tmp/manifest.json\n")

    def test_unsupported_adf_is_flagged_and_raw_issue_data_is_kept(self):
        description = {
            "type": "doc",
            "content": [{"type": "extension", "attrs": {"extensionKey": "custom"}, "content": [{"type": "text", "text": "Visible requirement"}]}],
        }
        path, manifest = self._manifest(issue=self._issue(description))
        self.assertIn("extension", manifest["sources"][0]["unsupported_adf_nodes"])
        snapshot = json.loads((path.parent / "jira.json").read_text(encoding="utf-8"))
        self.assertEqual(snapshot["fields"]["description"], description)

    def test_adf_ordered_lists_and_links_render_as_markdown(self):
        adf = {
            "type": "doc",
            "content": [{
                "type": "orderedList",
                "content": [
                    {"type": "listItem", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "A&B"}]}]},
                    {"type": "listItem", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Terms", "marks": [{"type": "link", "attrs": {"href": "https://example.atlassian.net/wiki/pages/99"}}]}]}]},
                ],
            }],
        }
        markdown, unsupported = jira_to_markdown({"description": adf})
        self.assertIn("1. A&B", markdown)
        self.assertIn("2. [Terms](https://example.atlassian.net/wiki/pages/99)", markdown)
        self.assertEqual(unsupported, [])

    def test_legacy_issue_mode_still_requires_a_remote_page(self):
        with patch.object(jira_client, "_get", return_value=[]):
            with self.assertRaisesRegex(ValueError, "no tiene ninguna página"):
                get_by_jira_issue.run("DEMO-12")


if __name__ == "__main__":
    unittest.main()