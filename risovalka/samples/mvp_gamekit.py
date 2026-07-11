import random

from risovalka.gamekit import Object, Point, Rotation, Size, Vector, file, game, geometry


CURRENT_FOLDER = file.get_current_folder()
PROJECT_ROOT = file.get_project_root_folder()
MASCOT_LOGO = PROJECT_ROOT / "assets" / "brand" / "risovalka-mascot-logo.png"
ASSET_ROOT = PROJECT_ROOT / "data" / "assets" / "kenney"
PARTICLE_ROOT = ASSET_ROOT / "particle-pack" / "PNG (Transparent)"

SPARK_IMAGE_PATHS = [
    PARTICLE_ROOT / "spark_01.png",
    PARTICLE_ROOT / "spark_02.png",
    PARTICLE_ROOT / "spark_03.png",
    PARTICLE_ROOT / "spark_04.png",
]
EXPLOSION_IMAGE_PATHS = [
    PARTICLE_ROOT / "flare_01.png",
    PARTICLE_ROOT / "fire_01.png",
    PARTICLE_ROOT / "fire_02.png",
    PARTICLE_ROOT / "smoke_01.png",
]
TARGET_IMAGE_PATH = ASSET_ROOT / "crosshair-pack" / "PNG" / "Black Retina" / "crosshair036.png"

STAR_SIZE = Size(180, 180)
STAR_POLYGON = geometry.generate_star((0, 0), 45, 90, 5)
MAX_ENEMIES = 8
HERO_HIT_RADIUS = 62


def main():
    assets = load_assets()
    world = create_world()

    game.set_window_title("Рисовалка: возможности gamekit")
    game.set_logo(assets.star_texture)
    game.open()
    game.set_stroke_color("transparent")

    while not game.is_close_clicked():
        update_world(world)
        draw_world(world, assets)
        game.show_canvas()


def load_assets():
    return Object(
        star_texture=game.load_image(MASCOT_LOGO),
        spark_images=[game.load_image(path) for path in SPARK_IMAGE_PATHS],
        explosion_images=[game.load_image(path) for path in EXPLOSION_IMAGE_PATHS],
        target_image=game.load_image(TARGET_IMAGE_PATH),
        shader=game.load_shader("space"),
    )


def create_world():
    world = Object(
        hero=Object(position=Point(0, 0), angle=0, angular_speed=100, speed=180),
        enemies=[],
        bullets=[],
        spark_trail=[],
        explosions=[],
        next_bullet_time=0,
        next_enemy_time=1.0,
        started_at=game.get_time(),
        score=0,
        game_over=False,
        mouse=Point(0, 0),
        mouse_world=Point(0, 0),
    )
    world.enemies = [create_enemy(world) for _ in range(5)]
    return world


def create_enemy(world):
    spawn_margin = 120
    viewport = camera_viewport(world)
    side = random.choice(["left", "right", "top", "bottom"])
    if side == "left":
        position = Point(viewport.left - spawn_margin, random.uniform(viewport.top, viewport.bottom))
    elif side == "right":
        position = Point(viewport.right + spawn_margin, random.uniform(viewport.top, viewport.bottom))
    elif side == "top":
        position = Point(random.uniform(viewport.left, viewport.right), viewport.top - spawn_margin)
    else:
        position = Point(random.uniform(viewport.left, viewport.right), viewport.bottom + spawn_margin)

    shape = random.choice(["hex", "box", "star"])
    if shape == "hex":
        points = geometry.generate_regular_polygon((0, 0), 48, 6)
        color = "orange"
    elif shape == "box":
        points = [Point(-56, -40), Point(56, -40), Point(56, 40), Point(-56, 40)]
        color = "#44aaffff"
    else:
        points = geometry.generate_star((0, 0), 24, 56, 7)
        color = "#9f7affff"

    return Object(
        points=points,
        position=position,
        angle=random.uniform(0, 360),
        spin=random.uniform(-45, 45),
        speed=random.uniform(35, 72),
        color=color,
    )


def update_world(world):
    dt = game.get_delta_time()
    world.mouse = game.get_mouse_position()
    world.mouse_world = screen_to_world(world, world.mouse)

    if world.game_over:
        update_explosions(world.explosions, dt)
        return

    world.score = game.get_time() - world.started_at
    update_hero(world.hero, world.spark_trail, dt)
    update_enemies(world, dt)
    update_sparks(world.spark_trail, dt)
    update_shooting(world)
    update_bullets(world, dt)
    resolve_bullet_collisions(world)
    resolve_hero_collision(world)
    update_explosions(world.explosions, dt)


