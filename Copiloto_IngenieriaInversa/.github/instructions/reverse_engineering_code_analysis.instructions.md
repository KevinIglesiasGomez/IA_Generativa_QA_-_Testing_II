# Instrucciones de Análisis de Código para el Agente: Reverse Engineering Functional Analyst

## Objetivo

Estas instrucciones definen las técnicas específicas de análisis de código que el agente debe aplicar para extraer información funcional de cada capa de la aplicación. Están organizadas por tipo de artefacto de código.

---

## 1. ANÁLISIS DE ROUTING MODULES

### Qué buscar

```typescript
// Patrones a identificar en archivos *-routing.module.ts o *.routes.ts
{
  path: 'ruta',                    // → Ruta de la vista
  component: ComponentPage,         // → Componente principal
  canActivate: [Guard1, Guard2],    // → Guards de acceso
  children: [...]                   // → Rutas hijas (jerarquía)
  loadChildren: () => import(...)   // → Lazy loading de módulos
  redirectTo: 'ruta'               // → Redirecciones
  data: { ... }                    // → Metadata de la ruta
}
```

### Qué documentar

- Ruta completa incluyendo los segmentos padre
- Parámetros dinámicos con su nombre (`:idTasacion`, `:matricula`)
- Query params identificados en el componente (`ActivatedRoute.queryParams`)
- Guards en `canActivate`, `canDeactivate`, `canLoad`
- Resolvers si existen

### Construcción del path completo

Recorrer la jerarquía de rutas para construir el path completo:
```
/root/inspeccion/detalle/{idTareaInspeccion}/taller/{codInstalacion}
```

---

## 2. ANÁLISIS DE COMPONENTES (PÁGINAS)

### Archivo TypeScript (.page.ts / .component.ts)

**Ciclo de vida**:
- `constructor()` — Inyección de dependencias → identificar servicios usados
- `ngOnInit()` / `ionViewWillEnter()` — Carga inicial → identificar llamadas API al entrar
- `ngOnDestroy()` / `ionViewWillLeave()` — Limpieza → identificar subscripciones

**Variables de estado**:
- Variables booleanas de loading (`loading`, `isLoading`, `loadingData`)
- Variables de datos principales (`listado`, `detalle`, `formulario`)
- Variables de control de UI (`showModal`, `isExpanded`, `selectedTab`)

**Métodos de acción**:
- Métodos llamados desde el template que ejecutan lógica de negocio
- Métodos de navegación (`router.navigate`, `navController.navigateForward`)
- Métodos de llamada a servicios API

### Archivo Template (.page.html / .component.html)

**Estructura visual**:
- `<ion-header>` — Cabecera con título, botones back, opciones
- `<ion-content>` — Contenido principal
- `<ion-footer>` — Pie con botones de acción
- `<ion-fab>` — Botones flotantes (FAB)

**Condicionales de estado**:
- `*ngIf="loading"` → Estado CARGANDO
- `*ngIf="!datos || datos.length === 0"` → Estado SIN DATOS
- `*ngIf="datos && datos.length > 0"` → Estado CON DATOS
- `[hidden]="condicion"` → Visibilidad condicional

**Elementos interactivos**:
- `(click)="metodo()"` → Acciones del usuario
- `ion-item-sliding` → Gestos de swipe
- `ion-refresher` → Pull to refresh
- `ion-infinite-scroll` → Scroll infinito
- `formControlName` → Campos de formulario
- `[routerLink]` → Navegación declarativa

**Iteraciones**:
- `*ngFor="let item of items"` → Listas de datos a documentar

---

## 3. ANÁLISIS DE SERVICIOS Y ADAPTERS

### Qué buscar

```typescript
// Métodos HTTP típicos
this.http.get<T>(`${baseUrl}/endpoint/${param}`)
this.http.post<T>(`${baseUrl}/endpoint`, body)
this.http.put<T>(`${baseUrl}/endpoint/${id}`, body)
this.http.delete<T>(`${baseUrl}/endpoint/${id}`)
```

### Qué documentar por endpoint

| Campo | Fuente |
|-------|--------|
| Operación | Nombre descriptivo del método del servicio |
| Método HTTP | `get`, `post`, `put`, `delete` del `HttpClient` |
| URL | Template literal con parámetros resueltos |
| Parámetros de ruta | Segmentos dinámicos en la URL (`:id`) |
| Query params | Parámetros después del `?` |
| Body | Objeto enviado en POST/PUT |
| Respuesta | Tipo genérico `<T>` del Observable |

### Patrones de URL a resolver

