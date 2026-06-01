from risovalka.gamekit import game, geometry_tools

game.open()

star = geometry_tools.generate_star((200, 200), 20, 100, 8)

уголПоворота = 0
while not game.is_close_clicked():
    dt = game.get_delta_time()
    уголПоворота += 100 * dt
    game.set_fill_color("yellow")
    game.clear_canvas()
    game.set_fill_color("green")
    star_rotated = geometry_tools.rotate_polygon(star, уголПоворота, (200, 200))
    game.draw_polygon(star_rotated)
    game.show_canvas()
    game.set_window_title(f'Частота кадров: {game.get_fps():.0f}')
    game.sleep(0.01)

# game.wait_close()