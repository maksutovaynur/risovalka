import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


game.set_window_title("Задание 4: неизвестный цвет")
game.set_window_size(800, 600)
game.open()

while not game.is_close_clicked():
    # Проблема: Python не принимает один из цветов.
    # Подсказка: попробуй имя из примера или HEX-запись.
    game.set_fill_color("skyblue")
    game.clear_canvas()
    game.set_fill_color("orange")
    game.draw_rectangle(250, 240, 300, 150)
    game.show_canvas()
