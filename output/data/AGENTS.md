# AGENTS.md — `template_literature_meta_analysis/output/data`

> Generated 2026-08-29 during the ongoing-docs fleet pass. Description derived
> from the on-disk listing; semantics marked (unverified) where not confirmed
> by running code.

## Role

Generated analysis data (CSV/NPZ/JSON) emitted by project analysis stages.

## Layout

- Files: `assertion_summary.json`, `bibliography.bib`, `citation_graph.gml`, `citation_network.json`, `corpus.jsonl`, `deep_research_replay.json`, `descriptive_stats.json`, `embedding_analysis.json`, `entities.json`, `fulltext_assessment.json`, `hypothesis_scores.json`, `hypothesis_trends.json`, `keyphrases.json`, `literature_evaluation.json`, `nanopublications.jsonl`, `nanopublications.trig`, `reproducibility_scores.json`, `reproducibility_summary.json`, `retrieval_report.json`, `subfield_classification.json`, `subfield_timeline.json`, `temporal_analysis.json`, `tfidf_data.json`, `topics.json`, `workflow_graphs.jsonl`

## Invariants

- Repository-wide policy for template projects is maintained in the template repository, not restated here.
- Generated outputs in these trees are regenerable via the repo's canonical
  pipeline; do not hand-edit artifacts to "fix" results.
- This repo lives in the public docxology mirror — anything written here
  becomes public once pushed to the repo's GitHub remote.

## Gotchas

- No silent omissions: if a child folder above is undocumented, that is a
  known gap of this auto-generated doc — replace it with a verified
  description when you work here.
