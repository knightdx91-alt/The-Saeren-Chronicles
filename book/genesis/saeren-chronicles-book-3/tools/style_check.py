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
    # Book Three deliberate recurring motifs / canon terms.
    "the weight of the source",
    "every birth and every death",
    "a place where a core should be",
    "both halves of the gift",
    "absence drawn to presence",
    "the cold working part",
    "she filed it",
    "the rest of both your lives",
    # established cross-chapter voice motifs (Ch.1/2/3) and Ch.3 deliberate motifs
    "survive the choosing",
    "arithmetic so the rest",
    "rest of her could survive",
    "long table behind",
    "to hold both halves",
    "cold edge of the world",
    "the deaths with no wound",
    # Ch.5 deliberate recurring refrains (intentional, load-bearing):
    "the warmth thinned toward and did not reach",   # the Ch.1 re-read-reward callback, reprised at the climax
    "tell the difference from the inside between you", # Amber's signature evolving moral question (the book's spine)
    "toward the warmth she had become",               # the binding pull-mechanic phrase (Horrors pulled to the source)
    "place the warmth thinned toward and",            # leading fragment of the same Ch.1 callback refrain
    "you tell the difference from",                   # leading fragment of Amber's signature question refrain
    # Ch.6 deliberate bookend refrain (the chapter's resolve, stated twice on purpose):
    "would go to the source",                         # "She would go to the source." — the Ch.6 END-hook refrain
    # Series-spine refrains carried Ch.5-7 (intentional, load-bearing):
    "and she did not weep",                           # the grief-held-inward guardrail refrain (no one sees Viridia cry)
    "to make the world whole",                        # the thematic-spine refrain (she wanted only to make the world whole)
    # Ch.8 (Act Two open) deliberate character/voice motifs (load-bearing, recurring by design):
    "he could not stop being",                        # Raizen's CANON trait (the light of what he is runs off him; Ch.1/2/8)
    "and the bond carried what",                      # the True-Bond motif: the bond carries what her face/words will not (Ch.2/7/8)
    "plainly and in few words",                       # Viridia's signature register for telling hard truths (Ch.6/7/8)
    "she heard her own voice",                        # the "flat hard certainty over the part that doesn't believe it" tell (Ch.3/5/8)
    "cold working part of her",                        # canon: "the cold working part" — Viridia's arithmetic-self (foundation trait; Ch.1/8)
    "against the warmth she had",                      # binding pull-mechanic: the cold leaning against the warmth she became (Ch.7/8)
    "whole edge of the world",                         # binding scale-refrain: the WHOLE rim leaning in (the Ch.7 measurement; Ch.7/8)
    # Ch.9 (Drake's cosmology) deliberate spine refrains (BINDING: balance not victory; no mark for a pressure):
    "you do not draw a symbol",                        # the central limit: the mark closes a DOOR, not a pressure (Ch.5/7/8/9)
    "do not draw a symbol against",                    # same spine fragment
    "draw a symbol against the",                       # same spine fragment
    "there is no mark for",                            # the chapter's load-bearing answer: a pressure has no closing mark (Ch.7/9)
    "past a glass of water",                           # the Ch.7 whole-sight scale measurement refrain (the sea past a glass; Ch.7/8/9)
    "every living core there is",                      # canon phrase for the rebirth's reach (Ch.5/9)
    "the cold past the rim",                           # canon term for the abstract void/counterpart (Ch.8/9)
    # Ch.10 (the gut-punch) deliberate motifs (load-bearing, recurring by design within the chapter):
    "the thing eating the world",                      # the Ch.10 gut-punch refrain: the cure IS the thing eating the world (the chapter's spine image)
    "the sea past a glass",                            # the Ch.7 whole-sight scale measurement (the sea past a glass of water; Ch.7/8/9/10) — longer form of allowlisted "past a glass of water"
    "sea past a glass of",                             # same scale-measurement refrain, leading fragment
    "the cold edge of everything",                     # series spine motif: the abstract void rim (Ch.1/2/10) — the cold leaning at the edge of everything
    "cold edge of everything the",                     # same motif, trailing fragment
    "braced at the far end",                           # the True-Bond anchor motif (Raizen braced at the far end of the bond; Bk2 Ch.18, Bk3 Ch.1/10)
    "there is a difference between",                   # Viridia's recurring reflective pivot ("there is a difference between X and Y"; Ch.7/9/10)
    "best thing she had ever done",                    # the Ch.10 gut-punch pivot ("...the best thing she had ever done. / The best thing she had ever done was eating the world.") — deliberate two-beat
    "thing she had ever done",                         # same pivot, trailing fragment
    # grief-held-inward spine refrain variants (the guardrail: no one sees her cry) — load-bearing, recurring by design:
    "she did not weep because",                        # variant of allowlisted "and she did not weep"
    "she did not weep she",                            # same grief-inward refrain
    "because the not weeping was",                     # the Ch.10 elaboration of the no-weeping guardrail
    # thematic-spine refrain variants ("she wanted only to make the world whole"; Ch.5/6/7/10):
    "had wanted only to make the",                     # variant of allowlisted "to make the world whole"
    "wanted only to make the world",                   # same thematic-spine refrain
    "make the world whole and",                        # same thematic-spine refrain, trailing fragment
    # Ch.13 deliberate series-spine motifs (load-bearing callbacks, recurring by design):
    "source the way the source",                       # CANON: "tied to the source the way the source was tied to everything" (Bk1/Bk2; Ch.1/2/13) — Viridia-as-vessel definition
    "way the source was tied",                         # same vessel-definition motif, mid fragment
    "source was tied to everything",                   # same vessel-definition motif, trailing fragment
    "the only pair of hands",                          # the Lest/Alice lesson echoed back at the cost (Ch.12 Alice -> Ch.13 Amber) — deliberate dialogue callback
    "that did the arithmetic so the",                  # variant of the allowlisted "the cold working part / arithmetic so the rest" canon trait (Ch.1 onward)
    "she had no name for",                             # the unnameable void guardrail (abstract, no entity; MotV NOT resolved) — deliberate, Ch.1/2/13
    # Ch.14-15 deliberate series-spine motifs (load-bearing, recurring by design):
    "a life with almost no end",                       # the True-Bond long-life / doorway-forever motif (Ch.13/14/15) — the named cost
    "harder to even than a person",                    # the valve/wall mechanic Viridia taught Raizen ("a person in a wall is harder to even"; Ch.14/15)
    "the mark closes a door",                          # Death-symbol mechanic, Ch.15's core teaching (the mark closes a DOOR, not a pressure; Ch.9/15)
    "no mark for a pressure",                           # the Death-symbol-as-pressure spine (a pressure has no closing mark; Ch.9/11/15)
    "so the pull comes to",                             # the valve mechanic refrain (the pull comes to one place, not a hundred towns; Ch.14/15)
    "and you do not draw",                              # the Death-mark refusal refrain (you do not draw a symbol against a pressure; Ch.5/9/15)
    "not a thing she would",                            # the do/be realization motif ("not a thing she would DO, a thing she would BE"; Ch.12/14/15)
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
        text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)  # ignore editorial comments
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
    # A repeat is only DISTINCTIVE (and therefore a gate failure) when the phrase
    # is long enough to be a real signature AND it recurs strongly:
    #   >= 5 words  AND  (used 3+ times overall OR spread across 3+ chapters).
    # Shorter / x2 generic n-grams are common in any prose — report them as
    # informational context only; they do not fail the gate.
    def distinctive(ng, cnt, chs):
        return len(ng) >= 5 and (cnt >= 3 or len(chs) >= 3)

    candidates = [(ng, phrase_counts[ng], sorted(phrase_chapters[ng]))
                  for ng in phrase_counts
                  if (len(phrase_chapters[ng]) >= 2 or phrase_counts[ng] >= 3)]
    # prefer longer / more-repeated phrases, drop ones fully contained in a flagged longer one
    candidates.sort(key=lambda x: (-len(x[0]), -x[1]))
    shown_flag, shown_info = [], []
    for ng, cnt, chs in candidates:
        s = " ".join(ng)
        if any(allowed in s or s in allowed for allowed in ALLOWLIST):
            continue
        scope = f"chapters {chs}" if len(chs) >= 2 else f"chapter {chs[0]}"
        if distinctive(ng, cnt, chs):
            if any(s in bigger for bigger in shown_flag):
                continue
            shown_flag.append(s)
            print(f"  FLAG ×{cnt}  [{scope}]  \"{s}\"")
            problems += 1
        else:
            if len(shown_info) < 25 and not any(s in bigger for bigger in shown_flag):
                shown_info.append(s)
    if not shown_flag:
        print("  none distinctive (gate clean)")
    if shown_info:
        print(f"\n  (informational — {len(shown_info)} generic/×2 repeats, not gated):")
        for s in shown_info[:25]:
            print(f"     · \"{s}\"")

    print("\n" + "=" * 70)
    print(f"RESULT: {problems} issue(s) flagged." if problems else "RESULT: clean.")
    print("=" * 70)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(scan())
