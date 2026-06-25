# Continuity Check: Book Three, Chapter 7 — "The Rim, Read Whole" (End of Act One)

**Date:** 2026-06-25
**Mode:** single-chapter audit (full-manuscript spirit), ENTITY_STATE.yaml as primary source
**Chapter reviewed:** chapter-7.md (~5,522 words)
**Primary source:** ENTITY_STATE.yaml (chapters_tracked 1-6; Ch.7 is the first untracked chapter)
**Cross-checked against:** Bk3 Ch.1-6 (via ENTITY_STATE), Book One cavern prose as preserved in
research/book2-chapter-18-rebirth.md, research/book2-final-chapter-20.md (the "shade"), CLAUDE.md +
STATE.yaml guardrails.

**Total issues found:** 0 CRITICAL · 0 WARNING · 2 MINOR (both non-blocking, log-only)

---

## VERDICT: CLEAN

Chapter 7 is **continuity-clean against all inherited canon and all locked guardrails.** Every
high-risk element flagged in the brief was checked against the actual earlier-book prose (not just the
ENTITY_STATE summary, per the continuity-discipline rule) and matches. The two MINOR items below are
note-level observations for the entity-tracker's next UPDATE pass, not defects in the chapter.

---

## HIGH-RISK ELEMENT CHECKS (the brief's verification list)

### 1. SOURCE-CAVERN FIDELITY — PASS (the most-at-risk element this chapter)
Ch.7 does NOT invent a new chamber. It reproduces the Book One / Book Two Ch.18 cavern with near-verbatim
fidelity and adds no new features.

- Ch.7 p49: "The cave was dark, and cold, and the only light in it came from a stone pedestal a few feet
  ahead, where something glowed." — **identical** to Bk2 Ch.18 p13.
- Ch.7 p51: "low and rough and older than old, the walls unworked stone, the air still and dry and tasting
  of nothing but stone, of the deep places of the world that had never had weather and never would" —
  **identical** to Bk2 Ch.18 p15. Silence-with-weight / "room that had been waiting" preserved.
- Ch.7 p55: "the light came from the pool itself, a clean pale glow with no source above it or below it,
  only the liquid shining of its own accord, and it was not water" — **matches** Bk2 Ch.18 p19.
- Reached by PORTAL/SEAM (p45), sealed "the way it had sealed on the girl who came before" — matches the
  Bk2 Ch.18 p7 seam language and locations/the-source-cavern (`DO_NOT_RE_RENDER: true`).
- Correct ESCALATION of the room's history without altering it: Bk2 said it "had waited for her once
  before… It had her again now." Ch.7 (p51) extends to "a third time" (first-year banking; broken-open
  mending; now half-blind reading) — consistent, additive, not contradictory.
- Crucially, she does NOT put her hand in the pool (p55, p57, p103, p105). This is the chapter's own
  promise and correctly distinguishes this visit from the rebirth.

No invented features (no drip, no second pedestal, no carvings, no new light source). PASS.

### 2. THE VOID/SOURCE PRESSURE DIFFERENTIAL — PASS (escalation, not contradiction)
Bk2 Ch.20 established the differential as "a shade wider… No more than a shade… not enough for anyone to
feel," and predicted she would one day "look again… and the differential would be wider than she
remembered." Ch.7 delivers exactly that prediction:
- p71 quotes the prior measure directly: "*A shade*… *No more than a shade.*"
- p73/p77/p83: "It was not a shade… the shade was a thing that had happened at the start of a thing… the
  sea is past a glass of water." Vastly wider — consistent with the "wider than she remembered" seed.
- ACCELERATION (p79): the rate is steepening, "faster now than a season ago and faster a season ago than
  the season before" — a NEW reading the whole-sight-at-the-fount vantage justifies (p79 explicitly notes
  the wall/half-sight could never read rate). Consistent with the binding pressure-differential mechanic
  ("a held breath gets harder to hold the fuller the lung," Bk2 Ch.20 p83). PASS.
- Stays ABSTRACT throughout — "the place that is not a place," "no person… no name." No void woman, no
  entity. Matches world_rules + void guardrail. PASS.

