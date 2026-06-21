# Revision Plan — Round 6 (The Hazel Years): Fix the Passive Protagonist

*Created 2026-06-21. This is the master execution plan for the next revision cycle. A fresh
session can resume from this file alone. **Nothing in §3 has been applied to the manuscript yet** —
it is gated on author approval of the conversion plan (see §2).*

Current build: **r5, ~89,898 words**, style gate CLEAN, all canon held. Deliverables are
revision-tagged (`delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r5.pdf`,
`manuscript/full-manuscript-r5.md`); the tag is driven by the `REVISION` file at the book root —
bump it (e.g. to `r6`) and rerun `tools/assemble_manuscript.py` + `tools/build_pdf.py` to re-stamp.

---

## 0. Why round 6 exists (the honest agent verdict)

An agent-style reader's report (delivered in chat 2026-06-21) said: strong literary voice, real
heart, top-5%-of-slush prose — but **not yet a clean offer**, held back by:

1. **PRIMARY: a passive protagonist.** Events happen TO Viridia far more than she causes them
   (the focus is given to her, sponsorship spent on her, the pact dispatches her guardians, the
   attack befalls her while she sleeps). Her only fully-active beats are the History-quiz stance
   and the Ch.16 rune-kill — and they're the most alive in the book. *(Source: the agency problem
   is independently flagged in `evaluations/review/analytical-peer-reviewer.md` and `beta-reader-panel.md`.)*
2. **Positioning: a quiet book in a loud aisle.** The introspective, grief-driven voice is the
   book's edge but competes in the most saturated YA lane (magic-school + chosen-one). This is the
   *same* problem as the recurring "still feels a bit slow" notes — not a bug, a position to choose.
3. **Opening velocity.** Improved, but the first real external pressure lands late. NOTE: this
   largely *self-corrects* once Viridia makes a real decision earlier — do NOT keep doing trim passes.
4. **Credibility seams:** "knew all day, ignored it" before the attack (partly paid off now by the
   planted early-misread), selective survival in the massacre, two perfectly-fitted artifacts in six weeks.

**Through-line insight:** the agency problem and the "too quiet/slow" problem are the SAME problem.
A protagonist who *decides* more *feels* faster without cutting a word of the voice. So the
highest-leverage work is NOT more opening trims — it is **seeding 3–5 costly Viridia decisions,
mostly in Ch.1–9.**

---

## 1. Core principle for the fix

**Do NOT invent new plot.** Convert beats that already happen *to* her into beats she *chooses*.
Same events, different grammar of causation. Cheaper, safer, protects canon, adds little length.
Agency without cost is not agency — every converted choice must carry a real **price/risk/sacrifice**.

Conversion candidates the book already hands us:

| Currently happens TO her | Convert to a costly CHOICE |
|---|---|
| The focus is given; the note says "tell her no" | She *decides* to defy/obey the note — and lives with not knowing who steers her |
| Amber's sponsorship is spent on her | She *does* something that earns or provokes it (a risk, a reveal) |
| The pact dispatches Lor-ar/Raizen to her | She *chooses* to call, knowing it breaks a rule and costs her |
| She sleeps through the attack trigger | She *reads* the warning (the planted misread pays off) and makes a wrong call under pressure — passive→tragic-active |

Aim: 4 conversions across Ch.1–9 + a causally-decisive Ch.16 ≈ the "passive" note dissolves.

---

## 2. STEP 1 — DESIGN (read-only, IN PROGRESS / may be done)

Dispatched `book-architect` to produce **`feedback/agency-conversion-plan.md`** containing:
- **Part A — Decision Map:** every beat Ch.1–18 tagged `[ACTS]` vs `[PASSIVE]`, with per-act ratios
  and the worst passive stretches.
- **Part B — Conversion Plan:** 3–5 surgical conversions (current beat → the decision she makes →
  what it COSTS → downstream ripple/canon risk → effort/payoff).

**GATE: the author approves/edits the conversion list in `agency-conversion-plan.md` BEFORE any
prose is rewritten.** This is the one change that can ripple through the whole book, so it is the
author's call. → If that file exists when you resume, read it and bring the conversion list to the
author for sign-off. If it does NOT exist (session ran out), re-dispatch the `book-architect` task
described above.

---

## 3. STEP 2 — IMPLEMENT (only after §2 approval)

Use **`book-editor`** (surgical), chapter by chapter — editor not writer, because we are CONVERTING
existing passages, not drafting new chapters. Optionally follow with **`book-disruptor`** to add
friction where a choice should sting. Also fold in the **credibility-seam** patches (§0.4) here.

Per-chapter discipline (unchanged from prior rounds):
`read → convert the approved beats → python3 tools/style_check.py (must say "RESULT: clean.") →
check word floor → commit`.

