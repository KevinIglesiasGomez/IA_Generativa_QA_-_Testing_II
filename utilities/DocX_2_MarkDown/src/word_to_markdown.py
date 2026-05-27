#!/usr/bin/env python3
"""
Word to Markdown Converter
This script converts Word documents to Markdown format with images and hyperlinks.
"""

import os
import re
import sys
import uuid
import shutil
import traceback
import configparser
import xml.etree.ElementTree as ET
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE
from docx.text.paragraph import Paragraph
from docx.table import Table, _Cell

# --- Global Namespace Mappings for XML Parsing ---
ns = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
}

# --- Configuration for sections to skip ---
DEFAULT_SKIP_SECTIONS = [
    "Historia de Versiones",
    "Indice"
]

def create_dir_if_not_exists(path):
    """Create directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def load_config_file(config_path="word_to_markdown_config.ini"):
    """Load configuration from INI file if it exists."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, config_path)
    
    skip_sections = DEFAULT_SKIP_SECTIONS.copy()
    
    if os.path.exists(config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            
            if 'conversion' in config and 'skip_sections' in config['conversion']:
                skip_sections_str = config['conversion']['skip_sections']
                if skip_sections_str.lower() == 'none':
                    skip_sections = []
                else:
                    skip_sections = [section.strip() for section in skip_sections_str.split(',') if section.strip()]
            
            print(f"Loaded configuration from {config_file_path}")
        except Exception as e:
            print(f"Error reading config file {config_file_path}: {e}")
            print("Using default configuration.")
    
    return skip_sections

def should_skip_section(text, skip_sections):
    """Check if a heading text matches any section to skip."""
    if not text or not skip_sections:
        return False
    
    text_clean = text.strip().lower()
    for skip_section in skip_sections:
        if skip_section.lower() in text_clean or text_clean in skip_section.lower():
            return True
    return False

def find_next_heading_level(blocks, current_index, current_level):
    """Find the index of the next heading at the same or higher level."""
    for i in range(current_index + 1, len(blocks)):
        block = blocks[i]
        if isinstance(block, Paragraph):
            block_level = get_heading_level(block)
            if block_level > 0 and block_level <= current_level:
                return i
    return len(blocks)  # Return end of document if no such heading found

def extract_and_save_images(doc, image_dir):
    """Extracts images from the docx and saves them to image_dir."""
    image_map = {}
    for rel in doc.part.rels.values():
        if rel.reltype == RELATIONSHIP_TYPE.IMAGE:
            # Skip external images to avoid errors
            if rel.is_external:
                print(f"Skipping external image link: {rel.target_ref}")
                continue
            
            try:
                image_data = rel.target_part.blob
                image_filename = f"image_{rel.rId}{Path(rel.target_ref).suffix}"
                image_path = os.path.join(image_dir, image_filename)
                
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data)
                
                image_map[rel.rId] = os.path.join(os.path.basename(image_dir), image_filename)
                print(f"Extracted image: {image_filename}")
            except Exception as e:
                print(f"Skipping image {rel.rId} due to error: {e}")
                continue
    return image_map

def get_hyperlink_url(paragraph, rel_id):
    """Get hyperlink URL from a relationship ID."""
    try:
        return paragraph.part.rels[rel_id].target_ref
    except (KeyError, AttributeError):
        # Fallback for different document structures
        try:
            return paragraph.document.part.rels[rel_id].target_ref
        except (KeyError, AttributeError):
            return None

def get_heading_level(paragraph):
    """Determine the heading level of a paragraph."""
    style_name = paragraph.style.name
    if style_name.startswith('Heading'):
        try:
            return int(style_name.split(' ')[-1])
        except (ValueError, IndexError):
            return 0
    return 0

def get_list_info(paragraph):
    """Get list type and level of a paragraph if it's a list item."""
    # Check if the paragraph style indicates it's a list
    if paragraph.style.name.startswith('List Paragraph'):
        return "unordered", 1
    
    # Check for numbered list styles
    if any(style_name in paragraph.style.name.lower() for style_name in ['list number', 'numbered']):
        return "ordered", 1
    
    # Check for bullet list styles
    if any(style_name in paragraph.style.name.lower() for style_name in ['list bullet', 'bullet']):
        return "unordered", 1
    
    # Try to check paragraph numbering properties (if available)
    try:
        p_element = paragraph._p
        numPr = p_element.find('.//w:numPr', ns)
        if numPr is not None:
            # This is a numbered paragraph
            ilvl_elem = numPr.find('.//w:ilvl', ns)
            level = 1
            if ilvl_elem is not None:
                level = int(ilvl_elem.get(qn('w:val'), 0)) + 1
            return "ordered", level
    except Exception:
        pass
    
    return None, 0

