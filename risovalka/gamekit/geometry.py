"""Explicit geometry helpers for generated and transformed points."""

from __future__ import annotations

import math
from collections.abc import Iterable

from .values import Point, as_point


def rotate_point(point: Point | Iterable[float], *args, anchor: Point | Iterable[float] = (0, 0), angle: float = 0) -> Point:
    if len(args) == 1:
        angle = args[0]
    elif len(args) == 2:
        anchor, angle = args
    elif len(args) > 2:
        raise TypeError("rotate_point accepts (point, angle) or (point, anchor, angle)")
    point = as_point(point)
    anchor = as_point(anchor)
    radians = math.radians(angle)
    cos_a = math.cos(radians)
    sin_a = math.sin(radians)
    dx = point.x - anchor.x
    dy = point.y - anchor.y
    return Point(anchor.x + dx * cos_a - dy * sin_a, anchor.y + dx * sin_a + dy * cos_a)


def generate_regular_polygon(center: Point | Iterable[float], radius: float, sides: int) -> list[Point]:
    if sides < 3:
        raise ValueError("Regular polygon needs at least 3 sides")
    center = as_point(center)
    return [
        Point(
            center.x + math.cos(2 * math.pi * index / sides) * radius,
            center.y + math.sin(2 * math.pi * index / sides) * radius,
        )
        for index in range(sides)
    ]


def generate_star(
    center: Point | Iterable[float],
    lower_radius: float,
    higher_radius: float,
    num_ends: int,
) -> list[Point]:
    if num_ends < 2:
        raise ValueError("Star needs at least 2 ends")
    center = as_point(center)
    points: list[Point] = []
    for index in range(num_ends * 2):
        radius = higher_radius if index % 2 == 0 else lower_radius
        angle = math.pi * index / num_ends - math.pi / 2
        points.append(Point(center.x + math.cos(angle) * radius, center.y + math.sin(angle) * radius))
    return points


def rotate_polygon(points, angle: float = 0, anchor: Point | Iterable[float] = (0, 0)) -> list[Point]:
    return [rotate_point(point, anchor, angle) for point in points]


def move_polygon(points, delta: Point | Iterable[float] = (0, 0)) -> list[Point]:
    delta = as_point(delta)
    return [Point(as_point(point).x + delta.x, as_point(point).y + delta.y) for point in points]


def scale_polygon(points, scale=1, anchor: Point | Iterable[float] = (0, 0)) -> list[Point]:
    anchor = as_point(anchor)
    if isinstance(scale, (int, float)):
        sx = sy = scale
    else:
        sx, sy = scale
    scaled: list[Point] = []
    for point in points:
        point = as_point(point)
        scaled.append(Point(anchor.x + (point.x - anchor.x) * sx, anchor.y + (point.y - anchor.y) * sy))
    return scaled
