#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Knowmadmood Comunidad QA
# SPDX-License-Identifier: GPL-3.0-only
"""
Validador de calidad - Dataset sintetico
Dimensiones: Completitud, Validez, Unicidad, Consistencia, Integridad Referencial
"""
import json
import re
from pathlib import Path
from datetime import datetime, date

DATASETS = Path("/home/amartinez/Documentos/DEMO_IA/Demo_SyntheticData/Datos/datasets")
VALIDATION_DIR = Path("/home/amartinez/Documentos/DEMO_IA/Demo_SyntheticData/Datos/metadata")

def load(name):
    with open(DATASETS / f"{name}.json", encoding="utf-8") as f:
        return json.load(f)

# ---------------------------------------------------------------------------
reclamaciones     = load("reclamaciones")
siniestros        = load("siniestros")
propietarios      = load("propietarios_causante")
conductores       = load("conductores_causante")
vehiculos_danados = load("vehiculos_danados")
victimas          = load("victimas")
comunicaciones    = load("comunicaciones")
documentos        = load("documentos")
pagos             = load("pagos")

errors   = []
warnings = []

def err(entity, rec_id, field, msg):
    errors.append({"entity": entity, "id": rec_id, "field": field, "message": msg})

def warn(entity, rec_id, field, msg):
    warnings.append({"entity": entity, "id": rec_id, "field": field, "message": msg})

# ---------------------------------------------------------------------------
# 1. UNICIDAD DE PKs
# ---------------------------------------------------------------------------
def check_pk_uniqueness(rows, pk_field, entity):
    ids = [r[pk_field] for r in rows]
    dupes = len(ids) - len(set(ids))
    if dupes > 0:
        err(entity, "GLOBAL", pk_field, f"{dupes} IDs duplicados")
    return dupes

pk_dupes = 0
pk_dupes += check_pk_uniqueness(reclamaciones, "id_reclamacion", "Reclamacion")
pk_dupes += check_pk_uniqueness(siniestros, "id_siniestro", "Siniestro")
pk_dupes += check_pk_uniqueness(propietarios, "id_propietario", "PropietarioCausante")
pk_dupes += check_pk_uniqueness(conductores, "id_conductor", "ConductorCausante")
pk_dupes += check_pk_uniqueness(vehiculos_danados, "id_vehiculo_danado", "DatosVehiculoDanado")
pk_dupes += check_pk_uniqueness(victimas, "id_victima", "Victima")
pk_dupes += check_pk_uniqueness(comunicaciones, "id_comunicacion", "Comunicacion")
pk_dupes += check_pk_uniqueness(documentos, "id_documento", "Documento")
pk_dupes += check_pk_uniqueness(pagos, "id_pago", "Pago")

# Unicidad referencia_entidad
refs = [r["referencia_entidad"] for r in reclamaciones]
ref_dupes = len(refs) - len(set(refs))
if ref_dupes > 0:
    err("Reclamacion", "GLOBAL", "referencia_entidad", f"{ref_dupes} referencias duplicadas")

# ---------------------------------------------------------------------------
# 2. INTEGRIDAD REFERENCIAL
# ---------------------------------------------------------------------------
rec_ids = {r["id_reclamacion"] for r in reclamaciones}

def check_fk(rows, entity, fk_field, parent_ids):
    broken = 0
    for r in rows:
        val = r.get(fk_field)
        if val and val not in parent_ids:
            err(entity, r.get(list(r.keys())[0]), fk_field, f"FK {val} no existe en padre")
            broken += 1
    return broken

fk_errors = 0
fk_errors += check_fk(siniestros, "Siniestro", "id_reclamacion", rec_ids)
fk_errors += check_fk(propietarios, "PropietarioCausante", "id_reclamacion", rec_ids)
fk_errors += check_fk(conductores, "ConductorCausante", "id_reclamacion", rec_ids)
fk_errors += check_fk(vehiculos_danados, "DatosVehiculoDanado", "id_reclamacion", rec_ids)
fk_errors += check_fk(victimas, "Victima", "id_reclamacion", rec_ids)
fk_errors += check_fk(comunicaciones, "Comunicacion", "id_reclamacion", rec_ids)
fk_errors += check_fk(documentos, "Documento", "id_reclamacion", rec_ids)
fk_errors += check_fk(pagos, "Pago", "id_reclamacion", rec_ids)

