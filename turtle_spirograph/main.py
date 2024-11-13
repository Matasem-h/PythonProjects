import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed("fastest")

for _ in range(360):
    tim.circle(150)
    tim.right(5)
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = Screen()
screen.exitonclick()
