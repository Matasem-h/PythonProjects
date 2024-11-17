from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
michelangelo = Turtle()
michelangelo.shape("turtle")
michelangelo.color("orange")


def move_forward():
    michelangelo.forward(10)


def move_backwards():
    michelangelo.backward(10)


def move_left():
    michelangelo.left(10)


def move_right():
    michelangelo.right(10)


def reset():
    michelangelo.clear()
    michelangelo.penup()
    michelangelo.home()
    michelangelo.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
