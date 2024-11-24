from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(key="Up", fun=r_paddle.r_move_up)
screen.onkey(key="Down", fun=r_paddle.r_move_down)

screen.onkey(key="w", fun=l_paddle.l_move_up)
screen.onkey(key="s", fun=l_paddle.l_move_down)

screen.exitonclick()
