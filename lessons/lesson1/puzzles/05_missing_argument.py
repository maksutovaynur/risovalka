import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


game.set_window_title("Задание 5: не хватает значения")
game.set_window_size(800, 600)
game.open()

while not game.is_close_clicked():
    # Проблема: команда круга получила не всё, что ей нужно.
    # Подсказка: кругу нужны место и радиус.
    game.set_fill_color("#20242d")
    game.clear_canvas()
    game.set_fill_color("#4bb35f")
    game.draw_circle((400, 300))
    game.show_canvas()
