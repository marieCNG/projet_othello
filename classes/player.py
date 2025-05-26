# File: greetings.py

class Player():
    def __init__(self,color="X"):
        self.color = color
        self.is_autonomous = False
        
    def pawn_coord(self):
        notDone = True
        while notDone:
            try:
                coords_alphanum = input("player {self.color}: Enter coordinates <[A-H][1-8]>: ")
                coord_numnum = self.convert_coord(coords_alphanum)
                notDone = False
            except ValueError:
                print(f"The input {coords_alphanum} does not satisfy the syntaxe <[A-H][1-8]>, please try again")
        return(coord_numnum)
    def convert_coord(self,alphanumCoord:str):
        """
        Player.convert("A1")=(1,1) #int*int
        Player.convert("H7")=(8,7) #int*int
        Player.convert("----____***&&&&H7{}{}{[][]")=(8,7) #int*int
        """
        str_strip = alphanumCoord.strip()
        if len(str_strip)!=2:
            raise ValueError(f"The input {alphanumCoord} does not satisfy the syntaxe <[A-H][1-8]>")
        x = ord(str_strip[0]) - ord('A') + 1
        y = int(str_strip[1])
        if x<1 or x>8:
            raise ValueError(f"The input {alphanumCoord} does not satisfy the syntaxe <[A-H][1-8]>")  
        if y<1 or y>8:
            raise ValueError(f"The input {alphanumCoord} does not satisfy the syntaxe <[A-H][1-8]>")       
        return(x,y)
