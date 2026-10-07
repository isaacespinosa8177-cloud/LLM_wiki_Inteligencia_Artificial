---
title: Practice problems — Unit 3 (Logic and Prolog)
type: study
tags: [study, practice, logic, prolog]
sources: [slides-xx-logic-programming-prolog, code-prolog-examples, book-russell-norvig-aima]
updated: 2026-10-07
---
# Practice problems — Unit 3: Logic and Prolog (Problemas de práctica — Unidad 3)

> **Summary (EN):** Exercises on CNF conversion, Horn clauses, unification, predicting Prolog answers, arithmetic, negation as failure, the cut and writing recursive predicates. All Prolog answers were checked in SWI-Prolog with the course's `family.pl`. Questions in English, solutions in Spanish with the English answer.

## Problem 1 — CNF

Convert to CNF: (a) A ⇔ B, (b) (A ⇒ B) ⇒ C, (c) ¬(A ∧ (B ∨ C)).

> *En español:* Pasa a CNF: (a) A ⇔ B, (b) (A ⇒ B) ⇒ C, (c) ¬(A ∧ (B ∨ C)).

<details><summary>Solución</summary>

(a) (A ⇒ B) ∧ (B ⇒ A) = **(¬A ∨ B) ∧ (¬B ∨ A)**.
(b) ¬(¬A ∨ B) ∨ C = (A ∧ ¬B) ∨ C = **(A ∨ C) ∧ (¬B ∨ C)**.
(c) ¬A ∨ ¬(B ∨ C) = ¬A ∨ (¬B ∧ ¬C) = **(¬A ∨ ¬B) ∧ (¬A ∨ ¬C)**.
</details>

## Problem 2 — Horn clauses

Classify each clause as definite clause (rule), fact, goal clause, or not Horn: (a) ¬A ∨ ¬B ∨ C, (b) A ∨ B, (c) ¬A ∨ ¬B, (d) C, (e) ¬A ∨ B ∨ C. Write the Horn ones in Prolog.

> *En español:* Clasifica cada cláusula como regla (cláusula definida), hecho, pregunta (cláusula objetivo) o no-Horn: (a) ¬A ∨ ¬B ∨ C, (b) A ∨ B, (c) ¬A ∨ ¬B, (d) C, (e) ¬A ∨ B ∨ C. Escribe en Prolog las que sean de Horn.

<details><summary>Solución</summary>

(a) Cláusula definida: `c :- a, b.` (b) **No Horn** (2 positivos). (c) Cláusula objetivo: `?- a, b.` (d) Hecho: `c.` (e) **No Horn** (2 positivos: B y C).
</details>

## Problem 3 — Unification

Give the most general unifier or say "fail": (a) `p(X, f(Y)) = p(a, f(b))`, (b) `p(X, X) = p(a, b)`, (c) `f(X, g(X)) = f(Y, g(a))`, (d) `[H|T] = [a]`, (e) `[A, B] = [1, 2, 3]`, (f) `X = 2 + 3`.

> *En español:* Da el unificador más general o di "falla": (a) `p(X, f(Y)) = p(a, f(b))`, (b) `p(X, X) = p(a, b)`, (c) `f(X, g(X)) = f(Y, g(a))`, (d) `[H|T] = [a]`, (e) `[A, B] = [1, 2, 3]`, (f) `X = 2 + 3`.

<details><summary>Solución</summary>

(a) {X/a, Y/b}. (b) **Falla**: X no puede ser a y b. (c) X = Y y luego g(X) = g(a) → **{X/a, Y/a}**. (d) {H/a, T/[]}. (e) **Falla** (longitudes distintas). (f) {X/2+3} — un **término**, no 5.
</details>

## Problem 4 — Predict the answers (family.pl)

Using the lecture's `family.pl` (hector → ana, luis; ana → sofia; luis → diego), what do these return? (a) `?- parent(hector, X).` (all answers) (b) `?- findall(Z, grandparent(hector, Z), L).` (c) `?- sibling(ana, X).` (d) `?- findall(D, ancestor(hector, D), L).` (e) `?- \+ parent(sofia, _).` (f) `?- \+ parent(X, ana).`

> *En español:* Con el `family.pl` de clase (hector → ana, luis; ana → sofia; luis → diego), ¿qué responde cada consulta? (a) `?- parent(hector, X).` (todas las respuestas) (b) `?- findall(Z, grandparent(hector, Z), L).` (c) `?- sibling(ana, X).` (d) `?- findall(D, ancestor(hector, D), L).` (e) `?- \+ parent(sofia, _).` (f) `?- \+ parent(X, ana).`

<details><summary>Solución</summary>

(a) `X = ana ; X = luis.` (b) `L = [sofia, diego].` (c) `X = luis.` (d) `L = [ana, luis, sofia, diego]` (primero los hijos —primera cláusula—, luego los nietos). (e) `true` (no hay hijos registrados para sofia: mundo cerrado). (f) `false`: existe un X (hector) que es padre de ana; negar con variables sin ligar no pregunta "¿quién no es padre de ana?".
</details>

