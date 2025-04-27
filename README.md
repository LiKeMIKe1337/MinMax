# 🤖 Tic-Tac-Toe AI: Minimax vs Alpha-Beta Pruning

## Overview
This project is a command-line Tic-Tac-Toe game featuring AI players powered by the **Minimax Algorithm** and its optimized version with **Alpha-Beta Pruning**.  
You can play against AI or watch AI vs AI matches, while comparing their performance in terms of **speed** and **node exploration**.

---

## ✨ Key Features
- Play **Human vs AI** (Minimax or Alpha-Beta)
- Watch **AI vs AI** matches
- Compare performance between **standard Minimax** and **Alpha-Beta Pruning**

### Real-time display of:
- Number of **nodes explored**
- **Time** taken for decision-making
- **Speedup** and **efficiency comparison**

---

## 🛠️ Project Structure
- **TicTacToe** class: Handles board and win conditions
- **HumanPlayer** class: Handles user input
- **RandomComputerPlayer** class: (Optional random AI)
- **MinimaxPlayer** class: AI using Minimax
- **AlphaBetaPlayer** class: AI using Alpha-Beta Pruning
- **play()** function: Manages gameplay
- **compare_algorithms()** function: Benchmarks Minimax vs Alpha-Beta

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai
```

### 2. Run the Python file
```bash
python tic_tac_toe_ai.py
```
### 3. Choose a mode:
```makefile 
1: Human vs Minimax AI
2: Human vs Alpha-Beta AI
3: Minimax AI vs Alpha-Beta AI
4: Compare performance
5: Exit
```
## 📷 Preview
```makefile
Welcome to Tic-Tac-Toe!
1: Human vs Minimax AI
2: Human vs Alpha-Beta AI
3: Minimax AI vs Alpha-Beta AI
4: Compare Algorithm Performance
5: Exit
Choose a game mode (1-5):
```
Sample Board Layout:
```
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```

⚙️ Requirements

- Python 3.x
- No external libraries needed (only time and random from the standard library)

🧠 Algorithm Insights
 __Minimax__
A recursive backtracking algorithm that simulates all possible moves to pick the best one.

Alpha-Beta Pruning
An optimization that cuts off branches that cannot affect the final decision, greatly reducing computation.

After running Compare Algorithm Performance, you'll see:

- Nodes explored by each algorithm

- Time taken

- Percentage of node reduction

- Speed improvement factor

🙌 Acknowledgements

Inspired by classic AI studies and games to showcase the power of search algorithms in simple environments.

