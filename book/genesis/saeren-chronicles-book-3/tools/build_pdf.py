#!/usr/bin/env python3
"""
Build a print-ready interior PDF of Book Three to IngramSpark interior specs.

Trim: 6" x 9" (standard YA/fantasy trade paperback).
Margins: side 0.75", top 0.75", bottom 0.70" (gutter-safe for <=~500pp).
Fonts: IBM Plex Serif (Regular/Italic/Bold/BoldItalic), fully embedded.
Body: 11pt / 15.5pt leading, justified, 16pt first-line indent (no indent on
  the first paragraph of a chapter or after a scene break).
Output: delivery/production/Saeren-Chronicles-Book-Three-6x9-interior-<rev>.pdf

Mirrors Book One's build_pdf.py (same geometry, font embedding, running heads,
even-page padding). This produces an embedded-font, exact-trim RGB PDF; the
final PDF/X-1a:2001 (CMYK) conversion needs Ghostscript (see make_pdfx.sh).
"""
import os, re, html
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, PageBreak, NextPageTemplate)

# Pure K-only black for text: converts cleanly to K-only in a CMYK pass.
K_BLACK = CMYKColor(0, 0, 0, 1)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Single source of truth for the revision tag (bump book/.../REVISION to re-stamp).
try:
    REV = open(os.path.join(ROOT, "REVISION"), encoding="utf-8").read().strip()
except FileNotFoundError:
    REV = ""
_rev = f"-{REV}" if REV else ""
SRC = os.path.join(ROOT, "manuscript", f"full-manuscript{_rev}.md")
OUT = os.path.join(ROOT, "delivery", "production",
                   f"Saeren-Chronicles-Book-Three-6x9-interior{_rev}.pdf")

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("PlexSerif", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-It", f"{FONT_DIR}/IBMPlexSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-Bd", f"{FONT_DIR}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-BdIt", f"{FONT_DIR}/IBMPlexSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("PlexSerif", normal="PlexSerif", bold="PlexSerif-Bd",
                              italic="PlexSerif-It", boldItalic="PlexSerif-BdIt")
# Override the base-14 Helvetica slot so it embeds a TTF (passes IngramSpark preflight).
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))

TRIM_W, TRIM_H = 6 * inch, 9 * inch
M_SIDE, M_TOP, M_BOT = 0.75*inch, 0.75*inch, 0.70*inch

body = ParagraphStyle("body", fontName="PlexSerif", fontSize=11, leading=15.5,
                      alignment=TA_JUSTIFY, firstLineIndent=16,
                      textColor=K_BLACK, allowWidows=0, allowOrphans=0)
body_first = ParagraphStyle("body_first", parent=body, firstLineIndent=0)
scene = ParagraphStyle("scene", parent=body, alignment=TA_CENTER,
                       firstLineIndent=0, spaceBefore=10, spaceAfter=10)
ch_num = ParagraphStyle("ch_num", fontName="PlexSerif-Bd", fontSize=13,
                        alignment=TA_CENTER, leading=16, spaceAfter=6,
                        textColor=K_BLACK, keepWithNext=1)
ch_title = ParagraphStyle("ch_title", fontName="PlexSerif-It", fontSize=18,
                          alignment=TA_CENTER, leading=22, spaceAfter=28,
                          textColor=K_BLACK, keepWithNext=1)
title_main = ParagraphStyle("title_main", fontName="PlexSerif-Bd", fontSize=26,
                            alignment=TA_CENTER, leading=32, textColor=K_BLACK)
title_sub = ParagraphStyle("title_sub", fontName="PlexSerif-It", fontSize=15,
                           alignment=TA_CENTER, leading=20, textColor=K_BLACK)
fm_center = ParagraphStyle("fm_center", fontName="PlexSerif", fontSize=11,
                           alignment=TA_CENTER, leading=16, textColor=K_BLACK)
fm_small = ParagraphStyle("fm_small", fontName="PlexSerif", fontSize=9.5,
                          alignment=TA_CENTER, leading=14, textColor=K_BLACK)
