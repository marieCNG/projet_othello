import numpy as np
from classes.pawn import Pawn

class Board:
    def __init__(self,listOfDisplayColor:list):
        assert len(listOfDisplayColor)==3
        temp = np.array([Pawn(color=' ', listOfDisplayColor = listOfDisplayColor) for i in range(64)]).reshape((8,8))
        temp[3,3] = Pawn(color="O",listOfDisplayColor = listOfDisplayColor) 
        temp[4,4] = Pawn(color="O",listOfDisplayColor = listOfDisplayColor) # white
        temp[3,4] = Pawn(color="X",listOfDisplayColor = listOfDisplayColor)
        temp[4,3] = Pawn(color="X",listOfDisplayColor = listOfDisplayColor) # black
        self.array_of_cases = temp

    def add_pawn_to_case(self, coord_row, coord_col, pawn):
        self.array_of_cases[coord_row, coord_col] = pawn

    def is_available(self, coord_row, coord_col):
        return(self.array_of_cases[coord_row, coord_col].color == ' ')
    
    def display_board(self):
        inter_row = "  +---+---+---+---+---+---+---+---+"
        print("Board state is")
        print("    A   B   C   D   E   F   G   H")
        for i in range(8):
            print(inter_row)
            # print("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |".format(i+1, self.array_of_cases[i, 0].color, self.array_of_cases[i, 1].color, self.array_of_cases[i, 2].color, self.array_of_cases[i, 3].color, self.array_of_cases[i, 4].color, self.array_of_cases[i, 5].color, self.array_of_cases[i, 6].color, self.array_of_cases[i, 7].color))
            print("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} |".format(i+1, self.array_of_cases[i, 0].__str__(), self.array_of_cases[i, 1].__str__(), self.array_of_cases[i, 2].__str__(), self.array_of_cases[i, 3].__str__(), self.array_of_cases[i, 4].__str__(), self.array_of_cases[i, 5].__str__(), self.array_of_cases[i, 6].__str__(), self.array_of_cases[i, 7].__str__()))
        print(inter_row)
    