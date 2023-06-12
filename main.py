from turtle import Turtle, Screen
from paddle import Paddle, Turtle
from ball import Ball
import time
from scoreboard import Score


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height= 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score= Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor()> 280 or ball.ycor() < -280:
        ball.bounce()


    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320:
        ball.hit_paddle()



    elif ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.hit_paddle()



    elif ball.xcor() > 360:
        score.l_win()
        ball.reset_position()
        ball.move_speed = 0.1

    elif ball.xcor() < -360:
        score.r_win()
        ball.reset_position()
        ball.move_speed = 0.1







screen.exitonclick()