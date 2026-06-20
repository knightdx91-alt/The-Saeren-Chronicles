# Voice DNA / Style Calibration — The Saeren Chronicles, Book One

*Read-only. Leads with the objective gate, then qualitative anti-AI scan, then voice-match to the locked Ch.1 benchmark and voice-dna.md.*

---

## 1. OBJECTIVE GATE — `python3 tools/style_check.py`

**Per-chapter metrics (all WITHIN their ceilings):**

| Ch | Words | Simile/1k (≤4.0) | Adverb/1k (<20) | Em-dash count | CEILING flag | FINGERPRINT flag |
|----|-------|------------------|------------------|---------------|--------------|------------------|
| 1  | 4960 | 3.6 | 14.9 | 2 | none | none |
| 2  | 4565 | 3.1 | 12.0 | 0 | none | none |
| 3  | 4469 | 3.8 | 11.4 | 0 | none | none |
| 4  | 4528 | 3.8 | 12.6 | 0 | none | none |
| 5  | 4652 | 3.9 | 11.2 | 1 | none | none |
| 6  | 4360 | 2.3 | 12.2 | 0 | none | none |
| 7  | 4717 | 2.5 | 12.5 | 0 | none | none |
| 8  | 4886 | 3.1 | 8.4 | 1 | none | none |
| 9  | 4752 | 1.7 | 11.4 | 0 | none | none |
| 10 | 4682 | 1.1 | 14.1 | 0 | none | none |
| 11 | 4629 | 2.8 | 12.1 | 0 | none | none |
| 12 | 5177 | 1.5 | 8.9 | 0 | none | none |
| 13 | 4806 | 2.1 | 9.6 | 0 | none | none |
| 14 | 5292 | 3.2 | 11.3 | 1 | none | none |
| 15 | 4985 | 1.0 | 7.0 | 4 | none | none |
| 16 | 5135 | 1.2 | 9.5 | 4 | none | none |
| 17 | 4834 | 1.9 | 9.3 | 3 | none | none |
| 18 | 4606 | 1.5 | 12.6 | 1 | none | none |

**Per-chapter verdict: CLEAN.** No simile breaches (max 3.9, Ch.5), no adverb breaches (max 14.9, Ch.1 — well under the 20 ceiling), em-dashes negligible (max 4/chapter, ~0.8/1k — far under the ~10/1k guidance). No CEILING or FINGERPRINT flags on any chapter.

**Cross-chapter repeated-phrase check: NOT CLEAN. `RESULT: 1315 issue(s) flagged.` Exit code 1 (non-zero).**

> ⚠️ **Discrepancy with STATE.yaml.** STATE.yaml records the latest passes as `result: clean` and `per_chapter_ceilings: all clean`. The **per-chapter** gate is indeed clean — but the **cross-chapter n-gram gate is not**, and the script exits non-zero, which by its own docstring means "Exit code is non-zero if any chapter breaches a ceiling **or any cross-chapter** [phrase repeats]." STATE.yaml's "clean" claim is therefore accurate for the per-chapter layer and **overstated for the cross-chapter layer.** This should be reconciled.

**Reading the 1315.** The count is inflated by overlapping fragments of the same sentence (e.g., "did not know what to say to that so she said" generates 5+ separate 4–6-grams) and by **stopword-heavy strings the content filter lets through** ("she could not find," "did not look back," "middle of the night," "rise and fall of"). These are *noise*, not voice failures. After discounting those, the **genuine voice-tic repetitions** worth a human's attention are:

