# Book Three — Tier 1 execution plan: compress the denouement (Ch.20–22 → one closing chapter)
**Date:** 2026-06-29 · **Source diagnosis:** `book3-developmental-edit-2026-06-29.md`
**Status: AWAITING AUTHOR SIGN-OFF before any prose is rewritten** (per the project rule that the
cut/keep list is approved first). This is the keep/merge/cut ledger, not the rewrite.

## Goal
Climax is Ch.18; the watch is taken up Ch.18–19. Today the resolution runs **four** chapters
(19, 20, 21, 22 ≈ 21,700 w, ~18% of the book) and restates one earned thesis three times across
three near-identical "high wall at evening" chapters before the Fen/void finale. Target: **two**
resolution chapters —
- **Ch.19 stays as-is** (aftermath at the cave mouth: lifting the hand from the pool, the company,
  Drake's farewell, the first night of the watch). Distinct, earned, not repetitive. **No change.**
- **New Ch.20 ("The New Shape" / retitle optional)** = a single consolidated closing chapter that
  states the thesis once, lands each farewell once, and fires the void-socket finale clean.

Result: ~119k → ~111–113k; resolution ~18% → ~11%. Word floor (95k) unaffected. The trilogy's
most important forward hook (the void-socket) becomes the **only** note of un-resolution, instead
of competing with three prior "last-page" evenings.

## What recurs across 20/21/22 (the redundancy being removed)
1. **"Asked to rule → says no"** as a full scene: Ch.20 (the five city men). (Ch.3 Vale and Ch.12
   Lest already carried this; Ch.20 restates Ch.3's logic to the answer she's already reached.)
2. **The wall-at-evening "no as discipline / borrowed world / column-with-no-bottom" meditation:**
   delivered in full in Ch.20, again Ch.21, again Ch.22.
3. **"Raise a hand to Amber's lit doorway":** closes Ch.20, recurs Ch.21, frames Ch.22.
4. **Amber's mortality / the grey at the temple:** Ch.21 (Viridia looks at it alone) and Ch.22
   (Amber walks up and hands it to her). The Ch.22 version is stronger — keep that one.
5. **Raizen the span-equal / "you don't have to do the dry face with me":** Ch.21. Excellent once.

## Keep / merge / cut ledger

| Beat | Now in | Disposition |
|------|--------|-------------|
| Lifting hand from pool; watch is portable not postural; company at cave mouth; Drake flies north (farewell); Dangris released; first night of the watch | Ch.19 | **KEEP — Ch.19 unchanged** |
| The five city men ask her to rule; she refuses | Ch.20 | **MERGE → keep as the new chapter's one external beat.** It is the best-dramatized "no" and it gives Amber the on-page "the difference is the no" answer. Trim its internal meditation (covered below). |
| Amber: "the difference isn't the wanting, it's the no" | Ch.20 | **KEEP** — this is the *answer* to the book's controlling question; it must land, once, here. |
| Who stayed / who went (Drake north, Dangris gone, Lor-ar quiet, Amber/Alice/Raizen stay) | Ch.20 | **KEEP, compress to a tight passage** — it's the roll-call the ending needs. |
| Alice's laugh returns at the bowls-of-water table | Ch.20 | **KEEP — relocate** as the chapter's warmth beat (YA-tone load-bearing). One instance. |
| Wall meditation: borrowed world / daily no / discipline-not-virtue | Ch.20 **and** Ch.21 | **CUT to ONE statement.** Keep the sharpest phrasing (the Ch.21 §"The difference was the no" passage is the cleanest); delete the Ch.20 and the second Ch.22 restatements. |
| Raizen counts the years / "how many will we watch go" / "the stair you're on" | Ch.21 | **KEEP, condense** — the span-equal scene is the emotional core of the resolution and the YA-warmth anchor. One pass. |
| Raizen "you don't have to do the dry face with me" | Ch.21 | **KEEP** (once) — it's the payoff of the sanctioned-break guardrail (she lets only Raizen see). |
| "Am I still myself" wall soliloquy (the eleven she lets die, the lease, world-borrowed) | Ch.21 | **CUT ~half.** This is the densest restatement of the thesis already stated in the city-men scene. Keep a few lines folded into the single retained meditation; cut the rest. |
| Amber walks up the slope, hands over the grey at her temple, "carry me when I'm gone, not before" | Ch.22 | **KEEP — this is the definitive Amber-mortality beat.** Supersedes the Ch.21 solo version (cut that one). |
| Final wall evening / "it felt like an ending — the whole of it" | Ch.22 | **KEEP as the chapter's penultimate movement** (the earned "last page" stillness) — but only once, here, not pre-echoed in 20 and 21. |
| **The low stone room: Fen draws the symbol, the tentacle, the severed end, he runs; Viridia feels "a place where a core should be"** | Ch.22 | **KEEP VERBATIM as the finale.** Untouched. This is the binding image; do not edit. |

## New chapter shape (single closing chapter, ~5,000–5,800 w)
1. **Spring on the watch (short open).** She trusts her arms now; lets spring be spring. (from
   Ch.22 open — strongest version of the "settled into the cost" note.)
2. **The five city men / the refusal / Amber lands "it's the no."** The book's controlling question
   gets its answer, dramatized, once. (from Ch.20, internal meditation trimmed.)
3. **Roll-call + Alice's laugh.** Who stayed/went, condensed; Alice warm all the way down. (from Ch.20.)
4. **Raizen on the wall: the column with no bottom / the stair you're on / "just with you."** The
   span-equal warmth beat. One pass. (from Ch.21, condensed.)
5. **Amber walks up, hands over the grey.** The definitive mortality beat. (from Ch.22.)
6. **The last evening / "it felt like an ending — the whole of it."** The earned stillness, stated once.
7. **The void-socket finale.** Fen, the room, the tentacle, the run; cut to Viridia feeling the
   place where a core should be. Verbatim. End.

## Constraints / gates (on execution, after sign-off)
- Voice-match Books One/Two; **bump `REVISION` r1→r2 BEFORE rebuild**; rebuild manuscript + PDF
  (RGB + PDF/X-1a); keep r1 as history; log in a `book3-r2-changes.md`.
- Gates: `style_check.py` RESULT clean + em-dash ≤4/ch; `grammar_check.py` RESULT clean;
  `rhythm_check` no flat triplets. Re-run after the merge (the "very long way off" motif density
  drops, which *helps* the gate).
- Continuity: nothing canon moves — this is subtraction + reordering of existing beats. Run a
  light `continuity-guardian` pass on the merged chapter vs the void-socket guardrail (Fen/tentacle
  unexplained; no Masters/void-woman) to confirm nothing was lost in the cut.
- **Do not touch** Ch.1–19 or the Fen finale text.
