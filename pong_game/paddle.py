from turtle import Turtle


class Paddle:
    def __init__(self, position):
        self.paddle = Turtle()
        self.paddle.hideturtle()
        self.paddle.speed("fastest")
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.shapesize(5, 1)
        self.paddle.color("white")
        # rp_x_pos = 350
        # rp_y_pos = 0
        self.paddle.goto(position)
        self.paddle.showturtle()

    def r_move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def r_move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def l_move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def l_move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)