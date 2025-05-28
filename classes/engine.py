import numpy as np
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
    
    @staticmethod
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
            if sens_direction[1:3] == 'GH':
                row -= 1
                col -= 1
            elif sens_direction[1:3] == 'GB':
                row += 1
                col -= 1
            elif sens_direction[1:3] == 'DH':
                row -= 1
                col += 1
            elif sens_direction[1:3] == 'DB':
                row += 1
                col += 1

        return(row, col)
    
    def isInGrid(self, i, j):
        return i >= 0 and i < 8 and j >= 0 and j < 8
    
    def isPlayerColor(self,row_neighbor, col_neighbor):
        return (self.current_player.color == self.othello_board.array_of_cases[row_neighbor, col_neighbor].color)
    
    def isOppositeColor(self,row_neighbor, col_neighbor):
        isNotEmpty = not self.othello_board.is_available(row_neighbor, col_neighbor) #isNotEmpty
        different_color = self.current_player.color != self.othello_board.array_of_cases[row_neighbor, col_neighbor].color
        return (different_color and isNotEmpty)
    
    def find_pawns_to_flip(self, coord_new_pawn):
        directions = ['VH', 'VB', 'HG', 'HD', 'DGH', 'DGB', 'DDH', 'DDB']

        all_pawns_to_flip = list() 

        for direction in directions:

            row_add, col_add = self.move_direction(direction)
            dir_pawns_to_flip = list() # pqzn to flip in direction
            row_neighbor = coord_new_pawn[0] + row_add 
            col_neighbor = coord_new_pawn[1] + col_add

            while self.isInGrid(row_neighbor, col_neighbor) \
                and not self.othello_board.is_available(row_neighbor, col_neighbor) \
                and self.isOppositeColor(row_neighbor, col_neighbor):

                neighbor_pawn = self.othello_board.array_of_cases[row_neighbor, col_neighbor]
                dir_pawns_to_flip.append(neighbor_pawn)
                row_neighbor += row_add
                col_neighbor += col_add

            # If this list is not empty,
            # We must check that the last pawn is of the player's color
            # if that is the case, the sandwiched pawns are flipped
            if len(dir_pawns_to_flip) > 0:
                if self.isInGrid(row_neighbor, col_neighbor) and self.isPlayerColor(row_neighbor, col_neighbor): # does it make a sandwich ?
                    all_pawns_to_flip.extend(dir_pawns_to_flip)

        return all_pawns_to_flip

    
    @current_player.setter
    def current_player(self,some_player:Player):
        if not (some_player in [self.player1,self.player2]):
            raise ValueError(f"{some_player} not a valid value")
        self._current_player = some_player

    def board_update(self, playerMoveCoordinates):
        x,y = playerMoveCoordinates
        current_color = self.current_player.color
        
        pawns_to_flip = self.find_pawns_to_flip(playerMoveCoordinates, self.current_player)

        if len(pawns_to_flip) > 0:
            self.othello_board.add_pawn_to_case(x,y,Pawn(color=current_color))

            for pawn in pawns_to_flip:
                pawn.flip_pawn()
            
            return(True)

        else:
            return(False)
        
    def can_current_player_play():
        """
        return True IFF current player has a available case where he can play (i.e. flip pawn of opposit color)
        """
        for row_coord in range(0,8):
            for col_coord in range(0,8):
                if self.is_adjacent(row_coord, col_coord):
                    if self.find_pawns_to_flip((row_coord, col_coord)): #True IFF the list contains one pawn to flip
                        return(True)
        return(False)                     


    def switch_player(self):
        if self.current_player == self.player1:
            self._current_player = self.player2
        else:
            self._current_player = self.player1

    def coord_to_alphanum(self,x:int,y:int):
        return(x+1,chr(ord('A')+y))
    
    def is_adjacent(self, row_coord, col_coord):
        directions = ['VH', 'VB', 'HG', 'HD', 'DGH', 'DGB', 'DDH', 'DDB']
        for direction in directions:
            row_add, col_add = self.move_direction(direction)
            if not self.othello_board.is_available(row_coord + row_add, col_coord + col_add):
                return True
            else:
                break
        return False

    def ask_player_pawn_coord(self): #WIP reformat
        coordinate_is_free = False
        while not coordinate_is_free:
            (x,y) = self.current_player.pawn_coord()
            coordinate_is_free = self.othello_board.is_available(x,y)
            if not coordinate_is_free and self.is_adjacent(x,y): 
                print(f"The case {self.coord_to_alphanum(x,y)} is not available")
        
        has_worked = self.board_update((x,y))

        if has_worked:
            self.switch_player()
            return None
        else:
            print(f"The chosen coordinates ( {self.coord_to_alphanum(x,y)} ) does not flip any pawns. Choose other coordinates, you dirty noob.")
            self.ask_player_pawn_coord()
    
    def play(self):
        i = 0
        a_player_played_last_turn = True
        game_is_over = False
        while not game_is_over: #WIP move player switch from .ask_player_pawn_coord() to inside 
            self.othello_board.display_board()
            if self.can_current_player_play():
                self.ask_player_pawn_coord()
                a_player_played_last_turn = True
            else:
                if a_player_played_last_turn:
                    print(f"Player {self.current_player.color} Cannot play, their turn is skipped")
                    a_player_played_last_turn = False
                else:
                    game_is_over = True
                    print(f"The game is over on turn {i}")
            i += 1
        self.display_scores()
        
    def display_scores(self):
        board_array = self.othello_board.array_of_cases
        score_O = np.count_nonzero(board_array == 'O')
        score_X = np.count_nonzero(board_array == 'X')
        if score_O > score_X:
            winner_is = "Player O"
        elif score_X > score_O:
            winner_is = "Player X"
        else:
            winner_is = "no one"
        print(f"Scores \n Player O: {score_O} \n Player X: {score_X} \n Winner is {winner_is}")
        self.display_winner()
    def pawn_to_coord(self,p:Pawn):
        for i in range(0,8):
            for j in range(0,8):
                if self.othello_board.array_of_cases[i,j] == p:
                    return(i,j)
    def pawn_to_alphanum(self,p:Pawn):
        i,j = self.pawn_to_coord(p)
        return(self.coord_to_alphanum(i,j))
    def display_winner():
        pass #WIP