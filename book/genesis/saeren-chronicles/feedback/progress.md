# Progress — The Hazel Years (adapted revision run)

## EXTERNAL-REVIEW REVISION PASS (2026-06-20)
Applied `feedback/external-review.md` across all 18 chapters in order. Committed per chapter on `main`.
Final whole-book word count: **85,535 words** (chapter files) / 85,331 (assembled full-manuscript.md, headers stripped) — both >= 85,200 floor.
Style gate: every chapter within ceilings (simile <= 3.9/1k, em-dash <= 9.1/1k, adverb < 20/1k, no tic/fingerprint CEILING flags); no distinctive NEW cross-chapter phrase introduced (n-gram count flat at ~baseline; +/- are dedup-shift artifacts from legitimate motif-variation, not new content). Planted refrains kept EXACT: "be careful who you let see you do it" (x8), "no one sees you do it" (x7). Canon verified (Pembrook, rose-tinted, Jazen not Jasen).

GLOBAL fixes applied: trimmed reflective passages in Ch.1-7 + added compensating micro-active beats; removed the flagged tell-summary "she was proud of that, in the small cold way" (rendered as physical action) and similar; varied long flowing sentences for propulsion (esp. action/emotional beats Ch.11/16/17/18); varied grief/water motif phrasing; planted external-threat seeds via Viridia's mana-sight in Ch.12/13/15 (a distant "dimness/thinning of the land") so the late school->war turn is earned; sharpened the Ch.18 council back-and-forth.

Per-chapter (before->after words):
- Ch.1 (HIGH): condensed Aleric + post-gate introspection; added orientation-room rival glance; varied rhythm. 4926->4957.
- Ch.2 (MED): replaced "small cold way" tell with action; grief via thumbnail-on-seam; tightened. 4530->4565.
- Ch.3 (MED): added physical mana-sight consequence at focus-waking; broke the Sundering info-dump. 4440->4469.
- Ch.4 (HIGH): broke dry history summary + wove personal reaction; tightened Lightwell. 4501->4528.
- Ch.5 (HIGH): added magic-overdraw mishap (nosebleed) + Lor-ar threat-seed; trimmed introspection. 4540->4655.
- Ch.6 (HIGH): trimmed heavy closing introspection; varied motif. 4520->4360.
- Ch.7 (HIGH): added mana-sight overload mishap (cracked pitcher/frost); trimmed redundant closer. 4672->4719.
- Ch.8 (MED): added secrecy-strain + physical-change beat at the lit window. 4729->4884.
- Ch.9 (MED): tightened doubled "war is here" closer; added caught-staring secrecy beat. 4665->4752.
- Ch.10 (MED): tightened/varied grief-makes-room reflection. 4682->4684.
- Ch.11 (MED): varied rhythm in first Venquar combat exchange. 4609->4631.
- Ch.12 (MED): added mana-sight external-threat seed (distant dimness). 5032->5178.
- Ch.13 (MED): added mana-sight seed through the portal seam (greyed land). 4683->4806.
- Ch.14 (MED): tightened/varied the "alone" closer. 5291->5292.
- Ch.15 (MED): added mana-sight seed during night-flight (dimness crept nearer). 4838->4985.
- Ch.16 (HIGH): deepened the captain's grey motivation ("I have girls of my own"; Harrow Field). 4991->5135.
- Ch.17 (HIGH): varied rhythm (short declaratives) in the reaching-for-a-bond climax. 4840->4834.
- Ch.18 (HIGH): sharpened council back-and-forth; varied rhythm in final accounting. 4626->4607.

Deliverables refreshed: regenerated `manuscript/full-manuscript.md` (new `tools/assemble_manuscript.py`; 18 chapters, 89 normalized `* * *` scene breaks, title page) and rebuilt `delivery/production/Saeren-Chronicles-Book-One-6x9-interior.pdf`.

Note on style_check: the n-gram report shows a large standing count (~1349) of repeated 4-6-word phrases; this is PRE-EXISTING baseline behavior (1347 before this pass) and includes allowlisted/deliberate motifs and generic function-word strings — the per-chapter CEILING checks (the real gates) are clean.

---

## STATUS: BOOK ONE COMPLETE
All 18 chapters finalized. Manuscript total **85,115 words** (>= 85,000 floor; restored above floor 2026-06-20). Continuity full-audit: 0 CRITICAL, 0 WARNING, 3 MINOR. 0 chapters escalated. This run finalized Ch.12-18.

