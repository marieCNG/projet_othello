from classes.board import Board
from classes.player import Player

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
    
    def board_update(self,last_coord):
        self.othello_board.add_pawn_to_case(last_coord)

        # i = row
        # for direction in directions:
        #     if direction[0] == 'V':
        #         if direction[1] == 'H':
        #             i -= 1
        #         elif direction[1] == 'B':
        #             i += 1


        pass # WIP, finish update by flipping Eaten pawn

    def switch_player(self):
        if self.current_player == self.player1:
            self._current_player = self.player1
        else:
            self._current_player = self.player2

    def ask_player_pawn_coord(self):
        (x,y) = self.current_player.pawn_coord()
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