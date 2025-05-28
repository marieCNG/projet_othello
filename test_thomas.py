# from board import Board
# from engine import Engine
# from pawn import Pawn
from classes.player import Player


def __main__():
    garryKasparov = Player('X')
    res = garryKasparov.pawn_coord()
    #magnusCarlsen = Player('O')
    print(res)
    return None

__main__()
