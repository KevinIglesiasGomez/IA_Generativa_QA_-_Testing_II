import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';
import { noAuthGuard } from './core/guards/no-auth.guard';
import { perfilGuard } from './core/guards/perfil.guard';
import { Perfil } from './core/enums/perfil.enum';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  {
    path: 'login',
    canActivate: [noAuthGuard],
    loadComponent: () => import('./features/login/login.page').then((m) => m.LoginPage),
  },
  {
    path: 'home',
    canActivate: [authGuard],
    loadComponent: () => import('./features/home/home.page').then((m) => m.HomePage),
  },
  {
    path: 'polizas',
    canActivate: [authGuard],
    loadChildren: () => import('./features/polizas/polizas.routes').then((m) => m.POLIZAS_ROUTES),
  },
  {
    path: 'siniestros',
    canActivate: [authGuard],
    loadChildren: () => import('./features/siniestros/siniestros.routes').then((m) => m.SINIESTROS_ROUTES),
  },
  {
    path: 'tasacion',
    canActivate: [authGuard, perfilGuard],
    data: { perfiles: [Perfil.AGENTE] },
    loadChildren: () => import('./features/tasacion/tasacion.routes').then((m) => m.TASACION_ROUTES),
  },
  { path: '**', redirectTo: 'home' },
];
