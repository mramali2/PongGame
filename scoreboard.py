from turtle import Turtle

# Create class for Scoreboard
class Score(Turtle):

    # Set scoreboard attributes
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.l_points = 0
        self.r_points = 0
        self.write(f"{self.l_points}   ||   {self.r_points}",
                   False, align="center", font=("Courier", 24, "normal") )

    # Methods for scoreboard to change if either team scores
    def l_win(self):
        self.clear()
        self.l_points += 1
        self.write(f"{self.l_points}   ||   {self.r_points}",
                   False, align="center", font=("Courier", 24, "normal"))

    def r_win(self):
        self.clear()
        self.r_points += 1
        self.write(f"{self.l_points}   ||   {self.r_points}",
                   False, align="center", font=("Courier", 24, "normal"))
