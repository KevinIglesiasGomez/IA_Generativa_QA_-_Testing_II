#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
# SPDX-License-Identifier: GPL-3.0-only
"""
Generador de Datos Sintéticos SCCS
Proyecto : SCCS-Dataset
Dominio  : Seguros - Reclamaciones de accidentes de circulación
Propósito: Testing funcional
Seed     : 42 | Locale: es_ES | Siniestros: 100
"""

import json, uuid, random, math
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from faker import Faker
fake = Faker("es_ES")
Faker.seed(42)
random.seed(42)

# ── Rutas ────────────────────────────────────────────────────
BASE     = Path(__file__).parent
DICT_DIR = BASE / "metadata" / "dictionaries"
OUT_DIR  = BASE / "datasets"
OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "samples").mkdir(exist_ok=True)

# ── Configuración ────────────────────────────────────────────
NUM_SINIESTROS = 100
DATE_START     = date(2024, 1, 1)
DATE_END       = date(2026, 3, 19)

# ── Carga de diccionarios ────────────────────────────────────
def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

_n  = load_json(DICT_DIR / "nombres_es.json")
_a  = load_json(DICT_DIR / "apellidos_es.json")
_c  = load_json(DICT_DIR / "calles_es.json")
_cp = load_json(DICT_DIR / "ciudades_provincias_es.json")
_d  = load_json(DICT_DIR / "accidentes.json")

NOMBRES    = _n["data"]["male"] + _n["data"]["female"]
APELLIDOS  = _a["data"]
CALLES     = _c["data"]
CIUDADES   = _cp["data"]
MARCAS     = _d["marcas_vehiculo"]
DESC_SIN   = _d["descripciones_siniestro"]
DESC_DM    = _d["descripciones_danios_dm"]
DESC_DP    = _d["descripciones_lesiones"]
HOSPITALES = _d["hospitales_es"]

ENTIDADES = [
    ("0049", "BBVA Seguros S.A."),
    ("0075", "Banco Santander Seguros"),
    ("0081", "Generali España S.A."),
    ("0153", "Mapfre Seguros Generales S.A."),
    ("0218", "Allianz Seguros S.A."),
    ("0301", "AXA Seguros Generales S.A."),
    ("0456", "Zurich Insurance plc, Sucursal en España"),
    ("0550", "Línea Directa Aseguradora S.A."),
    ("0712", "Mutua Madrileña Automovilista"),
    ("0890", "HDI Seguros S.A."),
]

# ── Helpers ──────────────────────────────────────────────────
def pick(lst, w=None):
    return random.choices(lst, weights=w, k=1)[0]

def maybe(val, pct_null=0.3):
    return None if random.random() < pct_null else val

def rand_date(s, e):
    d = (e - s).days
    return s + timedelta(days=random.randint(0, max(d, 0)))

def rand_datetime(d_date, offset_days=0):
    t = datetime.combine(d_date + timedelta(days=offset_days),
                         datetime.min.time(), tzinfo=timezone.utc)
    t += timedelta(hours=random.randint(7,20), minutes=random.randint(0,59))
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")

def gen_uuid():
    return str(uuid.uuid4())

def gen_nombre_completo():
    return f"{pick(NOMBRES)} {pick(APELLIDOS)} {pick(APELLIDOS)}"

def gen_matricula_es():
    nums = random.randint(1000, 9999)
    lets = "".join(random.choices("BCDFGHJKLMNPRSTUVWXYZ", k=3))
    return f"{nums}{lets}"

def dni_letra(num):
    return "TRWAGMYFPDXBNJZSQVHLCKE"[num % 23]

def gen_dni():
    n = random.randint(10_000_000, 99_999_999)
    return f"{n}{dni_letra(n)}"

def gen_nie():
    l1 = pick(["X","Y","Z"])
    n  = random.randint(1_000_000, 9_999_999)
    base = {"X":0,"Y":10_000_000,"Z":20_000_000}[l1] + n
    return f"{l1}{n:07d}{dni_letra(base)}"

def gen_cif():
    letras = "ABCDEFGHJKLMNPQRSUVW"
    l = pick(list(letras))
    n = random.randint(1_000_000, 9_999_999)
    return f"{l}{n:07d}0"

