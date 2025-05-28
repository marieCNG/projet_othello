from classes.board import Board

class AITree:
    def __init__(self, board, color, depth):
        self.node = board
        self.color = color
        self.min_move = None
        self.max_move = None
        self.is_terminal = (depth == 0)
        self.min_tree = None
        self.max_tree = None
        self.depth = depth

    def compute_min_move(self):
        """
        requires node and color
        set min_move
        """
        #find coordinates wich maximize score of my color
        pass

    def compute_max_move(self):
        """
        requires node and color
        set max_move
        """
        pass

    def compute_min_tree(self):
        """
        requires node and min_move

        """
        new_node = self.node.deepcopy() #WIP implement deepcopy in pawn
        new_node.play(self.color.min_move)
        new_color = other_color #WIP to be implemented
        self.min_tree=AITree(new_node,new_color, self.depth-1)
        return(None)
    
    def score(self):
        if is_terminal:
            return(self.node.score(self.color))
        else:
            return(max(self.min_tree.score(), self.max_tree.score()))