Tic-Tac-Toe AI (Minimax vs Alpha-Beta Pruning)
Welcome to an advanced Python implementation of Tic-Tac-Toe featuring AI players powered by the Minimax Algorithm and its optimized version using Alpha-Beta Pruning.
This project not only lets you play against the AI but also compare the performance of the two algorithms in terms of speed and node exploration.

✨ Features
Play Human vs AI (Minimax or Alpha-Beta).

Watch AI vs AI matches.

Compare performance between standard Minimax and Alpha-Beta Pruning.

Real-time display of:

Number of nodes explored

Time taken for decision-making

Speedup and efficiency comparison

📂 Project Structure
TicTacToe class: Handles the game board, moves, and win conditions.

Player classes:

HumanPlayer: Takes input from user.

RandomComputerPlayer: Random move selector (extendable).

MinimaxPlayer: AI using Minimax Algorithm.

AlphaBetaPlayer: AI using Alpha-Beta Pruning.

play() function: Manages gameplay between two players.

compare_algorithms() function: Benchmarks Minimax vs Alpha-Beta.

🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai
Run the Python file:

bash
Copy
Edit
python tic_tac_toe_ai.py
Choose a mode:

makefile
Copy
Edit
1: Human vs Minimax AI
2: Human vs Alpha-Beta AI
3: Minimax AI vs Alpha-Beta AI
4: Compare performance
5: Exit
📷 Preview
makefile
Copy
Edit
Welcome to Tic-Tac-Toe!
1: Human vs Minimax AI
2: Human vs Alpha-Beta AI
3: Minimax AI vs Alpha-Beta AI
4: Compare Algorithm Performance
5: Exit
Choose a game mode (1-5):
Sample Board Layout:

Copy
Edit
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
⚙️ Requirements
Python 3.x

No external libraries needed (only time and random modules from the standard library).

🧠 Algorithm Insights
Minimax:
A recursive backtracking algorithm that simulates all possible moves to pick the best one.

Alpha-Beta Pruning:
An optimization that cuts off branches that cannot affect the final decision, greatly reducing computation.

After running Compare Algorithm Performance, you'll see:

Nodes explored by each algorithm

Time taken

Percentage of node reduction

Speed improvement factor

🙌 Acknowledgements
Inspired by classic AI studies and games to showcase the power of search algorithms in simple environments.
