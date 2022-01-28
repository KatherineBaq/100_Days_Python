from turtle import Turtle

MOVE_STEPS = 10
MOVE_INCREASE = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto((0, 0))
        self.y_move = MOVE_STEPS
        self.x_move = MOVE_STEPS
        self.move_speed = 0.1

    def ball_move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto((new_xcor, new_ycor))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        if self.x_move > 0:
            self.x_move += MOVE_INCREASE
        else:
            self.x_move -= MOVE_INCREASE
        if self.y_move > 0:
            self.y_move += MOVE_INCREASE
        else:
            self.y_move -= MOVE_INCREASE
