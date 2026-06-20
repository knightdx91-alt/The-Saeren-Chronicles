# Continuity Check: FULL MANUSCRIPT (Chapters 1-18)

**Date:** 2026-06-20
**Chapters reviewed:** 1-18 (full)
**Scope note:** Ch.1-11 locked from prior runs; this audit focuses on Ch.12-18 and their interaction with the locked chapters and ENTITY_STATE.yaml.
**Total issues found:** 0 CRITICAL · 0 WARNING · 3 MINOR
**ENTITY_STATE.yaml:** present, last_updated_chapter 15; open_contradictions: 0.

---

## CRITICAL ISSUES
None.

## WARNING ISSUES
None.

## MINOR ISSUES

### [MINOR-001] Entity state staleness for Ch.16-18
- **Audit:** 6b (staleness)
- **Detail:** ENTITY_STATE.yaml meta is current through Ch.15; Ch.16-18 introduced/used: Jazen-on-page (camp), council members (Coram, Brutus, woman-in-blue, stately silver-bun woman, Hiram/Abe named), the fall of Hazel, the loss of the spellbook/focus in the fire, Viridia's self-cast portals in combat, Alice's unknown status.
- **Suggested fix:** entity-tracker UPDATE for 16-18 before Book-Two work. Non-blocking for Book One delivery.

### [MINOR-002] New minor names introduced after last tracker run
- Healer Brun (Ch.15), Petra (Ch.12/13/15), Regina (Ch.13/15), Della (reused, canon), council members (Ch.18). All consistent within their appearances; none conflict. Log for Book-Two continuity.

### [MINOR-003] "Mrs. Vicks" vs stray "Greyhook"
- Ch.15 uses Mrs. Vicks (creatures teacher), per the Ch.2 deviation note (Vicks is canon; the stray "Greyhook" from the orientation draft was to be resolved to Vicks). No "Greyhook" appears in Ch.12-18. The locked chapters were not re-checked for a stray Greyhook (out of scope — locked). Flag for a Book-Two cleanup pass if it ever surfaced in 1-11.

---

## AUDIT RESULTS

### AUDIT 1: CHARACTER CONSISTENCY
- **Names:** Viridia (540), Lor-ar (169), Lightwell (84), Raizen (43), Pembrook (9). NO "Jasen" (Jazen spelled correctly throughout 12-18). NO "Johnathan Masters", NO "void woman" anywhere. PASS.
- **Physical:** Viridia silver-blonde/green/slight/5'5" — not re-contradicted; "no one sees her cry" HELD across the climax (Ch.14 cave is the sanctioned alone-valve; Ch.16/17/18 are near-misses, never witnessed). Alice: long blond, freckles, one tooth out of line (Ch.12, 16, 18) — consistent. Lightwell: rose-tinted spectacles + blue shoes (Ch.12, callbacks) — consistent; true dark core unhidden Ch.16 (intentional, foreshadowed Ch.9). Lor-ar: house-cat indoors / full size in battle/outdoors — consistent. Raizen: grows, speaks, flies her — consistent. PASS.
- **Behavior/arc:** Viridia's escalating competence (kills in Ch.16) is arc-justified by Ch.11 Dangris training + Ch.14 core growth; flagged in-text as a cost, not a discontinuity. Amber's joke-armor → spent silence (Ch.16-17) → climbing back (Ch.18) is a coherent arc. PASS.

### AUDIT 2: TIMELINE
- Six-week span (arrival "three days orphaned" → finale) consistent. Ch.15 "the last peaceful night" + "days that followed" precede the Ch.16 attack; Raizen "gone two nights past" at Ch.16 open does NOT contradict his presence on the Ch.15 last-night (different, later night). Ch.16 night attack → Ch.17 same-night trek/camp → Ch.18 next morning. PASS.
- Era: trains + motorcars; capital army uses staves/spears/swords, NO firearms; portals as magic. No anachronisms in 12-18. PASS.

