"""A small JSON-Schema checker (the subset the project's schemas use).

No third-party dependency: ``type``, ``required``, ``properties``,
``additionalProperties`` (bool or schema), ``items``, ``enum``, ``pattern``,
``minItems``, ``minimum`` and ``$ref`` to ``#/definitions/…``.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, List, Mapping

_TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def _is(value: Any, name: str) -> bool:
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, _TYPES[name])


def validate(value: Any, schema: Mapping[str, Any], root: Mapping[str, Any] = None, path: str = "$") -> List[str]:  # type: ignore[assignment]
    """Every way ``value`` breaks ``schema`` (an empty list means it conforms)."""
    root = schema if root is None else root
    if "$ref" in schema:
        node: Any = root
        for part in schema["$ref"].lstrip("#/").split("/"):
            node = node[part]
        return validate(value, node, root, path)
    errors: List[str] = []
    kinds = schema.get("type")
    if kinds is not None:
        names = kinds if isinstance(kinds, list) else [kinds]
        if not any(_is(value, n) for n in names):
            return [f"{path}: expected {'/'.join(names)}, got {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")
    if isinstance(value, str) and "pattern" in schema and not re.search(schema["pattern"], value):
        errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
    if isinstance(value, (int, float)) and not isinstance(value, bool) and "minimum" in schema and value < schema["minimum"]:
        errors.append(f"{path}: {value} is below {schema['minimum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing «{key}»")
        props = schema.get("properties", {})
        extra = schema.get("additionalProperties", True)
        for key, item in value.items():
            if key in props:
                errors += validate(item, props[key], root, f"{path}.{key}")
            elif extra is False:
                errors.append(f"{path}: unknown key «{key}»")
            elif isinstance(extra, dict):
                errors += validate(item, extra, root, f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        if "items" in schema:
            for i, item in enumerate(value):
                errors += validate(item, schema["items"], root, f"{path}[{i}]")
    return errors


def check_file(data: Path, schema: Path) -> List[str]:
    return validate(json.loads(data.read_text(encoding="utf-8")), json.loads(schema.read_text(encoding="utf-8")))
