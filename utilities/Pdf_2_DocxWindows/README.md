# PDF to DOCX Converter

Aplicación ejecutable para Windows que convierte archivos PDF a formato DOCX (Microsoft Word) preservando el formato, estructura y contenido.

---

## Características

- **Conversión por lotes**: Procesa múltiples archivos PDF automáticamente
- **Preservación de formato**: Mantiene texto, tablas, imágenes y estructura
- **Ejecutable standalone**: No requiere Python instalado
- **Interfaz simple**: Uso mediante línea de comandos o scripts .bat
- **Multiplataforma**: Desarrollado en Python, ejecutable para Windows

---

## Uso rápido (ejecutable standalone)

El ejecutable **no requiere Python** instalado. Procesa todos los `.pdf` del directorio de entrada
y genera los `.docx` en el directorio de salida.

```cmd
pdf_to_docx.exe <directorio_entrada> <directorio_salida>
```

### Ejemplos de uso

**Conversión básica:**
```cmd
pdf_to_docx.exe .\input_pdfs .\output_docx
```

**Usar rutas absolutas:**
```cmd
pdf_to_docx.exe "C:\Documentos\PDFs" "C:\Documentos\Word"
```

**Convertir PDFs de una carpeta específica:**
```cmd
pdf_to_docx.exe "D:\Archivos\Contratos" "D:\Archivos\Contratos_Word"
```

---

## Ejecución con el lanzador `.bat`

El archivo `convert_pdfs.bat` usa el ejecutable automáticamente y configura las rutas por defecto.

### Pasos:

1. Coloca tus archivos PDF en la carpeta `input_pdfs/`
2. Ejecuta el script:
   ```cmd
   convert_pdfs.bat
   ```
3. Los archivos DOCX se generarán en `output_docx/`

Si las carpetas no existen, se crearán automáticamente.

---

## Salida generada

```
output_docx/
├── documento1.docx
├── documento2.docx
└── presentacion.docx
```

Cada archivo PDF genera un archivo DOCX con el mismo nombre.

---

## Compilar el ejecutable (solo si tienes Python)

Si necesitas recompilar el ejecutable desde el código fuente:

### Requisitos:
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos:

1. **Compilar automáticamente:**
   ```cmd
   build_exe.bat
   ```
   
   Este script:
   - Instala las dependencias necesarias
   - Compila el código con PyInstaller
   - Genera `pdf_to_docx.exe` en la raíz del proyecto

2. **Compilación manual (alternativa):**
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   pyinstaller --onefile --name pdf_to_docx --console src\pdf_to_docx.py
   ```

---

## Ejecutar con Python (sin compilar)

Si tienes Python instalado, puedes ejecutar el script directamente:

```cmd
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el conversor
python src\pdf_to_docx.py .\input_pdfs .\output_docx
```

---

## Dependencias

- **pdf2docx** >= 0.5.6: Librería principal para conversión PDF a DOCX
- **PyInstaller** >= 5.0.0: Para compilar el ejecutable (solo desarrollo)

---

## Requisitos del sistema

### Para usar el ejecutable:
- **Sistema operativo**: Windows 7 o superior
- **Espacio en disco**: ~50 MB para el ejecutable + espacio para archivos
- **RAM**: 512 MB mínimo (depende del tamaño de los PDFs)

### Para desarrollo (compilar desde fuente):
- Python 3.7 o superior
- pip (incluido con Python)
- Conexión a internet (para descargar dependencias)

---

## Limitaciones conocidas

- **PDFs escaneados**: Los PDFs que son imágenes escaneadas pueden no convertirse correctamente. Se recomienda usar OCR previamente.
- **Formatos complejos**: PDFs con diseños muy complejos o formularios interactivos pueden perder algo de formato.
- **Archivos grandes**: PDFs muy grandes (>100 MB) pueden tardar varios minutos en procesarse.
- **Fuentes especiales**: Algunas fuentes personalizadas pueden ser sustituidas por fuentes estándar.

---

## Casos de uso

- **Edición de documentos**: Convertir PDFs para editarlos en Microsoft Word
- **Procesamiento de texto**: Extraer contenido de PDFs para análisis o modificación
- **Migración de formatos**: Convertir documentación legacy de PDF a DOCX
- **Extracción de datos**: Convertir informes y reportes para procesamiento adicional
- **Documentos académicos**: Convertir papers y artículos para edición

---

## Solución de problemas

### El ejecutable no se encuentra o no funciona

1. Verifica que `pdf_to_docx.exe` esté en la misma carpeta que `convert_pdfs.bat`
2. Si no existe, compílalo ejecutando `build_exe.bat`
3. Si tienes problemas, ejecuta con Python directamente (ver sección correspondiente)

### Error: "No se encontraron archivos PDF"

1. Verifica que los archivos tengan extensión `.pdf` (no `.PDF` mayúscula en algunos casos)
2. Asegúrate de que los PDFs estén en el directorio correcto
3. Verifica que los archivos no estén corruptos

### La conversión falla o produce archivos vacíos

1. Verifica que el PDF no esté protegido con contraseña
2. Intenta abrir el PDF en un visor para confirmar que no está corrupto
3. Para PDFs escaneados, considera usar OCR primero

### El proceso es muy lento

1. Los archivos grandes tardan más tiempo (normal)
2. Cierra otras aplicaciones para liberar RAM
3. Considera procesar los archivos en lotes más pequeños

---

## Estructura del proyecto

```
Pdf_2_DocxWindows/
├── src/
│   └── pdf_to_docx.py       # Script principal de conversión
├── input_pdfs/               # Carpeta para PDFs de entrada (se crea automáticamente)
├── output_docx/              # Carpeta para DOCX de salida (se crea automáticamente)
├── build/                    # Archivos de compilación (generado)
├── dist/                     # Distribución del ejecutable (generado)
├── pdf_to_docx.exe          # Ejecutable standalone (generado)
├── convert_pdfs.bat         # Script de conversión rápida
├── build_exe.bat            # Script de compilación
├── requirements.txt         # Dependencias de Python
└── README.md                # Este archivo
```

---

## Licencia

Este proyecto es una herramienta de utilidad para conversión de documentos.
Desarrollado como parte de las utilidades de automatización de demos-ia.

Comunidad QA. Knowmadmood. Licencia GPL V3

---

**Versión**: 1.0.0  
**Última actualización**: Mayo 2026  
**Compatibilidad**: Windows 7/8/10/11
