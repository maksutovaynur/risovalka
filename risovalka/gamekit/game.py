"""The beginner-facing Game class."""

from __future__ import annotations

import math
import time
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any

from .assets import Image, Shader, make_shader
from .backend import require_pyglet
from .colors import Color
from .geometry import rotate_point, rotate_polygon
from .values import Point, Rotation, Size, as_point, as_rotation, as_size


@dataclass
class _FillState:
    kind: str
    value: Any = None
    start_position: Point = field(default_factory=Point)
    size: Size = field(default_factory=Size)
    rotation: Rotation = field(default_factory=Rotation)
    repeat: bool = True


_SHADER_VERTEX_SOURCE = """#version 330
in vec2 position;
in vec2 tex_coords;
out vec2 uv;

void main() {
    uv = tex_coords;
    gl_Position = vec4(position, 0.0, 1.0);
}
"""


class Game:
    def __init__(self, width: int = 800, height: int = 600, title: str = "Risovalka"):
        self._window = None
        self._batch = None
        self._frame_items: list[Any] = []
        self._title = title
        self._logo_image: Image | None = None
        self._requested_size = Size(width, height)
        self._fullscreen = False
        self._window_size = Size(width, height)
        self._fill = _FillState("color", Color("black"))
        self._stroke_color = Color("transparent")
        self._stroke_width = 1.0
        self._stroke_style = "solid"
        self._keys_down: set[str] = set()
        self._keys_clicked: set[str] = set()
        self._mouse_down: set[str] = set()
        self._mouse_clicked: set[str] = set()
        self._mouse_position = Point(0, 0)
        self._mouse_scroll = 0.0
        self._close_clicked = False
        self._opened_at = time.monotonic()
        self._last_frame_time = self._opened_at
        self._delta_time = 0.0
        self._instant_fps = 0.0
        self._frame_times: list[float] = []
        self._shader_programs: dict[int, Any] = {}

    @property
    def window_size(self) -> Size:
        return Size(self._window_size.width, self._window_size.height)

    def set_window_title(self, title: str) -> None:
        self._title = title
        if self._window is not None:
            self._window.set_caption(title)

    def set_logo(self, image: Image) -> None:
        self._logo_image = image
        if self._window is not None:
            self._window.set_icon(image.data)

    def set_window_size(self, width: int, height: int) -> None:
        self._requested_size = Size(int(width), int(height))
        self._window_size = Size(int(width), int(height))
        if self._window is not None:
            self._window.set_size(int(width), int(height))

    def set_window_fullscreen(self, enabled: bool) -> None:
        self._fullscreen = bool(enabled)
        if self._window is not None:
            self._window.set_fullscreen(self._fullscreen)

    def open(self) -> None:
        if self._window is not None:
            return
        pyglet = require_pyglet()
        self._window = pyglet.window.Window(
            width=self._requested_size.width,
            height=self._requested_size.height,
            caption=self._title,
            fullscreen=self._fullscreen,
            resizable=True,
        )
        self._batch = pyglet.graphics.Batch()
        self._window_size = Size(self._window.width, self._window.height)
        if self._logo_image is not None:
            self._window.set_icon(self._logo_image.data)
        self._install_handlers(pyglet)

    def wait_close(self) -> None:
        self.open()
        while not self._close_clicked:
            self.show_canvas()
            self.sleep(0.02)

    def is_close_clicked(self) -> bool:
        return self._close_clicked

    def sleep(self, seconds: float) -> None:
        time.sleep(seconds)

    def get_time(self) -> float:
        return time.monotonic() - self._opened_at

    def get_delta_time(self) -> float:
        return self._delta_time

    def get_fps(self, smoothness: float = 1) -> float:
        if smoothness <= 0:
            return self._instant_fps
        if len(self._frame_times) < 2:
            return 0.0
        end_time = self._frame_times[-1]
        start_time = end_time - smoothness
        frame_times = [frame_time for frame_time in self._frame_times if frame_time >= start_time]
        if len(frame_times) < 2:
            return 0.0
        duration = frame_times[-1] - frame_times[0]
        if duration <= 0:
            return 0.0
        return (len(frame_times) - 1) / duration

    def clear_canvas(self) -> None:
        if self._window is None:
            return
        pyglet = require_pyglet()
        if self._fill.kind == "color":
            red, green, blue, alpha = _rgba_float(self._fill.value)
            pyglet.gl.glClearColor(red, green, blue, alpha)
        else:
            pyglet.gl.glClearColor(0, 0, 0, 0)
        self._window.clear()
        if self._fill.kind == "shader":
            self._draw_shader_fill(pyglet, self._fill)
        if self._fill.kind == "texture":
            self._draw_texture_fill(pyglet, self._fill)

    def show_canvas(self) -> None:
        now = time.monotonic()
        self._delta_time = now - self._last_frame_time
        self._last_frame_time = now
        if self._delta_time > 0:
            self._instant_fps = 1 / self._delta_time
        self._frame_times.append(now)
        self._frame_times = self._frame_times[-1000:]
        if self._window is not None:
            self._window.dispatch_events()
            if self._batch is not None:
                self._batch.draw()
            self._window.flip()
            self._batch = require_pyglet().graphics.Batch()
            self._frame_items = []
        self._keys_clicked.clear()
        self._mouse_clicked.clear()
        self._mouse_scroll = 0.0

    def set_fill_color(self, color) -> None:
        self._fill = _FillState("color", Color(color))

    def set_fill_texture(
        self,
        image: Image,
        start_position: Point | Iterable[float] = (0, 0),
        size: Size | Iterable[float] | None = None,
        rotation: Rotation | float | None = None,
        repeat: bool = True,
    ) -> None:
        start_position = as_point(start_position)
        size = as_size(size or image.original_size)
        self._fill = _FillState("texture", image, start_position, size, _rotation_around(rotation, start_position), repeat)

    def set_fill_shader(
        self,
        shader: Shader,
        start_position: Point | Iterable[float] = (0, 0),
        size: Size | Iterable[float] | None = None,
        rotation: Rotation | float | None = None,
        repeat: bool = True,
    ) -> None:
        start_position = as_point(start_position)
        size = as_size(size or self.window_size)
        self._fill = _FillState("shader", shader, start_position, size, _rotation_around(rotation, start_position), repeat)

    def set_stroke_color(self, color) -> None:
        self._stroke_color = Color(color)

    def set_stroke_width(self, width: float) -> None:
        self._stroke_width = float(width)

    def set_stroke_style(self, params) -> None:
        self._stroke_style = params

    def draw_circle(self, *args) -> None:
        center, radius = _circle_args(args)
        if self._window is None:
            return
        pyglet = require_pyglet()
        x, y = self._to_backend(center)
        color = _shape_color(self._fill, self._stroke_color)
        shape = pyglet.shapes.Circle(x, y, radius, color=color[:3], batch=self._batch)
        shape.opacity = color[3]
        self._frame_items.append(shape)
        self._draw_stroke_circle(pyglet, x, y, radius)

    def draw_rectangle(self, *args) -> None:
        point, size = _rectangle_args(args)
        points = [
            point,
            Point(point.x + size.width, point.y),
            Point(point.x + size.width, point.y + size.height),
            Point(point.x, point.y + size.height),
        ]
        self.draw_polygon(points)

    def draw_polygon(self, *args) -> None:
        points = _points_args(args)
        if self._window is None or len(points) < 3:
            return
        pyglet = require_pyglet()
        if self._fill.kind == "texture":
            self._draw_textured_polygon(pyglet, points, self._fill)
            if self._stroke_width > 0:
                self.draw_line(points + [points[0]])
            return
        backend_points = [self._to_backend(point) for point in points]
        color = _shape_color(self._fill, self._stroke_color)
        shape = pyglet.shapes.Polygon(*backend_points, color=color[:3], batch=self._batch)
        shape.opacity = color[3]
        self._frame_items.append(shape)
        if self._stroke_width > 0:
            self.draw_line(points + [points[0]])

    def draw_line(self, *args) -> None:
        points = _points_args(args)
        if self._window is None or len(points) < 2:
            return
        pyglet = require_pyglet()
        color = self._stroke_color.as_tuple()
        for first, second in zip(points, points[1:]):
            x1, y1 = self._to_backend(first)
            x2, y2 = self._to_backend(second)
            line = pyglet.shapes.Line(x1, y1, x2, y2, thickness=self._stroke_width, color=color[:3], batch=self._batch)
            line.opacity = color[3]
            self._frame_items.append(line)

    def draw_image(
        self,
        image: Image,
        position: Point | Iterable[float],
        size: Size | Iterable[float] | None = None,
        rotation: Rotation | float | None = None,
    ) -> None:
        if self._window is None:
            return
        pyglet = require_pyglet()
        position = as_point(position)
        size = as_size(size or image.original_size)
        rotation = _rotation_around(rotation, Point(position.x + size.width / 2, position.y + size.height / 2))
        scale_x = size.width / image.original_size.width if image.original_size.width else 1
        scale_y = size.height / image.original_size.height if image.original_size.height else 1
        anchor_x = rotation.anchor.x - position.x
        anchor_y = size.height - (rotation.anchor.y - position.y)
        old_anchor_x = getattr(image.data, "anchor_x", 0)
        old_anchor_y = getattr(image.data, "anchor_y", 0)
        image.data.anchor_x = round(anchor_x / scale_x) if scale_x else 0
        image.data.anchor_y = round(anchor_y / scale_y) if scale_y else 0
        try:
            sprite = pyglet.sprite.Sprite(
                image.data,
                x=position.x + anchor_x,
                y=self._window_size.height - position.y - size.height + anchor_y,
                batch=self._batch,
            )
            sprite.scale_x = scale_x
            sprite.scale_y = scale_y
            sprite.rotation = -rotation.angle
            self._frame_items.append(sprite)
        finally:
            image.data.anchor_x = old_anchor_x
            image.data.anchor_y = old_anchor_y

    def draw_text(
        self,
        text: str,
        position: Point | Iterable[float],
        size: float = 20,
        rotation: Rotation | float | None = None,
        color=None,
    ) -> None:
        if self._window is None:
            return
        pyglet = require_pyglet()
        position = as_point(position)
        rotation = as_rotation(rotation)
        if color is not None:
            text_color = Color(color)
        elif self._fill.kind == "color":
            text_color = self._fill.value
        else:
            text_color = Color("white")
        label = pyglet.text.Label(
            text,
            font_size=size,
            x=position.x,
            y=self._window_size.height - position.y,
            anchor_x="left",
            anchor_y="top",
            color=text_color.as_tuple(),
            batch=self._batch,
        )
        label.rotation = -rotation.angle
        self._frame_items.append(label)

    def load_image(self, image_path) -> Image:
        pyglet = require_pyglet()
        data = pyglet.image.load(str(image_path))
        return Image(data=data, original_size=Size(data.width, data.height))

    def load_shader(self, shader_source: str) -> Shader:
        return make_shader(shader_source)

    def is_key_down(self, key_name: str) -> bool:
        return _key_name(key_name) in self._keys_down

    def is_key_clicked(self, key_name: str) -> bool:
        return _key_name(key_name) in self._keys_clicked

    def is_mouse_down(self, button_name: str) -> bool:
        return button_name.lower() in self._mouse_down

    def is_mouse_clicked(self, button_name: str) -> bool:
        return button_name.lower() in self._mouse_clicked

    def get_mouse_position(self) -> Point:
        return Point(self._mouse_position.x, self._mouse_position.y)

    def get_mouse_scroll(self) -> float:
        return self._mouse_scroll

    def _to_backend(self, point: Point) -> tuple[float, float]:
        return (point.x, self._window_size.height - point.y)

    def _draw_stroke_circle(self, pyglet, x: float, y: float, radius: float) -> None:
        if self._stroke_width <= 0:
            return
        color = self._stroke_color.as_tuple()
        outline = pyglet.shapes.Arc(x, y, radius, thickness=self._stroke_width, color=color[:3], batch=self._batch)
        outline.opacity = color[3]
        self._frame_items.append(outline)

    def _draw_shader_fill(self, pyglet, fill: _FillState) -> None:
        program = self._shader_program(fill.value, pyglet)
        for name, value in fill.value.params.items():
            if name in program.uniforms:
                program[name] = value
        vertices, uvs = _shader_quad(fill.start_position, fill.size, self._window_size, fill.repeat)
        vertex_list = program.vertex_list(
            6,
            pyglet.gl.GL_TRIANGLES,
            position=("f", vertices),
            tex_coords=("f", uvs),
        )
        program.use()
        vertex_list.draw(pyglet.gl.GL_TRIANGLES)
        program.stop()
        vertex_list.delete()

    def _draw_texture_fill(self, pyglet, fill: _FillState) -> None:
        if fill.size.width <= 0 or fill.size.height <= 0:
            return
        if fill.repeat:
            min_column = math.floor((0 - fill.start_position.x) / fill.size.width)
            max_column = math.ceil((self._window_size.width - fill.start_position.x) / fill.size.width)
            min_row = math.floor((0 - fill.start_position.y) / fill.size.height)
            max_row = math.ceil((self._window_size.height - fill.start_position.y) / fill.size.height)
        else:
            min_column = min_row = 0
            max_column = max_row = 1
        for column in range(min_column, max_column):
            for row in range(min_row, max_row):
                position = Point(
                    fill.start_position.x + column * fill.size.width,
                    fill.start_position.y + row * fill.size.height,
                )
                self._draw_texture_tile(pyglet, fill.value, position, fill.size, fill.rotation)

    def _draw_texture_tile(self, pyglet, image: Image, position: Point, size: Size, rotation: Rotation) -> None:
        scale_x = size.width / image.original_size.width if image.original_size.width else 1
        scale_y = size.height / image.original_size.height if image.original_size.height else 1
        anchor_x = rotation.anchor.x - position.x
        anchor_y = size.height - (rotation.anchor.y - position.y)
        old_anchor_x = getattr(image.data, "anchor_x", 0)
        old_anchor_y = getattr(image.data, "anchor_y", 0)
        image.data.anchor_x = round(anchor_x / scale_x) if scale_x else 0
        image.data.anchor_y = round(anchor_y / scale_y) if scale_y else 0
        try:
            sprite = pyglet.sprite.Sprite(
                image.data,
                x=position.x + anchor_x,
                y=self._window_size.height - position.y - size.height + anchor_y,
            )
            sprite.scale_x = scale_x
            sprite.scale_y = scale_y
            sprite.rotation = -rotation.angle
            sprite.draw()
            sprite.delete()
        finally:
            image.data.anchor_x = old_anchor_x
            image.data.anchor_y = old_anchor_y

    def _draw_textured_polygon(self, pyglet, points: list[Point], fill: _FillState) -> None:
        if fill.size.width <= 0 or fill.size.height <= 0:
            return
        texture = fill.value.data.get_texture()
        program = pyglet.sprite.get_default_shader()
        group = pyglet.sprite.SpriteGroup(
            texture,
            pyglet.gl.GL_SRC_ALPHA,
            pyglet.gl.GL_ONE_MINUS_SRC_ALPHA,
            program,
        )
        center = _polygon_center(points)
        vertices = [center, *points]
        positions: list[float] = []
        tex_coords: list[float] = []
        for point in vertices:
            x, y = self._to_backend(point)
            positions.extend((x, y, 0))
            tex_coords.extend(
                _texture_coords_for_point(point, texture.tex_coords, fill.start_position, fill.size, fill.rotation)
            )
        indices: list[int] = []
        for index in range(1, len(vertices)):
            indices.extend((0, index, 1 if index == len(vertices) - 1 else index + 1))
        vertex_list = program.vertex_list_indexed(
            len(vertices),
            pyglet.gl.GL_TRIANGLES,
            indices,
            self._batch,
            group,
            position=("f", positions),
            colors=("Bn", (255, 255, 255, 255) * len(vertices)),
            translate=("f", (0, 0, 0) * len(vertices)),
            scale=("f", (1, 1) * len(vertices)),
            rotation=("f", (0,) * len(vertices)),
            tex_coords=("f", tex_coords),
        )
        self._frame_items.append(vertex_list)

    def _shader_program(self, shader: Shader, pyglet):
        key = id(shader)
        if key not in self._shader_programs:
            vertex_shader = pyglet.graphics.shader.Shader(_SHADER_VERTEX_SOURCE, "vertex")
            fragment_shader = pyglet.graphics.shader.Shader(shader.source, "fragment")
            self._shader_programs[key] = pyglet.graphics.shader.ShaderProgram(vertex_shader, fragment_shader)
        return self._shader_programs[key]

    def _install_handlers(self, pyglet) -> None:
        @self._window.event
        def on_resize(width, height):
            self._window_size = Size(width, height)

        @self._window.event
        def on_close():
            self._close_clicked = True

        @self._window.event
        def on_key_press(symbol, modifiers):
            name = pyglet.window.key.symbol_string(symbol).lower()
            self._keys_down.add(name)
            self._keys_clicked.add(name)

        @self._window.event
        def on_key_release(symbol, modifiers):
            self._keys_down.discard(pyglet.window.key.symbol_string(symbol).lower())

        @self._window.event
        def on_mouse_press(x, y, button, modifiers):
            name = _mouse_button_name(pyglet, button)
            self._mouse_down.add(name)
            self._mouse_clicked.add(name)

        @self._window.event
        def on_mouse_release(x, y, button, modifiers):
            self._mouse_down.discard(_mouse_button_name(pyglet, button))

        @self._window.event
        def on_mouse_motion(x, y, dx, dy):
            self._mouse_position = Point(x, self._window_size.height - y)

        @self._window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            self._mouse_position = Point(x, self._window_size.height - y)

        @self._window.event
        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            self._mouse_scroll += scroll_y


