# Alpha-Othello

![Othello Game](https://img.shields.io/badge/Game-Othello-blue)  
![Python](https://img.shields.io/badge/Python-3.11+-yellow)  
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

`Alpha-Othello` is a Python-based implementation of the classic board game Othello (also known as Reversi). This project focuses on building intelligent AI agents to play Othello using various algorithms, including Minimax, Alpha-Beta Pruning, and Expectimax. The primary goal is to create a platform where AI agents can compete against each other, allowing for experimentation with different strategies and heuristics. The project also supports human vs. AI gameplay, making it a great tool for both learning and entertainment.

The project includes:
- A core Othello game engine (`othello.py`) that handles the game rules and board state.
- Three AI agents:
  - `minMaxAgent.py`: Uses the Minimax algorithm to evaluate moves.
  - `alphaBetaAgent.py`: Uses Alpha-Beta Pruning to optimize Minimax.
  - `expectimaxAgent.py`: Uses the Expectimax algorithm for probabilistic decision-making.
- Two main scripts:
  - `main.py`: Allows a human to play against an AI agent.
  - `a_vs_a_main.py`: Runs a match between two AI agents.

## Features

- Play Othello against an AI agent or watch AI agents compete against each other.
- Command-line interface for gameplay with a clear display of the board.
- Three distinct AI agents with different strategies:
  - Minimax: A baseline algorithm for optimal decision-making.
  - Alpha-Beta Pruning: An optimized version of Minimax for faster performance.
  - Expectimax: A probabilistic approach for experimenting with uncertainty.
- Modular design, making it easy to add new AI agents or modify existing ones.

## Prerequisites

To run this project, you'll need:
- Python 3.11 or higher.

No additional dependencies are required, as the project uses only the Python standard library.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/amabilisifi/alpha-othello.git
   cd alpha-othello
