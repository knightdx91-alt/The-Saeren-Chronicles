# Continuity Check: Book Three, Chapter 5 ("What She Will Not Do")

**Date:** 2026-06-25
**Mode:** Single-chapter audit (ENTITY_STATE.yaml = primary source; V4.1 database-first)
**Chapter reviewed:** chapter-5.md (~5,050 words)
**Primary source:** ENTITY_STATE.yaml (v1.0, chapters_tracked [1-4])
**Cross-checked against:** chapter-1.md … chapter-4.md, research/book2-chapter-18-rebirth.md, CLAUDE.md, STATE.yaml guardrails

**Total issues found:** 0 CRITICAL · 0 WARNING · 1 MINOR (non-blocking)

**Verdict: CLEAN.** Chapter 5 honors every locked guardrail and is consistent with the ENTITY_STATE summary and the Ch.1–4 prose. No re-learning of the Death symbol, no mis-attributed teacher, no eye-color slip, no cry, no premature on-page void/Marick/Fen, and the binding pull-mechanic is enacted exactly as the binding_beats require.

---

## CRITICAL ISSUES
None.

## WARNING ISSUES
None.

## MINOR ISSUES

### [MINOR-001] "two years" of Amber's questions — verify against series clock (not an error)
- **Audit:** Timeline (Audit 2) / Information Flow (Audit 3)
- **Location:** ch-5 p25 ("two years of them"), p53–55 ("two years gone"), p69 ("a year ago you reached into every person alive")
- **Description:** The chapter dates Amber's original question ("how do you tell the difference… between you and them?") to "two years gone," and the rebirth to "a year ago." ENTITY_STATE fixes the rebirth at "~A YEAR after" / time-skip ~1 year (timeline ch-1). Amber's first question was asked "in the bad days, when Viridia was first learning what she could do" — i.e. Book One. Book One + Book Two span + the ~1-year valley time-skip is plausibly ~two years, so this is internally consistent. Flagged only because the series does not pin an exact total elapsed time on-page elsewhere; if a later chapter or the packager needs a hard series clock, confirm "two years" against Book One→present. No contradiction with any tracked canon.
- **Suggested fix:** None required. Optionally have entity-tracker add an explicit "elapsed-since-Book-One ≈ 2 years" note to the timeline block so future chapters don't drift.

---

## GUARDRAIL VERIFICATION (the checklist requested)

### Death symbol — PASS
- Ch.5 treats the mark as **known and already used**, never re-learned. p81: "The Death symbol had taught her that already, on the Hallow bridge, the thing that asked nothing." This correctly references the Ch.4 FIRST-USE-TO-CLOSE-A-TEAR (objects/the-death-symbol.first_used / uses_since_then; the-two-tear-close-methods.free → ch-04).
- **No teacher named in Ch.5** — so no risk of the CRIT-001 "taught by Raizen" error recurring. The chapter does not assign Drake's lesson to anyone; it simply assumes prior mastery. Consistent with locked_guardrails.death_symbol.
- p157 correctly establishes the mark's LIMIT against the new threat: "You do not draw a symbol against yourself… you do not draw a symbol against yourself." The mark ends a door; the pull is not a door. This respects the PROVENANCE ("it ENDS… unmakes any made door") without overreaching.

### Raizen — PASS
- Raizen appears only in a list of cores Viridia senses (p89, p163). **No eye color rendered**, so the locked dark/ordinary-brown rule cannot be violated. No lightning-blue anywhere. Consistent with locked_guardrails.raizen and raizen.physical.eyes (LOCKED).

### Viridia physical / grief-inward — PASS
- No physical re-description that could drift (no hair/eye/height restatement). Consistent by omission.
- **No-cry guardrail explicitly honored** and self-aware about it: p149 "she did not weep, because she did not, because no one saw her do it and she did not do it alone either." This is the correct Book-Three posture (grief inward; the sanctioned break was Bk2 Ch.16 only). PASS on locked_guardrails.viridia.
- Age: not numerically restated in Ch.5; no conflict.