def update_enemies(world, dt):
    if len(world.enemies) < MAX_ENEMIES and game.get_time() >= world.next_enemy_time:
        world.enemies.append(create_enemy(world))
        world.next_enemy_time = game.get_time() + random.uniform(0.65, 1.35)

    for enemy in world.enemies:
        direction = world.hero.position - enemy.position
        if direction.size() > 0:
            enemy.position += direction / direction.size() * enemy.speed * dt
        enemy.angle += enemy.spin * dt


def update_hero(hero, spark_trail, dt):
    velocity_direction = read_movement_direction()
    if velocity_direction.size() > 0:
        hero.position += velocity_direction / velocity_direction.size() * hero.speed * dt
        spark_trail.append(create_timed_effect(hero.position))

    if game.is_key_down("space"):
        hero.angle += dt * hero.angular_speed


def read_movement_direction():
    direction = Vector(0, 0)
    if game.is_key_down("left"):
        direction.x = -1
    elif game.is_key_down("right"):
        direction.x = 1

    if game.is_key_down("up"):
        direction.y = -1
    elif game.is_key_down("down"):
        direction.y = 1

    return direction


def update_sparks(spark_trail, dt):
    update_effects(spark_trail, dt)
    spark_trail[:] = [spark for spark in spark_trail if spark.age < 0.45][-16:]


def update_shooting(world):
    if not game.is_mouse_down("left") or game.get_time() < world.next_bullet_time:
        return

    bullet = create_bullet(world.hero.position, world.mouse_world)
    if bullet is None:
        return

    world.bullets.append(bullet)
    world.next_bullet_time = game.get_time() + 0.08


def create_bullet(hero_position, mouse_position):
    start_position = hero_position + random_vector(-12, 12)
    target_position = mouse_position + random_vector(-10, 10)
    direction = target_position - start_position
    if direction.size() == 0:
        return None

    direction = direction / direction.size()
    direction = direction @ random.uniform(-8, 8)
    return Object(
        position=start_position,
        velocity=direction * random.uniform(390, 520),
        age=0,
        radius=random.uniform(4, 7),
    )


def update_bullets(world, dt):
    for bullet in world.bullets:
        bullet.position += bullet.velocity * dt
        bullet.age += dt

    world.bullets[:] = [bullet for bullet in world.bullets if is_bullet_alive(world, bullet)]


def is_bullet_alive(world, bullet):
    viewport = camera_viewport(world, margin=80)
    return (
        bullet.age < 1.6
        and viewport.left <= bullet.position.x <= viewport.right
        and viewport.top <= bullet.position.y <= viewport.bottom
    )


def resolve_bullet_collisions(world):
    remaining_bullets = []
    for bullet in world.bullets:
        enemy = find_hit_enemy(bullet, world.enemies)
        if enemy is None:
            remaining_bullets.append(bullet)
            continue

        world.enemies.remove(enemy)
        world.explosions.append(create_timed_effect(bullet.position))

    world.bullets[:] = remaining_bullets


def find_hit_enemy(bullet, enemies):
    for enemy in enemies:
        if is_point_inside_polygon(bullet.position, polygon_points(enemy)):
            return enemy
    return None


def resolve_hero_collision(world):
    for enemy in world.enemies:
        if (enemy.position - world.hero.position).size() <= HERO_HIT_RADIUS:
            world.game_over = True
            world.score = game.get_time() - world.started_at
            world.explosions.append(create_timed_effect(world.hero.position))
            return


def update_explosions(explosions, dt):
    update_effects(explosions, dt)
    explosions[:] = [explosion for explosion in explosions if explosion.age < 0.5]


def update_effects(effects, dt):
    for effect in effects:
        effect.age += dt


def create_timed_effect(position):
    return Object(position=Point(position.x, position.y), age=0)


def draw_world(world, assets):
    assets.shader.set_param("time", game.get_time())
    game.set_fill_shader(assets.shader, start_position=background_start_position(world))
    game.clear_canvas()

    draw_enemies(world)
    draw_sparks(world, assets.spark_images)
    draw_hero(world, assets.star_texture)
    draw_bullets(world)
    draw_explosions(world, assets.explosion_images)
    draw_cursor(world.mouse, assets.target_image)
    draw_hud(world)
    if world.game_over:
        draw_game_over(world.score)


