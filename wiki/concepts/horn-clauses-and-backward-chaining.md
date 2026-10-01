---
title: Horn Clauses and Backward Chaining
type: concept
tags: [logic, inference, prolog]
sources: [slides-xx-logic-programming-prolog, book-russell-norvig-aima, book-luger-ai]
updated: 2026-10-01
---
# Horn Clauses and Backward Chaining (Cláusulas de Horn y encadenamiento hacia atrás)

> **Summary (EN):** A Horn clause has at most one positive literal. Definite clauses (exactly one) read as rules A ∧ B ⇒ C; facts are definite clauses with an empty body; goal clauses (no positive literal) are queries. This restriction makes knowledge bases read as implications and allows inference by chaining — forward from facts or backward from the query — with propositional entailment linear in the size of the KB. Prolog is backward chaining over first-order definite clauses, depth first and left to right.

## Términos clave

| English | Español | Significado |
|---|---|---|
| Horn clause | Cláusula de Horn | A lo sumo un literal positivo. |
| Definite clause | Cláusula definida | Exactamente un literal positivo: una **regla**. |
| Fact | Hecho | Cláusula definida sin cuerpo: `True ⇒ C`. |
| Goal clause | Cláusula objetivo | Ningún literal positivo: una **consulta**. |
| Forward chaining | Encadenamiento hacia adelante | De los hechos hacia la consulta (dirigido por datos). |
| Backward chaining | Encadenamiento hacia atrás | De la consulta hacia los hechos (dirigido por metas). |
| AND–OR graph | Grafo Y–O | Arcos unidos = conjunción; enlaces separados = alternativas. |

## Explicación

**Las tres formas (slides XX, s4):**

| Forma clausal | Como implicación | Nombre | En Prolog |
|---|---|---|---|
| `¬A ∨ ¬B ∨ C` | `A ∧ B ⇒ C` | Definite clause (regla) | `c :- a, b.` |
| `C` | `True ⇒ C` | Fact | `c.` |
| `¬A ∨ ¬B` | `A ∧ B ⇒ False` | Goal clause (consulta) | `?- a, b.` |

**No todo es Horn.** `P ∨ Q` tiene dos literales positivos: no tiene forma de Horn. Ese es el precio de la eficiencia: **Prolog no puede decir "uno de estos, no sé cuál"**.

**Por qué importan (s5):**
1. Se leen como implicaciones (`L ∧ B ⇒ M` es más claro que `¬L ∨ ¬B ∨ M`).
2. La inferencia es por encadenamiento (forward o backward).
3. El entailment es **lineal** en el tamaño de una KB proposicional de cláusulas definidas. En primer orden sigue siendo semidecidible, pero la búsqueda es mucho más barata que resolución completa.

**Backward chaining (s6).** Desde la consulta: buscar una cláusula cuya cabeza coincida, y probar recursivamente su cuerpo hasta llegar a hechos — en profundidad, de izquierda a derecha. Solo toca hechos relevantes para la consulta y el espacio es lineal en el tamaño de la prueba.

**Ejemplo — ¿Es West un criminal? (AIMA Fig. 9.7)**

```
Criminal(West)
├── American(West)                 ✓ fact
├── Weapon(y)      ← Missile(y)    ✓ Missile(M1)   {y/M1}
├── Sells(West, M1, z) ← Missile(M1) ∧ Owns(Nono, M1)   ✓ ✓   {z/Nono}
└── Hostile(Nono)  ← Enemy(Nono, America)   ✓ fact
```

**Forward vs. backward** (complemento, AIMA §9.3–9.4): forward chaining deriva todo lo derivable (útil para monitoreo, sistemas de producción); backward solo lo necesario para la meta (útil para responder preguntas, es lo que hace Prolog).

## Errores comunes y tips de examen

- Una cláusula de Horn tiene **a lo sumo** uno positivo (0 o 1), una definida **exactamente** uno.
- Backward chaining en profundidad puede entrar en bucles con reglas recursivas por la izquierda (ver [Prolog](prolog.md), SLD).

## Relacionado

- [Propositional and First-Order Logic](propositional-and-first-order-logic.md)
- [Unification](unification.md)
- [Prolog](prolog.md)
- [Uninformed Search](uninformed-search.md) (DFS)

## Fuentes

- [Slides XX](../sources/slides-xx-logic-programming-prolog.md), slides 4–7.
- [AIMA 4e](../sources/book-russell-norvig-aima.md) §7.5.3 (Fig. 7.16) y §9.4 (Fig. 9.7).
- [Luger 6e](../sources/book-luger-ai.md) §14.2.
