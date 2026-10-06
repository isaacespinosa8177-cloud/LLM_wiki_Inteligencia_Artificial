---
title: Propositional and First-Order Logic
type: concept
tags: [logic, knowledge-representation]
sources: [slides-xx-logic-programming-prolog, slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-01
---
# Propositional and First-Order Logic (Lógica proposicional y de primer orden)

> **Summary (EN):** Propositional logic uses symbols that are true or false, combined with connectives; it is decidable but cannot talk about objects or say "every". First-order logic (FOL) adds constants, variables, predicates, functions and quantifiers (∀, ∃); it is far more expressive but undecidable (only semi-decidable). Every propositional sentence can be rewritten in conjunctive normal form (CNF), the input format for resolution. Horn clauses are the restricted fragment where inference stays cheap — the foundation of Prolog.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Proposition | Proposición | Enunciado que es verdadero o falso. |
| Propositional symbol | Símbolo proposicional | Representa un hecho (P, Q, *Raining*). |
| Connectives ¬ ∧ ∨ ⇒ ⇔ | Conectivos | no, y, o, implica, si y solo si. |
| Truth table | Tabla de verdad | Valor de una fórmula para cada combinación. |
| Constant / Variable / Predicate | Constante / variable / predicado | `West`, `x`, `American(x)`. |
| Quantifiers ∀ ∃ | Cuantificadores | Para todo / existe. |
| Literal | Literal | Un símbolo o su negación. |
| Clause | Cláusula | Disyunción de literales. |
| CNF | Forma normal conjuntiva | Conjunción de cláusulas. |
| Resolution | Resolución | Regla de inferencia única, *refutation-complete*. |
| Entailment ⊨ | Implicación lógica | KB ⊨ α: α es verdadera en todo modelo de KB. |
| Decidable / Semi-decidable | Decidible / semidecidible | Siempre termina / termina si la respuesta es "sí". |

## Explicación

**Escalera del curso (slides XX, s2):**

| Nivel | Qué puede decir | Costo |
|---|---|---|
| 1. Lógica proposicional | Conectivos y tablas de verdad; **no hay objetos** | Decidible, pero no puede decir "todo" |
| 2. Lógica de primer orden | Constantes, variables, predicados, cuantificadores | **Indecidible** |
| 3. Cláusulas de Horn | A lo sumo un literal positivo | Entailment barato (lineal en proposicional) |
| 4. Prolog | Horn + backward chaining + unificación | Ejecutable |

**Lógica proposicional.** Los símbolos representan hechos sobre el mundo y las oraciones complejas se construyen con conectivos. Problema: para decir "todos los humanos son mortales" necesitaríamos un símbolo por persona.

**Lógica de primer orden.** Habla de **objetos** y **relaciones**:

```
∀x,y,z  American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) ⇒ Criminal(x)
```

**CNF.** Toda oración proposicional se puede reescribir como conjunción de cláusulas, sin perder nada (es una equivalencia). ¿Para qué? La **resolución** — una sola regla de inferencia que es *refutation-complete* para lógica proposicional — necesita forma clausal. Pasos (complemento AIMA §7.5.2): eliminar ⇔ y ⇒, mover ¬ hacia adentro (De Morgan), distribuir ∨ sobre ∧.

Ejemplo: `A ∧ B ⇒ C` ≡ `¬(A ∧ B) ∨ C` ≡ `¬A ∨ ¬B ∨ C` (una cláusula).

## Pseudocódigo intuitivo (para explicar en el examen)

> **Idea (ES):** para pasar a CNF: quita ⇔ y ⇒, empuja la negación hacia adentro, y distribuye ∨ sobre ∧.

```text
CONVERT TO CNF:
1. Replace A ⇔ B with (A ⇒ B) ∧ (B ⇒ A).
2. Replace A ⇒ B with ¬A ∨ B.
3. Move ¬ inward: ¬(A ∧ B) = ¬A ∨ ¬B ; ¬(A ∨ B) = ¬A ∧ ¬B ; ¬¬A = A.
4. Distribute: A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C).
Result: a conjunction (AND) of clauses (ORs of literals).
```

**Say it in the exam (EN):** "Propositional logic is decidable but cannot talk about objects; first-order logic adds objects, predicates and quantifiers but is only semi-decidable. Every sentence has an equivalent CNF, which is what resolution needs."

## Errores comunes y tips de examen

- `P ⇒ Q` es falsa **solo** cuando P es verdadera y Q falsa.
- FOL es **semidecidible**: si KB ⊨ α, un procedimiento completo lo prueba en tiempo finito; si no, puede no terminar.
- En la notación del libro, mayúscula inicial = constante/predicado y minúscula = variable; **en Prolog es al revés** (ver [Prolog](prolog.md)).

## Relacionado

- [Horn Clauses and Backward Chaining](horn-clauses-and-backward-chaining.md)
- [Unification](unification.md)
- [Prolog](prolog.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md) (métodos formales)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 2–3, 7.
- [Slides 03](../sources/slides-03-intelligent-agents.md), slide 2 (viñetas sobre proposiciones).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 7–8 (Fig. 7.12 gramática CNF).
