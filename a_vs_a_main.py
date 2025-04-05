import pygame
from othello import Othello
from Agents.alphaBetaAgent import AlphaBetaAgent
from Agents.expectimaxAgent import ExpectimaxAgent
import copy

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Othello AI vs AI")

# Load game instance
game = Othello()

# Choose AI agents (Modify as needed)
ai_player_B = AlphaBetaAgent(depth=6)  # AI controlling Black pieces
ai_player_W = ExpectimaxAgent(depth=4)  # AI controlling White pieces

def draw_board(screen, game):
    """ Draws the Othello board and pieces """
    screen.fill((34, 139, 34))  # Green background
    for i in range(9):  # Grid lines
        pygame.draw.line(screen, (0, 0, 0), (i * 75, 0), (i * 75, 600))
        pygame.draw.line(screen, (0, 0, 0), (0, i * 75), (600, i * 75))

    # Draw pieces
    for r in range(8):
        for c in range(8):
            if game.board[r][c] == 'B':
                pygame.draw.circle(screen, (0, 0, 0), (c * 75 + 37, r * 75 + 37), 30)
            elif game.board[r][c] == 'W':
                pygame.draw.circle(screen, (255, 255, 255), (c * 75 + 37, r * 75 + 37), 30)

    # Display turn count
    font = pygame.font.Font(None, 36)
    turn_text = font.render(f"Turn: {game.turn_count}", True, (255, 255, 255))
    screen.blit(turn_text, (10, 10))
    
    pygame.display.flip()

# AI vs AI Game Loop
running = True
while running:
    pygame.event.pump()  # ✅ This prevents the game from freezing when clicked
    draw_board(screen, game)  # Update board graphics each frame

    if game.game_over():
        print("Game Over! Winner:", game.get_winner())
        pygame.time.delay(3000)
        break

    # Check if the current player has valid moves
    valid_moves = game.get_valid_moves()
    
    if not valid_moves:  
        # If no valid moves, skip the turn
        print(f"No valid moves for {game.current_player}. Skipping turn.")
        game.current_player = 'B' if game.current_player == 'W' else 'W'
        continue  # Restart loop without making a move

    # AI makes its move
    pygame.time.delay(500)  # Small delay for better visualization
    if game.current_player == 'B':
        ai_move = ai_player_B.get_move(game)
    else:
        ai_move = ai_player_W.get_move(game)
    
    if ai_move:
        game.make_move(*ai_move)

pygame.quit()
