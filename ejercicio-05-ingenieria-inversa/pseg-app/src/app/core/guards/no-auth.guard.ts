import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

// Impide ver el login a un usuario que ya tiene sesión vigente (autologado).
export const noAuthGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.haySesionVigente() ? router.createUrlTree(['/home']) : true;
};
