from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0, 0)
        self.set_angle()
        self.penup()

    def set_angle(self):
        angle = 45
        self.setheading(self.heading() + angle)

    def bounce(self, angle=1):
        print(f"Current heading: {self.heading()}")
        if self.heading() >= 315:
            angle *= -90
        elif self.heading() >= 225:
            angle *= 90
        elif self.heading() >= 135:
            angle *= -90
        else:
            angle *= 90
        self.setheading(self.heading() + angle)
        print(f"After heading: {self.heading()}")

    def wall_bounce(self):
        self.bounce(-1)


