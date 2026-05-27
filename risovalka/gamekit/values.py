"""Small mutable value types used by the beginner-facing API."""

from __future__ import annotations

import math
from collections.abc import Iterable
from typing import Any, Self


class _TupleLike:
    _fields: tuple[str, ...] = ()

    def __iter__(self):
        for field in self._fields:
            yield getattr(self, field)

    def __len__(self) -> int:
        return len(self._fields)

    def __getitem__(self, index: int):
        return getattr(self, self._fields[index])

    def __setitem__(self, index: int, value) -> None:
        setattr(self, self._fields[index], value)

    def __repr__(self) -> str:
        args = ", ".join(f"{name}={getattr(self, name)!r}" for name in self._fields)
        return f"{type(self).__name__}({args})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, _TupleLike):
            return type(self) is type(other) and tuple(self) == tuple(other)
        if isinstance(other, tuple):
            return tuple(self) == other
        return False


class Point(_TupleLike):
    _fields = ("x", "y")

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x - other.x, self.y - other.y)
        other = as_vector(other)
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        other = as_vector(other)
        return Point(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __mul__(self, scalar: float):
        return Point(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __matmul__(self, rotation):
        rotation = as_rotation(rotation)
        return _rotate_point(self, rotation.anchor, rotation.angle)

    @classmethod
    def zero(cls) -> Self:
        return cls(0, 0)


class Size(_TupleLike):
    _fields = ("width", "height")

    def __init__(self, width: float = 0, height: float = 0):
        self.width = width
        self.height = height

    def __add__(self, other):
        if isinstance(other, Point):
            return other + self
        if isinstance(other, Vector):
            return as_vector(self) + other
        other = as_size(other)
        return Size(self.width + other.width, self.height + other.height)

    __radd__ = __add__

    def __sub__(self, other):
        other = as_size(other)
        return Size(self.width - other.width, self.height - other.height)

    def __mul__(self, scalar: float):
        return Size(self.width * scalar, self.height * scalar)

    __rmul__ = __mul__

    def __matmul__(self, angle: float):
        radians = math.radians(angle)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        return Size(self.width * cos_a - self.height * sin_a, self.width * sin_a + self.height * cos_a)

    @classmethod
    def zero(cls) -> Self:
        return cls(0, 0)


class Vector(_TupleLike):
    _fields = ("x", "y")

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return other + self
        other = as_vector(other)
        return Vector(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __sub__(self, other):
        other = as_vector(other)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float):
        return Vector(self.x / scalar, self.y / scalar)

    def __matmul__(self, angle: float):
        radians = math.radians(angle)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        return Vector(self.x * cos_a - self.y * sin_a, self.x * sin_a + self.y * cos_a)

    def size(self) -> float:
        return math.hypot(self.x, self.y)

    @classmethod
    def zero(cls) -> Self:
        return cls(0, 0)


class Rotation(_TupleLike):
    _fields = ("angle", "anchor")

    def __init__(self, angle: float = 0, anchor: Point | tuple[float, float] | None = None):
        self.angle = angle
        self.anchor = as_point(anchor or Point(0, 0))


def as_point(value: Point | Iterable[float]) -> Point:
    if isinstance(value, Point):
        return value
    x, y = value
    return Point(x, y)


def as_size(value: Size | Iterable[float]) -> Size:
    if isinstance(value, Size):
        return value
    width, height = value
    return Size(width, height)


def as_vector(value: Vector | Size | Iterable[float]) -> Vector:
    if isinstance(value, Vector):
        return value
    if isinstance(value, Size):
        return Vector(value.width, value.height)
    x, y = value
    return Vector(x, y)


def as_rotation(value: Rotation | float | int | tuple[Any, Any] | None) -> Rotation:
    if value is None:
        return Rotation(0)
    if isinstance(value, Rotation):
        return value
    if isinstance(value, (int, float)):
        return Rotation(value)
    angle, anchor = value
    return Rotation(angle, as_point(anchor))

def _rotate_point(point: Point, anchor: Point, angle: float) -> Point:
    radians = math.radians(angle)
    cos_a = math.cos(radians)
    sin_a = math.sin(radians)
    dx = point.x - anchor.x
    dy = point.y - anchor.y
    return Point(anchor.x + dx * cos_a - dy * sin_a, anchor.y + dx * sin_a + dy * cos_a)
