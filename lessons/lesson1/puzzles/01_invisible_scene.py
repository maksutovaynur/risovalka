from risovalka.gamekit import game


game.set_window_title("Задание 1: почему ничего не видно")
game.set_window_size(800, 600)
game.open()

# Проблема: на экране должна быть сцена с героем и монетой, но она почти пустая.
# Подсказка: проверь порядок команд и координаты монеты.
game.set_fill_color("#6f5cff")
game.draw_circle(400, 300, 50)

game.set_fill_color("yellow")
game.draw_circle(420, 720, 35)

game.set_fill_color("#102030")
game.clear_canvas()

game.show_canvas()
game.wait_close()
