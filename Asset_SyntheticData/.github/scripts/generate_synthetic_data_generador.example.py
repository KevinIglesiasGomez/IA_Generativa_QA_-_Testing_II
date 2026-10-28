#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
# SPDX-License-Identifier: GPL-3.0-only
"""
Generador de Datos Sinteticos 
Proyecto: Seguros
Dominio: Seguros
Proposito: Testing funcional
Seed: 42 | Locale: es_ES | Registros: 100 reclamaciones
"""
import json
import csv
import uuid
import random
from datetime import datetime, date, timedelta
from pathlib import Path

# --- Faker ---
from faker import Faker
fake = Faker("es_ES")
Faker.seed(42)
random.seed(42)

# --- Rutas ---
BASE = Path("/home/amartinez/Documentos/DEMO_IA/Demo_SyntheticData")
DICT_DIR = BASE / "diccionarios"
OUT_DIR  = BASE / "Datos" / "datasets"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# CARGA DE DICCIONARIOS
# ============================================================
def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

nombres_raw   = load_json(DICT_DIR / "nombres_es.json")
apellidos_raw = load_json(DICT_DIR / "apellidos_es.json")
calles_raw    = load_json(DICT_DIR / "calles_es.json")
ciudades_raw  = load_json(DICT_DIR / "ciudades_provincias_es.json")
dominio_raw   = load_json(DICT_DIR / "sccs_dominio.json")

# nombres_es.json -> {"data": {"male": [...], "female": [...]}}
_nombres_data = nombres_raw["data"]
NOMBRES = _nombres_data["male"] + _nombres_data["female"]

# apellidos_es.json -> {"data": ["Garcia", ...]}
APELLIDOS = apellidos_raw["data"]

# calles_es.json -> {"data": ["Calle Mayor", ...]}
CALLES = calles_raw["data"]

# ciudades_provincias_es.json -> {"data": [{"ciudad": ..., "provincia": ..., "codigo_postal_inicio": ...}, ...]}
CIUDADES = ciudades_raw["data"]

MARCAS         = dominio_raw["marcas_vehiculo"]
CIRCUNSTANCIAS = dominio_raw["circunstancias_accidente"]
DESC_SINIESTRO = dominio_raw["descripciones_siniestro"]
DESC_DANIOS_DM = dominio_raw["descripciones_danios_dm"]
DESC_LESIONES  = dominio_raw["descripciones_lesiones"]
OBS_DM         = dominio_raw["observaciones_dm"]
OBS_DP         = dominio_raw["observaciones_dp"]
OBS_COM        = dominio_raw["observaciones_comunicacion"]
HOSPITALES     = dominio_raw["hospitales_es"]

# ============================================================
# HELPERS
# ============================================================
def pick(lst, weights=None):
    return random.choices(lst, weights=weights, k=1)[0]

def maybe_none(value, pct_null):
    return None if random.random() < pct_null else value

def rand_date(start: date, end: date) -> date:
    delta = (end - start).days
    if delta <= 0:
        return start
    return start + timedelta(days=random.randint(0, delta))

def rand_matricula():
    nums = f"{random.randint(1000,9999)}"
    lets = "".join(random.choices("BCDFGHJKLMNPRSTUVWXYZ", k=3))
    return nums + lets

def nif_fake():
    """Genera un NIF espanol bien formado."""
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    num = random.randint(10000000, 99999999)
    return f"{num}{letters[num % 23]}"

def cp_for_city(ciudad_entry):
    prefix = ciudad_entry.get("codigo_postal_inicio", "28")
    suffix = f"{random.randint(0, 999):03d}"
    return prefix + suffix

def ciudad_entry_by_name(nombre):
    for c in CIUDADES:
        if c["ciudad"] == nombre:
            return c
    return CIUDADES[0]

def rand_iban_es():
    banco    = pick(["0049","0075","0081","2038","2100","0182","0128","1465","0019","0073"])
    sucursal = f"{random.randint(1000,9999):04d}"
    dc       = f"{random.randint(10,99):02d}"
    cuenta   = f"{random.randint(1000000000,9999999999):010d}"
    return banco, sucursal, dc, cuenta

# Mapa codigo -> descripcion para documentos
DOC_DESC = {
    940: "Declaracion_accidente", 941: "Presupuesto_reparacion",
    942: "Peritacion", 943: "Factura_acreditativo_pago",
    944: "Denuncia_sustraccion", 945: "Atestado",
    946: "Boletin_recuperacion", 947: "Declaracion_testigos",
    948: "Informe_medico", 949: "Parte_baja_alta",
    950: "Controversia", 951: "Otros_documentos",
    954: "Justificante_no_envio"
}

