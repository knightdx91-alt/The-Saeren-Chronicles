# Progress — Book Two: The Resistance

## ▶ RESUME HERE: write Chapter 8 ("Dust to Dust" — Drake teaches the Death symbol; a road betrayed)
Architecture done (foundation.md, outline.md, ENTITY_STATE.yaml). **Chapters 1–7 DRAFTED via
the book-writer agent suite, all gate-clean AND evaluated.** ~35,951 words so
far (toward the 85,000 hard floor / 90–100k target).

> **2026-06-22 (Ch.7 done):** Chapter 7 "What She Tries First" opens Act Two — gate-clean
> (5,720 words; em-dash 4; style_check RESULT: clean) and reviewer PASS (Genesis Floor 8.5;
> continuity 0 critical / 0 warning / 2 minor confirmations). Report: `evaluations/eval-ch7.md`.
> Parallel structure: the peace-message/embassy strand (answering "Who else knows" with the
> costlier truth) braided with the dragon council (Drake + Varissa consulted; Varissa's fury
> that Viridia left True-Bonded Raizen off her ledger; Drake's grief). Hook: Drake agrees to
> teach the Death symbol tomorrow. **Resume at Ch.8** (outline ~4,800: Drake teaches the Death
> symbol; destined for meaningful use; a peace road betrayed).

> **2026-06-22 (Ch.6 done):** Chapter 6 "The Window Narrows" closes Act One — gate-clean
> (5,455 words; em-dash 4; style_check RESULT: clean) and reviewer PASS (Genesis Floor 8.6;
> continuity 0 critical / 0 warning / 3 minor, all addressed in ENTITY_STATE). Report:
> `evaluations/eval-ch6.md`. ENTITY_STATE bumped to ch.6 (Ferro added; Hiram wounded; spear
> inventory note). Hook into Act Two: Viridia asks Jazen to reach the capital's moderates in
> person, by shadow, before the march. **Resume at Ch.7** (outline beat ~4,900: the embassy /
> the dragons — Drake & Varissa consulted; peace attempt #1).

> **2026-06-22 session note:** The author cleared the prior Ch.1–9 drafts and restarted the chapter
> loop with the book-* agent suite (dispatched as `general-purpose` agents reading
> `~/.claude/agents/*.md`, since named book-* subagents aren't dispatchable in this env). Book Two now
> lives **directly on `main`** (no feature branch/PR), in `book/genesis/saeren-chronicles-book-2/`.
> Ch.1–5 redrafted + style-gate-clean + evaluator/continuity pass done (see below). Resume at Ch.6.

### Ch.1–5 quality pass (2026-06-22) — PASSED
- **Genesis Floor ≥ 8.5 on all five** (averages 8.71–9.00). Report: `evaluations/eval-ch1-5.md`.
- **Continuity: 0 critical / 3 warning / 5 minor**, all canon held. Report: `evaluations/continuity-ch1-5.md`.
- **3 warnings RESOLVED:** age (author ruling: 14 at open, turns 15 on-page — Ch.4 fixed, premise + AGE
  CANON note added, turn-to-15 still to be PLACED on-page, recommend around the march); war-clock (Ch.4
  Jazen acknowledges the named week lapsed / march held deliberately); reply-speed (Ch.5 rail-wire relay).
- 5 minor are watch-notes (e.g. add scout **Ferro** to ENTITY_STATE on next update; Mella named Ch.1 not Ch.3).

### Author constraints in force (2026-06-22)
- **85,000-word hard floor** (`manuscript_hard_min_words` in STATE.yaml). Aim ~95k for headroom.
- **Em-dash ≤ 4 per chapter** — enforced via `python3 tools/style_check.py --max-emdash 4`.
- **Brisk pacing across Ch.1–5** — done: chapters open in motion and end on concrete pulls.

### Author decisions (resolved, binding)
- Alice = **ALIVE, CAPTURED** in the capital (confirmed Ch.3).
- Raizen = **ALL ELEMENTS / prismatic**.
- Unsigned note = **Lightwell** (revealed Ch.4 via her papers; author may revise — only Ch.4/10 change).
- **Viridia's age = 14 at open, turns 15 on-page** (2026-06-22 ruling; birthday beat not yet placed).

### Chapters 1–5 (each ≥4,360 words, gate clean)
1. **The Box of Invisible Air** — the camp from inside; named villagers (Brutus, Mirelle, Hiram);
   the failing ward; Jazen reads what she is; supply line returns with a name.
2. **The Thread Pulled Taut** — Alice rumor (taken alive); Raizen returns w/ Drake (first words,
   the pact); Viridia commits to the march; Jazen opens up (Jan, his fear of his power).
3. **Alive Is Not the Same as Safe** — council resolves to empty & march; Alice CONFIRMED (workhouse,
   "Alice P."); Amber beat; the moral question first stated in full (mend all cores without consent).
4. **His Mother's Papers** — Lightwell's cache: the unsigned note (she chose Viridia first); the
   off-pattern family-tree name re-seeded; the camp empties; the Hiram micro-temptation; Lor-ar's
   counsel ("not who chose you, but what you will choose"); a peace road found (a Conclave moderate).
5. **The Furnace and the Match** — Viridia tests her power (mends a rowan; rebirth proven trivially
   easy); the first true cost is to the WORLD — the void-rim absence LEANS toward fullness (abstract,
   no entity; Bk3 seed); sends the first peace message; Amber's challenge deepens.

### style_check.py improvements made this run (documented, principled — not loosening to pass)
- Strips HTML comments before analysis (they are not prose).
- Added a proper stopword set (auxiliaries/function words) so connective n-grams aren't false fingerprints.
- Added `--max-emdash` ceiling (default 4) to actually GATE the author's em-dash rule.
- Cross-chapter repeats flag only when DISTINCTIVE: a 2-chapter pair must be ≥5 words, or any phrase ≥3×
  (matches the project's "no NEW *distinctive* repeated phrase" intent).
- ALLOWLIST extended with deliberate Book-Two motifs (the careful face; cold clear part; six hundred
  years; on half its wick; the filing habit; the promise refrain; "one circle, one maybe"; etc.).

## NEXT (Ch.6 → end)
- **Ch.6** closes Act One: patrol pressure / skirmish at the wards; Hiram further spent; the window
  narrows; Viridia commits the remaining days to the peace roads. End on a concrete pull into Act Two.
- **Act Two (7–13):** the three peace attempts (Ch.7 message/embassy + Drake & Varissa consulted;
  Ch.8 death symbol taught + a road betrayed; **Ch.9 Amber's full moral challenge**; Ch.10 the "almost";
  Ch.11 camp found & burned, the named-villager deaths; Ch.12 goodbyes incl. Drake/Varissa→Raizen;
  Ch.13 the march/walls, Jazen at his fullest).
- **Act Three (14–20):** battle; Alice rescue; **Ch.16 Jazen beheaded before both armies** (the banked
  breakdown spends); Ch.17 the decision + Drake kills the Chancellor; **Ch.18 the rebirth (≥3 pp)**;
  Ch.19 Raizen human (wonder+humor) + Lor-ar released; Ch.20 finale + Marick/lab seed.
- Keep the per-chapter gates (Genesis Floor ≥8.5 + style_check clean) and the 85k floor; run
  `book-evaluator`-style Genesis scoring before declaring chapters final if dispatching subagents.
