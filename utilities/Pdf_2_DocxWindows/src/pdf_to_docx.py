#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF to DOCX Converter
Convierte archivos PDF a formato DOCX preservando el formato y estructura.
"""

import os
import sys
import argparse
from pathlib import Path
from pdf2docx import Converter


def convert_pdf_to_docx(pdf_path, docx_path):
    """
    Convierte un archivo PDF a DOCX.
    
    Args:
        pdf_path: Ruta del archivo PDF de entrada
        docx_path: Ruta del archivo DOCX de salida
        
    Returns:
        bool: True si la conversión fue exitosa, False en caso contrario
    """
    try:
        print(f"  Convirtiendo: {os.path.basename(pdf_path)}")
        
        # Crear el conversor y realizar la conversión
        cv = Converter(pdf_path)
        cv.convert(docx_path)
        cv.close()
        
        print(f"  ✓ Completado: {os.path.basename(docx_path)}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error al convertir {os.path.basename(pdf_path)}: {str(e)}")
        return False


def process_directory(input_dir, output_dir):
    """
    Procesa todos los archivos PDF en el directorio de entrada.
    
    Args:
        input_dir: Directorio con archivos PDF
        output_dir: Directorio para archivos DOCX resultantes
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
        docx_filename = pdf_file.stem + ".docx"
        docx_path = output_path / docx_filename
        
        # Convertir
        if convert_pdf_to_docx(str(pdf_file), str(docx_path)):
            success_count += 1
    
    print("-" * 60)
    print(f"\nConversión completada: {success_count}/{len(pdf_files)} archivos procesados exitosamente.")
    
    if success_count > 0:
        print(f"\nArchivos DOCX generados en: {output_dir}")


def main():
    """Función principal del programa."""
    parser = argparse.ArgumentParser(
        description="Convierte archivos PDF a formato DOCX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  pdf_to_docx.exe .\\input_pdfs .\\output_docx
  pdf_to_docx.exe "C:\\Documentos\\PDFs" "C:\\Documentos\\Word"
        """
    )
    
    parser.add_argument(
        "input_dir",
        help="Directorio que contiene los archivos PDF a convertir"
    )
    
    parser.add_argument(
        "output_dir",
        help="Directorio donde se guardarán los archivos DOCX"
    )
    
    # Si no hay argumentos, mostrar ayuda
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("         PDF to DOCX Converter")
    print("=" * 60)
    
    # Procesar los archivos
    process_directory(args.input_dir, args.output_dir)
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
