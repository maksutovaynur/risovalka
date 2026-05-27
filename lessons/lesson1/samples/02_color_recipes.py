import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


COLORS = [
    ("red", "red"),
    ("green", "green"),
    ("blue", "blue"),
    ("RGB", (255, 180, 40)),
    ("HEX", "#44aaff"),
]


def draw_palette():
    game.set_fill_color("#20242d")
    game.clear_canvas()
    game.draw_text("Цвет — это рецепт", (40, 34), size=30, color="white")

    x = 70
    for name, color in COLORS:
        game.set_fill_color(color)
        game.draw_rectangle(x, 150, 110, 170)
        game.draw_text(name, (x, 335), size=20, color="white")
        x = x + 140

    game.draw_text("Поменяй числа RGB или HEX и запусти снова", (70, 450), size=22, color="#ffd166")


game.set_window_title("Урок 1: рецепты цвета")
game.set_window_size(800, 600)
game.open()

# Перерисовываем одну и ту же палитру, пока окно открыто.
while not game.is_close_clicked():
    draw_palette()
    game.show_canvas()
