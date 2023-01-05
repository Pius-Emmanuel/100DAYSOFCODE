import turtle as t
import random

r_walk = t.Turtle()
t.colormode(255)

#colours = ["deep pink","navy","dark cyan","tomato","black","red","blue","brown"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color =(r, g, b)
    return random_color


directions = [0, 90, 180, 270]
r_walk.pensize(15)
r_walk.speed("fastest")


for _ in range(200):
    r_walk.color(random_color())
    r_walk.forward(30)
    r_walk.setheading(random.choice(directions))



screen = t.Screen()
screen.exitonclick()