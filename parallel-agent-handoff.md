# Phaedo Translation: Parallel Agent Handoff

Use this file to restart the project in a new session and fan out the unfinished work.

> **Archived handoff:** The assignments below were completed and coordinator-reviewed on 2026-11-02. For the current inventory and review status, see `project-status.md`. The original prompts and wave plan are retained as a record of the parallel work.

## Baseline

- Start from the current `master` HEAD. The reviewed batches and project setup are in commit `645c30a` (`Add reviewed Phaedo translation batches 1-3`); the handoff and status files may be in a later commit.
- No Git remote was configured when this handoff was prepared. If that is still true after review, ask the user for the remote URL before attempting to push.
- Source: `phaedo-burnet-perseus-grc2.xml`; keep it immutable. Its expected SHA-256 is `baf65d8cb72f857e80ea4e2326a6808c1cf3cbc8df7b4340f14e79d142227d98`.
- Read `phaedo-translation-scope.md`, `translation-batches.md`, `style-sample-57a-60c.md`, `glossary.md`, and `translation-decisions.md` before assigning work.
- Batches 1 and 2 are fidelity reviewed. Batch 3 is drafted and its section boundaries were aligned to the Greek, but it still needs a full fidelity review.
- Batches 4–10 have no drafts yet.

## Parallel assignments

Run these as separate agent tasks. Each translation agent owns only its assigned output file. The batch 3 reviewer may edit only the batch 3 file and should report substantive changes.

| Task | Assignment | Range | File to create or review |
|---|---|---|---|
| Reviewer | Fidelity-review existing batch 3 against Greek; fix omissions, meaning shifts, labels, speakers, and queries | 70a–72e | `translations/batch-03-70a-72e.md` |
| Translator 4 | Recollection argument; Forms and prior existence of the soul; transition to affinity argument | 73a–77e | `translations/batch-04-73a-77e.md` |
| Translator 5 | Affinity argument; soul and body; Simmias’ objection and opening response | 78a–84e | `translations/batch-05-78a-84e.md` |
| Translator 6 | Simmias and Cebes’ objections; Socrates’ response and warning against misology | 85a–91e | `translations/batch-06-85a-91e.md` |
| Translator 7 | Replies to Simmias and Cebes; intellectual autobiography and turn to causes | 92a–99e | `translations/batch-07-92a-99e.md` |
| Translator 8 | Final argument from Forms and the soul’s essential life; immortality proof | 100a–107e | `translations/batch-08-100a-107e.md` |
| Translator 9 | Eschatological myth: earth, afterlife, judgment, and the fates of souls | 108a–115e | `translations/batch-09-108a-115e.md` |
| Translator 10 | Final instructions, hemlock, death of Socrates, and closing words | 116a–118a | `translations/batch-10-116a-118a.md` |

The output files do not overlap. With the usual three available subagent slots, run these waves:

1. Batch 3 reviewer, translator 4, translator 5
2. Translators 6, 7, 8
3. Translators 9 and 10

The coordinator can review completed outputs as each wave returns, but keep the whole-project seam review until all neighboring batches are present.

## Paste-ready coordinator prompt

```text
Coordinate the Plato, Phaedo translation project from the current checkout. Read parallel-agent-handoff.md, phaedo-translation-scope.md, translation-batches.md, style-sample-57a-60c.md, glossary.md, and translation-decisions.md first.

Use parallel agents for the eight assignments in the handoff table: one fidelity reviewer for batch 3 and one translator each for batches 4–10. Run up to three agents at once, following the listed waves. Give each agent the same source XML, project scope, batch map, style sample, glossary, and decision log. Keep each agent confined to its named output file. Do not ask agents to commit or push.

After all agents finish, review every returned file yourself. Check exact Stephanus heading coverage and order against the XML, verify the English passage at each heading boundary, inspect speaker turns and paragraph structure, reconcile queries and glossary proposals, and review every batch seam. Treat agent drafts as unchecked until this review is complete. Update glossary.md, translation-decisions.md, and project-status.md as coordinator-owned files. Preserve the source XML and its expected SHA-256. Do not use an existing English translation as a drafting source.

Do not claim semantic accuracy from heading checks alone. Report remaining interpretive questions explicitly. After all drafts pass coordinator review, commit the completed project deliverables. Push if a Git remote is configured; if none is configured, report that clearly and ask me for the remote.
```

## Per-agent translation prompt

Copy this prompt once per translator and fill in the bracketed fields from the assignment table.

```text
Translate Plato’s Phaedo directly from the Greek TEI source in phaedo-burnet-perseus-grc2.xml. Your assigned range is [START–END], and your only output file is [OUTPUT FILE]. Read phaedo-translation-scope.md, translation-batches.md, style-sample-57a-60c.md, glossary.md, and translation-decisions.md before drafting.

Requirements:
- Translate the Greek directly. Do not use an existing English translation as a drafting source.
- Include every Stephanus section label in your range exactly once, in source order, as a `### 57a`-style heading. Check the Greek milestone positions, not just the heading list; place translated clauses under the correct headings and show sentence continuations across boundaries with a brief continuation label or em dash.
- Preserve dialogue turns, paragraph structure, repetitions that carry argumentative force, and the steps of each argument. Do not summarize or silently resolve meaningful ambiguity.
- Follow current glossary choices where they fit. For a context-specific alternative, keep the English natural and note the choice. Do not edit the shared glossary or decision log.
- Follow the source’s constituted reading. Do not translate text marked `<del>` as main text; briefly note consequential deletions, additions, or variants where needed.
- Mark each unresolved interpretive issue inline as `[QUERY 74a: concise issue]`, then list it at the end with plausible alternatives and a brief reason. Do not leave an unexplained query marker.
- End with concise `## Queries` and `## Terminology and style notes` sections. State “None” if there are no queries or proposals.
- Save only your assigned output file. Do not edit another batch, shared project file, source XML, or Git history. Do not commit or push.

Before returning, compare your headings and each translated section boundary to the assigned Greek range, check for omissions and duplicates, and confirm the file ends at the assigned boundary.
```

Replace the example query reference `74a` with the actual Stephanus location when using the prompt.

## Batch 3 reviewer prompt

```text
Fidelity-review translations/batch-03-70a-72e.md line by line against the corresponding Greek in phaedo-burnet-perseus-grc2.xml. The current section placement was repaired, but the translation is not yet fidelity checked. You may edit only this file. Verify every translated clause against the source, including the boundaries at 71d, 71e, and 72a–72e; check speakers, omissions, negation, connectives, and the final recollection sentence. Preserve the section labels in exact order. Record genuine interpretive issues as inline [QUERY 70a: ...] markers and list them under `## Queries`. Follow the style sample, glossary, and decision log. Do not consult an existing English translation as a drafting source, do not edit shared files, and do not commit or push. Return a short note with the changed passages and any unresolved questions.
```

## Coordinator completion checklist

- Verify each batch heading list exactly matches the XML sequence for its range; also spot-check that the English clauses are aligned to the milestones.
- Confirm contiguous coverage from 57a through 118a with no missing, duplicate, or out-of-range section labels.
- Review the seams 72e/73a, 77e/78a, 84e/85a, 91e/92a, 99e/100a, 107e/108a, and 115e/116a, plus any internal seams affected by a boundary-spanning sentence.
- Consolidate agent terminology proposals and queries in the shared logs, then mark status by draft, fidelity reviewed, or checked; do not equate mechanical coverage with translation accuracy.
- Do the whole-work fidelity and fluency pass after batch review, and recompute the source hash before finalization.