fm_head = ParagraphStyle("fm_head", fontName="PlexSerif-Bd", fontSize=16,
                         alignment=TA_CENTER, leading=20, spaceAfter=22,
                         textColor=K_BLACK)
fm_body = ParagraphStyle("fm_body", fontName="PlexSerif", fontSize=11,
                         leading=16, alignment=TA_JUSTIFY, textColor=K_BLACK,
                         allowWidows=0, allowOrphans=0)
fm_half = ParagraphStyle("fm_half", fontName="PlexSerif-It", fontSize=16,
                         alignment=TA_CENTER, leading=20, textColor=K_BLACK)

BODY_OFFSET = [0]
PAGE_COUNT = [0]
CHAP_STARTS = []


def md_inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"_(.+?)_", r"<i>\1</i>", t)
    return t


def parse(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    chapters = []
    i = 0
    while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z-]+\s*$", lines[i].strip()):
        i += 1
    while i < len(lines):
        m = re.match(r"^CHAPTER\s+([A-Z-]+)\s*$", lines[i].strip())
        if not m:
            i += 1; continue
        num = m.group(1)
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        title = lines[i].strip() if i < len(lines) else ""
        i += 1
        buf = []
        while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z-]+\s*$", lines[i].strip()):
            buf.append(lines[i]); i += 1
        chapters.append((num, title, "\n".join(buf)))
    return chapters


def paras_from(text):
    blocks = re.split(r"\n\s*\n", text.strip())
    out = []
    for b in blocks:
        s = b.strip()
        if not s:
            continue
        if s in ("* * *", "***", "———", "* * * *"):
            out.append(("scene", "* * *"))
        else:
            out.append(("p", " ".join(line.strip() for line in s.split("\n"))))
    return out


