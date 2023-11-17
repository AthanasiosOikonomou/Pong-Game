from turtle import Turtle

class Scoreboard(Turtle):

    # Setting Scoreboard

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Updating Scoreboard

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        if self.l_score == 5:
            self.goto(0, 0)
            self.write("1st Player Wins", align="center", font=("Courier", 20, "normal"))
        if self.r_score == 5:
           self.goto(0, 0)
           self.write("2nd Player Wins", align="center", font=("Courier", 20, "normal"))   
    
    # Add score to 1st player (Left)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Add score to 2nd player (Right)

    def r_point(self):   
        self.r_score += 1
        self.update_scoreboard()        