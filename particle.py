from turtle import *
import random

speed(0)
bgcolor('black')
b = 200
while b > 0:
    color(random.choice(['fuchsia','white']))
    right(b)
    forward(b*2)
    b = b-1
    
