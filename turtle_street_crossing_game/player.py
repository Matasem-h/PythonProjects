from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    ken = Turtle("turtle")
    ken.hideturtle()
    ken.penup()
    ken.setheading(90)
    ken.goto(STARTING_POSITION)
    ken.showturtle()
    pass

