from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.ken = Turtle("turtle")
        self.ken.hideturtle()
        self.ken.penup()
        self.ken.setheading(90)
        self.ken.goto(STARTING_POSITION)
        self.ken.showturtle()

    def move_up(self):
        self.ken.forward(MOVE_DISTANCE)
