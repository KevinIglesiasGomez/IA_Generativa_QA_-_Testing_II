import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';
import { TipoPoliza } from '../enums/tipos.enum';
import { PaginaPolizas, Poliza } from '../models/poliza.model';

export const TAMANO_PAGINA_POLIZAS = 10;

@Injectable({ providedIn: 'root' })
export class PolizasService {
  constructor(private http: HttpClient) {}

  listar(tipo?: TipoPoliza, pagina = 1): Observable<PaginaPolizas> {
    let params = new HttpParams().set('page', pagina).set('size', TAMANO_PAGINA_POLIZAS);
    if (tipo) {
      params = params.set('tipo', tipo);
    }
    return this.http.get<PaginaPolizas>(`${environment.apiUrl}/polizas`, { params });
  }

  obtener(idPoliza: string): Observable<Poliza> {
    return this.http.get<Poliza>(`${environment.apiUrl}/polizas/${idPoliza}`);
  }
}
