# Book One — Reviewer Line-Edit (Eilidh Locherty) — captured 2026-06-29

Source: Google Doc "Saeren-Chronicles-Book-One-6x9-interior-r14". All comments + tracked
changes are confined to the **front-matter dedication and Chapter One's opening scene**
(the 18 individual chapter docs have zero comments; prose tracked-changes stop after the
first `* * *`). This is a close edit of the OPENING — a sample — but the patterns are
consistent and are now logged as the repo-wide "Recurring craft mistakes" guardrail in the
root `CLAUDE.md`.

## Root pattern
Dense, atmospheric, "literary" prose that serves the voice at the expense of the reader's
plain comprehension. Reviewer praises the atmosphere, the dedication, and the toast-joke
*concept* — so the fix is to CLARIFY, not flatten. Matches the standing Book One/Two
external note ("too quiet / over-narrated / slow") and the round-6 "over-narration trimmed."

## Comment layer (23 threads, all Eilidh Locherty)
Praise (not fixes): dedication; the toast-joke concept; the school atmosphere ("gothic
stillness"); "Just be careful who you let see you do it."

Fixes, grouped:
- **Over-packed sentences / pacing** — "doing a lot in one breath"; "we don't need to say
  everything"; repeated tightening + sentence splits. (anchors: father-at-stove sentence;
  "smelled of…"; the "warm room / smoke thinned / kettle ticked" sentence; school-description.)
- **Vague / unanchored phrasing** — "she always knew" → *knew what?*; "deep water" → *don't
  understand*; "held Viridia's eyes" → should be **gaze** (reads as literally holding eyes).
- **Cleverness over clarity** — the "character"/burnt-toast gag: liked the idea but
  "Eat the character. It builds character." made her reparse what "character" means; double
  "character" hard to read; suggested "It's not burnt." as the plain alternative.
- **Names** — dropping "Leon" into the mother's dialogue is unnatural; use "your father" and
  reserve "Leon"; be consistent about whether/when we learn the father's name.
- **Scene/time jump** — kitchen → arrival-at-school is "a huge jump… very confusing"; consider
  the kitchen as a short prologue ("___ Days Ago") to mark the gap.

## Tracked-edit layer — AUTHORITATIVE (parsed from the .docx, 2026-06-29)
The exported `.docx` (saved in `reviewer-edits/`) was parsed directly from its Word
insertion/deletion markup (55 ins / 55 del). This is the CLEAN source of truth and CORRECTS
the earlier `read_file_content` API read, whose garbled merged anchors had several edits
backwards. Format: ~~old~~ → **new**. (14 changed paragraphs; all in Ch.1's first two scenes.)

Word-ENDING / verb-form (the author's specific question — these are tense endings, NOT plural-s;
no plural-s fix appears in Ch.1):
- ~~looked~~ → **look** ("she had not looked up" → "she didn't look up") — dropped **-ed**
- ~~smelling~~ → **smelled** ("smelling of soap" → "smelled of soap") — **-ing → -ed**
- ~~he'd~~ → **he** (dropped contraction)

Wording / word-swaps:
- ~~smelled like~~ → **smelled of**; ~~had come~~ → **went**; ~~loose on her heels~~ → **loose at the heels**;
  ~~past the elbow~~ → **past his elbow**; ~~one big hand~~ → **his big hand**; ~~her chair~~ → **the chair**;
  cut ~~particular~~; ~~her mother said~~ → **Bella said** + ~~Bella was at the table~~ → **Her mother was**
  (name standardized: proper name in the tag, "her mother" in narration); ~~Leon has invented~~ → **Leon invented**;
  ~~stared up at~~ → **stared at**.
- Connectives varied: ~~and kissed~~ → **then kissed**; ~~two notes and stopped~~ → **two notes then stopped**;
  kettle clause "while…as" swapped to "as…while".

Sentence splits / restructures (the over-packed habit):
- "...beside her, and she had not looked up, and somehow she always knew" → three sentences.
- "...ran him through, and her mother laughed" → split at "through. Her mother laughed".
- "...ticked as it cooled, and her mother reached" → split; **cut "the smoke thinned"** ("we don't
  need to say everything"). ~~Viridia had never had a word~~ → **There had never been a word**; cut "It meant the opposite."
- School sentence rebuilt to fix the dangling modifier: "...by Hazel Greenwich. It looked like the
  sort of place designed to make you feel small before it had spoken a single word to you. It was
  built with grey stone…" (~~it was impressive, in the way of things that are~~ removed).

Two JUDGMENT-CALL edits flagged to the author (applied, easily reverted):
- ~~"without seeming to decide to do it"~~ → **"instinctively"** — this REVERSES our own guardrail #8
  (prefer shown action over -ly adverbs). Applied per reviewer, but it is the one edit that fights the guardrail.
- ~~"She thought about it for the rest of her life."~~ → **"For a while, it was."** — softens the
  foreshadow at the scene break; a real tonal change.

Comment-only fix also applied: "held Viridia's eyes" → "held Viridia's **gaze**" (reviewer comment #19).

Capitalization/punctuation: sentence-start caps after splits (grey→Grey, tall→Tall); added commas
("flat, colorless grey"); `said , without` → `said without`; em-dash → comma before "not the stillness of rest."

## Action taken
- Added "Recurring craft mistakes — NEVER repeat" to root `CLAUDE.md` (auto-loads every
  session, all three books) — checklist A (structural/over-narration) + B (line-craft tics).
- Open follow-ups (author's call):
  1. Apply Eilidh's 17 opening-scene fixes to the actual Book One Ch.1 (separate cleanup pass).
  2. If the s-ending question matters, export the `.docx` to read tracked changes cleanly.
