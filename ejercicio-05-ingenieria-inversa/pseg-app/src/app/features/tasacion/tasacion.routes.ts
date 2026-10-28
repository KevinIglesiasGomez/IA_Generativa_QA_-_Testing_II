import { Routes } from '@angular/router';

export const TASACION_ROUTES: Routes = [
  {
    path: '',
    loadComponent: () => import('./tasacion-preseleccion.page').then((m) => m.TasacionPreseleccionPage),
  },
];
