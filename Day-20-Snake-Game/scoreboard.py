from turtle import Turtle
from food import Food
ALIGNMENT = 'center'
FONT = ('Times New Roman', 25, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_score()


    def update_score(self):

        self.write(f"Score: {self.score} ", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ", align=ALIGNMENT, font=FONT)