### AUDIT 3: INFORMATION FLOW (signature audit)
- **Glasses of true seeing:** planted Ch.13 (worn while assessing) → Ch.14 (worn during the trap-question) → PAYOFF Ch.16 (captain: the Chancellor "looked, with the proper tools," confirmed the ties, signed the decree). Clean forward chain; no character acts on the glasses' meaning before it is earned.
- **Jazen = Lightwell's son:** known to Amber (ENTITY_STATE, withheld since Ch.6) and Lightwell; revealed to VIRIDIA for the first time in Ch.17 (she reacts with genuine shock — "Your mother?"). No forward-reference violation. PASS.
- **The well/source knowledge (Ch.14):** Viridia alone holds it; she tells only Lor-ar (Ch.14 night) and chooses NOT to tell Alice/the Chancellor. No one else references it. PASS.
- **The threshold (decree = war):** Viridia learns it from Amber (Ch.15) before acting on it; the decree is confirmed by the captain (Ch.16). Chain intact.
- **Alice's location:** established in the ward (overflow duty, Ch.13/15/16); Viridia cannot reach it (Ch.16); asks survivors (Ch.17) and Jazen (Ch.18). The not-knowing is maintained with zero accidental confirmation either way. PASS.
- **Raizen alive-but-unlocatable:** True Bond gives life-status (Ch.8 rule) but portals span any distance (Ch.16 rule) → he knows she lives, cannot find her (Ch.17). Logically consistent. PASS.

### AUDIT 4: WORLD RULES
- Magic system (cores, foci, Moravian, both-sided gift, severing) consistent and deepened, not contradicted. The well/source mechanics (Ch.14) are new but self-consistent and align with Ch.4 history-plant + Ch.7 "humans are broken." Death-symbol / explosion-linked-to-protection-rune (Ch.16) consistent with Lor-ar's Ch.11 tactical lesson (reading the thread / their core is open). Camp invisibility (3 casters) consistent within Ch.17-18. No Hazel houses (only year/ranking/sponsorship) preserved. Specialty schools post-Hazel preserved (Alice's ward is in-school helper duty, NOT a specialty track). PASS.

### AUDIT 5: PLOT THREADS
- **Resolved (Book One):** ranking test (Ch.13); the portal/well reward (Ch.14); the attack/escape (Ch.16); reaching the camp + Jazen (Ch.17-18); council decision to march (Ch.18).
- **Open BY DESIGN (Book Two seeds, all deliberate, none orphaned):** Alice's fate; the mother-thread in the well; the void-absence; the family-tree name that doesn't fit (now burned with the spellbook — seeded Ch.2, must be reintroduced via another route in Bk2); the unsigned note's author; the parents' true cause of death; the coming war / march on the capital; whether the severing can be mended.
- **Chekhov check:** Heart of the Spear (Ch.12) — worn, carried forward (background, fine for Bk1). Bone-white death-rod (Ch.13) — thematic, left in the burned vault (acceptable; it served theme, not a gun that must fire). Damascus spears — used (Ch.16). Glasses — fired (Ch.16). No major emphasized setup left without payoff or deliberate carry-forward. PASS.
- **Reverse-Chekhov (payoff without setup):** Viridia casting her own portals (Ch.16) IS set up (Ch.14: she recognizes/learns the portal spell at the well, "she could return by casting her own portal spell"). Self-healing in battle (Ch.16) set up Ch.11. No unestablished payoffs found. PASS.

---

## SUGGESTED YAML PATCHES
```yaml
suggested_patches:
  - entity: "meta.chapters_tracked"
    action: "update"
    value: "extend to 16,17,18"
    reason: "entity-tracker UPDATE needed for the Ch.16-18 events/entities (Jazen on-page, council, fall of Hazel, lost spellbook/focus, Viridia's portals, Alice unknown)."
  - entity: "jazen.on_page"
    action: "add"
    reason: "Jazen appears in person Ch.17-18; reveal of mother-identity to Viridia occurs Ch.17."
  - entity: "council_members"
    action: "create"
    reason: "Coram, Brutus, woman-in-blue, stately silver-bun woman, Hiram/Abe (named ward-casters) introduced Ch.18."
```

## SUMMARY
The Ch.12-18 batch is continuity-clean against the locked chapters, the roadmap, and the canon guardrails. 0 CRITICAL, 0 WARNING. The only follow-ups are an entity-tracker UPDATE for 16-18 and noting the family-tree-name seed was destroyed with the spellbook (re-seed in Book Two). Canon guardrails all honored: Pembrook, rose-tinted, Jazen, Viridia's description + no-one-sees-her-cry, trains+motorcars, no Hazel houses, post-Hazel specialty schools, NO Johnathan Masters / void woman.
