from classes.board import Board
from classes.pawn import Pawn
from classes.player import Player
from classes.engine import Engine

if __name__ == "__main__":

    ### test board
    board = Board()

    board.display_board()

    board.add_pawn_to_case(coord_row=4, coord_col=5, pawn=Pawn(color="X"))

    board.display_board()

    ### test player
    player1 = Player(color="X")
    player2 = Player(color="O")

    print(player1.color)

    # coord_num = player1.pawn_coord()
    # print(coord_num)

    ### test pawn
    pawn_11 = Pawn(color="O")
    print(pawn_11.color)

    pawn_11.flip_pawn()
    print(pawn_11.color)

    pawn_12 = Pawn(color="X")
    print(pawn_12.color)

    pawn_12.flip_pawn()
    print(pawn_12.color)

    print(vars(pawn_11))

    ### test engine
    partie_test = Engine()
    print(partie_test, vars(partie_test))
    print(partie_test.othello_board.display_board())

    partie_test.play()

    # print(first_round.move_direction("HD"))