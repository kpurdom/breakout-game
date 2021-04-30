from turtle import Turtle
BRICK_POINTS = {"yellow": 1, "green": 3, "orange": 5, "red": 7}
ROWS_PER_COLOUR = 2
BRICKS_PER_ROW = 14


class BrickManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.create_wall()

    def create_wall(self):
        for index, colour in enumerate(BRICK_POINTS):
            for row in range(ROWS_PER_COLOUR):
                for brick in range(BRICKS_PER_ROW):
                    new_brick = Turtle("square")
                    new_brick.color(colour)
                    new_brick.shapesize(stretch_wid=1, stretch_len=3)
                    new_brick.penup()
                    new_brick.goto(-460 + (brick * 70), 90 + (row + (index * 2)) * 30)
                    brick_info = {"brick": new_brick, "colour": colour, "points": BRICK_POINTS[colour]}
                    self.bricks.append(brick_info)