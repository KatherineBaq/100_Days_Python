import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# ## Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# ## Draw a dash line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

## Draw shapes
for i in range(3,30):

    angle = 360 / i
    #create a random color
    r = random.random()
    g = random.random()
    b = random.random()
    tim.pencolor((r,g,b))
    for _ in range(i):
        tim.forward(50)
        tim.right(angle)


screen = Screen()
screen.exitonclick()