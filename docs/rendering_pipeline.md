# Rendering and Validation

Run the fixture build in a disposable checkout. The project tracks a publication
snapshot under `output/`. The commands below move that snapshot aside within the
disposable checkout before deriving new artifacts from the synthetic fixture.

## Set up the renderer and project

Install uv, Pandoc 3.14, its compatible pandoc-crossref 0.3.26 filter, and a TeX
installation with XeLaTeX and BibTeX. Run the following commands from a directory
where you can create a separate renderer checkout.

```bash
git clone https://github.com/docxology/template.git
cd template
git checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
uv sync --locked --python 3.14
export TEMPLATE_REPO_ROOT="$PWD"
mkdir -p projects/working
git clone https://github.com/docxology/template_literature_meta_analysis.git \
  projects/working/template_literature_meta_analysis
cd projects/working/template_literature_meta_analysis
uv sync --locked --extra dev --python 3.14
```

## Run the offline fixture workflow

The bundled JSONL has 80 synthetic records. The configured analysis filters and
deduplicates the corpus before computing metrics. Here, script 03 processes zero
papers for assertion extraction, and script 08 uses the checked-in replay fixtures.
The render demonstrates the software workflow on synthetic data.

```bash
mv output ../template_literature_meta_analysis-published-output
mkdir -p output/data
cp data/fixtures/modafinil_corpus.jsonl output/data/corpus.jsonl
uv run --no-sync python scripts/02_meta_analysis_pipeline.py
uv run --no-sync python scripts/03_build_knowledge_graph.py --max-papers 0
uv run --no-sync python scripts/04_generate_figures.py --dpi 300
uv run --no-sync python scripts/06_fulltext_assessment.py
uv run --no-sync python scripts/07_literature_evaluation.py
uv run --no-sync python scripts/08_deep_research_dispatch.py
uv run --no-sync python scripts/09_export_bibliography.py
uv run --no-sync python scripts/05_inject_variables.py
```

Script 05 reads the maintained [manuscript](manuscript/README.md), fills its
`{{TOKEN}}` values from analysis artifacts, and writes a separate copy to the
project's `output/manuscript/`. Figures and analysis artifacts stay under the
project's `output/figures/` and `output/data/`.

## Render and validate

Run the shared renderer from its own checkout and environment. The qualified
project name selects the checkout under `projects/working/`.

```bash
cd "$TEMPLATE_REPO_ROOT"
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/template_literature_meta_analysis
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/template_literature_meta_analysis
```

The shared pipeline writes PDFs, web output, slide decks, and validation reports
under the project checkout's `output/pdf/`, `output/web/`, `output/slides/`,
and `output/reports/`. See the
[output inventory](output_inventory.md) and [troubleshooting guide](troubleshooting.md).