def build(pad_to_even=False, head_map=None):
    chapters = parse(SRC)
    story = []
    CHAP_STARTS.clear()
    state = {"page": 0}

    def end_page():
        state["page"] += 1
        story.append(PageBreak())

    def blank_verso_if_needed():
        if state["page"] % 2 == 1:
            story.append(Spacer(1, 1))
            end_page()

    story.append(NextPageTemplate("front"))

    # --- p1 recto: half-title ---
    story.append(Spacer(1, 3.2*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", fm_half))
    end_page()
    blank_verso_if_needed()

    # --- recto: title page ---
    story.append(Spacer(1, 1.8*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", title_main))
    story.append(Spacer(1, 0.30*inch))
    story.append(Paragraph("Book Three: The Weight of the Source", title_sub))
    story.append(Spacer(1, 1.6*inch))
    story.append(Paragraph("Post Peleos", fm_center))
    end_page()

    # --- verso: copyright page ---
    cp = [
        "Copyright © 2026 Post Peleos",
        "",
        "All rights reserved.",
        "",
        "This is a work of fiction. Names, characters, places, and incidents "
        "are products of the author’s imagination or are used fictitiously. "
        "Any resemblance to actual persons, living or dead, events, or locales "
        "is entirely coincidental.",
        "",
        "No part of this book may be reproduced in any form or by any "
        "electronic or mechanical means, including information storage and "
        "retrieval systems, without written permission from the author, except "
        "for the use of brief quotations in a book review.",
        "",
        "ISBN [ISBN]",
        "",
        "First Edition",
        "",
        "[IMPRINT]",
    ]
    story.append(Spacer(1, 3.0*inch))
    for line in cp:
        story.append(Paragraph(line if line else "&nbsp;", fm_small))
    end_page()

    # --- recto: dedication ---
    story.append(Spacer(1, 3.6*inch))
    story.append(Paragraph("[Dedication]", ParagraphStyle(
        "ded", parent=fm_center, fontName="PlexSerif-It")))
    end_page()
    blank_verso_if_needed()

    # --- Body (numbered) ---
    BODY_OFFSET[0] = state["page"]
    story.append(NextPageTemplate("body"))
    for idx, (num, title, text) in enumerate(chapters):
        story.append(Spacer(1, 1.1*inch))
        story.append(Paragraph(f"CHAPTER {num}", ch_num))
        if title:
            story.append(Paragraph(md_inline(title), ch_title))
        first = True
        for kind, content in paras_from(text):
            if kind == "scene":
                story.append(Paragraph("* * *", scene))
                first = True
            else:
                story.append(Paragraph(md_inline(content),
                                       body_first if first else body))
                first = False
        story.append(PageBreak())

    # --- Back matter ---
    story.append(Paragraph("About the Author", fm_head))
    story.append(Paragraph(
        "Post Peleos is a writer of fantasy. <i>The Saeren Chronicles</i> is "
        "their debut series.", fm_body))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("[EXPANDED BIO OPTIONAL]", fm_small))
    story.append(PageBreak())

    story.append(Paragraph("Acknowledgments", fm_head))
    story.append(Paragraph("[Acknowledgments]", fm_body))
    story.append(PageBreak())

    # --- Series-close note (final book; no Masters-of-the-Void tease — let it sit) ---
    teaser_it = ParagraphStyle("teaser_it", parent=fm_center, fontName="PlexSerif-It")
    story.append(Spacer(1, 1.0*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", fm_head))
    story.append(Paragraph("Book One: Hazel Academy", teaser_it))
    story.append(Paragraph("Book Two: The Resistance", teaser_it))
    story.append(Paragraph("Book Three: The Weight of the Source", teaser_it))
    story.append(Spacer(1, 0.35*inch))
    story.append(Paragraph("End of the trilogy.", fm_center))

    if pad_to_even:
        story.append(PageBreak())
        story.append(Paragraph("&nbsp;", fm_small))

    def front_page(canvas, doc):
        canvas.setFont("PlexSerif", 10)

    def body_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("PlexSerif", 10)
        n = doc.page - BODY_OFFSET[0]
        if n >= 1:
            canvas.setFillColor(K_BLACK)
            canvas.drawCentredString(TRIM_W/2, 0.45*inch, str(n))
            if head_map is not None:
                title = head_map.get(doc.page)
                if title:
                    canvas.setFont("PlexSerif-It", 9)
                    canvas.drawCentredString(TRIM_W/2, TRIM_H - 0.5*inch, title)
        canvas.restoreState()

    class BookDoc(BaseDocTemplate):
        def afterFlowable(self, flowable):
            style = getattr(flowable, "style", None)
            name = getattr(style, "name", "")
            if name == "ch_title":
                CHAP_STARTS.append((self.page, flowable.getPlainText()))
            elif name == "fm_head":
                CHAP_STARTS.append((self.page, ""))

    frame = Frame(M_SIDE, M_BOT, TRIM_W - 2*M_SIDE, TRIM_H - M_TOP - M_BOT, id="text")
    doc = BookDoc(OUT, pagesize=(TRIM_W, TRIM_H),
                  title="The Saeren Chronicles - Book Three: The Weight of the Source",
                  author="Post Peleos", leftMargin=M_SIDE, rightMargin=M_SIDE,
                  topMargin=M_TOP, bottomMargin=M_BOT)
    front = PageTemplate(id="front", frames=[frame], onPage=front_page)
    bodyt = PageTemplate(id="body", frames=[frame], onPage=body_page)
    doc.addPageTemplates([front, bodyt])
    doc.build(story)
    PAGE_COUNT[0] = doc.page
    return OUT


def _head_map_from_starts():
    starts = sorted(CHAP_STARTS)
    hm = {}
    for i, (pg, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else PAGE_COUNT[0] + 1
        if title:
            for p in range(pg + 1, end):
                hm[p] = title
    return hm


if __name__ == "__main__":
    out = build()
    pad = PAGE_COUNT[0] % 2 == 1
    head_map = _head_map_from_starts()
    out = build(pad_to_even=pad, head_map=head_map)
    print("wrote", out)
    print(f"front-matter pages (unnumbered): {BODY_OFFSET[0]}")
    print(f"TOTAL PHYSICAL PAGE COUNT (even for binding): {PAGE_COUNT[0]}")
