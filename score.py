from turtle import Turtle
with open("data.txt") as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
        with open("data.txt", mode="w") as f:
            f.write(f"{self.high_score}")
