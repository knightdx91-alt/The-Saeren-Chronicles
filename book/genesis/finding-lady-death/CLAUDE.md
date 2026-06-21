# CLAUDE.md — Finding Lady Death

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A **genesis-from-opening** project: the author supplied an OPENING SCENE (voice benchmark)
but no plot roadmap. The architect builds foundation + outline + voice-dna FROM that opening,
then the chapter loop writes the rest, matching the seed's voice. Paranormal romance, standalone.

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

## Quality gates (ALL must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **PACING CHECK — required after EVERY chapter.** Assess pacing in context of neighbors:
  scene-vs-summary balance (sag/rush?), dialogue share, the emotional-arc slot (right high/low
  for its place — see foundation.md), hook-and-pull, and chapter length vs. adjacent chapters
  (no chapter >2× another). Log a one-line verdict in `evaluations/` + `feedback/progress.md`;
  fix via book-editor/disruptor BEFORE finalizing.
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤4 per
  chapter (absolute), no NEW cross-chapter repeated phrase (add deliberate motifs to
  ALLOWLIST), tics under ceiling. Log frequent flags in `feedback/style-flags.md`.

## Canon guardrails (settled author decisions — never violate)
- **Alice Haywood** — sees Death since age 9; medical resident (Brookwood Medical Center);
  long black hair; wears the scythe-charm bracelet always (it means she won't die); sole car-
  crash survivor; drawn to the dying.
- **Acheron** — now Death; once a death-obsessed mortal who took the mantle in the Gods' War;
  long black hair, clear blue eyes, hawk nose; black tee w/ white scythe; seen only by the
  near-death or by Alice; black-handled scythe (boatman-with-lantern on the blade) summoned
  from his shirt; calls Alice "little one."
- **The bargain** — Acheron + wife lived a full mortal life; on death he became Death and must
  FIND her reincarnated; when found she becomes **Lady Death**. He's searched thousands of years.
- **Mythos** — the Old Gods' centuries-long War; abandoned domains; mysterious unknown BEINGS
  decreed new gods, stripping the old ones. Acheron is one replacement (Death).
- **Scope/heat** — paranormal romance; STANDALONE ~95k (floor 90k); heat = OPEN DOOR, MODERATE.
- Preserve the opening scene's VOICE as the benchmark.

## Open author decisions (ask, don't invent)
- The central threat: Old Gods returning vs the mysterious beings who deposed them (architect proposing).
- Whether/when Alice becomes Lady Death and what it costs her.
- How much of her past life she remembers.

## Status (update as you go)
- Scaffolded; opening staged as voice benchmark; decisions resolved (paranormal romance,
  standalone ~95k, open-door heat). **Next: architect pass** (foundation + outline + voice-dna).
