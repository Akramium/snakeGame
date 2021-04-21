from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=280)
        self.update_score()

    def update_score(self):
        self.write(f"Your score is: {self.score}, High score is: {self.high_score}", False, align="center")


    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", False, align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
