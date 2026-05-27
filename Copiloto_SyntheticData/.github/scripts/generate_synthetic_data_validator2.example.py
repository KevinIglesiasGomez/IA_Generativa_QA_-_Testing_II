#!/usr/bin/env python3
"""
Validador de Calidad - Dataset SCCS
Step 4: Validación y Exportación
"""
import json, re, math
from pathlib import Path
from datetime import datetime, timezone, date

BASE     = Path(__file__).parent
DS_DIR   = BASE / "datasets"
OUT_VAL  = BASE / "validation_reports"
OUT_QUAL = BASE / "quality_reports"
OUT_VAL.mkdir(exist_ok=True)
OUT_QUAL.mkdir(exist_ok=True)

def load(name):
    p = DS_DIR / f"sccs_{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []

# ── Carga de tablas ──────────────────────────────────────────
sin  = load("siniestros")
rec  = load("reclamaciones")
veh  = load("vehiculos")
prop = load("propietarios")
cond = load("conductores")
les  = load("lesionados")
perj = load("perjudicados")
docs = load("documentos")
imp  = load("importes")
db   = load("datos_bancarios")
dj   = load("datos_judiciales")
tal  = load("talleres")

ALL = {
    "siniestros": sin, "reclamaciones": rec, "vehiculos": veh,
    "propietarios": prop, "conductores": cond, "lesionados": les,
    "perjudicados": perj, "documentos": docs, "importes": imp,
    "datos_bancarios": db, "datos_judiciales": dj, "talleres": tal,
}

total_records = sum(len(v) for v in ALL.values())
errors   = []
warnings = []

def err(table, field, row_id, msg, severity="error"):
    entry = {"table": table, "id": str(row_id), "field": field,
             "message": msg, "severity": severity}
    if severity == "error":
        errors.append(entry)
    else:
        warnings.append(entry)

# ── COMPLETITUD ──────────────────────────────────────────────
REQUIRED = {
    "siniestros":     ["id_siniestro","referencia_entidad","fecha_siniestro","lugar",
                       "localidad","provincia","descripcion_accidente",
                       "existencia_atestado","hay_actuaciones_judiciales",
                       "codigo_entidad_acreedora","nombre_entidad_acreedora","created_at"],
    "reclamaciones":  ["id_reclamacion","id_siniestro","tipo_reclamacion","tipo_dano",
                       "cobertura","estado","reclamacion_en_nombre_de","created_at","updated_at"],
    "vehiculos":      ["id_vehiculo","id_siniestro","tipo_vehiculo","matricula","marca","modelo"],
    "propietarios":   ["id_propietario","id_vehiculo","tipo_documento","nombre_completo"],
    "conductores":    ["id_conductor","id_vehiculo","tipo_documento","nombre_completo"],
    "lesionados":     ["id_lesionado","id_reclamacion","nombre_completo","condicion_victima",
                       "descripcion_lesiones","incapacidad_temporal","incapacidad_permanente",
                       "gran_invalidez","fallecido"],
    "perjudicados":   ["id_perjudicado","id_reclamacion","tipo_documento","numero_documento",
                       "nombre_completo","domicilio"],
    "documentos":     ["id_documento","id_reclamacion","tipo_documento","formato",
                       "nombre_fichero","tamano_kb","fecha_subida","descargado_por_ccs"],
    "importes":       ["id_importe","id_reclamacion","tipo_importe","concepto","importe","moneda"],
    "datos_bancarios":["id_datos_bancarios","id_reclamacion","tipo_beneficiario",
                       "titular_cuenta","iban"],
    "datos_judiciales":["id_datos_judiciales","id_siniestro","juzgado","numero_procedimiento"],
    "talleres":       ["id_taller","id_reclamacion","cif","razon_social","direccion","telefono"],
}

completeness_results = {}
total_req_checks = 0
total_req_pass   = 0

for tname, rows in ALL.items():
    req_fields = REQUIRED.get(tname, [])
    null_counts = {f: 0 for f in req_fields}
    for row in rows:
        for f in req_fields:
            total_req_checks += 1
            v = row.get(f)
            if v is None or v == "":
                null_counts[f] += 1
                err(tname, f, row.get(f"id_{tname[:-1]}", "?"),
                    f"Campo obligatorio nulo: {f}")
            else:
                total_req_pass += 1
    completeness_results[tname] = {
        "rows": len(rows),
        "required_fields": len(req_fields),
        "null_counts": null_counts,
    }

completeness_score = round(total_req_pass / total_req_checks * 100, 2) if total_req_checks else 100.0

