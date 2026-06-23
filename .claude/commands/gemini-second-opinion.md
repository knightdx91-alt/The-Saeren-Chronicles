---
description: Get an independent cross-model (Google Gemini) second opinion on a manuscript chapter, tuned for fiction.
allowed-tools:
  - Bash(bash book/genesis/tools/gemini_review.sh:*)
  - Read
  - Glob
---

# Gemini Second Opinion (prose)

Run an INDEPENDENT cross-model craft critique of a chapter using Google's Gemini,
via `book/genesis/tools/gemini_review.sh`. This is a SECOND OPINION from outside
our own book-* pipeline — its value is catching things our same-model evaluator is
blind to. Do not defer to it automatically; weigh it against the author's settled
decisions (some "problems" it raises may be deliberate binding beats).

## Steps
1. Resolve the target chapter from `$ARGUMENTS`:
   - If a path is given, use it.
   - If a bare chapter number is given (e.g. "18"), use the current book's
     `manuscript/chapters/chapter-<n>.md` (default book: saeren-chronicles-book-2).
   - If nothing is given, ask which chapter, or default to the latest finalized one.
2. Run: `bash book/genesis/tools/gemini_review.sh <chapter-path> [optional focus notes from $ARGUMENTS]`
   (The script loads GEMINI_API_KEY from the environment or ~/.gemini_env, prefers
   gemini-2.5-pro and falls back to gemini-2.5-flash on quota.)
3. Relay Gemini's critique, then add YOUR take: which points are real and worth
   acting on vs. which conflict with settled canon / binding beats and should be
   noted-not-actioned. Offer to apply the high-leverage fixes you agree with.
