from turtle import Turtle
import random


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shapesize(5, 1)
        self.penup()
        self.shape("square")
        self.color("white")
        self.setposition(xcor, 0)

    def up(self):
        self.setposition(self.xcor(), self.ycor() + 20)

    def down(self):
        self.setposition(self.xcor(), self.ycor() - 20)

    def change_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        self.color(r, g, b)