import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


game.set_window_title("Задание 2: имя переменной")
game.set_window_size(800, 600)
game.open()

hero_x = 360
hero_y = 300

while not game.is_close_clicked():
    # Проблема: программа падает до появления героя.
    # Подсказка: внимательно сравни имена переменных.
    game.set_fill_color("#20242d")
    game.clear_canvas()
    game.set_fill_color("#ffd166")
    game.draw_circle(herо_x, hero_y, 45)
    game.show_canvas()
