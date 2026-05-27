# Reutilización del Módulo Budget Enforcement

Este documento explica cómo reutilizar el módulo de control de presupuesto de tokens (`shared_budget_enforcement.instructions.md`) en otros proyectos de copilotos personalizados.

## ¿Qué es Budget Enforcement?

Es una capa de control inteligente que:

✅ Monitorea el consumo de tokens en tiempo real  
✅ Advierte proactivamente cuando se alcanzan umbrales (75%, 90%)  
✅ Optimiza automáticamente el uso de herramientas  
✅ Crea checkpoints para recuperación de sesiones  
✅ Activa modo económico cuando el presupuesto es bajo  
✅ Previene pérdida de trabajo por agotamiento de presupuesto  

## Métodos de Reutilización

### Opción 1: Copia Directa (Más Simple)

Para proyectos independientes sin dependencias compartidas:

```bash
# Copiar el archivo a otro proyecto
cp .github/instructions/shared_budget_enforcement.instructions.md \
   /ruta/a/otro/proyecto/.github/instructions/

# O usando PowerShell en Windows
Copy-Item .github\instructions\shared_budget_enforcement.instructions.md `
          C:\ruta\a\otro\proyecto\.github\instructions\
```

**Ventajas:**
- Independencia total entre proyectos
- Sin configuración adicional
- Personalización libre por proyecto

**Desventajas:**
- Duplicación de contenido
- Actualizaciones manuales en cada proyecto

---

### Opción 2: Git Submodule (Para Múltiples Proyectos)

Para organizaciones con varios proyectos de copilotos:

#### 1. Crear repositorio compartido

```bash
# Crear repositorio de instrucciones compartidas
mkdir copilot-shared-instructions
cd copilot-shared-instructions
git init

# Crear estructura
mkdir -p instructions
cp ../Demo_AutomatizacionPlaywright/.github/instructions/shared_budget_enforcement.instructions.md \
   instructions/

# Agregar README
cat > README.md << 'EOF'
# Instrucciones Compartidas para Copilotos Personalizados

Módulos reutilizables:
- `instructions/shared_budget_enforcement.instructions.md`: Control de presupuesto de tokens
EOF

# Commit y push
git add .
git commit -m "Initial commit: Budget enforcement module"
git remote add origin https://github.com/tu-org/copilot-shared-instructions.git
git push -u origin main
```

#### 2. Usar como submodule en cada proyecto

```bash
# En cada proyecto de copiloto
cd /ruta/a/tu/proyecto
git submodule add https://github.com/tu-org/copilot-shared-instructions.git .github/shared

# Crear symlink o referencia
cd .github/instructions
ln -s ../shared/instructions/shared_budget_enforcement.instructions.md ./
```

#### 3. Actualizar en todos los proyectos

```bash
# Actualizar submodule a última versión
git submodule update --remote .github/shared
git add .github/shared
git commit -m "Update shared instructions"
```

**Ventajas:**
- Actualizaciones centralizadas
- Versionado controlado
- Sincronización automática

**Desventajas:**
- Complejidad adicional
- Dependencia de repositorio externo

---

### Opción 3: Paquete NPM Privado (Para Organizaciones)

Para empresas con registro NPM privado:

#### 1. Crear paquete npm

```bash
mkdir @tu-org-copilot-budget
cd @tu-org-copilot-budget

# package.json
cat > package.json << 'EOF'
{
  "name": "@tu-org/copilot-budget-enforcement",
  "version": "1.0.0",
  "description": "Budget enforcement module for custom GitHub Copilots",
  "main": "index.js",
  "files": [
    "instructions/",
    "README.md"
  ],
  "keywords": ["github-copilot", "budget", "tokens"],
  "author": "Tu Organización",
  "license": "MIT"
}
EOF

# Estructura
mkdir instructions
cp ../shared_budget_enforcement.instructions.md instructions/