# ── UNICIDAD ─────────────────────────────────────────────────
UNIQUE_FIELDS = {
    "siniestros":      ["id_siniestro","referencia_entidad"],
    "reclamaciones":   ["id_reclamacion"],
    "vehiculos":       ["id_vehiculo"],
    "propietarios":    ["id_propietario","id_vehiculo"],
    "conductores":     ["id_conductor","id_vehiculo"],
    "lesionados":      ["id_lesionado"],
    "perjudicados":    ["id_perjudicado"],
    "documentos":      ["id_documento"],
    "importes":        ["id_importe"],
    "datos_bancarios": ["id_datos_bancarios"],
    "datos_judiciales":["id_datos_judiciales","id_siniestro"],
    "talleres":        ["id_taller"],
}

unique_checks = 0
unique_pass   = 0

for tname, fields in UNIQUE_FIELDS.items():
    rows = ALL[tname]
    for f in fields:
        unique_checks += 1
        vals = [r.get(f) for r in rows if r.get(f) is not None]
        if len(vals) != len(set(vals)):
            dupes = len(vals) - len(set(vals))
            err(tname, f, "N/A", f"Campo único con {dupes} duplicado(s): {f}")
        else:
            unique_pass += 1

uniqueness_score = round(unique_pass / unique_checks * 100, 2) if unique_checks else 100.0

# ── VALIDEZ (enums, rangos, formatos) ────────────────────────
validity_checks = 0
validity_pass   = 0

ENUMS = {
    "reclamaciones": {
        "tipo_dano":             ["DM","DP","DV"],
        "tipo_reclamacion":      ["GESTION","REEMBOLSO_SIN_FRANQUICIA","REEMBOLSO_CON_FRANQUICIA"],
        "cobertura":             ["SEGURO_DIRECTO","ROBADO","SIN_SEGURO"],
        "estado":                ["INICIADA","DOCUMENTACION_PENDIENTE","EN_VALORACION",
                                  "EN_LIQUIDACION","PAGADA","DENEGADA","BAJA"],
        "reclamacion_en_nombre_de": ["ASEGURADO","ENTIDAD"],
    },
    "vehiculos": {
        "tipo_vehiculo": ["CAUSANTE","PERJUDICADO"],
    },
    "lesionados": {
        "condicion_victima": ["CONDUCTOR","PASAJERO","PEATON","CICLISTA"],
    },
    "documentos": {
        "formato": ["PDF","JPG","PNG","TIF","XLS","TXT"],
        "tipo_documento": ["DECLARACION_ACCIDENTE","ATESTADO_POLICIAL","DECLARACION_TESTIGOS",
                           "PRESUPUESTO_REPARACION","INFORME_PERICIAL","FACTURA_REPARACION",
                           "INFORME_MEDICO","INFORME_FORENSE","PARTE_BAJA_ALTA",
                           "DENUNCIA_SUSTRACCION","BOLETIN_RECUPERACION","CONTROVERSIA",
                           "DOCUMENTO_PAGO","OTROS"],
    },
    "importes": {
        "tipo_importe":  ["RECLAMADO","VALORADO_CCS","LIQUIDADO"],
        "moneda":        ["EUR"],
        "concepto":      ["DANOS_VEHICULO","OTROS_GASTOS_VEHICULO","PARALIZACION",
                          "DANOS_PERSONALES","GASTOS_MEDICOS","GASTOS_SEPELIO",
                          "DANOS_DIVERSOS","FRANQUICIA"],
    },
    "datos_bancarios": {
        "tipo_beneficiario": ["ENTIDAD","PERJUDICADO","LESIONADO","TALLER"],
    },
    "datos_judiciales": {
        "tipo_procedimiento": ["CIVIL","PENAL","ADMINISTRATIVO"],
    },
}

for tname, field_enums in ENUMS.items():
    for row in ALL[tname]:
        for field, allowed in field_enums.items():
            v = row.get(field)
            if v is None:
                continue
            validity_checks += 1
            if v not in allowed:
                err(tname, field, row.get(f"id_{tname[:-1]}","?"),
                    f"Valor '{v}' no está en enum {allowed}")
            else:
                validity_pass += 1

# Rangos
for row in docs:
    validity_checks += 1
    t = row.get("tamano_kb", 0)
    if not (1 <= t <= 3072):
        err("documentos","tamano_kb", row.get("id_documento","?"),
            f"Tamaño {t} KB fuera de rango [1,3072]")
    else:
        validity_pass += 1

