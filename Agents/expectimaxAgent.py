import copy
from Agents.minMaxAgent import evaluate_board

class ExpectimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def get_move(self, game):
        """ Runs Expectimax to determine the best move. """
        best_value = float('-inf')
        best_move = None
        
        for move in game.get_valid_moves():
            game_copy = copy.deepcopy(game)
            game_copy.make_move(*move)
            value = self.expectimax(game_copy, self.depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move 

    def expectimax(self, game, depth, maximizing_player):
        """ Uses probability-weighted decision-making instead of Minimax. """
        if depth == 0 or game.game_over():
            return evaluate_board(game)

        if maximizing_player:
            value = float('-inf')
            for move in game.get_valid_moves():
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                value = max(value, self.expectimax(game_copy, depth - 1, False))
            return value
        else:
            # Chance node: average of all possible outcomes
            valid_moves = game.get_valid_moves()
            if not valid_moves:
                return evaluate_board(game)
            
            total_value = 0
            for move in valid_moves:
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                total_value += self.expectimax(game_copy, depth - 1, True)
            return total_value / len(valid_moves) 
