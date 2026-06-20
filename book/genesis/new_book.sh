#!/usr/bin/env bash
# Scaffold a new genesis book project from the template.
#
# Usage:
#   bash book/genesis/new_book.sh <slug> "<Book Title>"
#
# Example:
#   bash book/genesis/new_book.sh son-of-none "Son of None"
#
# Creates book/genesis/<slug>/ with the standard structure, copies the template
# (STATE.yaml, CLAUDE.md, tools/style_check.py), and fills in title + today's date.
# Then: stage source material into research/, edit STATE.yaml canon, and run the pipeline.

set -euo pipefail

SLUG="${1:-}"
TITLE="${2:-}"
if [[ -z "$SLUG" || -z "$TITLE" ]]; then
  echo "usage: bash book/genesis/new_book.sh <slug> \"<Book Title>\"" >&2
  exit 1
fi

# Resolve repo paths relative to this script.
HERE="$(cd "$(dirname "$0")" && pwd)"        # .../book/genesis
TEMPLATE="$HERE/_template"
DEST="$HERE/$SLUG"
TODAY="$(date +%Y-%m-%d)"

if [[ -e "$DEST" ]]; then
  echo "error: $DEST already exists" >&2
  exit 1
fi

mkdir -p "$DEST"/{research,manuscript/chapters,evaluations/continuity,feedback,delivery/editorial,delivery/production,voice-bank/samples,tools}
cp "$TEMPLATE/STATE.yaml"          "$DEST/STATE.yaml"
cp "$TEMPLATE/CLAUDE.md"           "$DEST/CLAUDE.md"
cp "$TEMPLATE/tools/style_check.py" "$DEST/tools/style_check.py"

# Fill in title + date placeholders.
sed -i "s|<BOOK TITLE>|$TITLE|g; s|<YYYY-MM-DD>|$TODAY|g" "$DEST/STATE.yaml" "$DEST/CLAUDE.md"

cat > "$DEST/feedback/progress.md" <<EOF
# Progress — $TITLE

Scaffolded $TODAY from book/genesis/_template.

## Next steps
1. Pull source material from Google Drive into research/ (original draft + any roadmap/bible).
2. Fill in STATE.yaml: premise, genre, comps, canon_sources, guardrails, open_author_decisions.
3. Edit tools/style_check.py ALLOWLIST with this book's deliberate motifs.
4. Architect pass: build foundation.md + outline.md (if no scene-by-scene roadmap exists).
5. Run the chapter loop in order; commit per chapter; keep this file current.

## Resume point
Nothing drafted yet.
EOF

echo "Created $DEST"
echo "Next: stage source into $DEST/research/, edit $DEST/STATE.yaml, then run the pipeline."
