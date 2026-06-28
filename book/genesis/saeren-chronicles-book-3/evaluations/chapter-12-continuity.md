# Continuity Check: Book Three, Chapter 12 ("The Thing She Fought")

**Date:** 2026-06-28
**Mode:** Single-chapter audit (Ch.12 vs Ch.1–11, ENTITY_STATE.yaml, STATE.yaml guardrails/binding_beats, and Book One/Two prose where reused)
**Scope reviewed:** chapter-12.md against chapters 1–11; ENTITY_STATE.yaml (DETAILED through Ch.10, Ch.11 fold-in still pending); STATE.yaml guardrails + binding_beats; Book Two Ch.8 (Death-symbol provenance) and Ch.16 (the leash echo).

**Total issues found:** 5
**Critical:** 0 | **Warning:** 0 | **Minor:** 5

No fixes applied — nothing was clearly wrong. All five items are MINOR (tracking/fold-in notes), not prose defects.

---

## CRITICAL ISSUES
None.

## WARNING ISSUES
None.

---

## TARGETED CHECKS (all PASS)

### 1. Grief-inward guardrail — PASS
Viridia is NOT seen crying and does not weep anywhere in Ch.12. The only "weeping" instance (p173) is the **townspeople**: "the machinery starting up again over people who had not yet finished weeping." No third sanctioned break is added.
- The on-the-wall temptation peak (p131, p149) is rendered as her established tells — "pressed both palms down against the cold new stone" / "took her hands off the stone" — i.e. the flat-face/white-knuckle register, not a break. Consistent with the Ch.10 ruling that the room only ever gets the flat face.
- The leash beat (Raizen's hand p135–137, Amber's words p139–143, Alice p145) echoes the Bk2 Ch.16 hand-on-arm **without copying it** (explicitly "Not holding her down… they were not a leash and they were not a cage," p147) — as the chapter's own header intends. Clean.

### 2. Death symbol — PASS (named-but-NOT-used; attribution correct)
The Death symbol is referenced twice, both as the thing she is **not** using:
- p163: "not closing it, **not the Death symbol**, just her presence, the source's own weight set against the lean of the cold."
- p165: "there was no symbol to draw that would do it for her, no clever stroke, no easy mark that asked nothing."
This is the intended Ch.12 contrast: the mark would close the door cheaply; she instead **holds the doors with her own presence** at continuous cost. No misuse, no fresh-learning, no mis-attribution to Raizen. Consistent with ENTITY_STATE provenance (Drake taught it, Bk2 Ch.8; closes a DOOR; there is no mark for a pressure) and with the Ch.7 limit ("you do not draw a symbol against yourself"). The "holding the doors" framing matches the Ch.11 vow (Ch.11 p161, p163).

### 3. The pull reveal — PASS (not re-revealed)
The fact that the Horrors are pulled to the source = Viridia is treated strictly as **established background**, never re-revealed as new. It surfaces only as reasoning *from* the known fact:
- p79: "the cold lean toward the spilling the way it leaned toward all the new fullness… the cold always knew it."
- p185 (Amber): "a cold thing leaning on the whole world because of **a mercy you'd do again**."
No restatement of the binding pull-reveal as discovery. Correct (the reveal landed Ch.5, was measured Ch.7, felt Ch.10).

### 4. Character / series canon — PASS
- "Viridia Saeren" (p129) — correct **single-n Saeren**.
- Raizen: human, hand "large and careful, the way he touched things now that he could break them" (p137) — matches Ch.11 p9 verbatim-in-spirit. **No eye-color reference, no lightning-blue** anywhere in the chapter (the LOCKED dark/ordinary-brown is not contradicted). Prismatic affinity not invoked here; fine.
- Amber, Alice, Raizen all in-voice and consistent with Ch.11 (Amber "says the thing out loud," Alice "never obeyed an order that stood between her and a person who needed her hands").
- No Viridia age statement in Ch.12 (fine — plain reference is permitted but not required).
- **No Johnathan Masters, no void woman.** The void stays abstract ("the cold," "the void," "a thin place," p79/p159/p163). Clean.

### 5. Timeline / factional consistency with the Ch.11 Lest letter — PASS
Ch.12 pays off the Ch.11 END HOOK and is consistent with the letter's facts:
- Burning-man = whole-mage whose dark half came in wrong, uncontrollable (Ch.11 p85 → Ch.12 p9, p39) — consistent; now named **Harl**, a wheelwright.
- "three hundred people fled to the schoolhouse in the center of town" (Ch.11 p85) → Ch.12 p23/p45/p89 — consistent.
- "the factional assembly asking… formally, to intervene" / two factions disagreeing whether the three hundred have a right to be there (Ch.11 p85, p87) → Ch.12's Coyle vs Renwick, two sashes (p45, p97) — consistent and deepened.
- Travel: "two weeks west by the main line" (Ch.11 p85) → Ch.12 opens on the train down out of the western hills (p5). Consistent. (Minor texture note logged below re: the "eleven days"/"nine days" internal counts.)
- She honors the Ch.11 vow: "I hold the doors… and I don't reach in and fix him" (Ch.11 p161) → Ch.12 p157–163, executed exactly.

