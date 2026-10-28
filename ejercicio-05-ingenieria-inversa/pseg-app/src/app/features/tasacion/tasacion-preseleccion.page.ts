import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AbstractControl, FormBuilder, ReactiveFormsModule, ValidationErrors, Validators } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { ResultadoTasacion } from '../../core/enums/tipos.enum';
import { RespuestaPreseleccion } from '../../core/models/tasacion.model';
import { TasacionService } from '../../core/services/tasacion.service';

// 4 dígitos y 3 consonantes (sin vocales ni Ñ, Q).
const REGEX_MATRICULA = /^\d{4}[BCDFGHJKLMNPRSTVWXYZ]{3}$/;
const MAX_KM = 300000;

@Component({
  selector: 'app-tasacion-preseleccion',
  standalone: true,
  imports: [CommonModule, IonicModule, ReactiveFormsModule],
  templateUrl: './tasacion-preseleccion.page.html',
})
export class TasacionPreseleccionPage {
  consultando = false;
  respuesta?: RespuestaPreseleccion;
  errorServidor = false;
  resultados = ResultadoTasacion;

  form = this.fb.group({
    matricula: ['', [Validators.required, Validators.pattern(REGEX_MATRICULA)]],
    fechaMatriculacion: ['', [Validators.required, (c: AbstractControl) => this.validarFecha(c)]],
    kilometros: [0, [Validators.required, Validators.min(0), Validators.max(MAX_KM)]],
  });

  constructor(private fb: FormBuilder, private tasacionService: TasacionService) {}

  private validarFecha(control: AbstractControl): ValidationErrors | null {
    if (!control.value) return null;
    return new Date(control.value) > new Date() ? { futura: true } : null;
  }

  // Antigüedad en años completos del vehículo.
  get antiguedad(): number {
    const f = this.form.value.fechaMatriculacion;
    return f ? Math.floor((Date.now() - new Date(f).getTime()) / (365.25 * 86400000)) : 0;
  }

  solicitar(): void {
    this.form.markAllAsTouched();
    if (this.form.invalid) return;

    // Regla de negocio: vehículos con más de 15 años no son asegurables.
    if (this.antiguedad > 15) {
      this.respuesta = { resultado: ResultadoTasacion.RECHAZADA, motivo: 'Vehículo con más de 15 años de antigüedad.' };
      return;
    }

    this.consultando = true;
    this.errorServidor = false;
    const valores = this.form.value;
    this.tasacionService
      .preseleccionar({
        matricula: valores.matricula!.toUpperCase(),
        fechaMatriculacion: valores.fechaMatriculacion!,
        kilometros: valores.kilometros!,
      })
      .subscribe({
        next: (resp) => {
          // Entre 10 y 15 años el resultado pasa siempre a revisión manual.
          this.respuesta =
            this.antiguedad > 10 && resp.resultado === ResultadoTasacion.ACEPTADA
              ? { ...resp, resultado: ResultadoTasacion.REVISION_MANUAL, motivo: 'Antigüedad superior a 10 años.' }
              : resp;
          this.consultando = false;
        },
        error: () => {
          this.consultando = false;
          this.errorServidor = true;
        },
      });
  }
}
