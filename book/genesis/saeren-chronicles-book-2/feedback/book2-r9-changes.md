# Book Two — r8 → r9 changes log (LINE-BY-LINE EDIT, in progress)
**Started:** 2026-07-01 · **Mandate:** literary-preserving line edit (author directive), driven by the
"Recurring craft mistakes" checklist + the three gates + **the LanguageTool tier per chapter** (the
verb-form/tense/dangling class the Book One reviewer caught). Bump was r8 → r9 at the start of the pass;
**rebuild (assemble + PDF) happens once, at the END, after all 20 chapters.** Keep r8 builds as history.

Per-chapter gate protocol (all must pass):
- `style_check.py --max-emdash 4` → RESULT: clean
- `grammar_check.py --file <ch>` → RESULT: clean; split ≥1 of its longest sentences per scene
- `grammar_check.py --file <ch> --languagetool` → apply real tense/verb-form/dangling fixes, ignore
  voice false-positives
- `rhythm_check.py` → no NEW flat triplets vs the r8 baseline (book-wide 16)

---

## Chapter 1 — "The Box of Invisible Air" ✅ DONE
**LanguageTool:** grammatically clean — the 3 tier-2 warnings are false positives on deliberate voice
("The *this* was a wall"; "knees up" ≠ "knees-up"; Amber's colloquial "we none of us"). No verb-form or
dangling issues (unlike Book One Ch.1, which had them).

**Edits (all sentence-craft; no canon, no plot, voice preserved):**
1. Split the silver-bun council-member sentence (106 w) into three — the descriptor, "She sat very
   straight and did the arithmetic…", and "Viridia trusted her least…".
2. Split the "She had gone to the town hall…" run-on (91 w) into three, then varied the openings so it
   is not a triple "She had…" anaphora ("She had gone…" / "Coming in at the end of an argument, she
   made herself small…" / "It was a thing she understood by then…").
3. Split the "She put it away the way she banked her core…" sentence (80 w) into three (colon list +
   two sentences).
4. Cleared a cross-chapter repeat the edit introduced ("had learned by now" [1,7,8] → "understood by then").

**Result:** longest sentence now 72 w (the deliberate opening "bracing" sentence, left intact). All four
gates clean; book-wide rhythm unchanged at 16 (ch1's one flag is the pre-existing sanctioned
"The blacksmith's shed… The long table…" list). Word count 5,045 → 5,040.

**Deliberately NOT changed:** the "banking / count / small true things / careful face" motif density
(these are the book's deliberate, allowlisted motifs — de-tic only where incidental, not here); the
praised atmospheric opener (only its one over-long tail sentence was left as the deliberate 72-w beat).
