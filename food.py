from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        self.goto(x=x_food, y=y_food)
