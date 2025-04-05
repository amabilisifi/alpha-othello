import copy
from Agents.minMaxAgent import evaluate_board

class AlphaBetaAgent:
    def __init__(self, depth):
        self.depth = depth

    def get_move(self, game):
        """Runs Alpha-Beta Pruning to determine the best move"""
        if not game.get_valid_moves():  # Check if there are no valid moves
            return None
        best_value = float('-inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in game.get_valid_moves():
            game_copy = copy.deepcopy(game)
            game_copy.make_move(*move)
            value = self.alpha_beta(game_copy, self.depth - 1, alpha, beta, False)
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
        return best_move

    def alpha_beta(self, game, depth, alpha, beta, maximizing_player):
        """Applies pruning to Minimax for efficiency"""
        if depth == 0 or game.game_over():
            return evaluate_board(game)

        valid_moves = game.get_valid_moves()
        if not valid_moves:  # If no valid moves, return evaluation of current state
            return evaluate_board(game)

        if maximizing_player:
            value = float('-inf')
            for move in valid_moves:
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                value = max(value, self.alpha_beta(game_copy, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cutoff
            return value
        else:
            value = float('inf')
            for move in valid_moves:
                game_copy = copy.deepcopy(game)
                game_copy.make_move(*move)
                value = min(value, self.alpha_beta(game_copy, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break  # Alpha cutoff
            return value