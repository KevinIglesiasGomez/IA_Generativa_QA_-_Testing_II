# Tester Creativo

Copiloto de VS Code especializado en generar pruebas creativas e innovadoras para asegurar la calidad de software, explorando casos limite y escenarios no convencionales.

**Genera automáticamente informes concisos (4-6 páginas) con 10-20 escenarios de prueba priorizados + 5-8 pruebas extremas "muy locas" que desafían los límites de lo convencional.**

---

## Que hace

Analiza capturas de pantalla, documentacion, codigo fuente o HTML de una aplicacion y genera un informe completo con escenarios de prueba que las pruebas convencionales no cubren: casos limite, interacciones no obvias, comportamientos adversariales y situaciones de concurrencia, entre otros.

Utiliza el modelo **EXPLORA** para clasificar y priorizar los escenarios creativos, enfocandose en los de mayor valor (alta prioridad) y presentando el resto en formato compacto.

**NUEVO**: Incluye una sección especial de **Pruebas Extremas e Inesperadas** con escenarios altamente creativos que exploran lo improbable pero técnicamente posible.

**Resultado**: Un informe accionable, escaneable y no abrumador, listo para ser utilizado por el equipo de QA.

---

## Características clave

- ✅ **Automatico**: genera el informe completo sin necesidad de aprobacion iterativa
- ✅ **Conciso**: maximo 4-6 paginas, escaneable rapidamente
- ✅ **Priorizado**: 10-20 escenarios de alta prioridad con detalle completo
- ✅ **Visual**: tablas y listas para facilitar lectura rapida
- ✅ **Accionable**: cada escenario incluye pasos claros y ejecutables
- ✅ **Creativo**: exploracion de casos limite y escenarios no convencionales
- ✅ **Basado en modelo EXPLORA**: cobertura sistematica de 7 categorias de riesgo
- 🚀 **NUEVO: Pruebas Extremas**: 5-8 escenarios "muy locos" que desafían suposiciones implícitas

### Por qué este enfoque

**Velocidad**: obten un informe completo en una sola ejecucion, sin iteraciones.

**Claridad**: formato conciso y visual que facilita la revision rapida del equipo.

**Enfoque**: se priorizan automaticamente los escenarios de mayor valor, evitando ruido.

**Cobertura balanceada**: 10-20 escenarios detallados proporcionan cobertura adecuada sin abrumar.

---

## Modelo EXPLORA

| Letra | Categoria | Que cubre |
|---|---|---|
| **E** | Extremos y Limites | Valores limite, tipos inesperados, volumenes extremos |
| **X** | Cross-cutting | Seguridad, rendimiento percibido, accesibilidad, compatibilidad |
| **P** | Percepcion del usuario | Usabilidad no obvia, feedback, primera impresion |
| **L** | Logica de negocio | Reglas de negocio, flujos complejos, coherencia de datos |
| **O** | Operaciones concurrentes y de estado | Concurrencia, gestion de estado, interrupciones |
| **R** | Resiliencia y recuperacion | Manejo de errores, recuperacion, degradacion elegante |
| **A** | Adversarial / Antagonista | Uso malintencionado, abuso del sistema, ingenieria social |

---

## 🚀 Pruebas Extremas e Inesperadas (NUEVO)

Además del modelo EXPLORA estructurado, el agente genera una sección especial de **pruebas extremadamente creativas** que desafían los límites de la imaginación:

### Características
- **Altamente improbables pero técnicamente posibles**
- **Combinaciones inesperadas de acciones**
- **Comportamientos absurdos pero válidos técnicamente**
- **Desafían suposiciones implícitas de los desarrolladores**

### Categorías de pruebas extremas

