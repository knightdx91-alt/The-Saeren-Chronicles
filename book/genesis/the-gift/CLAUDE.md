# CLAUDE.md — The Gift

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A **genesis-from-opening+notes** project: the author supplied a finished Chapter 1 (AO3 work
45324940, staged as the voice benchmark) plus detailed continuation notes
(`research/author-continuation-notes.md`). The architect builds foundation + outline + voice-dna
from those; the chapter loop writes the rest. Near-future sci-fi thriller, multi-POV, series.

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
  scene-vs-summary balance, dialogue share, the emotional-arc slot, hook-and-pull, and length
  vs. adjacent chapters (no chapter >2× another). Log a one-line verdict in `evaluations/` +
  `feedback/progress.md`; fix before finalizing.
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, em-dash ≤4 per
  chapter (absolute), no NEW cross-chapter repeated phrase (ALLOWLIST motifs), tics under ceiling.

## Canon guardrails (settled author decisions — never violate)
- **ORIGINAL IP ONLY.** X-Men is Troy's in-world *fandom*; the story's powers/characters/teams
  must be original — NO Marvel names/trademarks in the story world. Powers are archetypes
  (phasing, bio-electricity) described originally.
- **The three MCs:** Troy (genetics prodigy, self-experiments first), Raven (phasing), Knight
  (bio-electric blood, electric-blue eyes). Sympathetic antiheroes.
- **Engine:** public biotech (designer babies / disease-gene removal) secretly funds seeding a
  Goldilocks-zone planet — "A New World" / hidden "A New World At Any Cost." Modified settlers;
  orphan children as the resilient base; deadly wilderness camp; a one-way wormhole as endgame.
- **Antagonist clock:** grieving govt investigator (daughter died from another company's work)
  hunts Troy.
- **Scope/heat:** multi-POV; SERIES, Book One ~100k (floor 95k), ending on the launch/escape;
  Troy/Raven strong thread, OPEN-DOOR MODERATE heat.
- Preserve the Ch.1 voice benchmark; build to `research/author-continuation-notes.md`.

## Open author decisions (ask, don't invent)
- Exact Book One endpoint / who makes it through the wormhole; how far the antiheroes go on-page
  with the children; the investigator's name; assistant & key-kid names; city setting.

## Status (update as you go)
- Scaffolded; Ch.1 + continuation notes staged; decisions resolved (antiheroes, multi-POV,
  series Bk1 ~100k, open-door moderate heat). **Next: architect pass.**
