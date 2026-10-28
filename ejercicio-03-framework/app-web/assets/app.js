/* Datos y utilidades compartidas de Pruebas Seguros Web (aplicación de demostración) */
const USUARIOS = {
  cliente1: { password: 'Cliente#24', rol: 'cliente', nombre: 'Lucía Fernández' },
  agente1: { password: 'Agente#24', rol: 'agente', nombre: 'Marcos Ortega' },
};

const POLIZAS = [
  { id: 'P-1001', tipo: 'auto', descripcion: 'Seat León 1234BCD', titular: 'cliente1', prima: 412.5, estado: 'Vigente', desde: '2026-01-01', hasta: '2026-12-31' },
  { id: 'P-1002', tipo: 'hogar', descripcion: 'C/ Alcalá 45, Madrid', titular: 'cliente1', prima: 238.0, estado: 'Vigente', desde: '2026-02-15', hasta: '2027-02-14' },
  { id: 'P-1003', tipo: 'vida', descripcion: 'Seguro de vida individual', titular: 'cliente1', prima: 120.0, estado: 'Anulada', desde: '2024-03-01', hasta: '2025-02-28' },
  { id: 'P-2001', tipo: 'auto', descripcion: 'Renault Clio 5678FGH', titular: 'cliente2', prima: 365.9, estado: 'Vigente', desde: '2026-05-10', hasta: '2027-05-09' },
  { id: 'P-2002', tipo: 'hogar', descripcion: 'C/ Mayor 12, Valencia', titular: 'cliente2', prima: 199.0, estado: 'Vigente', desde: '2026-06-01', hasta: '2027-05-31' },
];

const SESSION_KEY = 'pseg.sesion';

function getSesion() {
  const raw = sessionStorage.getItem(SESSION_KEY);
  return raw ? JSON.parse(raw) : null;
}

function guardarSesion(usuario) {
  const datos = USUARIOS[usuario];
  sessionStorage.setItem(SESSION_KEY, JSON.stringify({ usuario, rol: datos.rol, nombre: datos.nombre }));
}

function cerrarSesion() {
  sessionStorage.removeItem(SESSION_KEY);
  window.location.href = 'login.html';
}

function exigirSesion() {
  const sesion = getSesion();
  if (!sesion) {
    window.location.href = 'login.html';
    return null;
  }
  return sesion;
}

function polizasVisibles(sesion) {
  return sesion.rol === 'agente' ? POLIZAS : POLIZAS.filter((p) => p.titular === sesion.usuario);
}

function formatoEuros(valor) {
  return valor.toFixed(2).replace('.', ',') + ' €';
}