# Publicar
npm publish --access restricted
```

#### 2. Instalar en proyectos

```bash
# En cada proyecto
npm install --save-dev @tu-org/copilot-budget-enforcement

# Crear symlink en .github/instructions/
ln -s ../../node_modules/@tu-org/copilot-budget-enforcement/instructions/shared_budget_enforcement.instructions.md \
     .github/instructions/
```

**Ventajas:**
- Versionado semántico
- Gestión de dependencias con npm
- CI/CD integrado

**Desventajas:**
- Requiere registry privado
- Overhead de configuración

---

## Personalización por Proyecto

Puedes ajustar los límites según el tipo de proyecto:

### Para proyectos de testing (como este)
```yaml
---
description: Control de presupuesto - Configuración para Testing
applyTo: "**"
priority: 100
---

# Budget Enforcement - Pruebas Automatizadas

## Límites ajustados para testing
- Límite máximo: 200,000 tokens
- Umbral advertencia: 150,000 tokens (75%)
- Tarea simple: 20,000 tokens
- Tarea media: 50,000 tokens (1-3 escenarios)
- Tarea compleja: 100,000 tokens (refactorización)
```

### Para proyectos de desarrollo backend
```yaml
---
description: Control de presupuesto - Configuración para Backend
applyTo: "**"
priority: 100
---

# Budget Enforcement - Desarrollo Backend

## Límites ajustados para backend
- Límite máximo: 200,000 tokens
- Umbral advertencia: 150,000 tokens (75%)
- Tarea simple: 15,000 tokens (endpoint único)
- Tarea media: 40,000 tokens (CRUD completo)
- Tarea compleja: 80,000 tokens (módulo completo)
```

### Para proyectos de frontend
```yaml
---
description: Control de presupuesto - Configuración para Frontend
applyTo: "**"
priority: 100
---

# Budget Enforcement - Desarrollo Frontend

## Límites ajustados para frontend
- Límite máximo: 200,000 tokens
- Umbral advertencia: 150,000 tokens (75%)
- Tarea simple: 25,000 tokens (componente único)
- Tarea media: 60,000 tokens (página completa)
- Tarea compleja: 120,000 tokens (feature completo)
```

---

## Integración en Agentes Personalizados

### En archivos .agent.md

Mencionar en las restricciones del agente:

```yaml
---
name: "Mi Copiloto Personalizado"
description: "..."
tools: [...]
model: "Claude Sonnet 4.5"
---

# Mi Copiloto

## Restricciones de presupuesto de tokens
- Control automático de presupuesto según `shared_budget_enforcement.instructions.md`
- Advertir proactivamente al alcanzar 75% y 90% del límite
- Crear checkpoints automáticos en hitos clave
- Activar modo económico con menos de 25% restante
- Sugerir fragmentación cuando una tarea amenace agotar presupuesto
```

### En archivos .instructions.md

Las instrucciones se aplican automáticamente según el patrón `applyTo: "**"` del frontmatter YAML. No requiere referencia explícita.

---

## Comandos Disponibles para Usuarios

Estos comandos funcionan en cualquier copiloto que use este módulo:

| Comando | Descripción |
|---------|-------------|
| `estado presupuesto` | Muestra consumo actual y estimaciones |
| `optimizar` | Activa modo económico manualmente |
| `dividir tarea` | Sugiere puntos de división óptimos |
| `checkpoint` | Crea checkpoint manual inmediato |
| `estimar tarea` | Estima tokens antes de ejecutar |

---

## Versionado y Actualizaciones

### Versionado semántico recomendado

- **1.0.x**: Correcciones de bugs, ajustes menores
- **1.x.0**: Nuevas funcionalidades compatibles
- **x.0.0**: Cambios breaking, nueva arquitectura

### Changelog ejemplo

```markdown
# Changelog - Budget Enforcement

## [1.1.0] - 2026-04-27
### Added
- Comando `estimar tarea` para pre-calcular consumo
- Soporte para fragmentación inteligente de tareas

