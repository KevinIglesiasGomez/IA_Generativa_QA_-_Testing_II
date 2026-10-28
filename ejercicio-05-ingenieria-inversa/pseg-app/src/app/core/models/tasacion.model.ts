import { ResultadoTasacion } from '../enums/tipos.enum';

export interface SolicitudPreseleccion {
  matricula: string;
  fechaMatriculacion: string;
  kilometros: number;
}

export interface RespuestaPreseleccion {
  resultado: ResultadoTasacion;
  primaEstimada?: number;
  motivo?: string;
}
