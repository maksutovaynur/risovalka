import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


def draw_grid():
    game.set_fill_color("white")
    game.clear_canvas()
    game.draw_text("Координаты: x вправо, y вниз", (30, 24), size=26, color="black")

    game.set_stroke_color("#d0d7de")
    game.set_stroke_width(1)

    for x in range(0, 801, 100):
        game.draw_line((x, 80), (x, 560))
        game.draw_text(str(x), (x + 4, 84), size=14, color="gray")

    for y in range(100, 561, 100):
        game.draw_line((0, y), (800, y))
        game.draw_text(str(y), (8, y + 4), size=14, color="gray")

    hero_x = 320
    hero_y = 280
    game.set_fill_color("#6f5cff")
    game.draw_circle(hero_x, hero_y, 36)
    game.draw_text("герой (320, 280)", (hero_x + 45, hero_y - 12), size=18, color="black")


game.set_window_title("Урок 1: карта координат")
game.set_window_size(800, 600)
game.open()

# Сетка не меняется: по ней удобно проверять координаты.
while not game.is_close_clicked():
    draw_grid()
    game.show_canvas()
