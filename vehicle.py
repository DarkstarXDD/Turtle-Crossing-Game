from turtle import Turtle
from background import Background
import random


background = Background()

RANDOM_VAL_MIN = -background.screen_width
RANDOM_VAL_MAX = background.screen_width

VEHICLE_MOVE_AMOUNT = 5


class Vehicle(Turtle):

    def __init__(self):
        super().__init__()

    def create_vehicle(self):

        self.penup()
        self.shape("square")
        self.speed(2)
        self.goto(x=background.screen_width/2, y=random.randint(-200, 200))

    def vehicle_move(self):

        new_pos = (self.xcor() - VEHICLE_MOVE_AMOUNT, self.ycor())
        self.goto(new_pos)

    def vehicle_color(self):

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rand_color = (r, g, b)
        return rand_color
