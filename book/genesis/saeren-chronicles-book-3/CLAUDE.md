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
  load-bearing between dark beats. Grief held inward — NO ONE sees Viridia cry (the once-in-a-life
  break was Book Two Ch.16).
- **Do NOT introduce Johnathan Masters or the void woman** (Masters of the Void is a separate series).
  The ONLY connection is the final image — Viridia feeling a void for the first time — and the
  roadmap says **do not explain it; let it sit.**
- **Binding beats:** the Horrors are PULLED toward the source (not attacking) — the rebirth made a
  pressure differential with the void → Viridia created the next threat; resolution is BALANCE, not
  victory; ending = the lab, a severed tentacle, **Fen** runs, Viridia feels the void. (See STATE.yaml.)
- **Continuity discipline:** before reusing a Book One/Two element (the physical source-cavern, the
  death-symbol, a returning character/rule), open that book's prose and match it; run
  continuity-guardian vs BOTH earlier books before finalizing each Act-Three chapter.

## Open author decisions (ask, don't invent — see STATE.yaml `open_author_decisions`)
- **Reconcile Marick (planted in Book Two Ch.20) vs Fen (roadmap's Book Three ending)** — same person
  or two threads? Decide before Act One + the finale.
- **Age on-page:** roadmap says Viridia is **sixteen**; Book Two used a strict no-age-number rule —
  decide whether to state 16 or keep the convention.
- Raizen's elemental affinity; whether the human–beast pact applies to the Dangris; Mrs. Zoran's role.

## Status (update as you go)
- **Scaffolded + seeded (2026-06-24).** Research staged (`research/`): Book Three roadmap section
  (premise/3-conflict-levels/key-revelation/resolution/ending/magic-bible), Book Two ENTITY_STATE,
  Book Two final chapter (Ch.20 — the Marick/lab + void-rim seeds) and the rebirth chapter (Ch.18).
  STATE.yaml filled (premise, canon, binding beats, open threads, word floor 95k). Own PDF/production
  pipeline mirrored from Book Two (REVISION policy: bump before rebuild; keep prior builds).
- **NEXT: architect pass** — build `foundation.md` + `outline.md` (≈20–23 chapters) from the roadmap,
  resolve the open author decisions with the author, then run the chapter loop in order. No prose yet.
