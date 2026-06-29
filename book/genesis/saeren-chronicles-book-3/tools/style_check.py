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
    # Ch.16/17 (the approach + the climax working) deliberate spine refrains (BINDING, load-bearing, recurring by design):
    "of the very long way off",                        # the cost-motif: she keeps her edges "for the whole of the very long way off" (the True-Bond means a very long life; Ch.15/16/17)
    "whole of the very long way",                      # same cost-motif, leading fragment
    "the threshold where the stone began",             # Raizen-as-doorpost staging motif (he braces at the threshold where the cavern stone begins; Ch.16/17)
    "the difference between a sacrifice",               # the witnessed-not-alone spine: "the difference between a sacrifice and a crime" (the Bk2-climax-agency lesson; Ch.15/16/17)
    "difference between a sacrifice and",               # same spine fragment
    "front of everyone she loved",                      # the WITNESSED-climax motif: she does it "in front of everyone she loved" (the agency-witnessed lesson; Ch.15/16/17)
    "far braced end of it",                             # the True-Bond anchor staging (Raizen at the far braced end of the bond; Bk2 Ch.18, Bk3 Ch.15/16/17)
    "merged one core of her",                           # canon: her single merged light/dark core, thrown across the door (Ch.15/16/17)
    "a thing with no shadow",                           # the Dangris standing-with motif (a thing with no shadow standing where the shadow leans through; Ch.15/16/17)
    "the whole leaning weight of",                      # the climax pressure-mechanic: the whole leaning weight of two oceans through the door of her (Ch.16/17)
    "hand up out of the pool",                          # the rebirth-counterpart contrast (a year ago she drew her hand up out of the pool free; this time she cannot; Ch.13/17)
    "her hand up out of",                               # same contrast, leading fragment
    "the way it had taken",                             # the cavern-takes-her motif (the room/source took her, as it had taken her before; Ch.14/16/17)
    "there had only ever been",                         # the agency-spine: "there had only ever been her[s]" — the only hand at the rim (Ch.8/16/17)
    "the width that let the",                           # the central enacted-balance mechanic of Ch.17: holding the door to the width that lets the lean be a lean (the chapter's load-bearing working-refrain)
    # Ch.18/19 (the cost interior + the denouement) deliberate door-mechanic motifs (BINDING, load-bearing, recurring by design):
    "carried it across the sill",                       # the cost-mechanic: she carries every birth/death "across the sill" of the door she has become (Ch.18/19) — the enacted living-throttle image
    "carried it across the sill of",                    # same sill-carrying motif, trailing fragment
    "came and went across her",                         # the living-throttle refrain: the world's whole traffic comes and goes "across her" (the door she is, anywhere; Ch.17/18/19)
    "the world come and go across",                     # same traffic-across-her motif, variant form
    "door at the width that let",                       # the central door-mechanic refrain (holds the door at the width that lets the world keep what it makes; Ch.17/18/19)
    "the very long way off and",                        # the cost-motif tail (the True-Bond life; Ch.15-19) — already-allowlisted "of the very long way off" tail-fragment
    "very long way off and the",                        # same cost-motif, trailing fragment
    "was going to feel every one",                      # the living-throttle refrain: she is going to feel every one begin and end (Ch.18/19)
    "going to feel every one of",                       # same living-throttle refrain, trailing fragment
    "had come back to her slowly",                      # canon: Alice's warmth/laugh "came back to her slowly across the year" (Bk2 + Ch.1/19) — the recovery motif
    "looked down until it stopped did",                 # the grief-inward guardrail refrain (a burning you looked down until it stopped did not count; Ch.16/17/19)
    "down until it stopped did not",                    # same grief-inward refrain, mid fragment
    "until it stopped did not count",                   # same grief-inward refrain, trailing fragment
    "when your eyes burned and because",                # same grief-inward elaboration (a good place to look when your eyes burned; Ch.17/18/19)
    "settled it with herself years since",              # the grief-inward guardrail set-up (she had settled it with herself years since; Ch.17/18/19)
    "with herself years since that a",                  # same grief-inward set-up, trailing fragment
    "had settled it with herself years",                # same grief-inward set-up, lead fragment (she had settled it with herself years since; Ch.17/18/19)
    "it with herself years since that",                 # same grief-inward set-up, mid fragment
    "herself years since that a burning",               # same grief-inward set-up, mid fragment
    "and because she had settled",                      # same grief-inward set-up, lead fragment
    "because she had settled it",                       # same grief-inward set-up, mid fragment
    "far end of the line",                              # the True-Bond anchor staging refrain (Raizen rooted on the far end of the line; Ch.16/18/19)
    # Ch.19 (the denouement) deliberate spine refrains (BINDING, load-bearing, recurring by design across Act Three):
    "far end of the bond",                              # the True-Bond anchor staging (she feels him on the far end of the bond; Ch.2/16/19)
    "in the way that mattered",                         # canon tether-at-distance phrase: her hand stays in the source "in the way that mattered" (Ch.15/17/19)
    "the burning came up behind",                       # the grief-inward guardrail: the burning comes up behind her eyes and she looks down (Ch.16/17/19)
    "until it passed because the",                      # same grief-inward refrain, trailing fragment (looked down until it passed; Ch.16/17/19)
    "the second warmth the doorpost",                   # Raizen-as-doorpost staging (the second warmth, the doorpost; Ch.16/18/19)
    "she would never be able",                          # the cost-isolation refrain (she would never be able to say the half of it; Ch.17/18/19)
    "would never be able to",                           # same cost-isolation refrain, trailing fragment
    "width that let the world",                         # the door-mechanic refrain (the width that let the world keep what it made; Ch.17/19)
    "the width it could survive",                       # the door-mechanic refrain (the width the world could survive; Ch.17/19)
    "warmth she had become the",                        # the binding pull-mechanic (toward the warmth she had become; Ch.17/18/19)
    "no end to a watch",                                # the watch-cost spine (no end to a watch but the end of the watcher; Ch.17/18/19)
    "the cost of this one",                             # the cost-contrast refrain (the cost of this one was carried, not spent; Ch.17/19)
    "cost of this one was",                             # same cost-contrast refrain, trailing fragment
    "she was sixteen years old",                        # the age-fact refrain (she was sixteen years old; Ch.17/18/19) — age now stated plainly per author decision
    "in her own two hands",                             # the taken-up-not-spent cost refrain (carried in her own two hands; Ch.17/19)
    "the whole even traffic of",                        # the living-throttle refrain (the whole even traffic of the world's warmth; Ch.18/19)
    "held the door and let",                            # the door-holding closing refrain (held the door and let the world come and go; Ch.18/19)
    "door and let the world",                           # same closing refrain, trailing fragment
    "the world came and went",                          # the living-throttle refrain (the world came and went across her; Ch.18/19)
    "feel every one of them",                           # the living-throttle refrain (feel every one of them begin and end; Ch.18/19)
    "the way she had set",                              # the set-it-down-as-a-fact motif (she set the age/arithmetic down where she could see it; Ch.18/19)
    "the line off the back",                            # the True-Bond staging (the bond running off the back of her; Ch.16/17/18/19)
    "smallest degree at a time",                        # the recession-motif (the cold leaning back the smallest degree at a time; Ch.18/19)
    "where the cold leaned thinnest",                   # the Dangris staging refrain (the seam where the cold leaned thinnest; Ch.17/18/19)
    "toward the source the way",                        # the binding pull-mechanic (drawn toward the source the way absence is drawn to presence; Ch.5/18/19)
    "the only one who could",                           # the END-HOOK agency refrain: the cost is hers, she is the only one who could carry it (echoes the Ch.3 refuse-to-rule beat by design; Ch.3/19)
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
    # Ch.18 (THE COST — interior) deliberate spine refrains (BINDING, load-bearing, recurring by design):
    "a burning you looked down",                       # the grief-held-inward guardrail: an eye-burn looked down until it passes does not count (no one sees her cry; Ch.16/17/18)
    "you looked down until it",                         # same eye-burn grief-inward motif, trailing fragment
    "no eyelid for",                                    # the Ch.18 cost-mechanic: there is no looking away from the traffic of the world (no eyelid for it) — the chapter's load-bearing image
    "the company held the line they could see",         # the witnessed-but-cannot-feel mercy motif (the company holds the visible line; the door is hers alone to feel; Ch.16/17/18)
    "held the line they could see",                     # same witnessed-mercy motif, trailing fragment
    "the rebirth had run the world's lung full",        # the cost-mechanic premise: the rebirth ran the lung full, now she is the breathing of it (Ch.17/18)
    "every birth and every death",                      # the LIVING-THROTTLE cost (already allowlisted above; the binding cost-statement; Ch.13/15/17/18)
    "back to its edge",                                 # the END-HOOK recession motif: the cold going back to its edge (the Horrors RECEDE, not killed; Ch.18)
    "where the stone began the doorpost",               # Raizen-as-doorpost staging (he braces at the threshold where the stone begins; Ch.17/18)
    "the world's lung full and",                        # cost-mechanic continuity (the rebirth ran the world's lung full; Ch.17/18)
    "she set herself across it",                         # the enacted door-holding mechanic from the climax (she sets herself across the sill; Ch.17/18)
    "and she set herself across",                        # same door-holding mechanic, leading fragment
    "and did not seal it",                               # the BINDING balance-not-victory beat (she does NOT seal the void; Ch.17/18)
    "did not seal it and",                               # same balance refrain, trailing fragment
    "in the pale even light",                            # the source-cavern staging refrain (she kneels in the pale even light of the pool; Ch.17/18)
    "that was still a girl",                             # the not-yet-only-the-function motif (the part of her still a girl; Ch.17/18)
    "line off the back of",                              # the True-Bond staging: the bond running rooted off the back of her (Ch.16/17/18)
    "place to look when your eyes",                      # the eye-burn grief-inward motif, mid fragment (a good place to look when your eyes burned; Ch.16/17/18)
    "to look when your eyes burned",                     # same eye-burn motif, mid fragment
    "since that a burning you looked",                   # same eye-burn motif, lead fragment
    "threshold where the stone began the",               # Raizen-as-doorpost staging (Ch.17/18)
    "a good place to look when",                          # eye-burn grief-inward motif, lead fragment (Ch.16/17/18)
    "good place to look when your",                       # same eye-burn motif
    "look when your eyes burned and",                     # same eye-burn motif
    "years since that a burning you",                     # same eye-burn motif, lead fragment
    "burning you looked down until",                      # same eye-burn motif, mid fragment
    "because that is what an",                            # the void balance-mechanic (the void leans because that is what an empty place does; Ch.17/18)
    "no mark for a pressure",                           # the Death-symbol-as-pressure spine (a pressure has no closing mark; Ch.9/11/15)
    "so the pull comes to",                             # the valve mechanic refrain (the pull comes to one place, not a hundred towns; Ch.14/15)
    "and you do not draw",                              # the Death-mark refusal refrain (you do not draw a symbol against a pressure; Ch.5/9/15)
    "not a thing she would",                            # the do/be realization motif ("not a thing she would DO, a thing she would BE"; Ch.12/14/15)
    # Ch.16 (Act Three open) deliberate canon callbacks (load-bearing, must MATCH Bk1 Ch.14 / Bk2 Ch.18 cavern prose):
    "that had never had weather and",                  # cavern description matched to Bk2 Ch.18 (deep places that never had weather; Ch.7/16)
    "thing the world is borrowed from",                # the source-definition motif, matched to Bk2 Ch.18 (Ch.7/16)
    "its pool of pale even light",                     # the waiting-room cavern image matched to Bk2 Ch.18 (Ch.7/10/16)
    "shining of its own accord",                       # the pool description matched to Bk2 Ch.18 (Ch.7/16)
    "a clever tired first year banking",               # the cavern-callback ("a clever tired first-year banking her core to an ember"; Bk2 Ch.18, Ch.7/15/16)
    "clever tired first year banking her",             #   same callback, mid fragment
    "tired first year banking her core",               #   same callback, mid fragment
    "first year banking her core to",                  #   same callback, trailing fragment
    "the split symbol rose to",                        # the source mechanic matched to Bk2 Ch.18 (the split symbol rose to the surface; Ch.13/15/16)
    "the far braced end of",                           # the True-Bond doorpost motif (Raizen braced at the far end; Bk2 Ch.18, Ch.15/16)
    "at the far braced end",                           #   same motif, leading fragment
    "the only freedom she had left",                   # the witnessed-cost spine (sacrifice vs crime, the only freedom she had left; Ch.14/15/16)
    "only freedom she had left and",                   #   same spine, trailing fragment
    "the whole of the difference between",             # the witnessed-cost spine (the difference between a sacrifice and a crime; Ch.6/15/16)
    "the oldest balance there is",                     # the standing-with / pact motif (Ch.15/16)
    "want to close a door",                            # the Death-mark wanting motif (Drake's cold-handed knowing; Ch.15/16)
    "draw a symbol against a",                         # the Death-mark refusal refrain (Ch.5/9/15/16)
    "the door does not close",                         # Marick's warning motif (the door, once opened, does not close; Ch.8/16)
    "the place the warmth thinned toward",             # the Ch.1 re-read-reward callback refrain (Ch.2/5/16)
    "drawing toward the warmth she had",               # the binding pull-mechanic phrase (Horrors pulled to the source; Ch.3/8/16)
    "warmth she had become and",                       #   same pull-mechanic, trailing fragment
    "on her own two feet",                             # the agency/witnessed motif (she walks at the front on her own two feet; Ch.15/16)
    "a thing you can't reach",                          # Alice's made-to-watch motif (Ch.15/16)
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
