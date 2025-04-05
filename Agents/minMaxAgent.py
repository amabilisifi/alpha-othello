import copy

def evaluate_board(game):
    """Simple evaluation function: difference in piece count"""
    black_count = sum(row.count('B') for row in game.board)
    white_count = sum(row.count('W') for row in game.board)
    return black_count - white_count if game.current_player == 'B' else white_count - black_count

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def get_move(self, game):
        """ Runs Minimax to determine the best move. """
        best_value = float('-inf')
        best_move = None
        for move in game.get_valid_moves():
            # Create a deep copy of the game state
            game_copy = copy.deepcopy(game)
            game_copy.make_move(*move)
            value = self.minimax(game_copy, self.depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move  

    def minimax(self, game, depth, maximizing_player):
        """ Recursively explores possible moves using Minimax. 
            maximizing_player is a boolean that determines the type of the current player """
        if depth == 0 or game.game_over():
            return evaluate_board(game)

        if maximizing_player:
            max_eval = float('-inf')
            for move in game.get_valid_moves():
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                eval = self.minimax(game_copy, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in game.get_valid_moves():
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                eval = self.minimax(game_copy, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval  
