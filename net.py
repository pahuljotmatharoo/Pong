from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(5)
        self.setheading(90)
        self.penup()
        self.setposition(0, -300)
        self.draw_net()

    def draw_net(self):
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)