# Phaedo Translation Batches

Ranges below use the numbered `unit="section"` milestones in the local Perseus/Burnet XML. They are contiguous, nonoverlapping, and cover 57a–118a (303 source section milestones). A few milestones omit the TEI `resp="Stephanus"` attribute; they still count as section boundaries and are included. Batch boundaries follow the dialogue's major turns and arguments; section size varies, so this is a practical division rather than equal word counts.

For current progress, use `project-status.md`. All ten batch files are present and coordinator fidelity reviewed.

| Batch | Stephanus range (inclusive) | Main content | Output file |
|---|---|---|---|
| 01 | 57a–63e | Opening; Socrates on philosophy and death; discussion of suicide, hope, and misology | `translations/batch-01-57a-63e.md` |
| 02 | 64a–69e | Definition of philosophical death; purification; objections and replies about the afterlife | `translations/batch-02-64a-69e.md` |
| 03 | 70a–72e | First argument for the soul's survival: opposites and cyclical generation | `translations/batch-03-70a-72e.md` |
| 04 | 73a–77e | Recollection argument; Forms and the soul's prior existence; transition to the affinity argument | `translations/batch-04-73a-77e.md` |
| 05 | 78a–84e | Affinity argument; soul and body; Simmias' objection and the opening response | `translations/batch-05-78a-84e.md` |
| 06 | 85a–91e | Simmias and Cebes' objections; Socrates' response and warning against misology | `translations/batch-06-85a-91e.md` |
| 07 | 92a–99e | Replies to Simmias and Cebes; Socrates' intellectual autobiography and turn to causes | `translations/batch-07-92a-99e.md` |
| 08 | 100a–107e | Final argument from Forms and the soul's essential life; conclusion of the immortality proof | `translations/batch-08-100a-107e.md` |
| 09 | 108a–115e | Eschatological myth: earth, the afterlife, judgment, and the fates of souls | `translations/batch-09-108a-115e.md` |
| 10 | 116a–118a | Final instructions, hemlock, death of Socrates, and closing words | `translations/batch-10-116a-118a.md` |

## Parallel-agent handoff

Give every agent the same source XML, this batch map, and the project scope/style decisions. Ask them to:

1. Translate directly from the Greek, without using an existing English translation as a drafting source.
2. Preserve the assigned Stephanus labels as headings, in source order, and include every label in the assigned range exactly once (even if a section is very short).
3. Save only their assigned output file. Do not edit the source XML, this map, glossary, decision log, or another batch file.
4. Keep paragraph/dialogue structure and speaker turns clear. Do not compress arguments or omit repetitions that carry argumentative force.
5. Mark uncertain readings inline as `[QUERY 64a: ...]` and list each query with alternatives and a brief reason at the end of the batch.
6. Add a brief batch-end note listing proposed glossary entries or departures from existing choices; do not silently impose a new global convention.

## Coordinator checks after drafting

- Mechanically compare each file's Stephanus headings with the expected labels from the source; require exact coverage, no duplicates, and no labels outside that batch.
- Check file boundaries for off-by-one gaps/overlaps (for example, batch 1 ends at 63e and batch 2 starts at 64a).
- Record word counts per Stephanus section and flag empty or extreme source-to-English ratios for review.
- Reconcile queries and terminology across batches before a continuous read-through.

Agent outputs are independent drafts, not final text. A coordinator must review transitions at every seam and perform a full consistency and fidelity pass against the Greek.
