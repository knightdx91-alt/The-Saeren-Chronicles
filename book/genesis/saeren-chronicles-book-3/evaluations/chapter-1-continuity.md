# Continuity Check: Book Three, Chapter 1 ("What the World Became")

**Date:** 2026-06-24
**Mode:** Single-chapter audit vs Books One & Two canon (pre-batch)
**Chapter reviewed:** chapter-1.md
**Canon sources read:** STATE.yaml, CLAUDE.md, foundation.md, roadmap-vs-books-reconciliation.md,
book2-ENTITY_STATE.yaml, book2-chapter-18-rebirth.md, book2-final-chapter-20.md, plus actual prose:
Book Two ch.1, ch.2, ch.19 (Raizen transformation), ch.20 (finale).

**Total issues found:** 5
**Critical:** 0 | **Warning:** 2 | **Minor:** 3

---

## CRITICAL ISSUES

None. Every load-bearing canon element checks out (see verification ledger below). Names, spelling,
Viridia's physical/grief canon, the spent-then-returning sight, everyone carrying both halves, the
abstract void with no entity, the drained-death + tear-at-the-rim hook, and the non-over-explanation
of the Ch.10 revelation are all consistent with Books One & Two.

---

## WARNING ISSUES

### [WARN-001] Raizen's human eyes contradict Book Two Ch.19 (rendered "ordinary" there)
- **Audit:** 1b Physical Description Consistency
- **Chapters:** Bk3 ch.1 (¶ at line 19) vs Bk2 ch.19 (line 37)
- **Description:** Bk3 Ch.1 says the transformation "had given him dark hair and the height of a tall
  young man, but the eyes had stayed exactly what they were, the lightning-blue of the prismatic
  dragon looking out of a human face." Book Two Ch.19 — the chapter that actually staged the
  transformation — rendered his new human eyes as **ordinary**: "the light went out of him by
  degrees, dimming down into the ordinary, until what stood there was only a young man... blinking in
  the grey afternoon as if the afternoon were the first thing he had ever seen, which, with these eyes,
  it was." That passage deliberately makes his human seeing new and ordinary; nothing there says the
  dragon eye-color was retained.
- **Evidence:**
  - Bk2 ch.19:37 "the light went out of him by degrees, dimming down into the ordinary, until what
    stood there was only a young man, naked and new and blinking in the grey afternoon... which, with
    these eyes, it was."
  - Bk3 ch.1:19 "the eyes had stayed exactly what they were, the lightning-blue of the prismatic
    dragon looking out of a human face."
- **Suggested fix:** Either (a) drop the "eyes unchanged / lightning-blue" claim and let his human
  eyes read as the Ch.19 "new and ordinary" pair, or (b) if the author WANTS the retained-dragon-eye
  image (it is a strong one), treat it as a deliberate canon addition and log it — but it should not
  be asserted as if Book Two established it, since Book Two established the opposite.
- **Cascade risk:** Low. If kept, log it in the book-changes file as a retro-detail and keep it
  consistent in every later Raizen description in Book Three.

