from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    def rebound(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -320)
        self.move_speed = 0.1
        self.rebound()