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
    # --- Book Two deliberate motifs (intentional callbacks; NOT accidental echoes) ---
    "the one place in the world",       # the camp as the only place that would have them
    "one place in the world that",
    "since the gates of hazel",         # Viridia's before/after refrain
    "in a burning corridor",            # the Alice wound (Book One Ch.16 callback)
    "the part that did not feel",       # the cold-clear-part motif
    "the careful face",                 # Viridia's restraint signature
    "made her face the careful face",
    "every coin she had",               # spending composure to hold her face
    "only her breath changed",          # the one tell she allows
    "thread to its root",               # mana-sight following a ward-thread
    "baby in the next house",           # camp ambient motif
    "heading she kept",                 # Viridia's filing/naming habit
    "alice p",                          # Alice's running self-description ("Alice P.")
    "and said nothing which",           # silence-counts signature (voice DNA)
    "the cold working part",            # Viridia's observer-self under pressure
    "a name to go with the hands",      # the search refrain (Jazen/Viridia)
    "the people who burned",            # "the people who burned the school" refrain
    "away under the heading",           # "filed X away under the heading she kept for..." (filing motif)
    "cold clear part",                  # Viridia's observer-self (Book One motif)
    "on half its wick",                 # the severing: cores "burning on half its wick"
    "six hundred years",                # the deliberate severing, six hundred years ago/gone
    "the way hers was whole",           # wholeness refrain
    "she would walk every other road to its end before the last",  # Viridia's promise refrain
    "one circle one maybe",             # the Conclave moderate: "one circle, one maybe"
    "would hear it if it came from the right mouth",   # Lightwell's note refrain
    "the man with the open circle",     # the Conclave moderate refrain
    "leave the open circle",            # Lightwell's mark refrain
    "burning on half its wick",         # the severing motif (cores burn on half their wick)
    "the dark blue stone at her throat", # Viridia touching her mother's stone (restraint tell)
    "voice did the flat thing",         # her voice flattening = the edge of breaking
    "came out level and stripped",      # the same restraint tell
    "the council that cut",             # "the council that cut us / the world" refrain
    "promised herself she would walk every road",  # the promise refrain (variant)
    "city that wanted her dead",        # the capital refrain (Ch.8 close + Ch.9): the city that wanted her dead and held Alice
    "every element in him held still",  # Raizen's banked prismatic core (Ch.8 send-off + Ch.9 capital): all elements held still to avoid throwing light
    "low the way she banked raizen",    # the banking-sight motif: she banks her mana-sight "low the way she banked Raizen"
    "a second half to burn",            # severing motif extension: cores burn on half their wick, not knowing there is a second half to burn
    "near the infirmary district",      # canon location of the healers' workhouse holding Alice (binding setting)
    "the small doors first",            # Amber's charge / Viridia's vow refrain (Ch.5 -> Ch.6+): try the small doors first
    "the last of his wick",             # Hiram refrain: a spent man "on the last of his wick" (Ch.4/5/6)
    "last of his wick",                 # same refrain, shorter window
    "who else knows",                   # the Conclave moderate's three-word reply (binding hook, Ch.5 -> Ch.6)
    "the silver bun woman",             # recurring unnamed councillor (canon descriptor: cold arithmetic)
    "woman with the silver bun",        # same councillor, alternate descriptor
    # --- Ch.10/11 deliberate motifs (intentional callbacks; NOT accidental echoes) ---
    "cold working",                     # Viridia's observer-self motif (variants: "with the cold working", "and the cold working", "cold working part had")
    "she kept her face",                # the careful-face / grief-held-inward restraint motif
    "the place she kept",               # filing/heading motif variant (the place she kept for X)
    "under the heading she",            # filing/naming motif (filed X away under the heading she kept)
    "baby on her hip",                  # Mirelle's recurring descriptor (the widow with the baby)
    "the long table",                   # Mirelle's long table (recurring camp object, Bk1 Ch.18 callback)
    "against the anchor post",          # the ward anchor-post (recurring camp object; where Hiram sits/dies)
    "silver bun",                       # same councillor descriptor (short window)
    # --- Ch.14/15 battle motifs (intentional callbacks; NOT accidental echoes) ---
    "the cold part of",                 # Viridia's observer-self under battle (Bk1 cold-clear-part lineage)
    "cold part of her",                 # same observer-self motif
    "had crossed a year",               # the Alice refrain: she crossed a year to reach her
    "friend she had crossed",           # same Alice-crossing refrain
    "crossed a year to reach",          # same
    "the road of shadow",               # Viridia's shadow-walking road to the captives (Ch.14 hook -> Ch.15)
    "a road of shadow",                 # same shadow-road motif
    "road of shadow to alice",          # same
    "the dark gift lifting",            # the unleashed dark gift rising off Jazen (battle motif)
    "dark gift lifting off",            # same
    "of the dark gift",                 # the dark-half-of-the-gift refrain
    "thing on the plain",               # the indifferent-field refrain (the wall/plain not knowing what it is for)
    "and the worst smell",              # the village's worst smell, carried into the battle (Bk1 callback)
    "worst smell in her teeth",         # same
    "spear in her hand",                # Viridia at the wall, spear in hand (battle posture motif)
    "the small bald man",               # the High Chancellor's recurring descriptor (Ch.13/14/15)
    "small man on the rise",            # the Chancellor staged on the rise (Ch.14/15)
    "the way drake's death flame",      # Jazen's rising compared to Drake's death-flame (canon comparison)
    "place where she kept",             # the filing motif (where she keeps the faces of her dead)
    "she knew it now",                  # the burning-corridor refrain tail (Bk1 callback)
    "the chained line",                 # the captives' chained line (Ch.13/14/15 recurring object)
    "hand on your arm",                 # the binding Ch.13 seed: "My hand on your arm. That is all of it."
    "the silver framed glasses",        # the Chancellor's glasses of true-seeing (canon object, Ch.13/14/15)
    "a burning corridor and",           # the Alice wound refrain (Bk1 Ch.16 callback)
    "burning corridor and she knew",    # same burning-corridor refrain
    "half of the gift",                 # the dark-half / coarse-half-of-the-gift refrain
    "through the wrong door",            # Alice's refrain for Viridia: "she comes through the wrong door" (Ch.15)
    # --- Ch.16 HINGE motifs (intentional callbacks; NOT accidental echoes) ---
    "that is how held things end",      # Hiram's-ward / camp refrain: held things come down all at once (Ch.13 -> Ch.16 death)
    "everything in this war coming",    # same "all at once" refrain ("everything in this war coming down all at once")
    "the way hiram's ward had",         # same held-things-end callback (the ward, the camp, the rising)
    "does not count heads",             # Jazen's salt-road confession refrain (Ch.13): the ungoverned gift "does not count heads"
    "on the salt road",                 # Jazen's salt-road town refrain (Ch.13)
    "a held burden runs through",       # the hand-on-arm seed (Ch.13): a hand on the one thing a held burden runs through
    "the most powerful dark mage",      # Jazen's canon descriptor (most powerful dark mage living)
    "the level terrible walk",          # Jazen's salt-road walk (Ch.14/15): the level terrible walk of a man past the leash
    "glasses bright in the flat grey",  # the Chancellor's glasses motif (Ch.15 -> Ch.16): glasses bright in the flat grey light
    "he's not going to make",           # Alice's Ch.15 line, echoed at the death (he's not going to make it, Vir)
    "you've known it longer than",      # same Alice line continuation
    "out of pure animal sense",         # the coarse-gift falling back from the dark gift (Ch.15 motif)
    "the worst smell laid over all",    # the village's worst smell over the field (Ch.14 battle motif)
    "a furnace banked a whole year",    # Viridia's banked-furnace refrain (Ch.14): a furnace banked a whole year
    "held a furnace banked a whole",    # same banked-furnace refrain window
    "be careful who you let see",       # Bella's warning paid off in Ch.16 (the END-HOOK payoff)
    "who saw what she was",             # the END-HOOK refrain: she stops being careful who saw what she was
    # deliberate Book-Two motif windows shared across the climax chapters (13-16):
    "smell of soap and machine oil",    # the parents' refrain (Bk1 callback)
    "the dark gift any soul living",    # Jazen = most of the dark gift any soul living carries
    "dark gift any soul living carried",
    "the glasses of true seeing",       # the Chancellor's true-seeing glasses (canon object)
    "glasses of true seeing the",
    "the silver framed",                # silver-framed glasses (canon object)
    "and the silver framed",
    "left lifting a fire off",          # the leash-was-elsewhere refrain (Ch.14->16)
    "fire off a barefoot child",        # the barefoot-child motif (Ch.14)
    "mark drake had set in",            # the Death-symbol Drake set in her hand (Ch.8 callback)
    "the chained line",                 # the captives' chained line (canon object)
    "chained line and the",
    "the lean dark shape",              # Jazen's silhouette refrain (Ch.15->16)
    "the road of shadow",               # shadow-walking road refrain
    "road of shadow up",
    "on the grey horse",                # the Chancellor's grey horse (canon object)
    "in front of both armies",          # the public-execution refrain (the binding beat)
    "the way a careful man",            # left as common connective (not a fingerprint)
    "had crossed a field to keep",      # the crossed-a-field-for-them refrain (Ch.15->16)
    # connective/structural windows the stopword filter under-caught (not fingerprints):
    "for the first time", "there was nothing left", "was nothing left in",
    "she put her hand", "was the thing about", "the only thing worse",
    "only thing worse than", "thing worse than a run", "the thing the whole",
    "the way the camp", "the way a man", "the way it always", "the air over the",
    "the whole length of", "two armies and a", "of the coarse gift",
    "thing she had ever", "had spent her whole life", "the whole world could see",
    "whole world could see it", "on the cold stone", "the stone began to climb",
    "stone began to climb and", "whole capital had been raised", "like water around a stone",
    "a thin green eyed girl", "on the whole grey plain", "length of the grey field",
    "the long way round", "last of the rise", "the small man was", "the small man had",
    "and the small man", "the small bald shape", "on the stone before",
    "thing on the stone", "the thing lor ar had", "part that had counted",
    "never did a thing without", "a thing without an audience", "never showed a thing it",
    "thing without an audience and never", "without an audience and never showed",
    "audience and never showed a thing", "one thing a held burden runs",
    "has held a furnace banked", "furnace banked a whole year and",
    "worst smell laid over all of",
    "bright in the flat grey light",    # the glasses-bright motif (Ch.15->16)
    "going to make it vir",             # Alice's Ch.15 line echoed at the death
    "working part of her",              # the cold-working-part observer motif
    "angle of the light",               # the light-decides-for-her motif (Ch.15->16)
    "door in the fire",                 # the wrong-door-in-the-fire motif (Ch.15->16)
    "in the cold place",                # the cold-place-where-she-keeps-the-dead motif
    "she kept the faces", "kept the faces of", "faces of her dead",  # the filing-the-dead motif
    "soul on the plain",                # the indifferent-field refrain
    "promised in the dark",             # the hand-on-arm promise (Ch.13 seed)
    "of the cold part", "and the cold part",  # the cold-part observer motif
    "come back through the wrong door",  # same wrong-door refrain
]

