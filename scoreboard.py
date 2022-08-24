from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y, player_number):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.setposition(x, y)
        self.score = 0
        self.player_number = player_number
        self.x = x
        self.y = y

    def write_score(self):
        self.write(f"Player {self.player_number}: {self.score}", font=("Arial", 16, "normal"), align="left")

    def add_score(self):
        self.score += 1

    def clear_score(self):
        self.clear()
        self.setposition(self.x, self.y)

    def game_over(self):
        self.setposition(0, 0)
        self.color("white")
        self.write(f"GAME OVER!", font=("Times New Roman", 60, "normal"), align="center")

