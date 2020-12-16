#!/bin/python3

import turtle
import random
mia = turtle.Turtle()
turtle.Screen().bgcolor("cyan")
colours = ["cyan", "purple", "white", "blue"]
mia.penup()
mia.forward(90)
mia.left(45)
mia.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            mia.forward(30)
            mia.backward(30)
            mia.right(45)
        mia.left(90)
        mia.backward(30)
        mia.left(45)
    mia.right(90)
    mia.forward(90)

for i in range(8):
    branch()
    mia.left(45)

#mia.color(random.choice(colours))
    
   
