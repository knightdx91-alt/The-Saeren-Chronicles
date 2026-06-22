# Progress — Book Two: The Resistance

## ▶ RESUME HERE: write Chapter 6 (Act One close)
Architecture done (foundation.md, outline.md, ENTITY_STATE.yaml). **Chapters 1–5 drafted,
committed to `main`, all gate-clean.** ~22,885 words so far (toward the 85,000 hard floor /
90–100k target).

### Author constraints in force (2026-06-22)
- **85,000-word hard floor** (`manuscript_hard_min_words` in STATE.yaml). Aim ~95k for headroom.
- **Em-dash ≤ 4 per chapter** — enforced via `python3 tools/style_check.py --max-emdash 4`.
- **Brisk pacing across Ch.1–5** — done: chapters open in motion and end on concrete pulls.

### Author decisions (resolved, binding)
- Alice = **ALIVE, CAPTURED** in the capital (confirmed Ch.3).
- Raizen = **ALL ELEMENTS / prismatic**.
- Unsigned note = **Lightwell** (revealed Ch.4 via her papers; author may revise — only Ch.4/10 change).

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
