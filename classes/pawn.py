class Pawn:
    def __init__(self, color, listOfDisplayColor:list):
        assert len(listOfDisplayColor)==3
        self.display_color = listOfDisplayColor
        if color in ['X', 'O', ' ']:
            self.color = color
            self.display_colors=listOfDisplayColor
        else:
            raise ValueError(f'{color} is not a valid value. Valid values are: X, O')

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,c:str):
        self._color = c 
    @property
    def display_colors(self):
        return self._display_colors

    @display_colors.setter
    def display_colors(self,l:list):
        self._display_colors = l
    
    def flip_pawn(self):
        if self.color == "X":
            self._color = "O"
        elif self.color == "O":
            self._color = "X"
    def __str__(self):
        if self.color == "X":
            return self.display_colors[0]
        elif self.color == "O":
            return self.display_colors[1]
        else:
            return self.display_colors[2]