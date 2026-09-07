# Scripts - Literature Meta-Analysis Pipeline

Project-specific stage wrappers. Each script delegates computation to `src/` and handles CLI arguments, paths, logging, and sequencing.

## Inventory

| Script | Purpose | Delegates to | Command |
|--------|---------|--------------|---------|
| `01_literature_search.py` | Multi-source literature retrieval | `literature.search_runner` | `uv run python projects/templates/template_literature_meta_analysis/scripts/01_literature_search.py` |
| `02_meta_analysis_pipeline.py` | Subfield/temporal/TF-IDF/topic/citation analysis | `analysis.pipeline_runner` | `uv run python projects/templates/template_literature_meta_analysis/scripts/02_meta_analysis_pipeline.py` |
| `03_build_knowledge_graph.py` | LLM assertion extraction + hypothesis scoring | `knowledge_graph.kg_runner` | `uv run python projects/templates/template_literature_meta_analysis/scripts/03_build_knowledge_graph.py` |
| `04_generate_figures.py` | Publication figure generation | `visualization.figure_runner` | `uv run python projects/templates/template_literature_meta_analysis/scripts/04_generate_figures.py` |
| `05_inject_variables.py` | Manuscript variable injection (run last) | `manuscript.variables` | `uv run python projects/templates/template_literature_meta_analysis/scripts/05_inject_variables.py` |
| `06_fulltext_assessment.py` | Full-text/OA availability report | `literature.fulltext_assessment` | `uv run python projects/templates/template_literature_meta_analysis/scripts/06_fulltext_assessment.py` |
| `07_literature_evaluation.py` | Corpus-quality and routing summary | `literature.evaluation` | `uv run python projects/templates/template_literature_meta_analysis/scripts/07_literature_evaluation.py` |
| `08_deep_research_dispatch.py` | Offline deep-research adapter replay | `deep_research.deep_research_adapter` | `uv run python projects/templates/template_literature_meta_analysis/scripts/08_deep_research_dispatch.py` |
| `09_export_bibliography.py` | Unified BibTeX export | `literature.bibliography` | `uv run python projects/templates/template_literature_meta_analysis/scripts/09_export_bibliography.py` |
| `10_reproducibility_assessment.py` | Reproducibility scoring (after `11`) | `reproducibility.runner` | `uv run python projects/templates/template_literature_meta_analysis/scripts/10_reproducibility_assessment.py` |
| `11_fulltext_download.py` | Opt-in OA PDF download/extract (before `10`) | `literature.fulltext_download_cli` | `uv run python projects/templates/template_literature_meta_analysis/scripts/11_fulltext_download.py` |
| `generate_fixture_corpus.py` | Rebuild synthetic fixture corpus | `literature.fixture_corpus` | `uv run python projects/templates/template_literature_meta_analysis/scripts/generate_fixture_corpus.py` |

All scripts accept `--log-level`; see the stage commands below for the flags that matter per stage.

## Stage Commands
```bash
# Live/network retrieval from configured engines
uv run python projects/templates/template_literature_meta_analysis/scripts/01_literature_search.py

# Offline analysis from the current corpus/fixture data
uv run python projects/templates/template_literature_meta_analysis/scripts/02_meta_analysis_pipeline.py

# Optional knowledge graph; --max-papers 0 avoids new LLM extraction
uv run python projects/templates/template_literature_meta_analysis/scripts/03_build_knowledge_graph.py --max-papers 0

# Figures
uv run python projects/templates/template_literature_meta_analysis/scripts/04_generate_figures.py --dpi 300

# Manuscript token hydration
uv run python projects/templates/template_literature_meta_analysis/scripts/05_inject_variables.py

# Full-text availability report
uv run python projects/templates/template_literature_meta_analysis/scripts/06_fulltext_assessment.py

# Corpus evaluation / routing coverage
uv run python projects/templates/template_literature_meta_analysis/scripts/07_literature_evaluation.py --query "active inference"

# Offline deterministic replay of the deep-research adapter
uv run python projects/templates/template_literature_meta_analysis/scripts/08_deep_research_dispatch.py

# Unified BibTeX export from the complete de-duplicated corpus
uv run python projects/templates/template_literature_meta_analysis/scripts/09_export_bibliography.py

# Opt-in network stage: download/extract full text first
uv run python projects/templates/template_literature_meta_analysis/scripts/11_fulltext_download.py

# Opt-in LLM stage: consume the full text produced by script 11
uv run python projects/templates/template_literature_meta_analysis/scripts/10_reproducibility_assessment.py
```

## Pipeline Notes

- `docs/manuscript/config.yaml` owns search term, ten enabled-engine toggles, relevance keywords, hypotheses, sampling, reproducibility scoring, and subfields.
- The default `analysis.scripts` allowlist is offline and deterministic; it intentionally excludes network/LLM scripts `01`, `03`, `10`, and `11`.
- The explicit full-text/reproducibility chain is `11_fulltext_download.py` → `10_reproducibility_assessment.py`; reversing it scores stale or absent full text.
- `05_inject_variables.py` remains last in every declared pipeline order so it sees all available upstream artifacts.
- Network/API-key failures should degrade to `skipped` where the engine contract says they may.
- `output/` is regenerated by these scripts; the canonical public exemplar tracks its latest publication-evidence snapshot.
- `generate_fixture_corpus.py` rebuilds the committed synthetic fixture corpus for offline demonstrations.
