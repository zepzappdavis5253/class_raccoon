#lab01_turtle.py

from turtle import *

#stick figure

#make circular head!
x = range(359)
for n in x:
    forward(1)
    left(1)
left(1)

#make body
right(90)
forward(200)

#make left arm
penup()
left(180)
forward(100)
left(90)
pendown()
forward(80)
right(90)
forward(80)
left(90)
forward(25)

#move back to center
left(180)
forward(25)
right(90)
forward(80)
left(90)

#make right arm
forward(160)
right(90)
forward(80)
left(90)
forward(25)

#move back to center
left(180)
forward(25)
right(90)
forward(80)
left(90)
forward(80)
left(90)
forward(100)

#left leg
right(35)
forward(110)
right(55)
forward(30)
right(180)
forward(30)
left(55)
forward(110)

#right leg
right(110)
forward(110)
left(55)
forward(30)
left(180)
forward(30)
right(55)
forward(110)


done()
