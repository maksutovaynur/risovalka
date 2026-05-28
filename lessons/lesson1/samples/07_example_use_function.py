from risovalka.gamekit import game


def draw_robot(x, y):
    game.set_fill_color("#44aaff")
    game.draw_rectangle(x, y, 80, 90)

    game.set_fill_color("#20242d")
    game.draw_circle(x + 22, y + 30, 8)
    game.draw_circle(x + 58, y + 30, 8)

    game.set_stroke_color("#20242d")
    game.set_stroke_width(4)
    game.draw_line((x, y + 95), (x - 30, y + 135))
    game.draw_line((x + 80, y + 95), (x + 110, y + 135))


game.set_window_title("Урок 1: своя команда")
game.set_window_size(800, 600)
game.open()

game.set_fill_color("#f4f8ff")
game.clear_canvas()
game.draw_text("Повтор решается своей командой", (40, 34), size=26, color="black")

draw_robot(120, 210)
draw_robot(340, 250)
draw_robot(560, 190)

game.draw_text("draw_robot меняет только место, а детали робота остаются внутри команды", (45, 500), size=20, color="#b45309")

game.wait_close()
