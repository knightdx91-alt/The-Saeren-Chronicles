#!/usr/bin/env python3
"""
rhythm_check.py — flag the "observation / reflection / expanded-reflection"
paragraph template that beta readers noticed recurring across the book.

It is a TARGETING aid, not a gate. It scores narration paragraphs (no
dialogue) on how strongly they match the template, so an editor can fix the
real offenders instead of guessing. Heuristics, not truth — always read the
flagged paragraph before cutting.

Signals (each adds to a score):
  * 3+ sentences, no dialogue (the template is pure interiority)
  * reflective cue phrases ("she only knew", "it was not ... it was",
    "not X but Y", "as though", "the way her mother", etc.)
  * a "restating" tail: 2+ trailing sentences that re-explain the same idea
  * descending cadence: sentences get shorter toward the end (long setup,
    short reflective payoff) — the signature of the template
"""
import re, sys, glob, os

CUES = [
    r"\bshe only knew\b", r"\bit was not because\b", r"\bit was because\b",
    r"\bthere was a way\b", r"\bthere was something\b", r"\bas though\b",
    r"\bthe way her mother\b", r"\bnot the .+ but the\b",
    r"\bnever had a word\b", r"\bsaid one way\b", r"\bsaid another way\b",
    r"\bwhich was\b.*\banyway\b", r"\bit was the first\b.*\bthe last\b",
    r"\bnot .+\. it was\b", r"\bnot .+\. she\b",
]
CUE_RE = [re.compile(c, re.I) for c in CUES]

def split_sentences(text):
    # naive but adequate for prose; keep terminal punctuation
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p for p in parts if p.strip()]

STOP = {"the", "a", "an", "she", "he", "it", "they", "and", "but", "her",
        "his", "their", "of", "to", "in", "on", "for", "that", "this"}

def first_word(s):
    m = re.search(r"[A-Za-z']+", s.lower())
    return m.group(0) if m else ""

def score_paragraph(p):
    # skip spoken dialogue (quotes) and italic telepathy (*...*)
    if '"' in p or '“' in p or '”' in p or p.count('*') >= 2:
        return 0, {}
    sents = split_sentences(p)
    if len(sents) < 3:
        return 0, {}
    score, why = 0, {}

    # PRIMARY signal: stacked reflective cue phrases
    cue_hits = sum(1 for s in sents for r in CUE_RE if r.search(s))
    if cue_hits:
        score += cue_hits
        why['cues'] = cue_hits

    # anaphora: consecutive sentences opening with the same content word
    # ("It was ... It was ...", "Said one way ... Said another way ...")
    anaphora = 0
    fws = [first_word(s) for s in sents]
    for a, b in zip(fws, fws[1:]):
        if a and a == b:
            anaphora += 1
    if anaphora:
        score += anaphora
        why['anaphora'] = anaphora

    # restating tail ONLY counts when paired with a cue/anaphora signal
    if (cue_hits or anaphora):
        tail = sents[-2:]
        if all(len(s.split()) <= 9 for s in tail):
            score += 1
            why['short_tail'] = [len(s.split()) for s in tail]

    # require a genuine reflective signal, not pure cadence
    if not (cue_hits or anaphora):
        return 0, {}
    return score, why

def main():
    chap_dir = os.path.join(os.path.dirname(__file__), '..', 'manuscript', 'chapters')
    files = sorted(glob.glob(os.path.join(chap_dir, 'chapter-*.md')),
                   key=lambda f: int(re.search(r'(\d+)', os.path.basename(f)).group(1)))
    threshold = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    grand = 0
    for f in files:
        with open(f) as fh:
            lines = fh.readlines()
        flagged = []
        for i, line in enumerate(lines, 1):
            p = line.strip()
            if not p or p.startswith('#') or p.startswith('<!--') or p.startswith('*') and len(p) < 6:
                continue
            sc, why = score_paragraph(p)
            if sc >= threshold:
                flagged.append((i, sc, why, p))
        grand += len(flagged)
        name = os.path.basename(f)
        print(f"\n=== {name}: {len(flagged)} flagged (score >= {threshold}) ===")
        for i, sc, why, p in sorted(flagged, key=lambda x: -x[1]):
            snippet = (p[:110] + '…') if len(p) > 110 else p
            print(f"  L{i:<4} score {sc}  {why}")
            print(f"        {snippet}")
    print(f"\nTOTAL flagged across book: {grand}")

if __name__ == '__main__':
    main()
