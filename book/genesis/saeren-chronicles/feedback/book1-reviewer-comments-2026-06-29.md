# Book One — Reviewer Line-Edit (Eilidh Locherty) — captured 2026-06-29, **refreshed 2026-07-01**

Source: Google Doc "Saeren-Chronicles-Book-One-6x9-interior-r14". All comments + tracked
changes are confined to the **front-matter dedication and Chapter One's opening scene**
(the 18 individual chapter docs have zero comments; prose tracked-changes stop after the
first `* * *`). This is a close edit of the OPENING — a sample — but the patterns are
consistent and are logged as the repo-wide "Recurring craft mistakes" guardrail in root `CLAUDE.md`.

**Refresh note (2026-07-01):** re-pulled the live doc via Google Drive. It now carries **28
comment threads** (was captured as 23) — **25 OPEN, 3 RESOLVED**. Full categorized list below.

## What KIND of issues were these? (the author's question: "grammatical or what?")
**Overwhelmingly NOT grammatical.** Of 28 comments, **exactly ONE is a true grammar issue**
(a dangling modifier). The rest are comprehension/craft. Breakdown by primary category:

| Category | Count | What it means |
|---|---|---|
| **Clarity / comprehension** | 11 | vague or unanchored referents ("Known what?", "deep water"), identity ("Bella is her mother?"), unclear reference |
| **Pacing / over-packed sentences** | 5 | "doing a lot in one breath", "we don't need to say everything", tighten + split |
| **Praise (not a fix)** | 4 | dedication, the toast-joke concept, the school atmosphere, "hahahaha" |
| **Dialogue mechanics** | 3 | who is speaking, new line for a new speaker, name naturalness in dialogue |
| **Word choice / precision** | 3 | "the wax" → "its wax seal"; "of" vs other; mouth/throat/tongue |
| **Grammar (true)** | **1** | a dangling modifier on the "grey stone" school sentence (#6) |
| **Structure** | 1 | unmarked kitchen→school time jump; consider a short prologue (#8) |

So: **1/28 grammar; the other 23 non-praise notes are clarity, pacing, dialogue, and word-choice** —
i.e. *readability and craft, not correctness.* This is the empirical basis for the "Recurring craft
mistakes" checklist (the root cause is comprehension-at-the-expense-of-voice, so the fix is CLARIFY,
not flatten).

## Comment layer — all 28 threads (verbatim, tagged) [C=clarity · P=pacing · D=dialogue · W=word · G=grammar · S=structure · ★=praise]
1. **[C]** "Known what?"
2. **[W]** "At the back of her mouth (or throat). OR on her tongue. Would work best here. :)"
3. **[C]** "Do we know what symbol?"
4. **[P]** "I've trimmed the sentence back so the focus stays on … the numbness rather than the physical action of standing."
5. **[W]** "I'd tweak 'the wax' to 'its wax seal' because the original phrasing makes the image slightly vague. The sigil would be pressed into the wax seal specifically, not just wax in general."
6. **[G]** "I adjusted the start … to avoid a dangling modifier … 'grey stone' left the sentence without a clear subject, so I reworked it … I love the atmosphere. The grey stone, blank windows, and bird stopping after only two notes give the school an almost gothic stillness."
7. **[P]** "I made a few tweaks to this to help with the way it reads. Thoughts?"
8. **[S]** "Everything here and up could be a little prologue … it's a huge jump where we don't know the length of time … This can be very confusing. … I'd say the proper start of the book is Viridia looking up at the building."
9. **[★]** "A very important message!"
10. **[C]** "This reads as she's actively holding her eyes. … Gaze would help clarify that."
11. **[P]** "I adjusted wording here … to tighten. We could imagine the smoke thinning while reading. We don't need to say everything. I also split the sentences to help readability."
12. **[C/★]** "I really like the running joke with the burnt toast being called 'character.' … I did find the original dialogue a little confusing … 'Eat the character. It builds character' made me pause over whether 'character' meant the burnt colour, the toast, or the joke itself."
13. **[D]** "Flagging just because of the dialogue above."
14. **[D]** "Did Leon say this? If so, it is fine as is. If it isn't, it should be on a new line and make it clear who said it. EG — 'Eat the crusts,' (character) said, 'It builds character.'"
15. **[C]** "I'm confused by double character here."
16. **[D]** "Is this her dads name? … I don't think a mother would say his name when talking to her daughter. Instead … 'Your father' here and using 'Leon' in the next dialogue … It would read more smoothly."
17. **[P]** "Adjusted here as I feel it'd read smoother this way with the pacing you've introduced."
18. **[C]** "Do we (or should we) know his name or is this not relevant at this time?"
19. **[★]** "hahahaha"
20. **[C] (RESOLVED)** "As a reader, I don't quite understand what you mean by 'deep water' here?"
21. **[C]** "Knew what?"
22. **[C] (RESOLVED)** "Bella is her mother?"
23. **[C]** "Might help visualise a bit better? :)"
24. **[P]** "This sentence is doing a lot in one breath and it might be helpful to tighten it … I have suggested the words to change or delete to tighten it up :)"
25. **[★]** "I love the visualisation here! A very simple way to give context on family life :)"
26. **[C] (RESOLVED)** "I'm guessing you are referring to family."
27. **[W]** "This intrigues me as I am curious what makes it 'ordinary'. I changed it to 'of' because it will help strengthen the first line that tiny bit more."
28. **[★]** "I love this dedication."

## Root pattern
Dense, atmospheric, "literary" prose that serves the voice at the expense of the reader's
plain comprehension. Reviewer praises the atmosphere, the dedication, and the toast-joke
*concept* — so the fix is to CLARIFY, not flatten. Matches the standing Book One/Two
external note ("too quiet / over-narrated / slow").

## Tracked-edit layer — AUTHORITATIVE (parsed from the .docx, 2026-06-29)
The exported `.docx` (saved in `reviewer-edits/`) was parsed directly from its Word
insertion/deletion markup (55 ins / 55 del). This is the CLEAN source of truth and CORRECTS
the earlier `read_file_content` API read, whose garbled merged anchors had several edits
backwards. Format: ~~old~~ → **new**. (14 changed paragraphs; all in Ch.1's first two scenes.)

**Edit-layer taxonomy (re-parsed from the .docx XML, 2026-07-01 — settles "were a lot of them word
endings?": NO, ~4 of ~55).** Counts of the ~55 tracked insertions/deletions by type:
| Type | ~count | Examples |
|---|---|---|
| Sentence splits (punctuation/caps) | ~10 | run-ons broken at ". S…", ". H…", ". It…" |
| Word swaps (precision) | ~8 | like→of, had come→went, stared up at→stared at, one big→his big |
| Phrase deletions (tighten/over-narration) | ~6 | cut "It meant the opposite.", "for the rest of her life.", "while the smoke thinned" |
| Article/possessive precision | ~5 | her chair→the chair, her→his, the→his |
| Connective variation | ~4 | and→then, while/as swaps |
| **Verb-form / word-ending** | **~4** | see below |
| Name standardization | ~2 | "her mother said"→"Bella said" |

Word-ENDING / verb-form (the author's specific earlier question — these are tense endings, NOT plural-s;
no plural-s fix appears in Ch.1). Only ~4 of the ~55 edits, i.e. a small minority — the dominant edits
were sentence-splitting and tightening, not morphology:
- ~~looked~~ → **look** ("she had not looked up" → "she didn't look up") — dropped **-ed**
- ~~smelling~~ → **smelled** ("smelling of soap" → "smelled of soap") — **-ing → -ed**
- ~~he'd~~ → **he** (dropped contraction)
- ~~has invented~~ → **invented** (dropped auxiliary; present-perfect → past)

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

Comment-only fix also applied: "held Viridia's eyes" → "held Viridia's **gaze**" (comment #10).

Capitalization/punctuation: sentence-start caps after splits (grey→Grey, tall→Tall); added commas
("flat, colorless grey"); `said , without` → `said without`; em-dash → comma before "not the stillness of rest."

## Action taken
- Added "Recurring craft mistakes — NEVER repeat" to root `CLAUDE.md` (auto-loads every
  session, all three books) — checklist A (structural/over-narration) + B (line-craft tics).
- Open follow-ups (author's call):
  1. Apply Eilidh's opening-scene fixes to the actual Book One Ch.1 (separate cleanup pass).
  2. The 3 RESOLVED threads ("deep water", "Bella is her mother?", "referring to family") were
     comprehension gaps the author has since addressed in the doc.
