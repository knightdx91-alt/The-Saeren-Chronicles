#!/bin/bash
# gemini_review.sh — a cross-model SECOND OPINION on a manuscript chapter, from
# Google's Gemini, tuned for FICTION (not code review).
#
# Sends a chapter's prose to Gemini with a veteran-YA-fantasy-editor prompt and
# returns a craft critique (voice, pacing, emotional truth, YA tone, continuity,
# what is not working). Same cross-model value as the off-the-shelf "Gemini peer
# review" plugins, but pointed at prose instead of git diffs.
#
# Auth: reads GEMINI_API_KEY. Looks for it in the environment, else sources
# ~/.gemini_env (mode 600, kept OUTSIDE the repo so it is never committed).
#
# Usage:
#   bash book/genesis/tools/gemini_review.sh <chapter.md> [extra focus notes...]
# Example:
#   bash book/genesis/tools/gemini_review.sh book/genesis/saeren-chronicles-book-2/manuscript/chapters/chapter-18.md
set -euo pipefail

CHAPTER="${1:?usage: gemini_review.sh <chapter.md> [focus notes]}"
shift || true
FOCUS="${*:-}"
[ -f "$CHAPTER" ] || { echo "No such file: $CHAPTER" >&2; exit 1; }

# Load the key (env first, then the out-of-repo file).
if [ -z "${GEMINI_API_KEY:-}" ] && [ -f "$HOME/.gemini_env" ]; then
  # shellcheck disable=SC1090
  source "$HOME/.gemini_env"
fi
[ -n "${GEMINI_API_KEY:-}" ] || { echo "GEMINI_API_KEY not set (add it to the environment or ~/.gemini_env)." >&2; exit 1; }
command -v gemini >/dev/null || { echo "gemini CLI not installed (npm i -g @google/gemini-cli)." >&2; exit 1; }
export GEMINI_CLI_TRUST_WORKSPACE=true

PROMPT_FILE=$(mktemp)
trap 'rm -f "$PROMPT_FILE"' EXIT
{
  echo "You are a veteran editor of upper/mature YA epic fantasy (think the editors of An Ember in the Ashes, Shadow and Bone, The Winner's Curse). You are giving a SECOND OPINION on a single chapter of a draft novel — independent of the author's own pipeline. Be candid, specific, and useful; flattery is worthless."
  echo
  echo "Series context: 'The Saeren Chronicles', Book Two ('The Resistance'). Protagonist Viridia: silver-blonde, green eyes, grief held strictly inward, an analytical 'cold working part' that files everything. Register is upper-mature YA — violence is consequence not spectacle, hope/connection kept load-bearing between dark beats."
  echo
  echo "Critique THIS CHAPTER on, in order of importance:"
  echo "1. What is genuinely NOT WORKING (the most important section — be blunt, rank the problems)."
  echo "2. Prose & VOICE: sentence rhythm, over-writing/over-narration, any line that rings false or purple."
  echo "3. PACING & tension: where it drags, where it rushes, whether the chapter earns its length."
  echo "4. EMOTIONAL truth: does the feeling land or is it asserted; is restraint maintained or undercut."
  echo "5. YA TONE: anything that tips toward adult grimdark or, conversely, deflates the stakes."
  echo "6. Anything that reads as AI-generated / formulaic, and any continuity or logic snags you notice."
  echo "End with the 3 highest-leverage fixes, concrete. Do NOT rewrite the chapter. Respond in prose/markdown only; do not attempt to use any tools or read any files."
  [ -n "$FOCUS" ] && { echo; echo "ALSO specifically address: $FOCUS"; }
  echo
  echo "===== CHAPTER TEXT BEGINS ====="
  cat "$CHAPTER"
  echo "===== CHAPTER TEXT ENDS ====="
} > "$PROMPT_FILE"

# Prefer pro (if the project has quota), fall back to flash automatically.
for MODEL in gemini-2.5-pro gemini-2.5-flash; do
  OUT=$(gemini -m "$MODEL" --skip-trust "$(cat "$PROMPT_FILE")" 2>/tmp/gemini_err.$$ || true)
  if echo "$OUT" | grep -qiE "exhausted your daily quota|quota exceeded|RESOURCE_EXHAUSTED|429"; then
    continue
  fi
  if [ -n "$OUT" ]; then
    echo "## Gemini second opinion ($MODEL) — $(basename "$CHAPTER")"
    echo
    echo "$OUT" | grep -viE "256-color support|^Warning: "
    rm -f /tmp/gemini_err.$$
    exit 0
  fi
done
echo "Gemini returned no usable output (all models quota-blocked?). Last stderr:" >&2
cat /tmp/gemini_err.$$ >&2 2>/dev/null || true
rm -f /tmp/gemini_err.$$
exit 1
