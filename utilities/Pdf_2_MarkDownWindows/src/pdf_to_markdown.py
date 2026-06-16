#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF to Markdown Converter
Convierte archivos PDF a formato Markdown preservando el formato y estructura.
"""

import os
import sys
import argparse
from pathlib import Path
import fitz  # PyMuPDF
import re


def extract_images_from_page(page, output_dir, pdf_name, page_num):
    """
    Extrae las imágenes de una página del PDF.
    
    Args:
        page: Página del PDF
        output_dir: Directorio donde guardar las imágenes
        pdf_name: Nombre del PDF (sin extensión)
        page_num: Número de página
        
    Returns:
        list: Lista de rutas de las imágenes extraídas
    """
    images = []
    image_list = page.get_images()
    
    for img_index, img in enumerate(image_list):
        try:
            xref = img[0]
            base_image = page.parent.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Crear directorio para las imágenes si no existe
            images_dir = output_dir / f"{pdf_name}_images"
            images_dir.mkdir(parents=True, exist_ok=True)
            
            # Guardar la imagen
            image_filename = f"image_p{page_num}_i{img_index}.{image_ext}"
            image_path = images_dir / image_filename
            
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            
            # Ruta relativa para el markdown
            relative_path = f"{pdf_name}_images/{image_filename}"
            images.append(relative_path)
            
        except Exception as e:
            print(f"    Advertencia: No se pudo extraer imagen {img_index} de la página {page_num}: {str(e)}")
    
    return images


def clean_text(text):
    """
    Limpia el texto extraído del PDF.
    
    Args:
        text: Texto a limpiar
        
    Returns:
        str: Texto limpio
    """
    # Eliminar saltos de línea innecesarios dentro de párrafos
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    
    # Normalizar espacios múltiples
    text = re.sub(r' +', ' ', text)
    
    # Normalizar saltos de línea múltiples
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


def detect_heading(text, font_size, avg_font_size):
    """
    Detecta si un bloque de texto es un encabezado basándose en el tamaño de fuente.
    
    Args:
        text: Texto del bloque
        font_size: Tamaño de fuente del bloque
        avg_font_size: Tamaño de fuente promedio del documento
        
    Returns:
        str: Nivel de encabezado markdown o texto normal
    """
    if font_size > avg_font_size * 1.5:
        return f"# {text.strip()}"
    elif font_size > avg_font_size * 1.3:
        return f"## {text.strip()}"
    elif font_size > avg_font_size * 1.1:
        return f"### {text.strip()}"
    else:
        return text


def convert_pdf_to_markdown(pdf_path, md_path, output_dir):
    """
    Convierte un archivo PDF a Markdown.
    
    Args:
        pdf_path: Ruta del archivo PDF de entrada
        md_path: Ruta del archivo Markdown de salida
        output_dir: Directorio de salida para imágenes
        
    Returns:
        bool: True si la conversión fue exitosa, False en caso contrario
    """
    try:
        print(f"  Convirtiendo: {os.path.basename(pdf_path)}")
        
        # Abrir el PDF
        doc = fitz.open(pdf_path)
        pdf_name = Path(pdf_path).stem
        
        markdown_content = []
        markdown_content.append(f"# {pdf_name}\n\n")
        markdown_content.append(f"*Documento convertido desde PDF*\n\n")
        markdown_content.append("---\n\n")
        
        # Procesar cada página
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            # Extraer el texto
            text = page.get_text()
            
            if text.strip():
                # Limpiar el texto
                clean = clean_text(text)
                markdown_content.append(clean)
                markdown_content.append("\n\n")
            
            # Extraer imágenes
            images = extract_images_from_page(page, output_dir, pdf_name, page_num + 1)
            
            for img_path in images:
                markdown_content.append(f"![Image]({img_path})\n\n")
            
            # Agregar separador de página (opcional)
            if page_num < len(doc) - 1:
                markdown_content.append(f"---\n\n")
                markdown_content.append(f"*Página {page_num + 2}*\n\n")
        
        # Cerrar el documento
        doc.close()
        
        # Escribir el archivo Markdown
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"  ✓ Completado: {os.path.basename(md_path)}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error al convertir {os.path.basename(pdf_path)}: {str(e)}")
        return False


def process_directory(input_dir, output_dir):
    """
    Procesa todos los archivos PDF en el directorio de entrada.
    
    Args:
        input_dir: Directorio con archivos PDF
        output_dir: Directorio para archivos Markdown resultantes
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Verificar que el directorio de entrada existe
    if not input_path.exists():
        print(f"Error: El directorio de entrada '{input_dir}' no existe.")
        return
    
    # Crear directorio de salida si no existe
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Buscar todos los archivos PDF
    pdf_files = list(input_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No se encontraron archivos PDF en '{input_dir}'")
        return
    
    print(f"\nEncontrados {len(pdf_files)} archivo(s) PDF")
    print(f"Directorio de salida: {output_dir}\n")
    print("-" * 60)
    
    # Procesar cada archivo PDF
    success_count = 0
    for pdf_file in pdf_files:
        # Crear nombre del archivo de salida
        md_filename = pdf_file.stem + ".md"
        md_path = output_path / md_filename
        
        # Convertir
        if convert_pdf_to_markdown(str(pdf_file), str(md_path), output_path):
            success_count += 1
    
    print("-" * 60)
    print(f"\nConversión completada: {success_count}/{len(pdf_files)} archivos procesados exitosamente.")
    
    if success_count > 0:
        print(f"\nArchivos Markdown generados en: {output_dir}")


def main():
    """Función principal del programa."""
    parser = argparse.ArgumentParser(
        description="Convierte archivos PDF a formato Markdown (.md)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  pdf_to_markdown.exe .\\input_pdfs .\\output_markdown
  pdf_to_markdown.exe "C:\\Documentos\\PDFs" "C:\\Documentos\\Markdown"
        """
    )
    
    parser.add_argument(
        "input_dir",
        help="Directorio que contiene los archivos PDF a convertir"
    )
    
    parser.add_argument(
        "output_dir",
        help="Directorio donde se guardarán los archivos Markdown"
    )
    
    # Si no hay argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("         PDF to Markdown Converter")
    print("=" * 60)
    
    # Procesar los archivos
    process_directory(args.input_dir, args.output_dir)
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
