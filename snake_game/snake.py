from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        leo_x_position = 0
        leo_y_position = 0
        for _ in range(3):
            leo = Turtle("square")
            leo.color("white")
            leo.penup()
            leo.goto(x=leo_x_position, y=leo_y_position)
            leo_x_position -= 20
            self.squares.append(leo)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)
