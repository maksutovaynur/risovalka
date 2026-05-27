import os
from importlib import import_module

import pytest

from risovalka.gamekit import (
    Color,
    Game,
    Image,
    Object,
    Point,
    Rotation,
    Shader,
    Size,
    Vector,
    game as default_game,
    geometry,
    geometry_tools,
)
from risovalka.gamekit.secret_tools import draw_object


def test_tuple_like_values_are_mutable_by_name_and_index():
    point = Point(1, 2)
    point.x = 5
    point[1] = 6
    assert (point.x, point.y) == (5, 6)

    size = Size(100, 50)
    size[0] = 120
    assert (size.width, size.height) == (120, 50)

    rotation = Rotation(45)
    rotation[0] = 90
    rotation.anchor = Point(1, 1)
    assert rotation.angle == 90
    assert rotation.anchor == Point(1, 1)


def test_vector_arithmetic():
    p1 = Point(10, 20)
    p2 = Point(3, 5)
    v = Vector(2, 4)
    assert not isinstance(v, Size)
    assert (v.x, v.y) == (2, 4)
    assert v.size() == pytest.approx(20**0.5)
    assert p1 - p2 == Vector(7, 15)
    assert p2 + v == Point(5, 9)
    assert v + p2 == Point(5, 9)
    assert p2 + Size(2, 4) == Point(5, 9)
    assert Size(2, 4) + p2 == Point(5, 9)
    assert p2 - v == Point(1, 1)
    assert v + Vector(1, 1) == Vector(3, 5)
    assert v + Size(1, 1) == Vector(3, 5)
    assert Size(1, 1) + v == Vector(3, 5)
    assert Size(2, 4) + Size(1, 1) == Size(3, 5)
    assert v - Vector(1, 1) == Vector(1, 3)
    assert p2 * 2 == Point(6, 10)
    assert 2 * p2 == Point(6, 10)
    assert v * 3 == Vector(6, 12)
    assert 3 * v == Vector(6, 12)
    assert Size(2, 4) * 3 == Size(6, 12)
    assert 3 * Size(2, 4) == Size(6, 12)
    rotated_point = Point(1, 0) @ Rotation(90, Point(0, 0))
    assert rotated_point.x == pytest.approx(0, abs=1e-6)
    assert rotated_point.y == pytest.approx(1, abs=1e-6)
    rotated = Vector(1, 0) @ 90
    assert rotated.x == pytest.approx(0, abs=1e-6)
    assert rotated.y == pytest.approx(1, abs=1e-6)


def test_color_parsing():
    assert Color("#ffaadd00").as_tuple() == (255, 170, 221, 0)
    assert Color("orange").get_hex_string() == "#ffa500ff"
    assert Color(1, 2, 3).as_tuple() == (1, 2, 3, 255)
    assert Color(1, 2, 3, 4).as_tuple() == (1, 2, 3, 4)
    assert Color("transparent").as_tuple() == (0, 0, 0, 0)


def test_shader_params_and_builtin(tmp_path):
    shader_file = tmp_path / "effect.glsl"
    shader_file.write_text("void main() {}", encoding="utf-8")
    shader = Game().load_shader(str(shader_file))
    shader.set_param("time", 12)
    assert isinstance(shader, Shader)
    assert shader.kind == "file"
    assert shader.params["time"] == 12
    builtin = Game().load_shader("water")
    assert builtin.kind == "builtin"
    assert "time" in builtin.source


def test_fill_defaults_use_origin_and_natural_sizes():
    game = Game(320, 240)
    image = Image(data="raw", original_size=Size(16, 24))
    shader = Shader("fragment")

    game.set_fill_texture(image)
    assert game._fill.start_position == Point(0, 0)
    assert game._fill.size == Size(16, 24)
    assert game._fill.rotation.anchor == Point(0, 0)
    assert game._fill.repeat is True

    game.set_fill_shader(shader)
    assert game._fill.start_position == Point(0, 0)
    assert game._fill.size == Size(320, 240)
    assert game._fill.rotation.anchor == Point(0, 0)
    assert game._fill.repeat is True


def test_rotation_and_geometry_defaults():
    game_module = import_module("risovalka.gamekit.game")
    assert game_module._rotation_around(45, Point(10, 20)) == Rotation(45, Point(10, 20))
    assert game_module._rotation_around(None, Point(10, 20)) == Rotation(0, Point(10, 20))
    assert geometry_tools.rotate_point(Point(1, 0), 90).x == pytest.approx(0, abs=1e-6)
    assert geometry_tools.rotate_polygon([Point(1, 0)]) == [Point(1, 0)]
    assert geometry_tools.move_polygon([Point(1, 2)]) == [Point(1, 2)]
    assert geometry_tools.scale_polygon([Point(1, 2)]) == [Point(1, 2)]


def test_set_logo_stores_image_before_window_open():
    image = Image(data="raw", original_size=Size(16, 16))
    game = Game()
    game.set_logo(image)
    assert game._logo_image is image


