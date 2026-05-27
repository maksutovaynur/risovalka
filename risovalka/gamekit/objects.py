"""Convenient dynamic object container."""

from __future__ import annotations

from typing import Any


class Object:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name: str) -> Any:
        raise AttributeError(name)

    def __repr__(self) -> str:
        args = ", ".join(f"{key}={value!r}" for key, value in sorted(self.__dict__.items()))
        return f"Object({args})"
