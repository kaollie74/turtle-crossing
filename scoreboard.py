from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.setposition(x=0, y=270)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increment_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write("Game Over", align="center", font=FONT)
