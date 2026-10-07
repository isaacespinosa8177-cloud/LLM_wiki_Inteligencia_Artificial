---
title: Recursion and Lists in Prolog
type: concept
tags: [prolog, recursion, lists, worked-example]
sources: [slides-xx-logic-programming-prolog, code-prolog-examples]
updated: 2026-10-07
---
# Recursion and Lists in Prolog (Recursión y listas en Prolog)

> **Summary (EN):** Prolog has no loops: repetition is recursion. A recursive predicate needs a base case (usually a fact) and a recursive clause that makes progress. The course examples — factorial, naive vs. accumulator Fibonacci, list membership/append/length, mutually recursive isEven/isOdd, the buggy isPerm, and a binary search tree — show the key ideas: is/2 must come after its inputs are bound, accumulators turn exponential or stack-heavy recursion into linear tail recursion, relations run "backwards", and data structures are just immutable terms.

> **En palabras simples (ES):** Prolog no tiene bucles (for, while); repite cosas con **recursión**: una regla que se usa a sí misma con un problema más pequeño. Siempre necesitas dos partes: el **caso base** (el problema más pequeño, que se responde directo) y el **caso recursivo** (achica el problema y usa la respuesta del pedazo más pequeño). Las cuentas con `is` van **después** de tener los valores. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado |
|---|---|---|
| Base case | Caso base | Cláusula que detiene la recursión. |
| Accumulator | Acumulador | Argumento extra que lleva el resultado parcial "hacia abajo". |
| Tail recursion | Recursión de cola | La llamada recursiva es la última meta: no hay que "volver". |
| List `[H\|T]` | Lista cabeza/cola | `[1,2,3]` es azúcar de `[1\|[2\|[3\|[]]]]`. |
| Memoisation / tabling | Memoización | Guardar resultados ya calculados (`:- table fibo/2.`). |

## Explicación y ejemplos

### Factorial (s17)

```prolog
factorial(0, 1).
factorial(A, B) :- A > 0, C is A - 1, factorial(C, D), B is A * D.
?- factorial(5, X).   % X = 120 ; false.
```

- El caso base es un hecho: 0! = 1. Dos cláusulas, no un if-then-else.
- `A > 0` evita que las cláusulas se solapen lógicamente (aún queda un *choicepoint*: por eso el `; false`).
- `C is A - 1` **debe ir antes** de la llamada recursiva (is/2 necesita la derecha ligada); `B is A * D` se ejecuta "a la vuelta".
- Enteros sin límite: `factorial(20, X)` funciona.
- Ejercicio de clase: ¿qué hace `?- factorial(X, 120).`? → error de instanciación en `A > 0`, porque A está libre: la aritmética de Prolog va en un solo sentido.

### Fibonacci: ingenuo vs. acumulador (s18)

```prolog
fibo(N, Y) :- N > -1, N < 2, Y is 1.                 % naive: exponential
fibo(N, Y) :- N > 1, C is N-1, D is N-2, fibo(C, A), fibo(D, B), Y is A + B.

fib(N, F) :- fib_(N, 1, 1, F).                       % accumulator: linear
fib_(0, A, _, A).
fib_(N, A, B, F) :- N > 0, N1 is N - 1, C is A + B, fib_(N1, B, C, F).
```

`time(fibo(25, _))` → 1 092 530 inferencias, porque cada llamada genera dos y los subproblemas se re-prueban. El acumulador lleva los dos valores previos hacia abajo: tiempo lineal y sin pila que deshacer. Alternativa: `:- table fibo/2.`

### Listas (s19)

```prolog
mymember(X, [X|_]).
mymember(X, [_|T]) :- mymember(X, T).

myappend([], L, L).
myappend([H|T], L, [H|R]) :- myappend(T, L, R).

mylen([], 0).
mylen([_|T], N) :- mylen(T, N0), N is N0 + 1.
```

Las relaciones corren al revés: `?- append(X, Y, [1,2,3]).` enumera las 4 formas de partir la lista. SWI ya trae `member/2`, `append/3`, `length/2`, `nth0/3`, `reverse/2`, `msort/2`, `sum_list/2`, `last/2`, `exclude/3`.

### isEven / isOdd — recursión mutua (s20)
Deciden la paridad de la **longitud** de la lista sin mirar los elementos. Los *singleton warnings* indican que `X` e `Y` deberían ser `_`. Versión idiomática — "devolver true/false es pensar en Java; aquí, **tener éxito es la respuesta**":

```prolog
even_length([]).
even_length([_|T]) :- odd_length(T).
odd_length([_|T])  :- even_length(T).
```

### isPerm — y un bug (s21)
`isPerm(X, Y) :- isInc(X, Y), isInc(Y, X).` comprueba que cada elemento de una lista esté en la otra: eso es **igualdad de conjuntos**, no permutación. `isPerm([1,1,2], [1,2,2])` da `true` (incorrecto). Arreglos: `is_perm(X, Y) :- msort(X, S), msort(Y, S).` o usar `permutation/2`.

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

Sin clases ni constructores: un árbol es el término `node(K, L, R)` y el pattern matching lo desarma. Los términos son **inmutables**: `insert/3` relaciona un árbol viejo con uno nuevo que comparte casi toda su estructura.

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

- Orden dentro del cuerpo: primero calcular (`is`), luego recursar, luego combinar.
- Recursión por la izquierda (`p :- p, …`) → bucle infinito.
- Fibonacci ingenuo es O(φⁿ); con acumulador O(n).

## Relacionado

- [Prolog](prolog.md)
- [Unification](unification.md)
- [N-Queens](n-queens.md)
- [Prolog Lab 01](../assignments/prolog-lab-01-family.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 17–22.
- [Code — Prolog examples](../sources/code-prolog-examples.md).