**Real recurring tics (NOT allowlisted, NOT noise) — candidates to vary:**
- **"X did not know what to say to that, so she said [the true thing]"** — Ch.1 & Ch.3 share this nearly verbatim. A signature *move*, but verbatim twice is a tell.
- **"did not sleep for a long time" / "not sleep for a long time"** — Ch.12, 14, 17 (three chapter-endings). A chapter-ending cadence repeated thrice.
- **"she had not meant to say it"** — Ch.3, 9, 12.
- **"a thing she had no name for and would later"** — Ch.4, 5 (the "no name for" construction also recurs Ch.8, 16).
- **"two lives that had briefly been one"** — Ch.6, 10 (the Alice-drift motif, near-verbatim).
- **"clapped both hands over her mouth"** — Ch.6, 10 (Alice's gesture; risks becoming a verbal tic rather than a character beat).
- **"the look of a person who has…"** — Ch.6, 10, and the construction recurs widely.
- **"reaching for something a light mage [has no business]"** — Ch.5, 6 (deliberate echo of Amber→Viridia, arguably intentional; borderline).

**Correctly allowlisted (do NOT touch — these are deliberate refrains):** "no one sees you do it / you decide who sees," "be careful who you let see you do it," "since the morning the world ended," "the detail that did not fit," "one tooth turned a little out of line," "more life than anyone had ever told her," "empty space the size of Alice," "scorched bread and her mother's tea," "a held note finally let go," "anything that keeps you alive is worth doing." The allowlist is well-curated and these recurrences are working motifs, not errors.

**ALSO flagged but is a process artifact (should be fixed):** the n-gram check is catching the **HTML comment headers** at the top of chapter files — *"word count target floor per state anchor"* appears as a ×2 cross-chapter phrase (Ch.4 & Ch.6). The `<!-- Word count… -->` editorial comments are being scanned as prose. Either strip comments before scanning or the assembled `full-manuscript.md` (which strips headers) should be the gate's input. This is why the assembled-manuscript count and the chapter-file count diverge in STATE.yaml.

---

## 2. ANTI-AI PATTERN SCAN (qualitative)

Overall: **LOW machine-tell density.** This prose does not read as generic LLM output — the restraint, the domestic sensory grounding, and the "one wrong detail" habit are a genuine, specific voice. The tells that *are* present are concentrated and consistent (which is itself slightly machine-like — a human writer's tics vary more).

**Per-tell findings:**

- **"not just X but Y" / "it wasn't X, it was Y":** RARE — the book mostly resists this. A few survive: Ch.1 *"Not glanced at. Seen."*; Ch.7 *"Not a flaw you were born with. A wound that was done to you."*; Ch.16 *"It was not personal survival… but moral residue."* These read as *deliberate antithesis* rather than padding, and the book earns them. Light.

- **Rule-of-three / balanced-clause sing-song:** **MEDIUM, and the most pervasive tell.** The book loves the triad-with-rising-clause. Examples: Ch.18 *"toward the trees, toward the war, toward the not-knowing and the work and whatever came next"*; Ch.17 *"the man in the doorway and the captain unmade inside his own shield and the bodies she had refused to look at and the choice in the alcove and the empty space the size of Alice"*; Ch.14 *"the cave and the pool and the pact and the cut in the world."* These polysyndeton-list cadences appear in nearly every chapter's emotional climax. They're beautiful individually; *as a fixed rhythm for every big moment* they become predictable. **This is the #1 calibration target.**

- **Summary-then-restate / over-tidy bows:** MEDIUM, concentrated in chapter endings. Many chapters close by *naming the lesson*: Ch.6 *"You carried the loss and the becoming in the same two hands"*; Ch.10 *"this was the high point"*; Ch.15 *"She was not as ready as she thought. No one ever is."*; Ch.18's whole "Less:/More:" accounting. The voice-dna explicitly prescribes restraint ("tells LESS than the moment demands"), and the chapter *bodies* honor it — but the chapter *endings* often violate it by spelling out the takeaway. **The book is most "AI-tidy" in its last paragraphs.**

- **Abstraction where sensory detail belongs:** LOW in early chapters (scorched bread, soap and machine oil, the pot still on, pink wool socks — excellent concrete texture). RISES in the back third: Ch.14's source sequence and Ch.18's accounting trade the domestic concreteness for abstraction ("the size of the world," "the cut in the world," "loss married to purpose"). The big metaphysical chapters lose the book's signature *thingness*.

- **Sentence-rhythm monotony:** LOW-MEDIUM. The voice-dna's prescribed contrast (long deep-water sentences for grief; short flat declaratives under pressure) is *executed well* and is the book's rhythmic strength — Ch.16's short combat declaratives ("Keep moving. Watch the bodies that are standing.") are a clean payoff of the spec. The monotony risk is the *medium-long reflective sentence* that dominates the calm chapters (7, 10, 15): paragraph after paragraph of similarly-shaped subordinate-clause sentences.

- **"the kind of … that" / "as if" / "something like":** LOW. "the kind of" is on the FINGERPRINT list and was actively reduced (STATE notes the Ch.9 fix). Spot-check confirms it's well-controlled.

**Per-chapter machine-tell weight:** Ch.1–5 *light*. Ch.6, 10, 15 *medium* (reflective, ending-tidy). Ch.7, 14, 18 *medium-heavy* (abstraction + thesis statements + triad cadences clustered). Ch.8, 11, 13, 16 *light* (scene-driven keeps it concrete).

---

## 3. VOICE MATCH TO SPEC / Ch.1 BENCHMARK

**Match: STRONG and improving in discipline; drifting slightly in *register* in the back third.**

- **The signature move** (read a person/room through the one detail that doesn't fit) is honored throughout and is the book's truest fingerprint: blue shoes (Ch.1, recurring), chipped nails (Ch.1), the tooth out of line (Ch.1), Venquar's eye-flick tell (Ch.11), Mrs. Zoran not looking back (Ch.12), the captain's "soldier's discipline under a laborer's coat" (Ch.16), the council members' tells (Ch.18). Excellent continuity.
- **Grief as ambient, restraint as engine:** honored in the bodies of chapters; *under-honored in the endings* (see §2 over-tidy bows). Ch.1's benchmark restraint ("She thought about it for the rest of her life.") is the gold standard; later chapters more often *explain* the feeling than land it sideways.
- **Domestic/concrete sensory texture (30–40% of detail):** strongest Ch.1–8, thinner Ch.14/18.
- **Voice-under-pressure (sentences shorten and flatten; the mantra surfaces):** *excellently* executed — Ch.16 is a textbook payoff of the spec.

**DRIFT from benchmark — the back-third "register creep."** Ch.14 and Ch.18 (and to a degree Ch.7) drift *more ornate and more abstract* than the Ch.1 benchmark: cosmic scale, capital-T Truths, the narrator philosophizing. The voice-dna says "British-inflected, slightly formal but never cold" — the back-third chapters edge toward *sermon*. This isn't wrong for an essayistic finale, but it's a measurable drift from the close-third domestic intimacy of the benchmark.

---

## 4. COVER-THE-NAME DIALOGUE TEST

Sampled multi-character scenes (Ch.4 office, Ch.9 office, Ch.15 breakfast, Ch.18 council). **Result: PASS for the principals, MIXED for the ensemble.**

- **Distinct without tags:** Viridia (spare; single-word "Yes."; precise true thing as a gift), Alice (warm, runs on, self-deprecating, waves the sentence away), Amber (lounging, ticks points, deflects with a joke), Lor-ar (ancient, dry, "little one"), Mrs. Zoran ("Knowledge is power"; enthusiastic), Quina ("do be" constructions — instantly identifiable), Drake (gruff, "Doesn't look like much"). These are genuinely differentiated; you can name the speaker with tags hidden.
- **UNDIFFERENTIATED:** the **Ch.18 council** (Coram, Brutus, woman-in-blue, silver-bun woman). With tags hidden, Coram/Brutus/the women speak in an interchangeable "wise-tired-resistance-elder" register; they are *described* distinctly (the locket, the sunburn, the cold arithmetic — the signature-detail move doing the work) but they *sound* the same. Also **Raizen and Lor-ar** occasionally blur (the text even lampshades it: "I have his sense and your memories" — a smart cover, but the voices do converge in their dry-wise mode). **Jazen** is adequately distinct (lets his grief show, blunt) but close to "earnest male leader" stock.

---

## VOICE RISK RATING (per chapter) & TOP CALIBRATION FIXES

**Voice risk (likelihood a reader senses "machine" or "drift"):**
LOW: 1, 2, 3, 4, 5, 8, 11, 13, 16. MEDIUM: 6, 9, 10, 12, 15, 17. MEDIUM-HEAVY: 7, 14, 18.

**Top calibration fixes:**
1. **Break the triad/polysyndeton cadence at emotional climaxes (§2).** It's the most pervasive tell. Vary the rhythm of the "big moment" sentence — sometimes a fragment, sometimes a single hard declarative — instead of the rising 3–5-item list every time.
2. **Stop naming the lesson in chapter endings (§2, §3).** The bodies honor "tell less"; the last paragraphs don't. Cut the explicit takeaway from the endings of Ch.6, 10, 15, 18 and trust the scene. This is also the analytical review's Ch.18 finding.
3. **Restore domestic concreteness to Ch.14 and Ch.18 (§2).** The abstraction in the metaphysical/finale chapters is where the book least sounds like itself. Anchor at least the emotional beats in *things*.
4. **Differentiate the Ch.18 council voices (§4)** — give Coram/Brutus/the two women one verbal habit each, not just one visual detail each.
5. **Vary the handful of verbatim signature-move repetitions (§1)** — "did not know what to say… so she said," "did not sleep for a long time," "clapped both hands over her mouth." These are real (non-allowlisted) tics; rephrase the second/third occurrences.
6. **Process: reconcile the gate.** Strip the `<!-- -->` editorial comments before scanning (or scan the assembled manuscript), and update STATE.yaml so "clean" reflects reality: per-chapter clean, cross-chapter n-gram gate flags (mostly noise + the real tics above).
