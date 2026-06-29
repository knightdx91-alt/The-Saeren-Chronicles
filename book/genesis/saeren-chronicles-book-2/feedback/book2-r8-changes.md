# Book Two — r7 → r8 changes log
**Date:** 2026-06-29 · **Build:** r8 (RGB interior + PDF/X-1a, 308 pp, 104,707 w; r7 kept as history)
**Driver:** Tier-1 developmental fix from `book2-developmental-edit-2026-06-29.md` /
`book2-tier1-act-one-and-reveal-plan.md` (author-approved). No canon moved.

## What changed (two small edits, both in Act One)

### Part A — Act One front-pressure (Ch.3)
Inserted one new scene (~470 w) into Ch.3 ("Alive Is Not the Same as Safe"), between the
second-evening Raizen beat and the third-night answer. During the three-day wait, a scout reports
that the capital's patrols east of Hazel have **stopped drifting and begun to quarter the country
in a search grid**, nearer each pass. Viridia goes to the east rim, reads the ground with the sight
herself, and names to the council what the change means: the wait she thought was "made of nothing"
now has a **second clock** in it, enemy-driven, on a schedule the capital sets.
- **Effect:** the "closing window" becomes a *dramatized, external* clock before the Ch.6 patrol,
  instead of dread Viridia only narrates. Keeps her **active** (she reads the track and names it).
- **Sets up, does not pre-empt, Ch.6:** this is a pre-contact *probe* (a tightening search), smaller
  than Ch.6's first true breach (the patrol that "walks a heading," the seer, Hiram taking the
  blade). The grid narrowing here is what later sharpens into the Ch.6 heading. No contradiction.

### Part B — develop-not-restate the moral question (Ch.5)
Added a short connective passage (~55 w) to Ch.5's world-mending meditation that explicitly marks it
as a **rung above** Ch.3: Ch.3 was the thought taken out in the dark and *banked unsure*; the rowan
proof in Ch.5 "takes the guess out of it" and turns it from a thought she can bank into a fact she
must live beside. Makes the Ch.3 → Ch.5 → Ch.9 climb legible as escalation rather than echo.
- **Ch.9 untouched** (the developed payoff — Amber's "I'm on the sheet" + Jazen's mirror — remains
  the strongest beat in the book).

## Gates (all green)
- `style_check.py --max-emdash 4`: **RESULT: clean** (Ch.3 em-dash 1, Ch.5 em-dash 2).
  Four new cross-chapter phrase collisions introduced by the Ch.3 insertion were varied to clear
  ("blind men feeling along a wall" vs Ch.6; "the way she read" vs Ch.13; "stood at the rim" vs
  Ch.7/9; "read the trot the way she read everything").
- `grammar_check.py`: **RESULT: clean**.
- `rhythm_check.py`: book-wide flags **16 → 16** (net-neutral). Ch.5's one flag remains on the
  pre-existing sanctioned "the severing was not one tree" anaphora line; the new Ch.3 scene adds
  no rhythm flags.

## Canon / continuity
- **No canon moved.** Word floor (85k) clear at 104,707. Six-weeks-at-Hazel timeline, Alice
  Pembrook, the search-then-breach escalation, and the Ch.9 payoff all intact.
- Viridia stays in-register: the careful face, grief inward (no public weeping; this round adds no
  break), the cold-working-part reading the patrol — all consistent.

## Book-Three cross-check (required: Book One/Two are upstream canon)
- Both edits are confined to Book Two's own Act One interior/Act-One pressure and touch **no element
  Book Three reuses**. Book Three opens a year+ later and depends on Book Two's *outcomes* (the
  rebirth, the cure, Alice freed/changed, the void-rim seed) — none of which are altered here. The
  new Ch.3 scout-probe and the Ch.5 framing clause introduce no new names, places, or rules.
- **No Book-Three continuity touchpoint.** No `continuity-guardian` retcon needed downstream.

## Deliverables
- `delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-r8.pdf` (RGB, 308 pp)
- `delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-r8-PDFX1a.pdf`
- r7 builds retained as history.
