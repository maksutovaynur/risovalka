from risovalka.gamekit import Point, Vector, game


game.set_window_title("Урок 1: вектор")
game.set_window_size(800, 600)
game.open()

hero = Point(190, 360)
shift = Vector(280, -170)
target = hero + shift

game.set_fill_color("#101820")
game.clear_canvas()
game.draw_text("Вектор показывает сдвиг", (40, 34), size=30, color="white")

game.set_stroke_color("#ffd166")
game.set_stroke_width(5)
game.draw_line(hero, target)

game.set_fill_color("#6f5cff")
game.draw_circle(hero, 34)
game.draw_text("старт", (hero.x - 28, hero.y + 45), size=18, color="white")

game.set_fill_color("#4bb35f")
game.draw_circle(target, 34)
game.draw_text("старт + вектор", (target.x - 50, target.y - 62), size=18, color="white")

game.draw_text("Vector(280, -170)", (310, 260), size=22, color="#ffd166")

game.wait_close()
