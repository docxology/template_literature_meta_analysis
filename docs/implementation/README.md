# Source Modules

Source code for the literature meta-analysis exemplar.

| Package | Purpose |
| --- | --- |
| `literature/` | Retrieval clients, canonical `Paper` records, corpus persistence, de-duplication, full-text assessment |
| `analysis/` | Descriptive stats, text processing, embeddings, topic modeling, temporal metrics, citation networks |
| `knowledge_graph/` | Optional assertion extraction, hypothesis scoring, nanopublications, RDF/TriG export |
| `visualization/` | Headless matplotlib figures and shared style config |
| `manuscript/` | Token computation and manuscript hydration helpers |

Run the project coverage gate from the repository root:

```bash
uv run pytest tests/   --cov=src --cov-fail-under=90
```

## Module guides

- [Analysis](analysis.md)
- [Deep research fixtures](deep_research-fixtures.md)
- [Deep research](deep_research.md)
- [Knowledge graph](knowledge_graph.md)
- [Literature](literature.md)
- [Manuscript variables extractors](manuscript-variables-extractors.md)
- [Manuscript variables](manuscript-variables.md)
- [Manuscript](manuscript.md)
- [Reproducibility](reproducibility.md)
- [Visualization advanced](visualization-advanced.md)
- [Visualization](visualization.md)
