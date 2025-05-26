class Pawn:
    def __init__(self, color=" "):
        self.color = color

    def flip_pawn(self):
        if self.color == "X":
            self.color = "O"
        elif self.color == "O":
            self.color = "X"


if __name__ == "__main__":

    square_11 = Pawn(color="O")
    print(square_11.color)

    square_11.flip_pawn()
    print(square_11.color)

    square_12 = Pawn(color="X")
    print(square_12.color)

    square_12.flip_pawn()
    print(square_12.color)

    print(vars(square_11))