# PDF to Markdown Converter

Aplicación ejecutable para Windows que convierte archivos PDF a formato Markdown (.md) preservando el contenido, estructura e imágenes.

---

## Características

- **Conversión por lotes**: Procesa múltiples archivos PDF automáticamente
- **Preservación de contenido**: Extrae texto, imágenes y mantiene la estructura
- **Extracción de imágenes**: Las imágenes del PDF se guardan en carpetas separadas
- **Ejecutable standalone**: No requiere Python instalado
- **Interfaz simple**: Uso mediante línea de comandos o scripts .bat
- **Formato Markdown**: Salida optimizada para documentación y gestión de contenido
- **Multiplataforma**: Desarrollado en Python, ejecutable para Windows

---

## Uso rápido (ejecutable standalone)

El ejecutable **no requiere Python** instalado. Procesa todos los `.pdf` del directorio de entrada
y genera los `.md` en el directorio de salida.

```cmd
pdf_to_markdown.exe <directorio_entrada> <directorio_salida>
```

### Ejemplos de uso

**Conversión básica:**
```cmd
pdf_to_markdown.exe .\input_pdfs .\output_markdown
```

**Usar rutas absolutas:**
```cmd
pdf_to_markdown.exe "C:\Documentos\PDFs" "C:\Documentos\Markdown"
```

**Convertir PDFs de una carpeta específica:**
```cmd
pdf_to_markdown.exe "D:\Archivos\Documentos" "D:\Archivos\Documentos_MD"
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
3. Los archivos Markdown se generarán en `output_markdown/`

Si las carpetas no existen, se crearán automáticamente.

---

## Salida generada

```
output_markdown/
├── documento1.md
├── documento2.md
├── presentacion.md
├── documento1_images/
│   ├── image_p1_i0.png
│   └── image_p3_i0.jpg
├── documento2_images/
│   └── image_p2_i0.png
└── presentacion_images/
    ├── image_p1_i0.png
    ├── image_p1_i1.png
    └── image_p5_i0.jpg
```

Cada archivo PDF genera:
- Un archivo `.md` con el contenido en formato Markdown
- Una carpeta `<nombre>_images/` con las imágenes extraídas (si las hay)

### Formato del Markdown generado

El archivo Markdown incluye:
- Título basado en el nombre del archivo
- Separadores de página
- Texto extraído del PDF
- Referencias a las imágenes extraídas
- Estructura preservada del documento original

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
   - Instala las dependencias necesarias (PyMuPDF)
   - Compila el código con PyInstaller
   - Genera `pdf_to_markdown.exe` en la raíz del proyecto

2. **Compilación manual (alternativa):**
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   pyinstaller --onefile --name pdf_to_markdown --console src\pdf_to_markdown.py
   ```

---

## Dependencias

Si ejecutas el código Python directamente (sin el ejecutable):

```
PyMuPDF>=1.23.0
PyInstaller>=5.0.0
```

### Instalación de dependencias:

```cmd
pip install -r requirements.txt
```

---

## Ejecución con Python (sin compilar)

Si tienes Python instalado, puedes ejecutar directamente el script:

```cmd
python src\pdf_to_markdown.py <directorio_entrada> <directorio_salida>
```

**Ejemplo:**
```cmd
python src\pdf_to_markdown.py .\input_pdfs .\output_markdown
```

---

## Notas técnicas

### Extracción de contenido

- **Texto**: Se extrae todo el texto visible del PDF preservando la estructura
- **Imágenes**: Se extraen en su formato original (PNG, JPG, etc.)
- **Formato**: Se intenta preservar la estructura de párrafos y secciones

### Limitaciones

- Los PDFs con texto como imagen (escaneados) requieren OCR previo
- Tablas complejas se extraen como texto plano
- El formato exacto puede variar según la complejidad del PDF original
- Elementos interactivos (formularios, enlaces) se extraen como texto

### Formatos soportados

- **Entrada**: Archivos PDF (.pdf)
- **Salida**: Markdown (.md) e imágenes (PNG, JPG, etc.)

---

## Solución de problemas

### El ejecutable no se encuentra

Compila el ejecutable ejecutando `build_exe.bat`

### Error al convertir un PDF

- Verifica que el PDF no esté protegido con contraseña
- Asegúrate de que el PDF no esté corrupto
- Intenta con otros archivos PDF para descartar problemas específicos

### Las imágenes no se extraen

Algunos PDFs tienen imágenes incrustadas de forma especial. El conversor intenta extraer todas las imágenes disponibles, pero algunas pueden no ser accesibles.

### Caracteres especiales no se muestran correctamente

El conversor utiliza UTF-8 para la salida. Asegúrate de abrir los archivos Markdown con un editor que soporte UTF-8.

---

## Estructura del proyecto

```
Pdf_2_MarkDownWindows/
├── src/
│   └── pdf_to_markdown.py    # Código fuente principal
├── build_exe.bat              # Script de compilación
├── convert_pdfs.bat           # Script de ejecución rápida
├── requirements.txt           # Dependencias de Python
└── README.md                  # Esta documentación
```

---

## Licencia

Este proyecto es una herramienta de utilidad desarrollada para facilitar la conversión de documentos PDF a formato Markdown.

Comunidad QA. Knowmadmood. Licencia GPL V3

---

## Créditos

Desarrollado utilizando:
- **PyMuPDF (fitz)**: Biblioteca para manipulación de PDFs
- **PyInstaller**: Para crear el ejecutable standalone
- **Python**: Lenguaje de programación principal
