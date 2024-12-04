from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
is_snake_moving = True
while is_snake_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280
    ):
        snake.reset()
        scoreboard.reset()  # Update high score and reset the scoreboard

    # Detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            snake.reset()
            scoreboard.reset()  # Update high score and reset the scoreboard

screen.exitonclick()
