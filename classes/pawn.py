class Pawn:
    def __init__(self, color, coord_row, coord_col):
        self.color = color
        self.coord_row = coord_row
        self.coord_col = coord_col

    def flip(self):
        if self.color == "X":
            self.color == "O"
        elif self.color == "O":
            self.color == "X"

    def __str__(self):
        return f'Infos about this pawn: color is {self.color}, row coordinate is {self.coord_row}, col coordinate is {self.coord_col}'
    

if __name__ == "__main__":

    pawn_1 = Pawn(color="X", coord_row=1, coord_col=1)
    print(str(pawn_1))