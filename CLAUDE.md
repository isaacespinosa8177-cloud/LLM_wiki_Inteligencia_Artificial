# CLAUDE.md — Schema for the "Inteligencia Artificial" LLM Wiki

This repository is a **personal study wiki** for a university course on Artificial
Intelligence (Universidad San Francisco de Quito, instructor Daniel Riofrío). It follows
Andrej Karpathy's *LLM Wiki* pattern ([docs/llm-wiki-pattern.md](docs/llm-wiki-pattern.md)):
the LLM reads raw course material once, compiles it into an interlinked markdown wiki,
and keeps that wiki current as new material arrives.

**Roles.** The student (Isaac) curates sources, asks questions and decides what matters.
The LLM does all the writing, cross-referencing, filing and bookkeeping. The student
reads the wiki; the LLM writes it.

---

## 1. Layout

```
CLAUDE.md            ← this schema (co-evolved; edit when a convention changes)
AGENTS.md            ← pointer to this file for non-Claude agents
README.md            ← human-facing intro: how to use the wiki
docs/                ← the original pattern document
raw/                 ← SOURCES. Immutable. Never edit, rename or delete.
  slides/              lecture decks (.pptx)
  papers/              research papers (.pdf)
  books/               textbooks (.pdf) — very large, ingest chapter by chapter
  code/class/          code handed out in class
  code/prolog_examples/ Prolog programs from the Prolog lecture (01_Code)
  assignments/         Isaac's own homework, labs and submissions
wiki/                ← THE WIKI. Owned and written entirely by the LLM.
  index.md             catalog of every page (read this first)
  log.md               append-only history of ingests, queries, lint passes
  overview.md          course map: how all topics fit together
  glossary.md          English term ↔ Spanish explanation, alphabetical
  people.md            who's who (researchers, authors), one section each
  sources/             one summary page per raw source
  concepts/            one page per concept / algorithm / technique
  assignments/         one page per assignment: what was asked, what was done, review
  study/               exam prep: comparisons, question banks, cheat sheets, errata
tools/               ← small helper scripts (see §7)
.cache/              ← extracted text of raw sources (git-ignored, regenerable)
```

Exception to "raw is immutable": a new source may be **added** to `raw/` (by the student
or by the LLM on request), and organizing a newly dropped file into the right subfolder
is allowed. Existing raw files are never modified.

## 2. Language convention (bilingual)

The student asked for: **English for key terms, code and summaries; Spanish for
explanations.** Concretely, on every wiki page:

| Part of the page | Language |
|---|---|
| Title (H1) | English term, Spanish in parentheses: `# A* Search (Búsqueda A*)` |
| `> **Summary (EN):**` block at the top | English, 2–4 sentences |
| Key terms table | English term · Spanish term · short Spanish meaning |
| `## Explicación` and other explanatory sections | **Spanish** |
| Code, pseudocode, formulas, identifiers | English (as in the sources) |
| Section headings | Spanish, except fixed headings listed in §3 |
| Quotes from sources | Original language |

Keep technical terms in English inside Spanish prose the first time, e.g.
"la frontera (*frontier*)". Use plain, student-friendly Spanish.

## 3. Page format

Every page in `wiki/` (except `index.md` and `log.md`) starts with YAML frontmatter:

```yaml
---
title: A* Search
type: concept            # concept | source | assignment | study | overview | glossary | people
tags: [search, informed-search]
sources: [slides-02-problem-solving, book-russell-norvig-aima]   # source-page slugs
updated: 2026-10-01
---
```

