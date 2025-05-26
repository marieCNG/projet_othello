import numpy as np
import pawn

class Board:
    def __init__(self):
        temp = np.array([pawn.Pawn() for i in range(64)]).reshape((8,8))
        temp[3,3] = temp[4,4] = pawn.Pawn(color="O") # white
        temp[3,4] = temp[4,3] = pawn.Pawn(color="X") # black
        self.array_of_cases = temp

    def add_pawn_to_case(self, coord_row, coord_col, pawn):
        self.array_of_cases[coord_row, coord_col] = pawn

    def display_board(self):
        inter_row = "  +---+---+---+---+---+---+---+---+"
        print("Board state is")
        print("    A   B   C   D   E   F   G   H")
        for i in range(8):
            print(inter_row)
            print("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |".format(i+1, self.array_of_cases[i, 0].color, self.array_of_cases[i, 1].color, self.array_of_cases[i, 2].color, self.array_of_cases[i, 3].color, self.array_of_cases[i, 4].color, self.array_of_cases[i, 5].color, self.array_of_cases[i, 6].color, self.array_of_cases[i, 7].color))
        print(inter_row)

if __name__ == "__main__":
    board = Board()

    board.display_board()

    board.add_pawn_to_case(coord_row=4, coord_col=5, pawn=pawn.Pawn(color="X"))

    board.display_board()