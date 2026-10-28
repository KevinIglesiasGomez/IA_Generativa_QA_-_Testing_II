import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const POLIZAS = [
  { id: 'P-1001', tipo: 'Auto', descripcion: 'Seat León 1234BCD', estado: 'Vigente' },
  { id: 'P-1002', tipo: 'Hogar', descripcion: 'C/ Alcalá 45, Madrid', estado: 'Vigente' },
  { id: 'P-1003', tipo: 'Vida', descripcion: 'Seguro de vida individual', estado: 'Anulada' },
];

// Pantalla con selectores de calidad mixta: ids genéricos, elementos sin identificar y una lista repetida.
export default function PolizasPage({ usuario, onLogout }) {
  const [tipo, setTipo] = useState('');
  const navigate = useNavigate();
  const filas = POLIZAS.filter((p) => !tipo || p.tipo === tipo);

  return (
    <div className="contenedor">
      <div id="div1">
        <h1 data-testid="polizas-titulo">Mis pólizas</h1>
        <span>Hola, {usuario}</span>
        <button id="btn1" className="btn" onClick={() => { onLogout(); navigate('/login'); }}>Cerrar sesión</button>
      </div>

      <select id="select2" value={tipo} onChange={(e) => setTipo(e.target.value)}>
        <option value="">Todas</option>
        <option value="Auto">Auto</option>
        <option value="Hogar">Hogar</option>
        <option value="Vida">Vida</option>
      </select>

      <table>
        <thead>
          <tr><th>Número</th><th>Tipo</th><th>Descripción</th><th>Estado</th><th></th></tr>
        </thead>
        <tbody>
          {filas.map((p) => (
            <tr key={p.id} className="fila">
              <td>{p.id}</td>
              <td>{p.tipo}</td>
              <td>{p.descripcion}</td>
              <td className={p.estado === 'Vigente' ? 'ok' : 'ko'}>{p.estado}</td>
              <td><button className="btn-link" onClick={() => window.alert('Detalle de ' + p.id)}>Ver detalle</button></td>
            </tr>
          ))}
        </tbody>
      </table>
      {filas.length === 0 && <p>No se han encontrado pólizas.</p>}

      <Link to="/siniestro/nuevo" data-testid="polizas-nuevo-siniestro">Declarar siniestro</Link>
    </div>
  );
}
