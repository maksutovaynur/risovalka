---
marp: true
theme: default
paginate: true
size: 16:9
---

<style>
.grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-top: 54px;
}
.big-card {
  border: 4px solid #1d4ed8;
  border-radius: 14px;
  padding: 42px;
  min-height: 130px;
  background: #e0f2fe;
  font-size: 38px;
  font-weight: 800;
}
.achievement-map,
.code-map {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-top: 68px;
}
.achievement-map span,
.code-map span {
  background: #fff7ed;
  border: 4px solid #f97316;
  border-radius: 12px;
  padding: 36px 28px;
  font-size: 36px;
  text-align: center;
  font-weight: 800;
}
.pipeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-top: 98px;
}
.pipeline div {
  background: #dcfce7;
  border: 4px solid #16a34a;
  border-radius: 12px;
  padding: 40px 18px;
  min-height: 116px;
  font-size: 32px;
  text-align: center;
  font-weight: 800;
}
.diagram-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
  margin-top: 76px;
}
.formula {
  background: #eef2ff;
  border-left: 14px solid #6366f1;
  padding: 28px 34px;
  font-family: ui-monospace, Consolas, monospace;
  font-size: 44px;
}
.variable-box {
  width: 560px;
  margin: 78px auto 0;
  border: 6px solid #1d4ed8;
  border-radius: 18px;
  overflow: hidden;
  text-align: center;
}
.variable-box b {
  display: block;
  background: #dbeafe;
  padding: 36px;
  font-size: 64px;
}
.variable-box span {
  display: block;
  background: white;
  padding: 48px;
  font-size: 92px;
  font-weight: 900;
}
</style>

<!-- _class: lead -->

# P1. Рисуем первый игровой мир

![bg right:56% contain](images/scene_goal.png)

Окно, координаты, фигуры, картинки и первые кадры.

---

# Что сделаем сегодня

<div class="grid-2">
<div class="big-card">1. Откроем окно игры</div>
<div class="big-card">2. Поставим объекты по координатам</div>
<div class="big-card">3. Проверим порядок рисования</div>
<div class="big-card">4. Соберём первые кадры движения</div>
</div>

---

# С чего начнём

![bg right:56% contain](images/scene_goal.png)

Сегодня мы впервые заставим компьютер нарисовать наш игровой мир.

Поменял число — объект переехал.

Поменял цвет — сцена стала другой.

---

# Окно игры

![bg right:58% contain](images/project_parts.png)

Окно — это сцена.

В нём живут фон, герои, предметы, эффекты и текст.

---

# Практический результат

<div class="achievement-map">
<span>окно</span>
<span>фон</span>
<span>герой</span>
<span>цвета</span>
<span>координаты</span>
<span>первые кадры</span>
</div>

Идеи для выбора: `lessons/lesson1/achivements.md`

---

# Экран как лист в клетку

![bg right:58% contain](images/coordinate_grid.png)

Чтобы поставить объект, компьютеру нужен адрес.

Этот адрес — координаты `x` и `y`.

---

# Координаты

![bg right:58% contain](images/coordinate_grid.png)

`x` — вправо.

`y` — вниз.

Начало — левый верхний угол.

---

# Фигуры — строительные блоки

<div class="code-map">
<span>круг</span>
<span>прямоугольник</span>
<span>линия</span>
<span>картинка</span>
<span>текст</span>
<span>фон</span>
</div>

Из простых деталей собирается игровая сцена.

---

# Первые команды gamekit

<div class="code-map">
<span>set_window_size</span>
<span>set_fill_color</span>
<span>clear_canvas</span>
<span>draw_circle</span>
<span>draw_rectangle</span>
<span>draw_text</span>
<span>show_canvas</span>
</div>

Это наши первые инструменты для рисования.

---

# Растр

![bg right:58% contain](images/raster_pixels.png)

Экран — сетка маленьких квадратиков.

Квадратик называется **пиксель**.

---

# Цвет как рецепт

![bg right:58% contain](images/rgb_recipe.png)

RGB:

- R — красный;
- G — зелёный;
- B — синий.

Сначала хватит готовых имён цветов.

RGB и HEX — секретный уровень для точной настройки.

---

# Картинки из файлов

![bg right:56% contain](images/final_showcase.png)

В игре можно рисовать не только фигуры.

Герой, монета, фон или значок могут быть обычными картинками из файлов.

---

# Вектор

![bg right:58% contain](images/vector_arrow.png)

Вектор отвечает:

**куда** и **на сколько** сдвинуться.

---

# Порядок рисования

<div class="pipeline">
<div>нарисовать фон</div>
<div>нарисовать героя</div>
<div>нарисовать текст</div>
<div>показать</div>
</div>

Кто нарисован позже — тот сверху.

---

# Ошибка дня

![bg right:56% contain](images/draw_order_bug.png)

Фон нарисовали после героя.

Фон закрыл героя.

---

# Очистка экрана

<div class="pipeline">
<div>очистить</div>
<div>нарисовать новую картинку</div>
<div>показать</div>
<div>подождать</div>
</div>

Если не очищать экран, объект оставит след.

Иногда это ошибка. Иногда — интересный эффект.

---

# Первые кадры

<div class="pipeline">
<div>кадр 1</div>
<div>кадр 2</div>
<div>кадр 3</div>
<div>движение</div>
</div>

Объект не «едет» сам.

Мы быстро показываем несколько картинок подряд.

---

# Зачем нужен sleep

`sleep` делает паузу.

Без паузы кадр промелькнёт слишком быстро.

Сегодня это мультфильм руками.

Настоящий игровой цикл — на следующем занятии.

---

# Практика: готовые примеры

Открываем:

- `lessons/lesson1/samples/01_first_scene.py`
- `lessons/lesson1/samples/02_color_recipes.py`
- `lessons/lesson1/samples/03_coordinate_map.py`
- `lessons/lesson1/samples/04_vectors.py`
- `lessons/lesson1/samples/05_manual_animation.py`
- `lessons/lesson1/samples/06_repeated_object.py`
- `lessons/lesson1/samples/07_example_use_function.py`

---

# Зачем потом понадобятся свои команды

Откройте `06_repeated_object.py`.

Один и тот же робот нарисован несколько раз.

Код повторяется. Позже мы научимся превращать такой повтор в свою команду.

---

# Как выглядит решение

Откройте `07_example_use_function.py`.

Повторяющийся робот спрятан в одну команду:

`draw_robot(120, 210)`

---

# Практика: задания-поломки

Почините:

- `lessons/lesson1/puzzles/01_invisible_scene.py`
- `lessons/lesson1/puzzles/02_python_messages.py`
- `lessons/lesson1/puzzles/03_animation_too_fast.py`
- `lessons/lesson1/puzzles/04_traces_or_bug.py`
- `lessons/lesson1/puzzles/05_background_covers_hero.py`
- `lessons/lesson1/puzzles/06_missing_picture.py`

---

# Финальный показ

![bg right:58% contain](images/final_showcase.png)

Покажите свой мир и ответьте:

**что вы изменили сами?**

---

# После урока

1. Открой инструкцию: `lessons/lesson1/lesson1_guide.md`.
2. Повтори запуск примера.
3. Выбери 2 достижения.
4. Исправь 1 задание-поломку.
