# AGENTS.md — `template_literature_meta_analysis/output/figures`

> Generated 2026-08-29 during the ongoing-docs fleet pass. Description derived
> from the on-disk listing; semantics marked (unverified) where not confirmed
> by running code.

## Role

Generated figure files (PNG/SVG) referenced by the manuscript render.

## Layout

- Files: `assertion_breakdown.png`, `assertion_summary.png`, `author_productivity.png`, `citation_distribution.png`, `citation_network.png`, `cooccurrence_matrix.png`, `degree_distribution.png`, `dendrogram.png`, `entity_bar_chart.png`, `evidence_timeline.png`, `field_summary.png`, `figure_registry.json`, `growth_curve.png`, `hypothesis_dashboard.png`, `pca_embeddings.png`, `similarity_heatmap.png`, `subfield_distribution.png`, `subfield_timeline.png`, `term_heatmap.png`, `top_venues.png`, `topic_term_bars.png`, `word_cloud.png`

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