Then this skeleton (drop sections that don't apply, never leave empty headings):

```markdown
# English Title (Título en español)

> **Summary (EN):** two to four sentences.

## Términos clave
| English | Español | Significado |

## Explicación
Spanish explanation, built up from intuition to formal definition.

## Pseudocódigo / Código        (English code)
## Ejemplo                       (worked example, ideally from the course)
## Errores comunes y tips de examen
## Relacionado                   (links to related wiki pages)
## Fuentes                       (links to source pages + exact slide/page/section)
```

**Source pages** (`wiki/sources/`) instead use: Summary (EN) · Ficha (metadata table:
author, year, file path in `raw/`, type, length) · Resumen por secciones (Spanish) ·
Ideas clave · Conceptos que alimenta (links) · Notas y discrepancias.

**Assignment pages** (`wiki/assignments/`) use: Summary (EN) · Enunciado · Qué se
implementó · Resultados (real outputs, if the code was run) · Revisión (strengths,
bugs, improvements — honest and specific) · Conceptos relacionados.

## 4. Linking rules

- Use **standard relative markdown links** (the wiki is read on GitHub / any viewer,
  not Obsidian): `[A* Search](../concepts/a-star-search.md)`.
- File names: lowercase kebab-case English, `.md`. Source slugs are prefixed by kind:
  `slides-`, `paper-`, `book-`, `code-`.
- Link to raw files with a relative path and URL-encode spaces (`%20`) so the link
  works on GitHub: `[slides](../../raw/slides/02_Problem%20Solving.pptx)`.
- Every concept page links to ≥1 source page and ≥2 related pages. Every page must be
  reachable from `index.md`. No orphans.
- Cite precisely: "slides-02, slide 14", "AIMA 4e §3.5", "Kennedy & Eberhart 1995, §3.6".

## 5. Operations

### Ingest (a new source)
1. Make sure the file is in the right `raw/` subfolder. Run
   `python3 tools/extract_text.py <path>` and read `.cache/text/...`.
   Slides often hold equations and diagrams as images: say so when content is missing
   rather than inventing it; fill gaps from the textbooks and mark them as such.
2. Briefly tell the student the key takeaways and ask what to emphasize
   (skip the question if they asked for batch mode).
3. Write `wiki/sources/<slug>.md`.
4. Create or update every affected concept page (expect 5–15 pages). When a new source
   adds to an existing page, integrate it — don't append a disconnected paragraph.
5. If the new source **contradicts** the wiki or another source, record it on the
   affected page under "Notas y discrepancias" and in `wiki/study/errata.md`.
6. Update `glossary.md`, `people.md`, `overview.md` and `index.md` as needed.
7. Append to `log.md`.

### Ingest (a textbook chapter)
Books in `raw/books/` are too large to ingest whole. Ingest them **chapter by chapter
on request**, using the chapter map on the book's source page. Enrich the existing
concept pages first; create new pages only for genuinely new concepts.

### Query
1. Read `wiki/index.md`, then the relevant pages; go to `.cache/text/` or `raw/` only
   when the wiki lacks the detail.
2. Answer in the bilingual style, citing wiki pages and sources.
3. If the answer is reusable (a comparison, a derivation, a worked exercise, an exam
   question), **file it** under `wiki/study/` (or extend a concept page), link it from
   `index.md`, and log it. Ask if unsure whether it is worth keeping.

### Lint
Run `python3 tools/lint_wiki.py` (broken links, orphans, missing frontmatter), then
review for: contradictions between pages, stale claims, concepts mentioned without a
page, missing cross-links, thin pages that a book chapter could fill. Report findings,
fix the mechanical ones, propose the rest, and log the pass.

### Assignment help
For a new assignment: create its page from the statement, link the concepts it needs,
and review the student's code when it is added to `raw/assignments/`. Explain and
guide; the student's submissions are their own work.

## 6. index.md and log.md

- `index.md` — sections: Start here · Sources · Concepts (grouped by unit) ·
  Assignments · Study. One line per page: `- [Title](path) — one-line summary`.
- `log.md` — append-only, newest at the bottom. Each entry starts with
  `## [YYYY-MM-DD] <op> | <title>` where `<op>` ∈ `ingest | query | lint | setup | update`,
  followed by bullets of pages created/updated. `grep "^## \[" wiki/log.md | tail -5`
  shows recent activity.

## 7. Tools

- `tools/extract_text.py [path…]` — .pptx (slides + speaker notes, stdlib only) and
  .pdf (`pdftotext`) → `.cache/text/`. Cached by mtime.
- `tools/lint_wiki.py` — checks broken relative links, pages unreachable from
  `index.md`, and missing frontmatter keys. Exit code 1 on problems.

## 8. Quality bar

- Faithful to sources; when adding outside knowledge (e.g., to fill an equation that was
  an image on a slide), say "(complemento: AIMA §x.y)" or "(conocimiento general)".
- Prefer worked examples from the course (Romania map, 8-puzzle, N-queens, family.pl,
  f(x,y)=(x+2)²+(y−2)²+10) over new ones.
- Write for exam preparation: definitions, properties (complete? optimal? complexity?),
  comparisons, typical traps.
- Keep `updated:` in frontmatter current when a page changes.
