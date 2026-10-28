import json

import get_by_id
import get_by_title_and_space
import get_by_jira_issue


def _procesar_item(item: dict, fmt_default: str) -> None:
    fmt = item.get("format", fmt_default)

    if "id" in item:
        get_by_id.run(item["id"], fmt)
    elif "issue" in item:
        get_by_jira_issue.run(item["issue"], fmt)
    elif "title" in item and "space" in item:
        get_by_title_and_space.run(item["title"], item["space"], fmt)
    else:
        raise ValueError(f"item sin identificador valido (id / issue / title+space): {item}")


# Procesa cada item de forma independiente: un fallo no detiene el resto del lote
def run(batch_path: str, fmt_default: str = "json") -> None:
    with open(batch_path, "r", encoding="utf-8") as f:
        items = json.load(f)

    if not isinstance(items, list):
        raise ValueError("El fichero de batch debe contener una lista JSON de items")

    correctos = 0
    fallidos = []

    for i, item in enumerate(items, start=1):
        etiqueta = item.get("id") or item.get("issue") or item.get("title") or f"item {i}"
        try:
            _procesar_item(item, fmt_default)
            correctos += 1
        except Exception as err:
            fallidos.append(etiqueta)
            print(f"Error en '{etiqueta}': {err}")

    print(f"\nProcesados {len(items)} item(s): {correctos} correcto(s), {len(fallidos)} con error.")
    if fallidos:
        print("Con error: " + ", ".join(str(f) for f in fallidos))
