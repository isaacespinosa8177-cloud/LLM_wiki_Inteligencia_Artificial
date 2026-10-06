---
title: "Prolog Lab 01 — Family knowledge base"
type: assignment
tags: [assignment, prolog, logic, plunit]
sources: [slides-xx-logic-programming-prolog, code-prolog-examples]
updated: 2026-10-01
---
# Prolog Lab 01 — Family knowledge base (Base de conocimiento familiar)

> **Summary (EN):** Build a family knowledge base in Prolog (≥16 people, four generations, spouse/2), write at least eight relationship rules plus a new recursive rule, prove them with ≥20 plunit tests (≥6 negative), and write a short analysis. Isaac's submission has 18 people over four generations, 10 rules including a recursive descendant/2, and 24 tests that all pass in SWI-Prolog. Review points: 15 "succeeded with choicepoint" warnings, an asymmetric spouse/2 that breaks father_in_law/2 in one direction, duplicate answers, and the optional related/2 bonus not attempted.

## Ficha

| Campo | Valor |
|---|---|
| Entrega | [raw/assignments/Espinosa_Isaac_lab01.pl](../../raw/assignments/Espinosa_Isaac_lab01.pl) |
| Borrador anterior | [raw/assignments/lab01.pl~](../../raw/assignments/lab01.pl~) (sin `use_module(plunit)`, una prueba distinta) |
| Base | [family.pl](../../raw/code/prolog_examples/family.pl) |
| Enunciado | [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 29–30 |
| ⚠️ Política de IA | Permitido un asistente de IA declarándolo en un comentario de cabecera con lo que cambiaste (slide 30). Revisión añadida tras la entrega (2026-10-01). |

## Enunciado (slides 29–30)

1. **Base de conocimiento (20 pts):** ≥ 16 personas en cuatro generaciones, nuevo `spouse/2`, ambos padres de cada hijo, una pareja con ≥ 3 hijos y alguien sin hijos.
2. **Relaciones (35 pts):** ≥ 8 reglas — `mother/2`, `sister/2`, `grandmother/2`, `uncle/2`, `cousin/2`, `father_in_law/2` — y una regla recursiva propia distinta de `ancestor/2`.
3. **Evidencia (25 pts):** ≥ 20 pruebas plunit, 6 negativas, una que muestre que nadie es su propio hermano; `?- run_tests.` debe pasar.
4. **Análisis (20 pts):** ¿Por qué `sibling/2` necesita `X \= Y`? ¿Qué reglas devuelven la misma respuesta dos veces y por qué? ¿Qué afirma el supuesto de mundo cerrado que nunca escribiste?
5. **Bonus (+10):** `related(X, Y)` por cualquier cadena padre/hijo/matrimonio, que termine.
- Entregables: `apellido_nombre_lab01.pl` + PDF (≤ 2 páginas). Debe cargar con `swipl -g true -t halt archivo.pl`; errores y *singleton warnings* restan puntos. Declarar uso de asistentes de IA.

## Qué se implementó

- **18 personas**, 4 generaciones (bayardo/margarita → mauricio → isaac → valeria), 4 parejas en `spouse/2`; marcelo+alicia y paulina+giovanni tienen 3 hijos cada una; varias personas sin hijos. ✅
- **10 reglas:** `mother`, `father`, `sibling`, `sister`, `brother`, `grandmother`, `uncle`, `cousin`, `father_in_law`, y la recursiva **`descendant/2`**. ✅
- **24 pruebas**, 6 negativas (con `\+`), incluida `nobody_is_their_own_sibling`. ✅

## Resultados (SWI-Prolog 9.0.4, 2026-10-01)

```
$ swipl -g true -t halt Espinosa_Isaac_lab01.pl
% All 24 tests passed        (+ 15 "Test succeeded with choicepoint" warnings)
```

Consultas de verificación:

| Consulta | Resultado | Comentario |
|---|---|---|
| `father_in_law(bayardo, marisol)` | true | ✅ |
| `father_in_law(marcelo, mauricio)` | **false** | ❌ debería ser true (marcelo es padre de marisol, esposa de mauricio) |
| `findall(X, sibling(isaac, X), L)` | `[elias, elias]` | duplicado: una vez por cada padre |
| `findall(U, uncle(U, isaac), L)` | `[vladimir, vladimir]` | duplicado; falta giovanni (tío político) |
| `findall(X-Y, cousin(X, Y), L)` | 52 respuestas, 22 distintas | cada par aparece hasta 4 veces |

## Revisión

**Fortalezas**
- Cumple todos los mínimos cuantitativos; carga sin errores ni *singleton warnings*; todas las pruebas pasan.
- Buena regla recursiva propia (`descendant/2`) y pruebas negativas bien elegidas.

**Puntos a mejorar**
1. **`spouse/2` no es simétrico.** Solo está `spouse(marisol, mauricio)`, así que `father_in_law` funciona para marisol pero no para mauricio. Arreglo:
   ```prolog
   married(X, Y) :- spouse(X, Y) ; spouse(Y, X).
   father_in_law(F, P) :- married(P, S), parent(F, S), male(F).
   ```
2. **15 avisos "succeeded with choicepoint".** La regla del enunciado es que cargue limpio. Igual que el ejemplo de la slide (`mother(rosa, ana), !.`), terminar las pruebas positivas con `!` o declarar `[nondet]`:
   ```prolog
   test(mother_marisol) :- mother(marisol, isaac), !.
   test(cousin_ismael_jude, [nondet]) :- cousin(ismael, jude).
   ```
3. **Prueba de "nadie es su propio hermano":** solo prueba a isaac. La versión general de la slide es `test(no_self_sibling, [fail]) :- sibling(X, X).`
4. **Hechos sueltos `bayardo.` … `valeria.`** al inicio definen 18 predicados de aridad 0 sin uso; probablemente se quería `person(bayardo).`
5. **`uncle/2` solo cubre tíos de sangre** (no por matrimonio); se puede añadir una segunda cláusula con `married/2`.
6. **Bonus `related/2` no implementado.** Pista: recorrer el grafo padre/hijo/cónyuge guardando una lista de visitados (o `:- table related/2.`) para que termine.
7. Nota: el comentario de `family.pl` dice "keep these facts and build on them", mientras la slide 30 dice "invent your own family"; la entrega inventó una familia nueva, lo cual es coherente con la slide 30.

**Respuestas para la parte de análisis (para estudiar)**
- *¿Por qué `X \= Y` en sibling?* Sin él, `sibling(isaac, isaac)` sería verdadero: isaac comparte padre consigo mismo.
- *¿Qué reglas repiten respuestas?* sibling, sister, brother, uncle, cousin: hay un camino de prueba por **cada padre en común** (madre y padre), y cousin multiplica por los dos abuelos. Se evita con `setof/3` o fijando un solo progenitor.
- *Mundo cerrado:* todo lo no derivable es falso — p. ej. que nadie más tiene hijos, que no hay otros matrimonios, que `\+ mother(mauricio, isaac)` porque no hay hecho `female(mauricio)`.

## Conceptos relacionados

- [Prolog](../concepts/prolog.md)
- [Recursion and Lists in Prolog](../concepts/prolog-recursion-and-lists.md)
- [Horn Clauses and Backward Chaining](../concepts/horn-clauses-and-backward-chaining.md)
- [Unification](../concepts/unification.md)
