from turtle import Turtle

class Ball(Turtle):
    
    # Setting Ball

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Moving the ball

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce from y walls

    def bounce_y(self):
        self.y_move *= -1       

    # Bounce from paddles and speed up the ball
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.8    

    # Reseting the ball after player scores
    
    def reset_position(self):
        self.goto(0,0)   
        self.move_speed = 0.1     
        self.bounce_x()