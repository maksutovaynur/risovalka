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
  margin-top: 45px;
}
.big-card {
  border: 4px solid #1d4ed8;
  border-radius: 14px;
  padding: 32px;
  min-height: 105px;
  background: #e0f2fe;
  font-weight: 800;
}
.pipeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 80px;
}
.pipeline div {
  background: #dcfce7;
  border: 4px solid #16a34a;
  border-radius: 12px;
  padding: 28px 16px;
  min-height: 82px;
  text-align: center;
  font-weight: 800;
}
.tool-map {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
  margin-top: 50px;
}
.tool-map span {
  background: #fff7ed;
  border: 4px solid #f97316;
  border-radius: 12px;
  padding: 24px;
  text-align: center;
  font-weight: 800;
}
</style>

<!-- _class: lead -->

# P0. Как код оживляет игры

![bg right:50%](images/p0_code_to_game.png)

Зачем понимать программирование в эпоху ИИ-агентов.

---

# Каждая игра начиналась с команд

![bg right:50%](images/p0_code_to_game.png)

Когда-то Minecraft, Roblox, навигатор и ИИ-бот были набором точных инструкций.

Сегодня мы начнём писать такие инструкции сами.

---

# Программы вокруг нас

![bg right:54%](images/p0_programs_around.png)

Смартфон, сайт, игра, робот, умная колонка, ИИ-помощник — всё это программы.

---

# Что делает компьютер

![bg right:54%](images/p0_input_process_output.png)

Он получает ввод, выполняет команды и показывает результат.

**ввод → обработка → вывод**

---

# Компьютер быстрый, но буквальный

<div class="grid-2">
<div class="big-card">Не угадывает</div>
<div class="big-card">Не додумывает</div>
<div class="big-card">Делает по порядку</div>
<div class="big-card">Ошибки превращает в подсказки</div>
</div>

---

# Программа — это инструкция

<div class="pipeline">
<div>сделай окно</div>
<div>нарисуй фон</div>
<div>поставь героя</div>
<div>покажи экран</div>
</div>

Похоже на рецепт, только для компьютера.

---

# Зачем нужны языки программирования

Язык программирования помогает говорить с компьютером достаточно точно.

Не «нарисуй красиво», а:

`нарисуй круг в точке (400, 300), радиус 50`

---

# Почему языков много

<div class="tool-map">
<span>игры</span>
<span>сайты</span>
<span>роботы</span>
<span>серверы</span>
<span>приложения</span>
<span>ИИ</span>
</div>

Как в мастерской: для разных задач нужны разные инструменты.

---

# Почему начинаем с игр

![bg right:50%](images/scene_goal.png)

В игре результат видно сразу.

Написал команду — увидел объект на экране.

---

# Ошибки — это не провал

![bg right:50%](images/draw_order_bug.png)

Если вышло странно, компьютер показывает, где мы с ним не договорились.

Иногда странность становится хорошей идеей.

---

# ИИ-агенты уже помогают писать код

![bg right:52%](images/p0_ai_driver.png)

Но человек всё равно выбирает цель, проверяет результат и управляет работой.

---

# Метафора с автомобилем

Автомобиль быстрее ходьбы и лошади.

Но водителю всё равно нужно понимать дорогу, правила и управление.

С ИИ так же: он помогает, но направление задаёт человек.

---

# Что будет на курсе

![bg right:54%](images/p0_course_path.png)

Рисуем → оживляем → управляем → добавляем правила → показываем свою игру.

---

# Сегодня начнём делать

<div class="grid-2">
<div class="big-card">окно</div>
<div class="big-card">экран</div>
<div class="big-card">координаты</div>
<div class="big-card">команды рисования</div>
</div>

Это подготовка к первой игровой сцене.

---

# Главная цель курса

![bg right:52%](images/final_showcase.png)

У каждого должен быть момент:

**«Смотрите, это сделал я»**

