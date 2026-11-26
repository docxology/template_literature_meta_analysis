# Forking & Re-targeting Guide — `template_literature_meta_analysis`

Start with a fork of this repository and use the [renderer setup](rendering_pipeline.md#set-up-the-renderer-and-project)
to clone it into `projects/working/<project-name>`. Run project scripts inside
that checkout. Pass `--project working/<project-name>` to the shared renderer
from its root.

Edit the topic, query, filters, taxonomy, and hypotheses in
[`docs/manuscript/config.yaml`](manuscript/config.yaml). Review the manuscript prose,
references, and release metadata for the new topic. Update the root citation
sidecars and package metadata when preparing a new publication.

For offline verification, generate a topic-appropriate synthetic fixture with
`scripts/generate_fixture_corpus.py --term <your_term>`, then use the
[offline sequence](rendering_pipeline.md#run-the-offline-fixture-workflow) with
that fixture in place of the bundled one. For new live evidence, run
`uv run --no-sync python scripts/01_literature_search.py --clear-corpus --no-resume`
in a disposable checkout, then run the downstream analysis and manuscript stages.

## The single control surface: `docs/manuscript/config.yaml`

Everything you need to re-target lives under `project_config:`. The blocks, in
the order you'll touch them:

### 1. `search` — what to fetch and how to filter

```yaml
project_config:
  search:
    term: "modafinil"                       # human-readable topic; drives titles, captions, word-cloud
    query: '"modafinil" OR "provigil" OR "armodafinil"'   # query for S2/OpenAlex/Crossref/PubMed
    start_year: 1990                        # drop anything older
    max_results: 1000                       # per-engine cap
    engines:                                # turn engines on/off independently
      arxiv: true
      openalex: true
      semantic_scholar: true
      crossref: true
      pubmed: true
    arxiv_queries:                          # arXiv uses its own field-prefixed syntax
      - 'all:"modafinil"'
      - 'all:"armodafinil"'
    relevance_keywords:                     # a paper is kept iff title+abstract contains ≥1 (case-insensitive)
      - "modafinil"
      - "wakefulness"
      - "narcolepsy"
```

**How the query is used per engine:** `query` is sent verbatim to Semantic
Scholar, OpenAlex, Crossref, and PubMed. arXiv is queried separately with each
entry in `arxiv_queries` (its API needs `all:"…"`/`ti:"…"` field prefixes).
If you leave `arxiv_queries`/`relevance_keywords` empty, the runner derives a
sensible fallback from `term`.

**Relevance filter (read this before you widen your keywords):** after retrieval,
a paper is dropped unless its title+abstract contains at least one
`relevance_keyword`. Keywords are matched **case-insensitively**, and an empty
list is treated as "no filter" (so you can't accidentally empty the corpus) —
but **over-narrow keywords silently shrink your corpus**. Start broad, inspect
`output/data/corpus.jsonl`, then tighten.

### 2. `subfield_keywords` — your taxonomy

Each top-level key is a subfield bucket; its list is the keyword set that
classifies a paper into that bucket. **Any number of buckets is supported** —
the `{{SUBFIELD_TABLE}}` and subfield figures adapt automatically.

```yaml
  subfield_keywords:
    clinical_sleep: ["narcolepsy", "shift work", "sleep apnea", "wakefulness"]
    cognition:      ["working memory", "attention", "executive function"]
    # … add/rename/remove buckets freely
```

### 3. `hypothesis_definitions` — what you want scored

Used by the optional knowledge-graph stage (03) to score the corpus's evidence
for/against each hypothesis. Keyed `H1`, `H2`, … with a `name`, `description`,
and `scope`. The `{{HYPOTHESIS_TABLE}}` renders these with an evidence score
that reads `pending` until stage 03 runs.

```yaml
  hypothesis_definitions:
    H1: { name: "Wakefulness Efficacy", description: "…", scope: "clinical" }
    H2: { name: "Cognitive Enhancement", description: "…", scope: "cognitive" }
```

### 4. Front-matter & optional blocks

- `paper.{title,subtitle}`, top-level `keywords:` — shown on the title page / abstract.
- `embeddings` — offline-deterministic `tfidf_svd` by default (`n_components`,
  `max_features`, `seed`); set `method: transformer` + install the `embeddings`
  extra to upgrade.
- `fulltext` — opt-in OA full-text download (needs an Unpaywall `email`).
- `knowledge_graph` / `llm_extraction` — stage-03 LLM settings (Ollama model,
  `min_confidence`, `max_papers`).

## The pipeline, end to end

| Stage | Script | Reads | Writes | Notes |
|---|---|---|---|---|
| 1 | `01_literature_search.py` | config | `output/data/corpus.jsonl` | 10-engine dispatch + cross-engine de-dup; `--clear-corpus --no-resume` for a fresh run |
| 2 | `02_meta_analysis_pipeline.py` | corpus | subfield/temporal/tfidf/topics/citation JSON + `citation_graph.gml` | deterministic (seeded) |
| 3 | `03_build_knowledge_graph.py` | corpus | nanopublications (JSONL + RDF/TriG), hypothesis scores | **optional** — needs Ollama; `--max-papers N` to sample |
| 4 | `04_generate_figures.py` | stage-2/3 JSON | up to 21 PNGs in `output/figures/` | KG-dependent figures skip gracefully if 03 didn't run |
| 5 | `05_inject_variables.py` | config + all outputs | `output/manuscript/*.md` | injects `{{TOKENS}}`; **raises on any unresolved token** |
| 6 | `06_fulltext_assessment.py` | corpus | full-text assessment | optional |

The opt-in stages `07_literature_evaluation.py`, `08_deep_research_dispatch.py`,
`09_export_bibliography.py`, and the full-text chain `11_fulltext_download.py` →
`10_reproducibility_assessment.py` have distinct inputs and output contracts; see
[script inventory](scripts.md).

De-duplication is by `canonical_id` with priority **normalized-DOI > PMID > arXiv > S2 >
OpenAlex > title-digest**; DOIs are case/prefix-folded so the same paper from two
engines merges.

## What re-targeting does and doesn't require

| You change… | You must also… | Auto-handled? |
|---|---|---|
| `search.term` / `query` / `arxiv_queries` / `relevance_keywords` | nothing else | ✅ all prose/figures derive from outputs |
| `subfield_keywords` (add/rename/remove buckets) | nothing | ✅ `{{SUBFIELD_TABLE}}` + subfield figures adapt |
| `hypothesis_definitions` | nothing (run stage 03 for live scores) | ✅ `{{HYPOTHESIS_TABLE}}` adapts |
| `paper.title` / `keywords` | nothing | ✅ |
| Add a **new** computed number to the prose | add the token to `src/manuscript/variables/compute.py::compute_variables` **and** reference `{{NEW_TOKEN}}` | ⚠️ unresolved tokens make stage 5 fail loudly |
| Add a **new search engine** | add a client in `src/literature/`, register it in `search_runner.py`, add an `engines:` toggle | ⚠️ code + test |

## Token discipline (why stage 5 fails loudly)

`05_inject_variables.py` replaces `{{TOKEN}}` in every `docs/manuscript/*.md` (except
the authoring docs `README.md`/`AGENTS.md`/`SYNTAX.md`, and the lenient
`02e_methods_viz_injection.md` which documents the token system). If a body file
references a token that `compute_variables` doesn't produce, injection **raises a
`RuntimeError`** — there are no silent `{{…}}` leaks in the rendered PDF. So:

1. Add tokens to `compute_variables()` (see [`syntax_guide.md`](syntax_guide.md)).
2. Reference them as `{{TOKEN}}` in the manuscript.
3. Re-run stage 5; a clean exit means every token resolved.

## Verify your fork

Run the [native coverage gate](quickstart.md) and the [render and validation
stages](rendering_pipeline.md#render-and-validate). Review the generated manuscript
and the analysis reports together before publishing a live run.

## Common friction points (and fixes)

| Symptom | Cause | Fix |
|---|---|---|
| Corpus is tiny / empty | `relevance_keywords` too narrow, or `query` too restrictive | Broaden keywords/query; inspect `output/data/corpus.jsonl`; remember the filter is case-insensitive substring |
| `Semantic Scholar: 0 papers` | S2 rate-limits (HTTP 429) without an API key | Expected; the run continues on the other engines. Set an S2 key for reliability |
| `RuntimeError: Unresolved variables in <file>` | A `{{TOKEN}}` isn't produced by `compute_variables` | Add it there, or remove the token from the manuscript |
| `{{TOKEN}}` literal in PDF | Stage 5 not re-run after a docs/manuscript/config edit | Re-run `05_inject_variables.py` |
| Hypothesis scores all read `pending` | Stage 03 (KG) hasn't run, or no Ollama | Run `03_build_knowledge_graph.py` (needs Ollama); scores then populate |
| `mmdc could not find Chrome` at PDF stage | Mermaid blocks need `chrome-headless-shell` | `npx --yes puppeteer browsers install chrome-headless-shell` |
| Stale `*.egg-info/` after rename | editable install under old name | `rm -rf src/*.egg-info/` (already git-ignored) |

## Sibling exemplars

If your work isn't a literature review, fork a closer sibling instead:
[`template_code_project`](https://github.com/docxology/template_code_project) (code-centric, algorithm + analysis),
[`template_prose_project`](https://github.com/docxology/template_prose_project) (prose review, no algorithm),
or [`template_textbook`](https://github.com/docxology/template_textbook) (book-length manuscript).

## See also

- [`quickstart.md`](quickstart.md) — 5-minute run of the bundled modafinil instance
- [`architecture.md`](architecture.md) — module boundaries and data flow
- [`syntax_guide.md`](syntax_guide.md) — the `{{TOKEN}}` system in depth
- [`output_inventory.md`](output_inventory.md) — producer/consumer graph of every artifact
- [`testing_philosophy.md`](testing_philosophy.md) — the zero-mock standard
- [`troubleshooting.md`](troubleshooting.md) — symptom-driven fixes
