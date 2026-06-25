# Continuity Check: Book Three, Chapter 6 ("The Cost of Half-Sight")

**Date:** 2026-06-25
**Mode:** Single-chapter audit (Ch.6), ENTITY_STATE.yaml as primary source
**Chapters cross-referenced:** Bk3 Ch.1-5 (via ENTITY_STATE + Ch.5 prose), research/book2-chapter-18-rebirth.md, CLAUDE.md / STATE.yaml guardrails
**Total issues found:** 0 critical · 0 warning · 2 minor (both non-blocking)

---

## VERDICT: CLEAN

Chapter 6 holds every load-bearing canon point checked. No re-learning of the Death symbol, no teacher re-naming, no eye-colour break, no broken cry-guardrail, no void entity, no Marick/Fen on-page, and the end-hook resolves to the correct physical Book One cavern in terms that match the Ch.5 setup and the Bk2 Ch.18 rendering. The two MINOR notes below are polish-level observations, not errors.

---

## ITEM-BY-ITEM VERIFICATION

### 1. Death symbol — KNOWN/USED, no re-learning, no teacher re-named — PASS
- Ch.6 USES the mark to close the mill tear (p33): "her hand came up with the mark already in it, the unjoined ring and the line drawn inward toward the centre it never reached, because her hand knew the mark now, her hand had not forgotten the mark since the bridge." This is consistent with established provenance: Drake taught it (Bk2 Ch.8), first used Bk2 Ch.10 on the true-glass, first tear-close Bk3 Ch.4 (Hallow bridge).
- **No re-learning:** the prose explicitly frames it as a thing her hand already owns "since the bridge" (= Ch.4). Correct.
- **No teacher re-named:** Drake is not invoked here; the mark is simply drawn from muscle memory. The CRIT-001 "taught by Raizen" error from the Ch.4 draft is NOT reintroduced — Raizen does not teach or re-teach in Ch.6.
- **Form matches canon exactly** (unjoined ring + inward line that never reaches centre; "unsays the making"). Confirmed again at p133.
- **"Asks nothing" danger preserved:** p33 "it cost her nothing, and it took the length of a breath, and it was a breath too long." Consistent with the-two-tear-close-methods (free method) and the Bk3 moral spine. Good.

### 2. Half-sight mechanic — "read it a beat too late" — PASS (and notably well-executed)
- ENTITY_STATE: sight SPENT in Bk2 Ch.18 rebirth, returning slowly, "still thin at the near and short at the far... a lamp turned low that lit the road ahead and left the doorstep dark." Ch.6 p19 uses nearly that image and grounds the failure mechanically: she reached north (the far rim, where she trained it) and the near doorstep was dark.
- This is consistent with Ch.5, where her sight reaches "further than a month ago and still guttered at the end" and is trained on the far rim/trail. Ch.6 p111 makes the causal link explicit and correct: "The sight came back as distance... a thing all reach and no grip... she had spent a year teaching her own returning eyes to look at the far cold edge of everything and not at the warm woman going for the noon bread under her own roof."
- Matches Bk2 Ch.18 (sight "burned to the wick," returns "an ember at a time," "a long slow count of weeks"). The Ch.6 "returning, layer by guttering layer, reaching further along the cold rim every month" is fully consistent.
- The failure is causally fair (she went north because the danger had always come from north — p15/p41), not a power-level reset. Strong.

