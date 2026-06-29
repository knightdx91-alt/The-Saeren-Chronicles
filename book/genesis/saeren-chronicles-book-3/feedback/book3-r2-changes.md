# Book Three — r1 → r2 changes log
**Date:** 2026-06-29 · **Build:** r2 (RGB interior + PDF/X-1a, 328 pp, 112,205 w; r1 kept as history)
**Driver:** Tier-1 developmental fix from `book3-developmental-edit-2026-06-29.md` /
`book3-tier1-denouement-compression-plan.md` (author-approved).

## What changed (one structural edit; no canon moved)

**Compressed the four-chapter denouement to two.** The book was 22 chapters; it is now **20**.
- **Ch.19 unchanged** (aftermath at the cave mouth, Drake's farewell, first night of the watch).
- **Former Ch.20 + Ch.21 + Ch.22 merged into a single closing chapter (new Ch.20,
  "A Place Where a Core Should Be").** ~14,750 w → ~7,900 w.
- Deleted `chapter-21.md` and `chapter-22.md`.

### Redundancy removed (each beat now appears once)
- The "asked to rule → she refuses" full scene: was effectively staged in former Ch.20 (city men)
  on top of Ch.3 (Vale) / Ch.12 (Lest). Kept once (new Ch.20) with Amber's series-answer
  ("the difference is the no").
- The "wall at evening / the no as discipline / borrowed world / column-with-no-bottom" meditation:
  was delivered in full in former Ch.20, again Ch.21, again Ch.22. Now stated once, folded into the
  single ending movement.
- The "raise a hand to Amber's lit doorway" image: closed former Ch.20, recurred Ch.21, framed
  Ch.22. Now used once, paid off by Amber walking up the slope (the stronger Ch.22 beat).
- Amber's mortality / the grey at the temple: former Ch.21 (solo) + Ch.22 (Amber hands it over).
  Kept the Ch.22 version only.

### Beats preserved (once each, in order)
First weeks / the bridge decided from below → the five city men + the active refusal + Amber's
"it's the no" → roll-call (Drake north; Dangris released, "we will come again"; Lor-ar quiet;
Amber/Alice/Raizen stay) + Alice's laugh returned → time-jump to the second spring → Raizen the
span-equal (the column with no bottom / the stair you're on / "just with you", the one sanctioned
private softness, **no full weeping — guardrail held**) → Amber hands over the grey → the earned
ending stillness ("it felt, this time, like an ending — the whole of it") → **the void/Fen finale
kept VERBATIM** (the lab, Fen draws the symbol, the tentacle, the severed end, he runs; cut to
Viridia feeling "a place where a core should be" — unexplained, the last line).

### Line-level (4 phrasings adjusted to clear the cross-chapter repeat gate)
The merge lightly reworded a few kept passages, creating new collisions with earlier chapters.
Reverted/varied four phrases in the new Ch.20 (denouement only; the verbatim finale untouched):
"neither of them said anything" → "the two of them said nothing at all"; "heard herself say it
and" → "heard it as she said it and"; "deaths with no wound" → "killings that left no wound";
"all the way down. The" → "all the way down now. The".

## Gates (all green)
- `style_check.py --max-emdash 4`: **RESULT: clean** (Ch.20 em-dash 2, simile 1.0/1k, adverb 8.2/1k).
- `grammar_check.py`: **RESULT: clean**.
- `rhythm_check.py`: book-wide flags **34 → 30** (net reduction); the single Ch.20 flag is the
  deliberate "Not very nearly. The whole of it." anaphora carried verbatim from the original
  finale — sanctioned, not a flat reflective triplet.

## Canon / continuity
- **No canon moved** — this is subtraction + reordering of existing beats. Word floor (95k) clear
  at 112,205. Title of the final chapter retained ("A Place Where a Core Should Be").
- Guardrails verified intact in the merged chapter: grief inward / no public weeping (only the
  sanctioned private Raizen softness, no full break); the void/Fen finale unexplained (no
  Masters/void-woman); Raizen human, dark ordinary eyes, the doorpost; source = physical Bk1
  cavern; Horrors receded not killed; world borrowed not owned; sixteen.
- Book-Two continuity touchpoints: none introduced or altered.

## Deliverables
- `delivery/production/Saeren-Chronicles-Book-Three-6x9-interior-r2.pdf` (RGB, 328 pp)
- `delivery/production/Saeren-Chronicles-Book-Three-6x9-interior-r2-PDFX1a.pdf`
- r1 builds retained as history.