```typescript
// Patrón con template literals
`tareasinspeccion/${idTarea}`
// → Endpoint: tareasinspeccion/{idTareaInspeccion}

// Patrón con query params
`endpoint?param1=${val1}&param2=${val2}`
// → Endpoint: endpoint?param1={valor1}&param2={valor2}

// Patrón con HttpParams
const params = new HttpParams().set('key', value);
// → Añadir como query params del endpoint
```

---

## 4. ANÁLISIS DE MODELOS E INTERFACES

### Qué documentar

Para cada interfaz/clase relevante:

| Campo | Tipo | Obligatorio | Descripción |
|-------|------|-------------|-------------|
| nombre | string | Sí | Nombre del campo |
| tipo | tipo TS | Sí | Tipo TypeScript (string, number, boolean, etc.) |
| opcional | ?/! | Sí | Si tiene `?` es opcional |
| descripción | string | Sí | Propósito funcional del campo |

### Interfaces anidadas

Documentar la estructura completa de objetos anidados, especialmente:
- Objetos con `informeInspeccion`, `condicionesEconomicas`, `desglose`
- Arrays tipados que indican colecciones de datos

---

## 5. ANÁLISIS DE ENUMERACIONES

### Qué documentar

```typescript
// Ejemplo de enum a documentar
enum EstadoTasacion {
  AVISO = 0,
  BORRADOR = 1,
  ABIERTA = 2,
  CERRADA = 3
}
// → Tabla: Estado | Código | Descripción
```

Para cada enumeración:
- Nombre del enum y ubicación del fichero
- Todos los valores con su código/valor
- Descripción funcional de cada valor
- Uso identificado en el código (dónde se referencia)

---

## 6. ANÁLISIS DE GUARDS

### Qué documentar

Para cada guard:
1. **Nombre**: Nombre de la clase
2. **Tipo**: `CanActivate`, `CanDeactivate`, `CanLoad`
3. **Condición**: Qué evalúa para permitir/denegar
4. **Éxito**: Qué ocurre cuando la condición se cumple
5. **Fallo**: Qué ocurre cuando la condición no se cumple (redirect, toast, bloqueo)
6. **Rutas protegidas**: Listar todas las rutas que usan este guard

### Patrones comunes

```typescript
// Guard de perfil
canActivate() {
  return this.userService.esPerito(); // → Solo peritos
}

// Guard de validación
canDeactivate() {
  return this.hasRequiredPhotos(); // → Valida condición antes de salir
}

// Guard de auditoría (side effect)
canActivate() {
  this.auditService.registrar(); // → Efecto secundario + permite paso
  return true;
}
```

---

## 7. ANÁLISIS DE STORES / STATE MANAGEMENT

### Qué documentar

- Estado inicial del store
- Actions/mutations que modifican el estado
- Selectors/getters que exponen datos
- Effects que realizan llamadas API
- Relación entre componentes y el store

---

## 8. ANÁLISIS DE PIPES Y DIRECTIVAS

### Pipes relevantes para documentación

- Pipes de formato de datos (currency, date, number)
- Pipes de transformación (formatComma, estadoLabel)
- Documentar el formato de salida para incluirlo en la descripción de campos

### Directivas relevantes

- Directivas de validación de formularios
- Directivas de comportamiento condicional
- Directivas de formato de entrada (máscaras, caracteres permitidos)

---

## 9. DETECCIÓN DE PATRONES TECNOLÓGICOS

### Angular + Ionic

- `IonicModule` — Componentes Ionic (ion-content, ion-item, etc.)
- `ModalController` — Gestión de modales
- `AlertController` — Alertas de confirmación
- `ToastController` — Mensajes toast
- `NavController` — Navegación Ionic
- `Platform` — Detección de plataforma (iOS/Android/Web)
- `Capacitor plugins` — Acceso a cámara, GPS, storage nativo

### Angular estándar

- `ReactiveFormsModule` — Formularios reactivos
- `HttpClientModule` — Llamadas HTTP
- `RouterModule` — Navegación
- `NgRx / NGXS / Akita` — State management

### React

- `useState` / `useEffect` — Estado y ciclo de vida
- `React Router` — Navegación
- `Redux / Zustand / MobX` — State management
- `fetch` / `axios` — Llamadas HTTP

---

## 10. RESTRICCIONES DE ANÁLISIS

- Solo documentar lo que se pueda verificar en el código fuente
- No extrapolar comportamiento de backend que no esté reflejado en el frontend
- **NO crear casos funcionales inferidos**: Registrar en la tabla de dudas cualquier comportamiento deducido pero no explícito en el código
- No documentar código comentado o sin uso aparente
- Priorizar la documentación de flujos principales sobre utilidades internas
