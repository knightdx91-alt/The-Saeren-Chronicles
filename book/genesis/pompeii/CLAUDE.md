# CLAUDE.md — Pompeii (working title)

Per-book playbook. A fresh Claude Code session should read this first, then continue.
(This is a copy of the template; fill in the <…> placeholders for this book.)

## What this is
A **genesis-from-idea** project: build a NEW long Outlander-style time-slip historical
romance from the author's story bible (`research/story-bible.md`), using the adapted
**Best Seller Studio** pipeline. There is NO original draft — architect builds
foundation + outline + voice-dna from the bible, then the chapter loop writes.

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

## Canon guardrails (settled author decisions — never violate)
- **Comp/tone:** Outlander — sweeping, romantic, immersive, historically grounded "to a point."
- **Scope:** ONE long standalone (~260k target / 220k floor) running through the eruption + final choice.
- **History:** Flavian era. Arrive ~70 AD (Vespasian); ~9-year span; **Vesuvius erupts 79 AD under Titus.** NOT Nero (died 68). Keep the political backdrop accurate.
- **The map:** purports to lead to the lost **Library of Alexandria**; real secret = a door through time. From the estate sale of a vanished self-proclaimed treasure hunter (left notes + coordinates).
- **Mechanism:** coordinates open a time-door; she lands in **Greece (Delphi)**; the **Oracle** tells her WHERE the door home is (Pompeii) but NOT WHEN; she learns the "when" later.
- **Greece first:** a lone foreign woman in antiquity can't just travel — real obstacle, not hand-waved.
- **Love interest:** disgraced **ex-gladiator** accused of an affair with the emperor's wife; they marry + have children over years.
- **Climax:** family can't pass to the future; **stay vs. leave** as Vesuvius erupts.
- **Romance heat:** EXPLICIT / spicy (on-page detailed intimacy).
- **magic spelling:** n/a (this is historical, not invented-magic — the only "magic" is the time-door).

## Open author decisions (ask, don't invent)
- Protagonist name + modern era; father OR grandfather as the archaeologist.
- Ex-gladiator's name + scandal specifics; how she learns WHEN the door opens.
- Treasure-hunter mystery payoff; final choice outcome (stay or go = the ending).

## Status (update as you go)
- Scaffolded; bible staged as canon; core decisions resolved (Flavian era, Library map,
  standalone, explicit heat). **Next: architect pass** (foundation + outline + voice-dna).
