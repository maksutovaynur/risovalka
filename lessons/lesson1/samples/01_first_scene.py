import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


def draw_scene():
    game.set_fill_color("#86c5ff")
    game.clear_canvas()

    game.set_fill_color("#4bb35f")
    game.draw_rectangle(0, 390, 800, 210)

    game.set_fill_color("yellow")
    game.draw_circle(680, 90, 52)

    game.set_fill_color("#5b3a29")
    game.draw_rectangle(155, 285, 80, 110)

    game.set_fill_color("#ffcc66")
    game.draw_polygon([(120, 285), (275, 285), (198, 210)])

    game.set_fill_color("#6f5cff")
    game.draw_circle(430, 310, 42)

    game.draw_text("Моя первая игровая сцена", (40, 36), size=28, color="white")


game.set_window_title("Урок 1: первая сцена")
game.set_window_size(800, 600)
game.open()

# Этот цикл держит окно открытым и заново рисует сцену.
while not game.is_close_clicked():
    draw_scene()
    game.show_canvas()
