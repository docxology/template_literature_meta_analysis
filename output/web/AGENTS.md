# AGENTS.md — `template_literature_meta_analysis/output/web`

> Generated 2026-08-29 during the ongoing-docs fleet pass. Description derived
> from the on-disk listing; semantics marked (unverified) where not confirmed
> by running code.

## Role

HTML web rendering of the manuscript.

## Layout

- Files: `_combined_manuscript.md`, `favicon.ico`, `index.html`, `manuscript__00_abstract.html`, `manuscript__01_introduction.html`, `manuscript__02_methods_overview.html`, `manuscript__02a_methods_retrieval.html`, `manuscript__02b_methods_extraction.html`, `manuscript__02c_methods_bibliometrics.html`, `manuscript__02d_methods_knowledge_graph.html`, `manuscript__02e_methods_viz_injection.html`, `manuscript__03_results_hypothesis.html`, `manuscript__03a_results_field_overview.html`, `manuscript__03b_results_subfields.html`, `manuscript__03c_results_text_analytics.html`, `manuscript__03d_results_citation_network.html`, `manuscript__03e_results_reproducibility.html`, `manuscript__04_discussion.html`, `manuscript__05_conclusion.html`, `manuscript__06_appendix_tooling.html`, `manuscript__07_appendix_technical.html`, `manuscript__08_appendix_accessibility.html`, `manuscript__98_symbols_glossary.html`, `manuscript__99_references.html`

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
