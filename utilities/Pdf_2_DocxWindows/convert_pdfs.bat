@echo off
REM ========================================================
REM  Script de conversión PDF a DOCX
REM  Convierte todos los archivos PDF del directorio de entrada
REM ========================================================

setlocal

REM Configurar directorios por defecto
set "INPUT_DIR=input_pdfs"
set "OUTPUT_DIR=output_docx"

REM Verificar si existe el ejecutable
if exist "pdf_to_docx.exe" (
    echo Usando ejecutable pdf_to_docx.exe
    echo.
    
    REM Crear directorios si no existen
    if not exist "%INPUT_DIR%" mkdir "%INPUT_DIR%"
    if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"
    
    REM Ejecutar la conversión
    pdf_to_docx.exe "%INPUT_DIR%" "%OUTPUT_DIR%"
) else (
    echo ERROR: No se encontró pdf_to_docx.exe
    echo.
    echo Por favor, compila el ejecutable primero ejecutando:
    echo   build_exe.bat
    echo.
    echo O si tienes Python instalado, puedes ejecutar:
    echo   python src\pdf_to_docx.py "%INPUT_DIR%" "%OUTPUT_DIR%"
)

echo.
pause
