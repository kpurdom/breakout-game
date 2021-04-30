from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
from scoreboard import Scoreboard
import time

GAMES = 2
PADDLE_DISTANCE = 45
PADDLE_HITS = 0

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball((0, -330))
bricks = BrickManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce()

    # Detect collision with top
    if ball.ycor() > 380:
        ball.rebound()
        paddle.shapesize(stretch_wid=1, stretch_len=3)
        PADDLE_DISTANCE = 30

    # Detect collision with paddle
    if ball.distance(paddle) < PADDLE_DISTANCE and ball.y_move < 0 and ball.ycor() >= -340:
        PADDLE_HITS += 1
        ball.rebound()
        if PADDLE_HITS >= 12:
            ball.move_speed = 0.025
        elif PADDLE_HITS >= 8:
            ball.move_speed = 0.05
        elif PADDLE_HITS >= 4:
            ball.move_speed = 0.075
        if not bricks.bricks:
            GAMES -= 1
            if GAMES > 0:
                bricks.create_wall()
            else:
                game_is_on = False
                scoreboard.game_over()

    # Detect paddle miss
    if ball.ycor() < -340:
        PADDLE_HITS = 0
        PADDLE_DISTANCE = 45
        ball.reset_position()
        paddle.reset_position()
        scoreboard.update_lives()
        if scoreboard.lives == 0:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with brick
    for brick in bricks.bricks:
        if ball.distance(brick["brick"]) < 30:
            scoreboard.update_score(brick["points"])
            brick["brick"].hideturtle()
            bricks.bricks.remove(brick)
            ball.rebound()


screen.exitonclick()
