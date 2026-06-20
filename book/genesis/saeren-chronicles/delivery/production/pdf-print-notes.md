# Print PDF — IngramSpark interior notes

**File:** `Saeren-Chronicles-Book-One-6x9-interior.pdf`
**Built by:** `tools/build_pdf.py` (reportlab; regenerate any time after manuscript edits)

## Specs as built
- **Trim size:** 6" × 9" (432 × 648 pt) — exact page size, no crop marks.
- **Page count:** 263 pages.
- **Margins (symmetric, gutter-safe):** sides 0.75", top 0.75", bottom 0.70".
  - IngramSpark minimum is 0.5" from trim; recommended gutter for ≤300 pp is
    ~0.625". 0.75" both sides clears both with margin. (Symmetric margins are
    used instead of mirrored inside/outside — simpler and fully compliant.)
- **Body:** IBM Plex Serif 11/15.5, justified, 16 pt first-line indent
  (no indent on first paragraph of a chapter or after a scene break).
- **Scene breaks:** centered `* * *`.
- **Fonts:** IBM Plex Serif Regular/Italic/Bold all **embedded (subset)**.
  Verified: zero non-embedded / base-14 fonts (the default Helvetica slot was
  overridden to an embedded TTF).
- **Page numbers:** centered footer; body numbering starts at 1 (title page +
  blank verso are unnumbered front matter).
- **No bleed** — correct for a text-only interior (nothing bleeds off-trim).

## Caveat to resolve before final upload (not possible in this environment)
- **Color space / PDF standard:** this PDF is **RGB**, not **PDF/X-1a:2001
  (CMYK + output intent)**, which is IngramSpark's *preferred* format. Text is
  pure black (0,0,0). IngramSpark accepts standard PDFs and will preflight/
  convert, but for a guaranteed pass either:
  1. let IngramSpark's uploader convert it, or
  2. run it through Acrobat Pro "Save as PDF/X-1a" or Ghostscript
     (`gs -dPDFX -dProcessColorModel=/DeviceCMYK ...` with a PDF/X def file).
  Ghostscript/Acrobat are not available here, so that final conversion is a
  one-step manual finish on a machine that has them.

## Front matter
Currently: title page + blank verso, then Chapter One. A retail interior
usually also has a half-title, copyright page, and (optionally) dedication/
epigraph. Say the word and I'll add a proper front-matter section.

## EPUB
A reflowable **EPUB** export (for Kindle/Apple/Kobo and IngramSpark's ebook
channel) is a separate build — see the reminder in chat. Not generated yet.
