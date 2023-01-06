from turtle import Turtle, Screen

drew = Turtle()
screen = Screen()

def move_forwards():
    drew.forward(10)

def move_backwards():
    drew.backward(10)

def move_left():
    new_heading = drew.heading() + 10 
    drew.setheading(new_heading)

def move_right():
    new_heading = drew.heading() - 10 
    drew.setheading(new_heading)

def clear():
    drew.clear()
    drew.penup()
    drew.home()
    drew.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "d", fun = move_right)
screen.onkey(clear, "c")



screen.exitonclick()