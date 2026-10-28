import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { RespuestaPreseleccion, SolicitudPreseleccion } from '../models/tasacion.model';

@Injectable({ providedIn: 'root' })
export class TasacionService {
  constructor(private http: HttpClient) {}

  preseleccionar(solicitud: SolicitudPreseleccion): Observable<RespuestaPreseleccion> {
    return this.http.post<RespuestaPreseleccion>(`${environment.apiUrl}/tasacion/preseleccion`, solicitud);
  }
}
