import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from risovalka.gamekit import game


game.set_window_title("Задание 3: потерянный объект")
game.set_window_size(800, 600)
game.open()

coin_x = 420
coin_y = 720

while not game.is_close_clicked():
    # Проблема: монета не видна на экране.
    # Подсказка: вспомни, куда направлена ось y.
    game.set_fill_color("#102030")
    game.clear_canvas()
    game.set_fill_color("yellow")
    game.draw_circle(coin_x, coin_y, 35)
    game.draw_text("Где монета?", (40, 40), size=28, color="white")
    game.show_canvas()