def _key_name(key_name: str) -> str:
    return key_name.lower().replace(" ", "_")


def _mouse_button_name(pyglet, button) -> str:
    mouse = pyglet.window.mouse
    if button == mouse.LEFT:
        return "left"
    if button == mouse.RIGHT:
        return "right"
    if button == mouse.MIDDLE:
        return "middle"
    return str(button).lower()


def _rgba_float(color: Color) -> tuple[float, float, float, float]:
    red, green, blue, alpha = color.as_tuple()
    return (red / 255, green / 255, blue / 255, alpha / 255)


def _rotation_around(rotation: Rotation | float | None, anchor: Point) -> Rotation:
    if rotation is None:
        return Rotation(0, anchor)
    if isinstance(rotation, Rotation):
        return rotation
    return Rotation(rotation, anchor)


def _shader_quad(
    start_position: Point,
    size: Size,
    window_size: Size,
    repeat: bool = True,
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    if repeat:
        left = -1
        right = 1
        top = 1
        bottom = -1
        uv_left = (0 - start_position.x) / size.width if size.width else 0
        uv_right = (window_size.width - start_position.x) / size.width if size.width else 1
        uv_top = (0 - start_position.y) / size.height if size.height else 0
        uv_bottom = (window_size.height - start_position.y) / size.height if size.height else 1
    else:
        left = start_position.x / window_size.width * 2 - 1
        right = (start_position.x + size.width) / window_size.width * 2 - 1
        top = 1 - start_position.y / window_size.height * 2
        bottom = 1 - (start_position.y + size.height) / window_size.height * 2
        uv_left = 0
        uv_right = 1
        uv_top = 1
        uv_bottom = 0
    return (
        (
            left,
            bottom,
            right,
            bottom,
            right,
            top,
            left,
            bottom,
            right,
            top,
            left,
            top,
        ),
        (
            uv_left,
            uv_bottom,
            uv_right,
            uv_bottom,
            uv_right,
            uv_top,
            uv_left,
            uv_bottom,
            uv_right,
            uv_top,
            uv_left,
            uv_top,
        ),
    )


def _shape_color(fill: _FillState, fallback: Color) -> tuple[int, int, int, int]:
    if fill.kind == "color":
        return fill.value.as_tuple()
    # Texture and shader fills are represented by backend-specific state during real rendering.
    return fallback.as_tuple()


def _polygon_center(points: list[Point]) -> Point:
    return Point(
        sum(point.x for point in points) / len(points),
        sum(point.y for point in points) / len(points),
    )


def _texture_coords_for_point(
    point: Point,
    texture_coords: tuple[float, ...],
    start_position: Point,
    size: Size,
    rotation: Rotation,
) -> tuple[float, float, float]:
    if rotation.angle:
        point = rotate_point(point, rotation.anchor, -rotation.angle)
    left = min(texture_coords[0::3])
    right = max(texture_coords[0::3])
    bottom = min(texture_coords[1::3])
    top = max(texture_coords[1::3])
    u = (point.x - start_position.x) / size.width if size.width else 0
    v = 1 - (point.y - start_position.y) / size.height if size.height else 0
    return (
        left + (right - left) * u,
        bottom + (top - bottom) * v,
        texture_coords[2],
    )


def _circle_args(args) -> tuple[Point, float]:
    if len(args) == 2:
        return as_point(args[0]), float(args[1])
    if len(args) == 3:
        return Point(args[0], args[1]), float(args[2])
    raise TypeError("draw_circle accepts (center, radius) or (x, y, radius)")


def _rectangle_args(args) -> tuple[Point, Size]:
    if len(args) == 2:
        first, second = args
        if isinstance(second, Size) or _looks_like_size(second):
            return as_point(first), as_size(second)
        point1 = as_point(first)
        point2 = as_point(second)
        return point1, Size(point2.x - point1.x, point2.y - point1.y)
    if len(args) == 4:
        return Point(args[0], args[1]), Size(args[2], args[3])
    raise TypeError("draw_rectangle accepts (x, y, width, height), (point1, point2), or (point, size)")


def _looks_like_size(value) -> bool:
    return hasattr(value, "width") and hasattr(value, "height")


def _points_args(args) -> list[Point]:
    if len(args) == 1 and isinstance(args[0], list):
        return [as_point(point) for point in args[0]]
    return [as_point(point) for point in args]


def _rotated_rect(position: Point, size: Size, rotation: Rotation) -> list[Point]:
    points = [
        position,
        Point(position.x + size.width, position.y),
        Point(position.x + size.width, position.y + size.height),
        Point(position.x, position.y + size.height),
    ]
    if rotation.angle:
        return rotate_polygon(points, rotation.angle, rotation.anchor)
    return points
