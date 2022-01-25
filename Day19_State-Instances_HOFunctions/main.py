import random
from turtle import Turtle, Screen

# ## Make an Etch-A-Sketch App
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear_drawing():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_drawing, "c")
# screen.exitonclick()

## Make a turtle race!

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []

for ind_color, color in enumerate(colors):
    turtles.append(Turtle(shape="turtle"))
    turtles[ind_color].color(color)
    turtles[ind_color].penup()
    turtles[ind_color].goto(x=-230, y=(30*(ind_color-3)))

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
