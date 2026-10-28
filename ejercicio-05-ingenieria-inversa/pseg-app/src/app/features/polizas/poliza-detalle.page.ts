import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { EstadoPoliza } from '../../core/enums/estados.enum';
import { Poliza } from '../../core/models/poliza.model';
import { Siniestro } from '../../core/models/siniestro.model';
import { PolizasService } from '../../core/services/polizas.service';
import { SiniestrosService } from '../../core/services/siniestros.service';

@Component({
  selector: 'app-poliza-detalle',
  standalone: true,
  imports: [CommonModule, IonicModule, RouterLink],
  templateUrl: './poliza-detalle.page.html',
})
export class PolizaDetallePage implements OnInit {
  poliza?: Poliza;
  siniestros: Siniestro[] = [];
  loading = true;
  noEncontrada = false;

  constructor(
    private route: ActivatedRoute,
    private polizasService: PolizasService,
    private siniestrosService: SiniestrosService
  ) {}

  get puedeDeclararSiniestro(): boolean {
    return this.poliza?.estado === EstadoPoliza.VIGENTE;
  }

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('idPoliza')!;
    this.polizasService.obtener(id).subscribe({
      next: (poliza) => {
        this.poliza = poliza;
        this.loading = false;
        this.siniestrosService.listarPorPoliza(id).subscribe((lista) => (this.siniestros = lista));
      },
      error: (err) => {
        this.loading = false;
        this.noEncontrada = err.status === 404 || err.status === 403;
      },
    });
  }
}
