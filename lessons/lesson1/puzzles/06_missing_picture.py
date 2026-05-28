from risovalka.gamekit import game


game.set_window_title("Задание 6: картинка не загрузилась")
game.set_window_size(800, 600)
game.open()

# Проблема: сцена должна показать героя-картинку, но программа не находит файл.
# Подсказка: проверь путь к файлу и имя папки.
hero_image = game.load_image("asset/brand/risovalka-mascot-logo.png")

game.set_fill_color("#86c5ff")
game.clear_canvas()
game.draw_image(hero_image, (340, 220), size=(140, 140))
game.draw_text("Герой из файла", (40, 40), size=28, color="white")
game.wait_close()
