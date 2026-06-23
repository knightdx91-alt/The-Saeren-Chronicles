# CLAUDE.md — The Saeren Chronicles

Guidance for Claude Code working in this repository. Read this first.

## What this repo is

This is the working repo for **The Saeren Chronicles** (a YA epic/school fantasy
trilogy by the author). Active work is on **Book One: The Hazel Years**.

**We work only on `main`. ALWAYS.** There must be NO other branch — regardless of
which book we are working on. Everything gets committed and pushed straight to
`main`. Do NOT create feature branches or PRs, ever (not even drafts). If a cloud
session starts on some other branch (e.g. `claude/...`), push your work to `main`
directly (fast-forward) so nothing splits off and everything stays in one place.

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

   > **STANDING AUTHOR DECISION (2026-06-22): USE THE AGENTS for the book-writing
   > suite.** The author has approved (and prefers) dispatching the book-* writer
   > and reviewer agents for drafting and reviewing chapters — do NOT default to
   > hand-writing chapters inline. Dispatch a writer agent per chapter under a HARD
   > GATE CONTRACT: do not return until the chapter is (a) ≥ the per-chapter word
   > floor (Book Two: ≥4,600–4,700; see STATE.yaml), (b) em-dash ≤ 4 (run
   > `python3 tools/style_check.py --max-emdash 4`), (c) `RESULT: clean` on the
   > whole style run, and (d) voice-matched to Book One. The agent self-runs the
   > tool and iterates until it passes; the parent only reviews and commits. Run
   > chapters SEQUENTIALLY (each needs the prior finalized chapter for voice +
   > plot + ENTITY_STATE continuity). Use a reviewer agent (book-evaluator +
   > continuity-guardian) on each batch. This avoids the under-length / repeated-
   > phrase churn that comes from drafting by hand.
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

## YA tone continuity (applies to every book in the trilogy)

The series is **upper/mature YA** — the same register as Book One's school-attack
climax (Ch.16–18), sustained, not exceeded. Hold this line in every chapter:

- **Violence is consequence, never spectacle.** Show death's weight and aftermath;
  do NOT linger on viscera. At the worst acts (e.g. Jazen's execution), **cut the
  camera on the act itself** — the horror lives in the silence after and in
  Viridia's reaction, not in describing the blade's work.
- **No content that pushes past YA:** no explicit sex, no graphic/lingered torture,
  no adult-register profanity.
- **Keep hope and connection LOAD-BEARING between the war beats.** Book Two lost
  Book One's lighter school-story buffer, so the YA-ness now rests on the
  Alice thread, the chosen-family bonds, and Viridia's agency. If those thin out and
  it becomes wall-to-wall grief, the book drifts toward adult grimdark — that, not
  any single image, is the real risk. Thread relief/connection through every dark
  stretch.
- The sanctioned exception to "grief held inward" is the **Book Two Ch.16 breakdown**
  (banked since Book One); everywhere else, grief stays inward (see guardrail below).

## Book One canon cross-check (catch continuity drift BEFORE drafting)

ENTITY_STATE is a SUMMARY, not the source of truth for *how a returning element
was actually rendered*. Whenever a later-book chapter reuses anything established
in an earlier book — a **place** (the source/well CAVERN, the school, a room), a
returning **character's** established traits/appearance, an **object**, or a rule —
the writer MUST open the earlier book's actual prose (`../saeren-chronicles/manuscript/chapters/`)
and match it, not just the one-line entity note. Drift example caught 2026-06-23:
the Book Two rebirth was about to happen as a metaphysical reach from the battlefield,
but Book One Ch.14 had already made the source a **physical cavern** (stone chamber,
pedestal, pool) reached by portal — so the rebirth must portal back THERE.
**Process:** (1) before drafting any Act-Three chapter that touches a Book One element,
grep Book One's chapters for it and read the passage; (2) run a `continuity-guardian`
pass against Book One canon (not just Book Two) before finalizing. Do not rely on the
author to catch these.

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

> ### ▶ NEXT SESSION — START HERE: non-prose tracks (round-6 prose is DONE)
> **Round 6 (the passive-protagonist fix) is COMPLETE & committed** — build **r6, 93,170 words**,
> gate clean, canon held. 5 beats converted to costly choices (Ch.3 keep focus openly, Ch.4 break
> cover for Lightwell, Ch.5 defy "start small", Ch.16 choose to leave Alice + spend hidden rune-craft
> to decide the escape). Verified: analytical active-beat ratio **~33%→~55-65%**; continuity **0 critical**;
> beta panel **7.7→8.3** (Critic 7.5→8.5, Hostile 6→7, Casual 7→8); over-narration trimmed.
> Deliverables retain every revision (`...-r5.pdf`, `...-r6.pdf`).
>
> **What's left (NON-PROSE, optional, author's call):**
> - `book-packager` → query/synopsis/comps that frame the QUIET voice as the feature (literary/boutique
>   agents + small press); see `feedback/revision-plan-round6.md` §6.
> - Production prep before print/self-pub: CMYK/PDF-X, full front+back matter, widows/orphans proof
>   (PDF is RGB). See `delivery/production/pdf-print-notes.md`.
> - Optional micro-polish from the r6 beta report: one irreversible bodily cost in the Ch.16 escape
>   (retire the boot-heel near-miss); replace Lightwell's flat "You were chosen."
> - Book-Two hooks logged: the Ch.5 "hungry thing"; the dateless family-tree name (re-homed via the
>   Well's mother-thread). Open author decisions still pending (see below) before Book Two.
>
> --- prior round notes (history) ---
> Rounds 3–5 are done and committed (pacing, show-don't-tell, motif variation, war-clock,
> climax causal joint, Ch.16 jeopardy, the dread-object named "the Hollowing"). Current build
> **r5, ~89,898 words**, style gate CLEAN, all canon held. Fresh evaluators say opening + middle
> now "work" (beta avg 7.7; pacing opening "submission-ready"). An honest agent-style read says
> the remaining blocker is **#1 the protagonist is too PASSIVE** (same root cause as the
> lingering "too quiet/slow" notes), plus positioning (quiet book in a loud aisle) and production.
>
> - **MASTER PLAN to execute:** `book/genesis/saeren-chronicles/feedback/revision-plan-round6.md`
>   (read its TL;DR first — full tool-sequenced steps, constraints, and pathways).
> - **The fix is CONVERSIONS, not new plot:** turn beats that happen TO Viridia into costly CHOICES
>   she makes (focus/"tell her no", the sponsorship, the bond-call, the slept-through attack warning).
>   Aim ~4 conversions in Ch.1–9 + a decisive Ch.16. Agency without cost is not agency.
> - **GATE:** Step 1 (design) is `book-architect` → `feedback/agency-conversion-plan.md` (decision-map
>   + proposed conversions). **AUTHOR MUST APPROVE that conversion list BEFORE any prose is rewritten.**
>   If that file is missing, re-dispatch the architect task (see round-6 plan §2).
> - Then implement with `book-editor` (per-chapter gate-clean), verify with the analysts
>   (`analytical-peer-reviewer`, `beta-reader-panel`, `character-arc-consistency`, `continuity-guardian`),
>   rebuild as **r6** (bump the `REVISION` file) + refresh the `book-review` branch.
> - **Non-prose tracks (parallel):** `book-packager` for a query that frames the quiet voice as the
>   feature (literary/boutique agents, small press); production (CMYK/front matter/widows) before print.
> - **Constraints:** canon absolute; don't contradict the fixed Ch.16 causality; gates green;
>   word floor ≥85,000 (ample headroom); Genesis Floor ≥8.5.

