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
3. Produce the next chapter IN ORDER. Build from the outline beats — match this book's voice.
   Run each chapter through: write → dialogue-polish → hook-craft → disruptor → **pacing
   check** → evaluate → quality gate.
4. Commit per chapter: `git add -A && git commit -m "genesis: finalize chapter N"`.

## Quality gates (ALL must pass before a chapter is "done")
- **Genesis Floor ≥ 8.5** (book-evaluator); below → book-editor polish loop (max 5).
- **PACING CHECK — required after EVERY chapter.** Before a chapter is finalized, assess its
  pacing and its pacing *in context of the chapters around it*:
  - scene-vs-summary balance; does any stretch sag or rush?
  - dialogue share within the genre band (~30–45%; target ~35%);
  - the emotional "W" — is this chapter's beat the right high/low for its slot in the arc
    (see foundation.md CALIBRATION), or are we stacking too many same-energy chapters?
  - tension/forward pull: does it open with a hook and end with a pull (hook-craft)?
  - chapter length vs. neighbors (no chapter >2× another; watch for bloat or thinness).
  - Log the verdict in `evaluations/` (a one-line pacing note per chapter is fine) and in
    `feedback/progress.md`. If pacing is off, fix via book-editor/disruptor BEFORE finalizing.
- **Style check** — `python3 tools/style_check.py` clean: simile ≤4/1k, **em-dash ≤4 per
  chapter (absolute)**, no NEW cross-chapter repeated phrase (add deliberate motifs to
  ALLOWLIST), tics under ceiling. Log frequent flags in `feedback/style-flags.md`.

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
- **Romance heat:** explicit when it occurs but OCCASIONAL/earned (NOT erotica, no per-page quota). ~3-4 on-page scenes across the arc (Ch.16/18/20 + a late payoff), none after the eruption begins. See STATE.yaml `resolved_author_decisions` for the exact wording.
- **magic spelling:** n/a (this is historical, not invented-magic — the only "magic" is the time-door).

## Open author decisions (ask, don't invent)
- Protagonist name + modern era; father OR grandfather as the archaeologist.
- Ex-gladiator's name + scandal specifics; how she learns WHEN the door opens.
- Treasure-hunter mystery payoff; final choice outcome (stay or go = the ending).

## Status (update as you go)

> ### ▶ NEXT SESSION — START HERE: write Chapter 3 "Coordinates"
> Blueprint COMPLETE (foundation.md + outline.md [45 ch, ~245k] + voice-dna.md), all author
> decisions resolved (see STATE.yaml `resolved_author_decisions`). **Cadence: ONE chapter at a
> time, then the author reviews** before the next.
>
> **Done & committed (both PASS, Genesis Floor 8.5, style gate clean):**
> - Ch.1 "The Drawer" — 4,906w. Grief-low establishing beat; the stuck drawer, the glasses *click*,
>   the obituary laugh, the dead bread-starter, the map arrives.
> - Ch.2 "Too Accurate to Be Fake" — 5,076w. Antique shop, pragmatist shopkeeper, vanished
>   August Fenn, anchor line "The map is honest. The door is not.", ends on Fenn "exactly my age".
>
> **Chapter loop per book (see Quality gates below):** book-writer → (self dialogue-polish/
> hook-craft) → style_check.py → **independent book-evaluator (Genesis Floor ≥8.5 + PACING check)**
> → fix if needed → commit per chapter. Eval reports in `evaluations/`, pacing one-liners in
> `feedback/progress.md`.
>
> **STANDING NOTE for Ch.3 "Coordinates" (from the Ch.2 evaluator):** the outline's Ch.3 anchor
> ("Fenn exactly her age") was spent as Ch.2's final line. **Re-anchor Ch.3 on the fieldwork
> kit-ritual** (loading the 35mm film camera, the wristwatch, the father's dig slides — re-read
> seed #4, load-bearing for the climax) and let the spent photo's dread COLOR the note-reading.
> Ch.3 beats otherwise intact: decode Fenn's notes/coordinates → isolation/fieldwork → travel to
> the site → the threshold. Target ~5,200w; match the Ch.1/Ch.2 voice exactly.
>
> **Resume:** `cd book/genesis/pompeii`; read STATE.yaml + feedback/progress.md + the Ch.2 eval;
> reread chapter-1.md & chapter-2.md for voice; then write chapter-3.md.

--- history ---
- Scaffolded; bible staged as canon; all decisions resolved; architect built the 45-ch blueprint.
- Ch.1 & Ch.2 finalized (see above).

## Other active books in this repo (each on its own branch — for cross-project awareness)
> This session set up several books, each as `book/genesis/<slug>/` on its own branch with the
> same pipeline + pacing gate. Switch branches to work on another.
- **rosalia** (branch `claude/elegant-wright-yyt925`) — vampire/shifter epic-romance; 29-ch ~150k blueprint done; chapter loop not started.
- **pompeii** (branch `claude/pompeii-story`, THIS) — Outlander-style time-slip; Ch.1-2 written.
- **finding-lady-death** (branch `claude/death-and-remembrance`) — paranormal romance; 20-ch ~96k blueprint done; loop not started.
- **the-gift** (branch `claude/the-gift`) — sci-fi antihero thriller; 21-ch ~103k blueprint done; loop not started; pick a company name (Helix Vanguard rec.).
- **son-of-none** (branch `claude/son-of-none`) — empty; awaiting the author's "Son of None" file/idea.
- **the-long-goodnight** (branch `claude/the-long-goodnight`) — empty placeholder.
- (saeren-chronicles is the original, on `main`.)
