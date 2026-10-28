import { Routes } from '@angular/router';

export const POLIZAS_ROUTES: Routes = [
  {
    path: '',
    loadComponent: () => import('./polizas-lista.page').then((m) => m.PolizasListaPage),
  },
  {
    path: ':idPoliza',
    loadComponent: () => import('./poliza-detalle.page').then((m) => m.PolizaDetallePage),
  },
];
