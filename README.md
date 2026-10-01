# LLM Wiki — Inteligencia Artificial

A personal study wiki for my university Artificial Intelligence course, built and maintained
by an LLM following Andrej Karpathy's
[LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
(copy in [docs/llm-wiki-pattern.md](docs/llm-wiki-pattern.md)).

Pages are **bilingual**: key terms, code and summaries in English; explanations in Spanish.

👉 **Start reading at [wiki/index.md](wiki/index.md)** (or the course map in [wiki/overview.md](wiki/overview.md)).

## How it works

| Layer | Folder | Who writes it |
|---|---|---|
| Raw sources (slides, papers, books, code, my assignments) | [`raw/`](raw/) | Me — never edited by the LLM |
| The wiki (summaries, concepts, assignment reviews, study sheets) | [`wiki/`](wiki/) | The LLM |
| The schema (rules and workflows for the LLM) | [`CLAUDE.md`](CLAUDE.md) | Both of us, over time |

## Using it with an LLM agent (Claude Code, Codex, …)

Open the repo in the agent and ask, for example:

- **Ingest:** "I added `raw/slides/05_Machine Learning.pptx` — ingest it."
- **Ingest a book chapter:** "Ingest AIMA chapter 4 (local search)."
- **Query:** "Compare A\* and greedy best-first with the Romania example." — good answers get filed into `wiki/study/`.
- **Quiz me:** "Ask me 5 exam questions on Unit 3 and grade my answers."
- **Lint:** "Lint the wiki." (runs `python3 tools/lint_wiki.py` and looks for contradictions and gaps)

The agent reads [`CLAUDE.md`](CLAUDE.md) for the conventions and records every operation in [`wiki/log.md`](wiki/log.md).

## Tools

```bash
python3 tools/extract_text.py            # slides/PDFs -> .cache/text/ (needs pdftotext for PDFs)
python3 tools/lint_wiki.py               # broken links, orphan pages, missing frontmatter
python3 tools/build_study.py             # regenerate pseudocode cheat sheet, Anki deck and quiz page
python3 tools/search.py "alpha beta"     # search the wiki and the extracted slides/PDFs
```

## Study tools

- **Anki deck:** [`study-tools/anki/ia-wiki-flashcards.txt`](study-tools/anki/ia-wiki-flashcards.txt) — import guide in [wiki/study/flashcards.md](wiki/study/flashcards.md).
- **Exam Drill quiz** and **Algorithm Lab** visualizers: [`study-tools/web/`](study-tools/web/) — open the `.html` files in a browser, or use the published links in [wiki/study/interactive-tools.md](wiki/study/interactive-tools.md).
