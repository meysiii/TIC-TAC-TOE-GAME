def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, mark):
    return (
        any(all(cell == mark for cell in row) for row in board) or
        any(all(row[i] == mark for row in board) for i in range(3)) or
        all(board[i][i] == mark for i in range(3)) or
        all(board[i][2-i] == mark for i in range(3))
    )


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn")

        # Ask row and column separately (fix)
        r = int(input("Enter row (0-2): "))
        c = int(input("Enter column (0-2): "))

        if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == " ":
            board[r][c] = player
            if check_winner(board, player):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw! 🤝")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move! Try again.")


# Run game
tic_tac_toe()

