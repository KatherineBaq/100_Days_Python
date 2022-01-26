from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_screen()

    def write_screen(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font= FONT)

        #self.write(f"Score: ", False, align="Center")
        #self.write((-300,0),True)

    def increase_score(self):
        self.score += 1
        self.write_screen()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font= FONT)

