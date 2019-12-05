import turtle
import os
import random
from player import Paddle

wn = turtle.Screen()
wn.title("Tennis Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop auto refresh


player_1 = Paddle('player 1')
player_2 = Paddle('player 2')


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball speed
ball.dx = random.choice([0.2 ,-0.2])
ball.dy = random.choice([0.2 ,-0.2])

# Pen. DRAW SCOREBOARD
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() #remove line moving
pen.hideturtle()
pen.goto(0, 260)
board = 'Player A:{}   Player B:{}'.format(player_1.score, player_2.score)
pen.write(board, align='center', font=('Courie', 24, 'normal'))






def ball_movement():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #bounce
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # off the screen(GOAL)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1.score += 1
        pen.clear()
        board = 'Player A:{}   Player B:{}'.format(player_1.score, player_2.score)
        pen.write(board, align='center', font=('Courie', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2.score += 1
        pen.clear()
        board = 'Player A:{}   Player B:{}'.format(player_1.score, player_2.score)
        pen.write(board, align='center', font=('Courie', 24, 'normal'))

def paddle_collision():
    # Paddle B collision
    if  ball.xcor() > 340 and ball.xcor() < 350:
        if ball.ycor() < player_1.paddle.ycor() + 40 and  ball.ycor() > player_1.paddle.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1
    
    # Paddle A collision
    if  ball.xcor() < -340 and ball.xcor() > -350:
        if ball.ycor() < player_2.paddle.ycor() + 40 and  ball.ycor() > player_2.paddle.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1    




# Keyboard binding
wn.listen()
wn.onkeypress(player_1.up, 'w')
wn.onkeypress(player_1.down, 's')

wn.onkeypress(player_2.up, 'Up')
wn.onkeypress(player_2.down, 'Down')

# TODO Game over condition
# TODO add Sound

# Main game loop
while True:
    wn.update()
    ball_movement()
    paddle_collision()














