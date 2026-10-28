import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const USUARIOS = { cliente1: 'Cliente#24', agente1: 'Agente#24' };

// Pantalla bien instrumentada: data-testid, id, label y roles accesibles.
export default function LoginPage({ onLogin }) {
  const [usuario, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [verPassword, setVerPassword] = useState(false);
  const [errores, setErrores] = useState({});
  const navigate = useNavigate();

  function enviar(e) {
    e.preventDefault();
    const nuevos = {};
    if (!usuario.trim()) nuevos.usuario = 'El usuario está vacío. Introduce tus datos e inténtalo de nuevo.';
    else if (!/^[A-Za-z0-9]{1,8}$/.test(usuario)) nuevos.usuario = 'El formato del usuario es incorrecto. Revisa tus datos e inténtalo de nuevo.';
    if (!password) nuevos.password = 'La contraseña está vacía. Introduce tus datos e inténtalo de nuevo.';
    if (!nuevos.usuario && !nuevos.password && USUARIOS[usuario] !== password) {
      nuevos.general = 'Usuario o contraseña incorrectos.';
    }
    setErrores(nuevos);
    if (Object.keys(nuevos).length === 0) {
      onLogin(usuario);
      navigate('/polizas');
    }
  }

  return (
    <main className="contenedor">
      <h1 data-testid="login-titulo">¡Bienvenido a Pruebas Seguros!</h1>
      {errores.general && <div role="alert" data-testid="login-error-general" className="error">{errores.general}</div>}
      <form onSubmit={enviar} noValidate>
        <div className="campo">
          <label htmlFor="usuario">Usuario</label>
          <input id="usuario" name="usuario" data-testid="login-usuario" value={usuario} onChange={(e) => setUsuario(e.target.value)} />
          {errores.usuario && <span className="error" data-testid="login-usuario-error">{errores.usuario}</span>}
        </div>
        <div className="campo">
          <label htmlFor="password">Contraseña</label>
          <input id="password" name="password" data-testid="login-password" type={verPassword ? 'text' : 'password'} value={password} onChange={(e) => setPassword(e.target.value)} />
          <button type="button" aria-label="Mostrar contraseña" data-testid="login-ver-password" className="btn-link" onClick={() => setVerPassword(!verPassword)}>
            {verPassword ? 'Ocultar' : 'Ver'}
          </button>
          {errores.password && <span className="error" data-testid="login-password-error">{errores.password}</span>}
        </div>
        <button type="submit" className="btn" data-testid="login-submit">Iniciar sesión</button>
      </form>
      <a href="https://sso.pruebas-seguros.example/recuperar" target="_blank" rel="noreferrer" data-testid="login-recuperar">¿Olvidaste tu contraseña?</a>
    </main>
  );
}
