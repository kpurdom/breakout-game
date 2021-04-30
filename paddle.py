from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_left(self):
        if self.xcor() > -480:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 480:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(0, -350)
        self.shapesize(stretch_wid=1, stretch_len=5)
