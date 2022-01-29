import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


# Create cars that are 20px high by 40px wide that are randomly generated
# along the y-axis and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.
# If you get stuck, check the video walkthrough in Step 4.

class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(random.randint(260, 300), random.randint(-240, 240))
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.level = level
        self.moving = STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT

    def move_car(self):
        self.forward(self.moving)

    def level_up(self):
        self.moving += MOVE_INCREMENT
