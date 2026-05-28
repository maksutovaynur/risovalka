from risovalka.gamekit import game


HERO_IMAGE = "assets/brand/risovalka-mascot-logo.png"

game.set_window_title("Урок 1: первая сцена")
game.set_window_size(800, 600)
game.open()

hero_image = game.load_image(HERO_IMAGE)

game.set_fill_color("#86c5ff")
game.clear_canvas()

game.set_fill_color("#4bb35f")
game.draw_rectangle(0, 390, 800, 210)

game.set_fill_color("yellow")
game.draw_circle(680, 90, 52)

game.set_fill_color("#5b3a29")
game.draw_rectangle(155, 285, 80, 110)

game.set_fill_color("#ffcc66")
game.draw_polygon([(120, 285), (275, 285), (198, 210)])

game.draw_image(hero_image, (500, 250), size=(120, 120))
game.draw_text("Моя первая игровая сцена", (40, 36), size=28, color="white")

# Окно остаётся открытым после первого нарисованного кадра.
game.wait_close()
