# Continuity Audit — Book Three, Chapter 4 ("The Easy Mark")

**Date:** 2026-06-25
**Auditor:** continuity-guardian
**File under review:** `manuscript/chapters/chapter-4.md` (~4,850 words)
**Scope:** Ch.4 vs Ch.1–3 (Book Three), Book Two ENTITY_STATE + Ch.18/Ch.20, reconciliation note, STATE.yaml + CLAUDE.md guardrails, Book One cavern canon.

> NOTE: `ENTITY_STATE.yaml` does not exist at the Book-Three project root. Per skill rule 6, this audit was run in **fallback mode** — databases (character facts, knowledge chain, timeline, threads) built from the manuscript and the staged Book-Two canon in `research/`.

**Total issues: 3** — **Critical: 1 | Warning: 1 | Minor: 1**

The chapter is excellent on prose, voice, and theme, and clean on most locked rules (see VERIFIED PASS list). It contains **one CRITICAL knowledge-chain contradiction** that must be fixed before the chapter is finalized: the Death symbol is treated as new knowledge Viridia learns here, but established canon says she already knows it.

---

## CRITICAL ISSUES (must fix before proceeding)

### [CRIT-001] Viridia already knows the Death symbol — Ch.4 wrongly dramatizes her learning it for the first time, and from the wrong teacher