def _get_image_and_hyperlink_info(paragraph, image_map):
    """Extracts image and hyperlink data from a paragraph's XML."""
    p_element = paragraph._p
    hyperlinks = {}
    images = []

    # First, find all hyperlinks and their associated runs
    for h_link in p_element.findall('.//w:hyperlink', ns):
        rel_id = h_link.get(qn('r:id'))
        if rel_id:
            url = get_hyperlink_url(paragraph, rel_id)
            if url:
                # Store URL by hyperlink element to handle nested content
                hyperlinks[h_link] = url
                # Check for images directly within this hyperlink
                for drawing in h_link.findall('.//w:drawing', ns):
                    for blip in drawing.findall('.//a:blip', ns):
                        embed_id = blip.get(qn('r:embed'))
                        if embed_id and embed_id in image_map:
                            image_path = image_map[embed_id].replace(os.path.sep, '/')
                            images.append({'path': image_path, 'url': url, 'hyperlink_el': h_link})

    # Find all images, including those not in hyperlinks
    for drawing in p_element.findall('.//w:drawing', ns):
        # Skip drawings already processed within a hyperlink
        is_in_hyperlink = any(h for h in hyperlinks if drawing in h)
        if is_in_hyperlink:
            continue

        for blip in drawing.findall('.//a:blip', ns):
            embed_id = blip.get(qn('r:embed'))
            if embed_id and embed_id in image_map:
                # Check if this image has already been added (as part of a hyperlink)
                if not any(img['path'] == image_map[embed_id].replace(os.path.sep, '/') for img in images):
                    image_path = image_map[embed_id].replace(os.path.sep, '/')
                    images.append({'path': image_path, 'url': None})
    
    return hyperlinks, images

def process_paragraph(paragraph, image_map):
    """Processes a single paragraph and returns its Markdown representation."""
    
    # Handle headings first
    heading_level = get_heading_level(paragraph)
    if heading_level > 0:
        return f"{'#' * heading_level} {paragraph.text.strip()}\n\n"

    # Handle lists
    list_type, _ = get_list_info(paragraph)
    if list_type == "unordered":
        return f"* {paragraph.text.strip()}\n"
    if list_type == "ordered":
        return f"1. {paragraph.text.strip()}\n" # Simplified ordered list

    hyperlinks, images = _get_image_and_hyperlink_info(paragraph, image_map)
    
    # If the paragraph only contains images, format them and return
    if not paragraph.text.strip() and images:
        md = ""
        for img in images:
            if img['url']:
                md += f"[![image]({img['path']})]({img['url']})\n"
            else:
                md += f"![image]({img['path']})\n"
        return md + "\n" if md else ""

    # Process paragraphs with text, potentially with hyperlinks
    md = ""
    # Group consecutive runs within the same hyperlink
    in_hyperlink = False
    hyperlink_text = ""
    hyperlink_url = ""

    for run in paragraph.runs:
        run_md = run.text
        
        # Apply bold, italic, underline
        if run.bold: run_md = f"**{run_md}**"
        if run.italic: run_md = f"*{run_md}*"
        if run.underline: run_md = f"__{run_md}__"

        # Check if the run is inside a hyperlink
        run_hyperlink_el = None
        for h_link in hyperlinks:
            if run._r in h_link.findall('.//w:r', ns):
                run_hyperlink_el = h_link
                break
        
        if run_hyperlink_el is not None:
            current_url = hyperlinks[run_hyperlink_el]
            if in_hyperlink and current_url == hyperlink_url:
                hyperlink_text += run_md
            else:
                # End previous hyperlink if any
                if in_hyperlink:
                    md += f"[{hyperlink_text}]({hyperlink_url})"
                
                # Start new hyperlink
                in_hyperlink = True
                hyperlink_url = current_url
                hyperlink_text = run_md
        else:
            # If we were in a hyperlink, close it
            if in_hyperlink:
                md += f"[{hyperlink_text}]({hyperlink_url})"
                in_hyperlink = False
                hyperlink_text = ""
                hyperlink_url = ""
            
            md += run_md

    # Close any remaining open hyperlink
    if in_hyperlink:
        md += f"[{hyperlink_text}]({hyperlink_url})"

    # Add any non-hyperlinked images found in the paragraph
    # This handles cases where images are mixed with text but not linked.
    # Note: The _get_image_and_hyperlink_info function already handles linked images.
    if images:
        img_md = ""
        for img in images:
            if not img.get('url'): # Only add non-linked images here
                img_md += f"\n![image]({img['path']})\n"
        # Add image markdown after the text content
        md += img_md

    return md.strip() + "\n\n" if md.strip() else ""

