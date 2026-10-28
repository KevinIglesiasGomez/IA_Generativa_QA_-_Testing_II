'use strict';
// API de demostración de Pruebas Seguros para el ejercicio de análisis de pruebas API. Sin dependencias.
const http = require('http');
const crypto = require('crypto');

const PORT = process.env.PORT || 3000;
const BASE = '/api/v1';

const USUARIOS = {
  cliente1: { password: 'Cliente#24', perfil: 'CLIENTE', nombre: 'Lucía Fernández' },
  agente1: { password: 'Agente#24', perfil: 'AGENTE', nombre: 'Marcos Ortega' },
};

const POLIZAS = [
  { idPoliza: 'P-1001', tipo: 'AUTO', descripcion: 'Seat León 1234BCD', titular: 'cliente1', estado: 'VIGENTE', primaAnual: 412.5, fechaInicio: '2026-01-01', fechaFin: '2026-12-31' },
  { idPoliza: 'P-1002', tipo: 'HOGAR', descripcion: 'C/ Alcalá 45, Madrid', titular: 'cliente1', estado: 'VIGENTE', primaAnual: 238.0, fechaInicio: '2026-02-15', fechaFin: '2027-02-14' },
  { idPoliza: 'P-1003', tipo: 'VIDA', descripcion: 'Seguro de vida individual', titular: 'cliente1', estado: 'ANULADA', primaAnual: 120.0, fechaInicio: '2024-03-01', fechaFin: '2025-02-28' },
  { idPoliza: 'P-2001', tipo: 'AUTO', descripcion: 'Renault Clio 5678FGH', titular: 'cliente2', estado: 'VIGENTE', primaAnual: 365.9, fechaInicio: '2026-05-10', fechaFin: '2027-05-09' },
  { idPoliza: 'P-2002', tipo: 'HOGAR', descripcion: 'C/ Mayor 12, Valencia', titular: 'cliente2', estado: 'VIGENTE', primaAnual: 199.0, fechaInicio: '2026-06-01', fechaFin: '2027-05-31' },
];

const TIPOS_SINIESTRO = ['COLISION', 'ROBO', 'INCENDIO', 'AGUA'];
const TIPOS_POLIZA = ['AUTO', 'HOGAR', 'VIDA'];
const sesiones = new Map();
const siniestros = [];
let secuencia = 1000;

function responder(res, estado, cuerpo, cabeceras = {}) {
  const data = cuerpo === undefined ? '' : JSON.stringify(cuerpo);
  res.writeHead(estado, { 'Content-Type': 'application/json; charset=utf-8', ...cabeceras });
  res.end(data);
}

function errorApi(res, estado, codigo, mensaje) {
  responder(res, estado, { error: { codigo, mensaje } });
}

function leerJson(req) {
  return new Promise((resolve, reject) => {
    let raw = '';
    req.on('data', (chunk) => (raw += chunk));
    req.on('end', () => {
      if (!raw) return resolve({});
      try {
        resolve(JSON.parse(raw));
      } catch {
        reject(new Error('JSON_INVALIDO'));
      }
    });
  });
}

function autenticar(req) {
  const cabecera = req.headers.authorization || '';
  const token = cabecera.startsWith('Bearer ') ? cabecera.slice(7) : '';
  const sesion = sesiones.get(token);
  return sesion && sesion.expira > Date.now() ? sesion : null;
}

function visibles(sesion) {
  return sesion.perfil === 'AGENTE' ? POLIZAS : POLIZAS.filter((p) => p.titular === sesion.usuario);
}

function vistaPoliza({ titular, ...resto }) {
  return resto;
}

async function login(req, res) {
  let body;
  try {
    body = await leerJson(req);
  } catch {
    return errorApi(res, 400, 'JSON_INVALIDO', 'El cuerpo de la petición no es un JSON válido.');
  }
  if (!body.usuario || !body.password) {
    return errorApi(res, 400, 'VALIDACION', 'Los campos usuario y password son obligatorios.');
  }
  const datos = USUARIOS[body.usuario];
  if (!datos || datos.password !== body.password) {
    return errorApi(res, 401, 'CREDENCIALES_INVALIDAS', 'Usuario o contraseña incorrectos.');
  }
  const token = crypto.randomBytes(16).toString('hex');
  sesiones.set(token, { usuario: body.usuario, perfil: datos.perfil, expira: Date.now() + 1800 * 1000 });
  responder(res, 200, { token, expiresIn: 1800, nombre: datos.nombre, perfil: datos.perfil });
}

function listarPolizas(res, sesion, query) {
  const page = query.has('page') ? Number(query.get('page')) : 1;
  const size = query.has('size') ? Number(query.get('size')) : 10;
  const tipo = query.get('tipo');
  if (!Number.isInteger(page) || page < 1) return errorApi(res, 400, 'VALIDACION', 'page debe ser un entero mayor o igual que 1.');
  if (!Number.isInteger(size) || size < 1 || size > 50) return errorApi(res, 400, 'VALIDACION', 'size debe ser un entero entre 1 y 50.');
  if (tipo && !TIPOS_POLIZA.includes(tipo)) return errorApi(res, 400, 'VALIDACION', 'tipo debe ser AUTO, HOGAR o VIDA.');
  const lista = visibles(sesion).filter((p) => !tipo || p.tipo === tipo);
  const items = lista.slice((page - 1) * size, page * size).map(vistaPoliza);
  responder(res, 200, { total: lista.length, items });
}

