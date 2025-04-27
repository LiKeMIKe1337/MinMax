import time
import random

class TicTacToe:
    def __init__(self):

        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_board(self):
     
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    def print_board_nums(self):
      
        number_board = [[str(i+j*3) for i in range(1, 4)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
  
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
    def empty_squares(self):

        return ' ' in self.board
        
    def num_empty_squares(self):
     
        return self.board.count(' ')
        
    def make_move(self, square, letter):
    
        if self.board[square] == ' ':
            self.board[square] = letter
         
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
        
    def winner(self, square, letter):
      
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
            
   
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
     
        if square % 2 == 0:
     
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
     
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
                
        return False

class Player:
    def __init__(self, letter):

        self.letter = letter
        
    def get_move(self, game):
   
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):

        square = random.choice(game.available_moves())
        return square

class MinimaxPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.nodes_explored = 0
        
    def get_move(self, game):
  
        self.nodes_explored = 0
        
        if len(game.available_moves()) == 9:
      
            square = random.choice([0, 2, 4, 6, 8])
        else:
     
            start_time = time.time()
            square = self.minimax(game, self.letter)['position']
            end_time = time.time()
            print(f"Standard Minimax: {self.nodes_explored} nodes explored in {end_time - start_time:.6f} seconds")
        
        return square
        
    def minimax(self, state, player):
        self.nodes_explored += 1
        
        max_player = self.letter 
        other_player = 'O' if player == 'X' else 'X'
        
    
        if state.current_winner == other_player:
        
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
           
            return {'position': None, 'score': 0}
        

        if player == max_player:
            best = {'position': None, 'score': float('-inf')} 
        else:
            best = {'position': None, 'score': float('inf')} 
        
        for possible_move in state.available_moves():
       
            state.make_move(possible_move, player)
            
          
            sim_score = self.minimax(state, other_player)
        
            state.board[possible_move] = ' '
            state.current_winner = None
         
            sim_score['position'] = possible_move
            
    
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
        return best

class AlphaBetaPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.nodes_explored = 0
        
    def get_move(self, game):
    
        self.nodes_explored = 0
        
        if len(game.available_moves()) == 9:
         
            square = random.choice([0, 2, 4, 6, 8])
        else:
      
            start_time = time.time()
            square = self.alpha_beta(game, self.letter, float('-inf'), float('inf'))['position']
            end_time = time.time()
            print(f"Alpha-Beta: {self.nodes_explored} nodes explored in {end_time - start_time:.6f} seconds")
        
        return square
        
    def alpha_beta(self, state, player, alpha, beta):
        self.nodes_explored += 1
        
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'
        
   
        if state.current_winner == other_player:
       
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
        
            return {'position': None, 'score': 0}
   
        if player == max_player:
            best = {'position': None, 'score': float('-inf')}  
        else:
            best = {'position': None, 'score': float('inf')} 
        
        for possible_move in state.available_moves():
       
            state.make_move(possible_move, player)
            
        
            sim_score = self.alpha_beta(state, other_player, alpha, beta)
            
       
            state.board[possible_move] = ' '
            state.current_winner = None
       
            sim_score['position'] = possible_move
     
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
                if beta <= alpha:
                    break 
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])
                if beta <= alpha:
                    break 
                    
        return best

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()
    
    letter = 'X'  
    
  
    while game.empty_squares():
      
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
            
    
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')
                
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
                    
            letter = 'O' if letter == 'X' else 'X'
            
    if print_game:
        print("It's a tie!")

def compare_algorithms():
    print("\n=== Comparing Minimax vs Alpha-Beta Pruning ===")
    game = TicTacToe()
    
 
    moves = [(0, 'X'), (4, 'O'), (2, 'X')]
    for pos, player in moves:
        game.make_move(pos, player)
    
    print("Starting board state:")
    game.print_board()
    
    minimax_player = MinimaxPlayer('X')
    start_time = time.time()
    minimax_move = minimax_player.get_move(game)
    minimax_time = time.time() - start_time
    

    minimax_nodes = minimax_player.nodes_explored

    alpha_beta_player = AlphaBetaPlayer('X')
    start_time = time.time()
    alpha_beta_move = alpha_beta_player.get_move(game)
    alpha_beta_time = time.time() - start_time
    
    alpha_beta_nodes = alpha_beta_player.nodes_explored
    
    print("\nComparison Results:")
    print(f"Standard Minimax: Chose move {minimax_move}, explored {minimax_nodes} nodes in {minimax_time:.6f} seconds")
    print(f"Alpha-Beta: Chose move {alpha_beta_move}, explored {alpha_beta_nodes} nodes in {alpha_beta_time:.6f} seconds")
    print(f"Node reduction: {(1 - alpha_beta_nodes/minimax_nodes) * 100:.2f}%")
    print(f"Speed improvement: {(minimax_time / alpha_beta_time):.2f}x faster")

if __name__ == '__main__':
 
    while True:
        print("\nWelcome to Tic-Tac-Toe!")
        print("1: Human vs Minimax AI")
        print("2: Human vs Alpha-Beta AI")
        print("3: Minimax AI vs Alpha-Beta AI")
        print("4: Compare Algorithm Performance")
        print("5: Exit")
        
        choice = input("Choose a game mode (1-5): ")
        
        if choice == '1':
            game = TicTacToe()
            human = HumanPlayer('X')
            minimax_ai = MinimaxPlayer('O')
            play(game, human, minimax_ai, print_game=True)
        elif choice == '2':
            game = TicTacToe()
            human = HumanPlayer('X')
            alpha_beta_ai = AlphaBetaPlayer('O')
            play(game, human, alpha_beta_ai, print_game=True)
        elif choice == '3':
            game = TicTacToe()
            minimax_ai = MinimaxPlayer('X')
            alpha_beta_ai = AlphaBetaPlayer('O')
            play(game, minimax_ai, alpha_beta_ai, print_game=True)
        elif choice == '4':
            compare_algorithms()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")