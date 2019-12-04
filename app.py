import turtle
import os

wn = turtle.Screen()
wn.title("Tennis Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop auto refresh

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball speed. up-right
ball.dx = .2 #TODO make it rand
ball.dy = .2

# Pen. DRAW SCOREBOARD
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup() #remove line moving
pen.hideturtle()
pen.goto(0, 260)
board = 'Player A:{}   Player B:{}'.format(score_a, score_b)
pen.write(board, align='center', font=('Courie', 24, 'normal'))




# Motion
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)    

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)  

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)    

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)  

def ball_movement(score_a, score_b):
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
        score_a += 1
        board = 'Player A:{}   Player B:{}'.format(score_a, score_b)
        pen.write(board, align='center', font=('Courie', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        board = 'Player A:{}   Player B:{}'.format(score_a, score_b)
        pen.write(board, align='center', font=('Courie', 24, 'normal'))
def paddle_collision():
    # Paddle B collision
    if  ball.xcor() > 340 and ball.xcor() < 350:
        if ball.ycor() < paddle_b.ycor() + 40 and  ball.ycor() > paddle_b.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1
    
    # Paddle A collision
    if  ball.xcor() < -340 and ball.xcor() > -350:
        if ball.ycor() < paddle_a.ycor() + 40 and  ball.ycor() > paddle_a.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1    



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()
    ball_movement(score_a, score_b)
    paddle_collision()













