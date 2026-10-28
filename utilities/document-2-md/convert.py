#!/usr/bin/env python3
"""
Conversor unificado de documentos.

Unico ejecutable del proyecto: "python convert.py". Funciona igual en Windows y
Linux, sin entorno virtual ni scripts auxiliares en el caso normal: instala solo
las dependencias que falten en el Python activo. Si el sistema bloquea la
instalacion directa (PEP 668, tipico en Debian/Ubuntu recientes), crea de forma
automatica un entorno virtual local (`.venv`) solo para ese caso y se relanza con el.

Detecta automaticamente el tipo del archivo de entrada y lo enruta al
conversor adecuado, sin necesidad de elegir manualmente el script:

    .docx -> Markdown
    .pdf  -> Markdown (por defecto) o DOCX (--pdf-to docx)

Reutiliza las funciones de conversion ya existentes en config/ (no duplica logica).
"""

import argparse
import importlib.util
import os
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent

# nombre de import -> especificador de paquete pip
REQUIRED_MODULES = {
    "docx": "python-docx>=0.8.11",
    "PIL": "Pillow>=9.0.0",
    "fitz": "PyMuPDF>=1.23.0",
    "pdf2docx": "pdf2docx>=0.5.6",
}


def ensure_dependencies():
    """Instala con pip, en el Python activo, los paquetes que falten.

    Si el sistema rechaza la instalacion directa (PEP 668, "externally-managed-
    environment", habitual en Debian/Ubuntu recientes), crea un venv local en
    .venv/, instala ahi las dependencias y relanza el script con ese Python.
    """
    missing = [pkg for mod, pkg in REQUIRED_MODULES.items() if importlib.util.find_spec(mod) is None]
    if not missing:
        return
    print(f"Instalando dependencias faltantes: {', '.join(missing)}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    except subprocess.CalledProcessError:
        in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
        if in_venv:
            raise
        _bootstrap_local_venv()


def _bootstrap_local_venv():
    """Crea .venv/, instala ahi las dependencias y relanza convert.py con ese Python."""
    venv_dir = ROOT_DIR / ".venv"
    print(f"El Python del sistema esta protegido (PEP 668). Creando entorno virtual local en {venv_dir}...")
    subprocess.check_call([sys.executable, "-m", "venv", str(venv_dir)])
    venv_python = venv_dir / ("Scripts\\python.exe" if os.name == "nt" else "bin/python")
    subprocess.check_call([str(venv_python), "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([str(venv_python), "-m", "pip", "install", *REQUIRED_MODULES.values()])
    os.execv(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]])


ensure_dependencies()

sys.path.insert(0, str(ROOT_DIR / "config"))

import word_to_markdown  # noqa: E402
import pdf_to_markdown as pdf_to_markdown_mod  # noqa: E402
import pdf_to_docx as pdf_to_docx_mod  # noqa: E402

SUPPORTED_EXTENSIONS = (".docx", ".pdf")
# reconocidas pero sin conversion automatica: se informan en el resumen en vez de ignorarse
UNSUPPORTED_EXTENSIONS = (".doc",)


def convert_file(path: Path, output_dir: Path, pdf_to: str, skip_sections_override):
    """Convierte un unico archivo segun su extension. Devuelve el formato generado."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ext = path.suffix.lower()

    if ext == ".docx":
        skip_sections = skip_sections_override
        if skip_sections is None:
            skip_sections = word_to_markdown.load_config_file()
        word_to_markdown.docx_to_markdown(str(path), str(output_dir), skip_sections)
        return "markdown"

    if ext == ".pdf":
        if pdf_to == "docx":
            out_path = output_dir / (path.stem + ".docx")
            pdf_to_docx_mod.convert_pdf_to_docx(str(path), str(out_path))
            return "docx"

        skip_sections, extract_images, preserve_links = pdf_to_markdown_mod.load_config_file()
        if skip_sections_override is not None:
            skip_sections = skip_sections_override
        pdf_to_markdown_mod.pdf_to_markdown(
            str(path), str(output_dir), skip_sections, extract_images, preserve_links
        )
        return "markdown"

    if ext == ".doc":
        raise ValueError(
            ".doc (formato binario Word 97-2003) no esta soportado. "
            "Abrelo y guardalo como .docx (Word o LibreOffice: 'Guardar como' -> .docx) y vuelve a intentarlo."
        )

    raise ValueError(f"extension no soportada: {path.suffix}")


def collect_input_files(input_path: Path):
    recognized = SUPPORTED_EXTENSIONS + UNSUPPORTED_EXTENSIONS
    if input_path.is_file():
        return [input_path]
    return sorted(
        p for p in input_path.iterdir()
        if p.is_file() and p.suffix.lower() in recognized and not p.name.startswith("~")
    )


def main():
    parser = argparse.ArgumentParser(
        description="Convierte documentos detectando automaticamente su tipo (.docx / .pdf).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python convert.py                              # usa input/ -> output/
  python convert.py mis_docs/ salida/
  python convert.py informe.pdf salida/ --pdf-to docx
  python convert.py mis_docs/ salida/ --skip-sections "none"
""",
    )
    parser.add_argument("input", nargs="?", default="input", help="Archivo o carpeta de entrada (por defecto: input/)")
    parser.add_argument("output", nargs="?", default="output", help="Carpeta de salida (por defecto: output/)")
    parser.add_argument(
        "--pdf-to", choices=["markdown", "docx"], default="markdown",
        help="Formato de salida para los PDF (por defecto: markdown)",
    )
    parser.add_argument(
        "--skip-sections", default=None,
        help='Secciones a omitir separadas por coma, o "none" (aplica a conversiones a Markdown)',
    )
    args = parser.parse_args()

    if args.skip_sections is None:
        skip_override = None
    elif args.skip_sections.lower() == "none":
        skip_override = []
    else:
        skip_override = [s.strip() for s in args.skip_sections.split(",") if s.strip()]

    input_path = Path(args.input)
    output_dir = Path(args.output)

    if not input_path.exists():
        if str(input_path) == "input":
            input_path.mkdir(parents=True, exist_ok=True)
            print(f"Carpeta de entrada '{input_path}' creada. Coloca ahi tus .docx/.pdf y vuelve a ejecutar.")
            return
        print(f"Error: '{input_path}' no existe.")
        sys.exit(1)

    files = collect_input_files(input_path)

    print("=" * 50)
    print("Conversor unificado de documentos")
    print("=" * 50)
    print(f"Entrada: {input_path}")
    print(f"Salida:  {output_dir}")
    print(f"PDF -> {args.pdf_to}")
    print("=" * 50)

    if not files:
        print(f"No se encontraron documentos .docx/.pdf/.doc en '{input_path}'.")
        return

    resultados = []  # (nombre, ok, detalle)
    for f in files:
        try:
            target = convert_file(f, output_dir, args.pdf_to, skip_override)
            print(f"[OK]    {f.name} -> {target}")
            resultados.append((f.name, True, target))
        except Exception as e:
            print(f"[ERROR] {f.name}: {e}")
            resultados.append((f.name, False, str(e)))

    ok_count = sum(1 for _, ok, _ in resultados if ok)

    print("\n" + "=" * 50)
    print("Resumen de la conversion")
    print("=" * 50)
    for nombre, ok, detalle in resultados:
        marca = "OK   " if ok else "ERROR"
        print(f"[{marca}] {nombre:<40} {detalle}")
    print("-" * 50)
    print(f"Total: {len(resultados)} | Exitosos: {ok_count} | Fallidos: {len(resultados) - ok_count}")
    print(f"Salida en: {output_dir}")


if __name__ == "__main__":
    main()
