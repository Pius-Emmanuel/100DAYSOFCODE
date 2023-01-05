import turtle


turtle.speed('slow')
#turtle.penup()
turtle.goto(-100, 0)


# Create a triangle
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
    turtle.color("brown")

# Create a square
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.color("blue")


# Create a pentagon
for i in range(5):
    turtle.forward(100)
    turtle.left(72)
    turtle.color("red")

# Create a hexagon
for i in range(6):
    turtle.forward(100)
    turtle.left(60)
    turtle.color("black")

# Create a heptagon
turtle.pendown()
for i in range(7):
    turtle.forward(100)
    turtle.left(51.4285714285714)
    turtle.color("tomato")

# Create an octagon
for i in range(8):
    turtle.forward(100)
    turtle.left(45)
    turtle.color("dark cyan")

# Create a nonagon
for i in range(9):
    turtle.forward(100)
    turtle.left(40)
    turtle.color("navy")

# Create a decagon
for i in range(10):
    turtle.forward(100)
    turtle.left(36)
    turtle.color("deep pink")

# Prevent the window from closing
turtle.exitonclick()
"deep pink","navy","dark cyan","tomato","black","red","blue","brown"