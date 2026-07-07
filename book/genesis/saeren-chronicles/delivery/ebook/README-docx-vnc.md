# Getting Book One into a Word doc (and up to Google Docs) from a VNC / Cloud Shell

This is the step-by-step for producing the upload-ready **Word (.docx)** of
Book One and getting it into Firefox inside your VNC session — formatted so it
looks the **same in Google Docs, Word, and everywhere else**, with the title,
copyright, and dedication each on their own page (just like the PDF).

You already know how to bring up the VNC and get Firefox running. This doc only
covers **making the book file and uploading it**.

---

## TL;DR — the one command

Open a terminal in your Cloud Shell / VNC session and run:

```bash
# clone once (skip if you already have the repo):
git clone https://github.com/knightdx91-alt/the-saeren-chronicles.git
cd the-saeren-chronicles

# pull latest + build the Word doc in one shot:
bash book/genesis/saeren-chronicles/tools/make_docx.sh
```

When it finishes it prints the exact path, e.g.:

```
 DONE. Upload this file:
   .../delivery/ebook/Saeren-Chronicles-Book-One-Hazel-Academy-r15.docx
```

That `.docx` is what you upload. Done. The rest of this doc explains each piece
and how to open/upload it inside the VNC.

---

## What the build produces

`Saeren-Chronicles-Book-One-Hazel-Academy-<rev>.docx` — a single Word file laid
out exactly like the print PDF:

| Page | Content |
|------|---------|
| 1 | Half-title (THE SAEREN CHRONICLES) |
| 2 | Title page (title + *Book One: Hazel Academy* + author) |
| 3 | Copyright page (ISBN, rights, first edition) |
| 4 | Dedication |
| 5+ | **Chapter One** — and every chapter starts on a fresh page |
| end | About the Author · Acknowledgments · Book Two teaser |

- Letter size (8.5 × 11), 1" margins — the standard Google Docs / Word page.
- Georgia serif, 12pt, 1.5 line spacing, justified body, first-line indents.
- Scene breaks rendered as centered `* * *`.
- The revision (r15, r16, …) is read from the `REVISION` file automatically and
  stamped into the filename, so you always know which cut you uploaded.

---

## Why this fixes the "bunched together" problem in Google Docs

When you paste prose into Google Docs — or let Docs *convert a PDF* — the
paragraphs collapse into one another because the source used soft line-breaks,
filler paragraphs, or a page geometry Docs ignores.

This build sidesteps all of it. It writes **real Word structures** that Google
Docs, Word, and LibreOffice all honor identically:

- one true paragraph per paragraph (no manual line breaks inside prose);
- **hard page breaks** between every front-matter piece and before every
  chapter — these survive the Google Docs import, so nothing runs together;
- indentation + justification set on the paragraph *style*, not tabs or spaces;
- a font Google Docs actually has (Georgia), so there's no substitution reflow.

Result: open it in Google Docs and it looks the same as in Word — title,
copyright, and dedication each on their own page, chapters cleanly separated.

---

## Opening / uploading it inside the VNC

The file lives on the Cloud Shell filesystem. Two easy ways to get it into your
uploader:

### A. Upload straight from Firefox in the VNC
1. Go to <https://docs.google.com> (or your publishing site) in the VNC's Firefox.
2. Choose **Open / Upload** (in Google Docs: the folder icon → **Upload** tab).
3. In the file picker, navigate to the path the script printed, e.g.
   `.../the-saeren-chronicles/book/genesis/saeren-chronicles/delivery/ebook/`
   and pick `Saeren-Chronicles-Book-One-Hazel-Academy-<rev>.docx`.
4. Google Docs converts it on upload — it will keep the page breaks and layout.

> Tip: to make the folder easy to find in Firefox's file picker, copy the file
> to your home or Desktop first:
> ```bash
> cp book/genesis/saeren-chronicles/delivery/ebook/Saeren-Chronicles-Book-One-Hazel-Academy-*.docx ~/
> ```

### B. Pull it down to your own machine (if the VNC has the download panel)
Most Cloud Shell VNCs expose the file browser / download button — use it on the
printed path, then upload from your laptop as usual.

---

## Keeping the Google Docs copy looking right

- Upload the `.docx` and let Google Docs **convert** it (don't copy-paste the
  text — pasting is what bunches it).
- After conversion, `File → Page setup` should already show Letter / 1" margins.
- If you ever need it double-spaced for a narrator/ACX pass instead, open
  `tools/build_docx.py` and change `LINE_SPACING = 1.5` to `2.0`, then rebuild.

---

## Rebuilding after the book changes

The script always uses the **current revision**. If the manuscript was revised
and the `REVISION` file bumped (say r15 → r16), just run the one command again;
you'll get `...-r16.docx`. The prior `...-r15.docx` stays as history.

```bash
bash book/genesis/saeren-chronicles/tools/make_docx.sh
```

---

## If something goes wrong

- **`python-docx` not found** — the script installs it, but you can do it
  manually: `pip install python-docx`.
- **`missing full-manuscript-<rev>.md`** — run the assembler first:
  `python3 book/genesis/saeren-chronicles/tools/assemble_manuscript.py`
  (the script already does this for you).
- **Pull says "skipped — offline"** — the build still runs on your local copy;
  just make sure you `git pull` when you're back online to get the latest cut.
