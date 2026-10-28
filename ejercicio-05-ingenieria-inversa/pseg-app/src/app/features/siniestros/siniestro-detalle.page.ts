import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { EstadoSiniestro } from '../../core/enums/estados.enum';
import { Siniestro } from '../../core/models/siniestro.model';
import { SiniestrosService } from '../../core/services/siniestros.service';

@Component({
  selector: 'app-siniestro-detalle',
  standalone: true,
  imports: [CommonModule, IonicModule],
  templateUrl: './siniestro-detalle.page.html',
})
export class SiniestroDetallePage implements OnInit {
  siniestro?: Siniestro;
  loading = true;
  error = false;

  constructor(private route: ActivatedRoute, private siniestrosService: SiniestrosService) {}

  get estaCerrado(): boolean {
    return this.siniestro?.estado === EstadoSiniestro.RESUELTO || this.siniestro?.estado === EstadoSiniestro.RECHAZADO;
  }

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('idSiniestro')!;
    this.siniestrosService.obtener(id).subscribe({
      next: (s) => {
        this.siniestro = s;
        this.loading = false;
      },
      error: () => {
        this.loading = false;
        this.error = true;
      },
    });
  }
}
