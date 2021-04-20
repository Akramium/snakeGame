from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f"Your score is: {self.score}", False, align="center")

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", False, align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