def gen_iban_es():
    banco    = pick(["0049","0075","0081","2038","2100","0182","0128"])
    suc      = f"{random.randint(1000,9999):04d}"
    dc       = f"{random.randint(10,99):02d}"
    cuenta   = f"{random.randint(1_000_000_000, 9_999_999_999):010d}"
    num_part = banco + suc + dc + cuenta
    # checksum simplificado: siempre válido en formato
    check = f"{random.randint(10,99):02d}"
    return f"ES{check} {banco} {suc} {dc} {cuenta[:5]} {cuenta[5:]}"

def gen_telefono():
    prefix = pick(["600","610","620","630","640","650","660","670","680","690",
                   "700","710","720","730","91","93","94","95"])
    return f"+34 {prefix} {random.randint(100000,999999)}"

def gen_email(nombre):
    base = nombre.lower().replace(" ",".")
    base = base.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
    domain = pick(["gmail.com","hotmail.com","yahoo.es","outlook.com","telefonica.net"])
    return f"{base}{random.randint(1,99)}@{domain}"

def ciudad_entry():
    return pick(CIUDADES)

def cp_for(entry):
    prefix = entry.get("codigo_postal_inicio","28")
    return prefix + f"{random.randint(0,999):03d}"

def gen_referencia_entidad(i, year):
    return f"ENT-{year}-{i:05d}"

# ── Generadores por entidad ──────────────────────────────────

def gen_siniestro(i):
    ciudad = ciudad_entry()
    cod_ent, nom_ent = pick(ENTIDADES)
    fs = rand_date(DATE_START, DATE_END - timedelta(days=30))
    ca = rand_datetime(fs, offset_days=random.randint(1,10))
    jud = random.random() < 0.20
    return {
        "id_siniestro": gen_uuid(),
        "referencia_entidad": gen_referencia_entidad(i, fs.year),
        "fecha_siniestro": fs.isoformat(),
        "lugar": f"{pick(CALLES)}, {random.randint(1,200)}",
        "localidad": ciudad["ciudad"],
        "codigo_postal": maybe(cp_for(ciudad), 0.15),
        "provincia": ciudad["provincia"],
        "pais": "España",
        "descripcion_accidente": pick(DESC_SIN),
        "existencia_atestado": random.random() < 0.60,
        "hay_actuaciones_judiciales": jud,
        "codigo_entidad_acreedora": cod_ent,
        "nombre_entidad_acreedora": nom_ent,
        "created_at": ca,
    }

def gen_datos_judiciales(id_siniestro, fecha_siniestro):
    ciudad = ciudad_entry()
    return {
        "id_datos_judiciales": gen_uuid(),
        "id_siniestro": id_siniestro,
        "juzgado": f"Juzgado de Primera Instancia nº {random.randint(1,10)} de {ciudad['ciudad']}",
        "numero_procedimiento": f"{random.randint(100,9999):04d}/{date.fromisoformat(fecha_siniestro).year}",
        "tipo_procedimiento": pick(["CIVIL","PENAL","ADMINISTRATIVO"], [60,30,10]),
    }

def gen_vehiculo(id_siniestro, tipo):
    m = pick(MARCAS)
    return {
        "id_vehiculo": gen_uuid(),
        "id_siniestro": id_siniestro,
        "tipo_vehiculo": tipo,
        "matricula": gen_matricula_es(),
        "marca": m["marca"],
        "modelo": pick(m["modelos"]),
        "numero_poliza": maybe(f"POL-{random.randint(2020,2026)}-{random.randint(10000,99999)}", 0.3),
        "vehiculo_reparado": maybe(random.random() < 0.55, 0.2),
        "intencion_reparar": maybe(random.random() < 0.70, 0.3),
        "peritado_por": maybe(pick(["COMPANIA","CCS","NO_PERITADO"],[50,35,15]), 0.25),
        "localizacion_vehiculo": maybe(f"Taller {pick(APELLIDOS)}, {pick(CALLES)} {random.randint(1,50)}", 0.4),
    }

def gen_persona(tipo_doc=None):
    nombre = gen_nombre_completo()
    td = tipo_doc or pick(["DNI","NIE","PASAPORTE"],[85,10,5])
    if td == "DNI":
        nd = gen_dni()
    elif td == "NIE":
        nd = gen_nie()
    else:
        nd = fake.bothify("??#######").upper()
    return nombre, td, nd

def gen_propietario(id_vehiculo):
    nombre, td, nd = gen_persona()
    return {
        "id_propietario": gen_uuid(),
        "id_vehiculo": id_vehiculo,
        "tipo_documento": td,
        "numero_documento": nd,
        "nombre_completo": nombre,
        "direccion": maybe(f"{pick(CALLES)}, {random.randint(1,100)}", 0.2),
        "telefono": maybe(gen_telefono(), 0.35),
        "email": maybe(gen_email(nombre), 0.45),
    }

