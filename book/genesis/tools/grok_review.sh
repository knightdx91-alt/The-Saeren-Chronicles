#!/bin/bash
# grok_review.sh — a cross-model SECOND OPINION on a manuscript chapter, from
# xAI's Grok, tuned for FICTION (not code review). Sibling of gemini_review.sh.
#
# Grok's API is OpenAI-compatible, so this is a plain HTTPS call — no CLI needed.
# Auth: reads XAI_API_KEY from the environment, else sources ~/.grok_env (mode
# 600, kept OUTSIDE the repo so it is never committed).
#
# NOTE: an xAI key with no team credits returns {"code":"permission-denied",...}.
# Buy credits at https://console.x.ai then this works unchanged.
#
# Usage:
#   bash book/genesis/tools/grok_review.sh <chapter.md> [extra focus notes...]
set -euo pipefail

CHAPTER="${1:?usage: grok_review.sh <chapter.md> [focus notes]}"
shift || true
FOCUS="${*:-}"
[ -f "$CHAPTER" ] || { echo "No such file: $CHAPTER" >&2; exit 1; }

if [ -z "${XAI_API_KEY:-}" ] && [ -f "$HOME/.grok_env" ]; then
  # shellcheck disable=SC1090
  source "$HOME/.grok_env"
fi
[ -n "${XAI_API_KEY:-}" ] || { echo "XAI_API_KEY not set (add it to the environment or ~/.grok_env)." >&2; exit 1; }

SYS="You are a veteran editor of upper/mature YA epic fantasy (think the editors of An Ember in the Ashes, Shadow and Bone, The Winner's Curse). You give a candid, specific SECOND OPINION on a single chapter of a draft novel, independent of the author's own pipeline. Flattery is worthless. Series: 'The Saeren Chronicles', Book Two. Protagonist Viridia: silver-blonde, grief held strictly inward, an analytical 'cold working part' that files everything. Register: upper-mature YA — violence is consequence not spectacle, hope/connection kept load-bearing."

INSTR="Critique THIS CHAPTER, in order: 1) what is genuinely NOT WORKING (rank it, be blunt); 2) prose & VOICE (rhythm, over-writing, false/purple lines); 3) PACING & tension (drags/rushes; does it earn its length); 4) EMOTIONAL truth (landed vs asserted; restraint kept or undercut); 5) YA TONE (drift to adult grimdark, or deflated stakes); 6) anything formulaic/AI-sounding + continuity snags. End with the 3 highest-leverage fixes, concrete. Do NOT rewrite the chapter. Prose/markdown only."
[ -n "$FOCUS" ] && INSTR="$INSTR Also specifically address: $FOCUS"

CHAP_TEXT=$(cat "$CHAPTER")

REQ=$(python3 - "$SYS" "$INSTR" <<'PY'
import json, sys
sys_msg, instr = sys.argv[1], sys.argv[2]
chapter = sys.stdin.read()
user = instr + "\n\n===== CHAPTER TEXT BEGINS =====\n" + chapter + "\n===== CHAPTER TEXT ENDS ====="
print(json.dumps({
    "messages": [
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": user},
    ],
    "temperature": 0.4,
}))
PY
<<<"$CHAP_TEXT")

for MODEL in grok-4 grok-3 grok-3-mini; do
  BODY=$(python3 -c "import json,sys; r=json.load(sys.stdin); r['model']='$MODEL'; print(json.dumps(r))" <<<"$REQ")
  RESP=$(curl -s -m 180 https://api.x.ai/v1/chat/completions \
    -H "Authorization: Bearer $XAI_API_KEY" -H "Content-Type: application/json" \
    -d "$BODY" 2>/dev/null || true)
  # credit/permission/model errors -> try next model
  if echo "$RESP" | grep -qiE "permission-denied|does not exist|model_not_found|insufficient"; then
    LASTERR="$RESP"; continue
  fi
  TEXT=$(python3 - <<PY 2>/dev/null
import json
try:
    r=json.loads('''$RESP''')
    print(r["choices"][0]["message"]["content"])
except Exception:
    pass
PY
)
  if [ -n "$TEXT" ]; then
    echo "## Grok second opinion ($MODEL) — $(basename "$CHAPTER")"
    echo
    echo "$TEXT"
    exit 0
  fi
  LASTERR="$RESP"
done

echo "Grok returned no usable output. Last response:" >&2
echo "${LASTERR:-<empty>}" | head -c 500 >&2; echo >&2
echo "(If this says 'permission-denied / no credits', buy credits at https://console.x.ai)" >&2
exit 1
