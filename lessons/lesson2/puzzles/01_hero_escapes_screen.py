from risovalka.gamekit import Object, Point, Size, Vector, game


def main():
    game.set_window_title("Поломка: герой убегает за экран")
    game.set_window_size(760, 460)
    game.open()
    game.set_stroke_color("transparent")

    hero = Object(position=Point(320, 190), size=Size(52, 52), speed=300)

    while not game.is_close_clicked():
        update_hero(hero)
        draw_scene(hero)
        game.show_canvas()


def update_hero(hero):
    dt = game.get_delta_time()
    direction = Vector(0, 0)

    if game.is_key_down("left") or game.is_key_down("a"):
        direction.x -= 1
    if game.is_key_down("right") or game.is_key_down("d"):
        direction.x += 1
    if game.is_key_down("up") or game.is_key_down("w"):
        direction.y -= 1
    if game.is_key_down("down") or game.is_key_down("s"):
        direction.y += 1

    if direction.size() > 0:
        direction = direction / direction.size()
        hero.position += direction * hero.speed * dt

    # Поломка: герой может уйти за край экрана.
    # Подсказка: после движения нужно ограничить x и y размерами окна.


def draw_scene(hero):
    game.set_fill_color("#111827")
    game.clear_canvas()

    game.set_fill_color("#22c55e")
    game.draw_rectangle(hero.position, hero.size)

    game.set_fill_color("white")
    game.draw_text("Исправь: герой не должен уходить за экран", Point(24, 24), 22)


if __name__ == "__main__":
    main()
