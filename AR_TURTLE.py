import turtle
import random

colours = {
    0: 'green',
    1: 'gold',
    2: 'orange',
    3: 'blue',
    4: 'navy',
    5: 'violet',
    6: 'cyan',
    7: 'yellow',
    8: 'red',
    9: 'light blue',
    }

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('white')
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while True:
    t.pencolor(random.choice(list(colours.values())))
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle()
turtle.done()
