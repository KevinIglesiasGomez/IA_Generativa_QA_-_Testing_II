# Code-Analysis-Instructions-for-Agent:Reverse-Engineering-Functional-Analyst

## Objective

Define-specific-code-analysis-techniques-agent-must-apply-to-extract-functional-info-from-each-app-layer.Organized-by-code-artifact-type.

---

## 1. ROUTING-MODULES-ANALYSIS

### What-to-Look-For

```typescript
// Patterns to identify in *-routing.module.ts or *.routes.ts files
{
  path: 'route',                    // → View route
  component: ComponentPage,         // → Main component
  canActivate: [Guard1, Guard2],    // → Access guards
  children: [...]                   // → Child routes (hierarchy)
  loadChildren: () => import(...)   // → Module lazy loading
  redirectTo: 'route'              // → Redirections
  data: { ... }                    // → Route metadata
}
```

### What-to-Document

-Complete-route-including-parent-segments
-Dynamic-parameters-with-name(`:idTasacion`,`:matricula`)
-Query-params-identified-in-component(`ActivatedRoute.queryParams`)
-Guards-in-`canActivate`,`canDeactivate`,`canLoad`
-Resolvers-if-exist

### Complete-Path-Construction

Traverse-route-hierarchy-to-build-complete-path:
```
/root/inspeccion/detalle/{idTareaInspeccion}/taller/{codInstalacion}
```

---

## 2. COMPONENT-ANALYSIS(PAGES)

### TypeScript-File(.page.ts/.component.ts)

**Lifecycle**:
-`constructor()`-Dependency-injection→identify-used-services
-`ngOnInit()`/`ionViewWillEnter()`-Initial-load→identify-API-calls-on-enter
-`ngOnDestroy()`/`ionViewWillLeave()`-Cleanup→identify-subscriptions

**State-variables**:
-Boolean-loading-variables(`loading`,`isLoading`,`loadingData`)
-Main-data-variables(`listado`,`detalle`,`formulario`)
-UI-control-variables(`showModal`,`isExpanded`,`selectedTab`)

**Action-methods**:
-Methods-called-from-template-executing-business-logic
-Navigation-methods(`router.navigate`,`navController.navigateForward`)
-API-service-call-methods

### Template-File(.page.html/.component.html)

**Visual-structure**:
-`<ion-header>`-Header-with-title,back-buttons,options
-`<ion-content>`-Main-content
-`<ion-footer>`-Footer-with-action-buttons
-`<ion-fab>`-Floating-action-buttons(FAB)

**State-conditionals**:
-`*ngIf="loading"`→LOADING-state
-`*ngIf="!datos || datos.length === 0"`→NO-DATA-state
-`*ngIf="datos && datos.length > 0"`→WITH-DATA-state
-`[hidden]="condicion"`→Conditional-visibility

**Interactive-elements**:
-`(click)="metodo()"`→User-actions
-`ion-item-sliding`→Swipe-gestures
-`ion-refresher`→Pull-to-refresh
-`ion-infinite-scroll`→Infinite-scroll
-`formControlName`→Form-fields
-`[routerLink]`→Declarative-navigation

**Iterations**:
-`*ngFor="let item of items"`→Data-lists-to-document

---

## 3. SERVICES+ADAPTERS-ANALYSIS

### What-to-Look-For

```typescript
// Typical HTTP methods
this.http.get<T>(`${baseUrl}/endpoint/${param}`)
this.http.post<T>(`${baseUrl}/endpoint`, body)
this.http.put<T>(`${baseUrl}/endpoint/${id}`, body)
this.http.delete<T>(`${baseUrl}/endpoint/${id}`)
```

### What-to-Document-per-Endpoint

|Field|Source|
|-------|--------|
|Operation|Service-method-descriptive-name|
|HTTP-Method|`get`,`post`,`put`,`delete`-from-`HttpClient`|
|URL|Template-literal-with-resolved-parameters|
|Route-parameters|Dynamic-URL-segments(`:id`)|
|Query-params|Parameters-after-`?`|
|Body|Object-sent-in-POST/PUT|
|Response|Observable-generic-type-`<T>`|

