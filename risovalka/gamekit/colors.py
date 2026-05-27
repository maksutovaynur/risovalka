"""Color value and parsing."""

from __future__ import annotations

from collections.abc import Iterable

_NAMED_COLORS: dict[str, tuple[int, int, int, int]] = {
    "transparent": (0, 0, 0, 0),
    "black": (0, 0, 0, 255),
    "white": (255, 255, 255, 255),
    "red": (255, 0, 0, 255),
    "green": (0, 128, 0, 255),
    "blue": (0, 0, 255, 255),
    "yellow": (255, 255, 0, 255),
    "orange": (255, 165, 0, 255),
    "purple": (128, 0, 128, 255),
    "pink": (255, 192, 203, 255),
    "gray": (128, 128, 128, 255),
    "grey": (128, 128, 128, 255),
}


class Color:
    def __init__(self, red, green=None, blue=None, alpha=255):
        if green is None and blue is None:
            red, green, blue, alpha = self._parse_single(red)
        self.red = _byte(red)
        self.green = _byte(green)
        self.blue = _byte(blue)
        self.alpha = _byte(alpha)

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (self.red, self.green, self.blue, self.alpha)

    def get_hex_string(self) -> str:
        return f"#{self.red:02x}{self.green:02x}{self.blue:02x}{self.alpha:02x}"

    def __iter__(self):
        return iter(self.as_tuple())

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Color):
            return self.as_tuple() == other.as_tuple()
        if isinstance(other, tuple):
            return self.as_tuple() == other
        return False

    def __repr__(self) -> str:
        return f"Color({self.red}, {self.green}, {self.blue}, {self.alpha})"

    def _parse_single(self, value) -> tuple[int, int, int, int]:
        if isinstance(value, Color):
            return value.as_tuple()
        if isinstance(value, str):
            text = value.strip().lower()
            if text in _NAMED_COLORS:
                return _NAMED_COLORS[text]
            if text.startswith("#"):
                return _parse_hex(text)
            raise ValueError(f"Unknown color name: {value!r}")
        if isinstance(value, Iterable):
            parts = tuple(value)
            if len(parts) == 3:
                red, green, blue = parts
                return (_byte(red), _byte(green), _byte(blue), 255)
            if len(parts) == 4:
                red, green, blue, alpha = parts
                return (_byte(red), _byte(green), _byte(blue), _byte(alpha))
        raise TypeError(f"Unsupported color format: {value!r}")


def _byte(value: int | float) -> int:
    value = int(value)
    return max(0, min(255, value))


def _parse_hex(text: str) -> tuple[int, int, int, int]:
    raw = text[1:]
    if len(raw) == 6:
        raw += "ff"
    if len(raw) != 8:
        raise ValueError("Hex colors must use #RRGGBB or #RRGGBBAA")
    return tuple(int(raw[index : index + 2], 16) for index in range(0, 8, 2))  # type: ignore[return-value]
