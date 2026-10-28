import React, { useState } from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import LoginPage from './pages/LoginPage.jsx';
import PolizasPage from './pages/PolizasPage.jsx';
import SiniestroPage from './pages/SiniestroPage.jsx';

export default function App() {
  const [usuario, setUsuario] = useState(null);

  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      <Route path="/login" element={<LoginPage onLogin={setUsuario} />} />
      <Route
        path="/polizas"
        element={usuario ? <PolizasPage usuario={usuario} onLogout={() => setUsuario(null)} /> : <Navigate to="/login" replace />}
      />
      <Route
        path="/siniestro/nuevo"
        element={usuario ? <SiniestroPage usuario={usuario} /> : <Navigate to="/login" replace />}
      />
    </Routes>
  );
}
