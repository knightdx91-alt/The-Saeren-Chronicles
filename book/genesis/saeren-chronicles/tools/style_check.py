#!/usr/bin/env python3
"""
Saeren Chronicles — cross-manuscript style checker.

Catches the three things the per-chapter agents can miss across the whole book:
  1. VERBAL TICS         — overused filler/crutch words (just, suddenly, seemed, somehow...)
  2. REPEATED PHRASES    — distinctive 4-6 word n-grams reused within or across chapters
  3. METAPHOR/SIMILE LOAD — simile markers per 1,000 words vs a ceiling

Also reports adverb (-ly) density and em-dash density per chapter.

Usage:
    python3 tools/style_check.py                 # scan manuscript/chapters/chapter-*.md
    python3 tools/style_check.py --max-simile 4  # set simile-per-1k ceiling (default 4)

Exit code is non-zero if any chapter breaches a ceiling or any cross-chapter
repeated phrase is found — so it can gate the pipeline.
"""
import argparse, glob, os, re, sys
from collections import Counter, defaultdict

# Crutch words / verbal tics to watch (lowercase, whole-word).
TIC_WORDS = [
    "just", "suddenly", "somehow", "seemed", "slightly", "simply", "really",
    "very", "almost", "perhaps", "actually", "felt like", "a beat",
    "for a moment", "for a long moment", "something like", "as if", "as though",
]
# Distinctive author fingerprints flagged in the session log to keep rare.
FINGERPRINT_PHRASES = [
    "there and gone", "the kind of", "not because", "deep water",
    "like water", "drew in", "made herself a smaller target",
]
SIMILE_MARKERS = re.compile(r"\b(like|as if|as though)\b", re.I)
ADVERB = re.compile(r"\b\w+ly\b", re.I)
WORD = re.compile(r"[a-z']+", re.I)

# Deliberate recurring motifs / canon terminology — NOT accidental reuse.
# Repeated phrases that contain any of these are ignored by the n-gram check.
ALLOWLIST = [
    "be careful who you let see you do it",
    "no one sees you do it",
    "let see you do it",
    "both sides of the gift",
    "dark blue stone", "dark-blue stone",
    "the source of all magic",
    "since the morning the world ended",   # recurring grief refrain (intentional)
]

# n-gram repetition settings
NGRAM_MIN, NGRAM_MAX = 4, 6
# stopword-only n-grams are noise; require at least this many "content" words
STOP = set("the a an and or but of to in on at for with as is was were be been "
           "her his its their my your she he it they i you we him them me".split())


def words(text):
    return [w.lower() for w in WORD.findall(text)]


def ngrams(toks, n):
    return [tuple(toks[i:i+n]) for i in range(len(toks)-n+1)]


def content_rich(ng):
    return sum(1 for w in ng if w not in STOP) >= max(2, len(ng)-2)


def scan():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="manuscript/chapters")
    ap.add_argument("--max-simile", type=float, default=4.0,
                    help="simile markers per 1,000 words ceiling")
    ap.add_argument("--max-adverb", type=float, default=20.0,
                    help="-ly adverbs per 1,000 words ceiling")
    ap.add_argument("--tic-ratio", type=float, default=6.0,
                    help="per-1,000-words ceiling for any single tic word")
    ap.add_argument("--max-emdash", type=int, default=4,
                    help="ABSOLUTE em-dashes allowed per chapter (AI tell — keep near zero)")
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(base)
    chap_dir = os.path.join(root, args.dir)
    files = sorted(glob.glob(os.path.join(chap_dir, "chapter-*.md")),
                   key=lambda p: int(re.search(r"chapter-(\d+)", p).group(1)))
    if not files:
        print("no chapter files found in", chap_dir); return 1

    problems = 0
    phrase_chapters = defaultdict(set)   # ngram -> {chapter numbers}
    phrase_counts = Counter()

    print("=" * 70)
    print("PER-CHAPTER STYLE REPORT")
    print("=" * 70)
    for f in files:
        n = int(re.search(r"chapter-(\d+)", f).group(1))
        text = open(f, encoding="utf-8").read()
        toks = words(text)
        wc = len(toks) or 1
        per1k = lambda c: round(c / wc * 1000, 1)

        similes = len(SIMILE_MARKERS.findall(text))
        adverbs = len(ADVERB.findall(text))
        emdash = text.count("—")

        sim1k, adv1k, em1k = per1k(similes), per1k(adverbs), per1k(emdash)
        flags = []
        if sim1k > args.max_simile:
            flags.append(f"SIMILE {sim1k}/1k > {args.max_simile}"); problems += 1
        if adv1k > args.max_adverb:
            flags.append(f"ADVERB {adv1k}/1k > {args.max_adverb}"); problems += 1
        if emdash > args.max_emdash:
            flags.append(f"EM-DASH {emdash}/chapter > {args.max_emdash} (density {em1k}/1k)"); problems += 1

        tic_hits = []
        low = text.lower()
        for t in TIC_WORDS:
            c = len(re.findall(r"\b"+re.escape(t)+r"\b", low))
            if c and per1k(c) > args.tic_ratio:
                tic_hits.append(f"{t}×{c} ({per1k(c)}/1k)"); problems += 1
        fp_hits = [f"'{p}'×{low.count(p)}" for p in FINGERPRINT_PHRASES
                   if low.count(p) > 1]

        print(f"\nCh{n:>2}  {wc} words | simile {sim1k}/1k | adverb {adv1k}/1k | em-dash {emdash} ({per1k(emdash)}/1k)")
        if flags:    print("   CEILING:", "; ".join(flags))
        if tic_hits: print("   TICS:   ", "; ".join(tic_hits))
        if fp_hits:  print("   FINGERPRINTS:", "; ".join(fp_hits)); problems += len(fp_hits)

        # collect n-grams for cross-chapter repetition
        for nlen in range(NGRAM_MIN, NGRAM_MAX+1):
            for ng in ngrams(toks, nlen):
                if content_rich(ng):
                    phrase_counts[ng] += 1
                    phrase_chapters[ng].add(n)

    print("\n" + "=" * 70)
    print("REPEATED PHRASES (4-6 words, content-rich)")
    print("=" * 70)
    # Cross-chapter (appears in 2+ chapters) OR heavily repeated overall
    repeated = [(ng, phrase_counts[ng], sorted(phrase_chapters[ng]))
                for ng in phrase_counts
                if (len(phrase_chapters[ng]) >= 2 or phrase_counts[ng] >= 3)]
    # prefer longer / more-repeated phrases, drop ones fully contained in a flagged longer one
    repeated.sort(key=lambda x: (-len(x[0]), -x[1]))
    shown = []
    for ng, cnt, chs in repeated:
        s = " ".join(ng)
        if any(allowed in s or s in allowed for allowed in ALLOWLIST):
            continue
        if any(s in bigger for bigger in shown):
            continue
        shown.append(s)
        scope = f"chapters {chs}" if len(chs) >= 2 else f"chapter {chs[0]}"
        print(f"  ×{cnt}  [{scope}]  \"{s}\"")
        problems += 1
    if not shown:
        print("  none")

    print("\n" + "=" * 70)
    print(f"RESULT: {problems} issue(s) flagged." if problems else "RESULT: clean.")
    print("=" * 70)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(scan())
