import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if there are any available moves left on the board
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # No winner yet
    return 0

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If the AI wins, return the evaluated score
    if score == 10:
        return score

    # If the player wins, return the evaluated score
    if score == -10:
        return score

    # If no moves are left, it's a draw
    if not is_moves_left(board):
        return 0

    # If the current player is the AI (X), maximize the score
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best_score

    # If the current player is the human (O), minimize the score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_move = (-1, -1)
    best_score = -math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_score = minimax(board, 0, False)
                board[i][j] = ' '

                if move_score > best_score:
                    best_move = (i, j)
                    best_score = move_score

    return best_move

# Function to check if the game has ended
def is_game_over(board):
    return evaluate(board) != 0 or not is_moves_left(board)

# Main game loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Human player's move (O)
        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Invalid move. Try again.")

        print_board(board)

        if is_game_over(board):
            break

        # AI player's move (X)
        print("AI's turn:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if is_game_over(board):
            break

    # Check for a winner or if it's a draw
    result = evaluate(board)
    if result == 10:
        print("AI wins!")
    elif result == -10:
        print("You win!")
    else:
        print("It's a draw!")

# Run the game
play_game()
