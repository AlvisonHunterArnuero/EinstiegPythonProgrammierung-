import turtle as t
import math as m
import random as r


def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)


def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)


t.bgcolor("#d3dae8")
t.setup(1000, 800)
t.penup()
t.goto(150, 0)
t.pendown()

t.pencolor("white")
t.begin_fill()

for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)

t.fillcolor("#fef5f7")
t.end_fill()

t.begin_fill()

for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i)
    t.goto(x, y)

for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)

t.fillcolor("#f2d7dd")
t.end_fill()
