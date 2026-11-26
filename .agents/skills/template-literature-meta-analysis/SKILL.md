---
name: template-literature-meta-analysis
description: "Literature meta-analysis exemplar — multi-engine retrieval, dedup, full-text, bibliometrics, embeddings, optional knowledge graph. Default term: modafinil."
version: 0.1.0
author: docxology
license: MIT
tags: [exemplar, literature, meta-analysis, bibliometrics]
---

# template-literature-meta-analysis

Project-scoped skill for this exemplar — the repository root of this standalone mirror
(monorepo path: ``). Load this when working inside the project.

## When to Use

- Working inside the `template_literature_meta_analysis` exemplar — running scripts, editing source,
  or regenerating outputs.
- Forking this exemplar as the starting scaffold for a new research project.
- Validating that the exemplar's contracts (thin-orchestrator, layer boundaries,
  no-mocks testing) still hold after changes.

## Quick Reference

From the project root, install the [locked project dependencies](../../../docs/quickstart.md)
and run the coverage gate.

```bash
uv run --no-sync pytest tests/ --cov=src --cov-fail-under=90
```

Use the [offline workflow](../../../docs/rendering_pipeline.md) for generation,
hydration, rendering, and validation.

## Pitfalls

- **Keep scripts thin.** Business logic belongs in `src/` or shared
  `infrastructure/`, not in `scripts/`.
- **No mocks.** All tests must use real data, real files, and real
  computation.
- **Use the locked project test command from the standalone project root.** A direct root
  `pytest` invocation does not provision this exemplar's scientific
  dependencies.
- **Outputs are disposable.** Never hand-edit `output/` — regenerate from
  source and config.
- **Run from the repo root.** Commands assume the standalone project root
  as working directory unless the child `AGENTS.md` states otherwise.

## Cross-refs

- Project contract: [`AGENTS.md`](../../../AGENTS.md)
- README: [`README.md`](../../../README.md)
- [Maintenance backlog](../../../docs/backlog.md)
