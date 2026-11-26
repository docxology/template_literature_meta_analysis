"""Bind the primary documentation surfaces to the isolated project test gate."""

from __future__ import annotations

from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_TEST_COMMAND = "uv run --no-sync pytest tests/ --cov=src --cov-fail-under=90"
PRIMARY_DOCS = (
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "docs" / "quickstart.md",
    PROJECT_ROOT / "AGENTS.md",
    PROJECT_ROOT / ".agents" / "skills" / "template-literature-meta-analysis" / "SKILL.md",
)


@pytest.mark.parametrize("document", PRIMARY_DOCS, ids=lambda path: path.name)
def test_primary_docs_use_canonical_isolated_test_command(document: Path) -> None:
    """Fresh-clone instructions must not drift back to root-environment pytest."""
    assert CANONICAL_TEST_COMMAND in document.read_text(encoding="utf-8")
