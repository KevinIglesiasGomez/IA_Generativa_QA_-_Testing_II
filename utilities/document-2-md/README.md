# Conversores de documentos

Herramientas en Python puro (sin ejecutables ni dependencias de PyInstaller) para convertir
documentos entre formatos. Funcionan igual en **Windows** y **Linux**.

## Uso

Un único ejecutable, `convert.py`, detecta automáticamente el tipo de cada archivo de
entrada y decide qué generar. En el primer uso instala por sí solo las dependencias que
falten (no requiere crear ni activar ningún entorno virtual):

- `.docx` → Markdown
- `.pdf` → Markdown (por defecto) o DOCX si se indica `--pdf-to docx`
- `.doc` (binario, Word 97-2003) → **no soportado**: se informa en el resumen final
  en vez de ignorarse en silencio. Guárdalo antes como `.docx` (Word o LibreOffice:
  "Guardar como" → `.docx`) y vuelve a convertirlo.

Admite una carpeta (procesa todos los `.docx`/`.pdf`/`.doc` que encuentre) o un único archivo.
Al terminar muestra un resumen con el resultado (éxito o error) de cada documento.

```bash
python convert.py                                   # usa input/ -> output/ (se crea si no existe)
python convert.py mis_documentos/ salida/
python convert.py informe.pdf salida/ --pdf-to docx
python convert.py mis_documentos/ salida/ --skip-sections "none"
```

Funciona igual en Windows (`python convert.py ...`) que en Linux (`python3 convert.py ...`).

## Requisitos

- Python 3.9 o superior instalado y disponible en el PATH (`python`/`python3`).
- Conexión a internet la primera vez que se ejecuta, por si necesita instalar alguna
  dependencia (`python-docx`, `Pillow`, `PyMuPDF`, `pdf2docx`).
- En Debian/Ubuntu recientes (Python "externally-managed", PEP 668), si el sistema
  bloquea la instalación directa, `convert.py` crea automáticamente un entorno
  virtual local (`.venv/`) y se relanza con él. No requiere intervención manual.

## Configuración

- `config/word_to_markdown_config.ini` y `config/pdf_to_markdown_config.ini` permiten
  definir, entre otras cosas, las secciones del documento a omitir (`skip_sections`,
  por defecto "Historia de Versiones, Indice").

## Estructura

```
convert.py              # unico ejecutable: detecta el tipo de entrada y convierte
input/  output/          # carpetas por defecto (se crean al vuelo)
config/
  word_to_markdown_config.ini
  pdf_to_markdown_config.ini
  word_to_markdown.py
  pdf_to_markdown.py
  pdf_to_docx.py
```

(La carpeta raíz del proyecto se puede renombrar libremente: todas las rutas se calculan
de forma relativa a `convert.py`, nada depende de un nombre de carpeta fijo.)

Los scripts dentro de `config/` contienen la lógica de conversión y son reutilizados
directamente por `convert.py` (no hay scripts duplicados ni lanzadores por sistema
operativo).
