from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    # oga_boga = True
    for _ in range(10):
        random_x = random.randint(0, 230)
        random_y = random.randint(-230, 230)
        car = Turtle("square")
        car.color(random.choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        car.goto(random_x, random_y)
