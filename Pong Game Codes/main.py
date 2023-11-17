from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting my screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Set paddles/ ball/ Scoreboard

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball() 
scoreboard = Scoreboard()

# Set R paddle to listen to 'Up arrow' and 'Down arrow'
# Set L paddle to listen to 'w' and 's'

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

# Until someone score 5 points the game will be on

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Set scores
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.l_score == 5:
            game_is_on = False

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.r_score == 5:
            game_is_on = False


screen.exitonclick()