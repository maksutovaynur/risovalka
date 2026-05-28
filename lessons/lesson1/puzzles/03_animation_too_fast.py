from risovalka.gamekit import game


game.set_window_title("Задание 3: почему виден только конец")
game.set_window_size(800, 600)
game.open()

# Проблема: мяч должен ехать по трём кадрам, но виден почти только финал.
# Подсказка: человеку нужно время, чтобы увидеть каждый кадр.
game.set_fill_color("#20242d")
game.clear_canvas()
game.set_fill_color("#6f5cff")
game.draw_circle(170, 350, 38)
game.show_canvas()

game.set_fill_color("#20242d")
game.clear_canvas()
game.set_fill_color("#44aaff")
game.draw_circle(320, 290, 38)
game.show_canvas()

game.set_fill_color("#20242d")
game.clear_canvas()
game.set_fill_color("#4bb35f")
game.draw_circle(500, 340, 38)
game.wait_close()