### [WARN-002] "Lightning-blue" + "kind and merciless / missed nothing" is Lor-ar's signature, reassigned to Raizen
- **Audit:** 1b/1c Description & verbal-signature consistency
- **Chapters:** Bk3 ch.1 (lines 19, 33) vs Bk2 ch.1 (line 65), ch.19 (line 145)
- **Description:** "lightning-blue eyes" is, across Book Two, **Lor-ar's** established marker
  (Bk2 ch.1:65 "He turned the lightning-blue eyes on her, kind and merciless at once"; ch.19:145 "the
  lightning eyes... two points of cold blue"). Bk3 Ch.1 maps both that color AND the paired
  "kind, and they missed nothing" register onto Raizen (ch.1:33), then the narration even gestures at
  the overlap ("a combination she had only ever met in two creatures and the other had been a tiger").
  This is arguably an intentional echo, but it currently reads as borrowing Lor-ar's signature wholesale
  and compounds WARN-001.
- **Evidence:**
  - Bk2 ch.1:65 "He turned the lightning-blue eyes on her, kind and merciless at once." (Lor-ar)
  - Bk3 ch.1:33 "He turned the blue eyes on her, and they were kind, and they missed nothing, which
    was a combination she had only ever met in two creatures and the other had been a tiger."
- **Suggested fix:** If WARN-001 is resolved toward "ordinary/new" eyes, this dissolves. If the author
  keeps the lightning-blue, differentiate the register from Lor-ar's exact phrase so Raizen doesn't
  read as a Lor-ar reskin. The explicit "the other had been a tiger" nod can stay as a deliberate
  callback if the author wants it.

---

## MINOR ISSUES

### [MINOR-001] Survivor headcount ("two hundred") — new number, not contradicted but unanchored
- **Audit:** 4d/2 Quantitative consistency
- **Location:** ch.1 lines 11, 107
- **Description:** Book Two Ch.20 says "two hundred of them and more strung back along the road." Bk3
  Ch.1 settles the valley at "perhaps two hundred of them folded into a place that had held forty."
  Consistent with Bk2's "two hundred and more" (Bk2 implies the column was somewhat larger than 200).
  Not a contradiction; flag only so the number stays stable across Book Three.
- **Suggested fix:** None required. Keep "~two hundred" stable in later chapters.

### [MINOR-002] Geography: "Wend," "a day and a half by the slow southern line," east/north — new, internally consistent
- **Audit:** 4b Geography
- **Location:** ch.1 lines 11, 111, 139
- **Description:** Book Two ended walking EAST "into a country that did not know them." Book Three
  places them in a valley settled after "the east road," with the threat coming from the NORTH. No
  contradiction with Bk2. New place-name and rail detail ("slow southern line") are fresh canon,
  consistent with the trains-and-motorcars rule.
- **Suggested fix:** None. Lock "Wend" and "north = the rim/threat direction" for later chapters.

### [MINOR-003] Old Tem / Mrs. Zoran / Marick / Fen not yet present — expected, no orphan
- **Audit:** 5a Plot-thread inventory
- **Location:** chapter-wide
- **Description:** Old Tem is new texture (a valley death, fine). Mrs. Zoran, Marick, and Fen — all
  required threads per STATE.yaml — do not appear in Ch.1; correct for an opening chapter, not an
  orphan. The Marick/lab thread (Bk2 Ch.20) is correctly NOT pre-empted; Ch.1 introduces the drained
  death + rim-tear as the reader-facing first symptom without naming the cause, matching the binding
  "Horrors are pulled, not attacking — do not over-explain" instruction.
- **Suggested fix:** None. Ensure Mrs. Zoran/Marick/Fen land on schedule in later chapters.

---

## VERIFICATION LEDGER (canon checks that PASS)

- **Names/spelling:** "Saeren" (single-n) — correct. Alice present, surname not stated here (Pembrook
  canon intact, not contradicted). Jazen not misspelled (referenced only in sources). Lightwell not
  mentioned — correctly absent (dead).
- **Viridia physical:** "silver-blonde girl" (39, 135) — correct; green eyes / 5'5' / slight not
  re-stated, not contradicted. **Age:** "She was sixteen now" (9) — matches the resolved ~1-year skip;
  STATE.yaml permits stating sixteen plainly in Book Three. The "fourteen... felt forty" retrospect
  (9) matches Bk2's 14-at-open.
- **Grief inward / no one sees her cry:** Held. "did not let the mill yard see her leave it unmade"
  (89); "made her face come back to the careful surface" (129); she tells Amber "a piece of the truth"
  but does NOT weep. The Bk2 Ch.16 break is correctly treated as past (matches Bk2 Ch.20: changed by
  the breaking, not broken open). She no longer hides what she IS (consistent with Bk2 "that, now, was
  not a rule she kept") but still does not cry. No violation.
- **Mana-sight SPENT then RETURNING, not whole:** Strongly correct. Lines 53–55 narrate the blind
  weeks after the cavern and the slow piecewise return across autumn/winter — matches Bk2 Ch.18/20
  ("burned to the wick... an ember at a time, a long count of weeks and beyond"). The rim-tear is
  readable now BECAUSE the sight returned far enough ("the kind of thing I couldn't have seen a year
  ago," 131) — the intended re-acquisition vehicle from the reconciliation note.
- **Everyone carries both halves:** Correct and central (Alice's lesson, 75–79: "You all carry both
  halves now"). Matches Bk2 Ch.18.
- **Raizen human + True-Bond:** Human, on two legs, new to it — matches Bk2 Ch.19. True-Bond as
  warmth "no longer had to stretch over miles" (21) — consistent (life-tied). Prismatic shimmer off
  his fingers (25) carries the all-element/prismatic affinity. (Eye detail flagged — WARN-001/002.)
- **Alice changed/recovering healer:** Correct — calm, warmth "banked not out," the one crooked tooth
  reappearing, healing and teaching again (67–79). Matches Bk2 Ch.19/20, incl. "crooked tooth the
  change could not reach."
- **Amber the conscience:** Correct. Her Bk2 question ("you decided for them... how do you tell the
  difference between you and them," 87) carries from Bk2 Ch.9/18/20; she is the one who "sees the
  carrying." Consistent.
- **Lor-ar:** Absent — permitted (released to forest). Not contradicted.
- **Void ABSTRACT (no entity / no void woman / no Masters):** Held. The rim is "the abstract cold," a
  "tear in the weave," "something... leaned in" — a pressure/absence with no figure, no name, no
  person. The final image ("something that was not attacking and did not need to be... leaned in toward
  the warmth she had become," 139) dramatizes the "pulled toward the source, not attacking" key
  revelation WITHOUT explaining it: Viridia only suspects the direction-toward-the-source (135) as
  unproven intuition, not the Ch.10 reveal stated outright. Good.
- **Drained-death hook:** Correct, well-matched to void rules — a core "drained," warmth "going
  somewhere... into a place that had no business taking it" (117), distinct from the clean dark of
  natural death. Consistent with the source/void differential.
- **No invented canon contradicting Books One/Two:** None beyond the Raizen-eye detail (WARN-001).

---

## SUGGESTED YAML PATCHES

```yaml
suggested_patches:
  - entity: "raizen.physical.human_eyes"
    action: "resolve_conflict"
    reason: "Bk2 ch.19 rendered his human eyes 'ordinary'; Bk3 ch.1 asserts retained 'lightning-blue
      of the prismatic dragon.' Author must pick: revert to ordinary, OR adopt retained-dragon-eye as
      deliberate new canon and log it. Note 'lightning-blue' is otherwise Lor-ar's marker."
```
