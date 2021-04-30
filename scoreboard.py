from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-400, 350)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))
        self.goto(400, 350)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 15, "normal"))

    def update_score(self, points):
        self.score += points
        self.update_scoreboard()

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        if self.lives == 0:
            message = "GAME OVER!"
        else:
            message = "CONGRATULATIONS, YOU'RE THE WINNER!"
        self.goto(0, -100)
        self.write(f"{message}\n\nYour score is {self.score}", align="center", font=("Courier", 30, "bold"))