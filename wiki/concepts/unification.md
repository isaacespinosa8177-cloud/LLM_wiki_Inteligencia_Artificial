---
title: Unification
type: concept
tags: [logic, prolog, inference]
sources: [slides-xx-logic-programming-prolog, book-russell-norvig-aima]
updated: 2026-10-07
---
# Unification (Unificación)

> **Summary (EN):** Unification finds a substitution that makes two terms identical, or fails. It is two-way pattern matching: neither side is the input. Atoms and numbers unify only with themselves; a variable unifies with anything and stays bound; compound terms unify if functor and arity match and their arguments unify pairwise. Prolog omits the occurs check by default, so X = f(X) builds a cyclic term.

> **En palabras simples (ES):** Unificar es contestar: **"¿qué valores deben tomar las variables para que estas dos expresiones sean idénticas?"**. Se comparan de afuera hacia adentro, pieza por pieza. Una variable acepta cualquier valor, pero los nombres y la cantidad de argumentos tienen que coincidir. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

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

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** Unificar es contestar: **"¿qué valores deben tomar las variables para que estas dos expresiones sean idénticas?"**. Se comparan de afuera hacia adentro, pieza por pieza. Una variable acepta cualquier valor, pero los nombres y la cantidad de argumentos tienen que coincidir.

**Antes de empezar: qué significa cada cosa**

| Palabra / símbolo | Qué es (en simple) | English |
|---|---|---|
| Variable | empieza con mayúscula en Prolog (X, Y): "un hueco" que se llena | variable |
| Constante (átomo) | empieza con minúscula (ana, a): un valor fijo | constant (atom) |
| Término compuesto | un nombre con argumentos: f(X, b), parent(ana, sofia) | compound term |
| Aridad | cuántos argumentos tiene: f(X, b) tiene 2 | arity |
| Sustitución {X/a} | "X vale a" | substitution |
| `=` | en Prolog significa "unifica", no "calcula" | unify |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. If A and B are identical → success, nothing to bind.
   - *ES:* Si ya son iguales, listo.
2. If one of them is a variable → bind it to the other (X = whatever is on the other side).
   - *ES:* Si uno es una variable, dale el valor del otro.
3. If both are compound terms with the SAME name and the SAME number of arguments → unify the arguments one by one, using the bindings found so far.
   - *ES:* Si los dos son "nombre(argumentos)" con el mismo nombre y la misma cantidad, compara argumento por argumento, usando lo que ya descubriste.
4. Otherwise → fail.
   - *ES:* En cualquier otro caso, no se puede (falla).
5. (Occurs check) Never bind X to a term that contains X itself.
   - *ES:* No le des a X un valor que contenga a X, como X = f(X). Prolog no revisa esto por defecto.

**Ejemplo con números:** unificar f(X, g(X)) con f(Y, g(a)).
1. Mismo nombre f, 2 argumentos ✓.
2. Primer argumento: X con Y → X = Y.
3. Segundo argumento: g(X) con g(a) → mismo nombre g → X = a.
4. Resultado: **{X/a, Y/a}**.
Otro ejemplo: p(X, X) con p(a, b) → X = a y luego X = b → **falla**: X no puede valer a y b a la vez.

**Say it in the exam (EN):** "Unification finds a substitution that makes two terms identical, or fails. A variable can take any value; constants only match themselves; compound terms match if they have the same name and number of arguments and their arguments unify one by one. For example, f(a, Y) and f(X, b) unify with {X/a, Y/b}. In Prolog '=' unifies without calculating: X = 2 + 3 gives the term 2+3, while X is 2 + 3 gives 5."

**Dilo así (ES):** "Unificar es encontrar valores para las variables que hagan idénticos dos términos, o fallar. Una variable acepta cualquier valor; una constante solo se iguala consigo misma; dos términos compuestos se unifican si tienen el mismo nombre y número de argumentos y sus argumentos se unifican uno por uno. En Prolog '=' unifica sin calcular; para calcular se usa 'is'."

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
