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

## Chapter 2 — "The Thread Pulled Taut" ✅ DONE
**LanguageTool:** grammatically clean — the 3 tier-2 warnings are false positives on deliberate voice
("came in his own time"; the litotes "did not pretend not to see it"; the stylistic "there was a someone").

**Edits (all sentence-craft; no canon, no plot, voice preserved):**
1. Split the Ferro-climbing sentence (120 w) into three (the climb / the church-window sight / "Ferro thought…").
2. Split the "Behind her… the prismatic dragon lifted his head" sentence (~90 w) into two.
3. Split the closing doorway sentence (106 w) into two ("…something crueller in its place." + "It was a
   knowing she could not trust…").

**Left intact (deliberate / load-bearing):** Jazen's climactic speech ("You feel all of it at once and it
tears you…") — dialogue cadence; and the remaining long descriptive beats (Raizen's prismatic-core
reveal 96 w; Drake's descent 81 w; the "seen by a dragon, a death-lizard, a scout" list 77 w) — these
are voice-benchmark images, not run-ons to break.

**Result:** all four gates clean; book-wide rhythm unchanged at 16 (ch2's one flag is pre-existing);
em-dash 0. Word count 5,001 → 4,998.

## Chapter 3 — "Alive Is Not the Same as Safe" ✅ DONE
**LanguageTool:** clean — 1 warning, a false positive (Raizen's colloquial "all of yesterday").
**Edits:** split three over-packed sentences — the "*Calm hands.*… wrong detail to undo her" reflection
(split at the semicolon), the "She kept it, banked…" run-on, and the closing dawn-vigil sentence. No
canon/plot change; the r8 Act-One probe scene (search-grid) untouched. All gates clean; rhythm improved
(ch3 1→0 flags, book total 16). 5,308 → 5,306 w.

## Chapter 4 — "His Mother's Papers" ✅ DONE
**LanguageTool:** clean (0 warnings). **Motif density:** 1.7/1k (below median) — nothing to thin.
**Verb-form sweep:** no warranted changes (deliberate, correct tense).
**Edits:** split one over-packed sentence — the chart-reading sentence (the dateless-name reveal) at
"…did not fit. And there it was:" — keeping the deliberate accumulating "that… that… as though…" tail.
Left the closing doorway-montage sentence intact (deliberate atmospheric close). All gates clean; rhythm 16.

## Chapter 5 — "The Furnace and the Match" ✅ DONE
**LanguageTool:** clean (1 warning = false positive, "let her hand shake" ≠ "handshake").
**Motif density:** 2.4/1k (at median). **Verb-form:** no warranted changes.
**Edits:** split two compound sentences — the letter-writing sentence (varied the "She set out… She set
out…" to avoid anaphora) and the "thing under Viridia's ribs… went quiet at that." sentence. Left the
void-rim cosmic beat intact (deliberate Bk3 seed). The r8 reveal-laddering clause untouched. All gates
clean; rhythm net-neutral (16; ch5's one flag is the pre-existing "severing was not one tree" anaphora).
