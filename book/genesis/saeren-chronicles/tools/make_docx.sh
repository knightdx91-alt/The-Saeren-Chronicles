#!/usr/bin/env bash
# Pull the latest Book One and build the upload-ready Word (.docx).
#
# One command to run in a VNC / Cloud Shell terminal. It:
#   1. moves into the repo and pulls the latest revision from main,
#   2. makes sure python3 + python-docx are available,
#   3. reassembles the manuscript at the current REVISION,
#   4. builds the .docx that mirrors the PDF's page layout,
#   5. prints the exact path of the file to upload.
#
# Usage:
#   bash book/genesis/saeren-chronicles/tools/make_docx.sh
# or from anywhere:
#   bash /path/to/The-Saeren-Chronicles/book/genesis/saeren-chronicles/tools/make_docx.sh
set -euo pipefail

# Resolve the book directory from this script's location (works no matter where
# you invoke it from).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$(dirname "$SCRIPT_DIR")"
REPO_ROOT="$(cd "$BOOK_DIR" && git rev-parse --show-toplevel)"

echo "==> Repo:  $REPO_ROOT"
cd "$REPO_ROOT"

# 1. Get the latest revision (we work only on main in this repo).
echo "==> Pulling latest from origin/main ..."
git checkout main 2>/dev/null || true
git pull --ff-only origin main || echo "   (pull skipped — offline or detached; using local copy)"

# 2. Dependencies.
if ! python3 -c "import docx" 2>/dev/null; then
  echo "==> Installing python-docx ..."
  pip install --quiet python-docx || pip3 install --quiet python-docx
fi

REV="$(cat "$BOOK_DIR/REVISION" 2>/dev/null || echo '?')"
echo "==> Current revision: $REV"

# 3 + 4. Assemble the manuscript, then build the docx.
cd "$BOOK_DIR"
echo "==> Assembling manuscript ..."
python3 tools/assemble_manuscript.py
echo "==> Building Word document ..."
python3 tools/build_docx.py

# 5. Report the file to upload.
OUT="$BOOK_DIR/delivery/ebook/Saeren-Chronicles-Book-One-Hazel-Academy-${REV}.docx"
echo
echo "======================================================================"
echo " DONE. Upload this file:"
echo "   $OUT"
echo "======================================================================"
ls -la "$OUT"
