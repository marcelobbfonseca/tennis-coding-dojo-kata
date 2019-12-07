import app
from player import Paddle
from app import Tennis, is_deuce, has_advantage


player1 = None
player2 = None
def setup_module(module):
    global player1, player2
    player1 = Paddle('player 1')
    player2 = Paddle('player 2')


def test_player_start_score():
    assert player1.score == 0
    assert player2.score == 0


def test_point_system():
    assert Tennis.POINT_SYSTEM[0] == 0
    assert Tennis.POINT_SYSTEM[1] == 15
    assert Tennis.POINT_SYSTEM[2] == 30
    assert Tennis.POINT_SYSTEM[3] == 40
    assert Tennis.POINT_SYSTEM[4] == 'Advantage'

def test_player_1_score_fifteen():
    player1.score += 1
    assert Tennis.POINT_SYSTEM[player1.score] == 15, 'Score should be 15'

def test_is_deuce():
    player1.score = 3
    player2.score = 3
    assert is_deuce(player1, player2) is True

def test_has_advantage():
    player1.score = 3
    player2.score = 4
    adv, player = has_advantage(player1,player2)
    assert adv == True
    assert player == player2.name
    assert Tennis.POINT_SYSTEM[player2.score] == 'Advantage'

def test_to_score_deuce():
    player1.score = 3
    player2.score = 4
    Tennis.to_score(scorer=player1, other=player2)
    assert player1.score == 3
    assert player2.score == 3
    assert is_deuce(player1, player2) == True

def test_to_score_win():
    player1.score = 3
    player2.score = 4
    Tennis.to_score(scorer=player2, other=player1)
    assert player2.score == 5
    assert Tennis.POINT_SYSTEM[player2.score] == 'Winner'
    assert Tennis.GAME_OVER == True
