# 06. Структура файлов курса

## Рекомендуемая структура репозитория

```text
game-course/
  README.md
  docs/
  presentations/
  student_materials/
  teacher_materials/
  engine/
  examples/
  sessions/
  assets/
  tools/
  build/
  .vscode/
  pyproject.toml
  uv.lock
```

## `docs/`

Концептуальные документы курса.

## `presentations/`

Исходники Marp и изображения.

```text
presentations/
  P0_intro_programming.marp.md
  P1_session1_graphics.marp.md
  P2_session2_game_loop_input.marp.md
  theme/
    game-course.css
  images/
```

## `engine/`

Учебный игровой движок.

```text
engine/
  gamekit/
    __init__.py
    game.py
    entity.py
    drawing.py
    input.py
    collision.py
    camera.py
    effects.py
```

## `sessions/`

Материалы занятий.

```text
sessions/
  session_1/
  session_2/
  session_3/
  session_4/
```

## `assets/`

Библиотека ассетов: фоны, персонажи, предметы, эффекты, UI, шрифты, звуки.

## `tools/`

Вспомогательные редакторы:

- bitmap-рисовалка;
- редактор спрайтов;
- векторная рисовалка;
- генератор achievements/leaderboard;
- экспорт материалов.

## `.vscode/`

Готовые настройки, чтобы детям не приходилось конфигурировать проект руками.
