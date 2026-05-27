#!/bin/bash

# Install required packages if not already installed
cd src

# Create virtual environment with a shorter path name to avoid path length limitations
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

# Run the Word to Markdown converter
# Configuration is loaded from word_to_markdown_config.ini
# You can override with command line arguments:
# python word_to_markdown.py ../input_guide ../output_markdown --skip-sections "none"
# python word_to_markdown.py ../input_guide ../output_markdown --skip-sections "Historia de Versiones,Indice,Referencias"

python word_to_markdown.py ../input_guide ../output_markdown
