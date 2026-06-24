# Progress — The Saeren Chronicles — Book Three: The Weight of the Source

Scaffolded + seeded 2026-06-24. **Genesis-from-roadmap** (no prior author draft).

## ▶ RESUME HERE: author-confirm the open items, then draft Ch.1
**Architect pass DONE** — `foundation.md` + `outline.md` (22 chapters, 3 acts: Unsettled World 1–7 /
The Pull 8–15 / Balance 16–22). Resolution = BALANCE not victory; the gut-punch (Horrors pulled
toward the source = she made them) lands Ch.10; the binding final image (Fen runs / Viridia feels the
void) closes Ch.22. Before drafting Ch.1, get author sign-off on the §6 open items in `foundation.md`
(time-skip ≈1 year; Mrs. Zoran in/out; Bella-thread attempt or hold; pact/Dangris; chapter count 22),
then edit `tools/style_check.py` ALLOWLIST with Book-Three motifs.

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

### Resolved (author, 2026-06-24)
- **Marick vs Fen:** Marick OPENS the portal (Bk2 Ch.20 seed); **Fen is his assistant who RUNS** at
  the end. Two people; Fen is new to Book Three.
- **Age on-page:** Book Three MAY state she is sixteen plainly (Book Two's no-number rule was for the
  private 14→15 turn; verified Book Two has no Viridia age-number after the r6 fix).
- **Roadmap reconciled against finished Books 1 & 2** → `research/roadmap-vs-books-reconciliation.md`.
  Biggest override: her mana-SIGHT is SPENT at open and returns slowly (NOT "feels every core at all
  times"); Alice taught Viridia Moravian (bible was reversed); Death symbol closes portals (the spine);
  Raizen is human; void-rim abstract; source = the physical Book One cavern. Finished books win.

### Next steps (in order)
1. **Resolve the remaining open decisions** (Mrs. Zoran's status; time-skip length for age 16;
   Raizen's affinity; pact-and-Dangris) — ideally with the author before/at the architect pass.
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
