# CLAUDE.md — Rosalia

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A **genesis-from-idea** project: build a NEW ~100k-word fantasy novel from the author's
story bible (`research/story-bible.md`, pulled from Google Drive "Rosalia"), using the
adapted **Best Seller Studio** pipeline. There is NO original prose draft — the architect
builds foundation + outline + voice-dna from the bible, then the chapter loop writes.

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
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, **em-dash ≤ 4 per
  chapter (absolute)**, no NEW cross-chapter repeated phrase (add deliberate motifs to
  ALLOWLIST), tics under ceiling.
- **Log every flag** in `feedback/style-flags.md`. If a phrase is flagged 3+ times: promote
  to the ALLOWLIST if it's a deliberate motif, or add it to the "watch / kill" list if it's an
  unconscious tic. Track which motifs/phrases keep getting refused so we stop repeating them.

## Word floor
Finished book ≥ `manuscript_min_words` (see STATE.yaml). Verify:
`wc -w manuscript/chapters/chapter-*.md`. If short, expand the thinnest chapters.

## Canon guardrails (settled author decisions — never violate)
- Spelling is **magyk** (not magic) for the in-world power.
- **Vampires** descend from Atlanteans (a failed disease-cure experiment); feudal "protection"
  pact over humans; ruled by a **Queen** with **blood magyk**.
- **Shifters**: human until the first full moon AFTER their 16th birthday; first shift assigns
  them to their animal's clan; ancestral memory trickles in **situationally** (never one info
  dump); all clans under a single **chief**.
- **The Treaty**: no NEW vampires may be made; silent on natural-born vampires (thought impossible).
- **Amelia**: Queen's daughter, first natural-born vampire in millennia, inherited blood magyk;
  hidden her whole life; want = to exist openly. No proof exists she's born vs made.
- **Korvan**: chief's son, UNSHIFTED at the banquet; first shift on the journey home (calendar
  coincidence, NOT magically triggered) → a **dragon**, a clan of one.
- **Loric**: shifter whose father the Queen killed in the last war; motive is emotional (wants
  the Queen to SUFFER); cannot be bought; exposes Amelia publicly so the chief loses either way.
- **Resolved structure**: single ~100k novel; **dual parallel POV** (Amelia + Korvan); dragon
  memory does NOT link to Atlantis; the Queen does NOT remember killing Loric's father.

## Open author decisions (ask, don't invent)
- Is Korvan's mother alive / does he have siblings?
- Does the chief know Korvan's bond with Amelia was genuine?
- Does Korvan confide the garden meeting to anyone, or carry it alone?

## Status (update as you go)
- Scaffolded; bible staged as canon; 4 structural decisions resolved. **Next: architect pass**
  (foundation.md + outline.md + voice-dna.md), then the chapter loop in order.
