# Continuity Audit — Book Three: The Weight of the Source (r3, 20 ch, ~111,853 w)

**Date:** 2026-07-11
**Mode:** Full-manuscript, REPORT-ONLY (no prose modified).
**Scope reviewed:** All 20 chapters + foundation.md, outline.md, STATE.yaml, CLAUDE.md, ENTITY_STATE seeds; cross-checked against Book One (cavern), Book Two (Ch.18 rebirth/cost, Ch.20 Marick/void-rim seeds) canon and the series guardrails.
**Method:** Full-manuscript greps (hair/appearance, cry-guardrail, age, names, Masters/void-woman, rebirth timing) + close reads of the load-bearing seam/information-flow chapters (Ch.5, 7, 8, 9, 10, 13, 16, 20).

**Total issues:** 1 CRITICAL · 0 WARNING · 3 MINOR
Everything else audited **CLEAN** — see the category roll-up at the end.

---

## CRITICAL

### [CRIT-001] Marick receives "both halves" a FORTNIGHT ago — contradicts the one-year-ago rebirth (and Varissa's own line)
- **Audit:** Timeline / Information-flow / Bk2 seam.
- **Chapter/line:** Ch.8, p.85 (`chapter-8.md:85`).
- **Description:** Marick dates his acquisition of the dark half to two weeks before the lab visit:
  > "And then, **a fortnight ago**, on a grey morning, I held both halves. I don't know why. No one came. No one told me. I woke and the dark half was in me, whole, six hundred years of severed depth handed to a candle…"
  This describes the **rebirth** (the grey morning when everyone woke whole, unbidden), but the rebirth is fixed **~one year before** Book Three opens. The book states this repeatedly and the whole premise rests on it:
  - Ch.1, p.81: holding both halves "was the whole of **what the year had been**."
  - Ch.9, p.73 — Varissa, on the same event: *"It went uneven **a year ago**. I felt it. He felt it. Every old thing on every mountain felt it, the morning the breath shifted…"*
  - Book Two Ch.20 seed (STATE.yaml `open_threads_from_book_two`): Marick is *"the forty-year candle handed a whole core **in the rebirth**"* — i.e., a year ago, not a fortnight.
  A reader tracking the world-state ("everyone has carried both halves for a year") will trip on Marick waking with his a fortnight ago. It is a datable, on-page contradiction with another on-page date in the same book.
- **What is NOT wrong:** Marick's *portal/working* being recent is fine and intended (the current crisis). Only the **dating of when he received the dark half** is off. His culpability beat ("picked up the chalk," ignored the worn warning) is fully consistent with the Bk2 seed.
- **Suggested fix (trivial, one clause):** Change "a fortnight ago" → "a year ago" (or "the morning the world changed"). Confirm the follow-on "No one came. No one told me. I woke and the dark half was in me" still reads as the rebirth (it does). If the author wants the reception to feel recent for drama, an alternative is to make the *wholeness reaching the remote west* explicitly lag — but that contradicts Varissa's "every old thing… felt it a year ago" and Ch.1, so the clean fix is the date change.
- **Cascade risk:** Low. No other line depends on Marick's reception being a fortnight old. Verify no companion phrasing in Ch.16 (Marick's return) re-dates it — checked: Ch.16 does not restate the fortnight (its "aged a fortnight into a year since the valley" refers to time elapsed since the Ch.8 lab visit, which is correct and unrelated).

---

## MINOR

### [MIN-001] "The year" compresses ~1.5 years of elapsed story time
- **Chapter/line:** Ch.1, p.9 (`chapter-1.md:9`).
- **Description:** "The girl who had walked out of the burning school had been fourteen… **The year** had not given the forty back, but it had given her the number." She is 14 at the Book One school-attack, turns 15 on-page in Book Two (six weeks), then ~1 year skip → 16. So ~1.25–1.5 years, two birthdays, have passed since the burning school, not "the year." The age arithmetic itself is **consistent** (see AGE roll-up); only the singular "the year" reads slightly loose against the fourteen→sixteen span. Not a contradiction — "the year" most naturally reads as the skip-year specifically. Optional to leave as voice.
- **Suggested fix:** None required. If tightening: "the years had not given the forty back."

### [MIN-002] Viridia's canonical hair color is never re-established until Ch.8 (noted as a POSITIVE, not an error)
- **Chapters:** first explicit appearance-tag is Ch.8 ("the plain **silver-blonde** girl," pp.7, 69, 149).
- **Description:** No physical hair descriptor appears in Ch.1–7. This is **not** drift — when the color IS stated it is correctly **silver-blonde** every time, and the Book-Two "silver-green" error does **NOT** recur anywhere (grep-confirmed: zero instances of "silver-green"). Flagged only so the author knows the appearance re-anchor lands late; unproblematic in a tight-3rd interior voice.
- **Suggested fix:** None.

### [MIN-003] Alice's surname never appears on the page in Book Three
- **Description:** Alice is referred to only as "Alice" throughout. **PEMBROOK** never appears — but neither does any misspelling, so the guardrail is not violated. Noted for completeness only.
- **Suggested fix:** None (surname-less is fine for the found-family register).

