from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")


right_player = Turtle()
right_player.penup()
right_player.shape("square")
right_player.shapesize(5, 1)
right_player.color("white")
rp_x_pos = 350
rp_y_pos = 0
right_player.goto(rp_x_pos, rp_y_pos)

left_player = Turtle()
left_player.penup()
left_player.shape("square")
left_player.shapesize(5, 1)
left_player.color("white")
lp_x_pos = -350
lp_y_pos = 0
left_player.goto(lp_x_pos, lp_y_pos)

screen.listen()
screen.onkey()




screen.exitonclick()
