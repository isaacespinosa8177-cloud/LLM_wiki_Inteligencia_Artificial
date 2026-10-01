---
title: Unification
type: concept
tags: [logic, prolog, inference]
sources: [slides-xx-logic-programming-prolog, book-russell-norvig-aima]
updated: 2026-10-01
---
# Unification (Unificación)

> **Summary (EN):** Unification finds a substitution that makes two terms identical, or fails. It is two-way pattern matching: neither side is the input. Atoms and numbers unify only with themselves; a variable unifies with anything and stays bound; compound terms unify if functor and arity match and their arguments unify pairwise. Prolog omits the occurs check by default, so X = f(X) builds a cyclic term.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Substitution θ | Sustitución | Conjunto de ligaduras variable/valor, p. ej. {X/a, Y/b}. |
| Unifier / MGU | Unificador / unificador más general | Sustitución que iguala los términos; la MGU es la menos restrictiva. |
| Functor / arity | Functor / aridad | Nombre y número de argumentos: `f/2`. |
| Occurs check | Prueba de ocurrencia | Impedir ligar X a un término que contiene X. |
| Binding | Ligadura | Valor asignado a una variable. |

## Explicación

**Reglas (slides XX, s14):**
1. Átomos y números unifican solo consigo mismos.
2. Una variable unifica con cualquier cosa y queda ligada.
3. Términos compuestos unifican si coinciden functor y aridad, y los argumentos unifican uno a uno.
4. Sin *occurs check*: `X = f(X)` crea un término cíclico.

```prolog
?- f(a, Y) = f(X, b).        % X = a, Y = b.
?- [H|T] = [1, 2, 3].        % H = 1, T = [2, 3].
?- f(a) = g(a).              % false: different functors
?- X = f(X).                 % X = f(X): cyclic, no occurs check
?- unify_with_occurs_check(X, f(X)).   % false.
?- X = 3 + 4.                % X = 3+4  (a term, NOT 7) — see is/2
```

**Por qué importa.** La unificación es lo que permite usar reglas generales con variables: para probar `criminal(west)` con la regla `criminal(X) :- …`, se unifica `criminal(west)` con `criminal(X)` → θ = {X/west}, y se aplica θ al cuerpo. Es el mecanismo de "paso de parámetros" de Prolog, pero **bidireccional**: por eso `append(X, Y, [1,2,3])` puede *partir* una lista.

**Unificador más general (complemento, AIMA §9.2.2).** `Knows(John, x)` y `Knows(y, z)` unifican con {y/John, x/z} (MGU) o con {y/John, x/John, z/John} (más específico). Se prefiere la MGU.

## Errores comunes y tips de examen

- `=` **no evalúa** aritmética: unifica estructuras. `3 + 4 = 7` es `false`.
- Mayúscula en Prolog = variable: `parent(Hector, ana)` unifica con *cualquier* padre de ana.
- Sin occurs check la unificación es más rápida pero puede ser lógicamente incorrecta (*unsound*).

## Relacionado

- [Prolog](prolog.md)
- [Horn Clauses and Backward Chaining](horn-clauses-and-backward-chaining.md)
- [Recursion and Lists in Prolog](prolog-recursion-and-lists.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 14, 16.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §9.2.
