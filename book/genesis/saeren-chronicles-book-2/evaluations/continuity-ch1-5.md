# Continuity Check: Book Two, Batch 1 (Chapters 1–5)

**Date:** 2026-06-22
**Auditor:** continuity-guardian (batch mode)
**Chapters reviewed:** 1–5 (Book Two, "The Resistance")
**Audited against:** `ENTITY_STATE.yaml`, `outline.md`, `foundation.md`, Book One canon (`research/book1-final-chapter-18.md`, `research/book1-entity-state.yaml`), `CLAUDE.md` canon guardrails, and internal consistency.
**Total issues found:** 8
**Critical:** 0 | **Warning:** 3 | **Minor:** 5

> ENTITY_STATE.yaml `open_contradictions: 0` confirmed; no `flag: "UNRESOLVED"` entries to process first. Canon guardrails verified clean: **Pembrook** (correct, never "Pembroke"), **Jazen** (zero instances of "Jasen"), **rose-tinted spectacles** (Ch.4 — correct), Viridia silver-blonde/green/5'5"/grief-inward (held — no one sees her cry; near-misses correctly resisted in Ch.2 reunion and Ch.4 across-the-case), **trains + motorcars** (trains/rail present, no anachronism), **no Johnathan Masters / no void woman** (the void is handled strictly as ABSTRACT absence — "the *not*", "a nothing... no quality at all"; Ch.5 — canon-correct), **Alice ALIVE/CAPTURED** (resolved Ch.3, on schedule), **Raizen ALL ELEMENTS** (prismatic/every colour, Ch.2 — correct), **unsigned note = Lightwell** (Ch.4 — correct).

---

## CRITICAL ISSUES
None. No character acts on information they cannot possess; no timeline impossibility; no plot resolution depends on unset-up material; no physical-attribute contradiction.

---

## WARNING ISSUES

### [WARN-001] Viridia's age: "fifteen-year-old" on the page vs. "14 at open" in ENTITY_STATE / foundation
- **Audit:** 2d (Age Tracking) / 6a (Entity State Divergence)
- **Chapters:** Ch.4 (and a soft echo in Ch.3 dialogue)
- **Description:** Binding state docs say Viridia is **14 at open, turns 15 during Book Two** (`ENTITY_STATE.yaml` characters.viridia_saeren.age; `foundation.md` §3 "Now: 14 turning 15"). But Ch.4 narration/dialogue has Jazen call her "a fifteen-year-old who holds her face like a woman three times her age." Book Two opens days after Book One's finale, before any birthday is shown on the page, so by the binding docs she should still read as 14. (Note: STATE.yaml's *premise* line also says "fifteen-year-old," so the source canon is itself internally split — but the doc the manuscript must track for state, ENTITY_STATE, says 14.)
- **Evidence:**
  - `ENTITY_STATE.yaml`: `age: "14 at open, turns 15 during Book Two"`
  - Ch.4, ¶ (Jazen): "I see a fifteen-year-old who holds her face like a woman three times her age"
  - Ch.1, ¶ near close: "she had arrived at Hazel six weeks ago" (so only ~6–7 weeks have elapsed since Book One start; no birthday shown)
- **Suggested fix:** Decide the canonical opening age and make it consistent. Cleanest: change Ch.4 to "a fourteen-year-old" to match ENTITY_STATE/foundation, and have the turn-to-15 occur on-page later in the book (the outline never schedules the birthday — recommend adding it as a quiet beat, e.g., around the march). Alternatively, if the author prefers she is already 15, update ENTITY_STATE + foundation to "15 at open" and reconcile the premise. Until resolved, do not let later chapters state a third number.
- **Cascade risk:** Low. If she "turns 15" later, ensure no chapter between here and that beat re-states 14 or 15 in a way that contradicts the chosen birthday placement.

