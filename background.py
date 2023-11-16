from turtle import Turtle, Screen
from scorecard import Scorecard

scorecard = Scorecard()


class Background(Turtle):

    def __init__(self):
        super().__init__()

        self.screen = Screen()
        self.penup()
        self.hideturtle()
        self.screen_width = 600
        self.screen_height = 500
        self.rules = """Instructions :
        Move the turtle to the opposite side.
        If the turtle hits a vehicle the game will end.
        Turtle can only move forward.
        Speed and the number of vehicles will increase as you go to higher levels.
        """

        self.screen.setup(width=self.screen_width, height=self.screen_height)
        self.screen.bgcolor("medium sea green")

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=("Arial", 20, "normal"))

        self.goto(0, -75)
        self.write("Press 'Q' to Play Again", move=False, align="center", font=("Arial", 12, "normal"))

    def close_app(self):
        self.screen.bye()

    def welcome(self):
        self.goto(0, 180)
        self.write("Welcome to Turtle Crossing!", move=False, align="center", font=("Arial", 20, "normal"))

        self.goto(0, 60)
        self.write("Press 'Q' to Start", move=False, align="center", font=("Arial", 12, "normal"))
        self.goto(0, 30)
        self.write("Press 'E' to Close", move=False, align="center", font=("Arial", 12, "normal"))

        self.goto(-50, -200)
        self.write(self.rules, move=False, align="center", font=("Arial", 10, "normal"))
