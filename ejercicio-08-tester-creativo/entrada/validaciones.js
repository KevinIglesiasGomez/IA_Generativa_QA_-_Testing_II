/* Lógica de validación y cálculo del presupuesto de auto */

const FRANQUICIAS = { 0: 1.15, 150: 1.0, 300: 0.95, 500: 0.9 };
const PRIMA_MINIMA = 90;

function calcularEdad(fechaNacimiento, hoy = new Date()) {
  const nacimiento = new Date(fechaNacimiento);
  return hoy.getFullYear() - nacimiento.getFullYear();
}

function validarMatricula(valor) {
  const matricula = valor.toUpperCase();
  return /^\d{4}[A-Z]{3}$/.test(matricula);
}

function validarCodigoPostal(valor) {
  return /^\d{5}$/.test(valor);
}

function validarKilometros(valor) {
  const km = parseInt(valor, 10);
  return !Number.isNaN(km) && km >= 0 && km < 60000;
}

function validarEmail(valor) {
  return /.+@.+/.test(valor);
}

function validarFechaCarnet(fechaCarnet, fechaNacimiento) {
  const carnet = new Date(fechaCarnet);
  const nacimiento = new Date(fechaNacimiento);
  return carnet.getFullYear() - nacimiento.getFullYear() >= 18;
}

function aplicarCupon(prima, cupon) {
  if (cupon === 'SOL10') return { prima: prima * 0.9, valido: true };
  if (cupon === 'BIENVENIDA50') return { prima: prima - 50, valido: true };
  return { prima, valido: !cupon };
}

function calcularPrima({ edad, kilometros, franquicia, adicionales, cupon }) {
  let prima = kilometros < 5000 ? 150 : 300;
  if (edad < 25) prima *= 1.3;
  prima *= FRANQUICIAS[franquicia];
  prima += 40 * adicionales;
  const resultado = aplicarCupon(prima, cupon);
  return { prima: Math.round(Math.max(resultado.prima, PRIMA_MINIMA) * 100) / 100, cuponValido: resultado.valido };
}

if (typeof module !== 'undefined') {
  module.exports = { calcularEdad, validarMatricula, validarCodigoPostal, validarKilometros, validarEmail, validarFechaCarnet, aplicarCupon, calcularPrima };
}