function obtenerPoliza(res, id) {
  // Defecto sembrado: no se comprueba que la póliza pertenezca al usuario autenticado.
  const poliza = POLIZAS.find((p) => p.idPoliza === id);
  if (!poliza) return errorApi(res, 404, 'NO_ENCONTRADO', 'La póliza no existe.');
  responder(res, 200, vistaPoliza(poliza));
}

async function declararSiniestro(req, res) {
  let body;
  try {
    body = await leerJson(req);
  } catch {
    return errorApi(res, 400, 'JSON_INVALIDO', 'El cuerpo de la petición no es un JSON válido.');
  }
  if (!body.polizaId) return errorApi(res, 400, 'VALIDACION', 'polizaId es obligatorio.');
  if (!TIPOS_SINIESTRO.includes(body.tipo)) return errorApi(res, 400, 'VALIDACION', 'tipo debe ser COLISION, ROBO, INCENDIO o AGUA.');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(body.fecha || '') || Number.isNaN(Date.parse(body.fecha))) {
    return errorApi(res, 400, 'VALIDACION', 'fecha debe tener formato AAAA-MM-DD.');
  }
  if (body.fecha > new Date().toISOString().slice(0, 10)) return errorApi(res, 400, 'VALIDACION', 'fecha no puede ser futura.');

  // Defecto sembrado: una descripción null provoca una excepción no controlada.
  const descripcion = body.descripcion.trim();
  if (descripcion.length < 20 || descripcion.length > 500) {
    return errorApi(res, 400, 'VALIDACION', 'descripcion debe tener entre 20 y 500 caracteres.');
  }

  const poliza = POLIZAS.find((p) => p.idPoliza === body.polizaId);
  if (!poliza) return errorApi(res, 404, 'NO_ENCONTRADO', 'La póliza no existe.');
  // Defecto sembrado: no se rechazan siniestros sobre pólizas ANULADA ni ajenas.
  const duplicado = siniestros.find((s) => s.polizaId === body.polizaId && s.fecha === body.fecha && s.tipo === body.tipo);
  if (duplicado) return errorApi(res, 409, 'DUPLICADO', 'Ya existe un siniestro con los mismos datos.');

  secuencia += 1;
  const siniestro = {
    idSiniestro: `S-${secuencia}`,
    referencia: `SIN-${new Date().getFullYear()}-${secuencia}`,
    polizaId: body.polizaId,
    tipo: body.tipo,
    fecha: body.fecha,
    descripcion,
    estado: 'ABIERTO',
  };
  siniestros.push(siniestro);
  responder(res, 201, siniestro, { Location: `${BASE}/siniestros/${siniestro.idSiniestro}` });
}

async function enrutar(req, res) {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const ruta = url.pathname.replace(/\/$/, '');
  const metodo = req.method;

  if (metodo === 'GET' && ruta === `${BASE}/health`) return responder(res, 200, { status: 'UP' });
  if (metodo === 'POST' && ruta === `${BASE}/auth/login`) return login(req, res);

  const sesion = autenticar(req);
  if (!sesion) return errorApi(res, 401, 'NO_AUTENTICADO', 'Falta un token válido.');

  if (metodo === 'GET' && ruta === `${BASE}/polizas`) return listarPolizas(res, sesion, url.searchParams);
  const detalle = ruta.match(new RegExp(`^${BASE}/polizas/([^/]+)$`));
  if (metodo === 'GET' && detalle) return obtenerPoliza(res, decodeURIComponent(detalle[1]));

  if (metodo === 'POST' && ruta === `${BASE}/siniestros`) return declararSiniestro(req, res);
  if (metodo === 'GET' && ruta === `${BASE}/siniestros`) {
    const polizaId = url.searchParams.get('polizaId');
    return responder(res, 200, siniestros.filter((s) => !polizaId || s.polizaId === polizaId));
  }
  const siniestro = ruta.match(new RegExp(`^${BASE}/siniestros/([^/]+)$`));
  if (metodo === 'GET' && siniestro) {
    const encontrado = siniestros.find((s) => s.idSiniestro === decodeURIComponent(siniestro[1]));
    return encontrado ? responder(res, 200, encontrado) : errorApi(res, 404, 'NO_ENCONTRADO', 'El siniestro no existe.');
  }

  return errorApi(res, 404, 'RUTA_DESCONOCIDA', 'Recurso no encontrado.');
}

http
  .createServer((req, res) => {
    enrutar(req, res).catch((err) => errorApi(res, 500, 'ERROR_INTERNO', err.message));
  })
  .listen(PORT, () => console.log(`Pruebas Seguros API de demostración en http://localhost:${PORT}${BASE}`));
