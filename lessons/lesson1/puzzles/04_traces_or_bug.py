from risovalka.gamekit import game


game.set_window_title("Задание 4: след или ошибка")
game.set_window_size(800, 600)
game.open()

# Проблема: вместо чистого движения остаются следы.
# Подсказка: каждый новый кадр обычно начинается с очистки экрана.
game.set_fill_color("#20242d")
game.clear_canvas()
game.set_fill_color("#6f5cff")
game.draw_circle(170, 350, 38)
game.show_canvas()
game.sleep(0.5)

game.set_fill_color("#44aaff")
game.draw_circle(320, 290, 38)
game.show_canvas()
game.sleep(0.5)

game.set_fill_color("#4bb35f")
game.draw_circle(500, 340, 38)
game.wait_close()
