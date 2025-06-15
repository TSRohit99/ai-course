class MinMaxAlphaBeta:
    def __init__(self):
        self.max_player = 'X'  # AI
        self.min_player = 'O'  # Human

    def min_max(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner == self.max_player:
            return 1
        elif winner == self.min_player:
            return -1
        elif not any(cell == ' ' for row in board for cell in row):
            return 0

        if is_maximizing:
            best = -float('inf')
            for move in self.get_possible_moves(board):
                new_board = self.make_move(board, move, self.max_player)
                best = max(best, self.min_max(new_board, depth + 1, False))
            return best
        else:
            best = float('inf')
            for move in self.get_possible_moves(board):
                new_board = self.make_move(board, move, self.min_player)
                best = min(best, self.min_max(new_board, depth + 1, True))
            return best

    def alpha_beta(self, board, depth, is_maximizing, alpha, beta):
        winner = self.check_winner(board)
        if winner == self.max_player:
            return 1
        elif winner == self.min_player:
            return -1
        elif not any(cell == ' ' for row in board for cell in row):
            return 0

        if is_maximizing:
            best = -float('inf')
            for move in self.get_possible_moves(board):
                new_board = self.make_move(board, move, self.max_player)
                best = max(best, self.alpha_beta(new_board, depth + 1, False, alpha, beta))
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return best
        else:
            best = float('inf')
            for move in self.get_possible_moves(board):
                new_board = self.make_move(board, move, self.min_player)
                best = min(best, self.alpha_beta(new_board, depth + 1, True, alpha, beta))
                beta = min(beta, best)
                if beta <= alpha:
                    break
            return best

    def get_best_move(self, board, is_maximizing):
        best_move = None
        best_value = -float('inf') if is_maximizing else float('inf')
        for move in self.get_possible_moves(board):
            new_board = self.make_move(board, move, self.max_player if is_maximizing else self.min_player)
            board_value = self.alpha_beta(new_board, 0, not is_maximizing, -float('inf'), float('inf'))
            if (is_maximizing and board_value > best_value) or (not is_maximizing and board_value < best_value):
                best_value = board_value
                best_move = move
        return best_move

    def get_possible_moves(self, board):
        moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    moves.append((row, col))
        return moves

    def make_move(self, board, move, player):
        new_board = [row[:] for row in board]
        new_board[move[0]][move[1]] = player
        return new_board

    def check_winner(self, board):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return board[0][2]
        return None

    def print_board(self, board):
        for row in board:
            print(" | ".join(row))
            print("-" * 5)


# ------------------------- Playable Game -------------------------
if __name__ == "__main__":
    game = MinMaxAlphaBeta()
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        game.print_board(board)
        winner = game.check_winner(board)
        if winner:
            print(f"\nGame Over! Winner is: {winner}")
            break
        elif not any(cell == ' ' for row in board for cell in row):
            print("\nGame Over! It's a draw.")
            break

        # Human player's move (O)
        try:
            row = int(input("Enter your move row (0-2): "))
            col = int(input("Enter your move col (0-2): "))
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
            board[row][col] = 'O'
        except:
            print("Invalid input. Try again.")
            continue

        # Check after human move
        winner = game.check_winner(board)
        if winner:
            game.print_board(board)
            print(f"\nGame Over! Winner is: {winner}")
            break
        elif not any(cell == ' ' for row in board for cell in row):
            game.print_board(board)
            print("\nGame Over! It's a draw.")
            break

        # AI move
        print("\nAI is thinking...")
        ai_move = game.get_best_move(board, is_maximizing=True)
        if ai_move:
            board = game.make_move(board, ai_move, 'X')
