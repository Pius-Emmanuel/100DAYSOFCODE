import turtle as t
import random

yu = t.Turtle()

colours = ["deep pink","navy","dark cyan","tomato","black","red","blue","brown"]

def shape(num_of_sides):
    angle = 360 / num_of_sides
    for  i in range(num_of_sides):
        yu.forward(100)
        yu.right(angle)

for sides in range(3, 11):
    yu.color(random.choice(colours))
    shape(sides)        