"""
demo.py
-------
Demuestra la construcción del prompt para 3 escenarios distintos del
Tutor Académico (Programación en Python). No hace ninguna llamada a un LLM:
solo imprime el prompt final que se le enviaría a un modelo en un avance
posterior del proyecto.

Uso:
    python src/demo.py
"""

from prompt_builder import build_prompt

ESCENARIOS = [
    {
        "titulo": "Escenario 1: Pregunta teórica -> se espera salida en Markdown",
        "course_material": (
            "Unidad 2 - Estructuras de datos en Python. Las listas son "
            "mutables y las tuplas son inmutables. Ambas son secuencias "
            "ordenadas indexables desde 0."
        ),
        "student_question": "¿Cuándo debería usar una tupla en vez de una lista?",
        "student_code": "",
    },
    {
        "titulo": "Escenario 2: Petición de ejercicio -> se espera salida en JSON",
        "course_material": (
            "Unidad 5 - Recursividad. Toda función recursiva necesita un "
            "caso base y un caso recursivo que reduzca el problema."
        ),
        "student_question": "Ponme un ejercicio de recursividad de nivel intermedio.",
        "student_code": "",
    },
    {
        "titulo": "Escenario 3: Revisión de código con error -> se espera salida en Markdown",
        "course_material": (
            "Unidad 3 - Condicionales y operadores de comparación en Python "
            "(==, !=, <, >, <=, >=)."
        ),
        "student_question": "¿Por qué no me funciona esta función?",
        "student_code": "def es_par(n):\n    if n % 2 = 0:\n        return True\n    return False",
    },
]


def main():
    for i, escenario in enumerate(ESCENARIOS, start=1):
        print("=" * 80)
        print(escenario["titulo"])
        print("=" * 80)
        prompt = build_prompt(
            course_material=escenario["course_material"],
            student_question=escenario["student_question"],
            student_code=escenario["student_code"],
        )
        print(prompt)
        print("\n")


if __name__ == "__main__":
    main()
