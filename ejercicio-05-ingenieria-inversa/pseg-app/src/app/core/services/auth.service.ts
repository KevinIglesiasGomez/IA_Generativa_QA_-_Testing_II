import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { environment } from '../../../environments/environment';
import { LoginRequest, LoginResponse, Sesion } from '../models/sesion.model';

const CLAVE_SESION = 'pseg.sesion';
const CLAVE_ULTIMO_USUARIO = 'pseg.ultimoUsuario';
const CLAVE_INTENTOS = 'pseg.intentosFallidos';
const MAX_INTENTOS = 5;
const BLOQUEO_MINUTOS = 15;

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private http: HttpClient) {}

  login(credenciales: LoginRequest): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${environment.apiUrl}/auth/login`, credenciales).pipe(
      tap((resp) => {
        const sesion: Sesion = {
          usuario: credenciales.usuario,
          nombre: resp.nombre,
          perfil: resp.perfil,
          token: resp.token,
          expiraEn: Date.now() + resp.expiresIn * 1000,
        };
        localStorage.setItem(CLAVE_SESION, JSON.stringify(sesion));
        localStorage.setItem(CLAVE_ULTIMO_USUARIO, credenciales.usuario);
        localStorage.removeItem(CLAVE_INTENTOS);
      })
    );
  }

  registrarIntentoFallido(): void {
    const actual = JSON.parse(localStorage.getItem(CLAVE_INTENTOS) ?? '{"n":0,"hasta":0}');
    const n = actual.n + 1;
    const hasta = n >= MAX_INTENTOS ? Date.now() + BLOQUEO_MINUTOS * 60000 : 0;
    localStorage.setItem(CLAVE_INTENTOS, JSON.stringify({ n, hasta }));
  }

  minutosBloqueoRestantes(): number {
    const { hasta } = JSON.parse(localStorage.getItem(CLAVE_INTENTOS) ?? '{"n":0,"hasta":0}');
    return hasta > Date.now() ? Math.ceil((hasta - Date.now()) / 60000) : 0;
  }

  ultimoUsuario(): string {
    return localStorage.getItem(CLAVE_ULTIMO_USUARIO) ?? '';
  }

  sesionActual(): Sesion | null {
    const raw = localStorage.getItem(CLAVE_SESION);
    return raw ? (JSON.parse(raw) as Sesion) : null;
  }

  haySesionVigente(): boolean {
    const sesion = this.sesionActual();
    return !!sesion && sesion.expiraEn > Date.now();
  }

  cerrarSesion(): void {
    localStorage.removeItem(CLAVE_SESION);
  }
}
