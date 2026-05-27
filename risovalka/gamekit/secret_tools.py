"""Optional helpers that are intentionally outside the core beginner API."""

from __future__ import annotations

from .values import Point, Size


def draw_object(game, object) -> None:
    shape = getattr(object, "shape", None)
    if shape == "circle":
        position = getattr(object, "position", Point(getattr(object, "x", 0), getattr(object, "y", 0)))
        game.draw_circle(position, getattr(object, "radius"))
    elif shape == "rectangle":
        position = getattr(object, "position", Point(getattr(object, "x", 0), getattr(object, "y", 0)))
        size = getattr(object, "size", Size(getattr(object, "width"), getattr(object, "height")))
        game.draw_rectangle(position, size)
    elif shape == "polygon":
        game.draw_polygon(getattr(object, "points"))
    elif shape == "line":
        game.draw_line(getattr(object, "points"))
    else:
        raise ValueError(f"Unknown object shape: {shape!r}")