1. **Usuario Caótico**: acciones aleatorias, clicks múltiples, recarga constante, cambios de idioma en medio de flujos
2. **Usuario Temporal**: formularios abiertos 7 días, cambios de fecha del sistema, suspender/reanudar sistema
3. **Multilenguaje Extremo**: mezcla RTL+LTR+emojis, caracteres Unicode raros, direccionales invisibles
4. **Hacker Absurdo**: manipulación del DOM con DevTools, cambiar métodos HTTP, inyectar CSS invisible
5. **Volumen Extremo**: 1 millón de caracteres, 10,000 archivos simultáneos, 500 items en carrito
6. **Usuario del Pasado/Futuro**: IE5, JavaScript deshabilitado, 320x240 píxeles, conexión 56k
7. **Combinaciones Imposibles**: race conditions, estados contradictorios simultáneos
8. **Culturalmente Inesperado**: nombres de 1 carácter, teléfonos de 5 dígitos, direcciones sin número
9. **Saboteador Creativo**: 5 extensiones modificando DOM simultáneamente, rotación continua, todas las funciones de accesibilidad activas
10. **Mundo Real Extremo**: usuario en avión cruzando zonas horarias, estación espacial (1000ms ping), evento masivo (10,000 en mismo WiFi)

### Filosofía

> "Si un tester experimentado lee esta prueba y dice 'jamás se me habría ocurrido eso', entonces es una buena prueba extrema."

**Balance recomendado:**
- 80-85% enfoque en EXPLORA (estructurado y confiable)
- 15-20% enfoque en Pruebas Extremas (creativo y explorador)

---

## Estructura del proyecto

```
.github/
  agents/
    tester_creativo.agent.md          # Definicion del agente
  instructions/
    main_TesterCreativo.instructions.md                  # Instrucciones centrales y modelo EXPLORA
    tecnicasCreativas_TesterCreativo.instructions.md     # Tecnicas de testing creativo y heuristicas
    buenasPracticas_TesterCreativo.instructions.md       # Buenas practicas y antipatrones
    informe_TesterCreativo.instructions.md               # Generacion y actualizacion de informes
    escenariosNoConvencionales_TesterCreativo.instructions.md  # Catalogo de escenarios no convencionales
    pruebasExtremas_TesterCreativo.instructions.md       # 🚀 Pruebas extremas e inesperadas (NUEVO)
  prompts/
    prompt_TesterCreativo.prompt.md              # Prompt completo del agente
    prompt_TesterCreativo_reducido.prompt.md     # Prompt en version reducida
```

---

## Entradas soportadas

El copiloto puede trabajar a partir de:

- **Capturas de pantalla**: analiza elementos visibles, infiere comportamiento, detecta ambiguedades.
- **Documentacion**: historias de usuario, criterios de aceptacion, especificaciones funcionales, diagramas de flujo.
- **Codigo fuente**: cualquier lenguaje; analiza logica, flujos condicionales, manejo de errores, integraciones.
- **HTML / Markup**: estructura del DOM, validaciones HTML5, atributos de accesibilidad, eventos.

---

## Como funciona

### Flujo de trabajo

1. **Confirmacion inicial**: el agente pregunta que tipo de informacion se va a proporcionar y cual es la funcionalidad a explorar.
2. **Analisis profundo**: pasa por 4 roles cognitivos internos (Analizador, Generador Creativo, Revisor Critico, Evaluador de Impacto).
3. **Priorizacion de escenarios**: enfoque en escenarios de alta prioridad (score >= 6.0) que realmente aporten valor.
4. **Generacion de pruebas extremas**: crea 5-8 escenarios "muy locos" que desafían suposiciones implícitas (Usuario Caótico, Temporal, Multilenguaje, Hacker Absurdo, Volumen Extremo, etc.).
5. **Generacion del informe completo**: crea un informe conciso (4-6 paginas) con:
   - Descripcion funcional breve (2-3 parrafos)
   - Tabla resumen de cobertura EXPLORA
   - Top 10-15 riesgos mas criticos
   - **10-20 escenarios de alta prioridad** con detalle completo (pasos, precondiciones, resultados esperados)
   - Escenarios de prioridad media/baja en tabla compacta
   - **🚀 5-8 Pruebas Extremas e Inesperadas** en formato diferenciado
   - Top 3-5 recomendaciones
