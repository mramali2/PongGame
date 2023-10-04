from turtle import Turtle

# Class for the pong ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Method to move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    # Method to change direction in the y-axis if the ball hits a wall
    def bounce(self):
        self.y_move*=-1

    # Method to change direction in x-axis and increase speed everytime it hits a paddle
    def hit_paddle(self):
        self.x_move *=-1
        self.move_speed /= 1.1

    # Method to reset ball back to the centre after each point won
    def reset_position(self):
        self.home()
        self.hit_paddle()
        self.move()






