import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { Perfil } from '../../core/enums/perfil.enum';
import { Sesion } from '../../core/models/sesion.model';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, IonicModule, RouterLink],
  templateUrl: './home.page.html',
})
export class HomePage implements OnInit {
  sesion!: Sesion;
  esAgente = false;
  sinPermiso = false;

  constructor(private auth: AuthService, private router: Router, private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.sesion = this.auth.sesionActual()!;
    this.esAgente = this.sesion.perfil === Perfil.AGENTE;
    this.sinPermiso = this.route.snapshot.queryParamMap.get('error') === 'sin-permiso';
  }

  cerrarSesion(): void {
    this.auth.cerrarSesion();
    this.router.navigate(['/login']);
  }
}