# ---------------------------------------------------------------------------
# 3. COMPLETITUD - campos obligatorios
# ---------------------------------------------------------------------------
REQUIRED = {
    "Reclamacion": ["id_reclamacion","referencia_entidad","codigo_entidad_dgs",
                    "tipo_tramitacion","tipo_reclamacion","cobertura","estado",
                    "fecha_alta","indicador_leido","tiene_actuaciones_judiciales"],
    "Siniestro":   ["id_siniestro","id_reclamacion","matricula_causante",
                    "fecha_siniestro","descripcion_siniestro","lugar_ocurrencia",
                    "localidad","provincia","existencia_atestado","circunstancia"],
}
completeness_errors = 0
for r in reclamaciones:
    for f in REQUIRED["Reclamacion"]:
        if r.get(f) is None or r.get(f) == "":
            err("Reclamacion", r["id_reclamacion"], f, "Campo obligatorio nulo")
            completeness_errors += 1
for s in siniestros:
    for f in REQUIRED["Siniestro"]:
        if s.get(f) is None or s.get(f) == "":
            err("Siniestro", s["id_siniestro"], f, "Campo obligatorio nulo")
            completeness_errors += 1

# ---------------------------------------------------------------------------
# 4. VALIDEZ - enums, formatos, rangos
# ---------------------------------------------------------------------------
validity_errors = 0

VALID_TIPO_TRAM  = {"DM","DP","DV"}
VALID_TIPO_REC   = {"GESTION","REEMBOLSO_SIN_FRANQUICIA","REEMBOLSO_CON_FRANQUICIA"}
VALID_COBERTURA  = {"SEGURO_DIRECTO","ROBADO","SIN_SEGURO"}
VALID_ESTADOS    = {"ABIERTA","LIQUIDADA","DENEGADA","BAJA_SOLICITADA","BAJA_ERROR_DATOS","BAJA_GESTION_DIRECTA"}
VALID_SN         = {"S","N"}
DATE_PATTERN     = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MATRICULA_PATTERN= re.compile(r"^\d{4}[A-Z]{3}$")

for r in reclamaciones:
    rid = r["id_reclamacion"]
    if r["tipo_tramitacion"] not in VALID_TIPO_TRAM:
        err("Reclamacion", rid, "tipo_tramitacion", f"Valor invalido: {r['tipo_tramitacion']}")
        validity_errors += 1
    if r["tipo_reclamacion"] not in VALID_TIPO_REC:
        err("Reclamacion", rid, "tipo_reclamacion", f"Valor invalido: {r['tipo_reclamacion']}")
        validity_errors += 1
    if r["cobertura"] not in VALID_COBERTURA:
        err("Reclamacion", rid, "cobertura", f"Valor invalido: {r['cobertura']}")
        validity_errors += 1
    if r["estado"] not in VALID_ESTADOS:
        err("Reclamacion", rid, "estado", f"Valor invalido: {r['estado']}")
        validity_errors += 1
    if r["indicador_leido"] not in VALID_SN:
        err("Reclamacion", rid, "indicador_leido", f"Valor invalido: {r['indicador_leido']}")
        validity_errors += 1
    # DP solo permite GESTION
    if r["tipo_tramitacion"] == "DP" and r["tipo_reclamacion"] != "GESTION":
        err("Reclamacion", rid, "tipo_reclamacion", "DP solo puede ser GESTION")
        validity_errors += 1

for s in siniestros:
    sid = s["id_siniestro"]
    if s.get("matricula_causante") and not MATRICULA_PATTERN.match(s["matricula_causante"]):
        warn("Siniestro", sid, "matricula_causante", f"Formato atipico: {s['matricula_causante']}")
    if s.get("fecha_siniestro") and not DATE_PATTERN.match(s["fecha_siniestro"]):
        err("Siniestro", sid, "fecha_siniestro", "Formato de fecha invalido")
        validity_errors += 1

