@echo off
REM ========================================================
REM  Script de compilación con PyInstaller
REM  Genera pdf_to_markdown.exe ejecutable standalone
REM ========================================================

echo ========================================================
echo   Compilando PDF to Markdown Converter
echo ========================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor, instala Python desde https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Instalando dependencias...
pip install -r requirements.txt

echo.
echo [2/4] Instalando PyInstaller...
pip install pyinstaller

echo.
echo [3/4] Compilando ejecutable...
pyinstaller --onefile ^
    --name pdf_to_markdown ^
    --console ^
    --clean ^
    --hidden-import=fitz ^
    --collect-all fitz ^
    --collect-all PyMuPDF ^
    src\pdf_to_markdown.py

echo.
echo [4/4] Limpiando archivos temporales...
if exist "pdf_to_markdown.spec" del "pdf_to_markdown.spec"

REM Copiar ejecutable a la raíz del proyecto
if exist "dist\pdf_to_markdown.exe" (
    copy /Y "dist\pdf_to_markdown.exe" "pdf_to_markdown.exe"
    echo.
    echo ========================================================
    echo   ¡Compilación exitosa!
    echo   Ejecutable generado: pdf_to_markdown.exe
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   ERROR: No se pudo generar el ejecutable
    echo ========================================================
)

echo.
pause
