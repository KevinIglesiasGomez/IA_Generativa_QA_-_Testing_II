import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormBuilder, ReactiveFormsModule, ValidationErrors, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { EstadoPoliza } from '../../core/enums/estados.enum';
import { TipoPoliza, TipoSiniestro } from '../../core/enums/tipos.enum';
import { Poliza } from '../../core/models/poliza.model';
import { PolizasService } from '../../core/services/polizas.service';
import { SiniestrosService } from '../../core/services/siniestros.service';

// Días máximos desde la ocurrencia hasta la declaración, según tipo de póliza.
const PLAZO_DECLARACION_DIAS: Record<TipoPoliza, number> = {
  [TipoPoliza.AUTO]: 30,
  [TipoPoliza.HOGAR]: 7,
  [TipoPoliza.VIDA]: 90,
};

const DESCRIPCION_MIN = 20;
const DESCRIPCION_MAX = 500;

@Component({
  selector: 'app-siniestro-declarar',
  standalone: true,
  imports: [CommonModule, IonicModule, ReactiveFormsModule],
  templateUrl: './siniestro-declarar.page.html',
})
export class SiniestroDeclararPage implements OnInit {
  polizasVigentes: Poliza[] = [];
  tipos = Object.values(TipoSiniestro);
  enviando = false;
  referencia = '';
  errorServidor = '';
  hoy = new Date().toISOString().slice(0, 10);

  form = this.fb.group({
    idPoliza: ['', Validators.required],
    tipo: ['', Validators.required],
    fechaSiniestro: ['', [Validators.required, (c: AbstractControl) => this.validarFecha(c)]],
    descripcion: ['', [Validators.required, Validators.minLength(DESCRIPCION_MIN), Validators.maxLength(DESCRIPCION_MAX)]],
  });

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private polizasService: PolizasService,
    private siniestrosService: SiniestrosService
  ) {}

  ngOnInit(): void {
    this.polizasService.listar().subscribe((pagina) => {
      this.polizasVigentes = pagina.items.filter((p) => p.estado === EstadoPoliza.VIGENTE);
      const preseleccionada = this.route.snapshot.queryParamMap.get('poliza');
      if (preseleccionada && this.polizasVigentes.some((p) => p.idPoliza === preseleccionada)) {
        this.form.patchValue({ idPoliza: preseleccionada });
      }
    });
  }

  private validarFecha(control: AbstractControl): ValidationErrors | null {
    if (!control.value) return null;
    if (control.value > this.hoy) return { futura: true };
    const poliza = this.polizasVigentes.find((p) => p.idPoliza === this.form?.value.idPoliza);
    if (!poliza) return null;
    const dias = (Date.now() - new Date(control.value).getTime()) / 86400000;
    return dias > PLAZO_DECLARACION_DIAS[poliza.tipo] ? { fueraDePlazo: PLAZO_DECLARACION_DIAS[poliza.tipo] } : null;
  }

  enviar(): void {
    this.form.markAllAsTouched();
    if (this.form.invalid) return;
    this.enviando = true;
    this.errorServidor = '';
    this.siniestrosService.declarar(this.form.value as any).subscribe({
      next: (siniestro) => {
        this.referencia = siniestro.referencia;
        this.enviando = false;
      },
      error: (err) => {
        this.enviando = false;
        this.errorServidor =
          err.status === 409
            ? 'Ya existe un siniestro declarado con los mismos datos.'
            : 'No se ha podido registrar el siniestro. Inténtalo más tarde.';
      },
    });
  }

  cancelar(): void {
    this.router.navigate(['/polizas']);
  }
}
