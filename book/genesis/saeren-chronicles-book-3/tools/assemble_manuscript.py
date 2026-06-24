#!/usr/bin/env python3
"""Reassemble manuscript/full-manuscript.md from manuscript/chapters/chapter-*.md.

Book Three: The Weight of the Source (20 chapters).
- Title page (THE SAEREN CHRONICLES / Book Three: The Weight of the Source).
- Each chapter rendered as:  CHAPTER <WORD>\n\n<Title>\n\n<prose>
- Scene breaks (— runs / *** variants) normalized to "* * *".
- Strips markdown headers (#), HTML comments, and any end markers.

The revision tag is read from book/.../REVISION (single source of truth) and
stamped into the output filename so each build keeps the prior one as history.
"""
import glob, os, re

NUMWORDS = {1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",
            8:"EIGHT",9:"NINE",10:"TEN",11:"ELEVEN",12:"TWELVE",13:"THIRTEEN",
            14:"FOURTEEN",15:"FIFTEEN",16:"SIXTEEN",17:"SEVENTEEN",18:"EIGHTEEN",
            19:"NINETEEN",20:"TWENTY",21:"TWENTY-ONE",22:"TWENTY-TWO",
            23:"TWENTY-THREE",24:"TWENTY-FOUR",25:"TWENTY-FIVE",26:"TWENTY-SIX"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Single source of truth for the revision tag (bump book/.../REVISION to re-stamp).
try:
    REV = open(os.path.join(ROOT, "REVISION"), encoding="utf-8").read().strip()
except FileNotFoundError:
    REV = ""
_rev = f"-{REV}" if REV else ""
CH_DIR = os.path.join(ROOT, "manuscript", "chapters")
OUT = os.path.join(ROOT, "manuscript", f"full-manuscript{_rev}.md")

def is_scene_break(line):
    s = line.strip()
    if not s:
        return False
    # runs of em/en dashes or hyphens, or asterisk variants
    if re.fullmatch(r"[—–-]{3,}", s):
        return True
    if re.fullmatch(r"\*(\s*\*){1,3}", s):
        return True
    return False

def parse_chapter(path, num):
    raw = open(path, encoding="utf-8").read()
    lines = raw.splitlines()
    title = None
    body_start = 0

    # markdown header form: "# Chapter N: Title"
    for idx, ln in enumerate(lines):
        m = re.match(r"^#\s*Chapter\s+\d+\s*:\s*(.+?)\s*$", ln)
        if m:
            title = m.group(1).strip()
            body_start = idx + 1
            break

    body = lines[body_start:]
    # drop HTML comments and end markers
    cleaned = []
    for ln in body:
        if re.match(r"^\s*<!--", ln):
            continue
        if re.match(r"^\s*\[END OF CHAPTER", ln):
            continue
        cleaned.append(ln)
    # collapse to text, normalizing scene breaks
    out = []
    for ln in cleaned:
        if is_scene_break(ln):
            out.append("* * *")
        else:
            out.append(ln.rstrip())
    text = "\n".join(out).strip("\n")
    # collapse 3+ blank lines to 1 blank
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text

def main():
    files = sorted(glob.glob(os.path.join(CH_DIR, "chapter-*.md")),
                   key=lambda p: int(re.search(r"chapter-(\d+)", p).group(1)))
    parts = ["THE SAEREN CHRONICLES", "", "Book Three: The Weight of the Source", "", ""]
    for f in files:
        num = int(re.search(r"chapter-(\d+)", f).group(1))
        title, text = parse_chapter(f, num)
        parts.append(f"CHAPTER {NUMWORDS[num]}")
        parts.append("")
        if title:
            parts.append(title)
            parts.append("")
        parts.append(text)
        parts.append("")
        parts.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(parts).rstrip() + "\n")
    print("wrote", OUT)

if __name__ == "__main__":
    main()
