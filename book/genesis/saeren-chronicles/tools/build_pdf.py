#!/usr/bin/env python3
"""
Build a print-ready interior PDF of Book One to IngramSpark interior specs.

Trim: 6" x 9" (standard YA/fantasy trade paperback).
Margins (mirrored): inside/gutter 0.875", outside 0.625", top 0.75", bottom 0.70".
  - IngramSpark minimum margin from trim is 0.5"; gutter here exceeds the
    recommended minimum for books up to ~500 pp.
Fonts: IBM Plex Serif (Regular/Italic/Bold/BoldItalic), fully embedded.
Body: 11pt / 15.5pt leading, justified, 16pt first-line indent (no indent on
  the first paragraph of a chapter or after a scene break).
Output: delivery/production/Saeren-Chronicles-Book-One-6x9-interior.pdf

NOTE: This produces an embedded-font, exact-trim, correctly-margined RGB PDF.
IngramSpark's *preferred* format is PDF/X-1a:2001 (CMYK + output intent); that
final conversion needs Acrobat/Ghostscript and is not available in this
environment. For pure-black text this PDF will print correctly; see the
production note for the X-1a/CMYK caveat.
"""
import os, re, html
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, PageBreak, NextPageTemplate,
                                CondPageBreak)

# Pure K-only black for text: converts cleanly to K-only in a CMYK pass
# (0% C, 0% M, 0% Y, 100% K) — no rich-black, no rosettes on press.
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
                   f"Saeren-Chronicles-Book-One-6x9-interior{_rev}.pdf")

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont("PlexSerif", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-It", f"{FONT_DIR}/IBMPlexSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-Bd", f"{FONT_DIR}/IBMPlexSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PlexSerif-BdIt", f"{FONT_DIR}/IBMPlexSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("PlexSerif", normal="PlexSerif", bold="PlexSerif-Bd",
                              italic="PlexSerif-It", boldItalic="PlexSerif-BdIt")
# reportlab declares a default /Helvetica in the shared font resources even when
# unused; that base-14 font is NOT embedded and fails IngramSpark preflight.
# Override the name so the slot embeds a TTF instead of base-14 Helvetica.
pdfmetrics.registerFont(TTFont("Helvetica", f"{FONT_DIR}/IBMPlexSerif-Regular.ttf"))

# Geometry — symmetric, gutter-safe margins (IngramSpark-compliant for <=~500pp).
# Both side margins 0.75" exceed the 0.5" minimum and meet gutter needs without
# fragile per-page mirroring. Top 0.75", bottom 0.70" (footer page number).
TRIM_W, TRIM_H = 6 * inch, 9 * inch
M_SIDE, M_TOP, M_BOT = 0.75*inch, 0.75*inch, 0.70*inch

# allowWidows=0 / allowOrphans=0 ask reportlab to never leave a single line
# of a paragraph stranded at the bottom (orphan) or top (widow) of a page.
body = ParagraphStyle("body", fontName="PlexSerif", fontSize=11, leading=15.5,
                      alignment=TA_JUSTIFY, firstLineIndent=16,
                      textColor=K_BLACK, allowWidows=0, allowOrphans=0)
body_first = ParagraphStyle("body_first", parent=body, firstLineIndent=0)
scene = ParagraphStyle("scene", parent=body, alignment=TA_CENTER,
                       firstLineIndent=0, spaceBefore=10, spaceAfter=10)
# keepWithNext on the chapter number/title binds the heading to the first
# body line so a heading can never strand alone at the foot of a page.
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
# Front/back-matter styles (centered, K-only black).
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


# Mutable holders so build() can report the front-matter offset / total pages.
BODY_OFFSET = [0]
PAGE_COUNT = [0]
# Records (physical_page, running-head text) for each chapter title and back-matter
# heading, captured during a build pass so the final pass can draw running heads.
CHAP_STARTS = []


def md_inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"_(.+?)_", r"<i>\1</i>", t)
    return t


WORDS = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,
         "NINE":9,"TEN":10,"ELEVEN":11,"TWELVE":12,"THIRTEEN":13,"FOURTEEN":14,
         "FIFTEEN":15,"SIXTEEN":16,"SEVENTEEN":17,"EIGHTEEN":18,"NINETEEN":19,"TWENTY":20}


