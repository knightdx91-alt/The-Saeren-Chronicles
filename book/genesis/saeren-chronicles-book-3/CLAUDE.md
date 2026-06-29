# CLAUDE.md — The Saeren Chronicles — Book Three: The Weight of the Source

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A genesis project to revise/expand an existing draft into a finished book, using the
adapted **Best Seller Studio** pipeline. We work only on `main`. Commit and push to `main`.

Git identity (so commits show verified):
```
git config user.email noreply@anthropic.com
git config user.name Claude
```

## Install the agents (fresh environment)
```
git clone https://github.com/felipelobomotta-blip/best-seller-studio /tmp/bss
cp /tmp/bss/agents/*.md ~/.claude/agents/
# Also install 4 skill-based roles as agents (add tools/model frontmatter):
#   entity-tracker, continuity-guardian (skills/optional/*/SKILL.md)
#   dialogue-polish, hook-craft        (skills/deprecated/*/SKILL.md)
# Frontmatter to prepend to each:
#   ---
#   name: <name>
#   description: <from SKILL.md>
#   tools: Read, Write, Edit, Grep, Glob, Bash
#   model: opus
#   maxTurns: 40
#   ---
```
Note: in some environments the Agent tool can't dispatch these named subagents. If so,
run ONE general-purpose agent that performs each role itself by reading ~/.claude/agents/*.md.

## Project layout
```
book/genesis/<slug>/
├── STATE.yaml                 # READ FIRST — project state, word/style gates, canon
├── research/                  # staged source: original-draft.txt + roadmap/bible/etc.
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point
└── tools/style_check.py       # style gate (edit ALLOWLIST for this book's motifs)
```

## How to continue
1. `cd book/genesis/<slug>` and read `STATE.yaml` and `feedback/progress.md`.
2. `ls manuscript/chapters/` and `git log --oneline` to find the last finalized chapter.
3. Produce the next chapter IN ORDER. Locate its material in `research/original-draft.txt`
   and REVISE/EXPAND to the roadmap beats — do not invent from scratch. Match the locked
   Ch.1 voice if one exists. Run each chapter through: write → dialogue-polish → hook-craft
   → disruptor → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (both must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤~10/1k,
  no NEW cross-chapter repeated phrase (add deliberate motifs to ALLOWLIST), tics under ceiling.
- **Grammar check** — `python3 tools/grammar_check.py` must report `RESULT: clean` (HARD GATE:
  doubled words, space-before-punct, a/an). Also reports the 3 longest sentences per chapter —
  split at least one of them unless deliberately load-bearing. Optional tense/agreement layer:
  `--file <chapter> --languagetool` (LanguageTool; needs Java + one-time download; non-gating).
  Built 2026-06-29 after the Book One Ch.1 reviewer line-edit; see root CLAUDE.md "Recurring
  craft mistakes".

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## This book is GENESIS-FROM-ROADMAP (no prior draft)
Unlike Books One/Two, there is **no author original draft** for Book Three. Build it from the
Series Roadmap's Book Three section (`research/series-roadmap-book3.md`, BINDING) + Book Two's
ENTITY_STATE and final chapters (in `research/`). Do not invent canon that contradicts Books
One/Two — open their actual prose when reusing any element (see continuity discipline below).
Match the Book One / Book Two Ch.1 voice.

## Canon guardrails (settled — never violate; see STATE.yaml `guardrails` + `binding_beats`)
- **Series canon:** single-n **Saeren**; Alice **PEMBROOK**; **JAZEN**; Lady Lightwell wore
  ROSE-TINTED spectacles (dead); Viridia silver-blonde, green eyes, slight 5'5'; trains + motorcars.
- **YA tone (series-wide):** violence = consequence, cut the camera on the worst acts; no explicit
  sex / graphic torture / adult profanity; keep hope/connection (Raizen, Alice, chosen family)
  load-bearing between dark beats. Grief held inward — NO ONE sees Viridia cry IN PUBLIC. Two
  sanctioned breaks ONLY: (1) Book Two Ch.16 (Jazen's death, public grief torn out of her); (2) Book
  THREE Ch.10 (the midpoint reckoning) — the FIRST time she lets ONE trusted person, RAIZEN, see her
  break, private and singular, the deliberate counterpart to Ch.16. Everyone ELSE still never sees;
  do not add a third break (author decision 2026-06-25).
- **Do NOT introduce Johnathan Masters or the void woman** (Masters of the Void is a separate series).
  The ONLY connection is the final image — Viridia feeling a void for the first time — and the
  roadmap says **do not explain it; let it sit.**
- **Binding beats:** the Horrors are PULLED toward the source (not attacking) — the rebirth made a
  pressure differential with the void → Viridia created the next threat; resolution is BALANCE, not
  victory; ending = the lab, a severed tentacle, **Fen** runs, Viridia feels the void. (See STATE.yaml.)
- **Continuity discipline:** before reusing a Book One/Two element (the physical source-cavern, the
  death-symbol, a returning character/rule), open that book's prose and match it; run
  continuity-guardian vs BOTH earlier books before finalizing each Act-Three chapter.

## Roadmap is PRE-FINAL — read the reconciliation note
The Series Roadmap was written before Books One/Two were finished. **`research/roadmap-vs-books-reconciliation.md`
is the override layer** — where the finished books diverge from the roadmap, the books win. Key overrides:
Viridia's mana-SIGHT is SPENT at Book-Three open and returns slowly (not "feels every core at all times");
Alice **taught Viridia** Moravian (bible had it reversed); Alice is **changed/recovering**; the Death symbol
**closes portals** (the tactical spine, since Horrors come through portals); Raizen is **human**; the void-rim
is **abstract, no entity**; the source = the **physical Book One cavern**.

## Resolved author decisions (2026-06-24)
- **Marick vs Fen — RESOLVED:** Marick OPENS the bad working/portal (Bk2 Ch.20 seed); **Fen is his
  assistant who RUNS** at the very end (roadmap's final image). Two people, one thread; Fen is new here.
- **Age on-page — RESOLVED:** Book Three MAY state her age (sixteen) plainly. (Book Two's no-number rule
  was for the private 14→15 turn-beat; verified Book Two has no Viridia age-number on-page after the r6 fix.)

## Still-open author decisions (ask, don't invent — see STATE.yaml)
- pact-and-Dangris; **Mrs. Zoran's status** (survival after Hazel unconfirmed); the **time-skip length**
  (needs ~a year, not a few months, for her to be 16). (**Raizen's affinity RESOLVED 2026-06-25: prismatic / all-elements.**)

## Status (update as you go)
- Scaffolded + seeded + architect pass done (foundation.md + outline.md, 22 ch). Author decisions locked.
- **DRAFTING IN PROGRESS — Ch.1 & Ch.2 FINALIZED on `main` (2026-06-24)** via the authentic agent
  pipeline. Both gate-clean, evaluator Floor 8.5 PASS, continuity clean. **READ `feedback/progress.md`
  for the full resume note** — it has (a) how to install the agents (curl-tarball, since `git clone` is
  403-blocked by the git rewrite and BSS's default branch is `master`), (b) the per-chapter pipeline
  that worked, and (c) the next-chapter beats.
- **NEXT: Ch.3 "A City With No Head"** (political chapter — temptation to rule named; END HOOK in the
  HUMAN/political register, not another source-sense close). Then Ch.4 "The Easy Mark" (FIRST Death-symbol
  portal-close + its eerie easiness — reserved here, deliberately NOT used in Ch.2) and Ch.5.
- **TWO CONTINUITY RULES LOCKED THIS SESSION (do not re-break):**
  1. **Raizen's HUMAN eyes are dark/ordinary brown** (Bk2 Ch.19 dimmed them down from lightning at the
     change). Lightning-blue = his DRAGON form AND Lor-ar's signature marker — never the human form.
  2. **The Death symbol is reserved for Ch.4** (its first portal-close + 'easy/asks nothing/Drake's
     daughter' theme). Ch.2 closes its tear the COSTLY way (Viridia spends her own source-warmth) to set
     up that contrast. Don't let an earlier chapter poach the Death symbol.
