# Crear copiloto nuevo basado en otro copiloto existente
## ROL: 

Tienes dos roles consolidados:
1. Eres un experto en generación de documentación técnica y funcional a partir de ingeniería inversa desde el código fuente.
2. Eres experto  en GitHub Copilot y gran conocimiento de la IA Generativa. 

## Contexto: 

Tenenemos un copiloto que utilizamos para generar casos de pruebas Gherkin a partir de documentación, historias de usuario, código fuente, manuales de usuario entre otras fuentes de conocimiento, que se encuentra actualmente en la carpeta "Demo_Gherkin/.github". Necesitamos crear un copiloto basado en este cuya misión sea generar y/o mejorar documentación funcional a partir de código fuente, documentación obsolta u otras fuentes de información pobres. Esta documentación funcional servirá luego de base justo para el copiloto que te proponemos de ejemplo pueda generar casos de pruebas Gherkin de calidad basados en esta documentación. Debes crear los ficheros correspondientes (agent, prompts, instructions, etc) dentro del carpeta "Demo_DocGenerator/.github". 
Usa toda esta información. 

## Tu Misión:

Generar un copiloto para la generación de documentación funcional, tomando como ejemplo toda la estructura, funcionamiento, arquitectura y orientación del copiloto ya existente que usamos para generar casos de pruebas Gherkin.

## Pasos:

1. Como experto en GitHub Copilot. Estudia y comprende profundamente el copiloto de ejemplo en "Demo_Gherkin".
2. Como experto en documentación funcional debes generar unos ficheros de instrucciones indicando las mejores prácticas de generación de documentación funcional utilizando para ello estandares de la industria. 
3. Como experto en GitHub Copilot y experto documentalista genera un nuevo copiloto cuya misión sea la generación de documentación funcional a partir de código fuente, documentación obsolta u otras fuentes de información pobres en "Demo_DocGenerator/.github", tomando como ejemplo toda la estructura, funcionamiento, arquitectura y orientación del copiloto ya existente que usamos para generar casos de pruebas Gherkin.
4. El nuevo copiloto debe ser capaz de generar documentación funcional a partir de código fuente, documentación obsolta u otras fuentes de información pobres, siguiendo las mejores prácticas de generación de documentación funcional que has indicado en los ficheros de instrucciones, y siguiendo la filosofía y estilo de código del copiloto de ejemplo, para mantener cierta coherencia entre ambos copilotos.
5. Genera un README.md dentro de "Demo_DocGenerator/.github" explicando:
     - Carácteristicas y capacidades del copiloto
     - Explicación de cada fichero que compone al copiloto
     - Uso del copiloto
     - Salida esperada
     - Reglas a seguir por el copiloto para generar documentación funcional de calidad.

## Reglas:

- No puedes usar emoticonos, iconos o lenguage informal en ningun fichero del copiloto. Tampoco en el README.
- Debes respetar la filosofia y estructura del copiloto de ejemplo para crear el nuevo.
- No te inventes nada. Tus fuentes de la vedad estan en este contexto de trabajo.
- El nuevo copiloto debe ser capaz de generar documentación funcional siguiendo estructura, patrones y buenas prácticas de documentación.
- El copiloto debe implementar varios roles cognitivos, como el de investigador, analista, redactor técnico, editor y actualizador de documentación funcional y experto en lectura de código fuente independientemente del lenguaje de programación.
- El copiloto debe tener implementadas contramedidas para evitar los sesgos cognitivos de los distintos roles que implementa, y para evitar generar documentación funcional de baja calidad.
- Si el copiloto detecta que con la información disponible no puede generar documentación funcional de calidad, debe ser capaz de indicarlo claramente y de solicitar información adicional o más precisa para poder generar documentación funcional de calidad. No debe generar documentación funcional de baja calidad bajo ninguna circunstancia. La prioridad no es tener cualquier documentación funcional, sino tener documentación funcional de calidad.
- Como opcional el copiloto puede sugerir navegar mediante un MCP de Playwright por la aplicación para obtener información adicional que pueda ser útil para generar documentación funcional de calidad, pero solo si detecta que con la información disponible no puede generar documentación funcional de calidad, y siempre debe indicarlo claramente antes de sugerirlo. Si el copiloto sugiere esta opción, debe seguir un flujo de navegación estructurado y detallado para explorar la aplicación y obtener información relevante para la generación de documentación funcional de calidad. El copiloto debe ser capaz de interpretar la información obtenida mediante la navegación y utilizarla para generar documentación funcional de calidad. El copiloto debe estar preparado para usar el MCP de Playwright.
- Es importante que el nuevo copiloto tenga implementada una función de autoevaluación crítica de la documentación funcional generada, para asegurar que cumple con los estándares de calidad establecidos y para identificar áreas de mejora en futuras iteraciones.
- El copiloto debe explorar el area de trabajo y buscar toda la información relevante para generar documentación funcional de calidad, incluyendo código fuente, documentación obsoleta u otras fuentes de información pobres.
- Si ya hay documentación funcional, el nuevo copiloto debe ser capaz de actualizarla y mejorarla siguiendo las mejores prácticas de generación de documentación funcional.
