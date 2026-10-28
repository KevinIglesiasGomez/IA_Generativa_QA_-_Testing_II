"""
Utilidades HTTP compartidas. Reproducen la semantica de axios: lanzan excepcion en
respuestas no 2xx y exponen mensaje y cuerpo de error de forma uniforme.
"""

import sys

import requests

TIMEOUT_SEGUNDOS = 120


def advertir(mensaje):
    """Equivalente a console.warn / console.error (salida de error estandar)."""
    print(mensaje, file=sys.stderr)


def verificar(respuesta):
    """Lanza HTTPError si la respuesta no es 2xx (como axios) y la devuelve."""
    respuesta.raise_for_status()
    return respuesta


def datos(respuesta):
    """Equivalente a response.data de axios: JSON si es posible, texto en otro caso."""
    try:
        return respuesta.json()
    except ValueError:
        return respuesta.text


def mensaje_error(error):
    """Equivalente a error.message de axios."""
    respuesta = getattr(error, "response", None)
    if isinstance(error, requests.HTTPError) and respuesta is not None:
        return f"Request failed with status code {respuesta.status_code}"
    return str(error)
