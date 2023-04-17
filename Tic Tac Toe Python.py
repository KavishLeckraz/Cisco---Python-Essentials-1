import random

def display_board(board):
    """
    Displays the current state of the board.
    """
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1]}   |   {board[2]}   |   {board[3]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[4]}   |   {board[5]}   |   {board[6]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[7]}   |   {board[8]}   |   {board[9]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def player_move(board):
    """
    Asks the player to make a move and returns the updated board.
    """
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)] == " ":
            board[int(move)] = "O"
            return board
        else:
            print("Invalid move. Please try again.")

def computer_move(board):
    """
    Generates a random move for the computer and returns the updated board.
    """
    while True:
        move = random.randint(1, 9)
        if board[move] == " ":
            board[move] = "X"
            return board

def check_win(board):
    """
    Checks if the game is over and returns one of four possible verdicts:
    "continue", "tie", "player wins", or "computer wins".
    """
    for a, b, c in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]:
        if board[a] == board[b] == board[c] == "X":
            return "computer wins"
        elif board[a] == board[b] == board[c] == "O":
            return "player wins"
    if " " not in board:
        return "tie"
    return "continue"

def main():
    """
    Runs the main game loop.
    """
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    board[5] = "X"
    display_board(board)
    while True:
        board = player_move(board)
        display_board(board)
        verdict = check_win(board)
        if verdict != "continue":
            print(verdict)
            break
        board = computer_move(board)
        display_board(board)
        verdict = check_win(board)
        if verdict != "continue":
            print(verdict)
            break

if __name__ == "__main__":
    main()