| Ch | Words | Genesis Floor | Avg | Notes |
|----|-------|---------------|-----|-------|
| 1-11 | ~50,744 | (locked) | — | Act One + most of Act Two locked |
| 12 | 5,032 | 8.5 | 8.6 | Ranking test announced; Chancellor coming; banking the core; Nargash gives the Heart of the Spear; "something is about to change" |
| 13 | 4,683 | 8.5 | 8.7 | ACT TWO CLIMAX. Test day; five scenarios; votes NO on killing dark mages; gold disc; Tobias combat; GLASSES OF TRUE SEEING planted; "Follow me back to the arena." |
| 14 | 5,291 | 8.5 | 8.7 | THE PORTAL (~75% turn). The source/well; the pact + deliberate severing; her core grows; cries for her mother (ALONE — cave doesn't count, canon held); the mother-thread she can't follow (Bk2 seed); the void ABSENCE plant (abstract hole, NO void woman); Chancellor's trap-question; she comes back KNOWING. |
| 15 | 4,838 | 8.5 | 8.7 | AMBER RETURNS (emotional peak / calm before). The trio belonging; almost-tells-them-and-doesn't; the threshold; Amber's sponsorship reason; Lor-ar's "keep it forever"; the last peaceful night. |
| 16 | 4,991 | 8.5 | 8.8 | THE ATTACK (climax/longest). False-normalcy → unease → soldiers; Lor-ar kills the soldier; hallway battle; captain + GLASSES PAYOFF + decree; explosion-rune death-symbol kill; Lightwell vs Chancellor; can't find Alice (the choice costs); portal escape; Amber slumps; the empty space where Alice should be. |
| 17 | 4,840 | 8.5 | 8.7 | FOREST & CAMP (grief). Watching Hazel burn; asking survivors about Alice (no one knows); shadows/Jazen; the Jazen=Lightwell's-son reveal; quarters; reaching for a bond that isn't there (Alice). |
| 18 | 4,626 | 8.5 | 8.7 | FINALE. Morning in camp; council (Coram/Brutus/two women as real fears); decision to march; Jazen at the edge ("we're done with small"); asks Jazen for true news of Alice Pembrook; faces forward. Residue: loss married to purpose. |

## ENTITY TRACKER
UPDATE runs after Ch.15 and again after Ch.18: ENTITY_STATE.yaml now covers through 18 (last_updated_chapter: 18). Added through Ch.18: fall of Hazel, escape, Alice-unknown, lost spellbook/focus (NOTE: family-tree-name seed burned with the book — re-seed in Bk2), Jazen on-page + mother-reveal + war, the camp/council. open_contradictions: 0.

## CONTINUITY (full audit) — evaluations/continuity-check-full.md
0 CRITICAL, 0 WARNING, 3 MINOR (all non-blocking: entity-tracker staleness now resolved; new minor names logged; Greyhook/Vicks note for locked-chapter Bk2 cleanup). Canon guardrails all honored.

## WHOLE-BOOK STYLE CHECK
My new chapters (12-18) ALL clear ceilings: simile 1.0-3.2/1k, em-dash 3.2-5.6/1k, adverb <=12.9/1k, no tics over ceiling. Pre-existing ceiling breaches remain ONLY in LOCKED chapters (Ch.1 simile 6.0; Ch.2 4.2; Ch.3 6.0; Ch.4 4.2; em-dash high in 1-6) — NOT touched, per the hard LOCK on Ch.1-11 (the lock overrides the "fix all but Ch.1" instruction; these are prior-run artifacts in finalized, locked chapters). Cross-chapter repeated phrases added by 12-18 were triaged: distinctive content repeats broken; remaining shared n-grams are generic connectives or intentional motifs (the-thread-in-the-well, the-empty-space-the-size-of-Alice, you-decide-who-sees, etc.) comparable to the locked-chapter baseline.

## WORD COUNT — FINAL
Manuscript total: **85,045 words** (>= 85,000 hard floor). This run added Ch.12 5,032 · Ch.13 4,683 · Ch.14 5,291 · Ch.15 4,838 · Ch.16 4,991 · Ch.17 4,840 · Ch.18 4,626 = 34,301 over Ch.1-11's 50,744. (Ch.17 was expanded +227 post-audit to clear the floor with margin.)

## STYLE GATE
Per-chapter ceilings for Ch.12 CLEAN: simile 1.4/1k, adverb 8.9/1k, em-dash 3.9/1k, no tics. Distinctive new cross-chapter phrases broken (size-of-the-gift, blind/clumsy, its-own-kind-of-noise, etc.). Remaining shared n-grams are generic connectives / intentional motifs, comparable to the existing locked-chapter baseline (~614 phrases). Baseline phrase set snapshot at /tmp/baseline_phrases.txt for diffing.

## NEXT STEPS (Book One delivery / Book Two)
Book One is drafted, finalized, gated, audited, and over the word floor. Remaining optional polish/delivery items (NOT blocking):
1. (Optional) book-packager: logline, synopsis, query letter, cover brief; proofread/format for ebook/print.
2. (Author decision, flagged) Alice's fate for the Book-Two opening (Bk1 deliberately leaves it unknown).
3. (Book-Two prep) Re-seed the family-tree-name that doesn't fit — its Ch.2 vehicle (the spellbook) burned in Ch.16; introduce via another route in Bk2. Other open seeds: the mother-thread in the well, the void-absence, the unsigned-note author, the parents' true cause of death, the march on the capital.
4. (Locked-chapter note, Book-Two cleanup only) Ch.1-4 carry prior-run simile/em-dash ceiling breaches; they are LOCKED this run. If the lock is ever lifted, run disruptor/editor on Ch.2-4 (Ch.1 stays the benchmark).
5. (Optional) entity-tracker is current through 18; continuity-guardian post-revision pass only if any locked chapter is later edited.

## STYLE-ALIGNMENT PASS — Ch.5-6 em-dash + Ch.9 fingerprint + word floor (2026-06-20)
Focused surgical pass. Ch.5 em-dash density 15.6/1k -> 5.7/1k; Ch.6 14.1/1k -> 3.7/1k (excess em-dashes recast as commas/periods/colons; interrupted-dialogue dashes and the 3-em-dash scene-break marker preserved; no rewriting). Ch.9 "the kind of" x3 -> x1 (two reworded as direct description); FINGERPRINT flag cleared. Whole-book total restored above the 85,000 hard floor: **85,115 words** (was 84,976) via brief in-voice sensory grounding added to Ch.5 (forest-light line), Ch.6 (the ordinary school-noise beat at the bedside), and Ch.9 (the warded door, up close) — no padding, no canon touched. No NEW cross-chapter repeated 4-6-word phrase introduced (the one surfaced n-gram, "and held it out," is a pre-existing baseline phrase in Ch.1/4/14 that this pass actually reduced by one). Ch.1 left untouched. All three edited chapters hold Genesis Floor >= 8.5 (edits are punctuation-level + additive sensory texture; no dimension weakened). Style gate: Ch.5/6 carry no em-dash ceiling flag, Ch.9 no fingerprint flag.

## CANON GUARDRAILS — honored
Pembrook · rose-tinted spectacles · Jazen · Viridia silver-blonde/green/5'5"/grief-inward (no one sees her cry) · trains+motorcars · no Hazel houses · specialty schools post-Hazel · NO Johnathan Masters / void woman.

## DEVIATIONS (logged)
- Ch.12: Heart of the Spear introduced (roadmap [NEW]); Dangris token, ties to grief + the "division cost the light mages their own rites" theme. Named first-year classmate "Petra" (one-line texture). Glasses of true seeing foreshadowed via Viridia's inference in Ch.12 (the actual on-page plant is Ch.13 per roadmap).

## STYLE-ALIGNMENT PASS — Ch.1-4 (2026-06-20)
Brought the four early chapters down to the book's prose-density ceilings (the rest of the book sits at simile <=3.2/1k, em-dash 3-6/1k; Ch.1-4 had been exceeding). Surgical only: weaker similes converted to direct description (strongest kept), excess em-dashes recast as commas/periods, "the kind of" reduced to <=1/chapter.

Before -> After (simile/1k, em-dash/1k):
- Ch.1: 6.0 / 14.1  ->  3.6 / 7.3
- Ch.2: 4.2 / 12.3  ->  3.1 / 5.5
- Ch.3: 6.0 / 15.9  ->  3.8 / 9.0
- Ch.4: 4.2 / 10.8  ->  3.8 / 6.2

style_check.py: Ch.1-4 no longer appear under CEILING or FINGERPRINT flags; no NEW repeated 4-6 word phrase shared with another chapter (verified by before/after n-gram diff). Word counts all above 4,400 floor (4935 / 4550 / 4453 / 4530). Net loss small.

PRESERVED: water motif (Ch.1), planted lines "be careful who you let see you do it" (x2) and "no one sees you do it" (Ch.1+2), all canon, voice, plot, continuity. Genesis Floor >= 8.5 maintained (density reduction does not weaken any dimension; no grounding/interiority/dialogue removed).

NOTE: supersedes NEXT STEPS item #4 above (the Ch.1-4 ceiling-breach lock) — that item is now resolved.

## BOOK-PACKAGER DELIVERY (2026-06-20)
Editorial package + production assembly complete (Book One delivery).

**delivery/editorial/**
- logline.md (primary + 3 alternates)
- synopsis.md (1-page + 3-page; reveals ending, for agents/editors)
- query-letter.md (hook, ~200-word summary, bio placeholder, comps Bardugo/Pierce/Nix, metadata: YA epic/school fantasy, ~85,000 words, Book One of a trilogy, standalone-with-series-potential)
- back-cover.md (no-spoiler cover copy + short variant + Amazon conversion description)
- cover-brief.md (art direction: dark-blue stone, Hazel grey stone/iron gate, Lor-ar, Raizen, two-halves core, rose-tinted motif; cool palette; Bardugo/Nix/Novik feel refs; title treatment)
- upstream-signals.md (logline easy → no premise-clarity issue; query break at the attack/Alice-unknown → no structural-suspense issue)

**delivery/production/**
- production-notes.md
- (master) manuscript/full-manuscript.md — title page + all 18 chapters, clean CHAPTER headings, `* * *` scene breaks normalized.

**Counts:** full-manuscript.md = 84,911 words (assembled, prose only); source chapter total 85,115 (incl. headers/comments stripped during assembly). 18 chapters.

**Proofread:** full read + targeted consistency search. Manuscript already clean — effectively zero copyedits needed. Canon spellings verified (Pembrook, Jazen [no "Jasen"], Lor-ar, Raizen, Isolde/Lightwell, rose-tinted). Sister "Jan" consistent (ch.15/17). High Chancellor unnamed on page — preserved (foundation's "Erik Meros" never appears in chapters; not invented into copy).

**Not done (non-blocking):** EPUB/print binaries (no platform specified); front/back matter beyond title page (need publishing details). Author decisions still open (Alice's fate, unsigned-note author, Raizen's affinity, the family-tree name). Re-seed family-tree-name in Bk2 (its Ch.2 spellbook vehicle burned in Ch.16).

## EM-DASH COPYEDIT PASS (2026-06-20)
Focused punctuation pass enforcing author rule: AT MOST 4 em-dashes per chapter (gate: `tools/style_check.py --max-emdash 4`).

- Edited chapters: 1,2,3,4,5,6,7,8,9,10,11,12,18 (the 13 over ceiling). Ch.13–17 already ≤4, untouched.
- Recasts: parentheticals/appositives → commas; interrupted/trailing dialogue → period or ellipsis (used sparingly, varied); dramatic dashes → period/colon. Refrains kept exact ("be careful who you let see you do it", "no one sees you do it"). Canon unchanged. Scene breaks left as `* * *`.
- Per-chapter em-dash before→after: ch1 20→2, ch2 13→0, ch3 28→0, ch4 16→0, ch5 17→1, ch6 8→0, ch7 19→0, ch8 11→1, ch9 7→0, ch10 13→0, ch11 10→0, ch12 5→0, ch18 9→1. (Residual 1–2 are intentional, under the 4 ceiling.)
- style_check.py: NO EM-DASH/FINGERPRINT/TIC ceiling flags on any chapter. Two repeated-phrase flags my recasts briefly introduced were reworded away; net problems vs pre-pass baseline DROPPED by 2 (no new flags). (The script's "RESULT: N issue(s)" total is dominated by its pre-existing cross-chapter 4–6gram inventory, unrelated to this pass.)
- Word count: 85,842 (chapters) — above the 85,200 floor. full-manuscript.md reassembled (assemble_manuscript.py) and 6x9 interior PDF rebuilt (build_pdf.py, delivery/production/, exit 0).
