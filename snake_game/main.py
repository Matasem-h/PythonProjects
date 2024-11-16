from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

leo_x_position = 0
leo_y_position = 0

squares = []

for _ in range(3):
    leo = Turtle("square")
    leo.color("white")
    leo.penup()
    leo.goto(x=leo_x_position, y=leo_y_position)
    leo_x_position -= 20
    squares.append(leo)

is_snake_moving = True
while is_snake_moving:
    screen.update()
    time.sleep(0.1)

    for square_num in range(len(squares) - 1, 0, -1):
        new_x = squares[square_num - 1].xcor()
        new_y = squares[square_num - 1].ycor()
        squares[square_num].goto(new_x, new_y)
    squares[0].forward(20)
    squares[0].left(90)


screen.exitonclick()
