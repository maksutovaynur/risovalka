from risovalka.gamekit import game


game.set_window_title("Задание 5: кто сверху")
game.set_window_size(800, 600)
game.open()

# Проблема: герой есть в коде, но его закрывает другой объект.
# Подсказка: кто нарисован позже, тот оказывается сверху.
game.set_fill_color("#6f5cff")
game.draw_circle(400, 300, 50)

game.set_fill_color("#86c5ff")
game.clear_canvas()
game.set_fill_color("#4bb35f")
game.draw_rectangle(0, 390, 800, 210)
game.set_fill_color("#86c5ff")
game.draw_rectangle(0, 0, 800, 390)

game.show_canvas()
game.wait_close()
