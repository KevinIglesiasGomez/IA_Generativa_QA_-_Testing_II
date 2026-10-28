"""
Orquestador de la integracion con XRay.
Envia los resultados del reporte Cucumber a XRay.

Uso directo: python xray_sync.py [ruta_cucumber_report.json]
Uso automatico: via xray_cli.py run (equivalente a test:xray:*) o xray_hooks.py
"""

import sys

import xray_config as config
from xray_http import advertir, mensaje_error
from xray_sender import enviar_resultados


def main(ruta_reporte=None):
    """Devuelve el codigo de salida del proceso (0 correcto, 1 error)."""
    if not config.enabled:
        print("Integracion con XRay desactivada (XRAY_ENABLED=false o .env.xray no encontrado).")
        return 0

    try:
        enviar_resultados(ruta_reporte)
    except Exception as error:
        advertir(f"Error en la sincronizacion con XRay: {mensaje_error(error)}")
        return 1
    return 0


# Ejecutar solo cuando se llama directamente como script
if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
