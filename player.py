import turtle

class Paddle:
    
    def __init__(self, player):
        if player == 'player 1':
            position_x = -350
        elif player == 'player 2':
            position_x = 350
        else:
            raise ValueError("Specify player 1 or 2")
        
        self.score = 0
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position_x, 0)

    def up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)  

    def down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)  