def gen_conductor(id_vehiculo):
    nombre, td, nd = gen_persona(pick(["DNI","NIE","PASAPORTE"],[85,10,5]))
    return {
        "id_conductor": gen_uuid(),
        "id_vehiculo": id_vehiculo,
        "tipo_documento": td,
        "numero_documento": nd,
        "nombre_completo": nombre,
        "direccion": maybe(f"{pick(CALLES)}, {random.randint(1,100)}", 0.25),
    }

ESTADOS_W = {
    "normal":      (["INICIADA","DOCUMENTACION_PENDIENTE","EN_VALORACION","EN_LIQUIDACION","PAGADA"],  [15,20,25,20,20]),
    "boundary":    (["DENEGADA","BAJA","DOCUMENTACION_PENDIENTE","EN_VALORACION"],                     [35,30,20,15]),
    "exceptional": (["BAJA","DENEGADA","PAGADA"],                                                      [40,40,20]),
}

def gen_reclamacion(id_siniestro, tipo_dano, escenario, created_at):
    tipo_rec = "GESTION" if tipo_dano == "DP" else \
               pick(["GESTION","REEMBOLSO_SIN_FRANQUICIA","REEMBOLSO_CON_FRANQUICIA"],[55,30,15])
    cobertura = pick(["SEGURO_DIRECTO","ROBADO","SIN_SEGURO"],[70,18,12])
    vals, ws  = ESTADOS_W[escenario]
    estado    = pick(vals, ws)
    motivo_den = pick(["Falta documentación obligatoria",
                        "Prescripción de la reclamación",
                        "Responsabilidad no acreditada",
                        "Datos incorrectos del vehículo causante",
                        "Cobertura no aplicable al CCS"]) if estado == "DENEGADA" else None
    ca_date = date.fromisoformat(created_at[:10])
    upd = rand_datetime(ca_date, offset_days=random.randint(0,90))
    return {
        "id_reclamacion": gen_uuid(),
        "id_siniestro": id_siniestro,
        "referencia_expediente_ccs": maybe(f"CCS-{ca_date.year}-{random.randint(10000,99999)}", 0.25),
        "referencia_tramitacion_ccs": maybe(f"TRAM-{ca_date.year}-{random.randint(10000,99999)}", 0.25),
        "tipo_reclamacion": tipo_rec,
        "tipo_dano": tipo_dano,
        "cobertura": cobertura,
        "estado": estado,
        "motivo_denegacion": motivo_den,
        "reclamacion_en_nombre_de": pick(["ASEGURADO","ENTIDAD"],[75,25]),
        "created_at": created_at,
        "updated_at": upd,
    }

def gen_lesionado(id_reclamacion, escenario):
    nombre, td, nd = gen_persona(pick(["DNI","NIE","PASAPORTE","SIN_DOCUMENTO"],[80,8,5,7]))
    if td == "SIN_DOCUMENTO":
        nd = "FICTICIO"
    # Tipo de lesión: solo uno puede ser true
    tipos = ["incapacidad_temporal","incapacidad_permanente","gran_invalidez","fallecido"]
    if escenario == "exceptional":
        ws_les = [40, 25, 15, 20]
    elif escenario == "boundary":
        ws_les = [50, 30, 15, 5]
    else:
        ws_les = [80, 12, 5, 3]
    tipo_les = pick(tipos, ws_les)
    ciudad = ciudad_entry()
    return {
        "id_lesionado": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "tipo_documento": td,
        "numero_documento": nd,
        "nombre_completo": nombre,
        "condicion_victima": pick(["CONDUCTOR","PASAJERO","PEATON","CICLISTA"],[40,35,20,5]),
        "descripcion_lesiones": pick(DESC_DP),
        "incapacidad_temporal": tipo_les == "incapacidad_temporal",
        "incapacidad_permanente": tipo_les == "incapacidad_permanente",
        "gran_invalidez": tipo_les == "gran_invalidez",
        "fallecido": tipo_les == "fallecido",
        "domicilio": maybe(f"{pick(CALLES)}, {random.randint(1,100)}", 0.3),
        "telefono": maybe(gen_telefono(), 0.4),
        "centro_hospitalario": maybe(pick(HOSPITALES), 0.5),
    }

