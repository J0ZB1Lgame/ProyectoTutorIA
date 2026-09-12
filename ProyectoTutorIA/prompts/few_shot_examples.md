# Few-Shot Examples — TutorIA

Estos ejemplos se insertan en el prompt (ver `FEW_SHOT_EXAMPLES` en
`src/prompt_builder.py`) para "anclar" el formato de salida antes de la
pregunta real del estudiante.

---

## Ejemplo 1 — Explicación teórica (formato Markdown)

**Entrada del estudiante:**
```
<student_question>
¿Qué es una lista en Python y en qué se diferencia de una tupla?
</student_question>
```

**Salida esperada del asistente:**
```markdown
## Definición breve
Una lista es una colección ordenada y **mutable** de elementos. Una tupla es
también ordenada, pero **inmutable**.

## Explicación detallada
Ambas estructuras permiten guardar varios valores en una sola variable y
acceder a ellos por índice. La diferencia clave está en que una lista se puede
modificar después de creada (agregar, eliminar o cambiar elementos), mientras
que una tupla, una vez creada, no puede cambiar de tamaño ni de contenido.
Esto hace que las tuplas sean más rápidas y útiles cuando quieres asegurar que
los datos no se alteren accidentalmente (por ejemplo, coordenadas fijas).

## Ejemplo en código
\`\`\`python
lista = [1, 2, 3]
lista.append(4)      # válido, las listas son mutables
lista[0] = 10         # válido

tupla = (1, 2, 3)
# tupla.append(4)     # Error: las tuplas no tienen append
# tupla[0] = 10        # Error: TypeError, no se puede modificar
\`\`\`

## Analogía
Piensa en una lista como una lista de compras escrita a lápiz: puedes borrar,
agregar o tachar cosas. Una tupla es como esa misma lista pero grabada en
piedra: una vez escrita, no cambia.
```

---

## Ejemplo 2 — Ejercicio práctico (formato JSON)

**Entrada del estudiante:**
```
<student_question>
Dame un ejercicio para practicar recursividad.
</student_question>
```

**Salida esperada del asistente:**
```json
{
  "enunciado": "Escribe una función recursiva `factorial(n)` que calcule el factorial de un número entero no negativo n.",
  "nivel_dificultad": "principiante",
  "pistas": [
    "Todo problema recursivo necesita un caso base: ¿cuál sería el factorial de 0?",
    "El caso recursivo debe reducir el problema: factorial(n) = n * factorial(n-1)"
  ],
  "solucion_codigo": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)",
  "explicacion_solucion": "La función se basa en la definición matemática del factorial: n! = n * (n-1)!. El caso base (n == 0) evita que la recursión sea infinita, devolviendo 1. Cada llamada recursiva reduce el problema en 1 hasta llegar al caso base."
}
```

---

## Ejemplo 3 — Corrección de código con error conceptual (formato Markdown)

**Entrada del estudiante:**
```
<student_code>
def es_par(n):
    if n % 2 = 0:
        return True
    else:
        return False
</student_code>
<student_question>
¿Por qué no me funciona esta función?
</student_question>
```

**Salida esperada del asistente:**
```markdown
## Definición breve
Tu función tiene un error de sintaxis: usaste `=` (asignación) en vez de `==`
(comparación).

## Explicación detallada
En Python, `=` se usa para **asignar** un valor a una variable, mientras que
`==` se usa para **comparar** si dos valores son iguales. Dentro de un `if`
siempre necesitas una expresión que devuelva `True` o `False`, y `n % 2 = 0`
no es una comparación válida, por eso Python lanza un `SyntaxError`.

## Ejemplo en código
\`\`\`python
def es_par(n):
    if n % 2 == 0:   # comparación, no asignación
        return True
    else:
        return False
\`\`\`

## Analogía
Piensa en `=` como poner una etiqueta a una caja ("esta caja se llama x") y en
`==` como preguntar "¿esta caja y esta otra tienen lo mismo adentro?". Son
acciones distintas aunque se parezcan en el símbolo.
```
