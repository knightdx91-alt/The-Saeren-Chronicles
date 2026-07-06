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

# --- Ensure the book pipeline is available (from book-pipeline, the source of truth) ---
# Installs the customized agents/commands/apodictic into ~/.claude, and drops a copy into
# this repo root (belt-and-suspenders, so a fresh session here works even without the
# environment setup script). Non-fatal if book-pipeline can't be reached.
REPO_ROOT="$(git -C "$HERE" rev-parse --show-toplevel 2>/dev/null || echo "")"
CFG="$HOME/.book-pipeline-src"
if [[ -d "$CFG/.git" ]]; then
  git -C "$CFG" fetch --depth 1 origin main >/dev/null 2>&1 && git -C "$CFG" reset --hard origin/main >/dev/null 2>&1 || true
else
  git clone --depth 1 https://github.com/knightdx91-alt/book-pipeline "$CFG" >/dev/null 2>&1 || true
fi
if [[ -d "$CFG/.claude" ]]; then
  mkdir -p "$HOME/.claude/agents" "$HOME/.claude/commands"
  cp -f "$CFG/.claude/agents/"*.md   "$HOME/.claude/agents/"   2>/dev/null || true
  cp -f "$CFG/.claude/commands/"*.md "$HOME/.claude/commands/" 2>/dev/null || true
  [[ -d "$CFG/tools/apodictic" ]] && { rm -rf "$HOME/.claude/apodictic"; cp -R "$CFG/tools/apodictic" "$HOME/.claude/apodictic"; }
  if [[ -n "$REPO_ROOT" && ! -d "$REPO_ROOT/.claude/agents" ]]; then
    cp -R "$CFG/.claude" "$REPO_ROOT/.claude" 2>/dev/null || true
    mkdir -p "$REPO_ROOT/tools"; cp -R "$CFG/tools/apodictic" "$REPO_ROOT/tools/apodictic" 2>/dev/null || true
    echo "Seeded pipeline into $REPO_ROOT/.claude + tools/apodictic (commit it)."
  fi
  echo "Pipeline ready: $(ls "$HOME/.claude/agents" 2>/dev/null | wc -l) agents in ~/.claude/agents."
else
  echo "note: book-pipeline not reachable — add it to this environment's repo scope for the full pipeline." >&2
fi

echo "Created $DEST"
echo "Next: stage source into $DEST/research/, edit $DEST/STATE.yaml, then run the pipeline."
