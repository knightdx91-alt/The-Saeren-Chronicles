# Progress — The Saeren Chronicles — Book Three: The Weight of the Source

Scaffolded + seeded 2026-06-24. **Genesis-from-roadmap** (no prior author draft).

## ▶ RESUME HERE: architect pass
Everything is staged. The next step is the **architect pass** — build `foundation.md` +
`outline.md` from the Series Roadmap's Book Three section, then run the chapter loop.

### Done
- Folder scaffolded in its own project: `book/genesis/saeren-chronicles-book-3/`.
- Research staged in `research/`:
  - `series-roadmap-book3.md` — BINDING (premise, 3 conflict levels, KEY REVELATION = Horrors pulled
    toward the source, RESOLUTION = balance, ENDING = the lab/Fen/void, full magic-system bible).
  - `book2-ENTITY_STATE.yaml` — continuity anchor (entities/threads at end of Book Two).
  - `book2-final-chapter-20.md` — Book Three opens months after this; holds the **Marick/lab** and
    **void-rim differential** seeds.
  - `book2-chapter-18-rebirth.md` — the rebirth + its named cost (sight spent, returns slowly) +
    the physical source-cavern.
- `STATE.yaml` filled (premise, canon guardrails, binding beats, open threads, word floor 95k,
  per-chapter floor 4,600).
- Own PDF/production pipeline mirrored from Book Two: `tools/{assemble_manuscript,build_pdf,make_pdfx}`
  + `PDFX_def.ps` + `rhythm_check.py` + `style_check.py`. (No `REVISION` file yet — create it = `r1`
  only when the first build is cut, per the bump-before-rebuild policy.)

### Next steps (in order)
1. **Resolve the open author decisions** (see STATE.yaml `open_author_decisions`) — especially
   **Marick vs Fen** and the **age-on-page** convention — before drafting.
2. **Architect pass:** `foundation.md` (premise/voice-DNA carried from Books One/Two, themes, magic
   rules as they now stand post-rebirth, the void/Horror logic) + `outline.md` (~20–23 chapters across
   three acts: the unsettled new world → the Horrors / the discovery that she is the cause → balance).
3. Edit `tools/style_check.py` ALLOWLIST with Book Three's deliberate motifs.
4. Run the chapter loop (write → dialogue-polish → hook-craft → disrupt → evaluate → gate),
   SEQUENTIALLY, each chapter ≥4,600w, style + rhythm clean, voice-matched, canon held vs Books One/Two.
   Commit per chapter to `main`.
5. Cut PDFs via the pipeline once chapters exist (create `REVISION`=`r1`, then assemble → build_pdf
   → make_pdfx; keep prior builds as history).

### Open author decisions (blockers to flag before drafting)
- **Marick vs Fen** (Book Two Ch.20 planted Marick; roadmap ending names Fen) — reconcile.
- **Age on-page** (roadmap says Viridia is 16; Book Two kept no number on-page) — decide.
- Raizen's elemental affinity; pact-and-Dangris; Mrs. Zoran's role.
