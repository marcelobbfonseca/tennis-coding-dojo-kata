import app
from player import Paddle


def test_player_start_score():
    paddle = Paddle('player 1')
    paddle2 = Paddle('player 2')
    assert paddle.score == 0
    assert paddle2.score == 0

def test_player_1_score_fifteen():
    player = Paddle('player 1')
    player.goal()
    assert player.score == '15', 'Score should be 15'

def test_is_deuce():
    pass 
    