# Reglamento de mensajes: codigo -> (descripcion, origen)
MSG_CATALOG = {
    140: ("EA Inicia tramite", "EA"),
    141: ("EA Inicia tramite perjudicado auto", "EA"),
    142: ("EA Inicia tramite perjudicado lesionado", "EA"),
    143: ("EA Inicia tramite perjudicado diverso", "EA"),
    526: ("EA solicita baja, no aplica tramite", "EA"),
    527: ("CCS comunica baja por gestion directa asegurado", "CCS"),
    528: ("EA comunica baja por error en datos", "EA"),
    530: ("CCS deniega el tramite", "CCS"),
    617: ("CCS solicita datos CC", "CCS"),
    618: ("CCS solicita documentacion", "CCS"),
    903: ("CCS comunica referencia expediente-tramitacion", "CCS"),
    906: ("CCS comunica importe indemnizacion (DP)", "CCS"),
    907: ("EA informa importe solicitado perjudicado (DP)", "EA"),
    908: ("EA envia nuevos datos", "EA"),
    909: ("EA envia modificacion de importes", "EA"),
    910: ("CCS comunica realizado el pago", "CCS"),
    916: ("EA envia datos CC", "EA"),
    917: ("CCS comunica cambio de cobertura", "CCS"),
    919: ("EA envia documentacion solicitada", "EA"),
    920: ("EA envia documentacion adicional", "EA"),
}

CODIGOS_ENTIDAD = ["0049","0072","0115","0153","0218","0301","0456","0550","0712","0890"]

# ============================================================
# GENERADORES POR ENTIDAD
# ============================================================

def gen_reclamaciones(n=100):
    rows = []
    hoy = date(2026, 3, 13)
    start = date(2021, 3, 13)
    estados = ["ABIERTA","LIQUIDADA","DENEGADA","BAJA_SOLICITADA","BAJA_ERROR_DATOS","BAJA_GESTION_DIRECTA"]
    estados_w = [35,30,10,10,8,7]
    tips_tram = ["DM","DP","DV"]
    tips_w    = [60,25,15]
    coberturas = ["SEGURO_DIRECTO","ROBADO","SIN_SEGURO"]
    cob_w      = [70,15,15]
    motivos_baja = [
        "Denegacion por documentacion incompleta",
        "Gestion directa con el asegurado",
        "Error en datos del alta",
        "Tramite no aplicable al CCS",
        "Baja solicitada por la entidad"
    ]
    seq_exp = [1]

    for i in range(1, n+1):
        tipo_tram  = pick(tips_tram, tips_w)
        if tipo_tram == "DP":
            tipo_rec = "GESTION"
        else:
            tipo_rec = pick(
                ["GESTION","REEMBOLSO_SIN_FRANQUICIA","REEMBOLSO_CON_FRANQUICIA"],
                [50,35,15]
            )
        cobertura  = pick(coberturas, cob_w)
        estado     = pick(estados, estados_w)
        fecha_alta = rand_date(start, hoy - timedelta(days=30))

        # expediente CCS: existe si no es ABIERTA sin 903 aun
        has_exp = estado in ("LIQUIDADA","DENEGADA","BAJA_SOLICITADA","BAJA_ERROR_DATOS","BAJA_GESTION_DIRECTA") or random.random() > 0.15
        seq_exp[0] += 1
        id_exp  = f"EXP{fecha_alta.year}{seq_exp[0]:06d}" if has_exp else None
        id_tram = f"TRAM{fecha_alta.year}{seq_exp[0]:06d}" if has_exp else None

        # fecha baja
        fecha_baja = None
        motivo_baja = None
        if estado != "ABIERTA" and estado != "LIQUIDADA":
            dias_baja = random.randint(5, 180)
            fecha_baja = (fecha_alta + timedelta(days=dias_baja)).isoformat()
            motivo_baja = pick(motivos_baja)

        # actuaciones judiciales
        judicial = "S" if random.random() < 0.12 else "N"
        ciudad_jud = pick(CIUDADES)["ciudad"] if judicial == "S" else None
        juzgado = f"Juzgado {random.randint(1,5)} de Primera Instancia de {ciudad_jud}" if judicial == "S" else None
        num_proc = f"{random.randint(100,9999):04d}/{fecha_alta.year}" if judicial == "S" else None

        rows.append({
            "id_reclamacion": str(uuid.uuid4()),
            "referencia_entidad": f"ENT{fecha_alta.year}-{i:06d}",
            "id_expediente_ccs": id_exp,
            "id_tramitacion_ccs": id_tram,
            "codigo_entidad_dgs": pick(CODIGOS_ENTIDAD),
            "tipo_tramitacion": tipo_tram,
            "tipo_reclamacion": tipo_rec,
            "cobertura": cobertura,
            "estado": estado,
            "fecha_alta": fecha_alta.isoformat(),
            "fecha_baja": fecha_baja,
            "motivo_baja": motivo_baja,
            "indicador_leido": pick(["S","N"], [80,20]),
            "tiene_actuaciones_judiciales": judicial,
            "juzgado": juzgado,
            "numero_procedimiento_judicial": num_proc,
        })
    return rows