for row in imp:
    validity_checks += 1
    v = row.get("importe", 0)
    if not (0.01 <= float(v) <= 999999.99):
        err("importes","importe", row.get("id_importe","?"),
            f"Importe {v} fuera de rango")
    else:
        validity_pass += 1

# Formatos de fecha en siniestros
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
for row in sin:
    validity_checks += 1
    fs = row.get("fecha_siniestro","")
    if not DATE_RE.match(str(fs)):
        err("siniestros","fecha_siniestro", row.get("id_siniestro","?"),
            f"Formato de fecha inválido: {fs}")
    else:
        validity_pass += 1

validity_score = round(validity_pass / validity_checks * 100, 2) if validity_checks else 100.0

# ── CONSISTENCIA ─────────────────────────────────────────────
consist_checks = 0
consist_pass   = 0

# created_at >= fecha_siniestro
for row in sin:
    consist_checks += 1
    fs  = row.get("fecha_siniestro","2000-01-01")
    cat = row.get("created_at","2000-01-01")[:10]
    if cat >= fs:
        consist_pass += 1
    else:
        err("siniestros","created_at", row.get("id_siniestro","?"),
            f"created_at ({cat}) es anterior a fecha_siniestro ({fs})", "warning")

# updated_at >= created_at en reclamaciones
for row in rec:
    consist_checks += 1
    ca  = row.get("created_at","2000-01-01")[:10]
    upd = row.get("updated_at","2000-01-01")[:10]
    if upd >= ca:
        consist_pass += 1
    else:
        err("reclamaciones","updated_at", row.get("id_reclamacion","?"),
            f"updated_at ({upd}) < created_at ({ca})", "warning")

# estado=DENEGADA => motivo_denegacion no nulo
for row in rec:
    if row.get("estado") == "DENEGADA":
        consist_checks += 1
        if row.get("motivo_denegacion"):
            consist_pass += 1
        else:
            err("reclamaciones","motivo_denegacion", row.get("id_reclamacion","?"),
                "Estado DENEGADA sin motivo_denegacion")

# Mutua exclusividad de tipos de lesión
for row in les:
    consist_checks += 1
    flags = [row.get("incapacidad_temporal"), row.get("incapacidad_permanente"),
             row.get("gran_invalidez"), row.get("fallecido")]
    true_count = sum(1 for f in flags if f is True)
    if true_count <= 1:
        consist_pass += 1
    else:
        err("lesionados","tipo_lesion", row.get("id_lesionado","?"),
            f"Más de un tipo de lesión activo ({true_count})")

consistency_score = round(consist_pass / consist_checks * 100, 2) if consist_checks else 100.0

# ── INTEGRIDAD REFERENCIAL ───────────────────────────────────
ref_checks = 0
ref_pass   = 0

sin_ids  = {r["id_siniestro"]  for r in sin}
rec_ids  = {r["id_reclamacion"] for r in rec}
veh_ids  = {r["id_vehiculo"]   for r in veh}

def check_fk(rows, fk_field, valid_set, tname):
    global ref_checks, ref_pass
    for row in rows:
        v = row.get(fk_field)
        if v is None:
            continue
        ref_checks += 1
        if v in valid_set:
            ref_pass += 1
        else:
            err(tname, fk_field, row.get(list(row.keys())[0],"?"),
                f"FK {fk_field}='{v}' no existe en tabla referenciada")

check_fk(rec,  "id_siniestro",   sin_ids,  "reclamaciones")
check_fk(veh,  "id_siniestro",   sin_ids,  "vehiculos")
check_fk(dj,   "id_siniestro",   sin_ids,  "datos_judiciales")
check_fk(prop, "id_vehiculo",    veh_ids,  "propietarios")
check_fk(cond, "id_vehiculo",    veh_ids,  "conductores")
check_fk(les,  "id_reclamacion", rec_ids,  "lesionados")
check_fk(perj, "id_reclamacion", rec_ids,  "perjudicados")
check_fk(docs, "id_reclamacion", rec_ids,  "documentos")
check_fk(imp,  "id_reclamacion", rec_ids,  "importes")
check_fk(db,   "id_reclamacion", rec_ids,  "datos_bancarios")
check_fk(tal,  "id_reclamacion", rec_ids,  "talleres")

# Reglas cruzadas: vehiculo CAUSANTE único por siniestro
causantes_por_sin = {}
for v in veh:
    if v.get("tipo_vehiculo") == "CAUSANTE":
        sid = v["id_siniestro"]
        causantes_por_sin[sid] = causantes_por_sin.get(sid, 0) + 1
