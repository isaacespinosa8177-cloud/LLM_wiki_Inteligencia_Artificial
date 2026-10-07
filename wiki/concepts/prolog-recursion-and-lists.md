---
title: Recursion and Lists in Prolog
type: concept
tags: [prolog, recursion, lists, worked-example]
sources: [slides-xx-logic-programming-prolog, code-prolog-examples]
updated: 2026-10-07
---
# Recursion and Lists in Prolog (Recursión y listas en Prolog)

> **Summary (EN):** Prolog has no loops, so repetition is done with recursion: a base case (usually a fact) for the smallest input, and a recursive rule that solves a smaller version of the problem. The course examples (factorial, naive vs. accumulator Fibonacci, list member/append/length, isEven/isOdd, the buggy isPerm and a binary search tree) show the key ideas: arithmetic with is/2 must come after its inputs have values, accumulators avoid repeated work, relations can run "backwards", and data structures are just terms that never change.

> **En palabras simples (ES):** Prolog no tiene bucles (for, while); repite cosas con **recursión**: una regla que se usa a sí misma con un problema más pequeño. Siempre necesitas dos partes: el **caso base** (el problema más pequeño, que se responde directo) y el **caso recursivo** (achica el problema y usa la respuesta del pedazo más pequeño). Las cuentas con `is` van **después** de tener los valores. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Recursion | Recursión | Una regla que se llama a sí misma con un problema más pequeño. |
| Base case | Caso base | El caso más pequeño, que se responde directo y detiene la recursión. |
| Accumulator | Acumulador | Un argumento extra que va llevando el resultado parcial. |
| Tail recursion | Recursión de cola | Cuando la llamada recursiva es lo último que se hace (no hay que "volver" a calcular). |
| List `[H\|T]` | Lista cabeza/cola | La lista partida en su primer elemento H y el resto T. `[1,2,3]` es `[1\|[2\|[3\|[]]]]`. |
| `[]` | Lista vacía | La lista sin elementos. |
| `_` | Variable anónima | "Aquí va algo, pero no me importa qué". |
| Memoisation / tabling | Memoización | Guardar resultados ya calculados para no repetirlos (`:- table fibo/2.`). |

## Explicación y ejemplos

### Factorial (s17)

El factorial de 5 es 5 × 4 × 3 × 2 × 1 = 120. En Prolog:

```prolog
factorial(0, 1).
factorial(A, B) :- A > 0, C is A - 1, factorial(C, D), B is A * D.
?- factorial(5, X).   % X = 120 ; false.
```

Cómo leerlo:
- **Caso base:** el factorial de 0 es 1.
- **Caso recursivo:** el factorial de A es B si A > 0, C = A − 1, el factorial de C es D, y B = A × D.

Detalles importantes:
- `C is A - 1` **va antes** de la llamada recursiva, porque `is` necesita valores para calcular. `B is A * D` se calcula "de regreso", cuando ya se conoce D.
- `A > 0` evita que la segunda regla se use con 0. Aun así, Prolog deja una opción pendiente: por eso, después de `X = 120`, si pides otra respuesta con `;` dice `false`.
- Los enteros no tienen límite: `factorial(20, X)` funciona.
- Pregunta de clase: ¿qué hace `?- factorial(X, 120).`? → da error, porque `A > 0` necesita que A tenga valor. **La aritmética de Prolog solo va en un sentido.**

### Fibonacci: ingenuo vs. con acumulador (s18)

La serie de Fibonacci es 1, 1, 2, 3, 5, 8…: cada número es la suma de los dos anteriores.

```prolog
fibo(N, Y) :- N > -1, N < 2, Y is 1.                 % naive: exponential
fibo(N, Y) :- N > 1, C is N-1, D is N-2, fibo(C, A), fibo(D, B), Y is A + B.

fib(N, F) :- fib_(N, 1, 1, F).                       % accumulator: linear
fib_(0, A, _, A).
fib_(N, A, B, F) :- N > 0, N1 is N - 1, C is A + B, fib_(N1, B, C, F).
```

- **Versión ingenua:** para calcular fibo(N) llama a fibo(N−1) **y** a fibo(N−2), y cada una vuelve a llamar a dos más. Muchos cálculos se repiten: `time(fibo(25, _))` hace **1 092 530** pasos.
- **Versión con acumulador:** lleva los dos últimos números (A y B) mientras cuenta hacia abajo, como cuando calculas a mano anotando solo los dos últimos. Solo hace N pasos (tiempo lineal).
- Otra opción: `:- table fibo/2.` hace que Prolog recuerde los resultados.

### Listas (s19)

```prolog
mymember(X, [X|_]).
mymember(X, [_|T]) :- mymember(X, T).

myappend([], L, L).
myappend([H|T], L, [H|R]) :- myappend(T, L, R).

mylen([], 0).
mylen([_|T], N) :- mylen(T, N0), N is N0 + 1.
```

Cómo leerlo:
- `mymember`: X está en la lista si es el primero, **o** si está en el resto.
- `myappend`: pegar `[]` con L da L; pegar `[H|T]` con L da H seguido de (T pegado con L).
- `mylen`: la lista vacía mide 0; una lista mide 1 más que su resto.

Las relaciones funcionan **al revés**: `?- append(X, Y, [1,2,3]).` encuentra las 4 formas de partir la lista en dos. SWI ya trae `member/2`, `append/3`, `length/2`, `nth0/3`, `reverse/2`, `msort/2`, `sum_list/2`, `last/2`, `exclude/3`.

### isEven / isOdd: dos reglas que se llaman entre sí (s20)

