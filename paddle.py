from turtle import Turtle

# Create class for Paddles
class Paddle(Turtle):
    # Attributes for paddles, including parameter to set the location of paddles on both sides
    def __init__(self, position):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    # Methods for moving paddles up and down
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

