# Reviewer Skills (reusable manuscript-QA toolkit)

Six read-only review skills that analyze a finished/draft manuscript and write reports
to `<book>/evaluations/review/`. They never edit prose — they diagnose.

| Skill | What it does |
|-------|--------------|
| analytical-peer-reviewer | Sequential passes: plot structure, theme, stakes, promise/payoff, claim-vs-achievement |
| pacing-heatmap | Per-chapter tension/momentum heatmap; flags drag and rush |
| character-arc-consistency | Tracks majors for motivation consistency; flags regressions/stalls |
| voice-dna-calibration | Style/voice match + anti-AI pattern scan; runs tools/style_check.py |
| beta-reader-panel | 4–5 distinct reader personas pressure-test for blindspots/confusion, then synthesis |
| info-dump-detector | Flags momentum-killing exposition; proposes dramatize/distribute/demote/delete |

## Install (fresh environment)
    cp book/genesis/_reviewer-skills/*.md ~/.claude/agents/

## Use
Dispatch each as an Agent `subagent_type` (if your environment registers them), or run
ONE general-purpose agent that performs each role by reading these files. Point it at a
book dir (e.g. book/genesis/saeren-chronicles); reports land in that book's
evaluations/review/. Run AFTER drafting/reva pass — they inform the next revision.
