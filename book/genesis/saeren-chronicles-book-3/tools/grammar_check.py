#!/usr/bin/env python3
"""
Saeren Chronicles — mechanical grammar / line-craft gate.

Built 2026-06-29 after reviewer Eilidh Locherty's Book One Ch.1 line-edit exposed a
class of slips the style/rhythm gates do NOT catch: tense/verb-form endings, doubled
words ("Bella Bella"), stray space before punctuation ("said , without"), a/an misuse,
and over-packed sentences. The point is to make "yes, we'll catch it" true BY CONSTRUCTION
instead of by good intentions — the same way style_check.py mechanically blocks em-dashes.

TWO TIERS:
  TIER 1 (deterministic, always runs, GATES — exit non-zero on any error):
     - doubled consecutive word            (e.g. "the the", "Bella Bella")
     - space before , ; : ! ?              (e.g. "said , without")
     - a/an article mismatch               (e.g. "a apple", "an dog")
     These are unambiguous typos with near-zero false positives.
  TIER 1 REPORT (non-gating, judgement needed):
     - the longest sentences per chapter (the over-packed habit). NOT gated, because the
       Book Two/Three house voice uses long polysyndeton on purpose — surfaced so a human
       runs the checklist rule "split at least one of the 3 longest unless load-bearing."
     - double spaces between words.
  TIER 2 (optional, non-gating WARNINGS): full tense/agreement/dangling-modifier scan via
     LanguageTool, IF available (`pip install language-tool-python`, needs Java + a one-time
     engine download). Enable with --languagetool. Never gates (false-positive-prone on
     fiction/dialogue); it is an assist, not an authority.

Usage:
    python3 tools/grammar_check.py                 # tier 1 on manuscript/chapters/chapter-*.md
    python3 tools/grammar_check.py --file manuscript/chapters/chapter-14.md
    python3 tools/grammar_check.py --long 60        # report sentences longer than 60 words
    python3 tools/grammar_check.py --languagetool   # also run LanguageTool (tier 2)

Exit code is non-zero if any TIER 1 ERROR is found, so it can gate the pipeline.
"""
import argparse, glob, os, re, sys

# Doubled-word pairs that are legitimately valid English and must NOT be flagged.
#   "he had had"  ·  "knew that that"  ·  "told you you would" (object + subject)  ·
#   "could not not tell" (deliberate double negative for emphasis)  ·  "where she is, is …"
#   "held her her whole life" (object + possessive). These are function words whose doubling
#   can be valid; doubling of CONTENT words (Bella Bella, river river) is still flagged.
DOUBLE_OK = {"had", "that", "you", "not", "is", "her", "him", "them", "he", "she", "we", "they"}
# Deliberate poetic/archaic doublings (intensifiers/motifs) — not typos.
DELIBERATE_DOUBLES = {"thousand thousand"}
# Word STEMS (leading letters, lowercased) after "a" that begin with a vowel LETTER but a
# consonant SOUND — don't flag.
A_OK_VOWEL = re.compile(r"^(one|once|uni|unit|union|unique|use|used|useful|useless|usual|"
                        r"usually|euro|european|ewe|ufo|u)", re.I)
# Word STEMS after "an" that begin with a consonant LETTER but a silent H / vowel sound.
AN_OK_CONSONANT = {"hour", "hours", "honest", "honestly", "honesty", "honor", "honour",
                   "honorable", "honourable", "heir", "heirs", "homage", "hourly"}

DOUBLE_WORD = re.compile(r"\b([A-Za-z']+)\s+\1\b")
SPACE_BEFORE_PUNCT = re.compile(r"\S(\s+)([,;:!?])")
A_ARTICLE = re.compile(r"\ba\s+([A-Za-z']+)", re.I)
AN_ARTICLE = re.compile(r"\ban\s+([A-Za-z']+)", re.I)
DOUBLE_SPACE = re.compile(r"\S(  +)\S")
WORD = re.compile(r"[A-Za-z']+")

def strip_noise(text):
    """Remove editorial HTML comments and scene-break markers before checking."""
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"^\s*\*\s+\*\s+\*\s*$", " ", text, flags=re.M)  # * * * scene breaks
    return text

def context(text, idx, width=38):
    a = max(0, idx - width); b = min(len(text), idx + width)
    return "…" + " ".join(text[a:b].split()) + "…"

def split_sentences(text):
    # collapse whitespace, then split on sentence-final punctuation followed by space+capital/quote
    t = " ".join(text.split())
    parts = re.split(r'(?<=[.!?])(?=\s+["\'A-Z])', t)
    return [p.strip() for p in parts if p.strip()]

