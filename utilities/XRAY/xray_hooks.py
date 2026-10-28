"""
Hook para sincronizacion automatica con XRay al finalizar la ejecucion (equivalente a AfterAll
de Cucumber). Se activa solo si XRAY_ENABLED=true en .env.xray.

Uso con behave, en features/environment.py:
    from xray_hooks import after_all
"""

import xray_config as config
from xray_http import advertir, mensaje_error
from xray_sender import enviar_resultados


def after_all(context=None):
    if not config.enabled:
        return

    print("\nEnviando resultados a XRay...")
    try:
        enviar_resultados()
    except Exception as error:
        # No fallar el build si XRay no esta disponible
        advertir(f"Error al enviar resultados a XRay: {mensaje_error(error)}")
