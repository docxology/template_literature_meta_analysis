# Literature Meta-Analysis Documentation

| Task | Guide |
| --- | --- |
| Install the locked project environment and run tests | [Quickstart](quickstart.md) |
| Reproduce the offline example and validate its publication | [Rendering and validation](rendering_pipeline.md) |
| Edit the paper, bibliography, or review configuration | [Manuscript source](manuscript/README.md) |
| Retarget the review or use live retrieval | [Forking guide](forking_guide.md), [standalone publication guide](standalone.md) |
| Understand data provenance and the offline corpus | [Data](data.md), [synthetic fixture](fixtures.md) |
| Find code and test responsibilities | [Architecture](architecture.md), [implementation](implementation/README.md), [testing](testing/README.md), [test patterns](test-patterns.md) |
| Find a script or add a stage | [Script inventory](scripts.md), [script conventions](script-conventions.md) |
| Edit manuscript formatting and injected variables | [Style](style_guide.md), [syntax](syntax_guide.md) |
| Inspect release artifacts | [Output inventory](output_inventory.md), [output conventions](output_conventions.md) |
| Diagnose problems | [Troubleshooting](troubleshooting.md), [FAQ](faq.md) |
| Review maintenance context | [Backlog](backlog.md), [historical commissioning notes](historical-commissioning.md), [agent guidance](AGENTS.md) |

The maintained sections, citations, and active configuration live in
[`docs/manuscript/`](manuscript/). The Python variable extractors live in
[`src/manuscript/`](../src/manuscript/). The files in [`output/`](../output/)
include the tracked publication snapshot. Generate offline fixture outputs in
a disposable checkout to keep the fixtures, release evidence, and outputs attributable.
