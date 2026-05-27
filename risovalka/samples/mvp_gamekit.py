import random
from pathlib import Path

from risovalka.gamekit import Object, Point, Rotation, Size, Vector, game, geometry


PROJECT_ROOT = Path(__file__).resolve().parents[2]
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
        water=game.load_shader("water"),
    )


def create_world():
    return Object(
        hero=Object(position=Point(400, 260), angle=0, angular_speed=100, speed=180),
        targets=create_targets(),
        bullets=[],
        spark_trail=[],
        explosions=[],
        next_bullet_time=0,
        mouse=Point(0, 0),
    )


def create_targets():
    return [
        Object(
            points=geometry.generate_regular_polygon((0, 0), 48, 6),
            position=Point(160, 140),
            angle=12,
            color="orange",
        ),
        Object(
            points=[Point(-70, -45), Point(70, -45), Point(70, 45), Point(-70, 45)],
            position=Point(330, 135),
            angle=-8,
            color="#44aaffff",
        ),
        Object(
            points=geometry.generate_star((0, 0), 24, 56, 7),
            position=Point(610, 210),
            angle=0,
            color="#9f7affff",
        ),
    ]


def update_world(world):
    dt = game.get_delta_time()
    world.mouse = game.get_mouse_position()

    update_hero(world.hero, world.spark_trail, dt)
    update_sparks(world.spark_trail, dt)
    update_shooting(world)
    update_bullets(world.bullets, dt)
    resolve_bullet_collisions(world)
    update_explosions(world.explosions, dt)


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

    bullet = create_bullet(world.hero.position, world.mouse)
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


def update_bullets(bullets, dt):
    for bullet in bullets:
        bullet.position += bullet.velocity * dt
        bullet.age += dt

    bullets[:] = [bullet for bullet in bullets if is_bullet_alive(bullet)]


def is_bullet_alive(bullet):
    return (
        bullet.age < 1.6
        and -40 <= bullet.position.x <= game.window_size.width + 40
        and -40 <= bullet.position.y <= game.window_size.height + 40
    )


def resolve_bullet_collisions(world):
    remaining_bullets = []
    for bullet in world.bullets:
        target = find_hit_target(bullet, world.targets)
        if target is None:
            remaining_bullets.append(bullet)
            continue

        world.targets.remove(target)
        world.explosions.append(create_timed_effect(bullet.position))

    world.bullets[:] = remaining_bullets


def find_hit_target(bullet, targets):
    for target in targets:
        if is_point_inside_polygon(bullet.position, polygon_points(target)):
            return target
    return None


def update_explosions(explosions, dt):
    update_effects(explosions, dt)
    explosions[:] = [explosion for explosion in explosions if explosion.age < 0.5]


def update_effects(effects, dt):
    for effect in effects:
        effect.age += dt


def create_timed_effect(position):
    return Object(position=Point(position.x, position.y), age=0)


def draw_world(world, assets):
    assets.water.set_param("time", game.get_time())
    game.set_fill_shader(assets.water, size=(100, None))
    game.clear_canvas()

    draw_targets(world.targets)
    draw_sparks(world.spark_trail, assets.spark_images, world.hero.angle)
    draw_hero(world.hero, assets.star_texture)
    draw_bullets(world.bullets)
    draw_explosions(world.explosions, assets.explosion_images)
    draw_cursor(world.mouse, assets.target_image)
    draw_hud()


def draw_targets(targets):
    for target in targets:
        game.set_fill_color(target.color)
        game.draw_polygon(polygon_points(target))


def draw_sparks(spark_trail, spark_images, hero_angle):
    for spark in spark_trail:
        frame_index = animation_frame(spark.age, 0.09, spark_images)
        spark_size = 48 * (1 - spark.age / 0.45) + 10
        draw_centered_image(
            spark_images[frame_index],
            spark.position,
            Size(spark_size, spark_size),
            Rotation(hero_angle + spark.age * 360, spark.position),
        )


def draw_hero(hero, star_texture):
    game.set_fill_texture(
        star_texture,
        start_position=hero.position - Size(STAR_SIZE.width / 2, STAR_SIZE.height / 2),
        size=STAR_SIZE,
        rotation=Rotation(hero.angle, hero.position),
        repeat=False,
    )
    game.draw_polygon(moved_polygon(STAR_POLYGON, hero.position, hero.angle))


def draw_bullets(bullets):
    game.set_fill_color("#ffd34dff")
    for bullet in bullets:
        game.draw_circle(bullet.position, bullet.radius)


def draw_explosions(explosions, explosion_images):
    for explosion in explosions:
        frame_index = animation_frame(explosion.age, 0.125, explosion_images)
        explosion_size = 72 * (1 - explosion.age / 0.5) + 28
        draw_centered_image(
            explosion_images[frame_index],
            explosion.position,
            Size(explosion_size, explosion_size),
            Rotation(explosion.age * 500, explosion.position),
        )


def draw_cursor(mouse, target_image):
    draw_centered_image(target_image, mouse, Size(48, 48), Rotation(game.get_time() * 45, mouse))


def draw_hud():
    game.set_fill_color("white")
    game.draw_text(f"FPS: {game.get_fps():.0f}", Point(20, 20), size=18)
    game.draw_text("Стрелки двигают звезду, SPACE вращает, мышь стреляет", Point(20, 48), size=16)


def draw_centered_image(image, center, size, rotation):
    game.draw_image(image, center - Size(size.width / 2, size.height / 2), size, rotation)


def animation_frame(age, frame_duration, frames):
    return min(int(age / frame_duration), len(frames) - 1)


def polygon_points(target):
    return moved_polygon(target.points, target.position, target.angle)


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


if __name__ == "__main__":
    main()
