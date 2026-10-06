#!/usr/bin/env python3
"""Extract plain text from raw sources so the LLM can read them.

Usage:
    python3 tools/extract_text.py              # every source under raw/
    python3 tools/extract_text.py raw/slides   # only one folder or file

Writes one .txt per source into .cache/text/, mirroring the raw/ layout.
.pptx is parsed with the standard library (slide text + speaker notes);
.pdf uses `pdftotext -layout` (poppler-utils). Code files are already text.
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / ".cache" / "text"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def _paragraphs(xml_bytes):
    tree = ET.fromstring(xml_bytes)
    lines = []
    for p in tree.iter(f"{A}p"):
        text = "".join(t.text or "" for t in p.iter(f"{A}t")).strip()
        if text:
            lines.append(text)
    return lines


def pptx_to_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        slides = sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"(\d+)", n.rsplit("/", 1)[1]).group(1)),
        )
        for name in slides:
            num = re.search(r"slide(\d+)\.xml", name).group(1)
            out.append(f"\n=== Slide {num} ===")
            out.extend(_paragraphs(z.read(name)))
            notes = f"ppt/notesSlides/notesSlide{num}.xml"
            if notes in names:
                note_lines = [l for l in _paragraphs(z.read(notes)) if not l.isdigit()]
                if note_lines:
                    out.append("--- notes ---")
                    out.extend(note_lines)
    return "\n".join(out)


def pdf_to_text(path):
    return subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        check=True, capture_output=True, text=True,
    ).stdout


def extract(path):
    rel = path.relative_to(RAW)
    dest = OUT / rel.with_suffix(rel.suffix + ".txt")
    if dest.exists() and dest.stat().st_mtime >= path.stat().st_mtime:
        return dest, False
    if path.suffix == ".pptx":
        text = pptx_to_text(path)
    elif path.suffix == ".pdf":
        text = pdf_to_text(path)
    else:
        return None, False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return dest, True


def main(args):
    targets = [Path(a).resolve() for a in args] or [RAW]
    for target in targets:
        files = [target] if target.is_file() else sorted(target.rglob("*"))
        for f in files:
            if f.suffix in (".pptx", ".pdf"):
                dest, fresh = extract(f)
                status = "extracted" if fresh else "cached"
                print(f"{status:9} {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