# Tipo documento valido
VALID_TIPOS_DOC = {940,941,942,943,944,945,946,947,948,949,950,951,954}
for d in documentos:
    if d["tipo_documento"] not in VALID_TIPOS_DOC:
        err("Documento", d["id_documento"], "tipo_documento", f"Tipo invalido: {d['tipo_documento']}")
        validity_errors += 1
    if d["tamano_bytes"] > 3145728:
        err("Documento", d["id_documento"], "tamano_bytes", f"Supera 3MB: {d['tamano_bytes']}")
        validity_errors += 1

# ---------------------------------------------------------------------------
# 5. CONSISTENCIA
# ---------------------------------------------------------------------------
consistency_errors = 0
rec_map = {r["id_reclamacion"]: r for r in reclamaciones}

# fecha_siniestro < fecha_alta
for s in siniestros:
    r = rec_map.get(s["id_reclamacion"])
    if r and s.get("fecha_siniestro") and r.get("fecha_alta"):
        if s["fecha_siniestro"] >= r["fecha_alta"]:
            err("Siniestro", s["id_siniestro"], "fecha_siniestro",
                f"fecha_siniestro {s['fecha_siniestro']} >= fecha_alta {r['fecha_alta']}")
            consistency_errors += 1

# fecha_baja > fecha_alta cuando existe
for r in reclamaciones:
    if r.get("fecha_baja") and r.get("fecha_alta"):
        if r["fecha_baja"] <= r["fecha_alta"]:
            err("Reclamacion", r["id_reclamacion"], "fecha_baja",
                "fecha_baja debe ser posterior a fecha_alta")
            consistency_errors += 1

# Estado LIQUIDADA -> debe existir pago
pago_recs = {p["id_reclamacion"] for p in pagos}
for r in reclamaciones:
    if r["estado"] == "LIQUIDADA" and r["id_reclamacion"] not in pago_recs:
        err("Reclamacion", r["id_reclamacion"], "estado",
            "Estado LIQUIDADA sin registro de Pago asociado")
        consistency_errors += 1

# Victimas solo en DP
dp_recs = {r["id_reclamacion"] for r in reclamaciones if r["tipo_tramitacion"] == "DP"}
for v in victimas:
    if v["id_reclamacion"] not in dp_recs:
        err("Victima", v["id_victima"], "id_reclamacion",
            "Victima vinculada a reclamacion que no es DP")
        consistency_errors += 1

# DatosVehiculoDanado solo en DM
dm_recs = {r["id_reclamacion"] for r in reclamaciones if r["tipo_tramitacion"] == "DM"}
for vd in vehiculos_danados:
    if vd["id_reclamacion"] not in dm_recs:
        err("DatosVehiculoDanado", vd["id_vehiculo_danado"], "id_reclamacion",
            "VehiculoDanado vinculado a reclamacion que no es DM")
        consistency_errors += 1

# Judicial: si tiene_actuaciones_judiciales=S deben existir juzgado y num procedimiento
for r in reclamaciones:
    if r["tiene_actuaciones_judiciales"] == "S":
        if not r.get("juzgado"):
            err("Reclamacion", r["id_reclamacion"], "juzgado",
                "Falta juzgado cuando tiene_actuaciones_judiciales=S")
            consistency_errors += 1
        if not r.get("numero_procedimiento_judicial"):
            err("Reclamacion", r["id_reclamacion"], "numero_procedimiento_judicial",
                "Falta numero_procedimiento_judicial cuando tiene_actuaciones_judiciales=S")
            consistency_errors += 1

# Pagos: importe_entidad + importe_asegurado coherente con perceptor=AMBOS
for p in pagos:
    if p["perceptor"] == "AMBOS":
        ie = p.get("importe_entidad") or 0
        ia = p.get("importe_asegurado") or 0
        total = p.get("importe_total") or 0
        if abs((ie + ia) - total) > 0.02:
            err("Pago", p["id_pago"], "importe_total",
                f"importe_entidad+importe_asegurado ({ie+ia}) != importe_total ({total})")
            consistency_errors += 1

# Victimas: al menos un indicador S
for v in victimas:
    indicadores = [v.get("incapacidad_temporal"), v.get("incapacidad_permanente"),
                   v.get("gran_invalidez"), v.get("muerte")]
    if all(i != "S" for i in indicadores):
        err("Victima", v["id_victima"], "indicadores",
            "Ninguno de los indicadores de dano es S")
        consistency_errors += 1

