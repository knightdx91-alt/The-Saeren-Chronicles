#!/usr/bin/env python3
"""Generate a reflowable EPUB3 (with EPUB2 NCX fallback) from an assembled
full-manuscript markdown. Cover + title + copyright + dedication + chapters +
back matter, with a navigable TOC. Pure stdlib (zipfile)."""
import os, re, zipfile, html, uuid, sys

FONTWORDS = {"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,
    "EIGHT":8,"NINE":9,"TEN":10,"ELEVEN":11,"TWELVE":12,"THIRTEEN":13,
    "FOURTEEN":14,"FIFTEEN":15,"SIXTEEN":16,"SEVENTEEN":17,"EIGHTEEN":18,
    "NINETEEN":19,"TWENTY":20}
WORDTITLE = {v:k.title() for k,v in FONTWORDS.items()}

def parse(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    chapters=[]; i=0
    while i < len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
        i+=1
    while i < len(lines):
        m=re.match(r"^CHAPTER\s+([A-Z]+)\s*$", lines[i].strip())
        if not m: i+=1; continue
        word=m.group(1); i+=1
        while i<len(lines) and not lines[i].strip(): i+=1
        title=lines[i].strip() if i<len(lines) else ""; i+=1
        buf=[]
        while i<len(lines) and not re.match(r"^CHAPTER\s+[A-Z]+\s*$", lines[i].strip()):
            buf.append(lines[i]); i+=1
        chapters.append((FONTWORDS.get(word,0), title, "\n".join(buf)))
    return chapters

def inline(s):
    s=html.escape(s, quote=False)
    s=re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s=re.sub(r"_(.+?)_", r"<em>\1</em>", s)
    return s

def paras(text):
    out=[]
    for b in re.split(r"\n\s*\n", text.strip()):
        s=b.strip()
        if not s: continue
        if s in ("* * *","***","———","* * * *","* * *  *"):
            out.append(("scene",None))
        else:
            out.append(("p"," ".join(l.strip() for l in s.split("\n"))))
    return out

CSS = """body{font-family:Georgia,'Times New Roman',serif;line-height:1.5;margin:5%;}
h1,h2,h3{font-weight:normal;text-align:center;}
h2.chnum{margin-top:3em;letter-spacing:.15em;text-transform:uppercase;font-size:1em;}
h3.chtitle{font-style:italic;margin:.3em 0 2em;font-size:1.3em;}
p{margin:0;text-indent:1.3em;text-align:justify;}
p.first{text-indent:0;}
p.scene{text-align:center;text-indent:0;margin:1.4em 0;letter-spacing:.4em;}
.center{text-align:center;}.title-main{font-size:1.6em;letter-spacing:.1em;margin-top:25%;}
.subtitle{font-style:italic;font-size:1.2em;margin-top:.6em;}
.author{margin-top:3em;letter-spacing:.2em;}
.cp{font-size:.85em;text-align:center;line-height:1.8;margin-top:30%;}
.ded{font-style:italic;text-align:center;margin-top:40%;}
img.cover{max-width:100%;height:auto;display:block;margin:0 auto;}"""

def xhtml(title, body):
    return ('<?xml version="1.0" encoding="utf-8"?>\n'
        '<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n<head>\n'
        f'<title>{html.escape(title)}</title>\n'
        '<meta charset="utf-8"/>\n<link rel="stylesheet" type="text/css" href="style.css"/>\n'
        f'</head>\n<body>\n{body}\n</body>\n</html>\n')

def build_epub(cfg):
    chapters=parse(cfg["manuscript"])
    assert chapters, "no chapters parsed"
    uid="urn:uuid:"+str(uuid.uuid4())
    items=[]  # (id, href, content_str_or_path, media_type, in_spine, nav_label)

    # cover image
    cover_ext = os.path.splitext(cfg["cover"])[1].lower().lstrip(".")
    cover_mt = "image/jpeg" if cover_ext in ("jpg","jpeg") else "image/png"
    items.append(("coverimg","cover."+cover_ext, ("FILE",cfg["cover"]), cover_mt, False, None))
    # cover page
    cover_body=f'<div class="center"><img class="cover" src="cover.{cover_ext}" alt="Cover"/></div>'
    items.append(("coverpage","cover.xhtml", xhtml("Cover",cover_body), "application/xhtml+xml", True, None))
    # title page
    tp=(f'<div class="center"><div class="title-main">THE SAEREN CHRONICLES</div>'
        f'<div class="subtitle">{html.escape(cfg["subtitle"])}</div>'
        f'<div class="author">POST PELEOS</div></div>')
    items.append(("titlepage","title.xhtml", xhtml("Title Page",tp), "application/xhtml+xml", True, "Title Page"))
    # copyright
    cp_lines=[f"Copyright &#169; 2026 Post Peleos","All rights reserved.",
        "This is a work of fiction. Names, characters, places, and incidents are "
        "products of the author&#8217;s imagination or are used fictitiously.",
        "No part of this book may be reproduced without written permission from "
        "the author, except for brief quotations in a book review.",
        "Ebook Edition","Post Peleos"]
    cp='<div class="cp">'+"<br/><br/>".join(cp_lines)+"</div>"
    items.append(("copyright","copyright.xhtml", xhtml("Copyright",cp), "application/xhtml+xml", True, None))
    # dedication
    items.append(("dedication","dedication.xhtml",
        xhtml("Dedication", f'<div class="ded">{cfg["dedication"]}</div>'),
        "application/xhtml+xml", True, "Dedication"))
    # chapters
    for n,title,text in chapters:
        body=[f'<h2 class="chnum">Chapter {WORDTITLE.get(n,n)}</h2>']
        if title: body.append(f'<h3 class="chtitle">{inline(title)}</h3>')
        for kind,content in paras(text):
            if kind=="scene": body.append('<p class="scene">* * *</p>')
            else:
                cls=' class="first"' if (body and body[-1].startswith("<h")) else ""
                body.append(f"<p{cls}>{inline(content)}</p>")
        lbl=f"Chapter {WORDTITLE.get(n,n)}"+(f" — {title}" if title else "")
        items.append((f"ch{n}", f"chapter-{n}.xhtml", xhtml(lbl,"\n".join(body)),
                      "application/xhtml+xml", True, lbl))
    # back matter
    bm=(f'<h2 class="chnum">About the Author</h2><p class="first">{cfg["bio"]}</p>'
        f'<h2 class="chnum">Acknowledgments</h2><p class="first">{cfg["ack"]}</p>')
    items.append(("backmatter","backmatter.xhtml", xhtml("About the Author",bm),
                  "application/xhtml+xml", True, "About the Author"))

    # nav.xhtml
    navlis="".join(f'<li><a href="{h}">{html.escape(lbl)}</a></li>\n'
        for (_id,h,_c,_m,spine,lbl) in items if lbl)
    nav=('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n'
        '<head><title>Contents</title><meta charset="utf-8"/></head>\n<body>\n'
        '<nav epub:type="toc" id="toc"><h1>Contents</h1>\n<ol>\n'+navlis+'</ol></nav>\n</body></html>\n')

    # toc.ncx (epub2 fallback)
    points=""; pn=1
    for (_id,h,_c,_m,spine,lbl) in items:
        if lbl:
            points+=(f'<navPoint id="np{pn}" playOrder="{pn}"><navLabel><text>'
                f'{html.escape(lbl)}</text></navLabel><content src="{h}"/></navPoint>\n'); pn+=1
    ncx=('<?xml version="1.0" encoding="utf-8"?>\n'
        '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">\n'
        f'<head><meta name="dtb:uid" content="{uid}"/></head>\n'
        f'<docTitle><text>{html.escape(cfg["full_title"])}</text></docTitle>\n'
        f'<navMap>\n{points}</navMap>\n</ncx>\n')

    # content.opf
    manifest=['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="style.css" media-type="text/css"/>']
    spine=[]
    for (_id,h,_c,mt,insp,lbl) in items:
        props=' properties="cover-image"' if _id=="coverimg" else ""
        manifest.append(f'<item id="{_id}" href="{h}" media-type="{mt}"{props}/>')
        if insp: spine.append(f'<itemref idref="{_id}"/>')
    opf=('<?xml version="1.0" encoding="utf-8"?>\n'
        '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">\n'
        '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        f'<dc:identifier id="bookid">{uid}</dc:identifier>\n'
        f'<dc:title>{html.escape(cfg["full_title"])}</dc:title>\n'
        '<dc:language>en</dc:language>\n<dc:creator>Post Peleos</dc:creator>\n'
        '<dc:publisher>Post Peleos</dc:publisher>\n'
        f'<dc:description>{html.escape(cfg["desc"])}</dc:description>\n'
        '<meta property="dcterms:modified">2026-06-24T00:00:00Z</meta>\n'
        '<meta name="cover" content="coverimg"/>\n</metadata>\n'
        '<manifest>\n'+"\n".join(manifest)+'\n</manifest>\n'
        '<spine toc="ncx">\n'+"\n".join(spine)+'\n</spine>\n</package>\n')

    # write zip
    out=cfg["out"]
    with zipfile.ZipFile(out,"w") as z:
        z.writestr("mimetype","application/epub+zip",compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
            '<?xml version="1.0"?>\n<container version="1.0" '
            'xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n'
            '<rootfiles><rootfile full-path="OEBPS/content.opf" '
            'media-type="application/oebps-package+xml"/></rootfiles></container>\n',
            compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf",opf,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/nav.xhtml",nav,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx",ncx,compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css",CSS,compress_type=zipfile.ZIP_DEFLATED)
        for (_id,h,content,mt,insp,lbl) in items:
            if isinstance(content,tuple) and content[0]=="FILE":
                z.write(content[1], "OEBPS/"+h, compress_type=zipfile.ZIP_DEFLATED)
            else:
                z.writestr("OEBPS/"+h, content, compress_type=zipfile.ZIP_DEFLATED)
    return out, len(chapters)

BIO=("Post Peleos writes character-driven fantasy about quiet people in loud "
     "worlds &#8212; stories that love to tease as much as they wound, and never "
     "quite stop wondering what waits out beyond the stars. <em>The Saeren "
     "Chronicles</em> is their debut series.")

ROOT="/home/user/The-Saeren-Chronicles/book/genesis"
configs=[
 {"manuscript":f"{ROOT}/saeren-chronicles/manuscript/full-manuscript-r14.md",
  "cover":"/tmp/claude-0/-home-user-The-Saeren-Chronicles/bce4b0a8-8b7e-52a1-818e-dbb13b0d329e/scratchpad/ebook-cover-book1-hazel-academy.jpg",
  "subtitle":"Book One: Hazel Academy","full_title":"The Saeren Chronicles — Book One: Hazel Academy",
  "dedication":"For my daughter Raelynn &#8212;<br/>may she have all the happiness she deserves.",
  "ack":"To my parents, for always believing in me.","bio":BIO,
  "desc":"A quiet, lyrical YA fantasy about grief, found family, and a girl who refuses to be made small.",
  "out":f"{ROOT}/saeren-chronicles/delivery/ebook/Saeren-Chronicles-Book-One-Hazel-Academy.epub"},
 {"manuscript":f"{ROOT}/saeren-chronicles-book-2/manuscript/full-manuscript-r7.md",
  "cover":"/tmp/claude-0/-home-user-The-Saeren-Chronicles/bce4b0a8-8b7e-52a1-818e-dbb13b0d329e/scratchpad/ebook-cover-book2-the-resistance.jpg",
  "subtitle":"Book Two: The Resistance","full_title":"The Saeren Chronicles — Book Two: The Resistance",
  "dedication":"For MNB &#8212;<br/>may your life be long and happy.",
  "ack":"Thanks to everyone who has read my books and encouraged me to keep writing.","bio":BIO,
  "desc":"The second book of The Saeren Chronicles: a devastating fantasy about grief, found family, consent, and the weight of being the only one who can.",
  "out":f"{ROOT}/saeren-chronicles-book-2/delivery/ebook/Saeren-Chronicles-Book-Two-The-Resistance.epub"},
]
for c in configs:
    os.makedirs(os.path.dirname(c["out"]), exist_ok=True)
    out,n=build_epub(c)
    print(f"wrote {out}  ({n} chapters, {os.path.getsize(out)//1024} KB)")
