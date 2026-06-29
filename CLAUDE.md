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

### Revision discipline (MANDATORY — never skip)
**Every time the manuscript changes and the PDF is rebuilt, bump the revision
FIRST.** The file `book/genesis/<book>/REVISION` (e.g. `r7`) is the single source
of truth — `tools/build_pdf.py`, `tools/assemble_manuscript.py`, and
`tools/make_pdfx.sh` all read it and stamp it into the deliverables. Process:
1. Edit `REVISION` to the next tag (`r7` → `r8`) BEFORE running the build.
2. Rebuild the manuscript + PDF (`python3 tools/assemble_manuscript.py`,
   `python3 tools/build_pdf.py`).
3. Keep the prior build (`...-r7.pdf`/`full-manuscript-r7.md`) as history; the new
   build carries the new tag.
4. Log what changed in `feedback/book1-r<N>-changes.md` (see below).
No manuscript/PDF update ships without a revision bump — title changes count.

### Book-Two cross-check log (Book One is upstream canon now)
Book One is no longer standalone — Book Two depends on it. **Any change to Book One
prose, names, places, or canon must be recorded** in `feedback/book1-r<N>-changes.md`
(chapter · what changed · any Book-Two continuity touchpoint), and a
`continuity-guardian` pass run against Book Two before the revision is finalized.

### Current Book One title
**"The Saeren Chronicles — Book One: Hazel Academy"** (changed 2026-06-24 from
"The Hazel Years" — she is at Hazel for one school year, cut short by the attack, so
the plural was inaccurate). Series name keeps the canonical single-n **Saeren**.
Book Two remains **"The Resistance"**.

## Recurring craft mistakes — NEVER repeat (applies to every book; read before drafting)

Distilled from reviewer **Eilidh Locherty's** line-edit of Book One Ch.1 (Google Docs,
2026-06-29) and corroborated by the standing external-review note across Books One & Two
("too quiet / over-narrated / slow"). These are the things WE keep doing wrong. The root is
one habit: **writing dense, atmospheric prose that serves the voice at the expense of the
reader's plain comprehension.** The fix is NOT to flatten the voice (reviewers praise the
atmosphere and humor) — it is to clarify without flattening. After drafting every chapter,
run this checklist as part of the gate:

**A. Structural / over-narration (the big one):**
1. **Over-packed sentences** — "doing a lot in one breath." After drafting, find the 3
   longest sentences per scene and SPLIT at least one unless it is deliberately load-bearing.
   "We don't need to say everything."
2. **Vague poetic reaches** — every "she knew / always / something / deep water"-type phrase
   must name what it refers to, or be cut. If a reader can ask "knew WHAT?", fix it.
3. **Cleverness over clarity** — any joke/wordplay or clever construction gets one plain
   re-read; if a smart reader has to reparse it (e.g. the "character"/toast gag), rewrite it.
4. **Unmarked scene/time jumps** — signal every time/place jump explicitly; don't cut from
   kitchen to gate with no marker.

**B. Line-craft tics (small, repeated, corrected again and again):**
5. **Tense drift** — hold the tense; watch simple-past vs past-perfect (`went` vs `had come`).
6. **Inconsistent contractions** in narration — pick a register and hold it.
7. **Connective monotony** — don't lean on `then`/`while`; vary.
8. **Telling adverbs** — prefer the shown action over `instinctively`/`-ly` tells.
9. **Agreement & dangling modifiers** — every opening modifier must attach to a clear subject.
10. **Name redundancy / dialogue attribution** — decide when a character is "Leon" vs "her
    father" and HOLD it; never double a name (`"Bella Bella said"` → `"her mother said"`);
    make every speaker unambiguous.

**MECHANICAL GATE (so this is enforced, not just intended):** every book has
`tools/grammar_check.py`. Run it per chapter alongside `style_check.py` — it is a HARD GATE.
- `python3 tools/grammar_check.py` → must report `RESULT: clean` (tier 1: doubled words,
  space-before-punctuation, a/an mismatch — unambiguous typos; exits non-zero on any).
- It also REPORTS (non-gating) the 3 longest sentences per chapter — use them to run rule A.1
  (split at least one of the longest unless deliberately load-bearing).