def gen_siniestros(reclamaciones):
    rows = []
    for r in reclamaciones:
        fecha_alta = date.fromisoformat(r["fecha_alta"])
        start_sin  = date(2021, 1, 1)
        end_sin    = fecha_alta - timedelta(days=1)
        fecha_sin  = rand_date(start_sin, end_sin)
        ciudad_ent = pick(CIUDADES)
        marca_ent  = pick(MARCAS)
        rows.append({
            "id_siniestro": str(uuid.uuid4()),
            "id_reclamacion": r["id_reclamacion"],
            "matricula_causante": rand_matricula(),
            "bastidor_causante": maybe_none(f"VF1RB{fake.bothify('???????????').upper()}", 0.4),
            "marca_causante": maybe_none(marca_ent["marca"], 0.3),
            "modelo_causante": maybe_none(pick(marca_ent["modelos"]), 0.3),
            "tipo_uso": maybe_none(pick(["PARTICULAR","COMERCIAL","TAXI","ALQUILER","OTROS"],[65,20,5,8,2]), 0.2),
            "clase_vehiculo": maybe_none(pick(["TURISMO","FURGONETA","CAMION","MOTO","AUTOBUS","OTROS"],[55,20,10,10,3,2]), 0.2),
            "fecha_siniestro": fecha_sin.isoformat(),
            "descripcion_siniestro": pick(DESC_SINIESTRO),
            "lugar_ocurrencia": f"{pick(CALLES)} {random.randint(1,200)}",
            "localidad": ciudad_ent["ciudad"],
            "provincia": ciudad_ent["provincia"],
            "codigo_postal": maybe_none(cp_for_city(ciudad_ent), 0.2),
            "existencia_atestado": pick(["S","N"],[40,60]),
            "circunstancia": pick(CIRCUNSTANCIAS),
        })
    return rows


def _persona_fisica():
    nombre   = pick(NOMBRES)
    ap1      = pick(APELLIDOS)
    ap2      = maybe_none(pick(APELLIDOS), 0.1)
    ciudad_e = pick(CIUDADES)
    return {
        "nombre": nombre, "apellido1": ap1, "apellido2": ap2,
        "ciudad_entry": ciudad_e,
    }


def gen_propietarios(reclamaciones):
    rows = []
    for r in reclamaciones:
        p = _persona_fisica()
        ce = p["ciudad_entry"]
        rows.append({
            "id_propietario": str(uuid.uuid4()),
            "id_reclamacion": r["id_reclamacion"],
            "nif_cif": maybe_none(nif_fake(), 0.2),
            "codigo_participe": "001",
            "apellido1": p["apellido1"],
            "apellido2": p["apellido2"],
            "nombre": p["nombre"],
            "razon_social": maybe_none(fake.company(), 0.85),
            "nombre_via": maybe_none(pick(CALLES), 0.25),
            "numero_via": maybe_none(str(random.randint(1,120)), 0.25),
            "piso_puerta": maybe_none(f"{random.randint(1,6)}{pick(['A','B','C','D'])}", 0.5),
            "poblacion": maybe_none(ce["ciudad"], 0.25),
            "codigo_postal": maybe_none(cp_for_city(ce), 0.25),
            "telefono": maybe_none(fake.phone_number(), 0.4),
            "email": maybe_none(fake.email(), 0.5),
        })
    return rows


