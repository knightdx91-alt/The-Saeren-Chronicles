# Rosalia — Style-Flag Tracker

Running log of what the style gate (`tools/style_check.py`) keeps flagging, so we can
spot patterns instead of fixing the same thing chapter after chapter.

## Rules
- **Em-dashes: max 4 per chapter** (absolute). Enforced by `--max-emdash 4` (the default).
- **Simile/metaphor markers: ≤ 4.0 per 1,000 words.**
- **No NEW repeated 4–6 word phrase across chapters** (deliberate motifs go in the ALLOWLIST).
- **Verbal tics: ≤ 6.0 per 1,000 words** for any single tic word.

## How to use this file
After each `python3 tools/style_check.py` run, log anything flagged below.
- If a phrase is flagged **3+ times** and it's a *deliberate* recurring motif → promote it to
  the ALLOWLIST in `tools/style_check.py` (and note it here).
- If a phrase/tic is flagged repeatedly and is **NOT** deliberate → it's an unconscious tic;
  add it to the "watch / kill" list so the writer/disruptor stops reaching for it.

## Approved motifs (in ALLOWLIST — intentional, do NOT "fix")
- "only what everyone saw"
- "eats voices"
- "survive to fight later"  (the Chief's creed)

## Frequently-flagged phrases (count → disposition)
_(none logged yet — populate during the chapter loop)_

| Phrase / tic | Times flagged | In chapters | Deliberate? | Disposition |
|---|---|---|---|---|
| | | | | |

## Watch / kill list (unconscious tics to avoid)
_(none yet)_
