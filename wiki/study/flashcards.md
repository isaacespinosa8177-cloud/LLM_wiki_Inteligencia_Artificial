---
title: Flashcards (Anki deck)
type: study
tags: [study, flashcards, anki, spaced-repetition]
sources: [book-russell-norvig-aima, slides-02-problem-solving, slides-04-optimization, slides-xx-logic-programming-prolog]
updated: 2026-10-01
---
# Flashcards — Anki deck (Tarjetas de estudio)

> **Summary (EN):** An Anki deck generated from the wiki: every glossary term, every exam question, every practice problem and every intuitive-pseudocode section, tagged by unit. It is rebuilt by `python3 tools/build_study.py`, so new wiki content becomes new cards automatically. Anki's spaced repetition shows you each card right before you would forget it — 15 minutes a day is enough.

## El archivo

[`study-tools/anki/ia-wiki-flashcards.txt`](../../study-tools/anki/ia-wiki-flashcards.txt) — texto separado por tabuladores con HTML, mazo **"Inteligencia Artificial (LLM Wiki)"**, tipo de nota *Basic*.

| Tag | Qué contiene |
|---|---|
| `glossary` | Término en inglés → término en español + explicación |
| `unit1-agents` … `unit4-optimization` | Preguntas de examen y problemas de práctica de cada unidad |
| `practice` | Problemas con solución completa |
| `pseudocode` | "Write the intuitive pseudocode for X" → pasos en inglés + respuesta de examen |
| `quiz` | Preguntas de opción múltiple del [quiz bank](quiz-bank.md) (las mismas del [Exam Drill](interactive-tools.md)) |

## Cómo importarlo

1. Instala **Anki** (escritorio, gratis: apps.ankiweb.net) o **AnkiDroid** (Android, gratis). En iPhone, AnkiMobile es de pago; alternativa: importar en el escritorio y sincronizar con AnkiWeb.
2. Descarga el archivo desde GitHub (botón *Download raw file*).
3. En Anki: **File → Import…** → elige el archivo. Las líneas de cabecera (`#separator:tab`, `#html:true`, `#deck:…`, `#tags column:3`) configuran todo solas; confirma **Import**.
4. Para estudiar una sola unidad: *Browse* → busca `tag:unit2-search` → *Create filtered deck*.
5. Cuando la wiki crezca, reimporta el archivo: Anki actualiza las tarjetas existentes (misma pregunta) y agrega las nuevas.

## Rutina sugerida hasta el test (8 de octubre)

- Todos los días: tarjetas vencidas + 20 nuevas.
- Prioridad: `pseudocode` y `practice` de la unidad del día en el [plan de estudio](study-plan.md).
- La noche anterior: solo repasar, sin tarjetas nuevas.

## Relacionado

- [Study plan](study-plan.md) · [Exam questions](exam-questions.md) · [Intuitive pseudocode](intuitive-pseudocode.md) · [Glossary](../glossary.md)