def gen_conductores(reclamaciones):
    rows = []
    for r in reclamaciones:
        p = _persona_fisica()
        ce = p["ciudad_entry"]
        rows.append({
            "id_conductor": str(uuid.uuid4()),
            "id_reclamacion": r["id_reclamacion"],
            "nif_cif": maybe_none(nif_fake(), 0.15),
            "codigo_participe": "001",
            "apellido1": p["apellido1"],
            "apellido2": p["apellido2"],
            "nombre": p["nombre"],
            "razon_social": maybe_none(fake.company(), 0.9),
            "nombre_via": maybe_none(pick(CALLES), 0.3),
            "numero_via": maybe_none(str(random.randint(1,120)), 0.3),
            "piso_puerta": maybe_none(f"{random.randint(1,6)}{pick(['A','B','C','D'])}", 0.55),
            "poblacion": maybe_none(ce["ciudad"], 0.3),
            "codigo_postal": maybe_none(cp_for_city(ce), 0.3),
            "telefono": maybe_none(fake.phone_number(), 0.35),
        })
    return rows


def gen_vehiculos_danados(reclamaciones):
    rows = []
    for r in reclamaciones:
        if r["tipo_tramitacion"] != "DM":
            continue
        p = _persona_fisica()
        ce = p["ciudad_entry"]
        marca_ent = pick(MARCAS)
        peritado_por = pick(["COMPANIA","CCS","NO_PERITADO"],[55,25,20])
        tipo_rec = r["tipo_reclamacion"]
        nif_pj = "FIC" if random.random() < 0.05 else nif_fake()
        rows.append({
            "id_vehiculo_danado": str(uuid.uuid4()),
            "id_reclamacion": r["id_reclamacion"],
            "nif_perjudicado": nif_pj,
            "nombre_perjudicado": f"{p['apellido1']} {p['apellido2'] or ''}, {p['nombre']}".strip(", "),
            "domicilio_nombre_via": pick(CALLES),
            "domicilio_numero": str(random.randint(1,150)),
            "domicilio_piso": maybe_none(f"{random.randint(1,6)}{pick(['A','B','C','D'])}", 0.4),
            "domicilio_poblacion": ce["ciudad"],
            "domicilio_codigo_postal": cp_for_city(ce),
            "domicilio_provincia": ce["provincia"],
            "telefono": maybe_none(fake.phone_number(), 0.3),
            "email": maybe_none(fake.email(), 0.4),
            "matricula_vehiculo": rand_matricula(),
            "marca_vehiculo": marca_ent["marca"],
            "modelo_vehiculo": pick(marca_ent["modelos"]),
            "bastidor": maybe_none(f"WDB{fake.bothify('??????????????').upper()}", 0.5),
            "kms": maybe_none(int(random.expovariate(1/80000)) + 5000, 0.4),
            "color": maybe_none(pick(["Blanco","Negro","Gris","Plata","Rojo","Azul","Verde","Beige","Marron"]), 0.4),
            "clase_riesgo": maybe_none(pick(["Automovil","Furgoneta","Motocicleta","Camion","Remolque"]), 0.3),
            "descripcion_danios": pick(DESC_DANIOS_DM),
            "importe_reclamado": maybe_none(round(random.uniform(200, 25000), 2), 0.3),
            "vehiculo_reparado": (vr := pick(["S","N"],[55,45])),
            "intencion_reparar": maybe_none(pick(["S","N"],[70,30]), 0) if vr == "N" else None,
            "peritado_por": peritado_por,
            "taller_nombre": fake.company() if peritado_por == "CCS" else maybe_none(fake.company(), 0.9),
            "taller_telefono": fake.phone_number() if peritado_por == "CCS" else None,
            "taller_direccion": fake.address() if peritado_por == "CCS" else None,
            "peritado_entidad": "S" if peritado_por == "COMPANIA" else "N",
            "pagado_entidad": "S" if "REEMBOLSO" in tipo_rec else "N",
            "otros_danios": pick(["S","N"],[25,75]),
            "paralizacion": pick(["S","N"],[20,80]),
            "cide": pick(["S","N"],[15,85]),
            "observaciones": maybe_none(pick(OBS_DM), 0.5),
        })
    return rows


