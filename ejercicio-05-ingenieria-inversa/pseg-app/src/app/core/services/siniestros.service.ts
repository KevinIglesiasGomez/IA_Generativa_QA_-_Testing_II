import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { DeclaracionSiniestro, Siniestro } from '../models/siniestro.model';

@Injectable({ providedIn: 'root' })
export class SiniestrosService {
  constructor(private http: HttpClient) {}

  declarar(declaracion: DeclaracionSiniestro): Observable<Siniestro> {
    return this.http.post<Siniestro>(`${environment.apiUrl}/siniestros`, declaracion);
  }

  listarPorPoliza(idPoliza: string): Observable<Siniestro[]> {
    const params = new HttpParams().set('polizaId', idPoliza);
    return this.http.get<Siniestro[]>(`${environment.apiUrl}/siniestros`, { params });
  }

  obtener(idSiniestro: string): Observable<Siniestro> {
    return this.http.get<Siniestro>(`${environment.apiUrl}/siniestros/${idSiniestro}`);
  }
}