### Changed
- Umbral de modo económico ajustado a 25% (era 20%)
- Checkpoints ahora incluyen métricas de eficiencia

## [1.0.0] - 2026-04-27
### Added
- Módulo inicial de budget enforcement
- Monitoreo automático de tokens
- Checkpoints automáticos
- Modo económico
```

---

## Soporte y Contribuciones

### Reportar issues
- Crear issue en el repositorio compartido
- Incluir: proyecto afectado, comportamiento esperado vs actual, logs

### Proponer mejoras
- Fork del repositorio
- Branch con nombre descriptivo: `feature/nombre-mejora`
- Pull request con descripción detallada

### Testing
Probar cambios en al menos 2 tipos de proyectos diferentes antes de merge:
- ✅ Proyecto de testing/QA
- ✅ Proyecto de desarrollo backend o frontend

---

## Ejemplos de Uso

### Ejemplo 1: Advertencia proactiva

Usuario inicia tarea grande:
```
Usuario: "Automatiza los 15 escenarios del feature Login"
```

Copiloto responde:
```
📋 Estimación de presupuesto necesaria:

Para automatizar 15 escenarios de Login:
- Escenarios simples (5): ~5,000 tokens c/u = 25,000 tokens
- Escenarios medios (8): ~10,000 tokens c/u = 80,000 tokens
- Escenarios complejos (2): ~15,000 tokens c/u = 30,000 tokens

Estimación total: ~135,000 tokens
Presupuesto actual disponible: 200,000 tokens
Restante tras completar: 65,000 tokens (32%)

⚠️ Recomendación: Proceder con todos los escenarios, pero se activará
modo económico al finalizar.

¿Continuar? (sí/no/dividir)
```

### Ejemplo 2: Checkpoint automático

Al alcanzar 75%:
```
💾 Checkpoint automático guardado (75% del presupuesto consumido)

Estado preservado en: /memories/session/login_feature_checkpoint_75.md

Progreso actual:
- ✅ Escenarios completados: 10/15
- ⏸️ Escenarios pendientes: 5/15
- Tokens restantes: 50,000 (suficiente para continuar)
```

### Ejemplo 3: Modo económico activado

Al quedar 25%:
```
🔋 Modo económico activado automáticamente

Tokens restantes: 48,000 / 200,000 (24%)

Restricciones activas:
- Búsquedas: Solo grep_search con filtros específicos
- Lecturas: Máximo 100 líneas por archivo
- Respuestas: Formato conciso obligatorio
- Validaciones: Solo operaciones críticas

Esto maximizará el aprovechamiento para completar los 5 escenarios restantes.
```

---

## FAQ

**P: ¿Funciona con modelos diferentes a Claude Sonnet 4.5?**  
R: Sí, es agnóstico al modelo. Los límites de tokens pueden ajustarse según el modelo usado.

**P: ¿Puedo desactivar temporalmente el control de presupuesto?**  
R: No recomendado, pero puedes comentar la línea en el frontmatter `applyTo: "**"`.

**P: ¿Los checkpoints afectan el presupuesto?**  
R: Mínimamente (~500-1000 tokens), pero son esenciales para recuperación.

**P: ¿Qué pasa si mi tarea requiere más de 200,000 tokens?**  
R: El módulo sugerirá fragmentación automática antes de comenzar.

**P: ¿Funciona con workspace multi-root?**  
R: Sí, el módulo es compatible con workspaces simples y multi-root.

---

## Licencia

Este módulo es parte del proyecto Demo_AutomatizacionPlaywright.
Puedes reutilizarlo libremente en tus proyectos personales o empresariales.

---

**Versión**: 1.0.0  
**Última actualización**: 27 de abril de 2026  
**Autor**: COMUNIDAD QA CE  
**Proyecto origen**: Demo_AutomatizacionPlaywright
