import os
import runpy
from pathlib import Path

import pytest

import risovalka.gamekit as gamekit


SAMPLE_PATH = Path(__file__).resolve().parents[1] / "risovalka" / "samples" / "mvp_gamekit.py"
MASCOT_LOGO = Path(__file__).resolve().parents[1] / "assets" / "brand" / "risovalka-mascot-logo.png"


class FakeShader:
    def set_param(self, key, value):
        pass


class FakeGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.window_size = gamekit.Size(width, height)
        self.frames = 0
        self.fill_shader_args = ()
        self.fill_shader_kwargs = {}
        self.fill_texture_args = ()
        self.fill_texture_kwargs = {}
        self.polygons = []
        self.circles = []
        self.images = []

    def set_window_title(self, title):
        self.title = title

    def open(self):
        self.opened = True

    def is_close_clicked(self):
        return self.frames >= 3

    def get_delta_time(self):
        return 1 / 60

    def get_time(self):
        return self.frames / 60

    def get_fps(self):
        return 60

    def load_image(self, path):
        return object()

    def set_logo(self, image):
        self.logo = image

    def load_shader(self, name):
        return FakeShader()

    def clear_canvas(self):
        pass

    def set_fill_color(self, color):
        pass

    def set_fill_shader(self, *args, **kwargs):
        self.fill_shader_args = args
        self.fill_shader_kwargs = kwargs

    def set_fill_texture(self, *args, **kwargs):
        self.fill_texture_args = args
        self.fill_texture_kwargs = kwargs

    def set_stroke_color(self, color):
        pass

    def draw_circle(self, *args):
        self.circles.append(args)

    def draw_rectangle(self, *args):
        pass

    def draw_polygon(self, *args):
        self.polygons.append(args)

    def draw_image(self, *args):
        self.images.append(args)

    def draw_text(self, *args, **kwargs):
        pass

    def is_key_down(self, key):
        return self.frames == 1

    def is_mouse_down(self, button):
        return self.frames == 2

    def is_mouse_clicked(self, button):
        return self.frames == 2

    def get_mouse_position(self):
        return gamekit.Point(120, 140)

    def show_canvas(self):
        self.frames += 1

    def sleep(self, seconds):
        pass


def load_sample_namespace(fake_game=None):
    namespace = runpy.run_path(str(SAMPLE_PATH))
    if fake_game is not None:
        namespace["game"] = fake_game
        namespace["main"].__globals__["game"] = fake_game
    return namespace


def test_mvp_sample_logic_with_fake_game():
    loaded_images = []

    class LoadingFakeGame(FakeGame):
        def load_image(self, path):
            loaded_images.append(path)
            return object()

    fake_game = LoadingFakeGame()

    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(gamekit, "game", fake_game)
    try:
        runpy.run_path(str(SAMPLE_PATH), run_name="__main__")
    finally:
        monkeypatch.undo()

    assert fake_game.frames == 3
    assert fake_game.title == "Рисовалка: возможности gamekit"
    assert loaded_images[0] == MASCOT_LOGO
    assert len(loaded_images) == 10
    assert all(path.exists() for path in loaded_images)
    assert fake_game.logo is not None
    assert len(fake_game.fill_shader_args) == 1
    assert "start_position" in fake_game.fill_shader_kwargs
    assert fake_game.fill_texture_args == (fake_game.logo,)
    assert fake_game.fill_texture_kwargs["repeat"] is False
    assert fake_game.fill_texture_kwargs["start_position"] == gamekit.Point(310, 210)
    assert fake_game.fill_texture_kwargs["rotation"].anchor == gamekit.Point(400, 300)


def test_mvp_sample_world_screen_conversion_helpers():
    fake_game = FakeGame()
    sample = load_sample_namespace(fake_game)
    world = gamekit.Object(hero=gamekit.Object(position=gamekit.Point(1000, -500)))

    assert sample["screen_center"]() == gamekit.Point(400, 300)
    assert sample["world_to_screen"](world, gamekit.Point(1010, -520)) == gamekit.Point(410, 280)
    assert sample["screen_to_world"](world, gamekit.Point(410, 280)) == gamekit.Point(1010, -520)

    viewport = sample["camera_viewport"](world)
    assert (viewport.left, viewport.right, viewport.top, viewport.bottom) == (600, 1400, -800, -200)


