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
  gap: 26px;
  margin-top: 40px;
}
.big-card {
  border: 4px solid #1d4ed8;
  border-radius: 14px;
  padding: 34px;
  min-height: 105px;
  background: #e0f2fe;
  font-weight: 800;
}
.achievement-map,
.code-map {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 55px;
}
.achievement-map span,
.code-map span {
  background: #fff7ed;
  border: 4px solid #f97316;
  border-radius: 12px;
  padding: 26px;
  text-align: center;
  font-weight: 800;
}
.pipeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 85px;
}
.pipeline div {
  background: #dcfce7;
  border: 4px solid #16a34a;
  border-radius: 12px;
  padding: 30px 18px;
  min-height: 85px;
  text-align: center;
  font-weight: 800;
}
.diagram-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 22px;
  margin-top: 60px;
}
.formula {
  background: #eef2ff;
  border-left: 14px solid #6366f1;
  padding: 20px 28px;
  font-family: ui-monospace, Consolas, monospace;
  font-size: 36px;
}
.variable-box {
  width: 430px;
  margin: 85px auto 0;
  border: 6px solid #1d4ed8;
  border-radius: 18px;
  overflow: hidden;
  text-align: center;
}
.variable-box b {
  display: block;
  background: #dbeafe;
  padding: 28px;
  font-size: 54px;
}
.variable-box span {
  display: block;
  background: white;
  padding: 38px;
  font-size: 78px;
  font-weight: 900;
}
</style>

<!-- _class: lead -->

# Урок 1. Экран оживает

![bg right:50%](images/scene_goal.png)

Тема занятия: **«Экран оживает»**.

Пишем первую игровую сцену и небольшую покадровую анимацию.

---

# План на сегодня

<div class="grid-2">
<div class="big-card">1. Запустим проект на Python</div>
<div class="big-card">2. Нарисуем сцену</div>
<div class="big-card">3. Поймём пиксели, цвет, координаты</div>
<div class="big-card">4. Исправим первые ошибки</div>
</div>

---

# Проект урока

![bg right:52%](images/project_parts.png)

**Обязательная часть**

- окно игры;
- фон;
- 3+ объекта;
- заголовок;
- 3 кадра покадровой анимации.

---

# Где будет ваша часть?

<div class="achievement-map">
<span>цвета</span>
<span>координаты</span>
<span>секретный объект</span>
<span>забавная ошибка</span>
<span>своя тема</span>
<span>мини-мультфильм</span>
</div>

Идеи для выбора: `lessons/lesson1/achivements.md`

---

# Почему программирование важно

![bg right:50%](images/input_program_output.png)

Игра — это диалог:

**действие игрока → правила → новый экран**

---

# Компьютер не догадывается

<div class="pipeline">
<div>очистить</div>
<div>нарисовать фон</div>
<div>нарисовать героя</div>
<div>показать</div>
</div>

Порядок команд — часть результата.

---

# Ошибка дня

![bg right:50%](images/draw_order_bug.png)

Нарисовали героя.

Потом очистили экран.

Герой исчез.

---

# Растр

![bg right:52%](images/raster_pixels.png)

Экран — сетка маленьких квадратиков.

Квадратик называется **пиксель**.

---

# Цвет как рецепт

![bg right:52%](images/rgb_recipe.png)

RGB:

- R — красный;
- G — зелёный;
- B — синий.

---

# Координаты

![bg right:55%](images/coordinate_grid.png)

`x` идёт вправо.

`y` идёт вниз.

Начало — левый верхний угол.

---

# Вектор

![bg right:52%](images/vector_arrow.png)

Вектор отвечает:

**куда** и **на сколько** сдвинуться.

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

# Числа и арифметика

<div class="diagram-row">
<div class="formula">центр = ширина / 2</div>
<div class="formula">земля = высота - 90</div>
<div class="formula">звезда = x + 40</div>
</div>

Код считает координаты за нас.

---

# Переменные

<div class="variable-box">
<b>hero_x</b>
<span>320</span>
</div>

Имя помогает не искать число по всему файлу.

---

# Функции

<div class="pipeline">
<div>draw_sky()</div>
<div>draw_ground()</div>
<div>draw_hero()</div>
<div>draw_title()</div>
</div>

Функция — своя команда.

---

# Если останется время

<div class="grid-2">
<div class="big-card">`if`<br>если нажата кнопка</div>
<div class="big-card">`while`<br>повторяй кадры</div>
</div>

Подробно разберём на следующем уроке.

---

# Практика: готовые примеры

Открываем:

- `lessons/lesson1/samples/01_first_scene.py`
- `lessons/lesson1/samples/02_color_recipes.py`
- `lessons/lesson1/samples/03_coordinate_map.py`
- `lessons/lesson1/samples/04_vectors.py`
- `lessons/lesson1/samples/05_manual_animation.py`

---

# Практика: задания-поломки

Почините:

- `lessons/lesson1/puzzles/01_wrong_order.py`
- `lessons/lesson1/puzzles/02_name_mistake.py`
- `lessons/lesson1/puzzles/03_lost_object.py`
- `lessons/lesson1/puzzles/04_unknown_color.py`
- `lessons/lesson1/puzzles/05_missing_argument.py`

---

# Финальный показ

![bg right:52%](images/final_showcase.png)

Покажите сцену и ответьте:

**что вы изменили сами?**

---

# После урока

1. Открой инструкцию: `lessons/lesson1/lesson1_guide.md`.
2. Повтори запуск образца.
3. Выбери 2 достижения.
4. Исправь 1 задание-поломку.
