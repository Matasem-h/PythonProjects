from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

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
    for square in squares:
        square.forward(20)






















screen.exitonclick()