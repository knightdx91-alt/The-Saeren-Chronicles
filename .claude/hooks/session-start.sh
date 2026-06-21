#!/bin/bash
# SessionStart hook: install the Best Seller Studio agents into ~/.claude/agents/.
#
# The book pipeline (book-orchestrator, book-writer, etc.) lives outside this repo
# and must be (re)installed into every fresh/ephemeral container before the agents
# are dispatchable. This script clones Best Seller Studio and populates the agent
# directory, including the 4 skill-based roles that need agent frontmatter added.
#
# Idempotent and non-interactive. Safe to run on every session start.
set -euo pipefail

# Only run in the remote (Claude Code on the web) environment.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

BSS_REPO="https://github.com/felipelobomotta-blip/best-seller-studio"
BSS_DIR="/tmp/bss"
AGENTS_DIR="$HOME/.claude/agents"

mkdir -p "$AGENTS_DIR"

# Clone (or refresh) Best Seller Studio.
if [ -d "$BSS_DIR/.git" ]; then
  git -C "$BSS_DIR" pull --quiet --ff-only || true
else
  rm -rf "$BSS_DIR"
  git clone --depth 1 --quiet "$BSS_REPO" "$BSS_DIR"
fi

# 1) Copy the 8 core book-* agents as-is.
cp "$BSS_DIR"/agents/*.md "$AGENTS_DIR"/

# 2) Build the 4 skill-based roles as agents (add tools/model/maxTurns frontmatter,
#    strip the original SKILL.md YAML frontmatter, keep its description + body).
make_agent () {
  local name="$1" src="$2" desc="$3"
  [ -f "$src" ] || { echo "warn: missing $src, skipping $name" >&2; return 0; }
  {
    printf -- '---\n'
    printf 'name: %s\n' "$name"
    printf 'description: %s\n' "$desc"
    printf 'tools: Read, Write, Edit, Grep, Glob, Bash\n'
    printf 'model: opus\n'
    printf 'maxTurns: 40\n'
    printf -- '---\n\n'
    awk 'NR==1&&$0=="---"{f=1;next} f&&$0=="---"{f=0;next} !f{print}' "$src"
  } > "$AGENTS_DIR/$name.md"
}

make_agent entity-tracker "$BSS_DIR/skills/optional/entity-tracker/SKILL.md" \
  "Builds and maintains ENTITY_STATE.yaml — the persistent structured database of every character, location, object, organization, timeline entry, and world rule in the manuscript. Operates in BUILD mode (initial extraction) and UPDATE mode (incremental tracking). The single source of truth other roles consume instead of rebuilding entity databases."
make_agent continuity-guardian "$BSS_DIR/skills/optional/continuity-guardian/SKILL.md" \
  "Cross-manuscript consistency auditor. Runs after every 3-5 chapter batch and after full completion. Catches continuity errors, information-flow violations, timeline contradictions, and orphaned plot threads that individual chapter writers miss."
make_agent dialogue-polish "$BSS_DIR/skills/deprecated/dialogue-polish/SKILL.md" \
  "Dedicated dialogue editing pass — ensures distinct character voices, subtext, natural rhythm, and correct dialogue-to-prose ratio. Runs AFTER the writer and BEFORE hook-craft/disruptor."
make_agent hook-craft "$BSS_DIR/skills/deprecated/hook-craft/SKILL.md" \
  "Specializes in chapter openings (hooks) and endings (pulls). Every chapter must start with a reason to keep reading and end with a reason to turn the page. The role that prevents the reader from putting the book down."

echo "Installed book pipeline agents into $AGENTS_DIR:"
ls "$AGENTS_DIR"