def parse(path):
    raw = open(path, encoding="utf-8").read()
    lines = raw.split("\n")
    # drop the leading title block (first 3 nonblank lines before CHAPTER ONE)
    chapters = []
    i = 0
    # find first chapter
    while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
        i += 1
    while i < len(lines):
        m = re.match(r"^CHAPTER\s+([A-Z]+)\s*$", lines[i].strip())
        if not m:
            i += 1; continue
        num = m.group(1)
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        title = lines[i].strip() if i < len(lines) else ""
        i += 1
        # gather body until next CHAPTER
        buf = []
        while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
            buf.append(lines[i]); i += 1
        chapters.append((num, title, "\n".join(buf)))
    return chapters


def paras_from(text):
    # split on blank lines into paragraphs; mark scene breaks
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

    # Track the running page index so we can drop blank versos to force the
    # next major element onto a recto (odd page). The whole front matter runs
    # on the "front" template (unnumbered).
    state = {"page": 0}  # number of pages already emitted

    def end_page():
        state["page"] += 1
        story.append(PageBreak())

    def blank_verso_if_needed():
        # After emitting a page, if the count is even (i.e. the next page would
        # be a verso/even page), emit a blank to push the next element to recto.
        if state["page"] % 2 == 1:  # last page was a recto -> next is verso
            story.append(Spacer(1, 1))
            end_page()

    story.append(NextPageTemplate("front"))

    # --- p1 recto: half-title ---
    story.append(Spacer(1, 3.2*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", fm_half))
    end_page()
    blank_verso_if_needed()  # blank verso so the title page lands on a recto

    # --- recto: title page ---
    story.append(Spacer(1, 1.8*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", title_main))
    story.append(Spacer(1, 0.30*inch))
    story.append(Paragraph("Book One: Hazel Academy", title_sub))
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
        "ISBN 979-8-2409-9043-4",
        "",
        "First Edition",
        "",
        "Post Peleos",
    ]
    story.append(Spacer(1, 3.0*inch))
    for line in cp:
        story.append(Paragraph(line if line else "&nbsp;", fm_small))
    end_page()

    # --- recto: dedication ---
    story.append(Spacer(1, 3.6*inch))
    story.append(Paragraph(
        "For my daughter Raelynn —<br/>may she have all the happiness she deserves.",
        ParagraphStyle("ded", parent=fm_center, fontName="PlexSerif-It")))
    end_page()
    blank_verso_if_needed()  # blank verso so Chapter One starts on a recto

    # --- Body (numbered) ---
    # Page numbering offset: body page "1" is the next physical page. The footer
    # callback subtracts this offset from doc.page.
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
        story.append(PageBreak())  # every chapter ends its page; back matter follows

    # --- Back matter (still numbered; runs on the body template) ---
    story.append(Paragraph("About the Author", fm_head))
    story.append(Paragraph(
        "Post Peleos writes character-driven fantasy about quiet people in loud "
        "worlds — stories that love to tease as much as they wound, and never "
        "quite stop wondering what waits out beyond the stars. <i>The Saeren "
        "Chronicles</i> is their debut series.", fm_body))
    story.append(PageBreak())

    story.append(Paragraph("Acknowledgments", fm_head))
    story.append(Paragraph(
        "To my parents, for always believing in me.", fm_body))
    story.append(PageBreak())

    # --- Book Two teaser (real excerpt + series note) ---
    teaser_it = ParagraphStyle("teaser_it", parent=fm_center, fontName="PlexSerif-It")
    story.append(Paragraph("The story continues in", fm_center))
    story.append(Spacer(1, 0.10*inch))
    story.append(Paragraph("THE SAEREN CHRONICLES", fm_head))
    story.append(Paragraph("Book Two: The Resistance", teaser_it))
    story.append(Spacer(1, 0.35*inch))
    b2 = [
        "On the fourth morning the camp put her to work, which was the kindest "
        "thing it could have done.",
        "It was Brutus who did it, the broad sunburned man from the council, who "
        "found her standing at the edge of the lanes with nothing in her hands and "
        "the look on her face of a person who has run out of things to be useful "
        "for. He did not ask her how she was, which she was grateful for, because "
        "she had heard the question a dozen times since the burning school and had "
        "not yet found a true answer that did not cost more than it was worth to "
        "give. He simply looked her up and down, the way he looked at a length of "
        "timber, and grunted, and said, “You. You’ve got two arms. Come hold this.”",
        "And running under all of it, under the washing and the games and the "
        "smell of bread, a thing she could feel the way you feel a clock in a quiet "
        "house: the count. <i>A week,</i> Jazen had said. <i>By this time next week "
        "I mean to be on the road to the capital.</i> Four days of it were already "
        "gone.",
    ]
    first_b2 = True
    for para in b2:
        story.append(Paragraph(para, body_first if first_b2 else body))
        first_b2 = False
    story.append(Spacer(1, 0.30*inch))
    story.append(Paragraph(
        "Viridia’s war is only beginning. <i>The Resistance</i> follows her from "
        "the hidden camp to the gates of the capital — and to the choice the whole "
        "of the first book has been quietly preparing her to make.", teaser_it))

    # IngramSpark requires an EVEN physical page count for perfect binding.
    # A first pass measures the count; if odd, we re-run with one trailing blank.
    if pad_to_even:
        story.append(PageBreak())
        story.append(Paragraph("&nbsp;", fm_small))

    def front_page(canvas, doc):
        canvas.setFont("PlexSerif", 10)  # avoid Helvetica default resource

    def body_page(canvas, doc):
        canvas.saveState()
        canvas.setFont("PlexSerif", 10)
        # Body page numbering starts at 1 on Chapter One. doc.page is the
        # physical page index (1-based); subtract the front-matter page count.
        n = doc.page - BODY_OFFSET[0]
        if n >= 1:
            canvas.setFillColor(K_BLACK)
            canvas.drawCentredString(TRIM_W/2, 0.45*inch, str(n))
            # Running head: chapter title, centered in the top margin. Suppressed
            # on a chapter's opening page and on back matter (head_map omits those).
            if head_map is not None:
                title = head_map.get(doc.page)
                if title:
                    canvas.setFont("PlexSerif-It", 9)
                    canvas.drawCentredString(TRIM_W/2, TRIM_H - 0.5*inch, title)
        canvas.restoreState()

    # Capture each chapter title (and back-matter heading) with the page it lands
    # on, so a measurement pass can build the page->running-head map.
    class BookDoc(BaseDocTemplate):
        def afterFlowable(self, flowable):
            style = getattr(flowable, "style", None)
            name = getattr(style, "name", "")
            if name == "ch_title":
                CHAP_STARTS.append((self.page, flowable.getPlainText()))
            elif name == "fm_head":
                CHAP_STARTS.append((self.page, ""))  # back matter: no running head

    frame = Frame(M_SIDE, M_BOT, TRIM_W - 2*M_SIDE, TRIM_H - M_TOP - M_BOT, id="text")
    doc = BookDoc(OUT, pagesize=(TRIM_W, TRIM_H),
                          title="The Saeren Chronicles - Book One: Hazel Academy",
                          author="Post Peleos", leftMargin=M_SIDE, rightMargin=M_SIDE,
                          topMargin=M_TOP, bottomMargin=M_BOT)
    front = PageTemplate(id="front", frames=[frame], onPage=front_page)
    bodyt = PageTemplate(id="body", frames=[frame], onPage=body_page)
    doc.addPageTemplates([front, bodyt])
    doc.build(story)
    # Total physical page count = the canvas page counter after build.
    PAGE_COUNT[0] = doc.page
    return OUT


def _head_map_from_starts():
    # A chapter's title appears on every body page AFTER its opening page, up to
    # the next chapter (or back-matter heading, recorded with an empty title).
    starts = sorted(CHAP_STARTS)
    hm = {}
    for i, (pg, title) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else PAGE_COUNT[0] + 1
        if title:
            for p in range(pg + 1, end):  # skip the opener page itself
                hm[p] = title
    return hm


if __name__ == "__main__":
    # Pass 1 (measurement): learn each chapter's opening page + total pages.
    out = build()
    pad = PAGE_COUNT[0] % 2 == 1  # odd -> add one trailing blank for even binding
    head_map = _head_map_from_starts()
    # Pass 2 (final): draw the chapter-title running heads (and pad if needed).
    out = build(pad_to_even=pad, head_map=head_map)
    print("wrote", out)
    print(f"front-matter pages (unnumbered): {BODY_OFFSET[0]}")
    print(f"TOTAL PHYSICAL PAGE COUNT (even for binding): {PAGE_COUNT[0]}")
