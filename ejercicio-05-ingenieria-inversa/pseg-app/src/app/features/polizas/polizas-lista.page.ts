import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { TipoPoliza } from '../../core/enums/tipos.enum';
import { Poliza } from '../../core/models/poliza.model';
import { PolizasService } from '../../core/services/polizas.service';

@Component({
  selector: 'app-polizas-lista',
  standalone: true,
  imports: [CommonModule, IonicModule, RouterLink],
  templateUrl: './polizas-lista.page.html',
})
export class PolizasListaPage {
  polizas: Poliza[] = [];
  total = 0;
  pagina = 1;
  tipoFiltro?: TipoPoliza;
  loading = false;
  error = false;
  tipos = Object.values(TipoPoliza);

  constructor(private polizasService: PolizasService) {}

  ionViewWillEnter(): void {
    this.cargar(true);
  }

  cambiarFiltro(tipo?: TipoPoliza): void {
    this.tipoFiltro = tipo;
    this.cargar(true);
  }

  masPolizas(evento: any): void {
    this.pagina++;
    this.cargar(false, evento);
  }

  get hayMas(): boolean {
    return this.polizas.length < this.total;
  }

  private cargar(reiniciar: boolean, evento?: any): void {
    if (reiniciar) {
      this.pagina = 1;
      this.polizas = [];
    }
    this.loading = true;
    this.error = false;
    this.polizasService.listar(this.tipoFiltro, this.pagina).subscribe({
      next: (resp) => {
        this.polizas = [...this.polizas, ...resp.items];
        this.total = resp.total;
        this.loading = false;
        evento?.target.complete();
      },
      error: () => {
        this.loading = false;
        this.error = true;
        evento?.target.complete();
      },
    });
  }
}