def draw_enemies(world):
    for enemy in world.enemies:
        game.set_fill_color(enemy.color)
        game.draw_polygon(polygon_points(enemy, world_to_screen(world, enemy.position)))


def draw_sparks(world, spark_images):
    for spark in world.spark_trail:
        frame_index = animation_frame(spark.age, 0.09, spark_images)
        spark_size = 48 * (1 - spark.age / 0.45) + 10
        screen_position = world_to_screen(world, spark.position)
        draw_centered_image(
            spark_images[frame_index],
            screen_position,
            Size(spark_size, spark_size),
            Rotation(world.hero.angle + spark.age * 360, screen_position),
        )


def draw_hero(world, star_texture):
    hero = world.hero
    screen_position = screen_center()
    game.set_fill_texture(
        star_texture,
        start_position=screen_position - Size(STAR_SIZE.width / 2, STAR_SIZE.height / 2),
        size=STAR_SIZE,
        rotation=Rotation(hero.angle, screen_position),
        repeat=False,
    )
    game.draw_polygon(moved_polygon(STAR_POLYGON, screen_position, hero.angle))


def draw_bullets(world):
    game.set_fill_color("#ffd34dff")
    for bullet in world.bullets:
        game.draw_circle(world_to_screen(world, bullet.position), bullet.radius)


def draw_explosions(world, explosion_images):
    for explosion in world.explosions:
        frame_index = animation_frame(explosion.age, 0.125, explosion_images)
        explosion_size = 72 * (1 - explosion.age / 0.5) + 28
        screen_position = world_to_screen(world, explosion.position)
        draw_centered_image(
            explosion_images[frame_index],
            screen_position,
            Size(explosion_size, explosion_size),
            Rotation(explosion.age * 500, screen_position),
        )


def draw_cursor(mouse, target_image):
    draw_centered_image(target_image, mouse, Size(48, 48), Rotation(game.get_time() * 45, mouse))


def draw_hud(world):
    game.set_fill_color("white")
    game.draw_text(f"Очки: {world.score:.1f}", Point(20, 20), size=24)
    game.draw_text(f"FPS: {game.get_fps():.0f}", Point(20, 52), size=16)
    game.draw_text("Стрелки двигают звезду, SPACE вращает, мышь стреляет", Point(20, 76), size=16)


def draw_game_over(score):
    game.draw_text(f"Вы проиграли! Очков {score:.1f}", Point(170, 250), size=42, color="red")
    game.draw_text("Закройте окно и запустите снова", Point(230, 310), size=24, color="white")


def draw_centered_image(image, center, size, rotation):
    game.draw_image(image, center - Size(size.width / 2, size.height / 2), size, rotation)


def animation_frame(age, frame_duration, frames):
    return min(int(age / frame_duration), len(frames) - 1)


def polygon_points(target, position=None):
    return moved_polygon(target.points, position or target.position, target.angle)


def moved_polygon(points, position, angle=0):
    return geometry.move_polygon(geometry.rotate_polygon(points, angle), position)


def is_point_inside_polygon(point, polygon):
    inside = False
    previous = polygon[-1]
    for current in polygon:
        crosses_y = (current.y > point.y) != (previous.y > point.y)
        if crosses_y:
            edge_x = (previous.x - current.x) * (point.y - current.y) / (previous.y - current.y) + current.x
            if point.x < edge_x:
                inside = not inside
        previous = current
    return inside


def random_vector(min_value, max_value):
    return Vector(random.uniform(min_value, max_value), random.uniform(min_value, max_value))


def screen_center():
    return Point(game.window_size.width / 2, game.window_size.height / 2)


def world_to_screen(world, point):
    return screen_center() + (point - world.hero.position)


def screen_to_world(world, point):
    return world.hero.position + (point - screen_center())


def camera_viewport(world, margin=0):
    center = screen_center()
    return Object(
        left=world.hero.position.x - center.x - margin,
        right=world.hero.position.x + center.x + margin,
        top=world.hero.position.y - center.y - margin,
        bottom=world.hero.position.y + center.y + margin,
    )


def background_start_position(world):
    return Point(-world.hero.position.x, -world.hero.position.y)


if __name__ == "__main__":
    main()