### Canon names — PASS
- "Alice" referenced (no surname mis-spelling); "Amber" consistent; no "Saeren"/"Jazen"/"Lightwell"/"Pembrook" mis-spellings introduced (none of those proper nouns appear in spell-at-risk form). Single-n Saeren not at issue (not written out). PASS.

### Void / Masters / Marick / Fen — PASS
- The western-lab thread stays **off-page and abstract.** p107 and p159 point at "a far quarter of the world… past the capital… where the maps put pictures of mountains," and a hypothetical "a working, a hand, a man, a stranger's mistake out in the grey west." This is the correct unexplained gesture toward Marick's lab **without naming Marick or Fen** and **without an entity/void woman.** PASS on locked_guardrails.void and the binding final-image discipline (which belongs much later, not here).
- The void itself is treated as the abstract negative/pressure differential (p137), not personified. PASS.

### The pull mechanic (binding beat) — PASS, and this chapter is its on-page LANDING
- Ch.5 is where the half-finished thought finally arrives (matches knowledge.fact "the half-finished thought she keeps filing and refusing to let it arrive" and the-horrors KEY_FACTS "She keeps FILING this thought and refusing to let it arrive").
- The mechanic is rendered exactly per binding_beats and the_rim/the-horrors: Horrors are **pulled toward the source she became** (not attacking), via the **source/void pressure differential** widened by the over-full rebirth. p137: "the source was full… fuller than it had been in six hundred years… the void out past the last of the warmth had been a shade wider after that… the difference… pulled." Matches the-rim.facts ("widened 'a shade'… the basis for the 'pressure differential' that PULLS the Horrors") and world_rules void rule. PASS.
- Source = the **physical Book One cavern**, reached by going there. p159: "a cavern, at a pedestal, over a pool that was not water, where a year ago she had put her hand in and run the weave full." This matches locations/the-source-cavern (DO_NOT_RE_RENDER) and research/book2-chapter-18-rebirth.md (pedestal + pool-that-is-not-water + hand in the pool). PASS — no re-rendering, correct elements.
- Mana-sight spent and returning slowly: p97 "further than a month ago and still guttered at the end"; p19 "she kept her eyes off it yet." Consistent with status_book3.sight ("RETURNING SLOWLY… still NOT whole, guttering at the edge of its reach"). PASS.
- Bella's-name thread correctly **not** followed here (book3_plan reserves the attempt for ~Ch.13); the thread is not even surfaced in Ch.5. No premature payoff. PASS.

### Tear-count escalation / western trail — PASS
- Ch.4 ended at "six… then seven… a fainter one beyond… and beyond it, fainter still, the breath of another," opening faster than she can close them (ch-04:p131; the-horrors.tear_count ch-04 = "~6-7 and rising, plus a fainter one beyond and another breath beyond that").
- Ch.5 carries this forward exactly: p99 "Six, seven, the fainter one beyond, opening faster than she could close them," and the three-nights-ago despair (p99) ties to the Ch.4 high-wall ending. PASS — no count regression or inflation.
- **Western trail** is a NEW reading (chronological ordering of the same tears: hamlet, Hallow, fainter-beyond) and is consistent with the binding premise — the tears march east toward the warmth, and the pull runs west/down to the source. This is the inverse-read of the same mechanic, not a new contradictory geography. The hamlet (ch-02, north past Hallow) and Hallow bridge (ch-04) positions are reused correctly as "stops on its road." PASS.

