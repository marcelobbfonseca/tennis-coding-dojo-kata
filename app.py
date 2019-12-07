import turtle
import os
import random
from player import Paddle

class Tennis:
                #   0   1   2   3   4           5
    POINT_SYSTEM = [0, 15, 30, 40, 'Advantage', 'Winner']
    GAME_OVER = False


    @staticmethod
    def to_score(scorer, other):
        # already won
        if scorer.score == 5:
            return

        if is_deuce(scorer, other):
            scorer.score = 4
            return 
        
        adv, adv_player = has_advantage(scorer, other)
        if adv:
            if adv_player == scorer.name:
                scorer.score = 5 # winner!
                Tennis.GAME_OVER = True
            else: # back to deuce
                other.score = 3
        elif scorer.score == 3 and other.score <=2:
            scorer.score = 5 # winner!
            Tennis.GAME_OVER = True
        else: 
            scorer.score +=1
        

def setup():
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

    # Key events
    wn.listen()
    wn.onkeypress(player_1.up, 'w')
    wn.onkeypress(player_1.down, 's')

    wn.onkeypress(player_2.up, 'Up')
    wn.onkeypress(player_2.down, 'Down')
    return ball, pen, player_1, player_2, wn



def ball_movement(ball, pen, player_1, player_2):
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
        board = 'Player A:{}   Player B:{}'.format(Tennis.POINT_SYSTEM[player_1.score], Tennis.POINT_SYSTEM[player_2.score])
        pen.write(board, align='center', font=('Courie', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2.score += 1
        pen.clear()
        board = 'Player A:{}   Player B:{}'.format(Tennis.POINT_SYSTEM[player_1.score], Tennis.POINT_SYSTEM[player_2.score])
        pen.write(board, align='center', font=('Courie', 24, 'normal'))

def paddle_collision(ball, player_1, player_2):
    # Paddle B collision
    if  ball.xcor() > 340 and ball.xcor() < 350:
        if ball.ycor() < player_2.paddle.ycor() + 40 and  ball.ycor() > player_2.paddle.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1
    
    # Paddle A collision
    if  ball.xcor() < -340 and ball.xcor() > -350:
        if ball.ycor() < player_1.paddle.ycor() + 40 and  ball.ycor() > player_1.paddle.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1    

def is_deuce(player_1, player_2):
    if(player_1.score == 3 and player_2.score == 3):
        return True
    else:
        return False

def has_advantage(player_1, player_2):
    if(player_1.score == 3 and player_2.score == 4):
        advantage = True, player_2.name
    elif(player_1.score == 4 and player_2.score == 3):
        advantage = True, player_1.name
    else:
        advantage = False, None
    return advantage


def main():
    ball, pen, p1, p2, wn = setup()
    
    # Main game loop
    while Tennis.GAME_OVER == False:
        wn.update()
        ball_movement(ball, pen, p1, p2)
        paddle_collision(ball, p1, p2)


if __name__ == "__main__":
    main()










