import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
jim = Turtle()
jim.shape("turtle")
jim.color("black")
jim.speed("fastest")
jim.width(18)
directions = [0 , 90, 180, 270]

for _ in range(300):
    jim.forward(30)
    jim.setheading(random.choice(directions))
    jim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = Screen()
screen.exitonclick()