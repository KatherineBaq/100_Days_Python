import random
from turtle import Turtle, Screen
import colorgram

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
    # create a random color
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

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
# num_circles = 100
# angle = 360/num_circles
# for _ in range(num_circles):
#     tim.circle(100)
#     tim.left(angle)
#     tim.pencolor(random_colors())

## Draw a Hirst painting

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)

colors_list = []
for i in range(len(colors)):
    colors_list.append((colors[i].rgb.r/255,colors[i].rgb.g/255,colors[i].rgb.b/255))

colors_list_n = colors_list[4:]
# paint the colors
pos_max = 10
space_step = 50
tim.pensize(20)
tim.penup()
tim.setpos(-200,-200)
tim.hideturtle()
for _ in range(pos_max):
    for _ in range(pos_max):
        tim.color(random.choice(colors_list_n))
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(space_step)
    tim.back((space_step+1)*pos_max)
    tim.left(90)
    tim.forward(space_step)
    tim.right(90)





screen = Screen()
screen.exitonclick()