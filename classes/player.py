class Player:
    def __init__(self,color="X"):
        self.color = color
    def place_pawn(self):
        coords = input("player {self.color}: Enter coordinates separated by spaces: ").split("")
        return(list(map(lambda x:int(x),coords)))