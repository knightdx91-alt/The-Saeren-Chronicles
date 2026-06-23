#!/bin/bash
# agent_stop_diag.sh — why did a dispatched sub-agent stop?
#
# Reads the sub-agent JSONL transcripts (small fields only — never dumps the
# whole transcript) and reports, per agent:
#   - record count and last-record role/type
#   - VERDICT: did it finish (last record is an assistant 'end_turn') or was it
#     CUT OFF mid-task (last record is a 'user' tool-result, i.e. it stopped right
#     after a tool call with no final message — the maxTurns-truncation signature).
#
# Background: the Best Seller Studio book-* agents shipped with `maxTurns: 40`,
# which truncated a full chapter write-plus-style/rhythm-gate loop, so the agent
# stopped mid-cleanup. The SessionStart hook now normalizes maxTurns to 120.
# Use this script to confirm the cause if an agent stalls again.
#
# Usage:
#   bash book/genesis/tools/agent_stop_diag.sh            # scan all transcripts for this session
#   bash book/genesis/tools/agent_stop_diag.sh <agentId>  # one agent
set -euo pipefail

# Find the session subagents dir (symlink targets under the tasks scratch dir, or
# the projects dir directly). Override with SUBAGENT_DIR=... if needed.
DIR="${SUBAGENT_DIR:-}"
if [ -z "$DIR" ]; then
  DIR=$(ls -d "$HOME"/.claude/projects/*/*/subagents 2>/dev/null | head -1 || true)
fi
[ -n "$DIR" ] && [ -d "$DIR" ] || { echo "No subagents transcript dir found. Set SUBAGENT_DIR=..." >&2; exit 1; }

FILTER="${1:-}"

for f in "$DIR"/agent-*.jsonl; do
  [ -e "$f" ] || { echo "No agent transcripts in $DIR"; exit 0; }
  base=$(basename "$f")
  [ -n "$FILTER" ] && [[ "$base" != *"$FILTER"* ]] && continue
  python3 - "$f" <<'PY'
import json, sys
f = sys.argv[1]
last = None; n = 0; tool_uses = 0; last_assistant_stop = None
for line in open(f):
    line = line.strip()
    if not line:
        continue
    n += 1
    try:
        rec = json.loads(line)
    except Exception:
        continue
    last = rec
    msg = rec.get("message") or {}
    if isinstance(msg, dict):
        if msg.get("role") == "assistant":
            sr = msg.get("stop_reason")
            if sr:
                last_assistant_stop = sr
            for blk in (msg.get("content") or []):
                if isinstance(blk, dict) and blk.get("type") == "tool_use":
                    tool_uses += 1
role = (last.get("message") or {}).get("role") if isinstance(last.get("message"), dict) else last.get("type")
# Verdict — the reliable signal is the LAST record's role:
#   user  = transcript ends on a tool result (agent stopped right after a tool
#           call with no final message) => cut off, almost always maxTurns.
#   assistant = agent delivered a closing message => finished its task.
if last_assistant_stop == "max_tokens":
    verdict = "CUT OFF (max_tokens on a single message — chapter/output too long for one message)."
elif role == "user":
    verdict = f"CUT OFF mid-task at ~{tool_uses} tool-uses (ended on a tool result, no final message). Hit the turn ceiling (maxTurns)."
elif role == "assistant":
    verdict = "FINISHED (delivered a closing message)."
else:
    verdict = f"UNCLEAR (last role={role}, last assistant stop_reason={last_assistant_stop})"
import os
print(f"{os.path.basename(f)}")
print(f"   records={n}  tool_uses={tool_uses}  last_role={role}  last_assistant_stop_reason={last_assistant_stop}")
print(f"   VERDICT: {verdict}")
PY
done