def gen_victimas(reclamaciones):
    rows = []
    for r in reclamaciones:
        if r["tipo_tramitacion"] != "DP":
            continue
        n_vic = random.choices([1,2,3], weights=[70,20,10])[0]
        for idx in range(1, n_vic+1):
            p = _persona_fisica()
            ce = p["ciudad_entry"]
            it = pick(["S","N"],[65,35])
            ip = pick(["S","N"],[15,85])
            gi = pick(["S","N"],[3,97])
            mu = pick(["S","N"],[5,95])
            # al menos uno debe ser S
            if it == "N" and ip == "N" and gi == "N" and mu == "N":
                it = "S"
            rows.append({
                "id_victima": str(uuid.uuid4()),
                "id_reclamacion": r["id_reclamacion"],
                "codigo_participe": f"{idx:03d}",
                "nif": maybe_none(nif_fake(), 0.2),
                "apellido1": p["apellido1"],
                "apellido2": p["apellido2"],
                "nombre": p["nombre"],
                "condicion_victima": pick(["CONDUCTOR","VIAJERO","PEATON","CICLISTA","OTROS"],[45,30,15,8,2]),
                "descripcion_lesiones": pick(DESC_LESIONES),
                "edad": maybe_none(max(1, int(random.gauss(40, 18))), 0.2),
                "sexo": maybe_none(pick(["M","F"],[52,48]), 0.15),
                "incapacidad_temporal": it,
                "incapacidad_permanente": ip,
                "gran_invalidez": gi,
                "muerte": mu,
                "importe_reclamado": maybe_none(round(random.uniform(500, 50000), 2), 0.35),
                "nombre_via_domicilio": maybe_none(pick(CALLES), 0.4),
                "numero_via": maybe_none(str(random.randint(1,150)), 0.4),
                "piso_puerta": maybe_none(f"{random.randint(1,6)}{pick(['A','B','C','D'])}", 0.55),
                "poblacion": maybe_none(ce["ciudad"], 0.4),
                "codigo_postal": maybe_none(cp_for_city(ce), 0.4),
                "telefono": maybe_none(fake.phone_number(), 0.45),
                "centro_hospitalario": maybe_none(pick(HOSPITALES), 0.4),
                "observaciones": maybe_none(pick(OBS_DP), 0.55),
            })
    return rows


def gen_comunicaciones(reclamaciones):
    rows = []
    for r in reclamaciones:
        estado = r["estado"]
        tipo_tram = r["tipo_tramitacion"]
        fecha_alta = date.fromisoformat(r["fecha_alta"])
        id_rec = r["id_reclamacion"]

        # Secuencia de mensajes segun tipo de dano y estado
        if tipo_tram == "DM":
            seq = [140]
        elif tipo_tram == "DP":
            seq = [142]
        else:
            seq = [143]

        # Si tiene expediente asignado, el CCS responde con 903
        if r["id_expediente_ccs"]:
            seq.append(903)

        # Mensajes intermedios segun estado
        if estado == "LIQUIDADA":
            seq += [618, 919, 910]
        elif estado == "DENEGADA":
            seq += [618, 530]
        elif estado == "BAJA_SOLICITADA":
            seq.append(526)
        elif estado == "BAJA_ERROR_DATOS":
            seq.append(528)
        elif estado == "BAJA_GESTION_DIRECTA":
            seq.append(527)
        elif estado == "ABIERTA":
            if random.random() > 0.5:
                seq.append(618)
            if tipo_tram == "DP" and random.random() > 0.6:
                seq += [906, 907]

        offset_days = 0
        for cod in seq:
            desc, origen = MSG_CATALOG.get(cod, (f"Mensaje {cod}", "EA"))
            destino = "CCS" if origen == "EA" else "EA"
            offset_days += random.randint(0, 10)
            fecha_envio = fecha_alta + timedelta(days=offset_days)
            rows.append({
                "id_comunicacion": str(uuid.uuid4()),
                "id_reclamacion": id_rec,
                "codigo_mensaje": cod,
                "descripcion_mensaje": desc,
                "origen": origen,
                "destino": destino,
                "fecha_envio": fecha_envio.isoformat() + "T" + f"{random.randint(8,18):02d}:{random.randint(0,59):02d}:00",
                "observaciones": maybe_none(pick(OBS_COM), 0.6),
                "leido": pick(["S","N"],[85,15]),
            })
    return rows


