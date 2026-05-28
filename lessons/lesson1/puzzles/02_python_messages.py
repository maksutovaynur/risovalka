from risovalka.gamekit import game


game.set_window_title("Задание 2: сообщения Python")
game.set_window_size(800, 600)
game.open()

hero_x = 360
hero_y = 300

# Проблема: программа останавливается. После одного исправления может появиться следующая ошибка.
# Подсказка: читай сообщение Python сверху вниз и исправляй по одному месту.
game.set_fill_color("skyblue")
game.clear_canvas()
game.set_fill_color("#ffd166")
game.draw_circle(herо_x, hero_y)
game.show_canvas()
