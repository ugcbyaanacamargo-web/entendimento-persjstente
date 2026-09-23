#!/usr/bin/env python3
"""Read-only validator for the ChatGPT Web memory repository."""
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote
import yaml
from jsonschema import Draft202012Validator

LINK = re.compile(r"(?<!!)\[[^\]]+\]\((<?[^)\s]+>?)(?:\s+\"[^\"]*\")?\)")
EV = re.compile(r"\bEV-\d{2,}\b")
REQUIRED = ["AGENTS.md", "README.md", "memory/STATE.yaml", "memory/ROUTER.yaml",
            "memory/SCHEMA.yaml", "memory/INDEX.md",
            "projects/formatacao-correta/registro-de-evidencias.md"]

def validate(root):
    root = Path(root).resolve()
    errors = []
    def require(path, where):
        if not isinstance(path, str) or not path or path.startswith(("/", "\\")):
            errors.append(f"{where}: invalid path {path!r}")
            return
        target = (root / unquote(path)).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            errors.append(f"{where}: missing/outside repository: {path}")
    for path in REQUIRED:
        require(path, "required")
    def read(name):
        try:
            return yaml.safe_load((root / name).read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            errors.append(f"{name}: cannot parse: {exc}")
            return None
    schemas = read("memory/SCHEMA.yaml")
    state = read("memory/STATE.yaml")
    router = read("memory/ROUTER.yaml")
    if not isinstance(schemas, dict):
        return errors + ["SCHEMA: expected mapping"]
    if schemas.get("schema_version") != 1:
        errors.append("SCHEMA: schema_version must be 1")
    for name, obj in (("state", state), ("router", router)):
        spec = schemas.get(name)
        if not isinstance(spec, dict):
            errors.append(f"SCHEMA: {name} missing")
            continue
        try:
            Draft202012Validator.check_schema(spec)
            for err in Draft202012Validator(spec).iter_errors(obj):
                errors.append(f"{name}/{list(err.absolute_path)}: {err.message}")
        except Exception as exc:
            errors.append(f"SCHEMA/{name}: invalid: {exc}")
    if isinstance(state, dict):
        for field in ("open_cases", "completed_checks"):
            values = state.get(field, [])
            if isinstance(values, list):
                ids = [v.get("id") for v in values if isinstance(v, dict)]
                if len(ids) != len(set(ids)):
                    errors.append(f"STATE/{field}: duplicate ids")
        for item in state.get("open_cases", []):
            if isinstance(item, dict) and "file" in item:
                require(item["file"], "STATE.open_cases")
        evidence_file = root / "projects/formatacao-correta/registro-de-evidencias.md"
        known = set(EV.findall(evidence_file.read_text(encoding="utf-8"))) if evidence_file.exists() else set()
        refs = [state.get("last_observation", {}).get("evidence_ref")]
        refs += [x.get("evidence_ref") for x in state.get("completed_checks", []) if isinstance(x, dict)]
        for ref in refs:
            if isinstance(ref, str) and ref not in known:
                errors.append(f"STATE: missing evidence {ref}")
    if isinstance(router, dict):
        routes = router.get("routes", [])
        if isinstance(routes, list):
            ids = [v.get("id") for v in routes if isinstance(v, dict)]
            if len(ids) != len(set(ids)):
                errors.append("ROUTER: duplicate ids")
            for route in routes:
                if isinstance(route, dict):
                    for path in route.get("files", []):
                        require(path, "ROUTER.files")
        for path in router.get("default", []):
            require(path, "ROUTER.default")
    for note in root.rglob("*.md"):
        fenced = False
        for line_no, line in enumerate(note.read_text(encoding="utf-8").splitlines(), 1):
            marker = re.match(r"^\s*((?:\x60){3,}|~{3,})", line)
            if marker:
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in LINK.finditer(line):
                address = match.group(1).strip("<>")
                if address.startswith(("https://", "http://", "mailto:", "#", "data:")):
                    continue
                rel = unquote(address.split("#")[0].split("?")[0])
                target = (note.parent / rel).resolve()
                if rel and (not target.is_relative_to(root) or not target.exists()):
                    errors.append(f"{note.relative_to(root)}:{line_no}: broken link {address}")
    mirror = root / "projects/formatacao-correta/estado-atual.md"
    if mirror.exists() and "## PRÓXIMA AÇÃO ÚNICA" in mirror.read_text(encoding="utf-8"):
        errors.append("estado-atual.md duplicates memory/STATE.yaml")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate(parser.parse_args().root)
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print(f"MEMORY {'INVALID' if errors else 'VALID'}: {len(errors)} errors")
    return bool(errors)

if __name__ == "__main__":
    raise SystemExit(main())
