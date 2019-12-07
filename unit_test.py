import app
from player import Paddle
from app import TennisGame, is_duece, to_score


player1 = None
player2 = None
def setup_module(module):
    global player1, player2
    player1 = Paddle('player 1')
    player2 = Paddle('player 2')


def test_player_start_score():
    assert player1.score == 0
    assert player2.score == 0

def test_duece():
    player1.score = 3
    player2.score = 3
    duece = is_duece(player1, player2)
    assert duece == True

def test_tennis_score_system():
    player1.score = 1
    assert TennisGame.SCORE_SYSTEM[player1.score] == 15

def test_pontuar_deuce():
    player1.score = 3
    player2.score = 3
    
    to_score(player1, player2)
    assert player1.score == 4

def test_pontuar_other_advantage():
    player1.score = 4
    player2.score = 3
    to_score(scorer=player2, other=player1)
    assert player1.score == 3
    assert player2.score == 3
    assert TennisGame.SCORE_SYSTEM[player1.score] == 40

def test_pontuar_player_advantage():
    player1.score = 4
    player2.score = 3
    to_score(scorer=player1, other=player2)
    assert player1.score == 5
    assert player2.score == 6
    assert TennisGame.SCORE_SYSTEM[player1.score] == 'win'

def test_player_win():
    player1.score = 3
    player2.score = 2
    to_score(scorer=player1, other=player2)   
    assert player1.score == 5 
    assert TennisGame.SCORE_SYSTEM[player1.score] == 'win'