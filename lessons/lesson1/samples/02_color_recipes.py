from risovalka.gamekit import game


game.set_window_title("Урок 1: рецепты цвета")
game.set_window_size(800, 600)
game.open()

game.set_fill_color("#20242d")
game.clear_canvas()
game.draw_text("Цвет — это рецепт", (40, 34), size=30, color="white")

game.set_fill_color("red")
game.draw_rectangle(70, 150, 110, 170)
game.draw_text("red", (70, 335), size=20, color="white")

game.set_fill_color("green")
game.draw_rectangle(210, 150, 110, 170)
game.draw_text("green", (210, 335), size=20, color="white")

game.set_fill_color("blue")
game.draw_rectangle(350, 150, 110, 170)
game.draw_text("blue", (350, 335), size=20, color="white")

game.set_fill_color((255, 180, 40))
game.draw_rectangle(490, 150, 110, 170)
game.draw_text("RGB", (490, 335), size=20, color="white")

game.set_fill_color("#44aaff")
game.draw_rectangle(630, 150, 110, 170)
game.draw_text("HEX", (630, 335), size=20, color="white")

game.draw_text("Поменяй один цвет и запусти снова", (70, 450), size=22, color="#ffd166")

game.wait_close()