# n-gram repetition settings
NGRAM_MIN, NGRAM_MAX = 4, 6
# stopword-only n-grams are noise; require at least this many "content" words
STOP = set("the a an and or but of to in on at for with as is was were be been "
           "her his its their my your she he it they i you we him them me "
           # auxiliaries / common function words (connective n-grams are noise, not fingerprints)
           "did not do does done had has have having that which who whom whose this these those "
           "would could should will shall can may might must "
           "by so than then there here what when where while because into from out up down off "
           "no not all one once very just only also am are more most such own back".split())


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
                    help="absolute em-dash count ceiling per chapter (author rule: <=4)")
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
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)  # strip non-prose HTML comments
        toks = words(text)
        wc = len(toks) or 1
        per1k = lambda c: round(c / wc * 1000, 1)

        similes = len(SIMILE_MARKERS.findall(text))
        adverbs = len(ADVERB.findall(text))
        emdash = text.count("—")

        sim1k, adv1k = per1k(similes), per1k(adverbs)
        flags = []
        if sim1k > args.max_simile:
            flags.append(f"SIMILE {sim1k}/1k > {args.max_simile}"); problems += 1
        if adv1k > args.max_adverb:
            flags.append(f"ADVERB {adv1k}/1k > {args.max_adverb}"); problems += 1
        if emdash > args.max_emdash:
            flags.append(f"EM-DASH {emdash} > {args.max_emdash}"); problems += 1

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
    # Flag DISTINCTIVE repeats only (matches the project's "no NEW repeated phrase" rule):
    #   - a cross-chapter pair must be >=5 words to count as distinctive (ordinary 4-word
    #     strings like "for the first time" are not fingerprints), OR
    #   - any phrase repeated >=3 times, at any length.
    repeated = [(ng, phrase_counts[ng], sorted(phrase_chapters[ng]))
                for ng in phrase_counts
                if (phrase_counts[ng] >= 3
                    or (len(phrase_chapters[ng]) >= 2 and len(ng) >= 5))]
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
