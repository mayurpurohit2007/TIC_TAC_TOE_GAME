import random

# Create the game board
board = [" " for _ in range(9)]

# print_board() is the function to print the board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to the check winner
def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# check_draw() is the function to check the match is draw
def check_draw():
    return " " not in board

# User move
def user_move():
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move. Try again.")

# Computer move using random
def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"
    print("Computer chose position", move + 1)

# Main game loop
print("Welcome to Tic-Tac-Toe")
print("You are X, Computer is O")

while True:
    print_board()
    user_move()

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        print_board()
        print("Computer wins!")
        break
