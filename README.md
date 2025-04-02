# Tic-Tac-Toe with AI

## Description
This is a Python implementation of the classic Tic-Tac-Toe game featuring an AI opponent that uses the Minimax algorithm with Alpha-Beta pruning to make optimal moves. The game allows a human player to play against the AI, with the human playing as 'X' and the AI as 'O'.

## Features
- **Interactive Gameplay**: Players input their moves via the command line.
- **AI Opponent**: The AI uses the Minimax algorithm with Alpha-Beta pruning to determine the best possible move.
- **Win/Draw Detection**: The game automatically checks for a winner or a draw after each move.
- **Clear Board Display**: The current state of the board is printed after each move for easy visualization.

## How to Play
1. **Run the Script**: Execute the `tic_tak_toe.py` file using Python.
2. **Enter Moves**: When prompted, enter your move by specifying the row and column numbers (0-based index, separated by a space). For example, entering `0 1` places an 'X' in the first row and second column.
3. **Game Outcome**: The game will announce the winner ('X' for human, 'O' for AI) or a draw if the board is full with no winner.

## Requirements
- Python 3.x
- NumPy library (install via `pip install numpy`)

## Code Structure
- **`check_winner(board)`**: Checks if there's a winner or a draw.
- **`print_board(board)`**: Displays the current state of the board.
- **`is_full(board)`**: Checks if the board is full.
- **`best_move(board)`**: Determines the AI's best move using the Minimax algorithm.
- **`min_max(board, depth, maximizer, alpha, beta)`**: Implements the Minimax algorithm with Alpha-Beta pruning.
- **`tic_tak_toe()`**: Main function to run the game loop.

## Example Game
```
Enter row and col: 1 1
 |   |  
---------
  | X |  
---------
  |   |  
```
The AI will respond with its move, and the game continues until a winner is determined or the board is full.

## Notes
- The AI is unbeatable; the best outcome you can achieve is a draw.
- Ensure you enter valid row and column numbers (0, 1, or 2) to avoid errors.
