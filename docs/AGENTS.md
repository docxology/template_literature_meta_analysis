# docs/ - Agent-Facing Documentation Hub

This directory documents how to work on the `template_literature_meta_analysis` exemplar. Keep these files project-specific; do not copy optimization or private-sidecar wording into this public template.

## File Inventory

| File | Purpose |
| --- | --- |
| `README.md` | Quick navigation and canonical commands |
| `agent_instructions.md` | Rules agents must read before source, test, or manuscript edits |
| `architecture.md` | Pipeline layers and dependency direction |
| `testing_philosophy.md` | No-mocks testing policy and representative test surfaces |
| `style_guide.md` | Source, script, doc, and error-message conventions |
| `syntax_guide.md` | Markdown, citations, figure refs, and token syntax |
| `rendering_pipeline.md` | Manuscript hydration and render sequence |
| `output_conventions.md` | What `output/` means and how to regenerate it |
| `output_inventory.md` | Producer/consumer inventory for generated artifacts |
| `forking_guide.md` | Retargeting the exemplar to a new literature topic |
| `troubleshooting.md` | Common pipeline failures and fixes |
| `quickstart.md` | First-run commands |
| `faq.md` | Recurring project questions |

## Verification

Follow the [quickstart](quickstart.md) for the native coverage gate. For changes
to data or the manuscript, use the [offline render and validation workflow](rendering_pipeline.md).
