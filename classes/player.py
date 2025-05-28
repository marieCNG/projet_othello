class Player():
    def __init__(self,color:str,displayColor:str):
        self.color = color
        self.display_color = displayColor
        self.is_autonomous = False

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,c:str):
        self._color = c
    
    @property
    def display_color(self):
        return self._display_color

    @display_color.setter
    def display_color(self,c:str):
        self._display_color = c
        
    def pawn_coord(self):
        notDone = True
        while notDone:
            try:
                coords_alphanum = input(f"player {self.__str__()}: Enter coordinates <[1-8][A-H]>: ")
                coord_numnum = self.convert_coord(coords_alphanum)
                notDone = False
            except ValueError:
                print(f"The input {coords_alphanum} does not satisfy the syntaxe <[1-8][A-H]>, please try again")
        return(coord_numnum)

    def convert_coord(self,coords_alphanum:str):
        """
        Player.convert_coord("1A")=(1,1) #int*int
        Player.convert_coord("7H")=(7,8) #int*int
        Player.convert_coord("----____***&&&&7H{}{}{[][]")=(7,8) #int*int
        """
        str_strip = coords_alphanum.strip()

        if len(str_strip)!=2:
            raise ValueError(f"The input {coords_alphanum} does not satisfy the syntaxe <[1-8][A-H]>")

        row = int(str_strip[0]) - 1
        col = ord(str_strip[1]) - ord('A')

        if row<0 or row>7:
            raise ValueError(f"The input {coords_alphanum} does not satisfy the syntaxe <[1-8][A-H]>")
        if col<0 or col>7:
            raise ValueError(f"The input {coords_alphanum} does not satisfy the syntaxe <[1-8][A-H]>")

        return(row,col)
    def __str__(self):
        return self.display_color