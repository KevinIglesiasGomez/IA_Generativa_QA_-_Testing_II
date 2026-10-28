import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

// Pantalla con selectores frágiles: clases ofuscadas, ids duplicados y botones sin identificar.
export default function SiniestroPage({ usuario }) {
  const [tipo, setTipo] = useState('');
  const [fecha, setFecha] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [aceptaCondiciones, setAceptaCondiciones] = useState(false);
  const [referencia, setReferencia] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  function enviar(e) {
    e.preventDefault();
    if (!tipo || !fecha || descripcion.trim().length < 20) {
      setError('Revisa los datos del formulario.');
      return;
    }
    setError('');
    setReferencia('SIN-2026-' + Math.floor(1000 + Math.random() * 9000));
  }

  return (
    <div className="contenedor">
      <h2>Nueva declaración de siniestro</h2>
      <p>Usuario: {usuario}</p>

      {referencia && <div className="css-1x2y3z">Siniestro registrado: {referencia}</div>}
      {error && <div className="css-9k8j7h">{error}</div>}

      <form onSubmit={enviar}>
        <div className="campo">
          <label>Tipo de siniestro</label>
          <select id="field" className="css-4f5g6h" value={tipo} onChange={(e) => setTipo(e.target.value)}>
            <option value="">Selecciona</option>
            <option value="colision">Colisión</option>
            <option value="robo">Robo</option>
            <option value="incendio">Incendio</option>
          </select>
        </div>

        <div className="campo">
          <label>Fecha</label>
          <input id="field" className="css-7a8b9c" type="date" value={fecha} onChange={(e) => setFecha(e.target.value)} />
        </div>

        <div className="campo">
          <label>Descripción</label>
          <textarea className="css-2d3e4f" rows="4" value={descripcion} onChange={(e) => setDescripcion(e.target.value)} />
        </div>

        <div className="campo">
          <input type="checkbox" checked={aceptaCondiciones} onChange={(e) => setAceptaCondiciones(e.target.checked)} />
          <span> Acepto las condiciones de tramitación</span>
        </div>

        <button className="btn" disabled={!aceptaCondiciones}>Enviar</button>
        <button type="button" className="btn-link" onClick={() => navigate('/polizas')}>Cancelar</button>
      </form>
    </div>
  );
}
