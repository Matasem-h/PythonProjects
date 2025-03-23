import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color from"
                                                          " (red, orange, yellow, green, blue, purple): ").lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)

Leonardo = Turtle(shape="turtle")
Leonardo.penup()
Leonardo.color(colors[0])
Leonardo.goto(x=-230, y=0)

Raffaello = Turtle(shape="turtle")
Raffaello.penup()
Raffaello.color(colors[1])
Raffaello.goto(x=-230, y=25)

Michelangelo = Turtle(shape="turtle")
Michelangelo.penup()
Michelangelo.color(colors[2])
Michelangelo.goto(x=-230, y=-25)


screen.exitonclick()
