---
title: Unification
type: concept
tags: [logic, prolog, inference]
sources: [slides-xx-logic-programming-prolog, book-russell-norvig-aima]
updated: 2026-10-07
---
# Unification (Unificación)

> **Summary (EN):** Unification answers "which values must the variables take to make these two terms identical?", or fails if that is impossible. It is two-way pattern matching: neither side is the input. Constants and numbers only match themselves; a variable matches anything and keeps that value; two compound terms match if they have the same name and number of arguments and their arguments match one by one. Prolog skips the occurs check by default, so X = f(X) builds an infinite (cyclic) term.

> **En palabras simples (ES):** Unificar es contestar: **"¿qué valores deben tomar las variables para que estas dos expresiones sean idénticas?"**. Se comparan de afuera hacia adentro, pieza por pieza. Una variable acepta cualquier valor, pero los nombres y la cantidad de argumentos tienen que coincidir. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Term | Término | Cualquier expresión: una constante (`ana`), una variable (`X`) o algo compuesto (`f(X, b)`). |
| Substitution θ | Sustitución | La lista de valores para las variables, p. ej. {X/a, Y/b} = "X vale a, Y vale b". |
| Unifier / MGU | Unificador / unificador más general | Una sustitución que iguala los dos términos; la más general es la que fija lo mínimo necesario. |
| Functor / arity | Functor / aridad | El nombre y la cantidad de argumentos: en `f(X, b)` el functor es `f` y la aridad es 2 (se escribe `f/2`). |
| Binding | Ligadura | El valor que quedó guardado en una variable. |
| Occurs check | Prueba de ocurrencia | Revisar que no le des a X un valor que contiene a X. |

## Explicación

### 1. La idea

Unificar es como resolver "llena los huecos para que las dos frases queden iguales":

`f(a, Y) = f(X, b)` → para que sean iguales, X tiene que ser `a` y Y tiene que ser `b`. Resultado: {X/a, Y/b}.

No hay un lado de "entrada" y otro de "salida": **las variables de los dos lados** pueden recibir valores. Por eso se dice que es "coincidencia de patrones en las dos direcciones".

### 2. Las reglas (slides XX, s14)

1. **Constantes y números** solo se igualan consigo mismos: `ana = ana` sí, `ana = luis` no.
2. **Una variable** se iguala con cualquier cosa y se queda con ese valor.
3. **Dos términos compuestos** se igualan si tienen **el mismo nombre** y **la misma cantidad de argumentos**, y sus argumentos se igualan uno por uno (usando los valores ya encontrados).
4. **Sin occurs check:** Prolog no revisa si X aparece dentro de su propio valor, así que `X = f(X)` crea un término infinito (`f(f(f(…)))`).

```prolog
?- f(a, Y) = f(X, b).        % X = a, Y = b.
?- [H|T] = [1, 2, 3].        % H = 1, T = [2, 3].
?- f(a) = g(a).              % false: different functors
?- X = f(X).                 % X = f(X): cyclic, no occurs check
?- unify_with_occurs_check(X, f(X)).   % false.
?- X = 3 + 4.                % X = 3+4  (a term, NOT 7) — see is/2
```

Cómo leerlo: la lista `[1, 2, 3]` se parte en cabeza `H = 1` y cola `T = [2, 3]`; `f(a)` no se iguala con `g(a)` porque los nombres son distintos; y `X = 3 + 4` guarda la **expresión** "3+4", no el número 7.

### 3. ¿Para qué sirve?

Es lo que permite usar reglas generales con variables. Para probar `criminal(west)` con la regla `criminal(X) :- …`, Prolog unifica `criminal(west)` con `criminal(X)`, obtiene {X/west}, y reemplaza X por west en las condiciones de la regla. Es como "pasar parámetros" a una función, pero en **las dos direcciones**: por eso `append(X, Y, [1,2,3])` puede **partir** una lista en todas sus formas posibles.

### 4. El unificador más general (complemento, AIMA §9.2.2)

`Knows(John, x)` y `Knows(y, z)` se pueden igualar con {y/John, x/z} o con {y/John, x/John, z/John}. La primera fija **lo mínimo necesario** (es la más general), así que es la que se prefiere: deja más opciones abiertas.

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

- `=` **no calcula**: compara estructuras. `3 + 4 = 7` da `false`. Para calcular se usa `is`.
- En Prolog, mayúscula = variable: `parent(Hector, ana)` se iguala con **cualquier** padre de ana, no solo con hector.
- Sin occurs check la unificación es más rápida, pero puede aceptar cosas que lógicamente no son correctas.

## Relacionado

- [Prolog](prolog.md)
- [Horn Clauses and Backward Chaining](horn-clauses-and-backward-chaining.md)
- [Recursion and Lists in Prolog](prolog-recursion-and-lists.md)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 14, 16.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §9.2.
