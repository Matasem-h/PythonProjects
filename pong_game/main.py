from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.r_move_up)
screen.onkey(key="Down", fun=r_paddle.r_move_down)
screen.onkey(key="w", fun=l_paddle.l_move_up)
screen.onkey(key="s", fun=l_paddle.l_move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with right paddle
    if (ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle.paddle) < 50 and ball.xcor()
            < -320):
        ball.bounce_x()

screen.exitonclick()