def gen_perjudicado(id_reclamacion):
    nombre, td, nd = gen_persona()
    ciudad = ciudad_entry()
    return {
        "id_perjudicado": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "tipo_documento": td,
        "numero_documento": nd,
        "nombre_completo": nombre,
        "domicilio": f"{pick(CALLES)}, {random.randint(1,100)}",
        "codigo_postal": maybe(cp_for(ciudad), 0.2),
        "provincia": ciudad["provincia"],
        "telefono": maybe(gen_telefono(), 0.35),
        "email": maybe(gen_email(nombre), 0.5),
    }

TIPOS_DOC_BASE = ["DECLARACION_ACCIDENTE","ATESTADO_POLICIAL","DECLARACION_TESTIGOS",
                  "PRESUPUESTO_REPARACION","INFORME_PERICIAL","FACTURA_REPARACION"]
TIPOS_DOC_DP   = ["DECLARACION_ACCIDENTE","INFORME_MEDICO","INFORME_FORENSE","PARTE_BAJA_ALTA"]
TIPOS_DOC_DV   = ["DECLARACION_ACCIDENTE","PRESUPUESTO_REPARACION","FACTURA_REPARACION"]

def gen_documentos(id_reclamacion, tipo_dano, cobertura, tipo_rec, created_at):
    docs = []
    cr_date = date.fromisoformat(created_at[:10])

    # DECLARACION_ACCIDENTE siempre
    docs.append({
        "id_documento": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "tipo_documento": "DECLARACION_ACCIDENTE",
        "formato": pick(["PDF","JPG"],[85,15]),
        "nombre_fichero": f"declaracion_accidente_{cr_date.strftime('%Y%m%d')}.pdf",
        "tamano_kb": random.randint(200, 2000),
        "fecha_subida": rand_datetime(cr_date, offset_days=0),
        "descargado_por_ccs": random.random() < 0.6,
    })

    # Según tipo_dano
    pool = TIPOS_DOC_BASE if tipo_dano == "DM" else (TIPOS_DOC_DP if tipo_dano == "DP" else TIPOS_DOC_DV)
    candidates = [t for t in pool if t != "DECLARACION_ACCIDENTE"]
    k = min(random.randint(1, 3), len(candidates))
    add = random.sample(candidates, k=k)
    for t in add:
        ext = "pdf" if t not in ["PRESUPUESTO_REPARACION","FACTURA_REPARACION"] else pick(["pdf","xls"],[70,30])
        docs.append({
            "id_documento": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_documento": t,
            "formato": ext.upper(),
            "nombre_fichero": f"{t.lower()}_{cr_date.strftime('%Y%m%d')}.{ext}",
            "tamano_kb": random.randint(50, 3000),
            "fecha_subida": rand_datetime(cr_date, offset_days=random.randint(0,5)),
            "descargado_por_ccs": random.random() < 0.5,
        })

    # Condicionales
    if cobertura == "ROBADO":
        docs.append({
            "id_documento": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_documento": "DENUNCIA_SUSTRACCION",
            "formato": "PDF",
            "nombre_fichero": f"denuncia_sustraccion_{cr_date.strftime('%Y%m%d')}.pdf",
            "tamano_kb": random.randint(100,1500),
            "fecha_subida": rand_datetime(cr_date, offset_days=random.randint(0,3)),
            "descargado_por_ccs": random.random() < 0.55,
        })

    if tipo_rec.startswith("REEMBOLSO"):
        docs.append({
            "id_documento": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_documento": "DOCUMENTO_PAGO",
            "formato": "PDF",
            "nombre_fichero": f"acreditativo_pago_{cr_date.strftime('%Y%m%d')}.pdf",
            "tamano_kb": random.randint(100,1200),
            "fecha_subida": rand_datetime(cr_date, offset_days=random.randint(1,7)),
            "descargado_por_ccs": random.random() < 0.6,
        })

    # Clamp tamaño
    for d in docs:
        d["tamano_kb"] = max(1, min(3072, d["tamano_kb"]))
    return docs

