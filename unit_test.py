import app
from player import Paddle


def test_player_start_score():
    paddle = Paddle('player 1')
    paddle2 = Paddle('player 2')
    assert paddle.score == 0
    assert paddle2.score == 0

