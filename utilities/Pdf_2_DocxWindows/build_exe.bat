@echo off
REM ========================================================
REM  Script de compilación con PyInstaller
REM  Genera pdf_to_docx.exe ejecutable standalone
REM ========================================================

echo ========================================================
echo   Compilando PDF to DOCX Converter
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
python -m pip install -r requirements.txt

echo.
echo [2/4] Instalando PyInstaller...
python -m pip install pyinstaller

echo.
echo [3/4] Compilando ejecutable...
python -m PyInstaller --onefile ^
    --name pdf_to_docx ^
    --console ^
    --clean ^
    --hidden-import=pdf2docx ^
    --collect-all pdf2docx ^
    src\pdf_to_docx.py

echo.
echo [4/4] Limpiando archivos temporales...
if exist "pdf_to_docx.spec" del "pdf_to_docx.spec"

REM Copiar ejecutable a la raíz del proyecto
if exist "dist\pdf_to_docx.exe" (
    copy /Y "dist\pdf_to_docx.exe" "pdf_to_docx.exe"
    echo.
    echo ========================================================
    echo   ¡Compilación exitosa!
    echo   Ejecutable generado: pdf_to_docx.exe
    echo ========================================================
) else (
    echo.
    echo ========================================================
    echo   ERROR: No se pudo generar el ejecutable
    echo ========================================================
)

echo.
pause