### URL-Patterns-to-Resolve

```typescript
// Pattern with template literals
`tareasinspeccion/${idTarea}`
// → Endpoint: tareasinspeccion/{idTareaInspeccion}

// Pattern with query params
`endpoint?param1=${val1}&param2=${val2}`
// → Endpoint: endpoint?param1={valor1}&param2={valor2}

// Pattern with HttpParams
const params = new HttpParams().set('key', value);
// → Add as endpoint query params
```

---

## 4. MODELS+INTERFACES-ANALYSIS

### What-to-Document

For-each-relevant-interface/class:

|Field|Type|Required|Description|
|-------|------|-------------|-------------|
|name|string|Yes|Field-name|
|type|tipo-TS|Yes|TypeScript-type(string,number,boolean,etc.)|
|optional|?/!|Yes|If-has-`?`-is-optional|
|description|string|Yes|Field-functional-purpose|

### Nested-Interfaces

Document-complete-structure-of-nested-objects,especially:
-Objects-with-`informeInspeccion`,`condicionesEconomicas`,`desglose`
-Typed-arrays-indicating-data-collections

---

## 5. GUARDS-ANALYSIS

### What-to-Look-For

```typescript
// Guard implementation
@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(route, state): Observable<boolean> {
    // Evaluated condition
    return this.authService.isLoggedIn();
  }
}
```

### What-to-Document

|Field|Info|
|-------|-----------|
|Guard-name|Class-name+file|
|Type|CanActivate,CanDeactivate,CanLoad|
|Evaluated-condition|Method/logic-determining-access|
|Behavior-on-failure|Redirect,message,block|
|Protected-routes|Routes-using-this-guard|

---

## 6. STATE-MANAGEMENT-ANALYSIS(STORES)

### What-to-Look-For

```typescript
// NgRx / Akita / custom store patterns
@State({
  name: 'storeName',
  defaults: { ... }
})
export class StoreClass {
  // Actions
  @Action(ActionName)
  actionMethod(ctx, payload) { ... }
  
  // Selectors
  @Selector()
  static selectorName(state) { ... }
}
```

### What-to-Document

|Element|Description|
|---------|--------------|
|Store-name|State-identifier|
|Managed-state|Data-structure-managed|
|Available-actions|Methods-modifying-state|
|Selectors|State-queries|
|Side-effects|API-calls-from-store|

---

## 7. ENUMS-ANALYSIS

### What-to-Look-For

```typescript
export enum StatusType {
  PENDING = 'PENDING',
  APPROVED = 'APPROVED',
  REJECTED = 'REJECTED'
}
```

### What-to-Document

Complete-table-per-enum:

|Value|Code|Description|
|-------|--------|--------------|
|PENDING|'PENDING'|Pending-approval-status|
|APPROVED|'APPROVED'|Approved-status|
|REJECTED|'REJECTED'|Rejected-status|

---

## 8. CROSS-CORRELATION

### Purpose

Connect-info-from-different-layers-to-build-complete-functional-vision.

### Correlation-Examples

1.**Route-+Component+Service**:
   -Route:`/inspecciones/:id`
   -Component:`InspeccionDetallePage`
   -Service-call:`getInspeccionById(id)`

2.**Guard+Route+Profile**:
   -Guard:`AdminGuard`
   -Protected-route:`/admin/usuarios`
   -Required-profile:`ROLE_ADMIN`

3.**Enum+View-state+Business-rule**:
   -Enum:`EstadoInspeccion.COMPLETADA`
   -UI-state:Green-badge-"Completed"
   -Business-rule:If-completed→enable-"Generate-report"-button

---

## 9. ANTI-PATTERNS-TO-AVOID

-❌Document-commented-code/apparently-unused
-❌Assume-backend-behavior-not-reflected-in-frontend
-❌Infer-business-rules-not-expressed-in-code
-❌Omit-routes/endpoints/states-considering-them-secondary
-❌Document-functionality-from-external-dependencies-without-verifying-actual-usage-in-project
