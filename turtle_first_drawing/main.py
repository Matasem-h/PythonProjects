import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
turtle.colormode(255)

for _ in range(3):
    tim.forward(100)
    tim.right(360 / 3)
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = Screen()
screen.exitonclick()