### [WARN-002] War-clock drift: "a week" / "four days gone" vs. the days actually consumed across Ch.1–5
- **Audit:** 2b (Logical Sequence Validation)
- **Chapters:** Ch.1 → Ch.5
- **Description:** Jazen's clock is "a week... to be on the road" with "Four days of it... already gone" (Ch.1). Then: Ch.1 council is "the fifth day"; Ch.2 reunion is the next morning (day ~6); Ch.3 spans the "three days" of the capital line answering (day ~6 → ~9); Ch.4 is "the fourth day after the answer" (≈ day ~13); Ch.5 the next morning (≈ day ~14). That is roughly **two weeks elapsed**, but the "march in a week" deadline is never shown passing or being renegotiated, and Ch.5 still treats the march as future ("two of the days we haven't got"). The clock is now over-spent without acknowledgement.
- **Evidence:**
  - Ch.1: "A week, Jazen had said... Four days of it were already gone."
  - Ch.3: "The three days did not pass..." (capital line)
  - Ch.4: "It was the fourth day after the answer"
- **Suggested fix:** Add one line in Ch.4 or Ch.5 acknowledging the original week has lapsed and the march has been deliberately held (consistent with the council's indecision and the new peace-road plan giving a reason to wait). E.g., Jazen: "The week I named is gone. I held us back when the line came. The roads bought us the delay." This converts an apparent drift into an intentional, characterized choice and keeps Ch.6 ("the window narrows") coherent.
- **Cascade risk:** Moderate. Ch.6 is outlined as the act-close where "the window for a bloodless answer shrinks" — the war-clock needs to be explicitly re-anchored by then or Ch.6's urgency reads as inconsistent with two already-spent weeks.

### [WARN-003] The open-circle reply arrives in "hours," undercutting the established "slow careful days" of the line
- **Audit:** 3d (Communication Tracking) / 5d (internal consistency)
- **Chapters:** Ch.4 → Ch.5
- **Description:** Ch.4 establishes the route to the moderate as deliberately slow: "It's slow and it's careful and it'll cost us two of the days we haven't got." Ch.5 sends the message "that afternoon" and the reply ("*Who else knows.*") returns "Not the slow careful days they'd budgeted for. Hours." The text flags this as intentional/ominous ("the way a careful man answers only one kind of thing"), which mostly licenses it — but a two-days-out courier route cannot physically round-trip in hours unless a faster channel exists. Currently no mechanism is shown for the rapid reply.
- **Evidence:**
  - Ch.4: "two days' travel and a hope" / "cost us two of the days we haven't got"
  - Ch.5: "The line had answered already. Not the slow careful days they'd budgeted for. Hours."
- **Suggested fix:** Add a half-line in Ch.5 establishing the fast channel (a ward-relay, a sympathetic railman's wire, a dark-mage sending) so the speed is a deliberate, explained alarm rather than a physics break. The dread beat is good and worth keeping — just give it a vehicle. (If the world has the "trains/motorcars + telegraph-era" tech implied, a wired relay is the easiest fit.)
- **Cascade risk:** Low, but if a fast channel is established it should be reused/consistent in Ch.7+ (the embassy attempts) rather than reverting to courier-only timing.

---

## MINOR ISSUES (polish-level)

### [MINOR-001] Ward-mage count phrasing: "three men" vs. mage gender neutrality
- **Audit:** 4c (Institutional consistency)
- **Location:** Ch.1 ("three men spent themselves holding it" / "Jazen held a third, and a man called Abe held the last"); Ch.4 ("three men holding the camp unseen").
- **Description:** Consistent internally (Jazen, Hiram, Abe — all male, matches ENTITY_STATE). No contradiction; flagged only as a watch-item: if any later chapter adds/replaces a ward-mage (Hiram is fated to die Ch.11, dropping the ward), keep the count and the "three" phrasing coherent when the third position changes.
- **Suggested fix:** None now. Track for Ch.6 (Hiram wounded) and Ch.11 (Hiram dies / ward drops).

### [MINOR-002] "six weeks" at Hazel vs. Book One duration
- **Audit:** 2a (Explicit time references)
- **Location:** Ch.1 ("She had spent six weeks at a school"); Ch.3 ("a lifetime ago"); Ch.4 ("six weeks").
- **Description:** Internally consistent across Book Two. Flag only to confirm against Book One's actual elapsed span (18 chapters). If Book One spanned materially more/less than ~6 weeks, reconcile. ENTITY_STATE does not pin Book One's duration, so this is unverifiable here.
- **Suggested fix:** Author/architect to confirm "six weeks" matches Book One's timeline; adjust if Book One ran longer.

### [MINOR-003] Mirelle's baby age vs. additive widow backstory
- **Audit:** 1b/2d
- **Location:** Ch.1 ("perhaps a year old"); Ch.4 ("husband two winters dead... borne the baby four months after").
- **Description:** "Two winters dead" + "baby born four months after his death" ⇒ baby ≈ 20 months / ~1.5+ years if "two winters" means ~2 years. Ch.1's "perhaps a year old" is a loose visual estimate and roughly compatible, but the upper edge is slightly tight. Not a contradiction; a soft-edge.
- **Suggested fix:** Optional — soften Ch.1 to "perhaps a year and a half" or leave (a stranger's eyeball estimate of a baby's age is realistically imprecise). ENTITY_STATE already records the additive backstory as canon, so keep the backstory and loosen the visual if desired.

### [MINOR-004] Lor-ar's size drift across chapters
- **Audit:** 1b (Physical description)
- **Location:** Ch.1 ("the size of a large dog"); Ch.5 ("seven feet of him moving like spilled water").
- **Description:** Lor-ar shrinks to house-cat and can resume full ~7ft form (ENTITY_STATE: "shrinks to house-cat"; full 7ft). Ch.1 "large dog" and Ch.5 "seven feet" are both within his established range (he sizes at will). Not an error — flagged only so the editor confirms each size is contextually chosen (camp = downsized for stealth; out past the wards = full size), which the text does support.
- **Suggested fix:** None. Consistent with canon shape-sizing.

### [MINOR-005] Coverage: scout "Ferro" not yet in ENTITY_STATE
- **Audit:** 6c (Coverage gaps)
- **Location:** Ch.2 (Ferro, the returning scout, named, with dialogue and interiority).
- **Description:** Ferro appears in one chapter with substantial dialogue but is not in ENTITY_STATE.yaml. Per the rule, a named entity with dialogue = WARNING-eligible, but Ferro is a single-scene messenger with no fated arc, so MINOR. Mella is named on-page Ch.1 (ENTITY_STATE expected her named Ch.3 — she is named earlier, in Ch.1; harmless, ahead of plan).
- **Suggested fix:** entity-tracker to add Ferro on next UPDATE (single-scene scout, may not recur). Note Mella named in Ch.1 (one chapter earlier than the ENTITY_STATE annotation "named on-page Ch.3").

---

## SUGGESTED YAML PATCHES (for entity-tracker on next UPDATE)
```yaml
suggested_patches:
  - entity: "characters.viridia_saeren.age"
    action: "review"
    reason: "Ch-04 calls her 'a fifteen-year-old'; ENTITY_STATE/foundation say 14 at open. Author must pick canonical opening age and schedule the turn-to-15 on-page (outline does not place the birthday)."
  - entity: "named_villagers.council_recur.mella"
    action: "update"
    value: "named on-page in Ch.1 (not Ch.3 as annotated)"
    reason: "Mella is named earlier than the ENTITY_STATE note states; harmless, but update the chapter reference."
  - entity: "new_characters_book2.ferro"
    action: "create"
    value:
      role: "returning scout (Ch.2); reports the 'collecting not killing' sorting at Hazel"
      status: "single-scene as of Ch.5; may not recur"
    reason: "Named entity with dialogue not yet tracked."
  - entity: "world_rules.communication"
    action: "add"
    reason: "Ch.5 has the moderate's reply return in 'hours' vs Ch.4's 'two days' travel'. If a fast channel (relay/wire) is canonized in the fix, record it so later embassy chapters stay consistent."
```

---

## TRACKING DATABASES (batch — cumulative seed for full-manuscript pass)

### Character Fact Sheet (verified across Ch.1–5)
| Character | Trait | Value | Source |
|-----------|-------|-------|--------|
| Viridia | hair / eyes / build | silver-blonde (silver-green in mana-light), green, slight | consistent Ch.1–5; canon ✓ |
| Viridia | age | "fifteen-year-old" (Ch.4) vs 14 (ENTITY_STATE) | **WARN-001** |
| Viridia | items | dark-blue stone (mother's) + small spear/Dangris | Ch.1, Ch.3 ✓ |
| Viridia | grief | inward; no one sees her cry; near-misses resisted | Ch.2, Ch.4 ✓ |
| Jazen | physical/voice | close-cropped dark hair, dark blue shirt; cries openly | Ch.1, Ch.4 ✓ |
| Amber | nails / hair / tic | chipped black nails, black ponytail, ticks fingers, "no three" | Ch.1, Ch.3, Ch.5 ✓ |
| Raizen | form / affinity / speech | prismatic/all-elements; now speaks | Ch.2 ✓ (canon ALL ELEMENTS) |
| Drake | form / register | pitch black, death-flames/frost, gruff grief | Ch.2 ✓ |
| Lor-ar | size / verbal | sizes house-cat→7ft; "little one" rationed | Ch.1, Ch.5 ✓ (MINOR-004) |
| Alice | status / detail | ALIVE, captured, capital workhouse; "calm hands" | Ch.2–3 ✓ (canon) |
| Hiram | state | grey, spent, half his wick; powers 1/3 ward | Ch.1, Ch.5 ✓ (fated Ch.6/11) |
| Mirelle | role | teaches Moravian; baby on hip; widow | Ch.1, Ch.4 ✓ (MINOR-003) |
| Lightwell | item | rose-tinted spectacles; unsigned note = hers | Ch.4 ✓ (canon) |

### Master Timeline (approximate, days since Book Two open)
- Day 4: Ch.1 (put to work) → Day 5: council. Clock = "march in a week, 4 days gone."
- Day ~6: Ch.2 Raizen returns; scout Ferro's rumor.
- Day ~6–9: Ch.3 "three days" for the capital line; answer = Alice confirmed.
- Day ~13: Ch.4 "fourth day after the answer" — the papers.
- Day ~14: Ch.5 next morning — the rowan test; message sent; reply in hours.
- **Flag: the original "one week to march" window is exceeded without on-page acknowledgement → WARN-002.**

### Knowledge Database (key items, chain verified)
- "Alice alive/captured": origin Ch.2 (Ferro's ridge sighting, rumor) → Ch.3 (Jazen's line confirms via railman + workhouse roll, "calm hands"). Viridia's knowledge path = present/told on-page ✓.
- "Viridia can mend the severing for all at once": origin = the well (Book One) → privately sized Ch.3 → empirically proven on the rowan Ch.5, witnessed only by Lor-ar. No premature leakage to other characters ✓.
- "Lightwell sent the unsigned note": origin Ch.4 (the cache, her hand). Viridia is the only one who knows the note matches her Book-One focus note; Jazen knows only "there was a girl." Knowledge boundary correct ✓.
- "The dateless family-tree name": re-seeded Ch.4 (Lightwell's chart). Held, unexplained, per canon (Book-Three thread) ✓.
- "The void-rim / the *not*": Viridia's private perception, Ch.5; abstract; told to no one. Canon (no entity) ✓.

### Open Plot Threads (batch — all correctly OPEN, none prematurely resolved)
| Thread | Opened | Status |
|--------|--------|--------|
| Alice rescue | Ch.2–3 | OPEN (resolution = war arc, per outline) ✓ |
| The rebirth / consent question | Ch.3, Ch.5 | OPEN (spine; Amber's challenge outlined Ch.9) ✓ |
| Peace road / open-circle moderate | Ch.4–5 | OPEN (hook = "*Who else knows.*") ✓ |
| Lightwell's note / chosen-first | Ch.4 | OPEN (full payoff Ch.10 per outline) ✓ |
| Dateless family name | Ch.4 | OPEN (Book-Three seed) ✓ |
| Void-rim differential | Ch.5 | OPEN (Ch.20 seed; abstract) ✓ |
| Hiram failing / ward fragility | Ch.1, Ch.5 | OPEN (Ch.6 wound / Ch.11 death foreshadowed) ✓ |
| War-clock to the march | Ch.1 | OPEN but **drifting — WARN-002** |

---

## AUDITOR'S NOTE
The batch is in strong continuity health: zero criticals, all canon guardrails held, all binding Book-Two beats for this stretch delivered on schedule (Alice resolved by Ch.3; Jazen development begun Ch.3–4; named villagers Brutus/Mirelle/Hiram seeded as living people; the peace-road thread opened; the void kept abstract). The three warnings are all small, mechanically fixable, and clustered around **time/communication speed** plus the one **age inconsistency** — none block proceeding to Ch.6, but WARN-001 (age) and WARN-002 (war-clock) should be resolved before or within Ch.6 so the act-close urgency stays coherent.