for sid, cnt in causantes_por_sin.items():
    ref_checks += 1
    if cnt == 1:
        ref_pass += 1
    else:
        err("vehiculos","tipo_vehiculo", sid,
            f"Siniestro {sid} tiene {cnt} vehículos CAUSANTE (debe ser 1)")

# DM única por siniestro
dm_por_sin = {}
for r in rec:
    if r.get("tipo_dano") == "DM":
        sid = r["id_siniestro"]
        dm_por_sin[sid] = dm_por_sin.get(sid, 0) + 1
for sid, cnt in dm_por_sin.items():
    ref_checks += 1
    if cnt <= 1:
        ref_pass += 1
    else:
        err("reclamaciones","tipo_dano", sid,
            f"Siniestro {sid} tiene {cnt} reclamaciones DM (máx 1)")

# DECLARACION_ACCIDENTE por reclamación
docs_por_rec = {}
for d in docs:
    rid = d["id_reclamacion"]
    if rid not in docs_por_rec:
        docs_por_rec[rid] = []
    docs_por_rec[rid].append(d["tipo_documento"])

for r in rec:
    rid = r["id_reclamacion"]
    ref_checks += 1
    if "DECLARACION_ACCIDENTE" in docs_por_rec.get(rid, []):
        ref_pass += 1
    else:
        err("documentos","tipo_documento", rid,
            f"Reclamación {rid} sin DECLARACION_ACCIDENTE obligatoria")

ri_score = round(ref_pass / ref_checks * 100, 2) if ref_checks else 100.0

# ── SCORE GLOBAL ─────────────────────────────────────────────
dims = {
    "completeness":          completeness_score,
    "validity":              validity_score,
    "uniqueness":            uniqueness_score,
    "consistency":           consistency_score,
    "referential_integrity": ri_score,
}
quality_score = round(sum(dims.values()) / len(dims), 2)

def status(score, critical=99.0, acceptable=95.0):
    if score >= critical:   return "APROBADO"
    if score >= acceptable: return "ADVERTENCIA"
    return "RECHAZADO"

now_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

quality_report = {
    "report_id": "QR-SCCS-001",
    "dataset": "SCCS-Dataset",
    "version": "1.0.0",
    "generated_at": now_ts,
    "total_records": total_records,
    "quality_score": quality_score,
    "overall_status": status(quality_score, 98, 95),
    "dimensions": {
        "completeness":          {"score": completeness_score, "status": status(completeness_score)},
        "validity":              {"score": validity_score,     "status": status(validity_score, 99.9)},
        "uniqueness":            {"score": uniqueness_score,   "status": status(uniqueness_score, 100)},
        "consistency":           {"score": consistency_score,  "status": status(consistency_score)},
        "referential_integrity": {"score": ri_score,           "status": status(ri_score, 100)},
    },
    "summary": {
        "total_errors":   len(errors),
        "total_warnings": len(warnings),
        "tables_validated": len(ALL),
        "tables_detail": {name: len(rows) for name, rows in ALL.items()},
    },
}

# ── Guardar reportes ─────────────────────────────────────────
(OUT_QUAL / "quality_report.json").write_text(
    json.dumps(quality_report, ensure_ascii=False, indent=2), encoding="utf-8")

(OUT_VAL / "validation_errors.json").write_text(
    json.dumps({"errors": errors, "warnings": warnings,
                "total_errors": len(errors), "total_warnings": len(warnings),
                "generated_at": now_ts},
               ensure_ascii=False, indent=2), encoding="utf-8")

# ── Imprimir resumen ─────────────────────────────────────────
print("\n" + "="*60)
print("  REPORTE DE CALIDAD - SCCS Dataset")
print("="*60)
print(f"  Total registros validados : {total_records}")
print(f"  Errores encontrados       : {len(errors)}")
print(f"  Advertencias              : {len(warnings)}")
print("-"*60)
for dim, val in dims.items():
    st = status(val, 99, 95)
    print(f"  {dim:<28} {val:>6.2f}%  [{st}]")
print("-"*60)
print(f"  SCORE GLOBAL              {quality_score:>7.2f}%  [{quality_report['overall_status']}]")
print("="*60)

if errors:
    print(f"\n  Primeros errores:")
    for e in errors[:5]:
        print(f"    [{e['table']}] {e['field']}: {e['message']}")
    if len(errors) > 5:
        print(f"    ... y {len(errors)-5} más (ver validation_reports/validation_errors.json)")

print(f"\n  Reportes guardados en:")
print(f"    quality_reports/quality_report.json")
print(f"    validation_reports/validation_errors.json\n")