### 3. MANA-SIGHT — PASS
- Returns to WHOLE only AT the fount (p59-63): "For an hour, in this chamber, a hand's breadth from the
  fount, she had the eyes she used to have." Partial elsewhere; guttering on the way out (p103) and
  "already going dim" / "half-blind" on return (p111). Matches status_book3.sight and the Bk2 Ch.18
  "burned to the wick… an ember at a time" cost.
- Correctly motivated: she came to the source BECAUSE it is the one place sight reads whole (p21, p55) —
  consistent with the year-long rendering of sight "returning as distance, all reach and no grip" (p55),
  i.e., the Ch.1-6 partial-sight engine.
- Distinguished from the rebirth (p25, p61): "it was not the rebirth and she had not opened herself to be
  poured into." She does not pour herself in; she reads. PASS.

### 4. THE DEATH SYMBOL — PASS (known/used, not re-learned)
- p87 references "the mark" she "did now without choosing it" — treated as a possessed, habitual working,
  not learned fresh. p7 "a thing a girl could do something about" and "not a thing a girl could close with
  a mark" both treat the mark as established. No re-teaching, no attribution to Raizen. Matches the
  death_symbol guardrail and the CRIT-001-fixed provenance (Drake, Bk2 Ch.8). PASS.

### 5. RAIZEN — PASS
- p27: "his ordinary brown eyes on the orchard." Human form, ordinary brown — matches the LOCKED eyes
  guardrail. No lightning-blue. PASS.
- Human-learning behavior (p27 "learning, still, after a year, how to be a man at a window"), patience,
  the True-Bond reach that cannot follow her to the source (p31, p113) — all consistent with the bond
  canon ("the one place that was not anywhere"). PASS.

### 6. VIRIDIA GUARDRAILS — PASS
- Silver-blonde/green/5'5"/16: no contradictory physical detail introduced; "silver-blonde girl" (p121).
- Grief inward / NO ONE sees her cry: the "and she did not weep" refrain appears clean three times
  (p87 — alone in the chamber, even with no witness; p119 region via "did not soften it"; p123 closing).
  p87 explicitly frames the not-weeping as involuntary habit "going down inward to the low place." Fully
  consistent with the once-in-a-life Bk2 Ch.16 exception staying closed. PASS.

### 7. NAMES / FORBIDDEN ELEMENTS — PASS
- Single-n **Saeren** (title heading consistent; no misspelling in body). Alice **Pembrook** (referenced
  as "Alice," surname not needed, no variant). **Jazen** referenced only as "a scorch on a flag" (p45) —
  no spelling issue. No Johnathan Masters, no void woman.
- Marick / Fen: correctly OFF-page. The western made-cause stays an explicit abstract inkling — p99: "She
  did not let herself name the something… It was not a face. It was an inkling… a hand she could not see
  and would not invent." No entity, no name, no footprint. This is exactly the guardrail's intent. PASS.

### 8. NO RE-REVEAL OF THE Ch.5 AXIS REVEAL — PASS
Ch.7 treats "the source is her / she is the axis" as fully settled, repeatedly and deliberately:
- p81: "she knew already and from before this chamber whose hand had heaped it… that was settled, that
  was a year old and a name on a table old, that was not why she had come. She had not come to learn she
  was the axis. She had come to learn how large the wheel was."
- p105: "The thing she had been afraid of was true already and was not a maybe. She *was* the weight at
  the centre."
This is a MEASUREMENT-of-scale chapter, not a re-reveal. PASS — and notably well-guarded against the
exact error the brief worried about.

### 9. TEAR / RIM ESCALATION CONSISTENT WITH Ch.4-6 — PASS
- Carries the half-sight count forward accurately: "six tears, seven, the fainter ones beyond she could
  not resolve" (p7) matches objects/the-horrors tear_count (~6-7 and rising at ch-04) and the
  ENTITY_STATE rim note (the half-sight could only ever resolve the near ones).
