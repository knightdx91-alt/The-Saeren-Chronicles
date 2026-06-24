# IngramSpark Submission Checklist — *The Saeren Chronicles, Book One: Hazel Academy*

Everything needed to publish the print paperback through IngramSpark, what is DONE,
and what still needs a human decision or asset. Current build: **r13** (93,728 words).
Requirements verified against IngramSpark's published guidance, June 2026 (sources at end).

---

## TL;DR — what's done vs. what you still need

| Item | Status |
|---|---|
| Interior print PDF (PDF/X-1a, 6×9, 294 pp, fonts embedded, K-only black) | ✅ **DONE** — `delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r13-PDFX1a.pdf` |
| Back-cover copy / description / bio | ✅ **DONE** — `delivery/editorial/10-back-cover-copy.md` + `06-metadata-keywords.md` |
| BISAC categories, keywords, audience, comps | ✅ **DONE** — `delivery/editorial/06-metadata-keywords.md` |
| **ISBN** (one for the paperback) | ⛔ **YOU DECIDE** — buy your own (Bowker) or take IngramSpark's free one (see §1) |
| **Cover PDF** (front+spine+back, one flat wrap) | ⛔ **NEEDS A DESIGNER + official template** (see §3) |
| **Retail price + distribution/returns settings** | ⛔ **YOU DECIDE** at setup (see §5) |
| IngramSpark account | ⛔ Create at ingramspark.com if you haven't |

You can do everything except the **cover** and the **business decisions (ISBN, price)**
right now. The manuscript side is finished.

---

## 1. ISBN — decide first (it drives the cover barcode)

A print book needs its **own** ISBN (separate from any ebook ISBN).
- **Option A — your own ISBN** (Bowker, myidentifiers.com in the US). ~$125 for one,
  cheaper in packs of 10. **You** are the publisher of record; you can use your own
  imprint name ("Post Peleos"), and the ISBN is portable to any printer/retailer later.
  *Recommended if you plan a trilogy* — buy a 10-pack and you're set for all formats/books.
- **Option B — IngramSpark free ISBN.** Free, but the imprint is listed as **"Indy Pub,"**
  it **cannot be transferred** to another account later, and the title **must** go in the
  wholesale distribution program. Fine for a one-off; limiting for a series.
- The 13-digit ISBN becomes the **barcode on the back cover** — so you need it *before*
  the cover is finalized.

## 2. Interior file — ✅ DONE (meets spec)

Verified against IngramSpark print requirements:
- **Format:** PDF/X-1a:2001 (GTS_PDFX marker present). ✓ (IS accepts X-1a:2001 or X-3:2002.)
- **Fonts:** all embedded (TrueType FontFile2 streams). ✓
- **Trim:** 6" × 9" (US trade paperback, standard for YA/epic fantasy). ✓
- **Page count:** 294 (even). ✓ IngramSpark will add their barcode page automatically.
- **Margins:** gutter 0.875", outside 0.625", top 0.75", bottom 0.70" — all exceed the
  0.5" minimum. ✓
- **Color:** body text is K-only black (0/0/0/100), well under the 240% CMYK density cap. ✓
- **Bleed:** none — this is a **text-only interior at exact trim**, which IngramSpark
  accepts. (Interior bleed is only required if art/text runs to the page edge; nothing does.)
- **Regenerate** after any manuscript change: `python3 tools/build_pdf.py && bash tools/make_pdfx.sh`
  (bump `REVISION` first). Upload the **`-PDFX1a.pdf`** file, not the RGB one.

## 3. Cover file — ⛔ the main thing still to make

A wrap cover is **one flat PDF**: back cover + spine + front cover, with bleed.
**Do this in order:**

1. **Generate the official template.** Use IngramSpark's free **Cover Template Generator**
   (in your account / on their site). Enter: trim **6×9**, **paperback**, bind type
   **perfect bound**, page count **294**, and your **paper stock** (see spine note).
   It emails you a PNG/PDF template with the **exact** spine width and wrap dimensions and
   the safe/bleed guides. **Always trust the generator's numbers over any estimate.**
2. **Spine width (estimate — confirm with the generator):**
   - Cream 50# stock: 294 × ~0.0025"/page ≈ **0.735"**
   - White 50# stock: 294 × ~0.0020"/page ≈ **0.588"**
   - *Recommendation:* **cream** stock (warmer, standard for fiction, less show-through).
