#!/bin/bash
# Shell script to convert PDF documents to Markdown
# Usage: ./convert_pdf.sh [input_dir] [output_dir]

# Set default directories
INPUT_DIR="${1:-input_guide}"
OUTPUT_DIR="${2:-output_markdown}"

echo "========================================"
echo "PDF to Markdown Converter"
echo "========================================"
echo "Input directory: $INPUT_DIR"
echo "Output directory: $OUTPUT_DIR"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r src/requirements_pdf.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Run the conversion script
echo "Running PDF to Markdown converter..."
python src/pdf_to_markdown.py "$INPUT_DIR" "$OUTPUT_DIR"

# Deactivate virtual environment
deactivate

echo "========================================"
echo "Conversion complete!"
echo "========================================"