- Optional tier 2 (tense/agreement/dangling-modifier via LanguageTool, non-gating warnings):
  `pip install language-tool-python` (needs Java + a one-time ~250MB engine download), then
  `python3 tools/grammar_check.py --file manuscript/chapters/chapter-N.md --languagetool`.
  Run it per-file (slow on a whole book). Treat as an assist, not an authority.

(Full evidence + per-comment list: `book/genesis/saeren-chronicles/feedback/book1-reviewer-comments-2026-06-29.md`.)

## APODICTIC — structural developmental-editing plugin (auto-loaded every session)

A third-party Claude Code plugin (`anotherpanacea-eng/apodictic`, v2.6.2, CC-BY-NC-SA) that
**diagnoses manuscript structure and NEVER rewrites** — reverse outline, pacing, character
architecture, reveal economy, genre calibration, 37 audits, series-continuity tracking. It is
the structural-diagnosis layer our own gates lack (style/grammar/rhythm are line-level;
book-evaluator/continuity-guardian are lighter). Best used as a structural second opinion before
locking a revision — exactly the "too quiet / over-narrated / passive / pacing" class of notes.

**It is VENDORED into this repo and auto-enabled — no install step needed:**
- Plugin lives at `tools/apodictic/` (marketplace root: `.claude-plugin/marketplace.json` +
  `plugins/apodictic/`). Vendored because this env's proxy blocks `git clone` of non-Saeren repos.
- `.claude/settings.json` declares it: `extraKnownMarketplaces.apodictic` → `{source: directory,
  path: tools/apodictic}` and `enabledPlugins: {"apodictic@apodictic": true}`. Project-level
  settings load every session for every clone (incl. cloud), so its commands/skills are present
  automatically. A restart/fresh session may be needed the first time after this was added.
- **Usage:** its slash commands — `/apodictic`, `/audit`, `/coach`, `/plot-coach`, `/ready`,
  `/start`, `/triage-feedback`, `/world-bible`, etc. Point it at a manuscript, e.g.
  `book/genesis/saeren-chronicles-book-3/manuscript/full-manuscript-r1.md`.
