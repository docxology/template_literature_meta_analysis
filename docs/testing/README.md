# Tests - Literature Meta-Analysis

Run from the project root:

```bash
uv run --no-sync pytest tests/ --cov=src --cov-fail-under=90 -q
```

The suite uses real fixtures, real files, and `pytest-httpserver`; do not add mocks. See the [test map](../../tests/AGENTS.md) and [test patterns](../test-patterns.md).

## Module guides

- [Analysis](analysis.md)
- [Knowledge graph](knowledge_graph.md)
- [Literature](literature.md)
- [Reproducibility](reproducibility.md)
- [Visualization](visualization.md)
