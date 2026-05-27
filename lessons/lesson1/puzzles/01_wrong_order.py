import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


game.set_window_title("Задание 1: порядок команд")
game.set_window_size(800, 600)
game.open()

while not game.is_close_clicked():
    # Проблема: герой должен быть виден, но экран пустой.
    # Подсказка: проверь порядок очистки и рисования.
    game.set_fill_color("#6f5cff")
    game.draw_circle(400, 300, 50)

    game.set_fill_color("black")
    game.clear_canvas()

    game.show_canvas()
