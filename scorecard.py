from turtle import Turtle


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.level = 0

        with open("high_score.txt", mode="r") as high_score_file:
            self.highScore = int(high_score_file.read())

    def display_level(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Level : {self.level}", move=False, align="center", font=("Arial", 16, "normal"))

        self.goto(-200, -200)
        self.write(f"High Score : {self.highScore}", move=False, align="center", font=("Arial", 16, "normal"))

    def count_level(self):
        self.level += 1

    def high_score(self):
        if self.level > self.highScore:
            self.highScore = self.level
            with open("high_score.txt", mode="w") as high_score_file:
                high_score_file.write(str(self.highScore))
