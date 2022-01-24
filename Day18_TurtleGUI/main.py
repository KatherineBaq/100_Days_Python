import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")

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

def random_colors():
    #create a random color
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

## Draw shapes
# for i in range(3,30):
#     angle = 360 / i
#     tim.pencolor(random_colors())
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(angle)


# # Draw a random walk
# directions=[0,90,180,270]

# tim.pensize(15)
# for _ in range(200):
#     tim.pencolor(random_colors())
#     #tim.forward(random.randint(1,5)*10)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     #tim.pensize(random.randint(1,20))

## Draw a spirograph
num_circles = 100
angle = 360/num_circles
for _ in range(num_circles):
    tim.circle(100)
    tim.left(angle)
    tim.pencolor(random_colors())



screen = Screen()
screen.exitonclick()