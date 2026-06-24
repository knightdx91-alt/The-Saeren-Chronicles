# Book One r12 — Change Log (for Book-Two cross-check)

Author-directed close-out of the 4th beta review (2026-06-24). PROSE UNCHANGED from
r11; the r12 deltas are production (running heads + real back matter) plus a verified
proofread/continuity pass.

---

## Production: chapter-title running heads (author chose "chapter-title heads")
- **tools/build_pdf.py** · added centered chapter-title running heads in the top margin
  of every body page, via a measurement pass that maps each page to its chapter. Heads
  are SUPPRESSED on chapter-opening pages and on all back matter (standard convention).
  Verified in the build: p9 shows "The Path to Hazel"; the Ch.1 opener (p7) shows only
  the chapter heading, no running head. Widows/orphans still enforced. · none

## Production: real Book Two back matter (author chose "add it now")
- **tools/build_pdf.py** · replaced the "Book Two / Coming soon" stub with a titled
  teaser — "Book Two: The Resistance" + a real excerpt from Book Two Ch.1 (the camp /
  Brutus opening + the war-clock "the count" beat) + a one-paragraph series note. Verified
  rendered on the final pages. · **Book-Two touchpoint:** excerpt copied verbatim from
  saeren-chronicles-book-2/manuscript/chapters/chapter-1.md — keep in sync if Book Two's
  opening is ever revised. The teaser also uses the established Book Two title "The
  Resistance." VERIFIED against current Book Two.

## Proofread + continuity pass (author chose "run it now")
RESULT: clean except one flagged timeline item (below).
- **Spelling/canon:** all "Pembrook" correct; no Jasen/Pembroke/Raisen slips; no doubled
  words; codespell's 3 hits are false positives ("singed" = burned in fire scenes Ch.16/17;
  "patter" = Mrs. Zoran's chatter Ch.3). No changes needed.
- **Age:** Viridia "fourteen" consistent throughout (the "fifteen years" in Ch.13 is an
  unrelated honour). ✓
- **Rose-tinted spectacles:** Lightwell always rose; the silver lenses are the Chancellor's,
  the silver-and-gold pair a Book-Two council woman — different characters. ✓
- **Blue shoes:** consistent (Ch.1/2/6/12/15, "the same plain scuffed blue"). ✓
- **Timeline — FLAGGED for author:** the established span is SIX WEEKS at school
  (Ch.18:113 "arrived six weeks ago"; Book Two Ch.1 "six weeks at a school"). The test is
  at "three weeks" (Ch.14). But **Ch.18 line 7** reads "because three weeks had taught her
  that grief fought at the door only comes in through the window" — at six weeks in, this
  grief-duration "three weeks" looks stale. Likely should be "six weeks" (or neutral "the
  weeks"). NOT changed unilaterally (touches the timeline) — awaiting author go/no-go.

## Build
- REVISION r11 → r12. Rebuilt full-manuscript-r12.md, r12 RGB interior PDF (with running
  heads + Book Two teaser), and r12 PDF/X-1a. Style gate CLEAN; 93,733 words; 294 pp.
