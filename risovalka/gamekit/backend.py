"""Lazy backend loading."""

from __future__ import annotations


def require_pyglet():
    try:
        import pyglet  # type: ignore
    except ModuleNotFoundError as exc:
        raise RuntimeError("pyglet is required for window, image, and rendering operations") from exc
    return pyglet
