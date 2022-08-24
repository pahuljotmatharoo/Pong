from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
from net import Net
import time
import turtle

screen = Screen()
paddle = Paddle(-350)
paddle2 = Paddle(350)
ball = Ball()
scoreboard = Scoreboard(-250, -250, 1)
scoreboard2 = Scoreboard(145, -250, 2)

screen.bgcolor("black")
screen.setup(width=750, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
# controls the left paddle
screen.onkeypress(paddle.up, "w")
screen.onkeypress(paddle.down, "s")
# controls the right paddle
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_over = False
# setting initial speed
speed = 0.04

# writing boards initially
scoreboard.write_score()
scoreboard2.write_score()
net = Net()
while not game_over:
    screen.update()
    time.sleep(speed)
    ball.forward(11)

    # check if it makes contact with the left paddle
    if ball.xcor() < -340 and paddle.distance(ball) < 50:
        i = 1
        ball.bounce()
        speed *= 0.9
        for x in range(i):
            speed = speed - 0.001
        paddle.change_color()
        scoreboard.add_score()
        scoreboard.clear_score()
        scoreboard.write_score()
        i = i + 0.5

    # check if it makes contact with the right paddle
    if ball.xcor() > 340 and paddle2.distance(ball) < 50:
        i = 1
        ball.bounce()
        speed *= 0.9
        for x in range(i):
            speed = speed - 0.001
        paddle2.change_color()
        scoreboard2.add_score()
        scoreboard2.clear_score()
        scoreboard2.write_score()
        i = i + 0.5

    # check if it makes contact with the wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.wall_bounce()

    # checks if lost
    if ball.xcor() > 360 or ball.xcor() < -360:
        time.sleep(1)
        game_over = True

# game over screen
scoreboard.game_over()
screen.exitonclick()
