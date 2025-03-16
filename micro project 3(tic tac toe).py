import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def reset_game():
    global board, current_player
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"

def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=tk.DISABLED)
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
            return
        if all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return
        current_player = "O" if current_player == "X" else "X"

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
