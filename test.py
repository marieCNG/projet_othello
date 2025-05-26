from classes.board import Board
from classes.engine import Engine
from classes.pawn import Pawn
from classes.player import Player

def test_player():
    garryKasparov = Player('X')
    res = garryKasparov.pawn_coord()

def test_engine():
    partie = Engine()
    partie.play()

def __main__():
    test_engine()

__main__()