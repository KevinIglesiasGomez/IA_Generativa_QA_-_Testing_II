"""
Interfaz de linea de comandos equivalente a los scripts npm de la version Node.js.

  python xray_cli.py validate [dir_features]        ~ npm run xray:validate
  python xray_cli.py send [cucumber-report.json]    ~ npm run xray:send
  python xray_cli.py run [--headed] -- <comando>    ~ npm run test:xray:headless / test:xray:headed

`run` valida los escenarios, ejecuta el comando de pruebas indicado (que debe generar el JSON de
Cucumber en reports/json/cucumber-report.json) y, solo si termina con codigo 0, envia los resultados.
Con --headed define HEADED=true en el entorno del comando.
"""

import argparse
import os
import subprocess
import sys

import scenario_validator
import xray_sync
from xray_http import advertir, mensaje_error


def _validar(directorio):
    try:
        scenario_validator.validar_y_sincronizar(directorio)
        return 0
    except Exception as err:
        advertir(f"Error en la validacion: {mensaje_error(err)}")
        return 1


def main(argv=None):
    parser = argparse.ArgumentParser(description="Integracion XRay / Jira Cloud")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_validate = sub.add_parser("validate", help="Sincroniza los .feature con XRay sin ejecutar pruebas")
    p_validate.add_argument("directorio", nargs="?")

    p_send = sub.add_parser("send", help="Envia el reporte JSON de Cucumber a XRay")
    p_send.add_argument("reporte", nargs="?")

    p_run = sub.add_parser("run", help="Valida, ejecuta las pruebas y envia resultados")
    p_run.add_argument("--headed", action="store_true")
    p_run.add_argument("--features", help="Directorio de features a validar")
    p_run.add_argument("comando_pruebas", nargs=argparse.REMAINDER)

    args = parser.parse_args(argv)

    if args.comando == "validate":
        return _validar(args.directorio)
    if args.comando == "send":
        return xray_sync.main(args.reporte)

    comando = [c for c in args.comando_pruebas if c != "--"] if args.comando_pruebas else []
    if not comando:
        advertir('Indica el comando de pruebas tras "--". Ej: xray_cli.py run -- behave features')
        return 2

    codigo = _validar(args.features)
    if codigo != 0:
        return codigo

    entorno = dict(os.environ)
    if args.headed:
        entorno["HEADED"] = "true"
    codigo = subprocess.call(comando, env=entorno)
    if codigo != 0:
        return codigo
    return xray_sync.main()


if __name__ == "__main__":
    sys.exit(main())