def test_shader_quad_covers_requested_canvas_area():
    game_module = import_module("risovalka.gamekit.game")
    vertices, uvs = game_module._shader_quad(Point(0, 0), Size(800, 600), Size(800, 600))
    assert vertices == (-1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1)
    assert uvs == (0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0)

    vertices, uvs = game_module._shader_quad(Point(10, 20), Size(100, 50), Size(310, 120))
    assert vertices == (-1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1)
    assert uvs == pytest.approx((-0.1, 2, 3, 2, 3, -0.4, -0.1, 2, 3, -0.4, -0.1, -0.4))

    vertices, uvs = game_module._shader_quad(Point(10, 20), Size(100, 50), Size(310, 120), repeat=False)
    assert vertices == pytest.approx((-0.93548, -0.16667, -0.29032, -0.16667, -0.29032, 0.66667, -0.93548, -0.16667, -0.29032, 0.66667, -0.93548, 0.66667), abs=1e-5)
    assert uvs == (0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1)


def test_image_wrapper_only_has_data_and_original_size():
    image = Image(data="raw", original_size=Size(10, 20))
    assert image.data == "raw"
    assert image.original_size == Size(10, 20)
    assert not hasattr(image, "width")
    assert not hasattr(image, "set_size")


def test_geometry_tools():
    point = geometry_tools.rotate_point(Point(1, 0), Point(0, 0), 90)
    assert point.x == pytest.approx(0, abs=1e-6)
    assert point.y == pytest.approx(1, abs=1e-6)
    assert len(geometry_tools.generate_regular_polygon(Point(0, 0), 10, 6)) == 6
    assert len(geometry_tools.generate_star(Point(0, 0), 5, 10, 5)) == 10

    polygon = [Point(0, 0), Point(1, 0)]
    moved = geometry_tools.move_polygon(polygon, Point(2, 3))
    assert moved == [Point(2, 3), Point(3, 3)]
    scaled = geometry_tools.scale_polygon(polygon, 2, Point(0, 0))
    assert scaled == [Point(0, 0), Point(2, 0)]


def test_object_is_plain_container_and_game_has_no_draw_object():
    obj = Object(x=1, y=2, speed=3.0, power=10)
    assert obj.x == 1
    assert obj.speed == 3.0
    assert not hasattr(obj, "set_drawable")
    assert not hasattr(Game(), "draw_object")


def test_secret_tools_draw_object_delegates_to_explicit_draws():
    calls = []

    class FakeGame:
        def draw_circle(self, *args):
            calls.append(("circle", args))

    draw_object(FakeGame(), Object(shape="circle", position=Point(10, 20), radius=5))
    assert calls == [("circle", (Point(10, 20), 5))]


def test_public_api_shape_aliases_absent_and_helpers_present():
    game = Game()
    assert hasattr(game, "draw_circle")
    assert hasattr(game, "draw_rectangle")
    assert hasattr(game, "draw_polygon")
    assert hasattr(game, "draw_line")
    assert hasattr(game, "draw_text")
    assert hasattr(game, "get_fps")
    assert not hasattr(game, "circle")
    assert not hasattr(game, "draw_star")
    assert not hasattr(game, "draw_regular_polygon")
    assert not hasattr(game, "draw_sprite")
    assert hasattr(game, "wait_close")
    assert hasattr(game, "is_close_clicked")
    assert game._stroke_color == Color("transparent")
    assert game._stroke_width == 1.0


def test_get_fps_uses_smoothness_window(monkeypatch):
    game_module = import_module("risovalka.gamekit.game")
    times = iter([0.0, 0.1, 0.2, 1.2])
    monkeypatch.setattr(game_module.time, "monotonic", lambda: next(times))

    game = Game()
    game.show_canvas()
    game.show_canvas()
    game.show_canvas()

    assert game.get_fps(0) == pytest.approx(1.0)
    assert game.get_fps() == pytest.approx(1.0)
    assert game.get_fps(2) == pytest.approx(2 / 1.1)


def test_singleton_game_is_exported():
    assert isinstance(default_game, Game)
    assert default_game.window_size == Size(800, 600)
    assert not hasattr(default_game, "window_width")
    assert not hasattr(default_game, "window_height")


def test_no_physics_or_collision_api():
    game = Game()
    forbidden = ["collide", "collision", "physics", "body", "velocity"]
    names = dir(game)
    assert not any(any(word in name.lower() for word in forbidden) for name in names)


def test_display_gated_window_smoke():
    pytest.importorskip("pyglet")
    if os.environ.get("DISPLAY") is None and os.environ.get("WAYLAND_DISPLAY") is None:
        pytest.skip("No display available for window smoke test")

    game = Game(120, 80)
    game.set_window_title("Тест")
    game.open()
    try:
        assert game.window_size == Size(120, 80)
        game.set_fill_color("black")
        game.clear_canvas()
        game.set_fill_color("white")
        game.draw_text("FPS", Point(10, 10), size=12)
        game.show_canvas()
    finally:
        if game._window is not None:
            game._window.close()
