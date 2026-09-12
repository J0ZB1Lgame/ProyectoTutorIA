# ProyectoTutorIA

Proyecto de la asignatura **Desarrollo de Aplicaciones con IA**: desarrollo de un
Asistente Experto basado en RAG y Agentes.

## Enfoque elegido: Tutor Académico Personalizado

**TutorIA** es un tutor académico personalizado especializado en
**Programación en Python y fundamentos de lógica y algoritmos**, dirigido a
estudiantes universitarios en niveles introductorio e intermedio.

El asistente está diseñado para:
- Explicar conceptos de programación apoyándose en el material propio del
  curso (temario, apuntes, guías de ejercicios).
- Priorizar la comprensión sobre la respuesta directa (da pistas antes de
  entregar soluciones completas).
- Revisar código del estudiante señalando y explicando errores conceptuales,
  no solo corrigiéndolos.
- Responder en un formato de salida predecible: **Markdown** para
  explicaciones teóricas y **JSON** para ejercicios/evaluaciones.

## Alcance de este Avance (Avance 1)

Según indicación del profesor, este avance **no incluye conexión con ningún
modelo LLM**. El alcance cubre únicamente:

1. **Diseño de Prompts** — System Prompt que define rol, tono, reglas de
   comportamiento y formato de salida del asistente.
2. **Few-Shot Prompting** — Ejemplos incrustados en el prompt para guiar el
   formato de la respuesta (Markdown / JSON).
3. **Estrategia de Delimitadores** — Uso de etiquetas XML
   (`<course_material>`, `<student_question>`, `<student_code>`) y triple
   comillas para separar claramente contexto, instrucciones y datos del
   estudiante dentro del prompt.

La conexión real con un LLM y la incorporación de RAG (carga del material del
curso) quedan planificadas para avances posteriores.

## Estructura del repositorio

```
ProyectoTutorIA/
├── README.md
├── prompts/
│   ├── system_prompt.md         # System prompt documentado
│   └── few_shot_examples.md     # Ejemplos few-shot documentados
├── src/
│   ├── prompt_builder.py        # Ensambla el prompt final (sin llamar a ningún LLM)
│   └── demo.py                  # Corre 3 escenarios de ejemplo y muestra el prompt ensamblado
└── docs/
    ├── Avance1_Tutor_Academico_IA.pdf   # Informe con explicación y evidencia de ejecución
    ├── diagrama_arquitectura.png
    ├── captura_ejecucion.png
    └── salida_demo.txt          # Salida completa de consola de demo.py
```

## Cómo ejecutar el demo

No requiere ninguna API key ni conexión a internet, ya que no se llama a
ningún modelo — solo se construye y muestra el texto del prompt.

```bash
cd src
python3 demo.py
```

Esto imprime en consola el prompt final ensamblado (system prompt + few-shot
+ contexto delimitado) para 3 escenarios distintos:
1. Pregunta teórica → se espera salida en Markdown.
2. Petición de ejercicio → se espera salida en JSON.
3. Revisión de código con error → se espera salida en Markdown.

## Próximos avances (fuera de alcance actual)

- Conexión real con un LLM vía API para probar el prompt con preguntas reales.
- Incorporación de RAG: indexar el material real de la asignatura para poblar
  `<course_material>` dinámicamente en vez de pasarlo manualmente.
- Validación automática de la salida (parseo de JSON, verificación de
  estructura Markdown).

## Integrantes

- Jose Luis Patiño & Jordi Alexis Madrid