def test_mvp_sample_initial_enemies_spawn_around_camera_viewport():
    fake_game = FakeGame()
    sample = load_sample_namespace(fake_game)
    world = sample["create_world"]()
    viewport = sample["camera_viewport"](world)

    assert len(world.enemies) == 5
    for enemy in world.enemies:
        outside_x = enemy.position.x < viewport.left or enemy.position.x > viewport.right
        outside_y = enemy.position.y < viewport.top or enemy.position.y > viewport.bottom
        assert outside_x or outside_y


def test_mvp_sample_mouse_target_and_bullets_use_world_coordinates():
    class ShootingFakeGame(FakeGame):
        def is_key_down(self, key):
            return False

        def is_mouse_down(self, button):
            return True

        def get_time(self):
            return 1

    fake_game = ShootingFakeGame()
    sample = load_sample_namespace(fake_game)
    world = sample["create_world"]()
    world.hero.position = gamekit.Point(1000, -500)
    world.enemies = []

    sample["update_world"](world)

    assert world.mouse_world == gamekit.Point(720, -660)
    assert len(world.bullets) == 1
    assert world.bullets[0].position.x > 900
    assert world.bullets[0].position.y < -400


def test_mvp_sample_draw_conversion_does_not_mutate_world_positions():
    fake_game = FakeGame()
    sample = load_sample_namespace(fake_game)
    world = gamekit.Object(
        hero=gamekit.Object(position=gamekit.Point(1000, -500), angle=0),
        enemies=[
            gamekit.Object(
                points=[gamekit.Point(0, 0), gamekit.Point(10, 0), gamekit.Point(0, 10)],
                position=gamekit.Point(1100, -450),
                angle=0,
                color="orange",
            )
        ],
        bullets=[gamekit.Object(position=gamekit.Point(1020, -480), radius=5)],
        spark_trail=[gamekit.Object(position=gamekit.Point(990, -510), age=0)],
        explosions=[gamekit.Object(position=gamekit.Point(980, -520), age=0)],
        mouse=gamekit.Point(120, 140),
        score=0,
        game_over=False,
    )
    assets = gamekit.Object(
        shader=FakeShader(),
        spark_images=[object()],
        explosion_images=[object()],
        star_texture=object(),
        target_image=object(),
    )
    original_positions = [
        gamekit.Point(world.enemies[0].position.x, world.enemies[0].position.y),
        gamekit.Point(world.bullets[0].position.x, world.bullets[0].position.y),
        gamekit.Point(world.spark_trail[0].position.x, world.spark_trail[0].position.y),
        gamekit.Point(world.explosions[0].position.x, world.explosions[0].position.y),
    ]

    sample["draw_world"](world, assets)

    assert world.enemies[0].position == original_positions[0]
    assert world.bullets[0].position == original_positions[1]
    assert world.spark_trail[0].position == original_positions[2]
    assert world.explosions[0].position == original_positions[3]
    assert fake_game.fill_texture_kwargs["rotation"].anchor == gamekit.Point(400, 300)


def test_mvp_sample_does_not_mutate_import_path():
    source = SAMPLE_PATH.read_text(encoding="utf-8")
    assert "sys.path.insert" not in source


def test_mvp_sample_real_window_smoke():
    pytest.importorskip("pyglet")
    if os.environ.get("DISPLAY") is None and os.environ.get("WAYLAND_DISPLAY") is None:
        pytest.skip("No display available for sample window smoke test")

    old_game = gamekit.game

    class AutoCloseGame(type(old_game)):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._sample_test_frames = 0

        def show_canvas(self):
            super().show_canvas()
            self._sample_test_frames += 1
            if self._sample_test_frames >= 2:
                self._close_clicked = True

    auto_close_game = AutoCloseGame()
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(gamekit, "game", auto_close_game)
    try:
        runpy.run_path(str(SAMPLE_PATH), run_name="__main__")
        import pyglet

        image = pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
        raw = image.get_data("RGBA", image.width * 4)
        colors = {tuple(raw[index : index + 4]) for index in range(0, len(raw), 4)}
        assert len(colors) > 2
    finally:
        if getattr(auto_close_game, "_window", None) is not None:
            auto_close_game._window.close()
        monkeypatch.undo()
