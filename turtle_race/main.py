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

Donatello = Turtle(shape="turtle")
Donatello.penup()
Donatello.color(colors[3])
Donatello.goto(x=-230, y=50)

Casey_Jones = Turtle(shape="turtle")
Casey_Jones.penup()
Casey_Jones.color(colors[4])
Casey_Jones.goto(x=-230, y=-50)

April_ONeil = Turtle(shape="turtle")
April_ONeil.penup()
April_ONeil.color(colors[5])
April_ONeil.goto(x=-230, y=75)

all_turtles = [Leonardo, Raffaello, Michelangelo, Donatello, Casey_Jones, April_ONeil]

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 223:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()
