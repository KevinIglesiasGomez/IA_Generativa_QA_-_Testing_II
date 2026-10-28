import { inject } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivateFn, Router } from '@angular/router';
import { Perfil } from '../enums/perfil.enum';
import { AuthService } from '../services/auth.service';

// Restringe la ruta a los perfiles definidos en route.data.perfiles.
export const perfilGuard: CanActivateFn = (route: ActivatedRouteSnapshot) => {
  const auth = inject(AuthService);
  const router = inject(Router);
  const permitidos: Perfil[] = route.data['perfiles'] ?? [];
  const sesion = auth.sesionActual();
  if (sesion && permitidos.includes(sesion.perfil)) {
    return true;
  }
  return router.createUrlTree(['/home'], { queryParams: { error: 'sin-permiso' } });
};
