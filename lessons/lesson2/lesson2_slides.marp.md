---
marp: true
theme: default
paginate: true
size: 16:9
---

<style>
section {
  font-family: Arial, sans-serif;
}
.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
  margin-top: 48px;
}
.card {
  background: #e0f2fe;
  border: 4px solid #0284c7;
  border-radius: 10px;
  padding: 30px;
  min-height: 100px;
  font-size: 34px;
  font-weight: 800;
  text-align: center;
}
.loop {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
  margin-top: 84px;
}
.loop div {
  background: #dcfce7;
  border: 4px solid #16a34a;
  border-radius: 10px;
  padding: 34px 14px;
  min-height: 115px;
  font-size: 30px;
  font-weight: 800;
  text-align: center;
}
.code {
  background: #111827;
  color: white;
  border-radius: 10px;
  padding: 30px;
  font-family: Consolas, monospace;
  font-size: 34px;
  line-height: 1.45;
  margin-top: 46px;
  white-space: nowrap;
}
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 42px;
  margin-top: 42px;
}
.screen {
  height: 330px;
  border: 8px solid #1f2937;
  border-radius: 12px;
  position: relative;
  background: #dbeafe;
}
.hero {
  width: 74px;
  height: 74px;
  position: absolute;
  left: 96px;
  top: 130px;
  background: #14b8a6;
  border-radius: 8px;
}
.wall {
  width: 150px;
  height: 90px;
  position: absolute;
  left: 310px;
  top: 120px;
  background: #fb7185;
  border-radius: 8px;
}
.arrow {
  font-size: 68px;
  text-align: center;
  margin-top: 124px;
  color: #1d4ed8;
}
.formula {
  background: #fef3c7;
  border-left: 14px solid #f59e0b;
  padding: 28px;
  margin-top: 70px;
  font-family: Consolas, monospace;
  font-size: 40px;
  white-space: nowrap;
}
.nowrap {
  white-space: nowrap;
}
</style>

<!-- _class: lead -->

# P2. Игровой цикл и ввод

Герой двигается, клавиши работают, экран обновляется сам.

---

# Что сделаем сегодня

<div class="cards">
<div class="card">запустим игровой цикл</div>
<div class="card">прочитаем клавиатуру</div>
<div class="card">двинем героя</div>
<div class="card">не пустим героя за экран</div>
</div>

---

# Почему не руками

В прошлый раз можно было показать несколько кадров вручную.

Но настоящая игра должна сама повторять кадры много раз в секунду.

<div class="formula">кадр + кадр + кадр + ... = движение</div>

---

# Сердце игры

<div class="loop">
<div>Input<br>ввод</div>
<div>Update<br>мир</div>
<div>Draw<br>кадр</div>
<div>Repeat<br>повтор</div>
</div>

---

# Цикл в коде

<div class="code">
while not game.is_close_clicked():<br>
&nbsp;&nbsp;&nbsp;&nbsp;update_world(world)<br>
&nbsp;&nbsp;&nbsp;&nbsp;draw_world(world)<br>
&nbsp;&nbsp;&nbsp;&nbsp;game.show_canvas()
</div>

---

# Клавиатура

<div class="split">
<div>
<div class="code">
if game.is_key_down("right"):<br>
&nbsp;&nbsp;&nbsp;&nbsp;x += speed
</div>
</div>
<div>
<div class="screen"><div class="hero"></div></div>
<div class="arrow">→</div>
</div>
</div>

---

# `if` — развилка

Если клавиша нажата — меняем координаты.

Если не нажата — ничего не делаем.

<div class="formula">если условие верно: сделать действие</div>

---

# Движение зависит от времени

<div class="formula">position += direction * speed * dt</div>

<span class="nowrap">`dt` — сколько времени прошло с прошлого кадра.</span>

Так движение не зависит от скорости компьютера.

---

# Границы и стены

<div class="screen">
<div class="hero"></div>
<div class="wall"></div>
</div>

Игра каждый кадр спрашивает: герой ещё внутри экрана? герой касается стены?

---

# Практика

Открой:

<span class="nowrap">`lessons/lesson2/samples/01_keyboard_game_loop.py`</span>

Потом попробуй исправить:

<span class="nowrap">`lessons/lesson2/puzzles/01_hero_escapes_screen.py`</span>
