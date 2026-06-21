# CLAUDE.md — The Saeren Chronicles

Guidance for Claude Code working in this repository. Read this first.

## What this repo is

This is the working repo for **The Saeren Chronicles** (a YA epic/school fantasy
trilogy by the author). Active work is on **Book One: The Hazel Years**.

**We work only on `main`.** Do not create feature branches or PRs unless the
author explicitly asks. Commit and push to `main`.

Git identity for commits (so GitHub shows them verified):
```
git config user.email noreply@anthropic.com
git config user.name Claude
```

## Repository layout

```
book/
├── The_Saeren_Chronicle_Original_Draft.txt   # author's full raw draft (Ch.1-18), source of truth for plot
├── Series Roadmap — Saeren Chronicles.md      # trilogy story bible (premise, themes, magic system)
├── Saeren Chronicles - Character Bible 2026-05-29.md
├── Saeren Chronicles - Chapter Roadmap 2026-05-29.md   # scene-by-scene plan for Book One
├── What Needs To Be Done — Saeren Chronicles Roadmap.md # master revision checklist
├── Saeren Chronicles - Session Log 2026-05-29.md
├── Saeren Chronicles - Working Session Protocol.md
└── genesis/saeren-chronicles/                 # the active pipeline project (see below)
```

The dated `.md` files were pulled from the author's Google Drive. The plain
`The_Saeren_Chronicle_Original_Draft.txt` is the original manuscript and is the
canonical source for plot/characters when revising.

## The pipeline (how the book is being written)

