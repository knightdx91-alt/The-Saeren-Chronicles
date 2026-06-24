# Book Two — Production Notes

## Revision policy (same as Book One)
`book/genesis/saeren-chronicles-book-2/REVISION` is the single source of truth for
the build tag (e.g. `r1`). **Bump it BEFORE rebuilding**, then rebuild; the prior
build files (`...-r1.pdf`, `full-manuscript-r1.md`) are kept as history and the new
build carries the new tag. No manuscript/PDF update ships without a revision bump.

## Build pipeline
```
cd book/genesis/saeren-chronicles-book-2
python3 tools/assemble_manuscript.py   # -> manuscript/full-manuscript-<rev>.md
python3 tools/build_pdf.py             # -> delivery/production/...-interior-<rev>.pdf  (RGB)
bash    tools/make_pdfx.sh             # -> delivery/production/...-interior-<rev>-PDFX1a.pdf  (CMYK/PDF-X-1a)
```

## Spec (mirrors Book One)
- Trim 6" × 9"; margins side 0.75", top 0.75", bottom 0.70" (gutter-safe ≤ ~500pp).
- IBM Plex Serif, fully embedded; body 11/15.5pt justified, 16pt indent.
- Chapter-title running heads; page numbers start at 1 on Chapter One.
- Even physical page count (auto-padded) for perfect binding.
- Body text is pure K-only black, so the CMYK pass yields clean black with no rich-black.

## Current build
- **r1 (V1)** — 20 chapters, 102,961 words, **306 pages** (even).
  - `Saeren-Chronicles-Book-Two-6x9-interior-r1.pdf` — RGB review/proof copy.
  - `Saeren-Chronicles-Book-Two-6x9-interior-r1-PDFX1a.pdf` — PDF/X-1a:2001 (IngramSpark).
- Front/back matter use placeholders ([ISBN], [IMPRINT], [Dedication],
  [Acknowledgments], expanded bio) — fill before final print.
- r1 includes the climax-agency "witnessed cost" revision (Ch.17 reframe + Ch.19
  Amber witness beat); see `feedback/climax-agency-witnessed-cost-2026-06-24.md`.
