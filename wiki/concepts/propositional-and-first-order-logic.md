---
title: Propositional and First-Order Logic
type: concept
tags: [logic, knowledge-representation]
sources: [slides-xx-logic-programming-prolog, slides-03-intelligent-agents, book-russell-norvig-aima]
updated: 2026-10-07
---
# Propositional and First-Order Logic (Lógica proposicional y de primer orden)

> **Summary (EN):** Propositional logic uses symbols that are true or false (like "it is raining") joined with connectives such as and, or, not, implies; it is decidable but cannot talk about objects or say "every". First-order logic (FOL) adds objects, variables, predicates, functions and the quantifiers "for all" (∀) and "there exists" (∃); it can say much more but is only semi-decidable. Every propositional sentence can be rewritten in conjunctive normal form (CNF), the format resolution needs. Horn clauses are a restricted form where reasoning stays cheap; they are the basis of Prolog.

> **En palabras simples (ES):** La lógica escribe frases que son verdaderas o falsas con símbolos. Para que una computadora razone con ellas, se pasan a un formato estándar llamado **CNF**: una lista de condiciones unidas con "y", donde cada condición es un grupo de opciones unidas con "o". Se logra con 4 pasos fijos: quitar ⇔, quitar ⇒, meter la negación hacia adentro y repartir. *(Abajo está el pseudocódigo paso a paso, en inglés y en español.)*

## Términos clave

| English | Español | Significado (en simple) |
|---|---|---|
| Proposition | Proposición | Una frase que es verdadera o falsa ("está lloviendo"). |
| Propositional symbol | Símbolo proposicional | Una letra que representa esa frase: P, Q, *Raining*. |
| ¬ ∧ ∨ ⇒ ⇔ | Conectivos | no · y · o · si… entonces · si y solo si. |
| Truth table | Tabla de verdad | Tabla con el resultado de una fórmula para cada combinación de verdadero/falso. |
| Constant | Constante | Un objeto concreto: `West`, `ana`. |
| Variable | Variable | Un "hueco" que puede ser cualquier objeto: x, y. |
| Predicate | Predicado | Una propiedad o relación: `American(x)` = "x es estadounidense". |
| ∀ / ∃ | Cuantificadores | "Para todo x…" / "existe algún x…". |
| Literal | Literal | Un símbolo solo o negado: A, ¬B. |
| Clause | Cláusula | Literales unidos con "o": (¬A ∨ B). |
| CNF | Forma normal conjuntiva | Cláusulas unidas con "y": (A ∨ C) ∧ (¬B ∨ C). |
| Resolution | Resolución | Una única regla de razonamiento que, usando CNF, sirve para demostrar cosas. |
| Entailment ⊨ | Consecuencia lógica | KB ⊨ α: "si todo lo que sé (KB) es verdad, α también lo es". |
| Decidable / semi-decidable | Decidible / semidecidible | Siempre da respuesta / da respuesta si es "sí", pero si es "no" puede no terminar nunca. |

## Explicación

### 1. La escalera del curso (slides XX, s2)

El curso sube por cuatro niveles; cada uno dice más cosas, pero cuesta distinto:

| Nivel | Qué puede decir | Costo |
|---|---|---|
| 1. Lógica proposicional | Frases verdaderas/falsas unidas con conectivos; **no habla de objetos** | Siempre da respuesta, pero no puede decir "todos" |
| 2. Lógica de primer orden | Objetos, variables, relaciones, "todos" y "existe" | Puede no terminar (**indecidible**) |
| 3. Cláusulas de Horn | Solo reglas "si… y… entonces…" y hechos | Razonar es barato |
| 4. Prolog | Horn + razonar hacia atrás + unificación | Se puede ejecutar como programa |

### 2. Lógica proposicional

Cada símbolo representa un hecho ("llueve", "hace frío") y se combinan con conectivos. Cómo se lee cada uno:

| Fórmula | Se lee | Es verdadera cuando… |
|---|---|---|
| ¬A | no A | A es falsa |
| A ∧ B | A y B | las dos son verdaderas |
| A ∨ B | A o B | al menos una es verdadera |
| A ⇒ B | si A, entonces B | **siempre, excepto** cuando A es verdadera y B falsa |
| A ⇔ B | A si y solo si B | las dos tienen el mismo valor |

**Su límite:** para decir "todos los humanos son mortales" necesitarías un símbolo por cada persona ("Ana es mortal", "Luis es mortal"…).

### 3. Lógica de primer orden (FOL)

Habla de **objetos** y de **relaciones** entre ellos, y puede decir "para todos" (∀) y "existe" (∃). Ejemplo del libro:

```
∀x,y,z  American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) ⇒ Criminal(x)
```

Se lee: "para cualquier x, y, z: si x es estadounidense, y es un arma, x le vende y a z, y z es hostil, entonces x es criminal".

### 4. CNF: el formato estándar

Toda frase proposicional se puede reescribir como **cláusulas unidas con "y"**, sin cambiar su significado. ¿Para qué? Porque la **resolución**, una sola regla de razonamiento que sirve para demostrar cualquier consecuencia (es *refutation-complete*), necesita las frases en ese formato.

Pasos (complemento AIMA §7.5.2):
1. Quitar ⇔: A ⇔ B → (A ⇒ B) ∧ (B ⇒ A).
2. Quitar ⇒: A ⇒ B → ¬A ∨ B.
3. Meter la negación hacia adentro (leyes de De Morgan): ¬(A ∧ B) → ¬A ∨ ¬B; ¬(A ∨ B) → ¬A ∧ ¬B; ¬¬A → A.
4. Repartir el "o" sobre el "y": A ∨ (B ∧ C) → (A ∨ B) ∧ (A ∨ C).

Ejemplo: `A ∧ B ⇒ C` → `¬(A ∧ B) ∨ C` → `¬A ∨ ¬B ∨ C`. Queda **una sola cláusula**: "no A, o no B, o C".

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

- `P ⇒ Q` es falsa **solo** cuando P es verdadera y Q es falsa. Si P es falsa, `P ⇒ Q` es verdadera ("si llueve, llevo paraguas" no se rompe en un día sin lluvia).
- FOL es **semidecidible**: si algo sí se deduce de lo que sabes, un método completo lo demuestra en tiempo finito; si no se deduce, puede quedarse buscando para siempre.
- En el libro, mayúscula inicial = constante o predicado y minúscula = variable; **en Prolog es al revés** (ver [Prolog](prolog.md)).

## Relacionado

- [Horn Clauses and Backward Chaining](horn-clauses-and-backward-chaining.md)
- [Unification](unification.md)
- [Prolog](prolog.md)
- [Statistical vs. Causal Models](statistical-vs-causal-models.md) (métodos formales)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 2–3, 7.
- [Slides 03](../sources/slides-03-intelligent-agents.md), slide 2 (viñetas sobre proposiciones).
- [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 7–8 (Fig. 7.12 gramática CNF).
