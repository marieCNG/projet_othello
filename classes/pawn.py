class Pawn:
    def __init__(self, color=' '):
        if color in ['X', 'O', ' ']:
            self._color = color
        else:
            raise ValueError(f'{color} is not a valid value. Valid values are: X, O')

    @property
    def color(self):
        return self._color

    def flip_pawn(self):
        if self.color == "X":
            self._color = "O"
        elif self.color == "O":
            self._color = "X"