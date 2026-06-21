# IngramSpark Print-Production Spec — The Saeren Chronicles, Book One: The Hazel Years

**Author/Imprint:** Post Peleos (imprint line placeholder `[IMPRINT]`)
**Build:** r7 (~93,677 words)
**Interior file:** `delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r7.pdf`
**Built by:** `tools/build_pdf.py` (reportlab) → regenerate after any manuscript change.

---

## 1. Trim & page count

- **Trim size:** 6" × 9" (US trade paperback; standard for YA/epic fantasy).
- **FINAL PAGE COUNT: 293 pages** (physical pages, including front + back matter).
  - Front matter (6 pp, unnumbered): half-title, blank, title, copyright,
    dedication, blank.
  - Body: Chapter One begins on a recto (physical p7), page number "1".
  - Back matter: About the Author, Acknowledgments, Book Two teaser.
  - IngramSpark requires the page count to be **even** for perfect binding —
    293 is **odd**. Add **one** blank page (e.g. a final blank verso) at upload
    or in `build_pdf.py` to reach **294** before submitting. The spine math below
    uses **294** as the bind-ready count.

> Bind-ready page count for ordering/spine: **294 pp.**

---

## 2. Spine-width calculation (cover only — interior has no spine)

**Formula:** `spine width (in) = interior page count × per-page caliper (in/page)`

Caliper depends on paper stock. IngramSpark's typical published values:

