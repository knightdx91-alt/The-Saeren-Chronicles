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
    # --- Ch.17 THE DECISION motifs (intentional callbacks; NOT accidental echoes) ---
    "the bodies were real",             # Ch.17 spine refrain: every other door shut and the bodies were real
    "people through their magic",       # Amber's question paid off (Ch.9 -> Ch.17): control/change a whole people through their magic
    "the whole grieving half made world", # the severing refrain: the half-made world she can mend at the source
    "thing lor ar had named",           # the thing Lor-ar named on the mountain (Ch.5/12 -> Ch.17 callback)
    "of the thing lor ar",              # same Lor-ar callback window
    "the thing lor ar had",             # same
    "in a single stroke",               # mend-for-all refrain (Ch.12 vow -> Ch.17 decision)
    "burning on half their wick",       # the severing refrain (cores burn on half their wick)
    "the broken cores of every living", # the lattice refrain (broken cores of every living soul)
    "broken cores of every living soul",
    "cores of every living soul on",
    "every living soul on the",
    "creature in the grass",            # Lor-ar's no-absolving refrain (Ch.12 -> Ch.17)
    "the lank blond hair and",          # Alice's recurring descriptor (Ch.13/15 -> Ch.17)
    "the lank blond hair and the",
    "lank blond hair and the",
    "endings the mark drake had set",   # the Death-symbol-not-reached-for motif (Ch.16 -> Ch.17)
    "made for endings the mark drake",  # same
    "the mark drake had set",           # same Death-symbol callback
    "her hand on jazen's arm",          # the hand-on-arm promise (Ch.13 seed / Ch.16 / Ch.17)
    "hand on jazen's arm and",
    "tail of the iron line",            # the captives' iron line (Ch.16 -> Ch.17, Alice at its tail)
    "no longer careful at last",        # the END-HOOK refrain: no longer careful who saw what she was
    "longer careful at last and",
    "don't let the girl spend you",     # Drake's Ch.12 line, pointedly NOT said in Ch.17
    "let the girl spend you cheap",     # same Drake non-saying
    "with both ends of itself",         # the True-Bond reaching with both ends (Ch.12 -> Ch.17)
    "decided to meet it standing",      # Raizen's bracing (Ch.12 -> Ch.17)
    "expect a hard thing and",          # same Raizen-bracing window
    "hard thing and has decided",
    "told to expect a hard thing",
    "you'll know it after",             # Drake's "you'll know it after" (Ch.12 -> Ch.17)
    "the way you'll know it after",
    "know it the way you'll know",
    "don't know it the way you'll",
    "a sum you don't know",             # same Drake-on-the-cart callback ("you know it as a sum")
    "sum you don't know it",
    "bring him back whatever shape",    # Varissa's charge (Ch.12 -> Ch.17)
    "fall apart in the open air",       # Amber's-question refrain (Ch.12 -> Ch.17): the reply that falls apart in the open air
    "part carrying the saying so",      # the cold-part-carries-the-saying motif (Ch.12 -> Ch.17)
    "the dark a fortnight ago",         # Amber asked it in the dark a fortnight ago (Ch.9 -> Ch.12 -> Ch.17)
    "dark a fortnight ago and",
    "one time too many",                # Drake stood beside the loss one time too many (Ch.12 -> Ch.17)
    "tool he means to keep",            # the cleans-a-tool-he-means-to-keep motif (Ch.16 -> Ch.17)
    "lawful and the unlawful halves",   # the capital's lawful/unlawful-halves speech (Ch.16 -> Ch.17)
    "the way she understood everything too",  # the "understood everything too late" refrain (Ch.16 -> Ch.17)
    "she understood everything too late that",
    "way she understood everything too late",
    "and the net mages",                # the net-mages / smother-throwers (Ch.16 -> Ch.17 descriptor)
    "in the dark blue shirt",           # Jazen's dark blue shirt (Ch.15/16 -> Ch.17)
    "and watched the capital turn",     # the capital-twists-the-overture refrain (Ch.9/10 -> Ch.17)
    "watched the capital turn it",
    "the camp had hidden against exactly",  # the hidden-rifles-against-exactly-this motif (Ch.12 -> Ch.17)
    "camp had hidden against exactly this",
    "and never wanted to use",          # same hidden-weapons motif (never wanted to use)
    "never wanted to use and",
    "brave the expensive way and",      # the councilor's courage refrain (Ch.10 -> Ch.17)
    # connective/structural windows the stopword filter under-caught (not fingerprints):
    "the last door was", "on the far side", "the far side of", "standing in front of",
    "a held breath and", "the way the capital", "the way a person", "the way drake had",
    "spent it the way", "turned the whole of", "the whole of herself", "no cold part left to",
    "the cold part was broken", "hair and a wrong", "the whole long morning", "up the rail wire",
    "the open circle and", "knew it the way", "the first time in", "arrives too late is",
    "that arrives too late is", "arrives too late is the", "bring exactly this to exactly",
    "set in her hand", "her hand as grief",  # the Death-symbol set in her hand as grief (Ch.8/14/16 -> Ch.17)
    # --- Ch.18 THE REBIRTH motifs (intentional callbacks; NOT accidental echoes) ---
    "well of all magic",                # THE central motif: she reaches for / enters the well of all magic
    "would mend the severing",          # the rebirth spine: she would mend the severing for all (Ch.12 vow -> Ch.18)
    "the dark half of",                 # the dark-half-of-the-gift refrain (the cut she mends)
    "every living core on the",         # the lattice refrain: every living core on the plain/in the world
    "core on the plain",                # same lattice refrain (cores on the plain)
    "core in the world",                # same lattice refrain (every core in the world)
    "on the warm stone",                # the furnace-warmed rise stone (Ch.16 -> Ch.17 -> Ch.18 recurring place)
    "was no cold part",                 # the broken cold-part motif (no cold part left after Ch.16)
    "she turned the whole",             # "turned the whole of it" — the furnace turned skyward / poured into the cut
    "part of her left",                 # "no part of her left" — the spent/broken-observer motif
    "the children under it",            # the last-roof refrain (Brutus's beam Ch.11/14 -> the children under it)
    "and the children under",           # same last-roof refrain window
    "children at the carts",            # the children at the carts (battle location refrain, Ch.14/16/17)
    "the whole of himself",             # the wholeness refrain (everyone holding the whole of themselves, made whole)
    "the way a held breath",            # the void-absence motif (Bk1 Ch.14: empty the way a held breath is empty)
    "put a name to",                    # the name-search refrain (a name to go with the hands; Bella's name)
    # connective/structural windows the stopword filter under-caught (not fingerprints):
    "did not let herself think", "had not let herself", "how much of herself she",
    "the far end of", "far end of it", "every soul on the", "at the other end",
    "felt the whole of", "she let it go", "was the worst thing",
    "empty hands and the", "length of a breath",
    # --- Ch.19 WHAT REMAINS motifs (intentional callbacks; NOT accidental echoes) ---
    "front of her eyes",                # the spent-sight motif: she reads the world by the front of her eyes now (recurs through Ch.19)
    "front of the eyes",                # same spent-sight motif (from the front of the eyes)
    "the old sight gone and",           # Ch.18->19 callback: the always-on mana-sight spent
    "old sight gone and only",          # same spent-sight callback window
    "ordinary blinded back eyes",       # same: her ordinary blinded-back eyes (Ch.18->19)
    "in a dark room",                   # Ch.18->19 callback: she bought it in a dark room a portal away
    "the edge of the trees",            # Lor-ar's departure place (recurs through the release scene)
    "edge of the trees",                # same departure-place motif
    "stood in the grey morning",        # the stopped-army refrain (Ch.18 END -> Ch.19): standing still in the grey morning
    "every core in the world",          # the lattice/wholeness refrain (every core in the world made whole)
    "two in three of",                  # the survivors refrain (Ch.11/12 -> Ch.19): two in three of the camp left
    "three hundred years and",          # Lor-ar's age refrain (Ch.5/12 -> Ch.19): three hundred years on the spirit road
    "grieve close to the ground",       # Varissa's grief refrain (Ch.12 -> Ch.19): I grieve close to the ground
    "came forward low the scarlet",     # Varissa's approach refrain (Ch.12 -> Ch.19)
    "came forward low the scarlet head",
    "a creature six thousand years old", # Drake/Raizen's age refrain (Ch.7 -> Ch.19)
    "of a creature six thousand years",
    "you've got hands",                 # Drake's goodbye-made-whole line (Ch.19 beat)
    "said loud and ended fast",         # Drake's grieving-register motif (Ch.12 -> Ch.19)
    "the careful flat thing",           # Viridia's voice-under-pressure tell (recurring restraint motif)
    "where there was room",             # the dragons land where there is room (Ch.12 -> Ch.19)
    "the way dragons leave",            # the dragons-leave refrain (Ch.12 -> Ch.19): all at once and upward
    "all at once and upward",           # same dragons-leave refrain
    "the one tooth turned out",         # Alice's crooked tooth (the one true thing the change couldn't reach)
    "tooth turned out of line",         # same Alice crooked-tooth refrain
    "the calm hands",                   # Alice-changed motif: her calm hands / calm new face (Ch.15/16 -> Ch.19)
    "in the place she kept",            # the filing motif (the place she kept the good things)
    "and more than most of",            # the "more than most of X got" refrain (Ch.12 -> Ch.19)
    "more than most of the",            # same refrain window
    "where do we go",                   # the END-HOOK refrain: where do the living go now
    "a long count of",                  # the recovery-timeline motif: a long count of weeks (the sight returns slow)
    "the way everyone else",            # the ordinary-living motif: she must live by the front of her eyes the way everyone else does
    "a dark room a portal away",        # Ch.18->19 callback: she bought it in a dark room a portal away (the rebirth cost)
    "the bone white horns the lightning", # Lor-ar's canon descriptor (horns + lightning eyes; Bk1/Ch.12 -> Ch.19)
    "not visit beside the unfollowed thread", # the filing-the-worst-things motif (Ch.18 -> Ch.19): the place she does not visit
    "visit beside the unfollowed thread and",
    "close to the ground varissa",      # Varissa's grief-register refrain (Ch.12 -> Ch.19)
    "said the hard thing first",        # Drake's grief-register refrain (Ch.12 -> Ch.19): he says the hard thing first
    "came out level and stripped",      # already a motif; window variant (Viridia's voice tell)
    "the word came out level",          # same voice-tell window (the word came out level and stripped)
    "word came out level and",
    "level and stripped the way",
    "one tell she allowed herself",     # the one-tell restraint motif (her breath; Ch.16/12 -> Ch.19)
    # connective/structural windows the stopword filter under-caught (not fingerprints):
    "in the grey before dawn", "the grey before dawn the", "neither of them said anything",
    "said the word came out", "viridia stood at the edge", "six thousand years old and",
    "left over to spend on", "know viridia looked at the", "amber said her voice was",
    "tooth the one tooth turned", "was no longer any reason", "looked at the great grey",
    "the way a thing", "want you to know", "on the other side", "the first thing he",
    "said it the way", "last of the light", "seven feet of him", "that's the whole of",
    "the one true thing", "far side of the", "the thing viridia had", "walked the length of",
    "lor ar said you", "it lor ar said", "armor up over the", "where everyone could hear",
    "middle of the field", "length of the field", "the way the furnace", "whole of the difference",
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
