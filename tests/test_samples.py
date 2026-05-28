import os
import runpy
from pathlib import Path

import pytest

import risovalka.gamekit as gamekit


SAMPLE_PATH = Path(__file__).resolve().parents[1] / "risovalka" / "samples" / "mvp_gamekit.py"
MASCOT_LOGO = Path(__file__).resolve().parents[1] / "assets" / "brand" / "risovalka-mascot-logo.png"


def test_mvp_sample_logic_with_fake_game():
    created = []
    loaded_images = []

    class FakeGame:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.window_size = gamekit.Size(width, height)
            self.frames = 0

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
            loaded_images.append(path)
            return object()

        def set_logo(self, image):
            self.logo = image

        def load_shader(self, name):
            class FakeShader:
                def set_param(self, key, value):
                    pass

            return FakeShader()

        def clear_canvas(self):
            pass

        def set_fill_color(self, color):
            pass

        def set_fill_shader(self, *args, **kwargs):
            self.fill_shader_args = args
            pass

        def set_fill_texture(self, *args, **kwargs):
            self.fill_texture_args = args
            self.fill_texture_kwargs = kwargs

        def set_stroke_color(self, color):
            pass

        def draw_circle(self, *args):
            pass

        def draw_rectangle(self, *args):
            pass

        def draw_polygon(self, *args):
            pass

        def draw_image(self, *args):
            pass

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

    fake_game = FakeGame(800, 600)
    created.append(fake_game)

    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(gamekit, "game", fake_game)
    try:
        runpy.run_path(str(SAMPLE_PATH), run_name="__main__")
    finally:
        monkeypatch.undo()

    assert created[0].frames == 3
    assert created[0].title == "Рисовалка: возможности gamekit"
    assert loaded_images[0] == MASCOT_LOGO
    assert len(loaded_images) == 10
    assert all(path.exists() for path in loaded_images)
    assert created[0].logo is not None
    assert len(created[0].fill_shader_args) == 1
    assert created[0].fill_texture_args == (created[0].logo,)
    assert created[0].fill_texture_kwargs["repeat"] is False
    assert created[0].fill_texture_kwargs["rotation"].anchor == (
        created[0].fill_texture_kwargs["start_position"] + gamekit.Size(90, 90)
    )


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
