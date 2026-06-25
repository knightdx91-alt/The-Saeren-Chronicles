# Uploading book PDFs to IngramSpark from a phone (broken file picker workaround)

This Codespace gives you a full Linux desktop with **Firefox** streamed into your
phone's browser, so you can use a *working* file picker. The book PDFs are already
on disk inside the Codespace — no download needed.

## Steps

1. On **github.com** (phone browser), open the repo `knightdx91-alt/The-Saeren-Chronicles`.
2. Tap the green **`<> Code`** button → **Codespaces** tab → **Create codespace on main**.
   Wait a few minutes for it to build (it installs the desktop + Firefox the first time).
3. When it opens, a **"Desktop (noVNC)"** port should pop up / open automatically.
   If not: open the **Ports** panel, find port **6080**, and open it in the browser.
4. The noVNC page loads → tap **Connect** → password: **`vscode`**.
   You should now see a Linux desktop.
5. **Right-click** the desktop (long-press on mobile) → **Applications → Network → Firefox**
   (or open a terminal and type `firefox-esr &`).
6. In Firefox, go to **ingramspark.com**, log in, and start your title upload.
7. When IngramSpark opens a file picker, navigate to the PDFs already in the workspace:
   - **Book One interior:** `/workspaces/The-Saeren-Chronicles/book/genesis/saeren-chronicles/delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r14-PDFX1a.pdf`
   - **Book One cover wrap:** `/workspaces/The-Saeren-Chronicles/book/genesis/saeren-chronicles/delivery/cover/Saeren-Book-One-FULL-WRAP-r1-PDFX1a.pdf`
   - **Book Two interior:** `/workspaces/The-Saeren-Chronicles/book/genesis/saeren-chronicles-book-2/delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-r7-PDFX1a.pdf`
   - **Book Two cover wrap:** `/workspaces/The-Saeren-Chronicles/book/genesis/saeren-chronicles-book-2/delivery/cover/Saeren-Book-Two-FULL-WRAP-r1-PDFX1a.pdf`
   (Use the `-PDFX1a.pdf` files for IngramSpark — they are the press-ready CMYK/PDF-X versions.)
8. Finish the upload. When done, **stop or delete the Codespace** from github.com →
   Codespaces (so it doesn't burn your free hours).

## Tips for driving a desktop on a phone
- Pinch to zoom; the noVNC toolbar (small tab on the left edge) has a keyboard button
  and settings if you need to type or adjust scaling.
- If Firefox is slow to appear, give it a few seconds after launching.
- Free tier includes ~60 Codespaces hours/month — plenty for uploads.