- **Book One COMPLETE.** All 18 chapters finalized & committed — **85,045 words**,
  every chapter Genesis Floor ≥ 8.5, full continuity audit clean (0 critical/0
  warning, 3 minor non-blocking). Canon guardrails held throughout.
- Delivery-ready. Optional next steps (non-blocking), see `feedback/progress.md`:
  - Run `book-packager` for the editorial package (logline/synopsis/query/cover)
    and production formatting (ebook/print).
  - Author decisions still open (see below) before Book Two.
  - Re-seed the "family-tree name that doesn't fit" — its Ch.2 vehicle (the
    spellbook) burned in Ch.16, so the plant needs a new home if kept.
- **Book Two ("The Resistance") IS IN PROGRESS** at `book/genesis/saeren-chronicles-book-2/`
  (everything pushed straight to `main` — single-branch workflow, no other branch ever). Drafted via
  the book-* agent suite (dispatched as `general-purpose` agents that read `~/.claude/agents/*.md`,
  since the named book-* subagents aren't dispatchable in this env), each chapter under the HARD GATE
  CONTRACT (≥4,600w; `style_check --max-emdash 4` → RESULT: clean; `rhythm_check` no flat triplets;
  voice-matched; canon held). Outline runs to **20 chapters**.
  > ### ▶ NEXT SESSION — Book Two: RESUME AT CHAPTER 18 ("The Rebirth")
  > **Chapters 1–17 FINALIZED on `main`** (all gate-clean, RESULT: clean). Ch.17 ("The Decision") DONE:
  >   Viridia chooses to mend-for-all unasked; **Drake kills Meros with death-flames (High Chancellor DEAD)**;
  >   she reaches for the well (rebirth held for Ch.18; Bella's-name thread named, untouched).
  > - **Word count: 86,375w through Ch.17 — past the 85,000 hard floor.** Target band 90–100k; 3 chapters
  >   left (18, 19, 20) give ample room.
  > - **Ch.18 ("The Rebirth") is the next BINDING beat:** the mending of the 600-year severing for every
  >   living core at once, ≥3 full pages, fragmented→whole; she touches **Bella's-name thread** and again
  >   cannot follow it (Bk3 held); END HOOK = battlefield simply stops, every mage whole and not knowing why.
  > - Then Ch.19 ("What Remains", quieter wonder+grief) and Ch.20 (close). See `outline.md`.
  > - **YA tone guardrail now in force** (see "YA tone continuity" section above): violence=consequence,
  >   cut the camera on the act, keep hope/connection load-bearing. The sanctioned grief-inward break was
  >   Ch.16 ONLY; she is changed by it but grief goes back inward after.
  >
  > --- prior resume note (history) ---
  > Chapters 1–5 finalized (24,715w); Ch.6–9 adopted from epic branch + age-scrubbed; Ch.10–13 (Act Two)
  > and Ch.14–16 (Act Three through THE HINGE: Jazen beheaded before both armies, the breakdown breaks)
  > all finalized gate-clean. Binding decision: **Viridia is 14 at open, turns 15 on-page** (turn-to-15
  > beat PLACED in Ch.12, felt/private, no number on the page).
- **Book Three is not started.** When ready, set it up as its own pipeline project seeded from the
  Series Roadmap + the Book Two ENTITY_STATE.yaml.

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
