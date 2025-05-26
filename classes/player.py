class Player():
    def __init__(self,color="X"):
        self.color = color
        self.is_autonomous = False
        
    def pawn_coord(self):
        notDone = True
        while notDone:
            try:
                coords_alphanum = input("player {self.color}: Enter coordinates <[1-8][A-H]>: ")
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

if __name__ == "__main__":
    player1 = Player(color="X")
    player2 = Player(color="O")

    print(player1.color)

    coord_num = player1.pawn_coord()
    print(coord_num)