# Word to Markdown Converter

Convierte documentos Word (`.docx`) a Markdown preservando imágenes, hipervínculos, tablas y formato.

---

## Uso rápido (ejecutable standalone)

El ejecutable **no requiere Python** instalado. Procesa todos los `.docx` del directorio de entrada
y genera los `.md` en el directorio de salida.

```
word_to_markdown.exe <directorio_entrada> <directorio_salida> [--skip-sections "sección1,sección2"]
```

### Ejemplos

**Conversión básica** (secciones a omitir según `word_to_markdown_config.ini`):
```cmd
word_to_markdown.exe .\input_guide .\output_markdown
```

**Convertir todo sin omitir ninguna sección:**
```cmd
word_to_markdown.exe .\input_guide .\output_markdown --skip-sections "none"
```

**Omitir secciones concretas:**
```cmd
word_to_markdown.exe .\input_guide .\output_markdown --skip-sections "Historia de Versiones,Indice"
```

**Usar rutas absolutas:**
```cmd
word_to_markdown.exe "C:\Documentos\entrada" "C:\Documentos\salida"
```

---

## Ejecución con el lanzador `.bat`

El archivo `convert_docs.bat` usa el ejecutable automáticamente si está presente
y configura las rutas de forma automática. Solo ejecuta:

```cmd
convert_docs.bat
```

---

## Configuración

Edita `word_to_markdown_config.ini` (junto al `.exe`) para definir las secciones
que se omiten por defecto:

```ini
[conversion]
skip_sections = Historia de Versiones, Indice
# skip_sections = none
```

---

## Salida generada

```
output_markdown/
├── documento.md
└── documento_images/
    ├── image_rId11.png
    └── ...
```

---

## Compilar el ejecutable (solo si tienes Python)

```cmd
build_exe.bat
```

Genera `word_to_markdown.exe` en la raíz del proyecto usando PyInstaller.

    ├── image_rId11.png
    ├── image_rId13.png
    └── ...
```

## Requirements

- Python 3.7+
- python-docx>=0.8.11
- Pillow>=9.0.0

## Installation

The `convert_docs.sh` script automatically creates a virtual environment and installs dependencies:

```bash
chmod +x convert_docs.sh
./convert_docs.sh
```

## Manual Installation

If you prefer manual setup:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Troubleshooting

### External Images
External image links (like `cid:image003.png@01D87055.85AFC650`) are automatically skipped and logged.

### Section Detection
The script detects sections by heading levels. If a section isn't being skipped correctly, check that it's formatted as a heading in the Word document.

### Configuration Priority
1. Command line arguments (highest priority)
2. Configuration file (`word_to_markdown_config.ini`)
3. Default configuration (Historia de Versiones, Indice)

## Support

For issues or questions, check the terminal output for detailed error messages and skipped sections information.