---

## MINOR ISSUES (tracking / fold-in; non-blocking)

### [MINOR-001] ENTITY_STATE fold-in pending — new Ch.11/Ch.12 entities not yet tracked
ENTITY_STATE is DETAILED only through Ch.10; the Ch.11 fold-in is already flagged pending. Ch.12 introduces several new entities that need the next entity-tracker UPDATE:
- **Lest** (town; the wrong-shaped new wall; the white square; the schoolhouse) — new LOCATION.
- **Harl** (the burning-man; wheelwright; went whole a year ago; dark half came in wrong nine days ago; burns down by chapter's end, helped to hold what remains — left **alive but unmade/changed**, not killed on-page) — new CHARACTER (minor).
- **Coyle** (~50; assembly-man with a sash; sent the letter; hope-then-cracked) — new CHARACTER (minor).
- **Renwick** (younger; second sash; fed the three hundred across the lines nine days; wants to be the one who "stopped the burning") — new CHARACTER (minor).
- **the three hundred** (the held-breath in the schoolhouse; a woman near her time among them; freed alive at chapter's end) — group entity.
Also fold in the **Lest letter** (Ch.11) and **Mrs. Zoran** (Ch.11 — arrived at Wend on foot per the Ch.11 header; verify on the fold-in and clear her `needs_review`).

### [MINOR-002] Harl's "year of wildness" vs the nine-day onset — internal, consistent (log only)
p67/p165: "He has been going whole all year and there is a year of it in him and it does not run out" — i.e. a year of *stored* dark half, but the uncontrolled *spilling* began nine days ago (p39, p55). Not a contradiction; the prose distinguishes the year-of-fullness from the nine-day giving-way. Logged for the tracker so it isn't mis-recorded as a timeline conflict.

### [MINOR-003] Soft day-count: "eleven days" vs "nine days"
The Lest government was "invented eleven days ago" (p31) and Harl's burning/the siege is "nine days" (p39, p63, p67, p89). Consistent (the wall/government formed ~two days after the burning began). The Ch.11 letter said factional mediators "had tried for six days"; the Ch.11→Ch.12 gap (two weeks' travel) comfortably absorbs the drift from six to nine days of holding. No hard calendar elsewhere to violate. Log only.

### [MINOR-004] "a woman near her time" echo of the hamlet dead
p89 deliberately rhymes the schoolhouse's pregnant woman with the Ch.10/ENTITY_STATE hamlet detail ("a woman who had been quick with a second child," ch-10:p31 / emptied-hamlet-folk). This is intentional motif, not a duplication error — flagged so the tracker records it as an echo, not a continuity slip.

### [MINOR-005] Harl's on-page status is open-ended (seed, not closure)
The camera cuts on the worst (p167, per YA tone) and Harl is brought "briefly back into the shape of a man" and then helped by Alice to "hold what remained" — he is left **alive and changed**, his ultimate fate not stated. Record his status as resolved-this-chapter-but-fate-open (parallel to how Marick was left a live thread), so a later chapter isn't flagged for "reviving" or "dropping" him.

---

## YA-TONE / VOICE SPOT-CHECK — PASS
Camera cut on the worst of the violence (p167: "the camera turns away here, from the worst of it… the horror of that is not for describing and Viridia did not look away from it and will not write it down"). Hope/connection load-bearing via the three-person leash (Raizen/Amber/Alice). Consistent with the series guardrail.

---

## SUGGESTED YAML PATCHES (for the pending entity-tracker UPDATE)
```yaml
suggested_patches:
  - entity: "locations.lest"
    action: "create"
    reason: "new town introduced Ch.12 (wrong-shaped wall, white square, schoolhouse; ~two weeks west by main line)"
  - entity: "characters.harl"
    action: "create"
    value: { importance: minor, role: "the burning-man/wheelwright; dark half came in wrong; left alive+changed, fate open" }
    reason: "Ch.11 END-HOOK payoff; new character"
  - entity: "characters.coyle"
    action: "create"
    reason: "Lest assembly-man (sent the Ch.11 letter); new minor character"
  - entity: "characters.renwick"
    action: "create"
    reason: "rival Lest assembly-man; new minor character"
  - entity: "named_villagers.the-three-hundred"
    action: "create"
    reason: "schoolhouse group; freed alive end of Ch.12 (incl. a woman near her time)"
  - entity: "characters.mrs-zoran"
    action: "review_clear"
    reason: "per Ch.11 header she arrived at Wend on foot — confirm on fold-in and clear needs_review"
  - entity: "meta.chapters_tracked"
    action: "extend"
    value: [11, 12]
    reason: "fold in Ch.11 + Ch.12 (currently detailed only through Ch.10)"
```
