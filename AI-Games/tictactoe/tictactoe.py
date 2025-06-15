import math

# --- Board & display ---
# Initialize the game board with 9 empty spaces
board = [' ']*9  # 0–8 positions

# Function to display the current state of the board
def show():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# --- Game logic ---
# Function to check for a winner or a tie
def winner(b):
    # Define all possible winning combinations
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    # Check if any winning combination is satisfied
    for x,y,z in wins:
        if b[x]==b[y]==b[z] and b[x] != ' ':
            return b[x]
    # Return 'Tie' if the board is full and no winner is found
    return 'Tie' if ' ' not in b else None

# --- Minimax ---
# Recursive minimax function to evaluate the best move
def minimax(is_ai):
    # Check if the game has ended and return the score
    win = winner(board)
    if win=='O': return 1      # AI win
    if win=='X': return -1     # Human win
    if win=='Tie': return 0    # Draw

    # Initialize best score based on the current player
    best = -math.inf if is_ai else math.inf
    mark = 'O' if is_ai else 'X'

    # Iterate through all possible moves
    for i in range(9):
        if board[i]==' ':
            # Make the move
            board[i] = mark
            # Recursively evaluate the move
            score = minimax(not is_ai)
            # Undo the move
            board[i] = ' '
            # Update the best score
            if is_ai:
                best = max(score, best)  # Maximize for AI
            else:
                best = min(score, best)  # Minimize for human
    return best

# Function to determine the AI's best move
def ai_move():
    best_score, move = -math.inf, None
    # Iterate through all possible moves
    for i in range(9):
        if board[i]==' ':
            # Make the move
            board[i] = 'O'
            # Evaluate the move using minimax
            score = minimax(False)
            # Undo the move
            board[i] = ' '
            # Update the best move if the score is better
            if score > best_score:
                best_score, move = score, i
    # Make the best move
    board[move] = 'O'

# --- Main loop ---
# Initialize the turn (X = human, O = AI)
turn = 'X'  # X = human, O = AI
while True:
    # Display the current state of the board
    show()
    # Check for a winner or a tie
    result = winner(board)
    if result:
        # Print the result and exit the loop
        print(
            "Result:",
            "Draw" if result == 'Tie'
            else ("AI wins!" if result == 'O' else "Human wins!")
        )
        break

    # Handle the human player's turn
    if turn=='X':
        try:
            # Get the human player's move
            move = int(input("Your move (1–9): ")) - 1
            # Check if the chosen spot is valid
            if board[move] != ' ':
                print("Spot taken!")
                continue
            # Make the move
            board[move] = 'X'
        except:
            # Handle invalid input
            print("Invalid input.")
            continue
    else:
        # Handle the AI's turn
        print("AI thinking...")
        ai_move()

    # Switch turns
    turn = 'O' if turn=='X' else 'X'
