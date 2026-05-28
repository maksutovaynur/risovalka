"""Educational 2D game engine package."""

from . import file, geometry
from .assets import Image, Shader
from .colors import Color
from .game import Game
from .objects import Object
from .values import Point, Rotation, Size, Vector

geometry_tools = geometry
game = Game()

__all__ = [
    "Color",
    "Game",
    "Image",
    "Object",
    "Point",
    "Rotation",
    "Shader",
    "Size",
    "Vector",
    "file",
    "geometry",
    "geometry_tools",
    "game",
]