def process_table(table, image_map):
    """Processes a table and returns its Markdown representation."""
    md = ""
    
    # Header
    header_cells = [cell.text.strip() for cell in table.rows[0].cells]
    md += f"| {' | '.join(header_cells)} |\n"
    
    # Separator
    md += f"|{'|'.join(['---'] * len(header_cells))}|\n"
    
    # Body
    for row in table.rows[1:]:
        row_md = []
        for cell in row.cells:
            cell_content = ""
            for p in cell.paragraphs:
                cell_content += process_paragraph(p, image_map).strip() + " "
            row_md.append(cell_content.strip())
        md += f"| {' | '.join(row_md)} |\n"
        
    return md + "\n"

def docx_to_markdown(docx_path, output_dir, skip_sections=None):
    """Convert a Word document to Markdown format with images."""
    if skip_sections is None:
        skip_sections = DEFAULT_SKIP_SECTIONS
    
    doc = Document(docx_path)
    doc_name = Path(docx_path).stem
    
    image_dir_name = f"{doc_name}_images"
    image_dir = os.path.join(output_dir, image_dir_name)
    create_dir_if_not_exists(image_dir)
    
    image_map = extract_and_save_images(doc, image_dir)
    
    markdown_path = os.path.join(output_dir, f"{doc_name}.md")
    
    # Convert document blocks to a list for easier navigation
    blocks = list(iter_block_items(doc))
    
    with open(markdown_path, 'w', encoding='utf-8') as md_file:
        i = 0
        while i < len(blocks):
            block = blocks[i]
            
            if isinstance(block, Paragraph):
                # Check if this is a heading we should skip
                heading_level = get_heading_level(block)
                if heading_level > 0 and should_skip_section(block.text, skip_sections):
                    print(f"Skipping section: '{block.text.strip()}'")
                    # Find the next heading at the same or higher level
                    next_heading_index = find_next_heading_level(blocks, i, heading_level)
                    # Skip all blocks until the next heading
                    i = next_heading_index
                    continue
                
                md_file.write(process_paragraph(block, image_map))
            elif isinstance(block, Table):
                md_file.write(process_table(block, image_map))
            
            i += 1

    print(f"Successfully converted {docx_path} to {markdown_path}")
    return markdown_path

def iter_block_items(parent):
    """
    Generate a sequence of paragraph and table objects in document order.
    `parent` can be a Document object or a _Cell object.
    """
    # Check if parent is a Document by checking if it has an element attribute and body
    if hasattr(parent, 'element') and hasattr(parent.element, 'body'):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("Unsupported parent type")

    for child in parent_elm.iterchildren():
        if child.tag.endswith('p'):
            yield Paragraph(child, parent)
        elif child.tag.endswith('tbl'):
            yield Table(child, parent)

def main():
    """Main function to process all Word documents in the input directory."""
    if len(sys.argv) < 3:
        print("Usage: python word_to_markdown.py <input_dir> <output_dir> [--skip-sections \"section1,section2\"]")
        print("Example: python word_to_markdown.py ./input_guide ./output_markdown")
        print("Example: python word_to_markdown.py ./input_guide ./output_markdown --skip-sections \"Historia de Versiones,Indice\"")
        print("Example: python word_to_markdown.py ./input_guide ./output_markdown --skip-sections \"none\"")
        print(f"Default skip sections: {DEFAULT_SKIP_SECTIONS}")
        print("\nConfiguration can also be set in 'word_to_markdown_config.ini' file.")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Load configuration from file first
    skip_sections = load_config_file()
    
    # Parse skip sections argument (command line overrides config file)
    if len(sys.argv) >= 5 and sys.argv[3] == "--skip-sections":
        skip_sections_arg = sys.argv[4]
        if skip_sections_arg.lower() == "none":
            skip_sections = []
        else:
            skip_sections = [section.strip() for section in skip_sections_arg.split(",") if section.strip()]
        print("Using command-line skip sections configuration.")
    
    if skip_sections:
        print(f"Configured to skip sections: {skip_sections}")
    else:
        print("No sections will be skipped.")
    
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)
    
    create_dir_if_not_exists(output_dir)
    
    processed_files = 0
    for filename in os.listdir(input_dir):
        if filename.endswith(".docx") and not filename.startswith("~"):
            docx_path = os.path.join(input_dir, filename)
            try:
                docx_to_markdown(docx_path, output_dir, skip_sections)
                processed_files += 1
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                traceback.print_exc()
    
    print("\n" + "="*50)
    if processed_files == 0:
        print("No Word documents found to convert.")
    else:
        print(f"Conversion complete. {processed_files} file(s) processed.")

if __name__ == "__main__":
    main()
