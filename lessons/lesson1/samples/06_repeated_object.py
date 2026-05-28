from risovalka.gamekit import game


game.set_window_title("Урок 1: повторяем сложный объект")
game.set_window_size(800, 600)
game.open()

game.set_fill_color("#f4f8ff")
game.clear_canvas()
game.draw_text("Один и тот же робот в разных местах", (40, 34), size=26, color="black")

game.set_fill_color("#44aaff")
game.draw_rectangle(120, 210, 80, 90)
game.set_fill_color("#20242d")
game.draw_circle(142, 240, 8)
game.draw_circle(178, 240, 8)
game.set_stroke_color("#20242d")
game.set_stroke_width(4)
game.draw_line((120, 305), (90, 345))
game.draw_line((200, 305), (230, 345))

game.set_fill_color("#44aaff")
game.draw_rectangle(340, 250, 80, 90)
game.set_fill_color("#20242d")
game.draw_circle(362, 280, 8)
game.draw_circle(398, 280, 8)
game.set_stroke_color("#20242d")
game.set_stroke_width(4)
game.draw_line((340, 345), (310, 385))
game.draw_line((420, 345), (450, 385))

game.set_fill_color("#44aaff")
game.draw_rectangle(560, 190, 80, 90)
game.set_fill_color("#20242d")
game.draw_circle(582, 220, 8)
game.draw_circle(618, 220, 8)
game.set_stroke_color("#20242d")
game.set_stroke_width(4)
game.draw_line((560, 285), (530, 325))
game.draw_line((640, 285), (670, 325))

game.draw_text("Много повторов. Скоро узнаем, как сделать свою команду.", (70, 500), size=22, color="#b45309")

game.wait_close()
