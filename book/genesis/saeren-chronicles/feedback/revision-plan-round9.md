# Revision Plan — Round 9 (Hazel Academy): r8→release polish

Supersedes `revision-plan-round8.md` (that scoping was written before r8 was consumed
by the title refresh). Drives the build to **r9**. Source: `beta-feedback-r8-2026-06-24.md`
(refined reviewer pass) + the chapter-by-chapter r7 read.

This is a LINE/PACING polish — no new plot, no canon change. "Very close to publishable."

## Hard constraints (unchanged)
- Canon guardrails absolute (Alice PEMBROOK, JAZEN, rose-tinted spectacles, grief-inward/
  no one sees her cry, trains+motorcars, no houses).
- **Word floor ≥ 85,000.** Current ~93,693 — so the requested mid-book "trim ~3–5%"
  (~2,800–4,700 words) is SAFE and will NOT breach the floor. This is the one round where
  net subtraction is allowed and wanted. Re-check total after.
- Style gate CLEAN (`style_check.py`, em-dash ≤ 4/chapter); `rhythm_check.py` clean.
- Ch.16–18 touched LAST + LIGHTEST (most-praised, Book-Two-load-bearing). Climax = clarity
  only, no causality change.
- Every change logged in `book1-r9-changes.md`; `continuity-guardian` vs Book Two on any
  canon-touching edit before finalizing.
- Bump `REVISION` r8 → r9 BEFORE rebuilding.

## Punch-list (priority order, mapped to reviewer notes)

### P1 — global filtering-word + sentence-variety pass (reviewer Priority #1)
- "filed/watching/observing" echoes: down to occasional, but kill the remaining
  formulaic reappearances — ESPECIALLY the first 10–15 pages of Ch.1 (reviewer flags the
  motif there explicitly). Leave ONE load-bearing instance per scene.
- Filtering verbs ("she felt / she realized / she noticed") — trim in tense beats; let the
  perception land unmediated. Hot spot: the dragon assembly (Ch.2–4) — heighten Viridia's
  risk calculation WITHOUT the filter.
- Split the long winding sentences in the Ch.1 arrival/hallway sections for rhythm; add
  short plain sentences for contrast. Run `rhythm_check.py`.

### P2 — mid-book montage trim, ~3–5% (reviewer's "BIGGEST remaining opportunity")
- Ch.6–12: identify blending lesson/daily-life beats. Cut redundant training beats.
- Where a scene earns its place, INFUSE immediate personal/emotional cost or interpersonal
  friction instead of cutting (reviewer offers either/or). Net target: ~2,800–4,700 words
  lighter, brisker, no interchangeable scenes.
- Ensure info-via-dialogue serves immediate tension, not a pause for exposition.

### P3 — show-don't-tell in early dialogue/exposition (Ch.2–5)
- A few spots still state feelings/rules directly (Alice's backstory; early magic
  explanations). Convert the most on-the-nose to action/reaction.

### P4 — side-character distinction (both reviewer passes)
- Early scenes (Ch.2–5): give 1–2 blurring classmates/teachers a fixed trait/quirk —
  PLANT it for later payoff.
- Later chapters: give a few recurring side characters one sharper defining moment or
  voice tic each. No new characters.

### P5 — stakes-timing + climax clarity (CAREFUL)
- Verify key revelations (Chancellor/institutional pressure) don't feel convenient in
  TIMING — adjust setup only, not events; check against Book Two first.
- Climax (Ch.16–18): tighten descriptive sentences in high-tension moments for clearer
  choreography. No causality change.

### P6 — loose-thread audit + back matter
- Confirm the deliberately-open sequel threads read as INTENTIONAL, not unresolved:
  magic secrets, bonds, the family-tree name (note: its Ch.2 spellbook vehicle burns in
  Ch.16 — confirm the plant still has a home or flag to author).
- Back matter: OPTIONAL short teaser excerpt or author note for series momentum —
  AUTHOR DECISION before adding (and would pull from Book Two — coordinate).

## Process / gates (every chapter touched)
1. Edit → `python3 tools/style_check.py` (RESULT: clean, em-dash ≤ 4).
2. `python3 tools/rhythm_check.py` (no flat triplets / unsanctioned anaphora).
3. `wc -w manuscript/chapters/chapter-*.md` — total ≥ 85,000 after the trim.
4. `continuity-guardian` vs Book Two on canon-touching edits (+ reviewer Priority #3:
   full magic-rules/timeline continuity check).
5. Log each change in `book1-r9-changes.md`.

## Finalize
- Bump `REVISION` → `r9`.
- `python3 tools/assemble_manuscript.py` → `full-manuscript-r9.md`.
- `python3 tools/build_pdf.py` → r9 RGB interior; `bash tools/make_pdfx.sh` → r9 PDF/X-1a.
- Reviewer Priority #4: proof the r9 PDF for widows/orphans + chapter-opener consistency.
- Update STATE.yaml + root CLAUDE.md status.