- **Manual fallback** (if the auto-enable doesn't take in some client): `/plugin marketplace add
  tools/apodictic` then `/plugin install apodictic@apodictic` (local path avoids the clone block).
- **To update it:** re-vendor from the tarball (`codeload.github.com/anotherpanacea-eng/apodictic/
  tar.gz/refs/heads/main`) into `tools/apodictic/`, keeping `.claude-plugin/` + `plugins/`.

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
  > ### ▶ NEXT SESSION — START HERE (Book Two r2 revision round, in progress 2026-06-24)
  > **An external r1 review came in (`feedback/r1-review-2026-06-24.md`)** with a sequenced r2 plan.
  > Global priorities r1→r2+: (1) prose tightening / repetition, (2) **mid-section pacing (reviewer's
  > top priority)**, (3) side-character distinction + exposition integration, (4) full continuity pass.
  >
  > **DONE this session:**
  > - **Climax agency fix ("witnessed cost")** — Ch.17 reframed (Drake clears the last obstacle to an
  >   act she's ALREADY begun, not a rescue); Ch.19 opens with **Amber witnessing the cost land**
  >   (returns blind, wrung out). Preserves BINDING 'Drake kills Meros' + 'rebirth in cavern' + the
  >   'none of them know why' capstone. See `feedback/climax-agency-witnessed-cost-2026-06-24.md`.
  > - **Book Two now has its OWN PDF/production pipeline** mirroring Book One, in its own folder:
  >   `REVISION` file + `tools/{assemble_manuscript,build_pdf,make_pdfx}.py/.sh` (+ PDFX_def.ps),
  >   `delivery/production/`. SAME revision policy as Book One (bump `REVISION` BEFORE any rebuild;
  >   keep prior builds as history). **V1 exported = r1**: RGB review PDF + PDF/X-1a, 306pp, ~102,961w.
  > - **r2 Track A done** — Ch.1 opening re-hook (disorientation beat) + recap trim + de-dup of the
  >   'wanted to be unseen→now seen' beat (was in both Ch.1 & Ch.2; Ch.2 now the load-bearing one).
  > - **r2 Track B+D (de-tic/de-dup) batches done** — Ch.3 (vary ch-end refrain dup of Ch.1),
  >   Ch.4 (de-dup 'filed under the heading…' + vary 'one thing that did not fit'), Ch.5 (drop the
  >   'There is a [X]' essay template — Ch.20 keeps it as bookend), Ch.6 (vary doubled tic), plus a
  >   Ch.1 timeline fix ('a whole school year'→'short stretch at Hazel'; Book Two = six weeks).
  > - **r2 PDF CUT** — bumped REVISION r1→r2, rebuilt RGB + PDF/X-1a (306pp, 103,042w); r1 kept as
  >   history. All gates clean throughout. Logged in `feedback/book2-r2-changes.md`.
  > - **KEY FINDING:** the book is in better shape than the r1 note implied. Ch.7 (Varissa
  >   confrontation) & Ch.8 (broadsheet reversal) were de-ticked 2026-06-23 and ALREADY deliver the
  >   friction/escalating-stakes the reviewer wanted; Ch.6 is a strong action beat. The
  >   'creature-monologue' cadence (Ch.5/7) is PLOT-LOAD-BEARING and dramatized — a structural pacing
  >   rewrite there is HIGH-RISK/low-gain and is NOT recommended.
  >
  > **r2 ROUND COMPLETE → r3 CUT (2026-06-24, second session).** All remaining tracks done:
  > - **Track D de-tic sweep FINISHED** across the book (Ch.10/13/14 thinned where NOT load-bearing;
  >   Ch.12/Ch.20 left intact as deliberate count/ledger motifs; climax 15–17 + protected 9/11/16/19
  >   untouched).
  > - **Track E continuity pass = CLEAN** (0 errors): age (no on-page number), Pembrook/rose-tinted/
  >   appearance, the six-weeks-Hazel timeline, the 'no one sees her cry' guardrail (only Ch.16),
  >   Ch.18 cavern matches Book-One Ch.14, no Masters/void-woman. See `feedback/book2-r2-changes.md`.
  > - **Finding #4 DONE** — Ch.18 rebirth overwhelm rewritten from asserted → ENACTED (flood as
  >   dissolving-of-self; Raizen's bond the concrete anchor held hand-over-hand). All binding beats kept.
  > - **r3 PDF cut** (REVISION r2→r3; RGB + PDF/X-1a, 306pp, 103,222w; r2 kept as history). Gates clean.
  >
  > **r4 CUT (2026-06-24) — r3-review response:** (a) **Book One↔Two seam** verified factually
  > consistent (Alice ask, war-clock, spears, rescued children, burned school) and STRENGTHENED —
  > Ch.1 opening now anchors in Book One's closing images (corridor/wood/rescued children/school to
  > smoke), shown not recapped. (b) **All 20 chapters reviewed** vs the r3 feedback; applied
  > clarity-splits to the two genuinely-excessive narration run-ons (Ch.10 224w, Ch.15 292w). Filtering
  > is mostly sight-justified (don't blanket-remove); side-char tics already distinct; other long
  > sentences are deliberate voice/dialogue/climax. r4 PDF cut (RGB + PDF/X-1a, 306pp, 103,247w); r3
  > kept as history. Gates clean.
  >
  > **r5 CUT (2026-06-24) — r4-review response (review strongly positive, "mostly refinement"):**
  > Ch.2 opening-scene sentence splits for rhythm; Book-One continuity re-verified clean; side-char
  > tics confirmed already distinct. **AUTHOR DECISION 2026-06-24: PRESERVE TEXTURE** — declined the
  > conditional mid-book 2–4% "brisk commercial pacing" trim (it trades against the book's literary-
  > voice positioning). r5 stands as the polished version (RGB + PDF/X-1a, 306pp, 103,244w; r4 history).
  >
  > **r6 CUT (2026-06-24) — r5-review response.** CONTINUITY FIX (canon): Ch.4 "a fourteen-year-old"
  > → "a half-grown girl" (violated the Book Two no-age-number-on-page guardrail before the Ch.12
  > turn-to-15; survived the epic-branch scrub). Also fixed a bug in the earlier continuity grep that
  > had falsely cleared it; re-verified names/spectacles/cry-guardrail correctly = clean. Ch.3 opening
  > split for rhythm. r6 PDF cut (306pp, 103,245w; r5 history). Gates clean.
  >
  > ⚠ **PROCESS NOTE:** the r2→r6 external reads are now near-identical positive "fine-tuning" notes
  > (split a couple sentences, light trim already declined, sharpen a side char). The book is at
  > publish-ready polish. **Recommend stopping the per-round revision treadmill** and pivoting to launch
  > prep: front/back matter ([ISBN]/[IMPRINT]/[Dedication]/[Acknowledgments]/bio), query+synopsis
  > (book-packager), physical proof for widows/orphans, then Book Three seed. Further identical rounds
  > risk over-polishing.
  >
  > **TO DO NEXT (resume point) — Book Two is in strong shape; remaining items are author's-call only:**
  > 1. Optional: a fresh external read of r6 to confirm the climax-agency + Ch.18-overwhelm + seam land.
  > 2. Fill print front/back matter placeholders ([ISBN]/[IMPRINT]/[Dedication]/[Acknowledgments]/bio)
  >    before any final print run.
  > 3. Tracks B(structural pacing)/C(side-char) were assessed NOT to need rewrites — the prose already
  >    carries them (Ch.7/8 deliver friction + escalating stakes; creature-monologue is plot-load-bearing).
  > 4. Book Three not started (seed from Series Roadmap + Book Two ENTITY_STATE when ready).
  > - ⚠ **Commits show 'Unverified'** (no GPG/SSH signing key in this env). Email is correct; this is an
  >   environment-config fix (provision a signing key), NOT something to fix by rewriting history.
  >
  > --- (Book Two status / history below) ---
  > ### BOOK TWO IS COMPLETE + REVIEWED + POLISHED — all 20 chapters FINALIZED on `main`, 103,149 words.
  > Every chapter gate-clean (style_check RESULT: clean, em-dash ≤4, rhythm only sanctioned anaphora),
  > canon held, YA tone held.
  >
  > **EXTERNAL REVIEW DONE (2026-06-23)** — two INDEPENDENT passes, artifacts in `feedback/`:
  > - `feedback/beta-read-bookwide.md` — 3-reader beta panel (primary 9/10, hostile 6.5/10, casual 7.5/10).
  > - `feedback/gemini/review-ch{1,14,16,17,18,20}.md` — Gemini cross-model second opinion (via the new
  >   `tools/gemini_review.sh` / `/gemini-second-opinion` command).
  > - `feedback/review-synthesis-2026-06-23.md` — consolidates both. STRONG CONVERGENCE on: (1) protagonist
  >   PASSIVITY / agency-theft at the climax [still OPEN — see below], (2) voice monotony/tics [FIXED, see polish],
  >   (3) the 'instant peace' ending plausibility [FIXED via B], (4) Ch.18 rebirth asserted-not-enacted [still open],
  >   (5) YA buffer banked too late. NOTE: Gemini's push for a gorier on-page beheading was REJECTED (violates the
  >   YA guardrail — the screened-off execution is the book's high-water mark per the beta panel).
  >
  > **POLISH ROUND DONE (2026-06-23), all committed gate-clean, no plot/canon change:**
  > - **C (voice de-tic / rhythm):** Ch.1,3,5,7,8,10,12,18,20 — thinned the worst repeated constructions
  >   ('filed it away', 'the cold working part', recursive 'whole of it') to one load-bearing instance per
  >   scene, split the longest polysyndeton run-ons, added short plain sentences for contrast. Deliberately
  >   LEFT the high-performing emotional chapters (9, 11, 16, 19) untouched.
  > - **B (eerie-not-tidy ending friction):** Ch.18 & Ch.20 — wove FEAR into the stopped battlefield (a man
  >   clawing his chest as if poisoned; a commander screaming at a line that won't re-form; a rifle raised
  >   halfway and lowered; a thin 'witchcraft' no one answers 'because no one knew whether he was right').
  >   Strengthens 'none of them know why' (now includes not knowing whether it was a gift or a violation) —
  >   does NOT soften it. War still gutters out; thesis intact.
  >
  > **STILL OPEN (author's call — NOT done; the two structural items):**
  > - **A — climax agency (the #1 review finding):** Viridia is reactive; at the end a dragon kills Meros
  >   FOR her and the world-mending happens alone in a sealed cave off-stage — even the devoted reader feels
  >   robbed (same root cause as Book One's round-6 passive-protagonist fix). Option: give her one decisive,
  >   hands-on, costly, WITNESSED win (her choice/hand the proximate cause of Meros's defeat, or stage the
  >   rebirth where the cost is seen). This is the biggest lever but a real change to the ending — get author
  >   sign-off before touching it.
  > - **#4 — enact the Ch.18 overwhelm** instead of narrating 'it was too much, it was meant to be too much'
  >   (a larger rebirth-middle rewrite; optional).
  >
  > **NEW TOOLING (this session, committed):**
  > - `tools/gemini_review.sh` + `/gemini-second-opinion <chapter>` — cross-model (Google Gemini) craft
  >   critique tuned for PROSE. Needs `GEMINI_API_KEY` (read from env or out-of-repo `~/.gemini_env`, NEVER
  >   committed; set it as an ENV SECRET in the web-environment config to persist — a pasted key is one
  >   container only). `gemini-2.5-pro` is quota-blocked on the current key (free-tier 0 → needs billing);
  >   runs on `gemini-2.5-flash`. SessionStart hook installs the Gemini CLI when a key is present.
  > - `book/genesis/tools/agent_stop_diag.sh` — diagnoses why a sub-agent stopped (FINISHED vs CUT-OFF/maxTurns).
  > - SessionStart hook hardened: clone-retry + verifies all 12 agents install each session + maxTurns→120.
  >
  > --- (history below) ---
  > Act Three landed in full: Ch.14 battle opens / Brutus dies on the field;
  > Ch.15 Alice freed-but-changed / too-late hook; Ch.16 THE HINGE (Jazen beheaded before both armies,
  > the banked breakdown breaks, camera cut on the act); Ch.17 the decision + **Drake kills Meros
  > (High Chancellor DEAD)**; Ch.18 THE REBIRTH (she PORTALS to the physical Bk1 cavern and mends the
  > 600-year severing for all cores at once; **named cost = mana-sight spent, TEMPORARY, returns slowly =
  > Bk3 thread**; Bella's-name thread touched-unfollowed); Ch.19 wonder+grief (Raizen human form;
  > Lor-ar released; Drake/Varissa goodbye completed; Alice reunited); Ch.20 FINALE (cost counted,
  > faces forward, "none of them know why," **Marick/the-lab seed planted**, void-rim a shade wider — no entity).
  > - **Optional next (author's call):** evaluator/continuity full-book audit pass; `book-packager`
  >   (logline/synopsis/query/cover) + production formatting; then **Book Three** (seed from Series Roadmap
  >   + Book Two ENTITY_STATE; open Bk3 threads: Marick/the lab, the void-rim differential, Bella's-name
  >   thread, Viridia's sight recovering over months).
  >
  > --- prior resume note (history) ---
  > Ch.1–17 finalized; Ch.18 rebirth-location decided by author (portal to the physical Bk1 cavern, not
  > a battlefield reach); Ch.18 cost decided TEMPORARY (sight spent, returns slowly). maxTurns on the
  > book-* agents raised 40->120 (they were stalling mid-gate; see book/genesis/tools/agent_stop_diag.sh).
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
- **Book Three ("The Weight of the Source") IS SCAFFOLDED + SEEDED** at `book/genesis/saeren-chronicles-book-3/`
  (2026-06-24, its own folder/pipeline; single-branch → main). **Genesis-from-roadmap** (no prior author
  draft). Research staged (Book Three roadmap section + magic bible, Book Two ENTITY_STATE, Book Two
  Ch.20 & Ch.18); STATE.yaml filled (premise, canon, **binding beats**, open threads, 95k floor); own
  PDF pipeline mirrored from Book Two. **NEXT: architect pass** (foundation.md + outline.md, ~20–23 ch)
  after resolving open decisions — esp. **Marick (Bk2 Ch.20 seed) vs Fen (roadmap ending)** and the
  **age-on-page** convention (roadmap says she's 16). Binding finale image (do NOT explain): the lab,
  a severed tentacle, Fen runs, Viridia feels the void → the thread to Masters of the Void. See the
  book's own `CLAUDE.md`, `STATE.yaml`, and `feedback/progress.md`.

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
