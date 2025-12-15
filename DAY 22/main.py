from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Pong")
sc.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_start =  True
speed = 0.1

while game_start:
    time.sleep(speed)
    sc.update()
    ball.move()

    #make it bounce on y-axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *= 0.9

    #right paddle missing the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
        speed = 0.1

    #left paddle missing the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()
        speed = 0.1

sc.exitonclick()