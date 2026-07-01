#!/usr/bin/env python3
"""tic_report.py — ASSIST (not a gate): surface motif/tic density + verb-form candidates per chapter.

It does NOT decide anything. It flags candidates so the line-edit judgment pass is systematic
instead of eyeballed. Two reports:

  1. MOTIF DENSITY — counts the book's deliberate recurring phrases per chapter. Deliberate motifs
     are load-bearing and STAY; the point is to spot *incidental over-use* (a chapter far above the
     book median) so the redundant instances can be thinned while the load-bearing one is kept.
     (This is the AI-reviewers' "vary internal motifs" note — banking / count / small true things.)

  2. VERB-FORM / RHYTHM CANDIDATES — lines with dense past-perfect ("had -ed") chains or -ing
     stacks. These are the class Eilidh (Book One reviewer) touched by preference (looked->look,
     smelling->smelled): grammatically correct, so LanguageTool stays silent — a human/Claude must
     judge whether the tense/ending reads better changed. Pure candidates, high false-positive rate.

Usage:
  python3 tools/tic_report.py                      # all chapters
  python3 tools/tic_report.py --file manuscript/chapters/chapter-4.md
"""
import argparse, glob, re, statistics
from pathlib import Path

# Deliberate recurring motifs (keep — flag only incidental over-use). Extend per book.
MOTIFS = [
    r"bank(?:ed|ing|s)?\b",
    r"the count\b", r"kept count\b", r"counting\b",
    r"small true thing",
    r"careful face", r"the flat( hard)? thing", r"flat and stripped",
    r"cold working part", r"the arithmetic\b", r"did the sum",
    r"paid for (?:it|before)", r"coin by coin",
    r"where no one could see", r"did not (?:let it|weep)",
    r"filed (?:it|that|the)", r"the way she (?:read|always)",
]

def strip_comments(t): return re.sub(r"<!--.*?-->", "", t, flags=re.S)

def analyze(path):
    raw = strip_comments(Path(path).read_text())
    words = len(raw.split())
    counts = {}
    for pat in MOTIFS:
        n = len(re.findall(pat, raw, flags=re.I))
        if n: counts[pat] = n
    total = sum(counts.values())
    # verb-form candidates: lines with >=3 "had <word>ed" or >=3 "-ing" in one sentence-ish span
    vf = []
    for i, line in enumerate(raw.splitlines(), 1):
        had_ed = len(re.findall(r"\bhad \w+ed\b", line))
        ing = len(re.findall(r"\b\w+ing\b", line))
        if had_ed >= 3 or ing >= 6:
            vf.append((i, had_ed, ing, line[:90]))
    return words, total, counts, vf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    a = ap.parse_args()
    files = [a.file] if a.file else sorted(
        glob.glob("manuscript/chapters/chapter-*.md"),
        key=lambda p: int(re.search(r"(\d+)", Path(p).name).group(1)))
    rows = []
    for f in files:
        w, total, counts, vf = analyze(f)
        per1k = round(total / max(w, 1) * 1000, 1)
        rows.append((f, w, total, per1k, counts, vf))
    med = statistics.median([r[3] for r in rows]) if rows else 0
    print(f"MOTIF DENSITY (per 1k words) — book median {med}")
    for f, w, total, per1k, counts, vf in rows:
        flag = "  <-- HIGH, review for incidental over-use" if per1k > med * 1.3 and len(rows) > 1 else ""
        print(f"  {Path(f).name:16} {per1k:5}/1k ({total} in {w}w){flag}")
    if a.file:
        f, w, total, per1k, counts, vf = rows[0]
        print(f"\nMotif breakdown for {Path(f).name}:")
        for pat, n in sorted(counts.items(), key=lambda x: -x[1]):
            print(f"  {n:3}x  {pat}")
        print(f"\nVERB-FORM / RHYTHM candidates (judge each; correct-but-maybe-reworkable):")
        for i, he, ing, s in vf:
            print(f"  L{i}: had-ed={he} -ing={ing}  {s}...")
        if not vf: print("  (none)")

if __name__ == "__main__":
    main()
