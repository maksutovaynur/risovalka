from risovalka.gamekit import Object, Point, Size, Vector, game


WINDOW_SIZE = Size(800, 520)
HERO_SIZE = Size(48, 48)
WALL_SIZE = Size(170, 90)


def main():
    game.set_window_title("Урок 2: игровой цикл и ввод")
    game.set_window_size(WINDOW_SIZE.width, WINDOW_SIZE.height)
    game.open()
    game.set_stroke_color("transparent")

    world = create_world()

    while not game.is_close_clicked():
        update_world(world)
        draw_world(world)
        game.show_canvas()


def create_world():
    return Object(
        hero=Object(position=Point(100, 220), size=HERO_SIZE, speed=260),
        wall=Object(position=Point(350, 210), size=WALL_SIZE),
        last_block="нет",
    )


def update_world(world):
    dt = game.get_delta_time()
    old_position = Point(world.hero.position.x, world.hero.position.y)
    direction = read_direction()

    if direction.size() > 0:
        direction = direction / direction.size()
        world.hero.position += direction * world.hero.speed * dt

    keep_inside_window(world.hero)

    if rectangles_touch(world.hero, world.wall):
        world.hero.position = old_position
        world.last_block = "стена"
    elif is_on_window_edge(world.hero):
        world.last_block = "край экрана"
    else:
        world.last_block = "нет"


def read_direction():
    direction = Vector(0, 0)

    if game.is_key_down("left") or game.is_key_down("a"):
        direction.x -= 1
    if game.is_key_down("right") or game.is_key_down("d"):
        direction.x += 1
    if game.is_key_down("up") or game.is_key_down("w"):
        direction.y -= 1
    if game.is_key_down("down") or game.is_key_down("s"):
        direction.y += 1

    return direction


def keep_inside_window(hero):
    hero.position.x = max(0, min(hero.position.x, game.window_size.width - hero.size.width))
    hero.position.y = max(0, min(hero.position.y, game.window_size.height - hero.size.height))


def is_on_window_edge(hero):
    return (
        hero.position.x == 0
        or hero.position.y == 0
        or hero.position.x == game.window_size.width - hero.size.width
        or hero.position.y == game.window_size.height - hero.size.height
    )


def rectangles_touch(first, second):
    return (
        first.position.x < second.position.x + second.size.width
        and first.position.x + first.size.width > second.position.x
        and first.position.y < second.position.y + second.size.height
        and first.position.y + first.size.height > second.position.y
    )


def draw_world(world):
    game.set_fill_color("#182033")
    game.clear_canvas()

    game.set_fill_color("#243b55")
    game.draw_rectangle(0, 0, game.window_size.width, game.window_size.height)

    game.set_fill_color("#5eead4")
    game.draw_rectangle(world.hero.position, world.hero.size)

    game.set_fill_color("#fb7185")
    game.draw_rectangle(world.wall.position, world.wall.size)

    game.set_fill_color("white")
    game.draw_text("Стрелки или WASD: двигаться", Point(24, 24), 24)
    game.draw_text(f"Блок: {world.last_block}", Point(24, 56), 22)


if __name__ == "__main__":
    main()
