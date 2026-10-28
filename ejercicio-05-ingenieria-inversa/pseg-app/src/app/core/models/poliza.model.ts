import { EstadoPoliza } from '../enums/estados.enum';
import { TipoPoliza } from '../enums/tipos.enum';

export interface Poliza {
  idPoliza: string;
  tipo: TipoPoliza;
  descripcion: string;
  estado: EstadoPoliza;
  primaAnual: number;
  fechaInicio: string;
  fechaFin: string;
}

export interface PaginaPolizas {
  total: number;
  items: Poliza[];
}
