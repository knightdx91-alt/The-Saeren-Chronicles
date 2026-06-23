---
description: Get an independent cross-model (xAI Grok) second opinion on a manuscript chapter, tuned for fiction.
allowed-tools:
  - Bash(bash book/genesis/tools/grok_review.sh:*)
  - Read
  - Glob
---

# Grok Second Opinion (prose)

Run an INDEPENDENT cross-model craft critique of a chapter using xAI's Grok, via
`book/genesis/tools/grok_review.sh`. Sibling of `/gemini-second-opinion`. Its value
is a DIFFERENT model catching things our own pipeline (and Gemini) miss. Do not
defer to it automatically; weigh it against settled canon / deliberate binding beats.

## Steps
1. Resolve the target chapter from `$ARGUMENTS` (a path; or a bare number → current
   book's `manuscript/chapters/chapter-<n>.md`, default book saeren-chronicles-book-2;
   or ask / default to the latest finalized chapter).
2. Run: `bash book/genesis/tools/grok_review.sh <chapter-path> [focus notes]`
   (Loads XAI_API_KEY from env or ~/.grok_env; tries grok-4 → grok-3 → grok-3-mini.)
3. If it reports 'permission-denied / no credits', tell the user the xAI key needs
   credits (https://console.x.ai) — the tool is correct, the account is just unfunded.
4. Otherwise relay Grok's critique + YOUR take: which points are real vs. which
   conflict with settled canon / binding beats. Offer to apply the fixes you agree with.
   For a TRUE multi-model consensus, run /gemini-second-opinion on the same chapter and
   compare where the two models AGREE (high-confidence) vs. diverge.
