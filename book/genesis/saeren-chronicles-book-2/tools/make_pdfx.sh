#!/usr/bin/env bash
# Convert the RGB interior PDF to PDF/X-1a:2001 (CMYK + OutputIntent) for IngramSpark.
# Requires Ghostscript (gs). Run AFTER tools/build_pdf.py.
#
#   bash tools/make_pdfx.sh
#
# Output: delivery/production/Saeren-Chronicles-Book-Two-6x9-interior-<REV>-PDFX1a.pdf
# Text in the interior is pure K-only black (set in build_pdf.py), so the CMYK
# conversion yields clean black text with no rich-black/rosetting on press.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
REV="$(cat "$ROOT/REVISION" 2>/dev/null || echo "")"
SUF=""; [ -n "$REV" ] && SUF="-$REV"

IN="$ROOT/delivery/production/Saeren-Chronicles-Book-Two-6x9-interior${SUF}.pdf"
OUT="$ROOT/delivery/production/Saeren-Chronicles-Book-Two-6x9-interior${SUF}-PDFX1a.pdf"
DEF="$HERE/PDFX_def.ps"

[ -f "$IN" ] || { echo "ERROR: interior PDF not found: $IN (run tools/build_pdf.py first)"; exit 1; }
command -v gs >/dev/null || { echo "ERROR: ghostscript (gs) not installed"; exit 1; }

# NOTE: -dNOSAFER is required so the PDF/X def file can read the ICC profile via
# the PostScript `file` operator (default -dSAFER blocks absolute file paths).
# Inputs here are local, trusted build artifacts, so this is safe.
gs -dPDFX -dBATCH -dNOPAUSE -dNOOUTERSAVE -dNOSAFER \
   -sDEVICE=pdfwrite \
   -dPDFSETTINGS=/prepress \
   -dCompatibilityLevel=1.3 \
   -sColorConversionStrategy=CMYK \
   -sProcessColorModel=DeviceCMYK \
   -dEmbedAllFonts=true -dSubsetFonts=true \
   -dAutoRotatePages=/None \
   -sOutputFile="$OUT" \
   "$DEF" "$IN"

echo "wrote $OUT"