def check_file(path, long_threshold):
    raw = open(path, encoding="utf-8").read()
    text = strip_noise(raw)
    errors = []   # gating
    reports = []  # non-gating

    for m in DOUBLE_WORD.finditer(text):
        w = m.group(1).lower()
        if w in DOUBLE_OK or f"{w} {w}" in DELIBERATE_DOUBLES:
            continue
        errors.append(("DOUBLED WORD", f"'{m.group(1)} {m.group(1)}'  {context(text, m.start())}"))

    for m in SPACE_BEFORE_PUNCT.finditer(text):
        errors.append(("SPACE BEFORE PUNCT", f"'{m.group(1)}{m.group(2)}'  {context(text, m.start())}"))

    def stem(w):
        mm = re.match(r"[A-Za-z]+", w)
        return mm.group().lower() if mm else ""
    for m in A_ARTICLE.finditer(text):
        w = m.group(1); s = stem(w)
        if s[:1] in "aeiou" and not A_OK_VOWEL.match(s):
            errors.append(("A/AN", f"'a {w}'  {context(text, m.start())}"))
    for m in AN_ARTICLE.finditer(text):
        w = m.group(1); s = stem(w)
        if s and s[:1] not in "aeiou" and s not in AN_OK_CONSONANT:
            errors.append(("A/AN", f"'an {w}'  {context(text, m.start())}"))

    for m in DOUBLE_SPACE.finditer(text):
        reports.append(("DOUBLE SPACE", context(text, m.start())))

    sents = split_sentences(text)
    scored = sorted(((len(WORD.findall(s)), s) for s in sents), reverse=True)
    longest = [(n, s) for n, s in scored if n >= long_threshold][:3]
    for n, s in longest:
        snippet = s if len(s) <= 140 else s[:120] + " … " + s[-15:]
        reports.append(("LONG SENTENCE", f"{n} words: {snippet}"))

    return errors, reports

def run_languagetool(paths):
    try:
        import language_tool_python  # noqa
    except Exception as e:
        print(f"\n[tier 2] LanguageTool not available ({e}). "
              f"Install with `pip install language-tool-python` (needs Java). Skipping.")
        return
    try:
        tool = language_tool_python.LanguageTool("en-US")
    except Exception as e:
        print(f"\n[tier 2] Could not start LanguageTool engine ({e}). Skipping.")
        return
    # Categories worth surfacing for prose; spelling/style off (too noisy on invented names).
    print("\n" + "=" * 70)
    print("TIER 2 — LanguageTool grammar/tense WARNINGS (non-gating)")
    print("=" * 70)
    for p in paths:
        text = strip_noise(open(p, encoding="utf-8").read())
        matches = tool.check(text)
        def attr(m, *names):
            for n in names:
                if hasattr(m, n):
                    return getattr(m, n)
            return ""
        def keep_match(m):
            issue = attr(m, "rule_issue_type", "ruleIssueType") or ""
            rid = attr(m, "rule_id", "ruleId") or ""
            return issue == "grammar" and "SPELL" not in rid and "MORFOLOGIK" not in rid
        keep = [m for m in matches if keep_match(m)]
        print(f"\n{os.path.basename(p)}: {len(keep)} grammar warning(s)")
        for m in keep[:40]:
            ctx = (attr(m, "context") or "").replace("\n", " ")
            rid = attr(m, "rule_id", "ruleId")
            reps = attr(m, "replacements") or []
            print(f"   · {rid}: {ctx}  -> {('; '.join(reps[:3]) or '?')}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="manuscript/chapters")
    ap.add_argument("--file", help="check a single file instead of the whole dir")
    ap.add_argument("--long", type=int, default=70,
                    help="report sentences longer than this many words (non-gating)")
    ap.add_argument("--languagetool", action="store_true",
                    help="also run the optional LanguageTool tier-2 scan (non-gating)")
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(base)
    if args.file:
        files = [args.file if os.path.isabs(args.file) else os.path.join(root, args.file)]
    else:
        chap_dir = os.path.join(root, args.dir)
        files = sorted(glob.glob(os.path.join(chap_dir, "chapter-*.md")),
                       key=lambda p: int(re.search(r"chapter-(\d+)", p).group(1)))
    if not files:
        print("no files found"); return 1

    total_errors = 0
    print("=" * 70)
    print("GRAMMAR / LINE-CRAFT GATE  (tier 1: deterministic)")
    print("=" * 70)
    for f in files:
        errors, reports = check_file(f, args.long)
        name = os.path.basename(f)
        print(f"\n{name}: {len(errors)} error(s), {len(reports)} report(s)")
        for kind, msg in errors:
            print(f"   ERROR  [{kind}] {msg}")
        for kind, msg in reports:
            print(f"   note   [{kind}] {msg}")
        total_errors += len(errors)

    if args.languagetool:
        run_languagetool(files)

    print("\n" + "=" * 70)
    print(f"RESULT: {total_errors} grammar error(s) flagged." if total_errors else "RESULT: clean.")
    print("=" * 70)
    return 1 if total_errors else 0

if __name__ == "__main__":
    sys.exit(main())