---

## CATEGORY ROLL-UP (explicit clean statements)

- **Names / spelling — CLEAN.** Series name **Saeren** correct throughout; no "Saeran/Serren." No "Pembroke," no "Jasen." Jazen/Meros/Lightwell are dead and correctly absent. Marick / Fen / Zoran / Moravian / Dangris / Lor-ar all spelled consistently.
- **Hair / appearance drift — CLEAN.** **Silver-blonde** held (Ch.8 ×3); **zero** "silver-green." Raizen's human eyes consistently **ordinary dark/brown** (Ch.7, 14, 16, 20) — the Bk2 Ch.19 dimming held; lightning/prismatic reserved for the dragon nature (shimmer off his fingers only). Drake addresses Viridia as **"child"** consistently (Ch.9, repeatedly) — canon held.
- **Cry-guardrail — HELD/CLEAN.** No public weeping anywhere. "Did not weep" recurs as the load-bearing motif (Ch.6, 7, 9, 10, 13); burning eyes are explicitly "looked down until it passed… did not count" (Ch.16, 20). The **one sanctioned break** is correctly the **Ch.10 private bond-share to Raizen alone** ("she let him see her break… this she chose"), framed as the deliberate private mirror of the Bk2 Ch.16 public break — and even it is **not tears** (an inch given down the bond; the face stays flat). No third break. Ch.20 explicitly reaffirms "had not wept… the guardrail held."
- **Age-on-page — CLEAN.** "Sixteen" stated plainly and consistently (Ch.1 ×3, Ch.9 Varissa "You are sixteen," Ch.18 "She was sixteen years old," Ch.9 Drake "any sixteen years"). Consistent with 14-at-the-burning-school and the confirmed ~1-year skip. The Bk2 no-number rule correctly does not apply here (author decision 2026-06-24). Only the loose "the year" phrasing in MIN-001.
- **Information flow (who knows what when) — CLEAN.** The gut-punch knowledge chain escalates without any forward-reference violation: Ch.5 she first *suspects* the pull points at the source/her (end hook, tentative) → Ch.7 *measures* the rim wide at the cavern → Ch.9 Drake *confirms* it aloud ("it's the rebirth") → Ch.10 the *emotional/moral landing* with sight whole. Each stage correctly treats the fact as already-suspected, not newly-invented. Marick's culpability ("picked up the chalk," read and dismissed the worn warning) is consistent Ch.8 ↔ Ch.16 ↔ Bk2 Ch.20 seed (except the CRIT-001 date). The **Bella-thread reveal (Ch.13)** is consistent with the Bk2 Ch.18 seed ("warm unfollowable thread… her mother's name… no bottom") and deepens it (mother "was the valve" and went) without contradicting anything established.
- **Plot threads — CLEAN (no orphans found).** All Bk2-carried threads land: Marick opens/ends (Ch.8, 16, camera-cut death, YA-consistent); **Fen the assistant survives and RUNS** (Ch.16, 20); Bella's-name thread attempted + paid (Ch.13, the "personal climax at ~Ch.13" the roadmap called for); Mrs. Zoran returns as the trained counterweight (Ch.13); Dangris/pact resolved lightly in the balance finale (Ch.16 standing-with, Ch.20 "we will come again"); Lor-ar acknowledged as released/quiet (Ch.20); Raizen human/True-Bond long-life weight carried to the close (Ch.20). Balance-not-victory resolution enacted (Ch.17–19). No introduced-with-emphasis object or setup left dangling.
- **Book-Two ↔ Book-Three seam — CLEAN (except CRIT-001).** Physical **source-cavern** matches Bk1 Ch.14 / Bk2 Ch.18 (low unworked stone, pedestal, self-lit pool "not water," split symbol, reached by seam) — Ch.10, 13, 16. **Rebirth cost = sight spent, returning slowly across the year** is honored precisely (Ch.1, 10 "the wick she had burned to nothing here a year ago," Ch.13 sight "come the rest of the way back"). **Void-rim differential widened** since the rebirth's "shade" (Bk2 Ch.20) is measured vastly wider and accelerating (Ch.7). Void stays **abstract, no entity**.
- **Finale "explains nothing" guardrail — CLEAN.** No "Masters," "Johnathan," or "void woman" in any prose (grep hits were only the Ch.17/18/20 HTML comment headers stating the rule). The Ch.20 severed-tentacle / Fen-runs / Viridia-feels-a-void beat is rendered as an unexplained absence ("a place where a core should be and is not… she did not know what it was or where"), landing on the wrongness and stopping. The MotV bridge is left to sit, exactly per the binding beat.

---

## Bottom line
Book Three is in strong continuity health. **One** substantive fix before print (CRIT-001, a one-clause date change in Ch.8 so Marick's wholeness dates to the rebirth "a year ago," not "a fortnight ago"). The three MINORs are optional/positive. All series guardrails — Saeren spelling, silver-blonde (no silver-green), Raizen's dark eyes, Drake's "child," the cry-guardrail with its single sanctioned Ch.10 private break, plain age-sixteen, the physical cavern, and the unexplained void finale — are held.
