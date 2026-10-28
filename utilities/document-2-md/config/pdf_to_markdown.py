#!/usr/bin/env python3
"""
PDF to Markdown Converter
This script converts PDF documents to Markdown format with images and hyperlinks.
"""

import os
import re
import sys
import shutil
import hashlib
import traceback
import configparser
from collections import Counter, defaultdict
from pathlib import Path
import fitz  # PyMuPDF

# --- Configuration for sections to skip ---
DEFAULT_SKIP_SECTIONS = [
    "Historia de Versiones",
    "Indice"
]

# --- Configuration for repeated header/footer detection ---
HEADER_ZONE_RATIO = 0.15  # top % of the page height considered a header
FOOTER_ZONE_RATIO = 0.10  # bottom % of the page height considered a footer
BOILERPLATE_MIN_PAGES_RATIO = 0.4  # a line/image must repeat on this share of pages...
BOILERPLATE_MIN_PAGES_COUNT = 3    # ...or at least this many pages, to count as boilerplate

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

def get_block_plain_text(block):
    """Plain-text content of a text block, ignoring bold/italic markup."""
    if "lines" not in block:
        return ""
    parts = []
    for line in block["lines"]:
        parts.append("".join(span["text"] for span in line["spans"]).strip())
    return " ".join(p for p in parts if p).strip()

def normalize_boilerplate_text(text):
    """Collapse page numbers/whitespace so a repeated header/footer compares equal across pages."""
    normalized = re.sub(r'\d+', '#', text)
    normalized = re.sub(r'\s+', ' ', normalized).strip().lower()
    return normalized

def is_in_header_or_footer_zone(bbox, page_height):
    """Whether a block's bbox lies in the top/bottom margin where running headers/footers live."""
    y0, y1 = bbox[1], bbox[3]
    in_header = y1 <= page_height * HEADER_ZONE_RATIO
    in_footer = y0 >= page_height * (1 - FOOTER_ZONE_RATIO)
    return in_header or in_footer

def detect_boilerplate_lines(pdf_document):
    """Find text lines that repeat in the header/footer margin of most pages
    (e.g. 'Company Name - Confidential', 'Page 3'), so they can be stripped later.
    """
    counts = Counter()
    num_pages = len(pdf_document)
    
    for page in pdf_document:
        page_height = page.rect.height
        seen_on_page = set()
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue
            if not is_in_header_or_footer_zone(block["bbox"], page_height):
                continue
            
            normalized = normalize_boilerplate_text(get_block_plain_text(block))
            if normalized and normalized not in seen_on_page:
                counts[normalized] += 1
                seen_on_page.add(normalized)
    
    min_pages = max(BOILERPLATE_MIN_PAGES_COUNT, int(num_pages * BOILERPLATE_MIN_PAGES_RATIO))
    return {text for text, count in counts.items() if count >= min_pages}

def detect_boilerplate_image_hashes(pdf_document):
    """Find images (by content hash) that repeat across most pages, e.g. a logo or
    decorative bar placed on every page's header/footer.
    """
    hashes_per_page = defaultdict(set)
    
    for page_num, page in enumerate(pdf_document):
        for img_info in page.get_images(full=True):
            try:
                image_bytes = pdf_document.extract_image(img_info[0])["image"]
            except Exception:
                continue
            hashes_per_page[page_num].add(hashlib.md5(image_bytes).hexdigest())
    
    hash_counts = Counter()
    for hashes_on_page in hashes_per_page.values():
        hash_counts.update(hashes_on_page)
    
    num_pages = len(pdf_document)
    min_pages = max(BOILERPLATE_MIN_PAGES_COUNT, int(num_pages * BOILERPLATE_MIN_PAGES_RATIO))
    return {h for h, count in hash_counts.items() if count >= min_pages}

def extract_images_from_pdf(pdf_document, image_dir, doc_name, boilerplate_hashes=None):
    """Extract all images from the PDF document, skipping repeated header/footer images."""
    boilerplate_hashes = boilerplate_hashes or set()
    image_map = {}
    image_counter = 0
    skipped_count = 0
    
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        image_list = page.get_images(full=True)
        
        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]
            
            try:
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                if hashlib.md5(image_bytes).hexdigest() in boilerplate_hashes:
                    skipped_count += 1
                    continue
                
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
    
    if skipped_count:
        print(f"Skipped {skipped_count} repeated header/footer image(s).")
    
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

