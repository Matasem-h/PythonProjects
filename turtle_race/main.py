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

screen.exitonclick()