- The chapter's whole-sight revelation — that the counted tears are "perhaps a hundredth" of a whole-rim
  even leaning (p75) — is a genuine ESCALATION/CLARIFICATION enabled by the new vantage, not a
  contradiction of the prior count. The tears are reframed as the already-failed places ("wrecks the tide
  left"), the differential as the underlying cause. Fully consistent with the binding
  pressure-differential mechanic and the Sela-drained-death engine of Ch.6. PASS.

---

## MINOR ISSUES (log-only; non-blocking)

### [MINOR-001] ENTITY_STATE is now stale relative to Ch.5-7 (expected)
- **Audit:** 6 (Entity State Divergence) / staleness check.
- **Detail:** `meta.chapters_tracked: [1,2,3,4,5,6]` but the body note and timeline only cover Ch.1-4 in
  detail; the file's own header still says fallback-era. Ch.7 (and the Ch.5 axis arrival, the Ch.6 Sela
  drained-death) are not yet reflected in `knowledge`, `timeline`, or `tear_count`.
- **Suggested fix (for entity-tracker, NOT this chapter):** On next UPDATE, add Ch.5-7 to the timeline;
  record the Ch.7 knowledge acquisition (see suggested patch below); update the rim entry to note the
  whole-sight reading that the prior tear-count was ~1/100th of an even whole-rim differential; bump
  `chapters_tracked` to include 7.
- **Cascade risk:** none for the chapter.

### [MINOR-002] "two hundred" Wend population, late-light timing — internal-consistent, just noting
- **Audit:** 4b/2 (geography/timeline).
- **Detail:** p111 "two hundred sleeping and waking warmths of Wend" matches locations/wend (~200). p45
  portal drawn at noon; p111 returns "late flat light of an afternoon… the hour gone in a breath" — the
  in-chamber-hour-passes-as-a-breath is consistent with Bk2 Ch.18 / the source's time-feel; the
  late-afternoon return after a noon departure is internally fine. No fix needed; logged for the timeline.

---

## SUGGESTED YAML PATCHES (for entity-tracker's next UPDATE, after any Editor pass)

```yaml
suggested_patches:
  - entity: "viridia-saeren.knowledge"
    action: "add"
    value:
      fact: "read the rim WHOLE from the fount (Ch.7): the differential is not 'a shade' but vastly wider
             (whole-rim even leaning toward the source) AND accelerating (rate steepening season over
             season); the counted tears were ~1/100th of it. Found a single NON-even fast-worn place — a
             'cut' with a leading edge — far to the GREY WEST: a made cause (no entity/name). Resolves Act
             One: scale confirmed + a direction (west)."
      learned: "ch-07"
      method: "witnessed (whole sight at the fount)"
    reason: "Ch.7 is the End-of-Act-One clarification; not yet in ENTITY_STATE."

  - entity: "the-rim.facts"
    action: "update"
    reason: "rim reading upgraded from escalating-tear-count to whole-rim even differential + steepening
             rate + one west-lying fast 'cut' (the Marick working, off-page/unnamed)."

  - entity: "meta.chapters_tracked"
    action: "update"
    value: [1, 2, 3, 4, 5, 6, 7]
    reason: "Ch.7 audited clean; fold in Ch.5 axis arrival, Ch.6 Sela, Ch.7 fount-reading."

  - entity: "timeline"
    action: "add"
    value:
      chapter: 7
      time: "morning-after the high-wall decision; portal at noon, returns late afternoon (the chamber-hour passes as a breath)"
      season: "spring"
      note: "END OF ACT ONE. Portals to the source-cavern, reads the rim whole; confirms scale + a WEST direction. END HOOK: go west, into the chaos, toward the made-worse."
    reason: "Ch.7 not yet on the timeline."
```

---

## SUMMARY

Chapter 7 passes the audit with zero CRITICAL and zero WARNING findings. The two highest-risk elements —
**source-cavern fidelity** and the **shade→vast differential escalation** — are handled with deliberate,
near-verbatim fidelity to the Book One cavern prose and exact callback to the Bk2 Ch.20 "shade" seed. The
chapter correctly treats the Ch.5 axis reveal as settled (no re-reveal), keeps the western cause an
abstract inkling (no entity/name/Marick/Fen on-page), holds Raizen's ordinary-brown human eyes, keeps the
Death symbol as a possessed-not-relearned working, and lands the "and she did not weep" refrain cleanly
(grief inward, no witness). The only follow-ups are routine ENTITY_STATE staleness updates for the
entity-tracker, not chapter defects.
