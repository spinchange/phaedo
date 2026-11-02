# Plato, *Phaedo*: Translation Project Scope

## Source text

- **Work:** Plato, *Phaedo* (Φαίδων)
- **Base edition:** John Burnet, ed., *Platonis Opera*, vol. 1, Oxford Classical Texts (1900–1907; *Phaedo* at pp. 57–118).
- **Digital source:** Perseus Digital Library CTS text, `urn:cts:greekLit:tlg0059.tlg004.perseus-grc2`.
- **Retrieved:** 2026-11-02 from the PerseusDL canonical Greek literature repository at `https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/master/data/tlg0059/tlg004/tlg0059.tlg004.perseus-grc2.xml`.
- **Local source file:** `phaedo-burnet-perseus-grc2.xml` (keep immutable; make any normalized working copy separately).
- **SHA-256:** `baf65d8cb72f857e80ea4e2326a6808c1cf3cbc8df7b4340f14e79d142227d98`.
- Source integrity check: valid UTF-8; 105,106 Greek-script characters; zero Unicode replacement characters. XML parses as TEI.

## Aim and editorial approach

Produce a new, readable modern-English translation directly from the Greek. Preserve the structure of the dialogue and the steps of each argument. Do not silently resolve meaningful ambiguity: record alternatives and rationale, and mark unresolved choices for review. Cite locations using Stephanus references (for example, 57a).

## Work plan

1. **Ingest and index:** retain the XML as the fixed baseline; extract all ordered Stephanus section milestones and paragraph/sentence identifiers into a coverage checklist.
2. **Set shared conventions:** settle voice, sentence length, treatment of dialogue, and initial terminology choices before parallel drafting. Use a short sample from 57a–60c if needed to establish these conventions.
3. **Draft in parallel batches:** use the contiguous ranges in `translation-batches.md`; each batch has a separate output file and named Stephanus boundaries. Keep Greek and English aligned by section and paragraph.
4. **Consistency review:** update the terminology ledger, check references and speaker turns, and revisit ambiguity decisions across the whole dialogue.
5. **Final review:** read against the Greek for argument fidelity, omissions, negations, connective logic, tone, and English fluency; close all unresolved flags or document them explicitly.

## Translation records

For each unit, record:

- Stephanus section/range and source paragraph or sentence identifier
- Greek source text (or stable reference to it)
- English draft and revision status: `not started`, `drafted`, `revised`, `checked`
- Translator notes for textual variants, syntactic ambiguity, or philosophical terms
- Optional confidence marker for consequential interpretive decisions

Maintain two companion logs:

- **Glossary:** Greek lemma/construction, default English rendering, context-specific alternatives, references, and rationale. Likely terms to track include ψυχή (*psychē*), εἶδος/ἰδέα (*eidos/idea*), οὐσία (*ousia*), φρόνησις (*phronēsis*), λόγος (*logos*), and αἰτία (*aitia*).
- **Decision log:** location, issue type, plausible readings, chosen rendering, rationale, and whether further review is needed.

## Deterministic quality checks

- Parse TEI and enumerate all Stephanus section milestones in source order.
- Require exactly one completed translation unit for every expected section; flag missing, duplicated, or out-of-order references.
- Require each source paragraph/sentence ID to map to an English unit, and vice versa.
- Report source and English word counts by section and batch; flag empty or extreme ratios for inspection (not as automatic errors).
- Search glossary terms and report occurrences/renderings to expose possible drift; review context exceptions manually.
- Lint for unresolved issue markers, missing translator notes on flagged passages, and broken references.
- Recompute the source hash before finalization to confirm the baseline has not changed.

These checks establish coverage and consistency; they cannot certify semantic accuracy. Meaning, syntax, philosophical interpretation, and style require close human review against the Greek.

## Scale estimate

This is a full-length dialogue and a multi-session translation project. The initial work map has ten nonoverlapping batches and calls for two whole-work review passes. Batch sizes may be adjusted after comparing actual text volume; Stephanus section counts alone do not guarantee equal workloads.
