# IngramSpark Upload Guide (from a locked phone, via Google Cloud Shell)

This is the exact workflow we used to upload **The Saeren Chronicles** to IngramSpark
from an FRP-locked Android phone whose native file picker doesn't work. Reuse it for
**Book 3** (and re-uploads). Everything here was learned the hard way — the gotchas
are called out so you don't repeat them.

> **About the access token:** there is NO live token saved in this file on purpose.
> GitHub's secret-scanning **auto-revokes any token committed to a repo**, so storing
> one here would be dead within minutes and flag the account. Minting a fresh one
> takes ~30 seconds (Part B, Step 1). That generation step was never the hard part —
> the hard part was the confusion, which this guide removes.

---

## Why we need all this
- The phone is FRP-locked → the OS file picker doesn't work → can't pick files to
  upload to IngramSpark in the normal browser.
- Fix: run a **full Linux desktop with a real browser inside Google Cloud Shell**,
  streamed into the phone's browser. That desktop's file picker works, and the book
  files are downloaded straight into it from GitHub. The phone is just a screen.

---

## PART A — Get a browser GUI running in Google Cloud Shell

Cloud Shell is free with a Google account, runs entirely in the phone's browser, no
install needed. (Note: installed apt packages and the desktop reset between sessions;
your `~` / `~/Downloads` files persist. If you come back later, just re-run Steps 1–3.)

**1. Open** https://shell.cloud.google.com and sign in. Wait for the black terminal.

**2. Install the desktop + a browser.** Chromium is snap-broken in Cloud Shell and
`firefox-esr` was removed from the repo, so we use **real Firefox from Mozilla**.
We use the full **XFCE** desktop (top panel, Applications menu, Thunar file
manager) so you can confirm `~/Downloads` before uploading:

```
sudo apt-get update -y && sudo apt-get install -y xfce4 xfce4-goodies dbus-x11 tigervnc-standalone-server novnc websockify
cd ~ && rm -rf firefox firefox.tar.xz
wget --content-disposition -O firefox.tar.xz "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
tar xf firefox.tar.xz
ls ~/firefox/firefox && echo "FIREFOX OK"
```

(If Firefox later won't launch for missing libs, run:
`sudo apt-get install -y libgtk-3-0 libdbus-glib-1-2 libx11-xcb1`.)

