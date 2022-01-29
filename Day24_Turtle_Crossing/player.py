STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north.
# If you get stuck, check the video walkthrough in Step 3.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.level = 1
        self.restart_game()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def restart_game(self):
        self.goto(STARTING_POSITION)
        self.level = 1

    def up_level(self):
        self.goto(STARTING_POSITION)
        self.level += 1

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y
