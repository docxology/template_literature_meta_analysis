# AI Agent Instructions - Literature Meta-Analysis Exemplar

Read this before modifying `template_literature_meta_analysis`.

## Rule 1: Config Owns Domain Policy

`docs/manuscript/config.yaml` is the control surface for the review topic, query strings, enabled engines, relevance keywords, subfield taxonomy, and hypotheses. Retargeting from `modafinil` to another topic should primarily be a config and fixture-corpus change, not a source-code fork.

## Rule 2: Scripts Stay Thin

Scripts under `scripts/` orchestrate stage inputs, outputs, logging, and CLI flags. Retrieval, de-duplication, bibliometrics, embeddings, hypothesis scoring, figure generation, and token computation live under `src/`.

## Rule 3: No Mocks

Tests use real objects, real temporary files, and local HTTP servers through `pytest-httpserver`. Do not add `unittest.mock`, `MagicMock`, `mocker.patch`, or call-count assertions.

## Rule 4: Synthetic Fixture Honesty

The committed `data/fixtures/modafinil_corpus.jsonl` is a synthetic offline fixture. It demonstrates the pipeline; it is not evidence about modafinil. Real claims require a live retrieval run and regenerated artifacts.

## Rule 5: Output Is Disposable

Never hand-edit `output/`. To change generated manuscript text, edit source manuscript sections, config, or `src/manuscript/variables/` and rerun `scripts/05_inject_variables.py`. To change figures or data, edit the relevant `src/` producer and rerun the stage.

## Rule 6: Use Generated Facts

Use the native test receipt for counts and coverage.

## Verification

Follow the [quickstart](quickstart.md) for the native coverage gate. For changes
to data or the manuscript, use the [offline render and validation workflow](rendering_pipeline.md).
