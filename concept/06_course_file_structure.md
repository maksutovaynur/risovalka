# 06. Структура файлов курса

## Рекомендуемая структура репозитория

```text
game-course/
  README.md
  docs/
  student_materials/
  teacher_materials/
  risovalka/
  sessions/
  assets/
  build/
  .vscode/
  pyproject.toml
  uv.lock
```

## `docs/`

Концептуальные документы курса.

## `lessons/`

Актуальные материалы занятий лежат в `lessons/`.

```text
lessons/
  setup_links.md
  lesson1/
    lesson1_slides.marp.md
    lesson1_slides.pdf
    lesson1_guide.md
    lesson1_guide.pdf
    achivements.md
    achivements.pdf
    samples/
    puzzles/
```

## `concept/presentations_legacy/`

Ранние презентации сохранены как legacy-архив идей. Новые материалы уроков не нужно добавлять в эту папку.

Старые исходники Marp и изображения:

```text
concept/presentations_legacy/
  P0_intro_programming.marp.md
  P1_session1_graphics.marp.md
  P2_session2_game_loop_input.marp.md
  theme/
    game-course.css
  images/
```

## `risovalka/`

Python-пакет проекта: учебный движок, вспомогательные инструменты и примеры.

```text
risovalka/
  __init__.py
  gamekit/
    __init__.py
    game.py
    entity.py
    drawing.py
    input.py
    collision.py
    camera.py
    effects.py
  tools/
    __init__.py
    raster/
      __init__.py
    vector/
      __init__.py
  samples/
    __init__.py
```

- `risovalka.gamekit` — учебный игровой движок.
- `risovalka.tools.raster` — bitmap/растровая рисовалка для ассетов.
- `risovalka.tools.vector` — векторная рисовалка с экспортом SVG и команд `game.draw_*`.
- `risovalka.samples` — примеры использования движка.

## `sessions/`

Материалы занятий и импортируемый пакет шаблонов сессий.

```text
sessions/
  __init__.py
  session_1/
  session_2/
  session_3/
  session_4/
```

## `assets/`

Библиотека ассетов: фоны, персонажи, предметы, эффекты, UI, шрифты, звуки.

## `.vscode/`

Готовые настройки, чтобы детям не приходилось конфигурировать проект руками.