def gen_importes(id_reclamacion, tipo_dano, tipo_rec, estado):
    if estado not in ("EN_LIQUIDACION","PAGADA","EN_VALORACION"):
        return []
    importes = []
    if tipo_dano == "DM":
        concepto = "DANOS_VEHICULO"
        rango = (500, 15000)
    elif tipo_dano == "DP":
        concepto = "DANOS_PERSONALES"
        rango = (5000, 100000)
    else:
        concepto = "DANOS_DIVERSOS"
        rango = (100, 10000)

    base = round(random.uniform(*rango), 2)
    importes.append({
        "id_importe": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "tipo_importe": "RECLAMADO",
        "concepto": concepto,
        "importe": base,
        "moneda": "EUR",
        "destinatario": pick(["PERJUDICADO","ENTIDAD","TALLER"],[50,30,20]),
        "descripcion": maybe(pick(DESC_DM), 0.3),
    })

    if estado in ("EN_LIQUIDACION","PAGADA"):
        val_ccs = round(base * random.uniform(0.7, 1.0), 2)
        importes.append({
            "id_importe": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_importe": "VALORADO_CCS",
            "concepto": concepto,
            "importe": val_ccs,
            "moneda": "EUR",
            "destinatario": importes[0]["destinatario"],
            "descripcion": maybe("Importe valorado por el CCS", 0.2),
        })

    if estado == "PAGADA":
        importes.append({
            "id_importe": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_importe": "LIQUIDADO",
            "concepto": concepto,
            "importe": importes[-1]["importe"],
            "moneda": "EUR",
            "destinatario": importes[0]["destinatario"],
            "descripcion": "Pago realizado por el CCS",
        })

    if tipo_rec == "REEMBOLSO_CON_FRANQUICIA":
        importes.append({
            "id_importe": gen_uuid(),
            "id_reclamacion": id_reclamacion,
            "tipo_importe": "RECLAMADO",
            "concepto": "FRANQUICIA",
            "importe": round(random.uniform(300, 1500), 2),
            "moneda": "EUR",
            "destinatario": "PERJUDICADO",
            "descripcion": "Importe de franquicia",
        })
    return importes

def gen_datos_bancarios(id_reclamacion, estado):
    if estado not in ("EN_LIQUIDACION","PAGADA"):
        return None
    nombre = gen_nombre_completo()
    return {
        "id_datos_bancarios": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "tipo_beneficiario": pick(["ENTIDAD","PERJUDICADO","LESIONADO","TALLER"],[35,40,15,10]),
        "titular_cuenta": nombre,
        "iban": gen_iban_es(),
        "entidad_financiera": pick(["BBVA","Santander","CaixaBank","Bankia","Sabadell",
                                    "Bankinter","ING","Unicaja","Kutxabank"]),
        "swift_bic": maybe(fake.bothify("????ES??###").upper(), 0.3),
    }

def gen_taller(id_reclamacion):
    ape = pick(APELLIDOS)
    ciudad = ciudad_entry()
    tel = gen_telefono()
    return {
        "id_taller": gen_uuid(),
        "id_reclamacion": id_reclamacion,
        "cif": gen_cif(),
        "razon_social": f"Talleres {ape} S.L.",
        "direccion": f"Polígono Industrial, {pick(CALLES)} {random.randint(1,50)}",
        "telefono": tel,
        "email": maybe(f"taller.{ape.lower()}@talleres.es", 0.4),
    }

# ── Orquestador principal ─────────────────────────────────────

