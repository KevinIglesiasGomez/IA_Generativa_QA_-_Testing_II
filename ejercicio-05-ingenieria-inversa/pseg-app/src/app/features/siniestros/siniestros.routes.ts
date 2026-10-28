import { Routes } from '@angular/router';

export const SINIESTROS_ROUTES: Routes = [
  {
    path: 'declarar',
    loadComponent: () => import('./siniestro-declarar.page').then((m) => m.SiniestroDeclararPage),
  },
  {
    path: ':idSiniestro',
    loadComponent: () => import('./siniestro-detalle.page').then((m) => m.SiniestroDetallePage),
  },
];