We are revising/expanding the original draft into a polished Book One using an
adapted version of **Best Seller Studio** (https://github.com/felipelobomotta-blip/best-seller-studio),
an agent pipeline for Claude Code. It was installed by copying its agent files to
`~/.claude/agents/`. The agents are: `book-orchestrator`, `book-researcher`,
`book-architect`, `book-writer`, `book-evaluator`, `book-editor`, `book-disruptor`,
`book-packager`, plus `entity-tracker`, `continuity-guardian`, `dialogue-polish`,
`hook-craft` (the last four are installed from the repo's `skills/` with agent
frontmatter added).

### Install the agents (do this in a fresh environment)
```
git clone https://github.com/felipelobomotta-blip/best-seller-studio /tmp/bss
cp /tmp/bss/agents/*.md ~/.claude/agents/
# Also install the 4 skill-based roles as agents (add tools/model frontmatter):
#   entity-tracker, continuity-guardian (from skills/optional/*/SKILL.md)
#   dialogue-polish, hook-craft        (from skills/deprecated/*/SKILL.md)
```
These four need a frontmatter header like the other agents:
```
---
name: <name>
description: <copy from SKILL.md>
tools: Read, Write, Edit, Grep, Glob, Bash
model: opus
maxTurns: 40
---
```

### Adaptation: this is NOT genesis-from-idea
Best Seller Studio's orchestrator normally invents a new book from a one-line
idea. We DON'T do that. We revise the existing draft. The project lives at:

```
book/genesis/saeren-chronicles/
├── STATE.yaml                 # project state — READ FIRST every session
├── foundation.md, outline.md, voice-dna.md, ENTITY_STATE.yaml
├── research/                  # staged canon: series-roadmap, character-bible,
│                              #   chapter-roadmap, master-checklist, original-draft.txt
├── manuscript/chapters/       # chapter-1.md ... chapter-N.md (the actual book)
├── evaluations/               # per-chapter eval reports + continuity audits
├── feedback/progress.md       # exact resume point — READ to continue
└── tools/style_check.py       # cross-manuscript style gate (see below)
```

## How to continue the book

1. `cd book/genesis/saeren-chronicles` and read `STATE.yaml` and `feedback/progress.md`.
2. Check the last finalized chapter: `ls manuscript/chapters/` and `git log --oneline`.
3. Produce the next chapter(s) IN ORDER. The `book-*` agents are now available as
   real Agent `subagent_type`s — you can dispatch `book-orchestrator`, or run the
   loop role-by-role (`book-writer` → `dialogue-polish` → `hook-craft` →
   `book-disruptor` → `book-evaluator` → `book-editor`). If subagents can't be
   dispatched in your environment, run one `general-purpose` agent that performs
   each role itself by reading `~/.claude/agents/*.md`.
4. For each chapter N: locate its material in `research/original-draft.txt` and
   REVISE/EXPAND to the roadmap beats — do NOT invent from scratch. Match the
   voice of `chapter-1.md`. Then run the gates (below). Commit per chapter:
   `git add -A && git commit -m "genesis: finalize chapter N"`.

### Quality gates (both must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator). The "Floor" is the lowest of the 7
  scored dimensions (Originality, Theme, Characters, Prose/Voice, Pacing, Emotion,
  World-building). Below 8.5 → book-editor polish loop (max 5).
- **Style check** — run `python3 tools/style_check.py`. It must stay clean:
  - simile/metaphor markers ≤ 4.0 per 1,000 words,
  - em-dashes ≤ ~10 per 1,000 words,
  - no NEW repeated 4-6 word phrase shared across chapters (deliberate motifs are
    allowlisted in the script — do not "fix" those),
  - verbal tics under ceiling.
  Fix flagged issues (disruptor/editor) and re-run until clean.

### Word floor
**Finished Book One must be ≥ 85,000 words.** Targets are in STATE.yaml
(`manuscript_min_words: 85000`, `per_chapter_min_words: 4500`). Remaining
chapters should run ~4,800-5,400 words. Verify total with:
`wc -w manuscript/chapters/chapter-*.md`. If short at the end, expand the thinnest
chapters using their roadmap `[EXPAND]`/`[NEW]` beats.

## Canon guardrails (settled author decisions — never violate)

- Alice's surname is **PEMBROOK**. Spelling is **JAZEN** (not Jasen).
- **Lady Lightwell wears ROSE-TINTED spectacles.**
- Viridia: silver-blonde hair, green eyes, slight build 5'5"; grief held inward —
  **NO ONE sees her cry.**
- The world has **trains and motorcars**. Hazel has **NO houses/internal grouping**
  (sorted only by year, ranking, fourth-year sponsorship). Specialty fields
  (healing, intelligence, therapy, building) are **separate post-Hazel schools**.
- **Do NOT introduce Johnathan Masters or the void woman** in this trilogy (they
  belong to the separate "Masters of the Void" series).
- Chapter 1 is the voice benchmark but is **no longer locked** — the author approved
  revising it in the round-2 pass. Preserve its voice, but edit it like the rest.
- If the roadmap and the original draft conflict, follow the **roadmap** and log
  the deviation in `evaluations/`.

## Open author decisions (do not invent — ask the author)

- Alice's ultimate fate (survives the school attack? — a Book Two decision).
- Who wrote the unsigned note packed with Viridia's focus.
- Raizen's elemental affinity.
- The identity behind the family-tree name that "doesn't fit the pattern."

## Status (update this section as you go)

> ### ▶ NEXT SESSION — START HERE: execute the Round-4 revision
> Book One has had a round-3 line pass (pacing/show-don't-tell/motif variation, all 18
> chapters, gate-clean, **86,726 words**) plus a full QA sweep. **The next task is to
> EXECUTE the Round-4 revision plan**, chapter by chapter, with the usual per-chapter
> discipline (read → fix → `python3 tools/style_check.py` clean → check word floor → commit).
>
> - **Plan to execute:** `book/genesis/saeren-chronicles/feedback/revision-plan-round4.md`
>   (read §7e "Consolidated round-4 priority" first — it's the ordered to-do).
> - **Supporting diagnostics:** `book/genesis/saeren-chronicles/evaluations/`
>   — `pacing-map.md`, plus `review/` (genesis-floor-scores, disruptor-differentiation,
>   info-dump-detector, character-arc-consistency, beta-reader-panel).
> - **Open with the front-50 pass (Ch.1–3):** seed the "whole-in-a-severed-world" *sensation*
>   earlier, add an early **misread**, reframe the heirloom note as surveillance-unease, give the
>   Alice friendship one misfire. Then Pacing #1 (decree-clock) + #2 (measurable greyness) in Ch.10–12.
> - **Verdict driving this:** strong draft, **not yet submission-ready**; the levers are early-act
>   pacing, front-50 differentiation, and the scene-end "narrated-meaning" tic. Craft is above gate;
>   the only systemic weakness is Pacing (Book Floor 7.8 @ Ch.15).
> - **Constraints:** keep gates green, respect per-chapter ~4,500 floor (Ch.4/Ch.6 run lean → convert
>   in place, don't net-cut), hold all canon guardrails.
> - After the pass: reassemble `full-manuscript.md` + rebuild PDF, log in `feedback/progress.md`,
>   re-run the beta panel. **Production track** (CMYK/front matter/proof) is still open and non-blocking.

- **Book One COMPLETE.** All 18 chapters finalized & committed — **85,045 words**,
  every chapter Genesis Floor ≥ 8.5, full continuity audit clean (0 critical/0
  warning, 3 minor non-blocking). Canon guardrails held throughout.
- Delivery-ready. Optional next steps (non-blocking), see `feedback/progress.md`:
  - Run `book-packager` for the editorial package (logline/synopsis/query/cover)
    and production formatting (ebook/print).
  - Author decisions still open (see below) before Book Two.
  - Re-seed the "family-tree name that doesn't fit" — its Ch.2 vehicle (the
    spellbook) burned in Ch.16, so the plant needs a new home if kept.
- **Books Two and Three are not started.** When ready, set them up as their own
  pipeline projects (e.g. `book/genesis/saeren-chronicles-book-2/`) seeded from
  the same Series Roadmap + the Book One ENTITY_STATE.yaml.

## Other books (folder-per-book in this repo)

This repo holds multiple book projects, one folder each under `book/genesis/<slug>/`.
A reusable template + scaffold makes new books quick to start:

- `book/genesis/_template/` — the starter (STATE.yaml, CLAUDE.md, tools/style_check.py).
- `book/genesis/new_book.sh` — scaffold script. Create a new book with:
  ```
  bash book/genesis/new_book.sh <slug> "<Book Title>"
  ```
  It creates the standard structure and fills in title + date.

**To start a new book (any fresh session can do this):**
1. `bash book/genesis/new_book.sh <slug> "<Title>"`.
2. Pull the book's source material from Google Drive into `book/genesis/<slug>/research/`
   (the original draft, plus any roadmap/bible).
3. Fill in `book/genesis/<slug>/STATE.yaml` (premise, genre, comps, canon_sources,
   guardrails, open author decisions) and the ALLOWLIST in its `tools/style_check.py`.
4. Install the Best Seller Studio agents (see install block above) and run the adapted
   pipeline chapter by chapter, honoring the per-book `CLAUDE.md` and the two gates
   (Genesis Floor ≥ 8.5 + style_check.py clean) and the word floor.

Each book's own `book/genesis/<slug>/CLAUDE.md` is the per-book playbook; read it first.
You do NOT need any particular chat to continue — the repo is the memory.
