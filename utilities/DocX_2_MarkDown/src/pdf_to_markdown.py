#!/usr/bin/env python3
"""
PDF to Markdown Converter
This script converts PDF documents to Markdown format with images and hyperlinks.
"""

import os
import re
import sys
import uuid
import shutil
import traceback
import configparser
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import io

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

def load_config_file(config_path="pdf_to_markdown_config.ini"):
    """Load configuration from INI file if it exists."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_dir, config_path)
    
    skip_sections = DEFAULT_SKIP_SECTIONS.copy()
    extract_images = True
    preserve_links = True
    
    if os.path.exists(config_file_path):
        try:
            config = configparser.ConfigParser()
            config.read(config_file_path)
            
            if 'conversion' in config:
                if 'skip_sections' in config['conversion']:
                    skip_sections_str = config['conversion']['skip_sections']
                    if skip_sections_str.lower() == 'none':
                        skip_sections = []
                    else:
                        skip_sections = [section.strip() for section in skip_sections_str.split(',') if section.strip()]
                
                if 'extract_images' in config['conversion']:
                    extract_images = config['conversion'].getboolean('extract_images')
                
                if 'preserve_links' in config['conversion']:
                    preserve_links = config['conversion'].getboolean('preserve_links')
            
            print(f"Loaded configuration from {config_file_path}")
        except Exception as e:
            print(f"Error reading config file {config_file_path}: {e}")
            print("Using default configuration.")
    
    return skip_sections, extract_images, preserve_links

def should_skip_section(text, skip_sections):
    """Check if a heading text matches any section to skip."""
    if not text or not skip_sections:
        return False
    
    text_clean = text.strip().lower()
    for skip_section in skip_sections:
        if skip_section.lower() in text_clean or text_clean in skip_section.lower():
            return True
    return False

def detect_heading_level(text, font_size, avg_font_size):
    """
    Detect if a text block is a heading based on font size.
    Returns heading level (1-6) or 0 if not a heading.
    """
    if not text or not text.strip():
        return 0
    
    # If font size is significantly larger than average, it's likely a heading
    size_ratio = font_size / avg_font_size if avg_font_size > 0 else 1
    
    if size_ratio >= 1.8:
        return 1
    elif size_ratio >= 1.5:
        return 2
    elif size_ratio >= 1.3:
        return 3
    elif size_ratio >= 1.15:
        return 4
    
    return 0

def extract_images_from_pdf(pdf_document, image_dir, doc_name):
    """Extract all images from the PDF document."""
    image_map = {}
    image_counter = 0
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)
        
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            
            try:
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                image_filename = f"{doc_name}_image_{image_counter}.{image_ext}"
                image_path = os.path.join(image_dir, image_filename)
                
                with open(image_path, "wb") as img_file:
                    img_file.write(image_bytes)
                
                # Store mapping with page and position info
                image_map[f"page_{page_num}_img_{img_index}"] = {
                    'filename': image_filename,
                    'path': os.path.join(os.path.basename(image_dir), image_filename),
                    'xref': xref
                }
                
                image_counter += 1
                print(f"Extracted image: {image_filename}")
            except Exception as e:
                print(f"Error extracting image on page {page_num}: {e}")
                continue
    
    return image_map

def get_average_font_size(pdf_document):
    """Calculate the average font size across the document."""
    font_sizes = []
    
    for page_num in range(min(5, len(pdf_document))):  # Sample first 5 pages
        page = pdf_document[page_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        font_sizes.append(span["size"])
    
    return sum(font_sizes) / len(font_sizes) if font_sizes else 12

def process_text_block(block, avg_font_size, preserve_links=True):
    """Process a text block and convert it to Markdown."""
    markdown = ""
    
    if "lines" not in block:
        return markdown
    
    # Extract text and detect formatting
    block_text = ""
    max_font_size = 0
    has_bold = False
    has_italic = False
    links = []
    
    for line in block["lines"]:
        line_text = ""
        for span in line["spans"]:
            text = span["text"]
            font_size = span["size"]
            font_flags = span.get("flags", 0)
            
            max_font_size = max(max_font_size, font_size)
            
            # Check for bold (bit 4) and italic (bit 1)
            if font_flags & (1 << 4):
                has_bold = True
                text = f"**{text}**"
            if font_flags & (1 << 1):
                has_italic = True
                text = f"*{text}*"
            
            line_text += text
        
        block_text += line_text.strip() + " "
    
    block_text = block_text.strip()
    
    if not block_text:
        return markdown
    
    # Detect if it's a heading
    heading_level = detect_heading_level(block_text, max_font_size, avg_font_size)
    
    if heading_level > 0:
        markdown = f"{'#' * heading_level} {block_text}\n\n"
    else:
        # Detect if it's a list item
        if re.match(r'^[\•\-\*]\s', block_text):
            markdown = f"* {block_text[2:]}\n"
        elif re.match(r'^\d+[\.\)]\s', block_text):
            markdown = f"1. {re.sub(r'^\d+[\.\)]\s', '', block_text)}\n"
        else:
            markdown = f"{block_text}\n\n"
    
    return markdown

def process_pdf_page(page, page_num, image_map, avg_font_size, extract_images=True, preserve_links=True):
    """Process a single PDF page and return Markdown content."""
    markdown = ""
    
    # Get text blocks
    blocks = page.get_text("dict")["blocks"]
    
    # Get images on this page for reference
    page_image_positions = []
    if extract_images:
        image_list = page.get_images(full=True)
        for img_index, img_info in enumerate(image_list):
            img_key = f"page_{page_num}_img_{img_index}"
            if img_key in image_map:
                # Get image position from the page
                try:
                    rects = page.get_image_rects(img_info[0])
                    if rects:
                        page_image_positions.append({
                            'key': img_key,
                            'rect': rects[0],
                            'used': False
                        })
                except:
                    page_image_positions.append({
                        'key': img_key,
                        'rect': None,
                        'used': False
                    })
    
    # Process each block
    for block in blocks:
        if block["type"] == 0:  # Text block
            markdown += process_text_block(block, avg_font_size, preserve_links)
        elif block["type"] == 1 and extract_images:  # Image block
            # Find corresponding image by position
            block_rect = fitz.Rect(block["bbox"])
            best_match = None
            min_distance = float('inf')
            
            for img_pos in page_image_positions:
                if img_pos['used']:
                    continue
                if img_pos['rect']:
                    # Calculate distance between block and image
                    distance = abs(block_rect.x0 - img_pos['rect'].x0) + abs(block_rect.y0 - img_pos['rect'].y0)
                    if distance < min_distance:
                        min_distance = distance
                        best_match = img_pos
                else:
                    # No position info, use first unused
                    best_match = img_pos
                    break
            
            if best_match:
                best_match['used'] = True
                img_data = image_map[best_match['key']]
                img_path = img_data['path'].replace(os.path.sep, '/')
                markdown += f"![image]({img_path})\n\n"
    
    # Add any remaining unused images at the end
    if extract_images:
        for img_pos in page_image_positions:
            if not img_pos['used']:
                img_data = image_map[img_pos['key']]
                img_path = img_data['path'].replace(os.path.sep, '/')
                markdown += f"![image]({img_path})\n\n"
    
    # Extract links if enabled
    if preserve_links:
        links = page.get_links()
        for link in links:
            if "uri" in link:
                markdown += f"\n<!-- Link found: {link['uri']} -->\n"
    
    return markdown

def pdf_to_markdown(pdf_path, output_dir, skip_sections=None, extract_images=True, preserve_links=True):
    """Convert a PDF document to Markdown format with images."""
    if skip_sections is None:
        skip_sections = DEFAULT_SKIP_SECTIONS
    
    try:
        pdf_document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return None
    
    doc_name = Path(pdf_path).stem
    
    # Create image directory
    image_dir_name = f"{doc_name}_images"
    image_dir = os.path.join(output_dir, image_dir_name)
    if extract_images:
        create_dir_if_not_exists(image_dir)
        image_map = extract_images_from_pdf(pdf_document, image_dir, doc_name)
    else:
        image_map = {}
    
    # Calculate average font size for heading detection
    avg_font_size = get_average_font_size(pdf_document)
    
    markdown_path = os.path.join(output_dir, f"{doc_name}.md")
    
    # Build content in memory first
    markdown_content = []
    skip_mode = False
    skip_until_level = 0
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_markdown = process_pdf_page(
            page, page_num, image_map, 
            avg_font_size, extract_images, preserve_links
        )
        
        # Handle section skipping
        lines = page_markdown.split('\n')
        for line in lines:
            # Check for headings to skip
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                heading_level = len(heading_match.group(1))
                heading_text = heading_match.group(2)
                
                if skip_mode and heading_level <= skip_until_level:
                    skip_mode = False
                    skip_until_level = 0
                
                if should_skip_section(heading_text, skip_sections):
                    print(f"Skipping section: '{heading_text}'")
                    skip_mode = True
                    skip_until_level = heading_level
                    continue
            
            if not skip_mode:
                markdown_content.append(line)
    
    # Join all content
    final_content = '\n'.join(markdown_content)
    
    # Write final content to file
    with open(markdown_path, 'w', encoding='utf-8') as md_file:
        md_file.write(final_content)
    
    pdf_document.close()
    print(f"Successfully converted {pdf_path} to {markdown_path}")
    return markdown_path

def main():
    """Main function to process all PDF documents in the input directory."""
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_markdown.py <input_dir> <output_dir> [--skip-sections \"section1,section2\"]")
        print("Example: python pdf_to_markdown.py ./input_guide ./output_markdown")
        print("Example: python pdf_to_markdown.py ./input_guide ./output_markdown --skip-sections \"Historia de Versiones,Indice\"")
        print("Example: python pdf_to_markdown.py ./input_guide ./output_markdown --skip-sections \"none\"")
        print(f"Default skip sections: {DEFAULT_SKIP_SECTIONS}")
        print("\nConfiguration can also be set in 'pdf_to_markdown_config.ini' file.")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    # Load configuration from file first
    skip_sections, extract_images, preserve_links = load_config_file()
    
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
    
    print(f"Extract images: {extract_images}")
    print(f"Preserve links: {preserve_links}")
    
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)
    
    create_dir_if_not_exists(output_dir)
    
    processed_files = 0
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            try:
                pdf_to_markdown(pdf_path, output_dir, skip_sections, extract_images, preserve_links)
                processed_files += 1
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                traceback.print_exc()
    
    print("\n" + "="*50)
    if processed_files == 0:
        print("No PDF documents found to convert.")
    else:
        print(f"Conversion complete. {processed_files} file(s) processed.")

if __name__ == "__main__":
    main()
