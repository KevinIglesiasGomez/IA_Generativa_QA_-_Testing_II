import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR / "config"))

import get_by_id  # noqa: E402
import get_by_title_and_space  # noqa: E402
import get_by_jira_issue  # noqa: E402
import search  # noqa: E402
import batch  # noqa: E402
import get_issue_context  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Descarga contenido de Confluence por ID, titulo+espacio o issue de Jira")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", metavar="PAGE_ID", help="ID de la pagina de Confluence")
    group.add_argument("--title", nargs=2, metavar=("TITULO", "ESPACIO"), help="Titulo y clave del espacio")
    group.add_argument("--issue", metavar="ISSUE_KEY", help="Clave del issue de Jira (ej. PROJ-123)")
    group.add_argument(
        "--issue-context",
        metavar="ISSUE_KEY_OR_URL",
        help="Descarga el issue de Jira y sus páginas de Confluence directas en un bundle versionado",
    )
    group.add_argument("--search", metavar="TEXTO", help="Busca paginas por texto libre (no descarga, solo lista resultados)")
    group.add_argument("--batch", metavar="FICHERO.json", help="Descarga varios items (id/issue/title+space) listados en un JSON")
    parser.add_argument("--space", metavar="ESPACIO", help="Acota --search a un espacio de Confluence")
    parser.add_argument("--limit", type=int, default=10, help="Numero maximo de resultados para --search (por defecto 10)")
    parser.add_argument("--format", choices=get_by_id.FORMATOS, default="json", help="Formato de salida (por defecto json)")

    args = parser.parse_args()

    try:
        if args.issue_context and "--format" in sys.argv and args.format != "json":
            parser.error("--issue-context siempre genera un manifest.json y documentos Markdown; no admite --format distinto de json")
        if args.id:
            get_by_id.run(args.id, args.format)
        elif args.title:
            get_by_title_and_space.run(args.title[0], args.title[1], args.format)
        elif args.issue:
            get_by_jira_issue.run(args.issue, args.format)
        elif args.issue_context:
            print(get_issue_context.run(args.issue_context))
        elif args.search:
            search.run(args.search, args.space, args.limit)
        elif args.batch:
            batch.run(args.batch, args.format)
    except Exception as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