Constraints that MUST hold (verify before committing):
- **Canon (absolute):** Pembrook; JAZEN not Jasen; Lady Lightwell rose-tinted spectacles; Viridia
  silver-blonde/green-eyes/5'5", **NO ONE sees her cry** (no new Viridia tears); trains+motorcars;
  no Hazel houses; no Johnathan Masters / void woman; planted refrains EXACT.
- **Fixed climax causality must not be contradicted:** Chancellor came for Lightwell; rose-tinted
  glasses read Lightwell's dark core; Viridia survived because she hid perfectly + the Ch.10-seeded
  rune-on-object craft. Making her *decisive* in Ch.16 means making her ACTIONS matter, not changing
  WHY the attack happened.
- **Gates:** style_check clean (simile ≤4/1k, em-dash ≤4/ch, tics under ceiling, no new distinctive
  cross-chapter repeat — add deliberate terms to the ALLOWLIST, not accidental repeats);
  **word floor ≥ 85,000** (r5 is ~89.9k, ample headroom); **Genesis Floor ≥ 8.5/chapter**.

---

## 4. STEP 3 — VERIFY (read-only, after implementation)

Re-run the analysts and confirm the agency score actually moved (don't trust the editor's self-report):
- `continuity-guardian` — new decisions can't break info-flow ("how does she know that?").
- `character-arc-consistency` — arc reads as growth, no regressions.
- `analytical-peer-reviewer` — the report that DIAGNOSED the passivity; re-run to confirm improvement.
- `beta-reader-panel` — re-score; target lifting **Hostile (was 6)** and **Critic (was 7.5)**, whose
  complaint was agency. (r5 panel average was 7.7: Devourer 9, Devoted 9, Critic 7.5, Casual 7, Hostile 6.)
- `pacing-heatmap` — confirm the opening reads faster now that a real decision lands earlier.
- `book-evaluator` + `style_check.py` — the gates.

---

## 5. STEP 4 — REBUILD & DISTRIBUTE

- Bump `REVISION` → `r6`. Run `tools/assemble_manuscript.py` then `tools/build_pdf.py`.
- `git rm` the old `-r5` deliverables; commit the new `-r6` PDF + `full-manuscript-r6.md`.
- Refresh the public **`book-review`** branch: merge main, regenerate `chapters/ch-NN.txt`
  (strip `<!-- -->` comments), commit, push. (Raw link pattern:
  `https://raw.githubusercontent.com/knightdx91-alt/The-Saeren-Chronicles/main/book/genesis/saeren-chronicles/delivery/production/Saeren-Chronicles-Book-One-6x9-interior-r6.pdf`)
- Update STATE.yaml status + `feedback/progress.md`.

Git identity for verified commits: `git config user.email noreply@anthropic.com && git config user.name Claude`.
Push with `-u origin main`; retry on network error (2s/4s/8s/16s backoff).

---

## 6. NON-PROSE TRACKS (parallel, not blocking the prose fix)

- **Positioning (matters as much as prose here):** run **`book-packager`** to write a query/synopsis/
  comps package that frames the QUIET voice as the FEATURE and targets literary-leaning / boutique
  agents and small presses (NOT big-commercial lead-title pitches). Comps: the interior/literary end
  of YA fantasy.
- **Production (before print/self-pub only):** CMYK / PDF-X conversion, full front + back matter
  (half-title, copyright, etc.), widows/orphans proof pass. See `delivery/production/pdf-print-notes.md`.
  Current PDF is RGB.
- **Fresh human betas** after the agency pass; compare to `delivery/beta-reader/`.

---

## 7. Pathways (set expectations)

- **Big-5 / top commercial agency:** not yet — they'd ask for the agency + opening-velocity revision
  (i.e. exactly this round 6).
- **Boutique / literary-leaning agent or small press:** plausible now; stronger after round 6.
- **Self-pub:** ready after a pro cover, fresh betas, and the production pass.

---

## 8. Housekeeping noticed (cheap, do anytime)

- `manuscript/chapters/chapter-1.md` still begins with a stale Session-1 "STATUS NOTE" header
  (lines ~1–16). It is HARMLESS — `assemble_manuscript.py` strips it, so it never reaches the
  PDF/full-manuscript — but it should be deleted from the source for cleanliness.

---

## TL;DR for next session
1. Open `feedback/agency-conversion-plan.md` (made by `book-architect`). If missing, re-dispatch it (§2).
2. Get the author to approve/edit the conversion list. **Do not rewrite prose before approval.**
3. Implement approved conversions with `book-editor`, per-chapter gate-clean, +credibility-seam patches (§3).
4. Verify with the analysts (§4); rebuild as `r6` + refresh review branch (§5).
5. Then `book-packager` for the quiet-voice query + (later) production prep (§6).
