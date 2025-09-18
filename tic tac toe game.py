def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, mark):
    return any(all(cell == mark for cell in row) for row in board) or \
           any(all(row[i] == mark for row in board) for i in range(3)) or \
           all(board[i][i] == mark for i in range(3)) or \
           all(board[i][2-i] == mark for i in range(3))

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    moves = 0

    while moves < 9:
        print_board(board)
        p = players[moves % 2]
        r, c = map(int, input(f"Player {p}, enter row and col (0-2): ").split())
        if board[r][c] == " ":
            board[r][c] = p
            moves += 1
            if check_winner(board, p):
                print_board(board)
                print(f"Player {p} wins!")
                return
        else:
            print("Cell already taken!")
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
