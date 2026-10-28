import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { environment } from '../../../environments/environment';
import { AuthService } from '../../core/services/auth.service';

const REGEX_USUARIO = /^[A-Za-z0-9]{1,8}$/;

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, IonicModule, ReactiveFormsModule],
  templateUrl: './login.page.html',
})
export class LoginPage implements OnInit {
  cargando = false;
  verPassword = false;
  errorGeneral = '';

  form = this.fb.group({
    usuario: ['', [Validators.required, Validators.pattern(REGEX_USUARIO)]],
    password: ['', [Validators.required]],
  });

  constructor(private fb: FormBuilder, private auth: AuthService, private router: Router) {}

  ngOnInit(): void {
    this.form.patchValue({ usuario: this.auth.ultimoUsuario() });
  }

  get errorUsuario(): string {
    const ctrl = this.form.controls.usuario;
    if (!ctrl.touched) return '';
    if (ctrl.hasError('required')) return 'El usuario está vacío. Introduce tus datos e inténtalo de nuevo.';
    if (ctrl.hasError('pattern')) return 'El formato del usuario es incorrecto. Revisa tus datos e inténtalo de nuevo.';
    return '';
  }

  get errorPassword(): string {
    const ctrl = this.form.controls.password;
    return ctrl.touched && ctrl.hasError('required')
      ? 'La contraseña está vacía. Introduce tus datos e inténtalo de nuevo.'
      : '';
  }

  iniciarSesion(): void {
    this.form.markAllAsTouched();
    this.errorGeneral = '';
    if (this.form.invalid) return;

    const minutos = this.auth.minutosBloqueoRestantes();
    if (minutos > 0) {
      this.errorGeneral = `Demasiados intentos fallidos. Inténtalo de nuevo en ${minutos} minutos.`;
      return;
    }

    this.cargando = true;
    this.auth.login({ usuario: this.form.value.usuario!, password: this.form.value.password! }).subscribe({
      next: () => this.router.navigate(['/home']),
      error: (err) => {
        this.cargando = false;
        if (err.status === 401) {
          this.auth.registrarIntentoFallido();
          this.errorGeneral = 'Usuario o contraseña incorrectos.';
        } else {
          this.errorGeneral = 'No se ha podido iniciar sesión. Inténtalo más tarde.';
        }
      },
    });
  }

  recuperarPassword(): void {
    window.open(environment.recuperarPasswordUrl, '_system');
  }
}