### 3. New named villager death — "Sela, the miller's wife" — PASS
- ENTITY_STATE `named_villagers/the-millers-wife`: ALIVE, one of Alice's four bowl-of-water students, "my mother would have called the dark half a sin" (ch-01:p77), previously UNNAMED. Ch.6 names her **Sela** at p83 and reuses the exact established characterization (p25: comes to the long table "four afternoons in five," "the dark half is a sin... her mother wouldn't have held with," "her short laugh"). The four-of-five matches Alice's "four bowl-of-water students" and Ch.5's reference to Alice holding the dark half "for the miller's wife." Consistent.
- **Naming-then-killing is consistent and thematically intentional:** she was deliberately kept unnamed in Ch.1-5 (everyone calls her "the miller's wife"); Ch.6 makes the act of *taking the name* the grief-beat (p81-83, mirroring the Dell's-boy name-taking at Hallow in Ch.4). This is a deliberate echo of the established `dells-boy` pattern ("resolved to learn the name though it makes the weight heavier"). No contradiction.
- **Camera-cut / YA tone — PASS:** p31-35 keep the camera off the act ("Viridia did not look at the worst of it"; "she kept her eyes off the coming-apart"). The horror lives in the aftermath (the empty bowl/empty hand, the flour, the children, the husband). No lingered viscera. Death is "drained" (no wound), matching the established drained-death rule. Fully within the guardrail.

### 4. Raizen — human eyes dark/ordinary, no lightning-blue — PASS
- Raizen appears (p47, p63, p67). No eye-colour is stated, and no lightning-blue/prismatic flare. The only "prismatic" cue is correctly absent here; he is rendered as the patient human presence (bond, plain speech, "in no hurry even now"). LOCKED rule held. (His dialogue at p67 is in-character per traits: speaks plainly, will not tell her an untrue comfort.)

### 5. Viridia canon — appearance, age, grief-inward / no-weep — PASS
- No physical description drift (no hair/eye/height claims that could contradict; none made). Age not stated this chapter (permitted either way in Bk3).
- **No-weep guardrail held EXPLICITLY and repeatedly:** p45 "She did not weep... because no one saw her do it"; p61 "held the careful surface and did not weep"; p83 "did not weep, because no one saw her do it, because she did not"; p149-equivalent at p133. The handling is the correct Book-Three rendering (grief goes "down inward to the low place"), and the wording even guards the rule self-consciously. No sanctioned-break violation (the once-in-a-life break was Bk2 Ch.16 only). Clean.

### 6. Series canon names / forbidden elements — PASS
- **Alice Pembrook** present, in-character (calm hands, soft step, the slow-way voice, the not-reaching kindness, "taught over a desk" — debt runs Alice→Viridia per p49/p101). Correct.
- **Amber** in-character (dresses the true thing in the cross thing — beans/goat at p59; demands the true thing "at the start, not at noon" p95; the two-columns/keeper role p89-93). Correct.
- **Single-n Saeren:** no misspelling. **Jazen:** not mentioned (no misspelling risk). No rose-tinted/Lightwell contradiction.
- **No Johnathan Masters, no void woman:** the void/cold stays abstract ("the cold," "absence," "the long low current"). No entity. PASS.
- **Marick / Fen stay off-page:** neither appears. The "man in the west / a hand / a stranger's mistake" is referenced abstractly (p123, p127) and explicitly DEMOTED ("That was a footprint and she had stopped believing in footprints") — consistent with Ch.5 and with keeping the trigger off-page/unexplained. PASS.

### 7. Source = physical Book One cavern; end-hook resolves to GO there — PASS
- Ch.6 p125 renders the source-cavern in terms that match `locations/the-source-cavern` (DO_NOT_RE_RENDER) and the Bk2 Ch.18 prose verbatim in spirit: "the cavern she had portalled into a year ago, the low rough chamber older than old, the pedestal, the pool that was not water." Matches Bk2 Ch.18 ("low and rough and older than old," "stone pedestal," "it was not water... This is magic itself"). Reached by portal — consistent (no walking-to). No new chamber invented.
- **Matches the Ch.5 setup precisely:** Ch.5 ended resolving to "go to the source itself... a cavern, at a pedestal, over a pool that was not water, where a year ago she had put her hand in and run the weave full." Ch.6 carries that decision forward and HARDENS it into action (she will tell them in the morning; she is going). The escalation from Ch.5's intellectual resolve to Ch.6's grief-driven commitment is explicitly marked (p121: "she had meant it the way you mean a thing you have worked out and not yet paid for... She meant it differently now"). Clean continuity, not a contradiction.
- Reason for going is consistent with the half-sight mechanic: a half-sight that can't read its own mill floor "might see whole" from the centre of the pull (p125, p135). Logically coherent with items 2 and 5.

### 8. Tear-count / fraying-world escalation — PASS
- ENTITY_STATE tear_count: ch-04 = "~6-7 and rising, plus a fainter one beyond." Ch.5 = "Six, seven, the fainter one beyond." Ch.6 p107 reads "six or seven and the fainter ones beyond." Consistent — no count regression or jump.
- Escalation framing held: tears "opening faster than her hand could close them and now faster than her eye could find them" (p113) is a fair, monotonic escalation from Ch.4/5 ("opening faster than she could close them"). The mill tear is correctly the *closest* and *smallest* yet (p31), consistent with Ch.5's revelation that the trail is "coming this way, opening as it comes, working east toward the warmth" — Wend is the next stop on the road. The trail-west + pull-to-source logic from Ch.5 is restated accurately (p129: the rim leans toward the source because the source is her). No drift.

---

## MINOR ISSUES (polish-level, non-blocking)

### [MINOR-001] Day-of-week softness ("a Tuesday, or near enough")
- **Audit:** Timeline (Audit 2)
- **Location:** Ch.6 p7: "It was a Tuesday, or near enough."
- **Description:** Ch.5's timeline is anchored to "the second morning" after the hamlet and "that afternoon / after dark." Ch.6 opens "the morning after" that night and then names a weekday. No prior Bk3 chapter establishes a weekday calendar, so "Tuesday" is unverifiable but also uncontradicted — and the prose hedges it deliberately ("or near enough," with the in-world justification that "the days in Wend had stopped having proper edges"). Not an error; flagged only so the weekday is not later contradicted by a hard calendar reference.
- **Suggested fix:** None required. If a later chapter pins an exact day, reconcile against this soft reference.

### [MINOR-002] "across two years" of Amber's questions vs "~1 year" since rebirth
- **Audit:** Timeline (Audit 2) / cross-book
- **Location:** Ch.6 p93 ("telling me for a year you feel every core there is") is consistent; but note Ch.5 p53 uses "two years of them [Amber's questions]." 
- **Description:** This is consistent on inspection: the source-sense/feeling-every-core dates to ~1 year (since the rebirth), while Amber's *questioning relationship* spans ~2 years (the original "how do you tell the difference" was asked "two years gone," Ch.5 p55, pre-dating the rebirth). Ch.6 p93's "for a year you feel every core" correctly scopes the *core-feeling* to one year. No contradiction — recorded only because the "one year" / "two years" figures sit close together and could read as a slip on a fast pass. Both are internally correct.
- **Suggested fix:** None.

---

## CROSS-REFERENCE NOTES FOR ENTITY-TRACKER (suggested patches, apply on next UPDATE)

```yaml
suggested_patches:
  - entity: "named_villagers.the-millers-wife"
    action: "update"
    value:
      canonical_name: "Sela (the miller's wife)"
      status: "DEAD (ch-06) — DRAINED death; a tear opened at the mill in daylight, Viridia's half-sight read it a beat too late (went north). Named on-page at last (Sela) by the husband at the long table. Camera cut on the act per YA tone."
    reason: "previously ALIVE + unnamed; named-then-killed in Ch.6. Mirrors the dells-boy name-taking pattern."

  - entity: "objects.the-death-symbol.uses_since_then"
    action: "add"
    value: "Bk3 Ch.6 (the MILL tear): USED to close the smallest tear yet; cost nothing, took a breath — 'a breath too late.' The free-method close is now the established reflex ('her hand knew the mark'). No re-learning, Drake not re-named."
    reason: "new on-page use of the mark; keeps provenance log current."

  - entity: "objects.the-horrors.tear_count"
    action: "add"
    value: { at: "ch-06", value: "six or seven + fainter ones beyond; now opening 'faster than her eye could find them' (the failure mode has crossed from her HAND to her EYE)" }
    reason: "escalation update — the threat now outpaces detection, not just closing."

  - entity: "characters.viridia-saeren.status_book3"
    action: "note"
    value: "Ch.6: RESOLVES to go to the physical source-cavern (portal) to read the rim from the centre of the pull — the Ch.5 decision hardened by Sela's death. End-hook = 'She would go to the source.'"
    reason: "advances the Act-One-to-Two pivot; flags the cavern return is imminent (DO_NOT_RE_RENDER applies)."

  - entity: "meta.chapters_tracked"
    action: "update"
    value: [1, 2, 3, 4, 5, 6]
    reason: "Ch.5 and Ch.6 not yet in chapters_tracked (file lists [1,2,3,4]); state is stale for the two newest chapters."
```

> Staleness note (Audit 6b): `meta.chapters_tracked: [1,2,3,4]` does not include Ch.5 or Ch.6. ENTITY_STATE is therefore stale for those two chapters — an entity-tracker UPDATE is recommended before relying on the YAML for Ch.5/6 entities. This audit verified Ch.6 against Ch.5 *prose* directly to cover the gap.

---

## SUMMARY

Chapter 6 is **continuity-clean** against ENTITY_STATE, the Ch.5 setup, the Bk2 Ch.18 cavern rendering, and all locked guardrails. All eight targeted checks PASS. The only findings are two MINOR timeline observations, both of which resolve as internally consistent on inspection. No edits required; the chapter may proceed to the standard gates. Recommend running an entity-tracker UPDATE to fold Ch.5-6 into `chapters_tracked`.
