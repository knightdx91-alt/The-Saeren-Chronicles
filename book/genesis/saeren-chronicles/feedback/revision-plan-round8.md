> **SUPERSEDED by `revision-plan-round9.md`** (r8 was consumed by the title
> refresh; the prose polish now builds to r9). Kept for history.

# Revision Plan — Round 8 (Hazel Academy): r7 beta polish

Source: external chapter-by-chapter beta read of the r7 manuscript (2026-06-24).
Scope: ONE focused polish pass. No new plot, no canon change. Build → **r8**.

## Hard constraints (do not violate)
- Canon guardrails absolute (see root CLAUDE.md). Alice = PEMBROOK, JAZEN, rose-tinted
  spectacles, Viridia grief-inward / no one sees her cry, trains+motorcars, no houses.
- **Word floor ≥ 85,000.** Current build is 85,045 — almost no slack. Every trim MUST
  be offset by deepening a beat elsewhere; net words must stay ≥ 85,000. Do NOT cut
  below floor to satisfy "tighten."
- Style gate stays CLEAN (`python3 tools/style_check.py`, em-dash ≤ 4/chapter as built).
- Ch.16–18 (climax/escape/hinge) are the most-praised + Book-Two-load-bearing —
  touch LAST and LIGHTEST. Confirm any climax edit against Book Two first.
- Every change logged in `feedback/book1-r8-changes.md` for Book-Two cross-check.
- Bump `REVISION` r7 → r8 BEFORE rebuilding the PDF.

## Punch-list (priority order)

### P1 — "filed X" / internal-filtering tic (most-cited across ALL external reads)
- Dedicated sweep, not vibes. Run `style_check.py` tic report; grep `filed`, "the cold
  working part", recursive "the whole of it", "watching/filing" clusters.
- Target: ≤ one load-bearing instance per scene. Prior rounds (r6/r7) thinned the worst;
  the reviewer still feels it, so go one level deeper — vary the *construction*, not just
  the word (replace some "filed it away" with the action it implies).
- Leave the high-performing emotional chapters (per Book-Two notes: 9/11/16/19 analog)
  lightest.

### P2 — mid-book "mosaic" drag (the lesson/day-blend chapters, ~Ch.6–13)
- Identify scenes that blend (training montages, repeated class days). Compress the
  weakest 5–8% — but REINVEST the words into specific interpersonal friction / a small
  failure (reviewer explicitly asks for "more small failures to raise tension").
- Net effect: same/greater word count, fewer interchangeable scenes, higher tension.
- Condense ONE training sequence (reviewer's specific note). Vary sentence rhythm in
  introspective passages (run `rhythm_check.py`).

### P3 — side-character distinction (cheap, high-impact)
- Classmates blur in class scenes. Give each recurring blurring classmate ONE fixed
  sensory/verbal tag and use it consistently. No new characters.

### P4 — early-chapter specifics (Ch.1–3)
- Ch.1: tighten hallway/paintings section ~10–15% for momentum (reviewer). Keep the
  kitchen flashback intact (praised). Ensure the copper-haired-girl laugh misread has a
  clear later payoff — verify the payoff line exists; if thin, sharpen it.
- Ch.2–3: trim Alice's backstory exposition / homesickness talk slightly; convert one
  expository beat to action. Heighten sensory detail on the "thirsty"/hungry magic in the
  spellbook scene. Make the dragon-incident consequences ripple (a line or two of shifted
  school atmosphere after).

### P5 — mid/late stakes & climax clarity (CAREFUL)
- Confirm stakes escalate consistently (Chancellor's attention, personal cost of power) —
  add a beat only if it doesn't contradict Book Two.
- Climax: one light pass for action clarity amid the prose style. Do NOT alter causality
  (the fixed Ch.16 joint) or antagonist motivation without author sign-off + Book-Two check.

## Items deliberately NOT done (flag, don't free-hand)
- "Antagonist motivation feels earned" — vague; risks contradicting Book Two's Meros/
  Chancellor thread. Needs author scope + Book-Two read before any change.
- The structural passivity note is already addressed in round 6 (agency conversions); not
  re-opened here.

## Process / gates (every chapter touched)
1. Edit → `python3 tools/style_check.py` (RESULT: clean, em-dash ≤ 4).
2. `python3 tools/rhythm_check.py` (no flat triplets / unsanctioned anaphora).
3. `wc -w manuscript/chapters/chapter-*.md` — total ≥ 85,000.
4. `continuity-guardian` against Book Two on any canon-touching change.
5. Log the change in `feedback/book1-r8-changes.md`.

## Finalize
- Bump `REVISION` → `r8`.
- `python3 tools/assemble_manuscript.py` → `manuscript/full-manuscript-r8.md`.
- `python3 tools/build_pdf.py` → r8 PDF (keep r7 as history).
- Update STATE.yaml status + root CLAUDE.md status note.
