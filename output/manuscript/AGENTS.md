# AGENTS.md — `template_literature_meta_analysis/output/manuscript`

> Generated 2026-08-29 during the ongoing-docs fleet pass. Description derived
> from the on-disk listing; semantics marked (unverified) where not confirmed
> by running code.

## Role

Rendered/hydrated manuscript markdown produced by the render stage.

## Layout

- Files: `00_abstract.md`, `01_introduction.md`, `02_methods_overview.md`, `02a_methods_retrieval.md`, `02b_methods_extraction.md`, `02c_methods_bibliometrics.md`, `02d_methods_knowledge_graph.md`, `02e_methods_viz_injection.md`, `03_results_hypothesis.md`, `03a_results_field_overview.md`, `03b_results_subfields.md`, `03c_results_text_analytics.md`, `03d_results_citation_network.md`, `03e_results_reproducibility.md`, `04_discussion.md`, `05_conclusion.md`, `06_appendix_tooling.md`, `07_appendix_technical.md`, `08_appendix_accessibility.md`, `98_symbols_glossary.md`, `99_references.md`, `config.yaml`, `config.yaml.example`, `layer_contract.yaml`, `preamble.md`, `references.bib`

## Invariants

- Local-only path under `projects/ongoing/` (root `.gitignore` rule
  `projects/*`) — never commit. Repo-wide policy: see
  `/Volumes/external_drive/Git/template/projects/ongoing/AGENTS.md`.
- Generated outputs in these trees are regenerable via the repo's canonical
  pipeline; do not hand-edit artifacts to "fix" results.
- This repo lives in the public docxology mirror — anything written here
  becomes public once pushed to the repo's GitHub remote.

## Gotchas

- No silent omissions: if a child folder above is undocumented, that is a
  known gap of this auto-generated doc — replace it with a verified
  description when you work here.
