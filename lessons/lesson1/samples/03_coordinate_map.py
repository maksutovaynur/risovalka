from risovalka.gamekit import game


game.set_window_title("Урок 1: карта координат")
game.set_window_size(800, 600)
game.open()

game.set_fill_color("white")
game.clear_canvas()
game.draw_text("Координаты: x вправо, y вниз", (30, 24), size=26, color="black")

game.set_stroke_color("#d0d7de")
game.set_stroke_width(1)

game.draw_line((100, 80), (100, 560))
game.draw_line((200, 80), (200, 560))
game.draw_line((300, 80), (300, 560))
game.draw_line((400, 80), (400, 560))
game.draw_line((500, 80), (500, 560))
game.draw_line((600, 80), (600, 560))
game.draw_line((700, 80), (700, 560))

game.draw_line((0, 100), (800, 100))
game.draw_line((0, 200), (800, 200))
game.draw_line((0, 300), (800, 300))
game.draw_line((0, 400), (800, 400))
game.draw_line((0, 500), (800, 500))

game.draw_text("100", (104, 84), size=14, color="gray")
game.draw_text("200", (204, 84), size=14, color="gray")
game.draw_text("300", (304, 84), size=14, color="gray")
game.draw_text("400", (404, 84), size=14, color="gray")
game.draw_text("500", (504, 84), size=14, color="gray")
game.draw_text("600", (604, 84), size=14, color="gray")
game.draw_text("700", (704, 84), size=14, color="gray")

hero_x = 320
hero_y = 280
game.set_fill_color("#6f5cff")
game.draw_circle(hero_x, hero_y, 36)
game.draw_text("герой (320, 280)", (hero_x + 45, hero_y - 12), size=18, color="black")

game.wait_close()