Deciden si una lista tiene **cantidad par o impar** de elementos, sin mirar qué elementos son. Los avisos de *singleton variable* indican que las variables `X` e `Y` deberían ser `_`. Versión más natural de Prolog ("devolver true/false es pensar como en Java; aquí, **que la pregunta tenga éxito ya es la respuesta**"):

```prolog
even_length([]).
even_length([_|T]) :- odd_length(T).
odd_length([_|T])  :- even_length(T).
```

Se lee: la lista vacía tiene largo par; una lista tiene largo par si su resto tiene largo impar, y viceversa.

### isPerm, y un error (s21)

`isPerm(X, Y) :- isInc(X, Y), isInc(Y, X).` revisa que cada elemento de una lista esté en la otra. Pero eso comprueba que tengan **los mismos elementos** (igualdad de conjuntos), no que sean una **permutación** (mismos elementos con las mismas repeticiones). `isPerm([1,1,2], [1,2,2])` da `true`, y eso está mal. Arreglos: `is_perm(X, Y) :- msort(X, S), msort(Y, S).` (ordenar las dos y comparar) o usar `permutation/2`.

### Árbol binario de búsqueda (s22)

```prolog
% tree = empty | node(Key, Left, Right)
member2(K, node(K, _, _)).
member2(K, node(N, S, _)) :- K < N, member2(K, S).
member2(K, node(N, _, T)) :- K > N, member2(K, T).
insert(N, empty, node(N, empty, empty)).
insert(N, node(K, L, R), node(K, M, R)) :- N < K, insert(N, L, M).
insert(N, node(K, L, R), node(K, L, M)) :- N > K, insert(N, R, M).
```

Cómo leerlo: un árbol es `empty` (vacío) o `node(K, L, R)` (un número K con un subárbol izquierdo L y uno derecho R). Para buscar: si K es la raíz, ya está; si es menor, busca a la izquierda; si es mayor, a la derecha. Para insertar se hace lo mismo hasta encontrar un lugar vacío.

No hay clases ni constructores: un árbol es solo el término `node(K, L, R)`, y la unificación lo "desarma". Los términos **no cambian nunca**: `insert/3` relaciona el árbol viejo con uno nuevo que comparte casi todas sus partes.

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Prolog no tiene bucles (for, while); repite cosas con **recursión**: una regla que se usa a sí misma con un problema más pequeño. Siempre necesitas dos partes: el **caso base** (el problema más pequeño, que se responde directo) y el **caso recursivo** (achica el problema y usa la respuesta del pedazo más pequeño). Las cuentas con `is` van **después** de tener los valores.

**Antes de empezar: qué significa cada cosa**

| Símbolo / palabra | Qué es (en simple) | English |
|---|---|---|
| Caso base | la versión más pequeña, con respuesta directa: `len([], 0).` ("la lista vacía mide 0") | base case |
| Caso recursivo | la regla que se llama a sí misma con algo más pequeño | recursive case |
| [H\|T] | una lista partida en su primer elemento H (cabeza) y el resto T (cola) | head and tail |
| [] | la lista vacía | empty list |
| `is` | calcula una operación: `N is N0 + 1` | arithmetic evaluation |
| `_` | "cualquier cosa, no me importa" | anonymous variable |
| Acumulador | un argumento extra que lleva el resultado parcial mientras avanzas | accumulator |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Base case: write the answer for the smallest input as a fact (len([], 0). or factorial(0, 1).).
   - *ES:* Escribe la respuesta del caso más pequeño como un hecho.
2. Recursive case: split the input into a smaller part (N − 1, or the tail T of [H|T]).
   - *ES:* Achica el problema: quita un elemento o resta 1.
3. Call the same predicate on the smaller part.
   - *ES:* Pide la respuesta del problema más pequeño.
4. Build the answer from it with `is`, only after the values are known.
   - *ES:* Con esa respuesta calcula la tuya. El `is` va después de la llamada, porque antes los valores todavía no existen.
5. Optional: add an accumulator to carry the partial result (makes it faster, e.g., linear Fibonacci).
   - *ES:* Opcional: lleva el resultado parcial en un argumento extra para no repetir cálculos.

**Ejemplo con números:** el largo de una lista:
```prolog
len([], 0).
len([_|T], N) :- len(T, N0), N is N0 + 1.
```
`?- len([a, b], N).` → necesita `len([b], N0)` → necesita `len([], N0')` = **0** (caso base) → entonces `len([b])` = 0 + 1 = **1** → entonces `len([a, b])` = 1 + 1 = **2**.

**Say it in the exam (EN):** "Prolog has no loops, so repetition is recursion: a base case written as a fact and a recursive rule that works on a smaller input. Lists are split into [Head|Tail]. Arithmetic with 'is' must come after its inputs are known. An accumulator carries the partial result and avoids repeating work, which turns the exponential naive Fibonacci into a linear one."

**Dilo así (ES):** "Prolog no tiene bucles; repite con recursión: un caso base escrito como hecho y una regla recursiva que trabaja con algo más pequeño. Las listas se separan en [Cabeza|Cola]. El 'is' debe ir después de tener los valores. Un acumulador lleva el resultado parcial y evita repetir trabajo, por ejemplo en Fibonacci."

## Errores comunes y tips de examen

- Orden dentro de una regla: primero calcular con `is` lo que se necesita, luego la llamada recursiva, luego combinar el resultado.
- Recursión por la izquierda (`p :- p, …`) → bucle infinito.
- Fibonacci ingenuo crece exponencialmente (O(φⁿ), φ ≈ 1.618); con acumulador es O(n).

## Relacionado

- [Prolog](prolog.md)
- [Unification](unification.md)
- [N-Queens](n-queens.md)
- [Prolog Lab 01](../assignments/prolog-lab-01-family.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 17–22.
- [Code — Prolog examples](../sources/code-prolog-examples.md).
