# 🎲 Tic Tac Toe Game (Python)

Author : M.S.MEYSINTHA

A Python-based Tic Tac Toe game where two players can play against each other on the same computer.
This project is simple yet fun and demonstrates basic Python programming, game logic, and loops.

# 📌 Features

✅ Two-player game (Player X and Player O)
✅ 3x3 game board displayed in the console
✅ Players take turns to place their marks
✅ Checks for win conditions (rows, columns, diagonals)
✅ Declares a draw if the board is full and no one wins
✅ Beginner-friendly project

# 📜 Code Example
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

board = [[" "]*3 for _ in range(3)]
current_player = "X"

while True:
    print_board(board)
    row = int(input(f"Player {current_player}, enter row (0-2): "))
    col = int(input(f"Player {current_player}, enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell already taken. Try again.")

# ▶️ Example Run
   |   |  
---------
   |   |  
---------
   |   |  

Player X, enter row (0-2): 0
Player X, enter column (0-2): 1

   | X |  
---------
   |   |  
---------
   |   |  

# ⚡ How to Run

Clone this repository:

git clone https://github.com/meysiii/TIC-TAC-TOE-GAME
cd tic-tac-toe


# Run the program:

python tictactoe.py

# output

<img width="1920" height="1030" alt="Image" src="https://github.com/user-attachments/assets/bc7c385c-1938-4e9e-b3a2-63df4799a27e" />

# 🚀 Future Improvements

Add AI opponent using Minimax algorithm 🤖

Create a GUI version using Tkinter or Pygame

Add scoreboard tracking across multiple rounds

Support network multiplayer
