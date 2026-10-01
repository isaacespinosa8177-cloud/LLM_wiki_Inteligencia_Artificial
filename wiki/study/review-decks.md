---
title: Review slide decks (one per unit)
type: study
tags: [study, slides, review, exam]
sources: [slides-01-introduction-to-ai, slides-02-problem-solving, slides-03-intelligent-agents, slides-04-optimization, slides-xx-logic-programming-prolog, book-russell-norvig-aima, book-eiben-smith-evolutionary-computing]
updated: 2026-10-01
---
# Review slide decks (Presentaciones de repaso)

> **Summary (EN):** Four short review decks (12–15 slides each), one per unit, condensed from this wiki for the test on Thursday, October 8. Slide text is in English (the exam language), with "ES:" tips in Spanish. Each deck ends with six self-check questions to answer aloud; the full solutions are on the practice pages. The PDFs open directly on GitHub or a phone.

## Las presentaciones

| Unidad | PDF (para leer) | Fuente Marp (para editar) | Diapositivas |
|---|---|---|---|
| 1 — Foundations & Agents | [unit-1-agents.pdf](../../study-tools/slides/pdf/unit-1-agents.pdf) | [unit-1-agents.md](../../study-tools/slides/unit-1-agents.md) | 13 |
| 2 — Search, Games & CSP | [unit-2-search.pdf](../../study-tools/slides/pdf/unit-2-search.pdf) | [unit-2-search.md](../../study-tools/slides/unit-2-search.md) | 15 |
| 3 — Logic & Prolog | [unit-3-logic.pdf](../../study-tools/slides/pdf/unit-3-logic.pdf) | [unit-3-logic.md](../../study-tools/slides/unit-3-logic.md) | 13 |
| 4 — Optimization & Metaheuristics | [unit-4-optimization.pdf](../../study-tools/slides/pdf/unit-4-optimization.pdf) | [unit-4-optimization.md](../../study-tools/slides/unit-4-optimization.md) | 13 |

## Cómo usarlas

- **La noche antes de cada día del [plan de estudio](study-plan.md):** repasa la presentación de la unidad del día siguiente (10 minutos) para llegar con el mapa mental listo.
- **Miércoles 7 (simulacro):** repasa las cuatro presentaciones seguidas y responde en voz alta, en inglés, las preguntas de la última diapositiva de cada una. Si fallas alguna, vuelve a la página de práctica: [U1](practice-unit-1-agents.md) · [U2](practice-unit-2-search.md) · [U3](practice-unit-3-logic.md) · [U4](practice-unit-4-optimization.md).
- Los recuadros naranjas "ES:" marcan trampas de examen y erratas de las slides (ver [Errata](errata.md)).

## Cómo regenerarlas

Las fuentes están en formato [Marp](https://marp.app) con el tema `study-tools/slides/ia-review.css`. Después de editar un `.md`:

```bash
npx @marp-team/marp-cli --theme-set study-tools/slides/ia-review.css --pdf \
    study-tools/slides/unit-2-search.md -o study-tools/slides/pdf/unit-2-search.pdf
```

(En VS Code, la extensión *Marp for VS Code* muestra la vista previa; hay que registrar el tema en `markdown.marp.themes`.)

## Relacionado

- [Study plan](study-plan.md) · [Interactive tools](interactive-tools.md) · [Flashcards](flashcards.md)
- [Search algorithms comparison](search-algorithms-comparison.md) · [Metaheuristics comparison](metaheuristics-comparison.md) · [Intuitive pseudocode](intuitive-pseudocode.md)

## Fuentes

Todo el contenido se condensó de las páginas de la wiki, que citan las fuentes originales: [Slides 01](../sources/slides-01-introduction-to-ai.md), [Slides 02](../sources/slides-02-problem-solving.md), [Slides 03](../sources/slides-03-intelligent-agents.md), [Slides 04](../sources/slides-04-optimization.md), [Slides XX](../sources/slides-xx-logic-programming-prolog.md), [AIMA 4e](../sources/book-russell-norvig-aima.md) cap. 2–6 y [Eiben & Smith](../sources/book-eiben-smith-evolutionary-computing.md) cap. 3–5. "Algorithm = Logic + Control" es de Kowalski (1979, conocimiento general).