- **Audit:** 3 (Information Flow / knowledge chain) + 5c (payoff vs setup) + locked-rule check.
- **Chapters:** Book Three Ch.4 vs Book Two Ch.8 / Ch.10 / Ch.17.
- **Description:** The whole spine of Ch.4 is Viridia encountering the Death symbol as a *brand-new, buried, unknown* thing that Raizen reveals and teaches her on the spot ("There is another way to shut a door... You only do not know it yet. I do." / "Teach it to me" / he draws it on her palm three times). But the established canon — confirmed in **three** independent sources — is that **Viridia already knows the Death symbol**:
  - `research/roadmap-vs-books-reconciliation.md` L44–45 (the OVERRIDE layer): *"The Death symbol CLOSES PORTALS. Viridia knows it (Drake taught it, Bk2 Ch.8; used on the true-glass Ch.10; Drake killed Meros with death-flame Ch.17)."*
  - `research/book2-ENTITY_STATE.yaml`: Viridia `magic` — *"knows the Death symbol once Drake teaches it (Ch.8)"*; world_rules `death_symbol: "...Drake teaches, Ch.8"`; Drake `role_book2: "...teaches Viridia the DEATH SYMBOL (Ch.8)..."`.
  - STATE.yaml continuity verdicts: Ch.2 *"Death symbol correctly absent"* and Ch.3 *"Death symbol correctly reserved for Ch.4"* — but "reserved" was intended to mean *first on-page USE in Book Three* (the contrast against Ch.2's costly close), **not** a first-time *discovery/learning*. The chapter overshot the brief into re-teaching an already-known working.
- **Two distinct errors bundled here:**
  1. **Knowledge-chain violation (the core error):** Viridia treats a working she has known since Bk2 Ch.8 and already used (Bk2 Ch.10) as something she has never heard of. This is the exact "but how does she know / why doesn't she know?" error a devoted reader catches.
  2. **Wrong teacher:** The chapter has **Raizen** teach it. Canon teacher is **Drake** (Raizen's father, the ~6000-year death-affinity dragon, Bk2 Ch.8). Notably the chapter's own anchor comment (line 3) is canon-correct — it names the fear as **Drake's** ("precisely why **Drake** spent his life afraid of it") — but the prose body never mentions Drake and routes the teaching through Raizen. The anchor and the body disagree.
- **Evidence (Ch.4):**
  - L27: *"There is another way to shut a door, little one. You only do not know it yet. I do."*
  - L31: *"a dragon... remembers the symbols from before they were taught wrong... She had not understood what he meant, and had filed it"* (frames it as a thing Raizen knows and she does not).
  - L35–39: Raizen delivers the full origin of the mark and physically teaches it — *"with one finger he drew the shape there, slow, three times, a thing... her hand seemed to know the moment it was drawn"* — i.e., first-contact learning.
  - L37: *"Teach it to me," Viridia said.* (She would not need to be taught a working she already used in Bk2 Ch.10.)
  - L3 (anchor, canon-correct, contradicts the body): *"...the Death symbol, which asks nothing, and that is precisely why **Drake** spent his life afraid of it."*
- **Contradicting canon location:** `research/roadmap-vs-books-reconciliation.md` L44–45; `research/book2-ENTITY_STATE.yaml` (Viridia magic / world_rules.death_symbol / Drake role_book2 / Lor-ar L92); STATE.yaml guardrail L72.
- **Suggested fix (lowest-disruption, preserves the chapter's theme intact):** Re-frame the Hallow-bridge beat from *learning the symbol* to *the first time she lets herself USE it* — which is the Book-Three brief, and which keeps every beat of the chapter's argument (the easiness, the relief, the "I liked it," Raizen/Alice's warnings) fully intact:
  - L23–27: Change Raizen's line from "You only do not know it yet. I do." to a reminder that she has carried this since Drake gave it to her — e.g. *"There is another way to shut a door, little one. Drake set it in your hand a year ago and you have not let yourself draw it. Draw it now."* This keeps Raizen present (correct: he is the one with her) without making him the teacher.
  - L31–39: Replace the "a dragon remembers the symbols / teach it to me / he drew it three times" learning sequence with **recall**: she remembers Drake teaching it (Bk2 Ch.8), remembers the warning he gave with it, and the chapter's *whole reason it is buried / it asks nothing* speech can be delivered as **Raizen reminding her of what Drake said**, or as her own remembered dread — not as new instruction. Her hand "seemed to know the shape" works even better as *her hand remembering a shape Drake taught her and she has refused to draw*.
  - Keep L35's superb buried-history exposition (the council let it out of the books) — just attribute the *teaching* of it to Drake (past, Bk2) and let Raizen here be the one who tells her it is finally time to use it.
  - The thematic engine of the chapter (easy/clean/asks-nothing → relief → "I already want to do it again") is **undamaged** by this fix; it actually sharpens, because the danger of an *already-owned* free tool she has been refusing is more pointed than a tool just handed to her.
- **Cascade risk:**
  - Check Ch.5+ (when drafted) do not re-introduce the symbol as new — after this fix it is "known since Bk2, first USED in Ch.4."
  - If the fix keeps Raizen *reminding* her of Drake's teaching, ensure Drake is referenced consistently as Raizen's father and the death-affinity dragon (Bk2 ENTITY_STATE) — do not let Drake's death-flame / killing of Meros get muddled with Raizen, who is now human with no death affinity on page.
  - The anchor comment (L3) already names Drake and needs no change; after the fix the body will finally agree with it.

---

## WARNING ISSUES

### [WARN-001] Tear-count arithmetic across Ch.2→Ch.4 — verify the "three or four" baseline is intended, not drift

- **Audit:** 2b (logical sequence) / 5a (thread tracking).
- **Chapters:** Ch.2 L123, Ch.4 L125–129.
- **Description:** Ch.2 establishes she felt *"Three of them, perhaps four"* tears opening at the cold rim. Ch.4 L125 restates this as *"three at the first fire, perhaps four"* and builds the escalation math on it (closed two of four → expected two left → found six/seven+). The arithmetic is internally consistent and the escalation is clearly the intended hook (the rim is *wearing*, not a fixed set of doors). This is **not an error** — flagged only as a verify-point: the entire end-hook depends on the reader trusting that baseline, so make sure no later chapter contradicts "three or four at the first fire." Recommend logging "rim baseline = 3–4 tears felt at Ch.2 fire" as a tracked thread so Ch.5+ don't drift it.
- **Suggested fix:** None required to Ch.4. Add to the running thread log for continuity going forward.

---

## MINOR ISSUES

### [MINOR-001] "Alice's bowl" simile assumes reader recall of a specific image

- **Audit:** 5c (payoff/setup, minor).
- **Location:** Ch.4 L39 — *"a small still mark at the centre where the closing met, like the dot of stillness in the heart of Alice's bowl."*
- **Description:** The image lands and is consistent with Ch.1/Ch.3's bowls-of-water lessons (Alice teaching the dark half = stilling water), so the referent exists and the simile is earned. Minor only: the phrasing "Alice's bowl" (singular, definite) leans on the reader having internalized the bowls motif from Ch.1/Ch.3. It reads fine; noted purely for awareness. No fix needed.

---

## VERIFIED — LOCKED RULES THAT PASS

All of the following were checked against the chapter text and confirmed **clean**:

- **Raizen's eyes = dark/ordinary brown (human form).** PASS. L25 *"the dark ordinary eyes"*; L77 *"the firelight did not catch in his eyes the way it would have caught in a dragon's, the dark human eyes only dark, only ordinary."* No lightning-blue anywhere. Matches Bk2 Ch.19 + Bk3 Ch.1 L19 + the locked rule.
- **Death symbol rendered as eerie / easy / asks-nothing.** PASS. L35 *"It is the simplest working there has ever been"*; L39 *"It asks nothing... the gladness is the danger"*; L51–61 the relief + *"That was easy... I could do that all day."* Exactly the intended danger-register. (The *easiness/asks-nothing* framing is correct; only WHO knows it and WHEN she learned it is the CRIT-001 problem.)
- **Death symbol NOT used in Ch.1–3.** PASS. Confirmed by direct read: Ch.2 closes its tear the COSTLY way (spends source-warmth, hand-over-hand re-knitting, wrung grey — L87); Ch.3 is the political/temptation chapter (no portal close). Ch.4 is its first Book-Three on-page USE. The contrast Ch.2(costly) vs Ch.4(free) is executed cleanly and is thematically strong.
- **Two close-methods consistent.** PASS. Ch.2's costly mending (re-knit worn threads with own warmth, "spent to the wick") and Ch.4's free ending ("it does not mend, it ends") are presented as deliberately opposed and internally coherent (L27, L35, L49–55). Alice's L115 healer-frame ("my whole craft is the slow way... there's always a fast way") seals the contrast.
- **Tears = pulled toward the source she became; worn-open places, not made doors.** PASS. L15 *"the worn place worrying itself wider"*; L27/L129 the rim *wearing*, *"leaned on from the far side... patient and certain and in no hurry."* Matches Ch.1 L123, Ch.2 L83, and STATE.yaml binding beat (Horrors PULLED, not attacking; abstract differential, no entity).
- **Viridia physical/character.** PASS. Age 16 referenced consistently with Ch.1/Ch.3 (no on-page number needed here; Book-Three age-on-page is allowed). Grief inward / no one sees her cry — UPHELD: L91 she says "I liked it" *flatly*; L103 *"let no one see the shame"*; no crying anywhere. Silver-blonde/green-eyes/slight not contradicted.
- **Names / forbidden elements.** PASS. Alice present and consistent (healer, bowls, crooked-tooth lineage from Ch.1). Jazen referenced only in canon-consistent past register (L77 "the things that hurt"; not named here but no misspelling introduced). No "Johnathan Masters," no void woman, no void-rim *entity* (the rim is abstract erosion). Lightwell not invoked (correctly — dead, Bk1).
- **Source-cavern canon.** PASS / not stressed. L57 references "the cavern" only as a past emotional benchmark (the relief "since the cavern") — no new geography asserted, so no conflict with the Bk1 physical-cavern canon.
- **YA tone.** PASS. Dell's boy's death is handled with the camera cut on the act (L19 *"there are things the carrying does not require the watching of"*; L55 the Horror "came apart, and made no sound coming apart, and she did not watch it"). Consequence, not spectacle. Hope/connection load-bearing via Amber + Alice + Raizen.

---

## TRACKING NOTES (for Ch.5+ and the entity-tracker)

- **Knowledge chain — Death symbol:** CANON = known since Bk2 Ch.8 (Drake taught), used Bk2 Ch.10 (true-glass), first Book-Three USE = Ch.4 Hallow bridge. After CRIT-001 is fixed, treat as **owned-and-now-used**, never as newly-learned, in all later chapters.
- **Teacher attribution:** Death symbol teacher = **Drake** (Raizen's father, death-affinity dragon, Bk2). Raizen (human, no death affinity on page) may *remind/prompt* but is not the source of the working.
- **Tear/rim count thread:** baseline 3–4 (Ch.2 fire) → 2 closed (hamlet Ch.2, Hallow Ch.4) → 6–7+ and growing (Ch.4 end). Escalation is intentional ("the rim is wearing"). Hold this baseline.
- **Suggested ENTITY_STATE seed (none exists yet for Book Three):** worth creating `ENTITY_STATE.yaml` for Book Three so future audits run in primary-source mode rather than fallback; seed Viridia.knowledge with the Death-symbol provenance above to prevent recurrence of CRIT-001.

---

## BOTTOM LINE

Chapter 4 is a strong chapter that nails the intended theme (the clean, free, terrible easy way and its seduction) and passes every locked physical/tone/naming rule. **It is NOT clean:** it contains **one CRITICAL knowledge-chain error** — Viridia learns the Death symbol here as if for the first time, taught by Raizen, when canon (reconciliation note + Bk2 ENTITY_STATE) establishes she already knows it from Drake (Bk2 Ch.8) and has used it (Bk2 Ch.10). The fix is a re-frame from *learning* to *first time letting herself use it*, which preserves the entire chapter intact and actually sharpens its argument. Recommend fixing CRIT-001 before finalizing.
