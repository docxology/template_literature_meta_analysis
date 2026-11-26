# Quickstart

Install [uv](https://docs.astral.sh/uv/) and clone the project. The test suite
uses the pinned Template checkout for integration tests.

```bash
git clone https://github.com/docxology/template.git
git -C template checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
export TEMPLATE_REPO_ROOT="$PWD/template"
git clone https://github.com/docxology/template_literature_meta_analysis.git
cd template_literature_meta_analysis
uv sync --locked --extra dev --python 3.14
uv run --no-sync pytest tests/ --cov=src --cov-fail-under=90
```

Tests exercise real transformations on fixtures and use local HTTP servers for
client requests. See [testing](testing/README.md) for the available suites.
Scripts that register figures or inject publication variables also load shared
docxology/template infrastructure. Follow the [rendering guide](rendering_pipeline.md)
to install that renderer and run the analysis and manuscript together.

The [canonical configuration](manuscript/config.yaml) sets the review topic, search
engines, subfield taxonomy, hypotheses, and optional stages. The
[configuration example](manuscript/config.yaml.example) and [forking guide](forking_guide.md)
show how to retarget a review. The [bundled fixture](fixtures.md) is synthetic.