| Stock | Caliper (in/page) | Spine @ 294 pp |
|-------|-------------------|----------------|
| **Cream** (50# / 80 gsm uncoated) | ~0.0025 | 294 × 0.0025 = **0.735"** |
| **White** (50# / 80 gsm uncoated) | ~0.0020 | 294 × 0.0020 = **0.588"** |

> **MUST CONFIRM:** Caliper varies by IngramSpark's current paper and region.
> Before building the cover, generate the **official cover template** from
> IngramSpark's cover-template generator for *your* exact trim, page count, and
> paper stock — it returns the authoritative spine width and wrap dimensions.
> The numbers above are estimates from typical IS calipers and must be verified.

**Recommendation:** Cream stock is the convention for fiction (warmer, less
show-through, easier on the eye for long reads). Use cream unless the cover
designer needs the slightly narrower white spine.

---

## 3. Full cover-wrap dimensions (front + spine + back + bleed)

Bleed = **0.125"** on all four sides. Wrap is one flat sheet.

```
Wrap width  = bleed + back cover + spine + front cover + bleed
            = 0.125 + 6 + spine + 6 + 0.125
            = 12.25 + spine
Wrap height = bleed + trim height + bleed
            = 0.125 + 9 + 0.125 = 9.25"
```

| Stock | Spine | **Full wrap (W × H)** |
|-------|-------|-----------------------|
| Cream | 0.735" | **12.985" × 9.25"** |
| White | 0.588" | **12.838" × 9.25"** |

Safety/live area: keep all text and essential art **≥ 0.125"** inside trim on
front/back, and **≥ 0.0625"** in from each spine edge (spine text only if spine
≥ ~0.0625"; at 0.59–0.74" there is room for a thin title/author spine line).

Back cover must leave clear space (bottom-right, ~2" × 1.2") for the
**ISBN barcode** that IngramSpark places automatically (or supply your own).

---

## 4. Interior PDF requirements (status of the file as built here)

| Requirement | Status in r7 interior |
|---|---|
| Exact trim page size 6"×9", no crop marks | ✓ (IngramSpark wants trim-size pages, no marks) |
| Fonts fully embedded (subset) | ✓ IBM Plex Serif R/It/Bd/BdIt; Helvetica slot overridden to embedded TTF |
| Body & heading text pure black (K-only) | ✓ set to `CMYKColor(0,0,0,1)` so it converts to **100% K, 0 CMY** |
| Margins ≥ 0.5" from trim | ✓ sides 0.75", top 0.75", bottom 0.70" (gutter-safe for ≤500 pp) |
| No bleed in interior (text-only) | ✓ nothing bleeds off-trim |
| Page numbering starts at 1 on Chapter One | ✓ front matter unnumbered |
| **Color space = CMYK / PDF/X-1a:2001** | ✗ **NOT done here** — see §5 |
| Even page count for binding | ✗ currently 293 — add one trailing blank → 294 |

---

## 5. The CMYK / PDF/X-1a finish step (CANNOT be done in this environment)

This environment has **no Ghostscript and no Acrobat**, so the file is an
embedded-font, exact-trim **RGB** PDF with pure-black (K-convertible) text.
IngramSpark *prefers* **PDF/X-1a:2001 (CMYK + output intent)**. Do ONE of these
on a machine that has the tools:

**Option A — Acrobat Pro (simplest, recommended):**
1. Open the interior PDF.
2. File → Save As Other → **PDF/X** → choose **PDF/X-1a:2001**.
   (or Print Production → Preflight → "Convert to PDF/X-1a" profile)
3. Output intent: **U.S. Web Coated (SWOP) v2** (IngramSpark's standard).
4. Save and upload.

**Option B — Ghostscript (command line):** create a PDF/X definition file
`PDFX_def.ps` (sets the SWOP output intent / ICC), then:

```
gs -dPDFX -dBATCH -dNOPAUSE -dNOOUTERSAVE \
   -sProcessColorModel=DeviceCMYK \
   -sDEVICE=pdfwrite \
   -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=CMYK \
   -sOutputICCProfile=USWebCoatedSWOP.icc \
   -sOutputFile=Saeren-interior-X1a.pdf \
   PDFX_def.ps Saeren-Chronicles-Book-One-6x9-interior-r7.pdf
```

Because all text is already K-only black, this conversion should keep text as
100% K with no rich-black artifacts.

**Option C — let IngramSpark convert it.** IS accepts standard PDFs and runs a
preflight/normalize. Acceptable, but A or B gives a guaranteed, predictable pass.

---

## 6. Pre-upload checklist

### Interior
- [ ] Page count made **even** (add trailing blank → 294 pp).
- [ ] Fonts embedded (confirmed ✓ in r7).
- [ ] Text pure K-only black (confirmed ✓ in r7).
- [ ] Margins ≥ 0.5", gutter adequate for 294 pp (✓).
- [ ] No crop marks / no bleed in interior (✓).
- [ ] Front matter complete: half-title, title, copyright (fill `[ISBN]`,
      `[IMPRINT]`), dedication (fill `[Dedication]`).
- [ ] Back matter: About the Author (`[EXPANDED BIO OPTIONAL]`),
      Acknowledgments (`[Acknowledgments]`), Book Two teaser.
- [ ] Converted to PDF/X-1a:2001 CMYK (manual step §5) — or accept IS convert.
- [ ] Visual proof of widow/orphan run (see `pdf-print-notes.md`).

### Cover
- [ ] Spine width from **IngramSpark's official template** for 294 pp + chosen stock.
- [ ] Wrap size matches template (cream ≈ 12.985"×9.25", white ≈ 12.838"×9.25").
- [ ] 0.125" bleed all four sides.
- [ ] ISBN barcode area kept clear (bottom-right back cover).
- [ ] Cover is CMYK, 300 DPI, flattened, fonts embedded/outlined.

### Metadata / account
- [ ] ISBN assigned (replace `[ISBN]` in copyright + cover barcode).
- [ ] Title, author "Post Peleos", BISAC categories, price set in IS dashboard.
- [ ] Paper stock selection in IS matches the spine width you built.

---

## UPDATE (2026-06-21): CMYK / PDF/X-1a is now generated automatically

The earlier note that PDF/X-1a could not be produced in this environment is
**superseded** — Ghostscript is now installed. Run `bash tools/make_pdfx.sh`
after `tools/build_pdf.py` to generate
`Saeren-Chronicles-Book-One-6x9-interior-<REV>-PDFX1a.pdf` (CMYK, OutputIntent,
embedded fonts, even 294-page count). Verified compliant. For an exact press
match, replace the ICC path in `tools/PDFX_def.ps` with a SWOP/printer profile.
