# Document to Markdown Converter

This project converts documents (Word .docx and PDF .pdf) to Markdown format while preserving images, hyperlinks, tables, and formatting.

## Features

- ✅ Converts Word documents (.docx) to clean Markdown format
- ✅ Converts PDF documents (.pdf) to clean Markdown format
- ✅ Extracts and links embedded images
- ✅ Preserves hyperlinks, tables, and basic formatting (bold, italic, underline)
- ✅ Handles headings and list structures
- ✅ **Configurable section skipping** - Skip unwanted sections like "Historia de Versiones" or "Indice"
- ✅ Skips external image links gracefully
- ✅ Batch processing of multiple documents
- ✅ Automatic font size-based heading detection (PDF)

## Quick Start

### For Word Documents

1. Place your Word documents in the `input_guide/` folder
2. Run the conversion script:
   ```bash
   ./convert_docs.sh
   # or on Windows:
   convert_docs_w.bat
   ```
3. Find your converted Markdown files in `output_markdown/`

### For PDF Documents

1. Place your PDF documents in the `input_guide/` folder
2. Run the conversion script:
   ```bash
   ./convert_pdf.sh
   # or on Windows:
   convert_pdf.bat
   ```
3. Find your converted Markdown files in `output_markdown/`

## Configuration Options

### Word Documents

#### 1. Configuration File (Recommended)

Edit `src/word_to_markdown_config.ini` to configure which sections to skip:

```ini
[conversion]
# Sections to skip during conversion (comma-separated list)
skip_sections = Historia de Versiones, Indice

# Other examples:
# skip_sections = Historia de Versiones, Indice, Referencias
# skip_sections = none
# skip_sections = Table of Contents, Version History, Index
```

#### 2. Command Line Arguments

You can override the configuration file with command line arguments:

```bash
# Skip default sections (Historia de Versiones, Indice)
python word_to_markdown.py input_guide output_markdown

# Skip no sections
python word_to_markdown.py input_guide output_markdown --skip-sections "none"

# Skip custom sections
python word_to_markdown.py input_guide output_markdown --skip-sections "Historia de Versiones,Referencias,Anexos"
```

### PDF Documents

#### 1. Configuration File (Recommended)

Edit `src/pdf_to_markdown_config.ini` to configure conversion options:

```ini
[conversion]
# Sections to skip during conversion (comma-separated list)
skip_sections = Historia de Versiones, Indice

# Extract images from PDF (true/false)
extract_images = true

# Preserve hyperlinks from PDF (true/false)
preserve_links = true
```

#### 2. Command Line Arguments

```bash
# Skip default sections
python pdf_to_markdown.py input_guide output_markdown

# Skip no sections
python pdf_to_markdown.py input_guide output_markdown --skip-sections "none"

# Skip custom sections
python pdf_to_markdown.py input_guide output_markdown --skip-sections "Historia de Versiones,Referencias"
```

## Usage Examples

### Word Documents

#### Basic Usage
```bash
cd src
source .venv/bin/activate
python word_to_markdown.py ../input_guide ../output_markdown
```

#### Skip No Sections
```bash
python word_to_markdown.py ../input_guide ../output_markdown --skip-sections "none"
```

#### Custom Section Skipping
```bash
python word_to_markdown.py ../input_guide ../output_markdown --skip-sections "Historia de Versiones,Indice,Referencias"
```

### PDF Documents

#### Basic Usage
```bash
cd src
source .venv/bin/activate
python pdf_to_markdown.py ../input_guide ../output_markdown
```

#### Skip No Sections
```bash
python pdf_to_markdown.py ../input_guide ../output_markdown --skip-sections "none"
```

#### Custom Section Skipping
```bash
python pdf_to_markdown.py ../input_guide ../output_markdown --skip-sections "Historia de Versiones,Referencias"
```

## Output Structure

```
output_markdown/
├── document_name.md                    # Converted Markdown file
└── document_name_images/              # Extracted images folder
    ├── image_rId11.png
    ├── image_rId13.png
    └── ...
```

## Requirements

### Word Documents
- Python 3.7+
- python-docx>=0.8.11
- Pillow>=9.0.0

### PDF Documents
- Python 3.7+
- PyMuPDF>=1.23.0
- Pillow>=9.0.0

## Installation

### For Word Documents

The `convert_docs.sh` (or `convert_docs_w.bat` on Windows) script automatically creates a virtual environment and installs dependencies:

```bash
chmod +x convert_docs.sh
./convert_docs.sh
```

### For PDF Documents

The `convert_pdf.sh` (or `convert_pdf.bat` on Windows) script automatically creates a virtual environment and installs dependencies:

```bash
chmod +x convert_pdf.sh
./convert_pdf.sh
```

## Manual Installation

If you prefer manual setup:

### For Word Documents
```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### For PDF Documents
```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_pdf.txt
```

## Troubleshooting

### Word Documents

#### External Images
External image links (like `cid:image003.png@01D87055.85AFC650`) are automatically skipped and logged.

#### Section Detection
The script detects sections by heading levels. If a section isn't being skipped correctly, check that it's formatted as a heading in the Word document.

### PDF Documents

#### Heading Detection
PDF heading detection is based on font size analysis. The script automatically calculates the average font size and identifies headings based on significantly larger font sizes.

#### Image Quality
Images are extracted in their original format and quality from the PDF. If images appear blurry, they may have been compressed in the original PDF.

#### Complex Layouts
PDFs with complex multi-column layouts or embedded forms may not convert perfectly. Simple text-based PDFs work best.

### General

#### Configuration Priority
1. Command line arguments (highest priority)
2. Configuration file (`.ini` file)
3. Default configuration (Historia de Versiones, Indice)

## Support

For issues or questions, check the terminal output for detailed error messages and skipped sections information.
