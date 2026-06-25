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

# 0) Manuscript-build toolchain. The PDF pipeline needs these in every fresh,
#    ephemeral container or `tools/build_pdf.py` / `tools/make_pdfx.sh` fail:
#      - reportlab + pillow (Python): build the RGB interior PDF.
#      - ghostscript (gs): PDF/X-1a:2001 CMYK conversion (make_pdfx.sh).
#    Idempotent and non-fatal — only installs what is missing.
if ! python3 -c 'import reportlab' >/dev/null 2>&1; then
  echo "Installing Python build deps (reportlab, pillow)..."
  pip install --quiet reportlab pillow >/dev/null 2>&1 \
    && echo "reportlab/pillow installed." \
    || echo "warn: pip install reportlab/pillow failed; build_pdf.py may not run." >&2
fi
if ! command -v gs >/dev/null 2>&1; then
  echo "Installing ghostscript (for PDF/X-1a CMYK conversion)..."
  { apt-get install -y ghostscript >/dev/null 2>&1 || sudo apt-get install -y ghostscript >/dev/null 2>&1; } \
    && echo "ghostscript installed ($(gs --version 2>/dev/null))." \
    || echo "warn: ghostscript install failed; make_pdfx.sh (PDF/X-1a) will be unavailable." >&2
fi

# Clone (or refresh) Best Seller Studio. Retry the clone a few times so a flaky
# network on container start does not leave the agents uninstalled.
if [ -d "$BSS_DIR/.git" ]; then
  git -C "$BSS_DIR" pull --quiet --ff-only || true
else
  for attempt in 1 2 3; do
    rm -rf "$BSS_DIR"
    git clone --depth 1 --quiet "$BSS_REPO" "$BSS_DIR" && break
    echo "warn: BSS clone attempt $attempt failed; retrying..." >&2
    sleep $((attempt * 2))
  done
fi
if [ ! -d "$BSS_DIR/.git" ]; then
  echo "ERROR: could not clone Best Seller Studio ($BSS_REPO); book-* agents may be missing." >&2
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
    printf 'maxTurns: 120\n'
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

# 3) Normalize maxTurns across ALL installed agents. The upstream book-* agents
#    ship with maxTurns: 40, which truncates a full chapter write-plus-gate-loop
#    (read/edit/style_check/rhythm_check per iteration easily exceeds 40 turns) —
#    the agent then stops mid-cleanup, ending its transcript on a tool result with
#    no final message. Raise the ceiling so the gate loop can finish in one shot.
#    (See book/genesis/tools/agent_stop_diag.sh for the diagnostic that found this.)
for f in "$AGENTS_DIR"/*.md; do
  if grep -qiE '^maxTurns:' "$f"; then
    sed -i -E 's/^maxTurns: *[0-9]+/maxTurns: 120/I' "$f"
  fi
done

# 4) VERIFY the full expected agent set is installed. The pipeline depends on all
#    of these being dispatchable from the first turn so we default to using them
#    (not hand-writing chapters). Loudly flag any that are missing.
EXPECTED=(book-orchestrator book-researcher book-architect book-writer \
  book-evaluator book-editor book-disruptor book-packager \
  entity-tracker continuity-guardian dialogue-polish hook-craft)
missing=()
for a in "${EXPECTED[@]}"; do
  [ -f "$AGENTS_DIR/$a.md" ] || missing+=("$a")
done

echo "Installed book pipeline agents into $AGENTS_DIR (maxTurns normalized to 120):"
ls "$AGENTS_DIR"
if [ "${#missing[@]}" -eq 0 ]; then
  echo "OK: all ${#EXPECTED[@]} expected sub-agents are installed and ready to dispatch."
else
  echo "ERROR: ${#missing[@]} expected sub-agent(s) MISSING: ${missing[*]}" >&2
  echo "       Re-run this hook or re-clone $BSS_REPO; do not hand-write chapters until fixed." >&2
fi

# 5) Cross-model SECOND-OPINION tooling (Google Gemini), used by
#    book/genesis/tools/gemini_review.sh and the /gemini-second-opinion command.
#    Only sets up when a key is available. To PERSIST across ephemeral containers,
#    set GEMINI_API_KEY as an environment secret in the Claude Code web environment
#    settings (a hand-pasted ~/.gemini_env lives only for one container's lifetime).
if [ -n "${GEMINI_API_KEY:-}" ] || [ -f "$HOME/.gemini_env" ]; then
  if ! command -v gemini >/dev/null 2>&1; then
    echo "Installing Gemini CLI for second-opinion reviews..."
    npm install -g @google/gemini-cli >/dev/null 2>&1 \
      && echo "Gemini CLI installed ($(gemini --version 2>/dev/null | head -1))." \
      || echo "warn: Gemini CLI install failed; /gemini-second-opinion will be unavailable." >&2
  fi
fi

# 6) OpenMontage (https://github.com/calesthio/OpenMontage) — evaluation track.
#    AGPL-3.0 agentic video-production system; intended for FREE book-trailer
#    creation (Piper TTS narration + open-footage archives + Remotion/FFmpeg).
#    Best-effort clone to /tmp/openmontage (OUTSIDE this repo, so AGPL copyleft
#    never touches the Saeren codebase — never copy its source in).
#    NOTE (2026-06-25): the first attempt to clone this in the web environment
#    returned a 403 from the egress proxy — github.com/calesthio/OpenMontage is
#    NOT on this session's network allowlist. If the clone still 403s, the fix is
#    to add the host to the environment's network policy (see
#    https://code.claude.com/docs/en/claude-code-on-the-web) or install locally.
#    Non-fatal: a failure here must never block the book pipeline.
OM_REPO="https://github.com/calesthio/OpenMontage"
OM_DIR="/tmp/openmontage"
if [ ! -d "$OM_DIR/.git" ]; then
  echo "Attempting OpenMontage clone (book-trailer evaluation track)..."
  if git clone --depth 1 --quiet "$OM_REPO" "$OM_DIR" 2>/dev/null; then
    echo "OpenMontage cloned to $OM_DIR (external to repo; AGPL boundary intact)."
  else
    rm -rf "$OM_DIR" 2>/dev/null || true
    echo "warn: OpenMontage clone failed (likely the egress-policy 403 noted above)." >&2
    echo "      Allowlist github.com/calesthio/OpenMontage in the env network policy, or install locally." >&2
  fi
fi
