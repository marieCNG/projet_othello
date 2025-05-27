from classes.board import Board
from classes.player import Player
from classes.pawn import Pawn

class Engine():
    def __init__(self):
        self.othello_board = Board()
        self.player1 = Player('O')
        self.player2 = Player('X')
        self.current_player = self.player1
    
    #Methods
    @property
    def current_player(self):
        return(self._current_player)
    
    def move_direction(sens_direction):
        row = 0
        col = 0
        if sens_direction[0] == 'V':
            if sens_direction[1] == 'H':
                row -= 1
            elif sens_direction[1] == 'B':
                row += 1
        elif sens_direction[0] == 'H':
            if sens_direction[1] == 'G':
                col -= 1
            elif sens_direction[1] == 'D':
                col += 1
        elif sens_direction[0] == 'D':
            if sens_direction[1:2] == 'GH':
                row -= 1
                col -= 1
            elif sens_direction[1:2] == 'GB':
                row += 1
                col -= 1
            elif sens_direction[1:2] == 'DH':
                row -= 1
                col += 1
            elif sens_direction[1:2] == 'DB':
                row += 1
                col += 1

        return row, col
    
    def find_pawns_to_flip(coord_dep, board, player):
        directions = ['VH', 'VB', 'HG', 'HD', 'DGH', 'DGB', 'DDH', 'DDB']

        pawns_to_flip = list()

        for direction in directions:
            row_add, col_add = Engine.move_direction(direction)

            row_neighbor, col_neighbor = coord_dep + row_add, coord_dep + col_add
            while row_neighbor <= 7 or col_neighbor <= 7:
                neighbor_pawn = board[row_neighbor, col_neighbor]
                if neighbor_pawn.color != player.color:
                    row_neighbor += row_add
                    col_neighbor += col_add
                else:
                    pawn_to_flip = board[row_neighbor, col_neighbor]
                    pawns_to_flip.append(pawn_to_flip)
        return pawns_to_flip

    
    @current_player.setter
    def current_player(self,some_player:Player):
        if not (some_player in [self.player1,self.player2]):
            raise ValueError(f"{some_player} not a valid value")
        self._current_player = some_player

    def board_update(self,last_coord):
        x,y = last_coord
        current_color = self.current_player.color
        self.othello_board.add_pawn_to_case(x,y,Pawn(color=current_color))

        pawns_to_flip = self.find_pawns_to_flip(last_coord, self.othello_board, self.current_player.color)

        for pawn in pawns_to_flip:
            pawn.flip_pawn()

        pass # WIP, finish update by flipping Eaten pawn

    def switch_player(self):
        if self.current_player == self.player1:
            self._current_player = self.player2
        else:
            self._current_player = self.player1

    def coord_to_alphanum(self,x:int,y:int):
        return(x+1,chr(ord('A')+y))
    
    def ask_player_pawn_coord(self):
        coordinate_is_free = False
        while not coordinate_is_free:
            (x,y) = self.current_player.pawn_coord()
            coordinate_is_free = self.othello_board.is_available(x,y)
            if not coordinate_is_free:
                print(f"The case {self.coord_to_alphanum(x,y)} is not available")
        self.board_update((x,y))
        self.switch_player()
        return None
    
    def play(self):
        i = 0
        while True and i < 60: #WIP
            self.othello_board.display_board()
            self.ask_player_pawn_coord()
            i += 1
        self.display_winner()
        
    def display_winner():
        pass #WIP