6. **Entrega**: el ingeniero recibe el informe completo, listo para revision y ejecucion por el equipo de QA.

### Principios del informe

- **Concision**: maximo 4-6 paginas, escaneable rapidamente
- **Calidad sobre cantidad**: enfoque en 10-20 escenarios de mayor valor
- **Visual y accionable**: uso de tablas y listas para facilitar lectura
- **Sin redundancia**: cada informacion aparece una sola vez
- **Priorizado**: escenarios ordenados por impacto y probabilidad

---

## Tecnicas creativas incluidas

- Analisis de valores limite (Boundary Value Analysis)
- Particion de equivalencia
- Tabla de decision
- Transicion de estados
- Testing exploratorio con heuristicas (SFDPOT, FEW HICCUPPS)
- Testing por mutacion conceptual
- Testing combinatorio (Pairwise)
- Inyeccion de fallos
- Heuristicas de pensamiento lateral: inversion, analogia, personificacion de usuarios extremos, WWWWWH

---

## Priorizacion de escenarios

Cada escenario se evalua con una matriz ponderada:

| Criterio | Peso |
|---|---|
| Probabilidad de ocurrencia | 30% |
| Impacto en el usuario | 25% |
| Impacto en el negocio | 25% |
| Dificultad de deteccion por otros medios | 20% |

- **Alta prioridad**: Score >= 7.0
- **Media prioridad**: Score entre 4.0 y 6.9
- **Baja prioridad**: Score < 4.0

---

## Informes generados

El copiloto genera un documento en el directorio `informes/`:

- **Informe** (`informe_<nombre>.md`): documento conciso (4-6 paginas) que incluye:
  - Metadata: fuente analizada, fecha, complejidad
  - Descripcion funcional breve
  - Tabla resumen de cobertura EXPLORA
  - Top 10-15 riesgos principales (score >= 6.0)
  - 10-20 escenarios de alta prioridad con detalle completo
  - Escenarios adicionales en tabla compacta
  - Top 3-5 recomendaciones

**Opcional**: Si se requieren actualizaciones futuras, se puede crear una **bitacora** (`bitacora_<nombre>.md`) para registrar cambios incrementales.

### Estructura del informe

El informe esta diseñado para ser:
- **Escaneable**: formato visual con tablas y listas
- **Accionable**: pasos claros y ejecutables para cada escenario
- **Priorizado**: enfoque en los escenarios de mayor impacto
- **Conciso**: sin informacion redundante o innecesaria

---

## Publico objetivo

- QA Architects y lideres de QA
- QA Engineers y testers
- Desarrolladores interesados en mejorar la calidad de su codigo
- Gerentes de proyecto y stakeholders

---

## Requisitos

- VS Code con GitHub Copilot habilitado
- Modelo: Claude Sonnet 4.5

---

## Uso

1. Abrir el workspace `Tester_creativo.code-workspace` en VS Code.
2. Invocar al agente **Tester Creativo** desde el chat de Copilot.
3. Proporcionar la informacion de la funcionalidad a analizar (captura, documentacion, codigo o HTML).
4. El agente analizara en profundidad y generara un informe completo con 10-20 escenarios creativos priorizados.
5. Revisar el informe generado en el directorio `informes/`.
6. Ejecutar los escenarios propuestos con el equipo de QA.

### Ejemplo de interaccion

```
Usuario: Analiza esta captura de pantalla de un formulario de registro

Tester Creativo:
- Confirma tipo de entrada y funcionalidad a explorar
- Realiza analisis profundo (4 roles cognitivos)
- Identifica riesgos segun modelo EXPLORA
- Genera informe completo con 10-20 escenarios creativos
- Entrega informe en formato Markdown listo para usar
```

El proceso es **directo y automatizado**: proporcionas la informacion, el agente analiza y entrega el informe completo sin necesidad de iteraciones adicionales.
