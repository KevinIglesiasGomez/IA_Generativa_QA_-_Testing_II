import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

// Exige sesión vigente; si ha caducado la elimina y redirige al login.
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  if (auth.haySesionVigente()) {
    return true;
  }
  auth.cerrarSesion();
  return router.createUrlTree(['/login']);
};
