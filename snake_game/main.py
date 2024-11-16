from turtle import Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

is_snake_moving = True
while is_snake_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