3. **Wrap math** (with 0.125" bleed all sides): width = 0.125 + 6 + spine + 6 + 0.125 =
   **12.25" + spine**; height = **9.25"**. (≈ 12.985" × 9.25" on cream.)
4. **Barcode area:** leave a clear **1.75" W × 1" H** zone on the **back cover** for the
   ISBN barcode — **100% black on a white background**, no text/art intruding. IngramSpark
   can place the barcode for you from your ISBN, or your designer embeds it.
5. **Cover content needed** (give these to the designer):
   - Front: title *Hazel Academy*, series line *The Saeren Chronicles · Book One*, author
     *Post Peleos*. Art direction in `delivery/editorial/07-cover-brief.md`.
   - Spine: title / author / (optional) series number, reading bottom-to-top.
   - Back: the **back-cover blurb** (`delivery/editorial/10-back-cover-copy.md`), the
     1-line bio, the barcode zone, and price (optional on cover).
   - Export as **PDF/X-1a:2001 or X-3:2002**, fonts embedded, CMYK, ≤240% density,
     bleed included.
6. If you don't have a designer: a cover artist (Reedsy, 100Covers, Miblart, etc.) can
   take the brief + template and deliver a print-ready wrap. This is the one task that
   genuinely needs a visual designer — I can't generate the cover image.

## 4. Title-setup metadata — ✅ copy is written, you enter it at setup

Have these ready to paste into IngramSpark's title-setup form (all drafted already):
- **Title / Subtitle:** Hazel Academy / The Saeren Chronicles, Book One (title field has a
  400-byte limit; you're well under).
- **Series name + number:** The Saeren Chronicles · Book 1.
- **Contributor:** Post Peleos (Author).
- **Description / annotation:** use `delivery/editorial/10-back-cover-copy.md` (book
  description). Keep within IngramSpark's byte limit for the field; the conversion version
  in `06-metadata-keywords.md` is a tighter alternative.
- **BISAC subject codes:** enter **3** (best practice) from `06-metadata-keywords.md` —
  recommend YAF019030 (Fantasy/Epic), YAF019050 (Fantasy/Wizards & Witches),
  YAF018070 (Family/Death, Grief, Bereavement).
- **Keywords:** ≥7, semicolon-separated, 500-char limit — pull from the 15 in
  `06-metadata-keywords.md` (e.g. *grief and loss young adult; magic school fantasy; found
  family fantasy; dragon bond fantasy; coming of age fantasy; lyrical YA fantasy; light and
  dark magic*).
- **Audience:** Young Adult (ages 13–18; crossover adult literary-fantasy).
- **Contributor bio:** 1-liner in `10-back-cover-copy.md`.
- **Publication date / on-sale date, language (English), territory rights, edition (First).**

## 5. Pricing, distribution & returns — ⛔ your business decisions at setup

- **List price (USD):** for a ~300-page 6×9 YA paperback, typical indie range is **$14.99–
  $18.99**. IngramSpark shows your **print cost** and **compensation** per price; pick a
  price that (a) clears print cost + your wholesale discount and (b) sits with comps.
- **Wholesale discount:** commonly **40%** (bookstore-friendly) or 55% (rarely needed).
  Higher discount = better bookstore stocking odds, lower per-unit comp.
- **Returns:** enabling returns (esp. "returnable–destroy") helps bookstores risk stocking
  you; it also means possible returned-copy costs. Many indies enable it for discoverability.
- **Distribution markets/currencies:** set US + UK + AU + EU prices (IngramSpark converts).
- **Ebook (optional):** if you also want the ebook via IngramSpark, that's a **separate
  ISBN** and an EPUB file (not built here — say the word and I'll generate one).

## 6. Final pre-upload validation (quick pass)

- [ ] Interior = the **`-PDFX1a.pdf`** at the current revision (r13), 294 pp.
- [ ] ISBN obtained and entered; barcode zone reserved on cover.
- [ ] Cover built from the **official template** for 294 pp + chosen stock; bleed + barcode correct.
- [ ] Description, 3 BISAC, ≥7 keywords, audience, bio, price all entered.
- [ ] Use IngramSpark's **online proof/preview** (and ideally a **physical proof copy**)
      before approving — check the running heads, page numbers, spine text centering, and
      the widow/orphan flow on a real copy.

---

### Sources (IngramSpark, accessed June 2026)
- File Requirements for Print Books — https://www.ingramspark.com/blog/file-requirements-for-print-books
- Print Book File Guidelines (PDF) — https://www.ingramspark.com/hubfs/downloads/Print-Book-File-Guidelines.pdf
- How to Set Up a Title with IngramSpark — https://www.ingramspark.com/blog/how-to-set-up-a-title-with-ingramspark-part-1
- Title Metadata Guide — https://www.ingramspark.com/lp/title-metadata-guide
- IngramSpark User Guide v3.2 — https://www.ingramspark.com/hubfs/downloads/user-guide.pdf
