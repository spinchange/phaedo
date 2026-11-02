# Phaedo Translation: Project Status

Updated 2026-11-02 from the repository and worktree state.

## Current state

- Source text and project scope are in the main checkout. The source XML is the fixed baseline; do not edit it.
- Shared style is drafted in `style-sample-57a-60c.md`. It is currently untracked in the main checkout.
- Three translation drafts have been copied into `translations/` in the main checkout. The original worktree copies remain in place; batch 3's worktree copy is the unrevised draft, so the main-checkout copy is authoritative.
- A working glossary and decision log are in the main checkout.
- No translation files for batches 4–10 were found.
- All section headings in batches 1–3 now match their expected source sequences exactly. Content and fidelity review remains pending.

## Draft inventory

| Batch | Range | File | Worktree | State |
|---|---|---|---|---|
| 01 | 57a–63e | `translations/batch-01-57a-63e.md` | `.worktrees/batch-01` | Fidelity reviewed; 32/32 headings; 62a tension documented |
| 02 | 64a–69e | `translations/batch-02-64a-69e.md` | `.worktrees/batch-02` | Fidelity reviewed; 30/30 headings |
| 03 | 70a–72e | `translations/batch-03-70a-72e.md` | `.worktrees/batch03` | Draft present; 15/15 headings; 70a–72e section placement aligned to source milestones; fidelity review pending |
| 04–10 | 73a–118a | As listed in `translation-batches.md` | — | No draft files found |

## Recommended next steps

1. Fidelity-review batch 3, including the repaired section boundaries.
2. Assign batches 4–10 using the existing map and handoff instructions. Keep each agent to one output file.
3. After drafting, reconcile queries and terminology, review every batch seam, and read the full translation against the Greek.

## Handoff guardrails

- Keep `phaedo-burnet-perseus-grc2.xml` unchanged.
- Agents should work only on their assigned batch file and return queries and proposed terminology at the end of that file.
- Treat all current batch files as independent drafts until their fidelity review is complete; heading coverage and seam review do not mean the translation is checked.
- Main branch was clean before this status file except for the untracked `.worktrees/` directory and style sample.
- Heading audit on 2026-11-02: batches 1, 2, and 3 contain all 32, 30, and 15 expected headings respectively, with no duplicates or out-of-order labels. Batch 3 headings were also repositioned within the dialogue to follow the Greek milestone boundaries, including continuations split across sections.
- Fidelity review on 2026-11-02: batches 1–2 checked against the Greek. Corrected the 59b speaker label (Echecrates), tightened the 67b purity line, and resolved the 62a wording editorially by preserving its apparent “never” / “at some time for someone” tension with an explanatory note.
- Source integrity rechecked on 2026-11-02: SHA-256 remains `baf65d8cb72f857e80ea4e2326a6808c1cf3cbc8df7b4340f14e79d142227d98`.
- Seam review: batch 1 closes at 63e with Socrates telling Crito “Let him be”; batch 2 begins at 64a with Socrates’ defense, continuing the same scene. Batch 2 closes at 69e with Socrates’ hope about meeting good companions; batch 3 opens at 70a with Cebes raising the survival objection. Both transitions are coherent.
- Terminology review recorded in `glossary.md` and `translation-decisions.md`. Contextual choices include *pharmakon* (“poison” in reports, “drug” in instructions), *logos* (context-dependent), and *phronēsis* (“wisdom” / “understanding” by context).