# ---------------------------------------------------------------------------
# 6. METRICAS DE COMPLETITUD
# ---------------------------------------------------------------------------
def completeness_pct(rows, required_fields):
    total = len(rows) * len(required_fields)
    if total == 0:
        return 100.0
    present = sum(1 for r in rows for f in required_fields if r.get(f) not in (None, ""))
    return round(present / total * 100, 2)

comp_rec = completeness_pct(reclamaciones, REQUIRED["Reclamacion"])
comp_sin = completeness_pct(siniestros, REQUIRED["Siniestro"])

# ---------------------------------------------------------------------------
# TOTALES Y SCORE
# ---------------------------------------------------------------------------
total_records = (len(reclamaciones) + len(siniestros) + len(propietarios) +
                 len(conductores) + len(vehiculos_danados) + len(victimas) +
                 len(comunicaciones) + len(documentos) + len(pagos))

total_errors = pk_dupes + ref_dupes + fk_errors + completeness_errors + validity_errors + consistency_errors
quality_score = round(max(0, (1 - total_errors / max(total_records, 1)) * 100), 2)

# ---------------------------------------------------------------------------
# REPORTE
# ---------------------------------------------------------------------------
report = {
    "generated_at": datetime.now().isoformat(),
    "project": "SCCS",
    "dataset_version": "1.0.0",
    "summary": {
        "total_records": total_records,
        "total_errors": total_errors,
        "total_warnings": len(warnings),
        "quality_score": quality_score,
        "status": "APROBADO" if quality_score >= 98 else "REVISION_REQUERIDA"
    },
    "entities": {
        "reclamaciones":         len(reclamaciones),
        "siniestros":            len(siniestros),
        "propietarios_causante": len(propietarios),
        "conductores_causante":  len(conductores),
        "vehiculos_danados":     len(vehiculos_danados),
        "victimas":              len(victimas),
        "comunicaciones":        len(comunicaciones),
        "documentos":            len(documentos),
        "pagos":                 len(pagos),
    },
    "dimensions": {
        "unicidad": {
            "pk_duplicados": pk_dupes,
            "referencia_entidad_duplicados": ref_dupes,
            "score": "100%" if pk_dupes + ref_dupes == 0 else f"{pk_dupes + ref_dupes} errores"
        },
        "integridad_referencial": {
            "fk_rotos": fk_errors,
            "score": "100%" if fk_errors == 0 else f"{fk_errors} errores"
        },
        "completitud": {
            "reclamaciones_pct": comp_rec,
            "siniestros_pct": comp_sin,
            "errores_campos_obligatorios": completeness_errors
        },
        "validez": {
            "errores": validity_errors
        },
        "consistencia": {
            "errores": consistency_errors
        }
    },
    "errors": errors[:50],
    "warnings": warnings[:20],
}

out_path = VALIDATION_DIR / "quality_report.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------
# CONSOLA
# ---------------------------------------------------------------------------
print("=" * 60)
print("  INFORME DE CALIDAD - DATASET SCCS")
print("=" * 60)
print(f"  Registros totales     : {total_records}")
print(f"  Errores encontrados   : {total_errors}")
print(f"  Avisos                : {len(warnings)}")
print(f"  Quality Score         : {quality_score}%")
print(f"  Estado                : {report['summary']['status']}")
print()
print("  Dimension                    Resultado")
print("  " + "-"*45)
print(f"  Unicidad (PKs)               {'OK' if pk_dupes+ref_dupes==0 else 'FALLO'} ({pk_dupes+ref_dupes} errores)")
print(f"  Integridad Referencial       {'OK' if fk_errors==0 else 'FALLO'} ({fk_errors} errores)")
print(f"  Completitud Reclamaciones    {comp_rec}%")
print(f"  Completitud Siniestros       {comp_sin}%")
print(f"  Validez                      {'OK' if validity_errors==0 else 'FALLO'} ({validity_errors} errores)")
print(f"  Consistencia                 {'OK' if consistency_errors==0 else 'FALLO'} ({consistency_errors} errores)")
print()
if errors:
    print(f"  Primeros errores detectados:")
    for e in errors[:5]:
        print(f"    [{e['entity']}] {e['field']}: {e['message']}")
print()
print(f"  Reporte guardado en: {out_path}")
print("=" * 60)
