from turtle import Turtle
from background import Background


background = Background()

START_POS_OFFSET = 10
START_POS = (0, -(background.screen_height/2 - START_POS_OFFSET))
PLAYER_MOVE_AMOUNT = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.start_pos = START_POS

    def create_player(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(self.start_pos)

    def player_move(self):
        new_pos = self.ycor() + PLAYER_MOVE_AMOUNT
        self.goto(x=0, y=new_pos)

    def at_finish_line(self):
        if self.distance(x=0, y=background.screen_height/2) < 30:
            return True