def gen_documentos(reclamaciones):
    rows = []
    cod_docs = [940,941,942,943,944,945,946,947,948,949,950,951,954]
    cod_w    = [20,10,10,15,5,10,5,5,8,5,3,3,1]
    formatos = ["pdf","jpg","tiff","txt","xls"]
    form_w   = [65,15,10,5,5]
    for r in reclamaciones:
        fecha_alta = date.fromisoformat(r["fecha_alta"])
        n_docs = random.choices([1,2,3,4], weights=[30,35,25,10])[0]
        docs_usados = set()
        for _ in range(n_docs):
            cod = pick(cod_docs, cod_w)
            docs_usados.add(cod)
            fmt = pick(formatos, form_w)
            desc = DOC_DESC.get(cod, "documento")
            short_id = r["id_reclamacion"][:8]
            offset = random.randint(0, 5)
            rows.append({
                "id_documento": str(uuid.uuid4()),
                "id_reclamacion": r["id_reclamacion"],
                "tipo_documento": cod,
                "descripcion_tipo": desc.replace("_"," "),
                "formato": fmt,
                "nombre_fichero": f"{desc}_{short_id}.{fmt}",
                "tamano_bytes": min(3145728, int(random.expovariate(1/500000)) + 10240),
                "descargado": pick(["S","N"],[70,30]),
                "fecha_subida": (fecha_alta + timedelta(days=offset)).isoformat() + "T" + f"{random.randint(8,18):02d}:00:00",
            })
    return rows


def gen_pagos(reclamaciones):
    rows = []
    for r in reclamaciones:
        if r["estado"] != "LIQUIDADA":
            continue
        tipo_rec = r["tipo_reclamacion"]
        fecha_alta = date.fromisoformat(r["fecha_alta"])
        franquicia = round(random.uniform(150, 600), 2) if tipo_rec == "REEMBOLSO_CON_FRANQUICIA" else 0.0
        if tipo_rec == "GESTION":
            perceptor = pick(["ASEGURADO","TALLER","ENTIDAD"],[50,30,20])
        else:
            perceptor = "ENTIDAD"
        importe_total = round(random.uniform(300, 30000), 2)
        imp_entidad   = round(importe_total - franquicia, 2) if perceptor in ("ENTIDAD","AMBOS") else None
        imp_asegurado = round(franquicia, 2) if perceptor == "AMBOS" else None
        banco, suc, dc, cuenta = rand_iban_es()
        dias_pago = random.randint(30, 180)
        rows.append({
            "id_pago": str(uuid.uuid4()),
            "id_reclamacion": r["id_reclamacion"],
            "importe_franquicia": franquicia,
            "perceptor": perceptor,
            "importe_total": importe_total,
            "importe_entidad": imp_entidad,
            "importe_asegurado": imp_asegurado,
            "codigo_banco": banco,
            "codigo_sucursal": suc,
            "digito_control": dc,
            "numero_cuenta": cuenta,
            "titular_cuenta": fake.company(),
            "fecha_pago": (fecha_alta + timedelta(days=dias_pago)).isoformat(),
        })
    return rows


# ============================================================
# EXPORTACION
# ============================================================
def write_csv(data, entity_name):
    if not data:
        return
    path = OUT_DIR / f"{entity_name}.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    return path


def write_json(data, entity_name):
    if not data:
        return
    path = OUT_DIR / f"{entity_name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    return path


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    start_time = datetime.now()
    print("Generando datos sinteticos SCCS...")
    print(f"  Seed: 42 | Locale: es_ES | Reclamaciones: 100\n")

    reclamaciones     = gen_reclamaciones(100)
    siniestros        = gen_siniestros(reclamaciones)
    propietarios      = gen_propietarios(reclamaciones)
    conductores       = gen_conductores(reclamaciones)
    vehiculos_danados = gen_vehiculos_danados(reclamaciones)
    victimas          = gen_victimas(reclamaciones)
    comunicaciones    = gen_comunicaciones(reclamaciones)
    documentos        = gen_documentos(reclamaciones)
    pagos             = gen_pagos(reclamaciones)

    entities = {
        "reclamaciones":     reclamaciones,
        "siniestros":        siniestros,
        "propietarios_causante": propietarios,
        "conductores_causante":  conductores,
        "vehiculos_danados": vehiculos_danados,
        "victimas":          victimas,
        "comunicaciones":    comunicaciones,
        "documentos":        documentos,
        "pagos":             pagos,
    }

    total = 0
    print(f"{'Entidad':<30} {'Registros':>10}  {'CSV':>5}  {'JSON':>5}")
    print("-" * 55)
    for name, data in entities.items():
        write_csv(data, name)
        write_json(data, name)
        print(f"  {name:<28} {len(data):>10}  {'OK':>5}  {'OK':>5}")
        total += len(data)

    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"\n{'='*55}")
    print(f"  Total registros generados : {total}")
    print(f"  Duracion                  : {elapsed:.2f}s")
    print(f"  Directorio de salida      : {OUT_DIR}")
    print(f"{'='*55}")
