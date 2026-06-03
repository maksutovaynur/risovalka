from risovalka.gamekit import game, Point, Rotation

game.set_window_title('Всем привет, я прогрооомммист (Айнур)')
game.set_window_size(1000, 600)
game.open()

start_time = game.get_time()

for i in range(100):
    if game.is_close_clicked():
        break
    game.set_fill_color('white')
    game.clear_canvas()
    game.draw_text(f'Привет, {game.is_close_clicked()}', (450, 250), size=20, rotation=Rotation(i), color="black")
    game.show_canvas()
    game.sleep(0.02)

end_time = game.get_time()

game.draw_text(f'Всего длительность анимации: {end_time - start_time}', (0, 0), color='black')
game.show_canvas()

game.wait_close()