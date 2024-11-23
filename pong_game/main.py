from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")

paddle = Turtle()
paddle.hideturtle()
paddle.speed("fastest")
paddle.penup()
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.color("white")
rp_x_pos = 350
rp_y_pos = 0
paddle.goto(rp_x_pos, rp_y_pos)
paddle.showturtle()


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)


screen.exitonclick()
