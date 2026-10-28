from confluence_client import search_pages


def run(query: str, space_key: str | None = None, limit: int = 10) -> list:
    data = search_pages(query, space_key, limit)
    resultados = data["results"]
    total = data["total"]

    if not resultados:
        print("No se encontraron resultados.")
        return resultados

    for r in resultados:
        print(f"{r['id']}\t{r['title']}\t{r['url']}")

    print(f"\nMostrando {len(resultados)} de {total} resultado(s) totales.")
    if total > len(resultados):
        print("Hay mas resultados disponibles: aumenta --limit para verlos.")

    return resultados
