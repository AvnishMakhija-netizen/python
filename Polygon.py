import turtle


screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor("red")

t=turtle.Turtle()
t.color("blue")
t.pensize(10)

sides=5
angle=360/sides

for i in range(sides):
    t.forward(100)
    t.right(angle)
    t.speed(10)
turtle.done