import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


FRAMES = [
    (170, 350, "#6f5cff"),
    (320, 290, "#44aaff"),
    (500, 340, "#4bb35f"),
]


def draw_frame(x, y, color):
    game.set_fill_color("#20242d")
    game.clear_canvas()

    game.draw_text("Ручная анимация: три кадра по очереди", (38, 32), size=24, color="white")
    game.draw_text("Следующий урок: настоящий игровой цикл", (38, 64), size=18, color="#ffd166")

    game.set_fill_color("#404857")
    game.draw_rectangle(90, 410, 620, 35)

    game.set_fill_color(color)
    game.draw_circle(x, y, 38)


game.set_window_title("Урок 1: ручной мультфильм")
game.set_window_size(800, 600)
game.open()

frame_index = 0
next_frame_time = 0

# Здесь цикл нужен только для показа кадров. Подробно разберём его позже.
while not game.is_close_clicked():
    if game.get_time() >= next_frame_time:
        frame_index = (frame_index + 1) % len(FRAMES)
        next_frame_time = game.get_time() + 0.55

    draw_frame(*FRAMES[frame_index])
    game.show_canvas()
