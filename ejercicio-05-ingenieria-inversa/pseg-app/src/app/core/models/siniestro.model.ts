import { EstadoSiniestro } from '../enums/estados.enum';
import { TipoSiniestro } from '../enums/tipos.enum';

export interface DeclaracionSiniestro {
  idPoliza: string;
  tipo: TipoSiniestro;
  fechaSiniestro: string;
  descripcion: string;
}

export interface Siniestro extends DeclaracionSiniestro {
  idSiniestro: string;
  referencia: string;
  estado: EstadoSiniestro;
}
