import { Perfil } from '../enums/perfil.enum';

export interface Sesion {
  usuario: string;
  nombre: string;
  perfil: Perfil;
  token: string;
  expiraEn: number;
}

export interface LoginRequest {
  usuario: string;
  password: string;
}

export interface LoginResponse {
  token: string;
  expiresIn: number;
  nombre: string;
  perfil: Perfil;
}
