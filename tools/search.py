#!/usr/bin/env python3
"""Search the wiki and the extracted source text (BM25 ranking, accent-insensitive).

Usage:
    python3 tools/search.py "alpha beta poda"          # wiki + sources
    python3 tools/search.py --wiki "heurística admisible"
    python3 tools/search.py --sources "pheromone evaporation" -n 5

Wiki pages are split into sections (## / ### headings); extracted sources in
.cache/text/ (run tools/extract_text.py first) are split into slides or pages.
Each hit shows the file, the section/slide/page, a score and a snippet.
"""
import argparse
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CACHE = ROOT / ".cache" / "text"
STOP = set("""a al and are as at be by de del el en es for from in is it la las los
lo of on or que se the to un una y o con por para su sus this that with""".split())


def norm(text):
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def tokens(text):
    return [t for t in re.findall(r"[a-z0-9*]+", norm(text)) if t not in STOP and len(t) > 1]


def wiki_chunks():
    for page in sorted(WIKI.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        title = re.search(r"^# (.+)$", text, flags=re.M)
        title = title.group(1) if title else page.stem
        for part in re.split(r"(?m)^(?=#{2,3} )", text):
            head = part.splitlines()[0].lstrip("# ").strip() if part.startswith("#") else "top"
            yield f"wiki/{page.relative_to(WIKI)}", f"{title} › {head}", part


def source_chunks():
    if not CACHE.exists():
        return
    for txt in sorted(CACHE.rglob("*.txt")):
        text = txt.read_text(encoding="utf-8", errors="ignore")
        name = txt.relative_to(CACHE).as_posix()[:-4]
        if "=== Slide" in text:
            for part in re.split(r"(?m)^(?==== Slide)", text):
                m = re.match(r"=== Slide (\d+)", part)
                if m:
                    yield f"raw/{name}", f"slide {m.group(1)}", part
        else:
            for i, part in enumerate(text.split("\f"), start=1):   # pdftotext page breaks
                yield f"raw/{name}", f"PDF page {i}", part


def snippet(text, query_terms, width=220):
    flat = re.sub(r"\s+", " ", text)
    low = norm(flat)
    pos = min((low.find(t) for t in query_terms if low.find(t) >= 0), default=0)
    start = max(0, pos - width // 3)
    snip = flat[start:start + width]
    for t in sorted(query_terms, key=len, reverse=True):
        snip = re.sub(f"({re.escape(t)})", r"«\1»", snip, flags=re.I) if t.isascii() else snip
    return ("…" if start else "") + snip.strip() + "…"


def search(query, use_wiki=True, use_sources=True, n=8):
    chunks = []
    if use_wiki:
        chunks += list(wiki_chunks())
    if use_sources:
        chunks += list(source_chunks())
    docs = [Counter(tokens(c[2])) for c in chunks]
    if not docs:
        return []
    avg = sum(sum(d.values()) for d in docs) / len(docs)
    q = tokens(query)
    df = {t: sum(1 for d in docs if t in d) for t in set(q)}
    k1, b = 1.5, 0.75
    scored = []
    for (path, where, text), d in zip(chunks, docs):
        length = sum(d.values()) or 1
        score = 0.0
        for t in q:
            if t not in d:
                continue
            idf = math.log(1 + (len(docs) - df[t] + 0.5) / (df[t] + 0.5))
            tf = d[t]
            score += idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * length / avg))
        if score > 0:
            scored.append((score, path, where, text))
    scored.sort(reverse=True)
    return [(s, p, w, snippet(t, q)) for s, p, w, t in scored[:n]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query")
    ap.add_argument("-n", type=int, default=8, help="number of results (default 8)")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--wiki", action="store_true", help="search only the wiki")
    group.add_argument("--sources", action="store_true", help="search only extracted sources")
    args = ap.parse_args()
    results = search(args.query, use_wiki=not args.sources, use_sources=not args.wiki, n=args.n)
    if not results:
        print("No results. (For sources, run python3 tools/extract_text.py first.)")
        return 1
    for score, path, where, snip in results:
        print(f"[{score:5.2f}] {path}  —  {where}\n        {snip}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