### Amber / Vale / settlement details — PASS
- **Amber:** behavior matches amber-summers.traits exactly — the moral-conscience question that "grew teeth" (p51–53; trait "THE MORAL CONSCIENCE… 'how do you tell the difference, from the inside, between you and them?'"), deflect-then-go-quiet at the real thing (p43; trait "DEFLECTS the true thing in jokes… goes quiet at the real one"), "the true thing at the start, not at noon" (p89; trait ch-04:p87), black chipped nails (p65; physical nails "black, chipped/bitten"). PASS.
- **Vale:** "Corwin Vale" + two colleagues, from the leaderless capital, the "stronger hand"/run-the-cores temptation, the river-district hand-checking-at-bridges, news a week stale — all consistent with Ch.3 (locations/the-leaderless-capital, organizations/capital-factions). Departure ("down the slow line… second morning") aligns with timeline ch-3 (Vale arrives) → Ch.5 opens the morning after. PASS.
- **Settlement (Wend):** high garden wall as the looking-point north (p23; wend.facts "the HIGH WALL at the top where Viridia reads the cold rim north"), mill that turns, doubled gardens, orchard, "two hundred lives folded into a place built for forty" (p29; wend.facts ~200 into a place that held 40). old Tem's death-before-the-knock referenced (p69; named_villagers.old-tem). Dell's boy off the bridge wall referenced (p155; named_villagers.dells-boy, ch-04). The miller's wife / Alice-holding-the-dark-half-for-her (p33; named_villagers.the-millers-wife + alice role_book3). All PASS.
- **Alice:** "banked and steady" core, the slow-way-over-bowls healer, "send the healer / I won't make her" (p11–13) — consistent with alice-pembrook.role_book3 (the slow-way counterweight) and her changed/calm state. PASS.

### YA tone — PASS
- No spectacle, no on-page viscera (Dell's boy referenced, not depicted). Hope/connection load-bearing: Amber/Alice/Raizen named explicitly as "the thing I have instead of a wall" (p89). Grief inward, no cry. Consistent with locked_guardrails.ya_tone.

---

## INFORMATION-FLOW CHECK (the signature audit)
No violations. Every fact Viridia acts on she is entitled to:
- The pull-toward-the-source revelation is **inferred by her** from her own returning sight/source-sense (method matches knowledge "inferred" / "the half-finished thought… refuses to fully think it"). She is not told it by anyone; it arrives as her own deduction. Correct.
- She has NOT yet told the others (p163 "no one to give it to until morning"; p165 "She would tell them in the morning") — so no character downstream knows the trail/pull conclusion. No forward-reference leak.
- Amber's knowledge ("you reached into every person alive and decided… they're glad, they didn't ask for it") is consistent with what Amber witnessed/was told across Bk1–2 and ch-01 (amber knowledge of the rebirth). No unearned knowledge.
- Vale's knowledge of the city's collapse is his own (he walked from the capital, Ch.3). Consistent.

---

## SUGGESTED YAML PATCHES (for entity-tracker's next UPDATE run, after Ch.5 is finalized)

```yaml
suggested_patches:
  - entity: "meta.chapters_tracked"
    action: "update"
    value: [1, 2, 3, 4, 5]
    reason: "Ch.5 now audited and consistent; extend tracking."

  - entity: "viridia-saeren.knowledge"
    action: "update_flag"
    target_fact: "the Horrors are PULLED toward the source she became — the half-finished thought she keeps filing and refusing to let arrive"
    value: "ARRIVED on-page ch-05:p143-145 — she finally lets the thought finish ('I made this. The pull is the rebirth.'). Change method note from 'refuses to fully think it' to 'inferred + now fully realized (ch-05).'"
    reason: "The binding key-revelation has landed; the filing/refusal is no longer her posture from Ch.5 forward."

  - entity: "viridia-saeren.knowledge"
    action: "add"
    value:
      fact: "the tears form a WESTERN TRAIL marching east toward the warmth; the pull runs west/down to the source; therefore she resolves to PORTAL to the source-cavern to read the rim from its centre"
      learned: "ch-05:p103-159"
      method: "inferred"
    reason: "New plot-driving knowledge + the next-act intention (go to the cavern)."

  - entity: "the-horrors.tear_count"
    action: "add"
    value: { at: "ch-05", value: "~6-7 carried forward (no new count); reframed from 'scatter/weather' to a WEST→EAST TRAIL with a directional PULL to the source." }
    reason: "Ch.5 reframes the same tears rather than adding to the count."

  - entity: "open_threads"
    action: "update"
    target_thread: "the void-rim differential"
    value: "the pull-to-the-source revelation now ON-PAGE (ch-05); Viridia knows she is the cause. Still abstract — no entity."
    reason: "Binding beat realized."
```

These are recommendations only; the entity-tracker applies them on its next UPDATE pass.