def run():
    # Tablas
    siniestros, reclamaciones, vehiculos = [], [], []
    propietarios, conductores = [], []
    lesionados, perjudicados = [], []
    documentos, importes = [], []
    datos_bancarios, datos_judiciales, talleres = [], [], []

    for i in range(1, NUM_SINIESTROS + 1):
        # Escenario
        r = random.random()
        if r < 0.70:
            escenario = "normal"
        elif r < 0.90:
            escenario = "boundary"
        else:
            escenario = "exceptional"

        # SINIESTRO
        sin = gen_siniestro(i)
        siniestros.append(sin)
        sid = sin["id_siniestro"]

        # DATOS JUDICIALES
        if sin["hay_actuaciones_judiciales"]:
            datos_judiciales.append(gen_datos_judiciales(sid, sin["fecha_siniestro"]))

        # VEHÍCULOS
        veh_c = gen_vehiculo(sid, "CAUSANTE")
        vehiculos.append(veh_c)
        propietarios.append(gen_propietario(veh_c["id_vehiculo"]))
        conductores.append(gen_conductor(veh_c["id_vehiculo"]))

        n_perj = pick([1,2,3],[65,25,10])
        for _ in range(n_perj):
            vehiculos.append(gen_vehiculo(sid, "PERJUDICADO"))

        # RECLAMACIONES
        tipos_presentes = [pick(["DM","DP","DV"],[60,30,10])]
        if escenario in ("boundary","exceptional") and random.random() < 0.4:
            extra = [t for t in ["DM","DP","DV"] if t not in tipos_presentes]
            tipos_presentes.append(pick(extra))

        for tipo in tipos_presentes:
            rec = gen_reclamacion(sid, tipo, escenario, sin["created_at"])
            reclamaciones.append(rec)
            rid = rec["id_reclamacion"]

            # LESIONADOS (solo DP)
            if tipo == "DP":
                n_les = pick([1,2,3,4],[55,30,10,5]) if escenario != "normal" else pick([1,2],[80,20])
                for _ in range(n_les):
                    lesionados.append(gen_lesionado(rid, escenario))
            else:
                perjudicados.append(gen_perjudicado(rid))

            # DOCUMENTOS
            documentos.extend(gen_documentos(rid, tipo, rec["cobertura"], rec["tipo_reclamacion"], rec["created_at"]))

            # IMPORTES
            importes.extend(gen_importes(rid, tipo, rec["tipo_reclamacion"], rec["estado"]))

            # DATOS BANCARIOS
            db = gen_datos_bancarios(rid, rec["estado"])
            if db:
                datos_bancarios.append(db)

            # TALLER (DM)
            if tipo == "DM" and rec["estado"] not in ("INICIADA","BAJA","DENEGADA") and random.random() < 0.65:
                talleres.append(gen_taller(rid))

    tables = {
        "siniestros": siniestros,
        "reclamaciones": reclamaciones,
        "vehiculos": vehiculos,
        "propietarios": propietarios,
        "conductores": conductores,
        "lesionados": lesionados,
        "perjudicados": perjudicados,
        "documentos": documentos,
        "importes": importes,
        "datos_bancarios": datos_bancarios,
        "datos_judiciales": datos_judiciales,
        "talleres": talleres,
    }

    # ── Exportar JSON ────────────────────────────────────────
    full_json = {"dataset": "SCCS-Dataset", "version": "1.0.0",
                 "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                 "tables": tables}
    with open(OUT_DIR / "sccs_dataset.json", "w", encoding="utf-8") as f:
        json.dump(full_json, f, ensure_ascii=False, indent=2, default=str)
    print(f"  [JSON] sccs_dataset.json")

    # JSON por tabla
    for name, rows in tables.items():
        with open(OUT_DIR / f"sccs_{name}.json", "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2, default=str)
        print(f"  [JSON] sccs_{name}.json ({len(rows)} registros)")

    # ── Exportar SQL ─────────────────────────────────────────
    def sql_val(v):
        if v is None:
            return "NULL"
        if isinstance(v, bool):
            return "TRUE" if v else "FALSE"
        if isinstance(v, (int, float)):
            return str(v)
        return "'" + str(v).replace("'","''") + "'"

    def rows_to_sql(table_name, rows):
        if not rows:
            return f"-- Tabla {table_name}: sin registros\n"
        cols = list(rows[0].keys())
        lines = [f"-- Tabla: {table_name} ({len(rows)} registros)"]
        for r in rows:
            vals = ", ".join(sql_val(r.get(c)) for c in cols)
            lines.append(f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({vals});")
        return "\n".join(lines) + "\n"

    ddl = """
-- ============================================================
-- SCCS Dataset - Scripts SQL de inserción
-- Generado: {ts}
-- ============================================================

""".format(ts=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    sql_path = OUT_DIR / "sccs_dataset.sql"
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(ddl)
        for name, rows in tables.items():
            f.write(rows_to_sql(name, rows))
            f.write("\n")
    print(f"  [SQL ] sccs_dataset.sql")

    # ── Muestras (5 registros por tabla) ────────────────────
    samples = {name: rows[:5] for name, rows in tables.items()}
    with open(OUT_DIR / "samples" / "sccs_samples.json", "w", encoding="utf-8") as f:
        json.dump(samples, f, ensure_ascii=False, indent=2, default=str)
    print(f"  [SAMP] sccs_samples.json")

    # ── Métricas ─────────────────────────────────────────────
    total = sum(len(v) for v in tables.values())
    metrics = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "seed": 42,
        "total_records": total,
        "tables": {name: len(rows) for name, rows in tables.items()},
        "formats": ["JSON", "SQL"],
        "samples": True,
    }
    with open(OUT_DIR / "../metadata/generation_metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    print(f"\n  TOTAL registros generados: {total}")
    return metrics

if __name__ == "__main__":
    import time
    print("\n=== Generando dataset SCCS ===")
    t0 = time.time()
    m  = run()
    elapsed = round(time.time() - t0, 2)
    print(f"  Duración: {elapsed}s")
    print("=== Generación completada ===\n")
