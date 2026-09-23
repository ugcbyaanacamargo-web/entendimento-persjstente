from copy import deepcopy
from pathlib import Path

import yaml

from tools.validate_memory import validate


def fixture(tmp_path: Path) -> Path:
    for path in ["README.md", "AGENTS.md", "memory/INDEX.md",
                 "projects/formatacao-correta/registro-de-evidencias.md"]:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("# Valid\n", encoding="utf-8")
    (tmp_path / "projects/formatacao-correta/registro-de-evidencias.md").write_text("| EV-05 | photo |\n", encoding="utf-8")
    schema = {
        "schema_version": 1,
        "state": {"type": "object", "required": ["phase"], "properties": {"phase": {"enum": ["preflight"]}}},
        "router": {"type": "object", "required": ["default", "routes"]},
    }
    state = {"phase": "preflight", "last_observation": {"evidence_ref": "EV-05"},
             "completed_checks": [], "open_cases": [{"id": "bsod", "file": "README.md"}]}
    router = {"default": ["README.md"], "routes": [{"id": "ram", "files": ["README.md"]}]}
    for name, value in [("SCHEMA", schema), ("STATE", state), ("ROUTER", router)]:
        (tmp_path / f"memory/{name}.yaml").write_text(yaml.safe_dump(value), encoding="utf-8")
    return tmp_path


def modify(root, filename, edit):
    path = root / f"memory/{filename}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    edit(data)
    path.write_text(yaml.safe_dump(data), encoding="utf-8")


def test_valid_memory(tmp_path):
    assert validate(fixture(tmp_path)) == []


def test_reject_missing_route(tmp_path):
    root = fixture(tmp_path)
    modify(root, "ROUTER", lambda x: x["routes"][0].update(files=["missing.md"]))
    assert any("missing.md" in error for error in validate(root))


def test_reject_missing_evidence(tmp_path):
    root = fixture(tmp_path)
    modify(root, "STATE", lambda x: x["last_observation"].update(evidence_ref="EV-99"))
    assert any("EV-99" in error for error in validate(root))


def test_reject_duplicate_case(tmp_path):
    root = fixture(tmp_path)
    modify(root, "STATE", lambda x: x["open_cases"].append(deepcopy(x["open_cases"][0])))
    assert any("duplicate" in error for error in validate(root))


def test_reject_broken_markdown_link(tmp_path):
    root = fixture(tmp_path)
    (root / "README.md").write_text("[broken](not-found.md)\n", encoding="utf-8")
    assert any("not-found.md" in error for error in validate(root))


def test_reject_stale_state_copy(tmp_path):
    root = fixture(tmp_path)
    (root / "projects/formatacao-correta/estado-atual.md").write_text("## PRÓXIMA AÇÃO ÚNICA\n", encoding="utf-8")
    assert any("duplicates" in error for error in validate(root))


def test_reject_invalid_schema_value(tmp_path):
    root = fixture(tmp_path)
    modify(root, "STATE", lambda x: x.update(phase="impossible"))
    assert any("phase" in error for error in validate(root))