**3. Start the GUI.** The `exec startxfce4` line is critical — if the xstartup
script exits, TigerVNC tears the whole session down (that was the "startup
immediately exiting" bug):

```
mkdir -p ~/.vnc
printf '#!/bin/sh\nunset SESSION_MANAGER\nunset DBUS_SESSION_BUS_ADDRESS\n%s/firefox/firefox &\nexec startxfce4\n' "$HOME" > ~/.vnc/xstartup
chmod +x ~/.vnc/xstartup
tigervncserver -kill :1 2>/dev/null
tigervncserver :1 -geometry 1280x800 -localhost no -SecurityTypes None --I-KNOW-THIS-IS-INSECURE
pkill websockify 2>/dev/null; sleep 1
websockify --web=/usr/share/novnc 8080 localhost:5901 >/tmp/novnc.log 2>&1 &
echo "started"
```

- For a **phone-shaped (portrait)** screen, use `-geometry 800x1280` instead of 1280x800.
- **XFCE gives you a full desktop** — a top panel, an Applications menu, and the
  **Thunar file manager** so you can open `~/Downloads` and confirm the book files
  are really there before the upload. `dbus-x11` is **required** or XFCE half-breaks
  (no panel / no menus). If the desktop comes up grey, wait ~15s for the panel to
  paint, or check `cat ~/.vnc/*.log` for errors. Cloud Shell wipes apt packages
  between sessions, so XFCE is reinstalled each time you come back (re-run Steps 1–3),
  but `~` files (including `~/.vnc/xstartup` and `~/.github_token`) persist.

**4. Open the desktop in the phone browser.** Cloud Shell toolbar (top-right) →
**Web Preview** (monitor/eye icon; may be under a `⋮` overflow on a narrow screen) →
**Change port → 8080 → Change and Preview**. A new tab opens.
- If it shows a **directory listing or 404**, add **`/vnc.html`** to that tab's URL.
- Tap **Connect**. You'll see the XFCE desktop (top panel + Applications menu) with
  Firefox already open.

**5. If the desktop is hard to navigate on the phone:** open the small noVNC tab on
the **left edge** → gear/Settings → **Scaling Mode → Local Scaling** (fits the whole
desktop to your screen, no pinch-zoom). There's also a fullscreen button there.

---

## PART B — Get the book files from GitHub into Cloud Shell

We download the files straight into the Cloud Shell desktop (no native picker needed),
then upload them to IngramSpark from there.

**1. Make a GitHub token** (on the phone's normal browser, already logged into GitHub):
GitHub → **Settings → Developer settings → Personal access tokens → Tokens (classic)
→ Generate new token (classic)** → scope **`repo`** → Generate → **copy it** (`ghp_…`).
Keep it until all uploads are done, then revoke it (Settings → revoke).

> **Use a CLASSIC token, not fine-grained.** A valid classic token is `ghp_` + 36
> chars = **40 characters total**. If `echo -n "$TOKEN" | wc -c` prints anything
> other than 40, the paste grabbed extra/missing characters — that's the usual
> cause of **HTTP 401 "Bad credentials."** Tokens are case-sensitive; never paste
> a token into a chat/log (treat any token that lands in one as compromised and
> revoke it).

**1a. (Recommended) Persist the token so you don't re-paste it every session.**
Cloud Shell wipes apt packages + the desktop between sessions, but **`~` files
survive**. Save the token once into your private home dir (NEVER into this repo —
GitHub secret-scanning auto-revokes any token committed to a repo, so a token in
these docs would be dead within minutes and flag the account):
```
echo 'export GH_TOKEN=PASTE_YOUR_TOKEN_HERE' > ~/.github_token
chmod 600 ~/.github_token
```
Then on every future session, instead of pasting the token, just run:
```
source ~/.github_token
TOKEN=$GH_TOKEN
```
and continue to Step 2. (Alternative: set it as an ENV SECRET in the web-environment
config — same mechanism as `GEMINI_API_KEY` — which persists it to the container
without it sitting in the repo.)

**Sanity-check the token before downloading** (200 = good, 401 = bad paste, 404 = no access):
```
curl -sL -o /dev/null -w "HTTP %{http_code}\n" -H "Authorization: token $TOKEN" \
  "https://api.github.com/repos/knightdx91-alt/The-Saeren-Chronicles"
```

**2. Download the files** — in the Cloud Shell **terminal**, paste this, replacing the
token. (Always `rm -f ~/Downloads/*` first — stale/old files caused upload failures.)

```
rm -f ~/Downloads/*
cd ~/Downloads
TOKEN=PASTE_YOUR_TOKEN_HERE        # ...or if you saved it (Step 1a): source ~/.github_token; TOKEN=$GH_TOKEN
api="https://api.github.com/repos/knightdx91-alt/The-Saeren-Chronicles/contents"
get(){ curl -sL -H "Authorization: token $TOKEN" -H "Accept: application/vnd.github.raw" -o "$2" "$api/$1"; }

# --- change these paths per book; Book-3 paths go under book/genesis/saeren-chronicles-book-3/ ---
# Book One (barcode-fixed cover = r3 PDF/X-1a; interior r14 PDF/X-1a):
#   USE THE -PDFX1a COVER, NOT -CMYK-noicc. The plain CMYK/no-ICC file previews BLANK/WHITE
#   on IngramSpark (and phone viewers) because it has no OutputIntent. PDF/X-1a (CMYK +
#   OutputIntent) is what IngramSpark expects and previews correctly.
#   get "book/genesis/saeren-chronicles/delivery/cover/Saeren-Book-One-FULL-WRAP-r3-PDFX1a.pdf" cover.pdf
#   get "book/genesis/saeren-chronicles/delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r14-PDFX1a.pdf" interior.pdf
get "book/genesis/saeren-chronicles-book-2/delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-r7-GRAY-noicc.pdf" interior.pdf
get "book/genesis/saeren-chronicles-book-2/delivery/cover/Saeren-Book-Two-FULL-WRAP-r2-CMYK-noicc.pdf" cover.pdf
get "book/genesis/saeren-chronicles-book-2/delivery/ebook/Saeren-Chronicles-Book-Two-The-Resistance.epub" book.epub

echo "=== check: want real sizes + %PDF / PK headers, NOT ~112 bytes ==="
for f in interior.pdf cover.pdf book.epub; do printf "%-14s " "$f"; ls -lh "$f"|awk '{print $5}'|tr -d '\n'; printf " hdr="; head -c4 "$f"; echo; done
```

**GOTCHA — the 112-byte file:** if any file is ~112 bytes or its header is `{`, the
token is wrong/revoked and you downloaded a GitHub error message. Mint a fresh token
and re-run. A real file shows `%PDF` (PDFs) or `PK` (epub/docx) and a sensible size.

**3. Upload in Firefox** (inside the Cloud Shell desktop): go to ingramspark.com, and
when its picker opens, choose the files from **Home → Downloads**.

---

## PART C — IngramSpark settings & file rules we learned

**Two formats per title:** "Print (Perfect Bound)" and "eBook" are separate. Each
has its own interior + cover steps. The "Preview my book" button validates *all*
formats, so an empty eBook format will block you even while you're on the print tab.

**Print Perfect Bound:**
- **Interior = the PDF** (6×9, 294pp Book 1 / 306pp Book 2). It is grayscale, no ICC.
- **Cover = the full-bleed wrap PDF** (CMYK, no ICC). On the cover step choose
  **"my cover already includes a barcode"** so IngramSpark doesn't overlay its own
  white barcode box on top of ours.

**eBook:**
- **Interior = the EPUB** (or a .docx). A PDF is rejected here ("ePub or Word
  interior file is required"). EPUB is preferred.
- eBook "page count" field is nominal — enter the print count (e.g. 306) to match.

**Barcode:** our covers have the barcode baked in (print ISBN), **no price add-on**
(per author preference). So always pick "I supply my own barcode."

**The ICC-profile warning** ("PDF CONTAINS ICC COLOR PROFILES…") is a **non-blocking
warning** — you can proceed. Our files are already profile-free, so it should stay
quiet; if it appears, proceed and **order a printed proof** to confirm the interior
text prints solid black (not gray) before approving for sale.

**Cover document size:** IngramSpark's current template wants a **tight full-bleed
wrap** (no white margins). The original wraps were built to the old 15×12 Lightning
Source template with white margins, which shifted the back content into the spine.
We crop them to the true art box. Final sizes used:
- Book 1: **12.911 × 9.249 in** (spine 0.661", 294pp cream)
- Book 2: **12.937 × 9.249 in** (spine 0.687", 306pp cream)

**Title field:** type the title **once**. Entering it repeatedly is what made the
main page show it 3–4×; the files themselves are clean.

---

## PART D — How the print/ebook files are produced (for Book 3, in this repo)

Run these in the book's folder (`book/genesis/saeren-chronicles-book-3/`). Needs
Ghostscript (`sudo apt-get install -y ghostscript`) and Python `pymupdf`,`pillow`,
`numpy`,`python-barcode`.

**1. Interior → grayscale, no ICC** (from the RGB interior build):
```
gs -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=Gray -sProcessColorModel=DeviceGray -dAutoRotatePages=/None \
   -sOutputFile=INTERIOR-GRAY-noicc.pdf  INTERIOR-rN.pdf
```

**2. Cover → crop white margins to full-bleed.** Read the official IngramSpark
template's vector rects (back/spine/front bleed boxes) to get the crop box
`x[backLeft .. 15.0] y[0 .. 9.249]`; raster the wrap at 300 DPI, (regenerate the
EAN-13 barcode with `python-barcode` for the print ISBN, **no add-on**, and paste it
over the old one), crop to the box, save, then:
```
gs -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK -dAutoRotatePages=/None \
   -sOutputFile=COVER-CMYK-noicc.pdf  cover-fullbleed-rgb.pdf
```
(See the Book-2 commit history for the exact barcode-swap + crop script.)

**3. EPUB ISBN swap:** unzip the epub; replace the old eBook ISBN in `OEBPS/content.opf`
(`dc:identifier`), `OEBPS/toc.ncx` (`dtb:uid`), and `OEBPS/copyright.xhtml`; rezip with
**mimetype stored first**:
```
zip -X -q0 OUT.epub mimetype && zip -X -qrg OUT.epub . -x mimetype
```

**Verify any PDF is clean** (no profiles): `OutputIntent` absent and `/ICCBased` absent.

---

## Quick reference — ISBNs used
- Book 1 print: 979-8-2409-9043-4
- Book 2 print: 979-8-2409-9382-4 · Book 2 eBook: 979-8-2561-0025-4
- (Book 3: fill in when assigned.)