def clean_table_cell(cell):
    """Normalize a raw table cell into a single-line, table-safe string."""
    if cell is None:
        return ""
    text = str(cell).strip()
    text = text.replace("|", "\\|")  # avoid breaking the table syntax
    text = re.sub(r'\s*\n\s*', '<br>', text)  # multi-line cells -> explicit line break
    return text

def table_to_markdown(table):
    """Render a detected table as a GitHub-flavored Markdown table.
    
    Built manually from extract() instead of PyMuPDF's to_markdown(), which
    double-escapes characters like "-" (e.g. "Item-42" -> "Item&amp;#45;42").
    """
    rows = table.extract()
    rows = [row for row in rows if any(cell not in (None, "") for cell in row)]
    if not rows:
        return None
    
    col_count = max(len(row) for row in rows)
    
    def build_row(row):
        cells = [clean_table_cell(c) for c in row] + [""] * (col_count - len(row))
        return "| " + " | ".join(cells) + " |"
    
    lines = [build_row(rows[0]), "|" + "|".join([" --- "] * col_count) + "|"]
    lines.extend(build_row(row) for row in rows[1:])
    
    return "\n".join(lines)

def detect_tables(page):
    """Detect tables on a page and return their bbox plus rendered Markdown."""
    tables_info = []
    try:
        found_tables = page.find_tables()
    except Exception as e:
        print(f"Warning: table detection failed on page {page.number}: {e}")
        return tables_info
    
    for table in found_tables.tables:
        try:
            table_markdown = table_to_markdown(table)
        except Exception as e:
            print(f"Warning: could not render table on page {page.number}: {e}")
            continue
        
        if not table_markdown:
            continue
        
        tables_info.append({
            'bbox': fitz.Rect(table.bbox),
            'markdown': table_markdown.strip() + "\n\n"
        })
    
    return tables_info

def rect_overlap_ratio(block_rect, table_rect):
    """Fraction of block_rect's area that falls inside table_rect."""
    block_area = block_rect.get_area()
    if block_area <= 0:
        return 0.0
    intersection = block_rect & table_rect
    if intersection.is_empty:
        return 0.0
    return intersection.get_area() / block_area

def process_pdf_page(page, page_num, image_map, avg_font_size, extract_images=True, preserve_links=True, boilerplate_lines=None):
    """Process a single PDF page and return Markdown content."""
    markdown = ""
    boilerplate_lines = boilerplate_lines or set()
    page_height = page.rect.height
    
    # Get text blocks
    blocks = page.get_text("dict")["blocks"]
    
    # Detect tables so their cells render as real Markdown tables instead of flattened text
    tables_info = detect_tables(page)
    emitted_tables = set()
    
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
        block_rect = fitz.Rect(block["bbox"])
        
        # If the block sits mostly inside a detected table, emit the table once and skip the raw block
        table_index = next(
            (i for i, t in enumerate(tables_info) if rect_overlap_ratio(block_rect, t['bbox']) > 0.5),
            None
        )
        if table_index is not None:
            if table_index not in emitted_tables:
                markdown += tables_info[table_index]['markdown']
                emitted_tables.add(table_index)
            continue
        
        if block["type"] == 0:  # Text block
            # Skip running headers/footers repeated across most pages (e.g. "Company Name - Confidential")
            if boilerplate_lines and is_in_header_or_footer_zone(block["bbox"], page_height):
                normalized = normalize_boilerplate_text(get_block_plain_text(block))
                if normalized in boilerplate_lines:
                    continue
            markdown += process_text_block(block, avg_font_size, preserve_links)
        elif block["type"] == 1 and extract_images:  # Image block
            # Find corresponding image by position
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
    
    # Create image directory (clear it first so re-runs don't leave orphaned files behind)
    image_dir_name = f"{doc_name}_images"
    image_dir = os.path.join(output_dir, image_dir_name)
    if extract_images:
        if os.path.exists(image_dir):
            shutil.rmtree(image_dir)
        create_dir_if_not_exists(image_dir)
        boilerplate_hashes = detect_boilerplate_image_hashes(pdf_document)
        image_map = extract_images_from_pdf(pdf_document, image_dir, doc_name, boilerplate_hashes)
    else:
        image_map = {}
    
    # Detect repeated header/footer text lines so they aren't duplicated on every page
    boilerplate_lines = detect_boilerplate_lines(pdf_document)
    if boilerplate_lines:
        print(f"Detected {len(boilerplate_lines)} repeated header/footer line(s) to strip.")
    
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
            avg_font_size, extract_images, preserve_links,
            boilerplate_lines
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