## Problem 5 — Arithmetic

What does each query print/return? (a) `X = 2 + 3.` (b) `X is 2 + 3.` (c) `2 + 3 =:= 5.` (d) `2 + 3 = 5.` (e) `X is Y + 1.` (Y unbound)

> *En español:* ¿Qué responde cada consulta? (a) `X = 2 + 3.` (b) `X is 2 + 3.` (c) `2 + 3 =:= 5.` (d) `2 + 3 = 5.` (e) `X is Y + 1.` (Y sin valor)

<details><summary>Solución</summary>

(a) `X = 2+3` (término). (b) `X = 5`. (c) `true` (compara valores). (d) `false` (estructuras distintas). (e) **Error**: *Arguments are not sufficiently instantiated* — `is` necesita la derecha ligada.
</details>

## Problem 6 — Write the rules

Using `parent/2`, `male/1`, `female/1`, write: (a) `aunt(A, N)`, (b) `last(X, List)` (last element), (c) `sum_list(List, S)`.

> *En español:* Usando `parent/2`, `male/1` y `female/1`, escribe: (a) `aunt(A, N)` (A es tía de N), (b) `last(X, List)` (último elemento de la lista), (c) `sum_list(List, S)` (suma de la lista).

<details><summary>Solución</summary>

```prolog
aunt(A, N) :- parent(P, N), parent(G, P), parent(G, A), A \= P, female(A).

last(X, [X]).
last(X, [_|T]) :- last(X, T).

sum_list([], 0).
sum_list([H|T], S) :- sum_list(T, S0), S is S0 + H.
```

Errores típicos: olvidar `A \= P` (la madre sería "tía" de su hijo), poner `S is S0 + H` **antes** de la llamada recursiva (S0 aún sin ligar).
</details>

## Problem 7 — Trace SLD resolution

Trace `?- factorial(2, X).` with `factorial(0, 1).` and `factorial(A, B) :- A > 0, C is A - 1, factorial(C, D), B is A * D.`

> *En español:* Traza paso a paso `?- factorial(2, X).` con `factorial(0, 1).` y `factorial(A, B) :- A > 0, C is A - 1, factorial(C, D), B is A * D.`

<details><summary>Solución</summary>

```text
factorial(2, X):  clause 1 fails (2 ≠ 0); clause 2: 2 > 0 ✓, C = 1, call factorial(1, D1)
  factorial(1, D1): clause 1 fails; clause 2: 1 > 0 ✓, C = 0, call factorial(0, D2)
    factorial(0, D2): clause 1 ✓ → D2 = 1   (a choice point for clause 2 remains)
  D1 is 1 * 1 = 1
X is 2 * 1 = 2      → X = 2 ;
on backtracking: factorial(0, D2) via clause 2 fails (0 > 0 is false) → false.
```

Por eso SWI muestra `X = 2 ;` y luego `false.`
</details>

## Problem 8 — The cut bug

`max(X, Y, X) :- X >= Y, !.` and `max(_, Y, Y).` What does `?- max(5, 3, 3).` return and why? Fix it.

> *En español:* Con `max(X, Y, X) :- X >= Y, !.` y `max(_, Y, Y).`, ¿qué responde `?- max(5, 3, 3).` y por qué? Arréglalo.

<details><summary>Solución</summary>

Devuelve **true** (¡incorrecto!). La primera cláusula no unifica (la cabeza pide max(5,3,5)), así que el corte nunca se ejecuta y la segunda cláusula acepta Y = 3. Arreglos: `max(X, Y, M) :- X >= Y, !, M = X.` (unificar la salida **después** del corte) o sin corte: `max(X, Y, M) :- ( X >= Y -> M = X ; M = Y ).`
</details>

## Problem 9 — Left recursion

Why does this loop, and give two fixes?
```prolog
path(X, Z) :- path(X, Y), link(Y, Z).
path(X, Z) :- link(X, Z).
```

> *En español:* ¿Por qué este programa se queda en un bucle infinito? Da dos formas de arreglarlo.

<details><summary>Solución</summary>

SLD toma la meta más a la izquierda y la primera cláusula: `path(a, c)` llama a `path(a, Y)`, que llama a `path(a, Y')`… sin consumir nada → *stack overflow*. Arreglos: (1) caso base primero y recursión **a la derecha**: `path(X, Z) :- link(X, Y), path(Y, Z).`; (2) `:- table path/2.`
</details>

## Relacionado

- [Prolog](../concepts/prolog.md) · [Unification](../concepts/unification.md) · [Horn Clauses](../concepts/horn-clauses-and-backward-chaining.md) · [Recursion and Lists](../concepts/prolog-recursion-and-lists.md)
- [Prolog Lab 01](../assignments/prolog-lab-01-family.md) · [Exam questions](exam-questions.md)
