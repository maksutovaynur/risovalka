"""Asset wrappers that hide backend objects from beginner-facing code."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .values import Size


@dataclass
class Image:
    data: Any
    original_size: Size


@dataclass
class Shader:
    source: str
    kind: str = "builtin"
    params: dict[str, Any] = field(default_factory=dict)

    def set_param(self, name: str, value: Any) -> None:
        self.params[name] = value


_SHADER_DIR = Path(__file__).with_name("shaders")
BUILTIN_SHADERS: dict[str, Path] = {
    "water": _SHADER_DIR / "water.glsl",
}


def make_shader(shader_source: str) -> Shader:
    path = Path(shader_source)
    if path.exists():
        return Shader(path.read_text(encoding="utf-8"), kind="file")
    if shader_source in BUILTIN_SHADERS:
        return Shader(BUILTIN_SHADERS[shader_source].read_text(encoding="utf-8"), kind="builtin")
    raise FileNotFoundError(f"Unknown shader builtin or file path: {shader_source}")
