---
title: Propositional and First-Order Logic
type: concept
tags: [logic, knowledge-representation]
sources: [slides-xx-logic-programming-prolog, slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-07
---
# Propositional and First-Order Logic (Lógica proposicional y de primer orden)

> **Summary (EN):** Propositional logic uses symbols that are true or false, combined with connectives; it is decidable but cannot talk about objects or say "every". First-order logic (FOL) adds constants, variables, predicates, functions and quantifiers (∀, ∃); it is far more expressive but undecidable (only semi-decidable). Every propositional sentence can be rewritten in conjunctive normal form (CNF), the input format for resolution. Horn clauses are the restricted fragment where inference stays cheap — the foundation of Prolog.

> **En palabras simples (ES):** La lógica escribe frases que son verdaderas o falsas con símbolos. Para que una computadora razone con ellas, se pasan a un formato estándar llamado **CNF**: una lista de condiciones unidas con "y", donde cada condición es un grupo de opciones unidas con "o". Se logra con 4 pasos fijos: quitar ⇔, quitar ⇒, meter la negación hacia adentro y repartir. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

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

> **Idea (ES):** La lógica escribe frases que son verdaderas o falsas con símbolos. Para que una computadora razone con ellas, se pasan a un formato estándar llamado **CNF**: una lista de condiciones unidas con "y", donde cada condición es un grupo de opciones unidas con "o". Se logra con 4 pasos fijos: quitar ⇔, quitar ⇒, meter la negación hacia adentro y repartir.

**Antes de empezar: qué significa cada cosa**

| Símbolo | Se lee | Qué significa (en simple) | English |
|---|---|---|---|
| ¬A | "no A" | lo contrario de A | not |
| A ∧ B | "A y B" | las dos son verdad | and |
| A ∨ B | "A o B" | al menos una es verdad | or |
| A ⇒ B | "si A, entonces B" | si A es verdad, B también debe serlo | implies |
| A ⇔ B | "A si y solo si B" | las dos son verdad o las dos son falsas | if and only if |
| Literal | — | un símbolo solo o negado: A, ¬B | literal |
| Cláusula | — | literales unidos con ∨: (¬A ∨ B) | clause |
| CNF | — | cláusulas unidas con ∧: (A ∨ C) ∧ (¬B ∨ C) | conjunctive normal form |
| ∀ / ∃ | "para todo" / "existe" | solo en lógica de primer orden: "todos los…" / "algún…" | for all / there exists |

**Pasos** — en inglés (como lo escribes en el examen) y debajo en español (para entender):

1. Replace A ⇔ B with (A ⇒ B) ∧ (B ⇒ A).
   - *ES:* "A si y solo si B" es lo mismo que "si A entonces B, y si B entonces A".
2. Replace A ⇒ B with ¬A ∨ B.
   - *ES:* "Si A entonces B" es lo mismo que "no A, o B" (solo es falsa cuando A es verdad y B no).
3. Move ¬ inward: ¬(A ∧ B) = ¬A ∨ ¬B; ¬(A ∨ B) = ¬A ∧ ¬B; ¬¬A = A.
   - *ES:* Mete la negación hasta los símbolos. Al entrar, el "y" se vuelve "o" y el "o" se vuelve "y" (leyes de De Morgan). Dos negaciones se cancelan.
4. Distribute ∨ over ∧: A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C).
   - *ES:* Reparte, como en álgebra a·(b + c) = a·b + a·c, pero con "o" sobre "y".
5. The result is an AND of clauses (each clause is an OR of literals).
   - *ES:* El resultado es una lista de cláusulas unidas con "y".

**Ejemplo con números:** convertir (A ⇒ B) ⇒ C.
1. Quito el ⇒ de adentro: (¬A ∨ B) ⇒ C.
2. Quito el ⇒ de afuera: ¬(¬A ∨ B) ∨ C.
3. Meto la negación: (A ∧ ¬B) ∨ C.
4. Reparto: **(A ∨ C) ∧ (¬B ∨ C)**. Son dos cláusulas: ya está en CNF.

**Say it in the exam (EN):** "Propositional logic uses true/false symbols joined by connectives; it is decidable but cannot talk about objects or say 'every'. First-order logic adds objects, predicates, functions and the quantifiers ∀ and ∃; it is much more expressive but only semi-decidable. Every sentence can be converted to CNF, an AND of clauses, by removing ⇔ and ⇒, pushing negations inward and distributing OR over AND; resolution needs CNF."

**Dilo así (ES):** "La lógica proposicional usa símbolos verdaderos o falsos unidos con conectivos; es decidible pero no habla de objetos ni puede decir 'todos'. La lógica de primer orden agrega objetos, predicados y los cuantificadores ∀ y ∃; es más expresiva pero solo semidecidible. Toda frase se puede pasar a CNF quitando ⇔ y ⇒, metiendo la negación y repartiendo el 'o' sobre el 'y'."

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
