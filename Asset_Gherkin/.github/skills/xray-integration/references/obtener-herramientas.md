# Obtener el repositorio de herramientas

Procedimiento para resolver `${tools_repo_url}` en una copia local utilizable.

## 1. Conseguir la URL o ruta

Si no se conoce todavía en la conversación actual, pregúntala antes de continuar. Acepta dos formatos:

- **Ruta local ya existente** (típico en desarrollo dentro del propio monorepo): p. ej.
  `C:\Users\<usuario>\OTT\demos-ia` o `../../demos-ia`. Útil cuando quien usa la skill ya tiene el repositorio
  completo descargado al lado.
- **URL de un repositorio git** (típico en una instalación de cliente externo, o cuando no existe copia
  local): p. ej. `https://git.miempresa.com/scm/qa/demos-ia.git`. Puede ser este mismo repositorio, un fork,
  un mirror interno del cliente, o un repositorio reducido que contenga solo `utilities/`.

No asumas ningún valor por defecto: si no se aporta, pregúntala explícitamente y espera la respuesta antes de
seguir.

## 2. Resolver una copia local

```
¿${tools_repo_url} existe como carpeta en disco?
├─ Sí, y contiene utilities/XRAY  → úsala directamente, sin clonar nada.
└─ No es una ruta local, o es una ruta local sin utilities/XRAY  → trátala como URL git:
   ├─ ¿Ya existe una caché local de esa URL? (ver carpeta de caché más abajo)
   │   ├─ Sí → actualízala: git -C <cache> pull
   │   └─ No → clónala: git clone --depth 1 <tools_repo_url> <cache>
   └─ Usa <cache>/utilities/XRAY como copia local
```

Carpeta de caché recomendada (evita volver a clonar en cada ejecución): `.copilot-tools-cache/<nombre-repo>`
dentro del proyecto de salida (`e2e_repo` o equivalente) que esté usando el copiloto en ese momento.
`<nombre-repo>` es el último segmento de la URL sin `.git` (p. ej. `demos-ia`).

Ejemplo (PowerShell) de resolución cuando es una URL git y no hay caché previa:

```powershell
$cache = ".copilot-tools-cache/demos-ia"
if (-not (Test-Path $cache)) {
    git clone --depth 1 $tools_repo_url $cache
} else {
    git -C $cache pull
}
$XRAY = Join-Path $cache "utilities/XRAY"
pip install -r "$XRAY/requirements.txt"
```

Si la URL de git requiere autenticación, debe estar ya configurada en el entorno de quien ejecuta el comando
(token, SSH, credential manager); no la solicites ni la guardes en ningún archivo.

## 3. Casos especiales

- **El repositorio proporcionado no tiene `utilities/XRAY` en esa ruta**: pregunta si la estructura es
  distinta (por ejemplo, un repositorio dedicado solo a utilidades, donde el contenido podría estar en la
  raíz) y ajusta la ruta resuelta en el paso 2 en consecuencia.
- **No hay acceso a git ni a red** (entorno aislado): pide directamente una ruta local ya descomprimida con el
  contenido de `utilities/XRAY` y úsala sin intentar clonar.
- **Ejecuciones repetidas en la misma sesión/proyecto**: una vez resuelta la copia local, no vuelvas a
  preguntar por `${tools_repo_url}` en la misma conversación; reutiliza la ruta ya resuelta.
